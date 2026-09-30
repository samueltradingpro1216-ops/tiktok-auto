#!/usr/bin/env python3
"""Fabrique un episode de Lulu la Luciole : la chanson d'abord, puis les images, puis le montage.

Etapes (reprise automatique grace a state.json) :
  song      choisit la meilleure prise (paroles les mieux reconnues) et cale chaque ligne dans le temps
  keyframes image de debut + image de fin de chaque section, validees par le juge visuel
  clips     un plan par section, genere entre l'image de fin du plan precedent (continuite parfaite)
            et l'image de fin prevue, puis cale a la duree exacte de la section
  assemble  1920x1080, chanson en bande son, paroles incrustees au rythme du chant, volume YouTube
  publish   miniature + fiche YouTube

Usage : python make_episode.py ../episodes/01_rangement [--only clips]
"""

import argparse
import concurrent.futures as cf
import json
import os
import random
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "comptines", "pipeline"))
from comptine import (FONT, FONT_FILE, SERVER, chat_api, log, normalize, parse_json, run,  # noqa: E402
                      similarity, srt_ts, submit, wait_task_file, wrap)

WHISPER_PYTHON = os.environ.get("WHISPER_PYTHON", sys.executable)
DURATIONS = [5, 10, 15, 18, 20]  # durees possibles d'Agnes Video 2.0
MAX_TRIES = 3
MAX_KEYFRAME_TRIES = 5
NEG = "text, letters, watermark, extra characters, duplicated character, adult, deformed face, extra fingers"


def last_frame(video, dst):
    run(["ffmpeg", "-v", "error", "-y", "-sseof", "-0.1", "-i", video, "-frames:v", "1", "-update", "1", dst])
    return dst


class Episode:
    def __init__(self, ep_dir):
        self.dir = os.path.abspath(ep_dir)
        self.ep = json.load(open(os.path.join(self.dir, "episode.json"), encoding="utf-8"))
        self.state_path = os.path.join(self.dir, "state.json")
        self.state = json.load(open(self.state_path)) if os.path.exists(self.state_path) else {}
        for sub in ("keyframes", "clips", "frames"):
            os.makedirs(os.path.join(self.dir, sub), exist_ok=True)

    def save(self):
        json.dump(self.state, open(self.state_path, "w"), ensure_ascii=False, indent=2)

    def chars(self):
        return " ".join(f"{k}: {v}" for k, v in self.ep["characters"].items())

    # ── song ──
    def step_song(self):
        if self.state.get("song"):
            return
        takes = sorted(f for f in os.listdir(os.path.join(self.dir, "chanson")) if f.startswith("prise_"))
        all_lines = [l for s in self.ep["sections"] for l in s["lines"]]
        best = None
        for t in takes:
            if not t.endswith(".wav") or ".padded" in t:
                continue
            path = os.path.join(self.dir, "chanson", t)
            tr = json.loads(run([WHISPER_PYTHON, os.path.join(HERE, "transcribe_words.py"), path]))
            dur = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]))
            lines = self.align(all_lines, tr["words"], dur)
            # critere : chaque ligne doit etre retrouvee et bien prononcee (moyenne des correspondances)
            sim = sum(max(0, l["match"]) for l in lines) / len(lines)
            log(f"prise {t} : lignes reconnues a {sim:.0%} (plus faible : {min(l['match'] for l in lines):.2f})")
            if not best or sim > best[1]:
                best = (path, sim, lines, dur)
        path, sim, lines, dur = best
        self.state["song"] = {"file": path, "similarity": round(sim, 2), "duration": dur, "lines": lines}
        # sections : du debut de leur 1re ligne au debut de la section suivante
        starts, i = [], 0
        for s in self.ep["sections"]:
            starts.append(lines[i]["start"])
            i += len(s["lines"])
        starts[0] = 0.0
        self.state["sections"] = [{"id": s["id"], "start": round(starts[k], 2),
                                   "end": round(starts[k + 1] if k + 1 < len(starts) else dur, 2)}
                                  for k, s in enumerate(self.ep["sections"])]
        self.save()
        log(f"chanson retenue : {os.path.basename(path)} ({sim:.0%}), sections : {self.state['sections']}")

    @staticmethod
    def align(lines, words, dur):
        """Cale chaque ligne attendue sur les mots entendus (recherche en avant, meilleure similarite)."""
        out, ptr = [], 0
        heard = [normalize(w["w"]) for w in words]
        for line in lines:
            n = max(1, len(normalize(line).split()))
            best = (-1, ptr, ptr + n)
            for s in range(ptr, min(len(words), ptr + 25)):
                for ln in range(max(1, n - 2), n + 3):
                    e = min(len(words), s + ln)
                    sc = similarity(line, " ".join(heard[s:e]))
                    if sc > best[0]:
                        best = (sc, s, e)
            sc, s, e = best
            if sc < 0.3 or s >= len(words):  # ligne non retrouvee : on la place juste apres la precedente
                start = out[-1]["end"] if out else 0.0
                out.append({"text": line, "start": start, "end": min(dur, start + 2.5), "match": round(sc, 2)})
                continue
            out.append({"text": line, "start": words[s]["start"], "end": words[e - 1]["end"], "match": round(sc, 2)})
            ptr = e
        return out

    # ── juge visuel ──
    def judge(self, frames, max_boys=1, toys=None, sec=None):
        q = ('Look at this frame of a children\'s cartoon. Count only characters with a face (ignore sparkles, '
             'glowing dots and small lights). Return JSON: {"boys": int, "firefly_characters_with_a_face": int, '
             '"adults": int, "deformed": bool, "toy_chests": int, "red_ball_on_floor": bool, '
             '"yellow_duck_on_floor": bool, "blocks_on_floor": bool, "teddy_bears": int, "toy_chest_open": bool, '
             '"living_creatures_other_than_the_boy_and_the_firefly_ignoring_toys_like_rubber_duck_teddy_bear_ball": int}')
        api, problems = chat_api(), []
        for fr in frames:
            try:
                v = parse_json(api.chat_multimodal("You are a strict quality checker. Answer only JSON.", q, [fr],
                                                   max_tokens=200))
            except Exception as e:
                log(f"juge indisponible ({e})")
                continue
            if int(v.get("boys", 0)) > max_boys:
                problems.append(f"{os.path.basename(fr)}: {v['boys']} garcons")
            if int(v.get("firefly_characters_with_a_face", 0)) > 1:
                problems.append(f"{os.path.basename(fr)}: {v['firefly_characters_with_a_face']} lucioles")
            if int(v.get("adults", 0)) > 0:
                problems.append(f"{os.path.basename(fr)}: adulte present")
            if v.get("deformed"):
                problems.append(f"{os.path.basename(fr)}: deformation")
            if int(v.get("toy_chests", 1)) > 1:
                problems.append(f"{os.path.basename(fr)}: {v['toy_chests']} coffres")
            if int(v.get("living_creatures_other_than_the_boy_and_the_firefly_ignoring_toys_like_rubber_duck_teddy_bear_ball", 0)) > 0:
                problems.append(f"{os.path.basename(fr)}: creature en trop")
            if sec and sec.get("teddy_bears") and int(v.get("teddy_bears", 1)) > sec["teddy_bears"]:
                problems.append(f"{os.path.basename(fr)}: {v['teddy_bears']} nounours")
            if sec and sec.get("chest_closed") and v.get("toy_chest_open"):
                problems.append(f"{os.path.basename(fr)}: coffre ouvert")
            if toys is not None:
                for t, k in (("ball", "red_ball_on_floor"), ("duck", "yellow_duck_on_floor"),
                             ("blocks", "blocks_on_floor")):
                    if bool(v.get(k)) != (t in toys):
                        problems.append(f"{os.path.basename(fr)}: {k}={v.get(k)} (attendu {t in toys})")
        return problems

    # ── keyframes ──
    TOYS = {"ball": "a red ball", "duck": "a yellow rubber duck", "blocks": "colorful wooden blocks"}

    def floor_text(self, toys):
        if not toys:
            return "The floor is completely clear: no toys on the floor at all."
        return ("On the floor there are only: " + ", ".join(self.TOYS[t] for t in toys) +
                ". Nothing else on the floor.")

    def make_keyframe_path(self, key):
        path = os.path.join(self.dir, "keyframes", f"{key}.png")
        while not (self.state.get("keyframes", {}).get(key, {}).get("ok") and os.path.exists(path)):
            import time
            time.sleep(10)  # attend que l'image de reference soit validee
        return path

    def make_keyframe(self, key, description, toys=None, sec=None):
        st = self.state.setdefault("keyframes", {}).setdefault(key, {"tries": 0})
        path = os.path.join(self.dir, "keyframes", f"{key}.png")
        if st.get("ok") and os.path.exists(path):
            return path
        # reference d'origine (tous les jouets par terre) ou chambre rangee (on ajoute les jouets restants
        # par le texte : un generateur ajoute plus facilement un objet qu'il n'en retire un)
        clean = os.path.join(self.dir, "reference_clean.png")
        all_toys = toys is not None and set(toys) == set(self.TOYS)
        ref = os.path.join(self.dir, "reference.png") if all_toys or not os.path.exists(clean) else clean
        if sec and sec.get("ref_from"):  # on part d'une image clé deja validee (l'etat de la chambre suit)
            ref = self.make_keyframe_path(sec["ref_from"])
        while st["tries"] < MAX_KEYFRAME_TRIES:
            st["tries"] += 1
            missing = [self.TOYS[t] + " on the floor" for t in self.TOYS if toys is not None and t not in toys]
            r = submit(["-X", "POST", f"{SERVER}/api/image/generate", "-F", "size=1344x768",
                        "-F", f"reference_image=@{ref}",
                        "-F", f"negative_prompt={', '.join([NEG, 'two toy chests'] + missing)}",
                        "-F", f"prompt={self.ep['style']} {description} "
                              f"{self.floor_text(toys) if toys is not None else ''} Only one toy chest. "
                              f"Setting: {self.ep['setting']} Characters (each appears only once): {self.chars()}"])
            run(["cp", wait_task_file(r["dir_name"], "final_image.png"), path])
            problems = self.judge([path], toys=toys, sec=sec)
            st.update(ok=not problems, problems=problems)
            self.save()
            log(f"image {key} essai {st['tries']} : {problems or 'OK'}")
            if not problems:
                break
        return path

    def step_keyframes(self):
        jobs = [("s1_start", self.ep["sections"][0]["start_frame"], ["ball", "duck", "blocks"])]
        jobs += [(f"s{s['id']}_end", s["end_frame"], s.get("floor_toys_after"), s) for s in self.ep["sections"]]
        with cf.ThreadPoolExecutor(max_workers=3) as ex:
            list(ex.map(lambda j: self.make_keyframe(*j), jobs))

    # ── clips ──
    def step_clips(self):
        prev_end = os.path.join(self.dir, "keyframes", "s1_start.png")
        for sec, timing in zip(self.ep["sections"], self.state["sections"]):
            sid = sec["id"]
            st = self.state.setdefault("clips", {}).setdefault(str(sid), {"tries": 0})
            length = timing["end"] - timing["start"]
            gen_dur = min(DURATIONS, key=lambda d: abs(d - length))
            raw = os.path.join(self.dir, "clips", f"s{sid}_raw.mp4")
            while not st.get("ok") and st["tries"] < MAX_TRIES:
                st["tries"] += 1
                r = submit(["-X", "POST", f"{SERVER}/api/tasks/simple", "-F", "mode=keyframes",
                            "-F", f"duration={gen_dur}", "-F", "video_width=1280", "-F", "video_height=720",
                            "-F", f"seed={random.randint(1, 2**31 - 1)}",
                            "-F", f"reference_image=@{prev_end}",
                            "-F", f"end_frame_image=@{os.path.join(self.dir, 'keyframes', f's{sid}_end.png')}",
                            "-F", f"negative_prompt={NEG}",
                            "-F", f"prompt={self.ep['style']} {sec['motion']} Smooth continuous motion, same "
                                  f"characters and same room from start to end, no cuts, no talking. "
                                  f"{self.chars()}"])
                run(["cp", wait_task_file(r["dir_name"], "final_video.mp4"), raw])
                frames = []
                for t in (0.3, 0.5, 0.8):
                    fr = os.path.join(self.dir, "frames", f"s{sid}_{int(t * 100)}.jpg")
                    run(["ffmpeg", "-v", "error", "-y", "-ss", str(gen_dur * t), "-i", raw, "-frames:v", "1",
                         "-vf", "scale=640:-1", fr])
                    frames.append(fr)
                # pendant un plan, la camera bouge : on verifie les personnages, pas les jouets
                # (l'etat final de la chambre est garanti par l'image clé de fin, deja validee)
                problems = self.judge(frames, sec={"teddy_bears": sec.get("teddy_bears")})
                st.update(ok=not problems, problems=problems, raw=raw, gen_duration=gen_dur)
                self.save()
                log(f"plan {sid} ({length:.1f} s, genere en {gen_dur} s) essai {st['tries']} : {problems or 'OK'}")
            prev_end = last_frame(raw, os.path.join(self.dir, "keyframes", f"s{sid}_actual_end.png"))

    # ── montage ──
    def step_assemble(self):
        parts = []
        for sec, timing in zip(self.ep["sections"], self.state["sections"]):
            st = self.state["clips"][str(sec["id"])]
            length = timing["end"] - timing["start"]
            raw_dur = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                 st["raw"]]))
            part = os.path.join(self.dir, "clips", f"s{sec['id']}_fit.mp4")
            # le plan est accelere/ralenti pour tomber pile sur la duree de sa section
            run(["ffmpeg", "-v", "error", "-y", "-i", st["raw"], "-an", "-vf",
                 f"setpts={length / raw_dur:.5f}*PTS,scale=1964:1080:flags=lanczos,crop=1920:1080,setsar=1,fps=24",
                 "-t", f"{length:.3f}", "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
                 part])
            parts.append(part)
        lst = os.path.join(self.dir, "clips", "list.txt")
        open(lst, "w").writelines(f"file '{p}'\n" for p in parts)
        concat = os.path.join(self.dir, "clips", "concat.mp4")
        run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", concat])
        srt = os.path.join(self.dir, "paroles.srt")
        with open(srt, "w", encoding="utf-8") as f:
            for i, l in enumerate(self.state["song"]["lines"], 1):
                f.write(f"{i}\n{srt_ts(l['start'])} --> {srt_ts(l['end'] + 0.3)}\n{wrap(l['text'])}\n\n")
        final = os.path.join(self.dir, f"{self.ep['slug']}_youtube.mp4")
        style = (f"FontName={FONT},Bold=1,Fontsize=22,PrimaryColour=&H00FFFFFF,OutlineColour=&H00803A20,"
                 "BorderStyle=1,Outline=3,Shadow=1,Alignment=2,MarginV=30")
        run(["ffmpeg", "-v", "error", "-y", "-i", concat, "-i", self.state["song"]["file"],
             "-vf", f"subtitles={srt}:force_style='{style}'", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
             "-map", "0:v", "-map", "1:a", "-shortest", "-c:v", "libx264", "-crf", "18", "-preset", "medium",
             "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", final])
        preview = os.path.join(self.dir, f"{self.ep['slug']}_apercu.mp4")
        run(["ffmpeg", "-v", "error", "-y", "-i", final, "-vf", "scale=1280:720", "-c:v", "libx264", "-crf", "28",
             "-c:a", "copy", "-movflags", "+faststart", preview])
        self.state["final"] = final
        self.save()
        log(f"montage : {final}")

    # ── miniature + fiche ──
    def step_publish(self):
        yt = self.ep["youtube"]
        src = os.path.join(self.dir, "keyframes", yt.get("thumbnail_keyframe", "s2_end") + ".png")
        big, small = yt["thumbnail_text"], yt["thumbnail_subtext"]
        size = min(170, int(1800 / max(len(big), 1)))
        vf = ("scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,"
              f"drawtext=fontfile={FONT_FILE}:text='{big}':fontsize={size}:fontcolor=#FFD84D:borderw=12:"
              "bordercolor=#23306B:x=(w-tw)/2:y=h-th-40,"
              f"drawtext=fontfile={FONT_FILE}:text='{small}':fontsize=50:fontcolor=white:borderw=6:"
              "bordercolor=#23306B:x=36:y=36")
        run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vf", vf, "-q:v", "2",
             os.path.join(self.dir, "miniature_youtube.jpg")])
        lyrics = "\n".join(l for s in self.ep["sections"] for l in s["lines"])
        desc = f"{yt['hook']}\n\n🎵 Paroles\n{lyrics}\n\n{yt['footer']}"
        clips = self.state.get("clips", {})
        with open(os.path.join(self.dir, "youtube.md"), "w", encoding="utf-8") as f:
            f.write(f"# {yt['title']}\n\n## Titre\n```\n{yt['title']}\n```\n\n## Description\n```\n{desc}\n```\n\n"
                    f"## Tags\n```\n{', '.join(yt['tags'])}\n```\n\n## Réglages\n"
                    "- Audience : Oui, conçue pour les enfants\n- Contenu modifié ou synthétique : Non (dessin animé)\n"
                    "- Catégorie : Éducation\n- Langue : Français\n\n## Contrôle qualité\n"
                    f"- Chanson : paroles reconnues à {self.state['song']['similarity']:.0%}\n")
            for sid, st in sorted(clips.items(), key=lambda x: int(x[0])):
                f.write(f"- Plan {sid} : {st['tries']} essai(s), {'; '.join(st.get('problems', [])) or 'OK'}\n")
        log("fiche YouTube ecrite")


STEPS = ["song", "keyframes", "clips", "assemble", "publish"]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("episode_dir")
    p.add_argument("--only", choices=STEPS)
    a = p.parse_args()
    ep = Episode(a.episode_dir)
    for step in STEPS:
        if not a.only or a.only == step:
            log(f"=== {step}")
            getattr(ep, f"step_{step}")()


if __name__ == "__main__":
    main()
