#!/usr/bin/env python3
"""Fabrique un episode de Lulu la Luciole : la chanson d'abord, puis les images, puis le montage.

Etapes (reprise automatique grace a state.json) :
  song      choisit la meilleure prise (paroles les mieux reconnues) et cale chaque ligne dans le temps
  reference image de reference de l'episode (personnages + chambre), si elle n'existe pas encore
  keyframes image de debut + image de fin de chaque section, validees par le juge visuel
  clips     un plan par section, genere entre l'image de fin du plan precedent (continuite parfaite)
            et l'image de fin prevue, puis cale a la duree exacte de la section
  assemble  1920x1080, chanson en bande son, paroles incrustees au rythme du chant, volume YouTube
  patch     (avec --redo) remplace seulement les plans refaits dans la video deja montee
  publish   miniature + fiche YouTube

Usage :
  python make_episode.py ../episodes/02_peur_du_noir [--only clips]
  python make_episode.py ../episodes/01_rangement --redo 4,7   # refait les plans 4 et 7 et repare la video
"""

import argparse
import concurrent.futures as cf
import json
import math
import os
import random
import re
import shutil
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "comptines", "pipeline"))
from comptine import (FONT, FONT_FILE, SERVER, chat_api, log, normalize, parse_json, run,  # noqa: E402
                      similarity, srt_ts, submit, wait_task_file, wrap)

WHISPER_PYTHON = os.environ.get("WHISPER_PYTHON", sys.executable)
LULU_REFERENCE = os.path.join(HERE, "..", "identite", "lulu_reference.png")
DURATIONS = [5, 10, 15, 18, 20]  # durees possibles d'Agnes Video 2.0
FPS = 24
MAX_TRIES = 3
MAX_KEYFRAME_TRIES = 5
SAMPLE_POINTS = (0.15, 0.3, 0.5, 0.7, 0.85)  # images controlees dans chaque plan
NEG = ("text, letters, watermark, extra characters, duplicated character, adult, deformed face, extra fingers, "
       "boy with wings, boy with antennae, toy with wings, toy with antennae, merged characters")
SUB_STYLE = (f"FontName={FONT},Bold=1,Fontsize=22,PrimaryColour=&H00FFFFFF,OutlineColour=&H00803A20,"
             "BorderStyle=1,Outline=3,Shadow=1,Alignment=2,MarginV=30")
# le generateur video fusionne parfois deux elements : Nino avec des ailes de luciole, un nounours avec
# les antennes de Lulu (episode 01, plans 4 et 7). Le juge pose donc la question explicitement.
HYBRID_BOY = "boy_has_insect_wings_or_antennae_growing_from_his_own_body"
HYBRID_TOY = "teddy_bear_toy_or_object_with_its_own_insect_wings_or_antennae"
LULU_SEEN = "is_the_firefly_in_the_picture"
# ep. 03 : petites ailes blanches dans le dos de Nino, Lulu a l'autre bout de l'image ; la question generale
# (HYBRID_BOY) ne les voit pas, une question a part sur le dos les trouve (5 sur 5, aucune fausse alerte sur 10)
WING_BACK = "a_wing_shape_attached_to_the_boys_back_or_shoulders"
WING_Q = ("Look at this frame of a children's cartoon. Look closely at the boy's back and shoulders. Sometimes "
          "a small white or translucent wing sticks out from the boy's back, as if he were a fairy: that is a "
          "defect, even if the firefly is somewhere else in the picture. The firefly's own wings are attached to "
          "the firefly's round body, not to the boy. Return JSON: {\"boys\": int, \"" + WING_BACK + "\": bool, "
          "\"where_is_the_firefly\": str}")
TEDDIES = "plush_teddy_bears_not_counting_the_firefly"
OTHERS = "living_creatures_other_than_the_boy_and_the_firefly_ignoring_toys_and_shadows"


def last_frame(video, dst):
    run(["ffmpeg", "-v", "error", "-y", "-sseof", "-0.1", "-i", video, "-frames:v", "1", "-update", "1", dst])
    return dst


def duration(path):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]))


def fit_filter(length, raw_dur, frames):
    """Accelere/ralentit un plan pour qu'il dure exactement `frames` images de la section, en 1920x1080."""
    return (f"setpts={length / raw_dur:.5f}*PTS,scale=1964:1080:flags=lanczos,crop=1920:1080,setsar=1,fps={FPS},"
            f"tpad=stop_mode=clone:stop_duration=0.5,trim=end_frame={frames},setpts=PTS-STARTPTS")


def floor_key(desc):
    """'a red ball' -> 'red_ball_on_floor' (nom de champ lisible pour le juge)."""
    words = [w for w in re.sub(r"[^a-z ]", " ", desc.lower()).split() if w not in ("a", "an", "the", "some")]
    return "_".join(words) + "_on_floor"


class Episode:
    def __init__(self, ep_dir):
        self.dir = os.path.abspath(ep_dir)
        self.ep = json.load(open(os.path.join(self.dir, "episode.json"), encoding="utf-8"))
        self.state_path = os.path.join(self.dir, "state.json")
        self.state = json.load(open(self.state_path)) if os.path.exists(self.state_path) else {}
        # objets suivis par terre (episode 01 : jouets a ranger) ; regles et interdits propres a l'episode
        self.toys = self.ep.get("floor_toys", {})
        self.rules = self.ep.get("rules", "")
        self.neg = ", ".join(x for x in (NEG, self.ep.get("negative", "")) if x)
        self.redo = set()
        for sub in ("keyframes", "clips", "frames"):
            os.makedirs(os.path.join(self.dir, sub), exist_ok=True)

    def save(self):
        json.dump(self.state, open(self.state_path, "w"), ensure_ascii=False, indent=2)

    def chars(self):
        return " ".join(f"{k}: {v}" for k, v in self.ep["characters"].items())

    def final_path(self):
        return os.path.join(self.dir, f"{self.ep['slug']}_youtube.mp4")

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
            dur = duration(path)
            lines = self.align(all_lines, tr["words"], dur)
            # critere : chaque ligne doit etre retrouvee et bien prononcee (moyenne des correspondances)
            sim = self.song_score(lines)
            missed = [l["text"] for l in lines if not l["sung"]]
            log(f"prise {t} : lignes reconnues a {sim:.0%} (plus faible : {min(l['match'] for l in lines):.2f})"
                + (f", non chantees : {missed}" if missed else ""))
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
    def song_score(lines):
        return sum(max(0, l["match"]) for l in lines) / len(lines)

    @staticmethod
    def align(lines, words, dur, min_match=0.4, max_gap=40):
        """Cale les lignes attendues sur les mots entendus : alignement global, dans l'ordre.

        Le modele musical saute parfois une ligne : elle est alors marquee non chantee ("sung": false) et
        placee entre ses voisines, sans decaler les suivantes (une recherche ligne par ligne derapait
        jusqu'a la fin de la chanson)."""
        heard = [normalize(w["w"]) for w in words]
        nw = len(words)
        cands = []  # pour chaque ligne : {debut: (fin, score)} des meilleurs passages entendus
        for line in lines:
            n, c = max(1, len(normalize(line).split())), {}
            for st in range(nw):
                for ln in range(max(1, n // 2), n + 3):  # whisper perd souvent des mots : passages courts admis
                    e = min(nw, st + ln)
                    sc = similarity(line, " ".join(heard[st:e]))
                    if sc >= min_match and sc > c.get(st, (0, 0))[1]:
                        c[st] = (e, sc)
            cands.append(c)
        # programmation dynamique : position dans les mots -> (score, chemin)
        states = {0: (0.0, ())}
        for c in cands:
            nxt = {}
            for j, (score, path) in states.items():
                if score > nxt.get(j, (-1,))[0]:
                    nxt[j] = (score, path + (None,))  # ligne non chantee
                for st in range(j, min(nw, j + max_gap + 1)):
                    if st in c:
                        e, sc = c[st]
                        gain = score + sc - min_match / 2
                        if gain > nxt.get(e, (-1,))[0]:
                            nxt[e] = (gain, path + ((st, e, sc),))
            states = nxt
        path = max(states.values(), key=lambda v: v[0])[1]
        out = []
        for line, m in zip(lines, path):
            if m:
                st, e, sc = m
                out.append({"text": line, "start": words[st]["start"], "end": words[e - 1]["end"],
                            "match": round(sc, 2), "sung": True})
            else:
                out.append({"text": line, "start": None, "end": None, "match": 0.0, "sung": False})
        # lignes non chantees : reparties entre la ligne chantee d'avant et celle d'apres
        i = 0
        while i < len(out):
            if out[i]["sung"]:
                i += 1
                continue
            k = i
            while k < len(out) and not out[k]["sung"]:
                k += 1
            a = out[i - 1]["end"] if i else 0.0
            b = out[k]["start"] if k < len(out) else min(dur, a + 2.5 * (k - i))
            step = max(0.0, b - a) / (k - i)
            for m in range(i, k):
                out[m]["start"], out[m]["end"] = round(a + step * (m - i), 2), round(a + step * (m - i + 1), 2)
            i = k
        return out

    # ── juge visuel ──
    def judge(self, frames, toys=None, sec=None, need_lulu=False):
        """Liste des problemes trouves sur ces images (vide = OK).

        need_lulu : Lulu doit etre visible ; sur un plan (plusieurs images) on tolere une image sans elle
        (camera qui bouge), au-dela c'est qu'elle a disparu ou fusionne avec un autre element."""
        sec = sec or {}
        fields = {"boys": "int", "firefly_characters_with_a_face": "int", LULU_SEEN: "bool", "adults": "int",
                  "deformed": "bool", HYBRID_BOY: "bool", HYBRID_TOY: "bool", "toy_chests": "int", "toy_chest_open": "bool",
                  TEDDIES: "int", OTHERS: "int"}
        for desc in self.toys.values():
            fields[floor_key(desc)] = "bool"
        q = ("Look at this frame of a children's cartoon. Count only characters with a face (ignore sparkles, "
             "glowing dots, small lights and shadows on the walls). The firefly often flies right next to the boy "
             "or in front of objects: her wings and antennae belong to her, never count them as the boy's or an "
             "object's. Check carefully that the boy has no insect wings or antennae on his own body and that no "
             "toy or object has its own insect wings or antennae. Return JSON: {" +
             ", ".join(f'"{k}": {t}' for k, t in fields.items()) + "}")
        teddies = sec.get("teddy_bears")
        if teddies is None:
            teddies = self.ep.get("teddy_bears")
        api, problems, no_lulu, no_nino = chat_api(), [], [], []
        for fr in frames:
            name = os.path.basename(fr)
            try:
                v = parse_json(api.chat_multimodal("You are a strict quality checker. Answer only JSON.", q, [fr],
                                                   max_tokens=300))
            except Exception as e:
                log(f"juge indisponible ({e})")
                continue
            if int(v.get("boys", 0)) > 1:
                problems.append(f"{name}: {v['boys']} garcons")
            if int(v.get("boys", 1)) == 0:
                no_nino.append(name)
            if int(v.get("firefly_characters_with_a_face", 0)) > 1:
                problems.append(f"{name}: {v['firefly_characters_with_a_face']} lucioles")
            if v.get(LULU_SEEN) is False or (LULU_SEEN not in v and
                                               int(v.get("firefly_characters_with_a_face", 1)) == 0):
                no_lulu.append(name)  # Lulu vue de dos n'a pas de visage : on demande si elle est visible
            if int(v.get("adults", 0)) > 0:
                problems.append(f"{name}: adulte present")
            if v.get("deformed"):
                problems.append(f"{name}: deformation")
            if v.get(HYBRID_BOY):
                problems.append(f"{name}: Nino a des ailes ou des antennes")
            elif int(v.get("boys", 0)) >= 1:
                try:
                    w = parse_json(api.chat_multimodal("You are a strict quality checker. Answer only JSON.", WING_Q,
                                                       [fr], max_tokens=200))
                    if w.get(WING_BACK):
                        problems.append(f"{name}: aile dans le dos de Nino")
                except Exception as e:
                    log(f"juge indisponible ({e})")
            if v.get(HYBRID_TOY):
                problems.append(f"{name}: un jouet ou un objet a des ailes ou des antennes")
            if int(v.get("toy_chests", 1)) > 1:
                problems.append(f"{name}: {v['toy_chests']} coffres")
            if int(v.get(OTHERS, 0)) > 0:
                problems.append(f"{name}: creature en trop")
            if teddies is not None and int(v.get(TEDDIES, 0)) > teddies:
                problems.append(f"{name}: {v[TEDDIES]} nounours")
            if sec.get("chest_closed") and v.get("toy_chest_open"):
                problems.append(f"{name}: coffre ouvert")
            if toys is not None:
                for t, desc in self.toys.items():
                    k = floor_key(desc)
                    if bool(v.get(k)) != (t in toys):
                        problems.append(f"{name}: {k}={v.get(k)} (attendu {t in toys})")
        if need_lulu and len(no_lulu) >= (1 if len(frames) == 1 else 2):
            problems.append(f"Lulu absente : {', '.join(no_lulu)}")
        # Nino est dans toutes les images (ep. 03 : Lulu geante avait pris sa place sur l'image de reference)
        if len(no_nino) >= (1 if len(frames) == 1 else 2):
            problems.append(f"Nino absent : {', '.join(no_nino)}")
        return problems

    # ── image de reference ──
    def step_reference(self):
        path = os.path.join(self.dir, "reference.png")
        if os.path.exists(path):
            return
        spec = self.ep.get("reference", {})
        base = os.path.normpath(os.path.join(self.dir, spec["from"])) if spec.get("from") else LULU_REFERENCE
        st = self.state.setdefault("reference", {"tries": 0})
        candidate = os.path.join(self.dir, "keyframes", "reference_candidate.png")
        while st["tries"] < MAX_KEYFRAME_TRIES:
            st["tries"] += 1
            r = submit(["-X", "POST", f"{SERVER}/api/image/generate", "-F", "size=1344x768",
                        "-F", f"reference_image=@{base}", "-F", f"negative_prompt={self.neg}",
                        "-F", f"prompt={self.ep['style']} {spec.get('description', '')} {self.rules} "
                              f"Setting: {self.ep['setting']} Characters (each appears only once): {self.chars()}"])
            run(["cp", wait_task_file(r["dir_name"], "final_image.png"), candidate])
            problems = self.judge([candidate], need_lulu=True)
            st.update(problems=problems)
            self.save()
            log(f"image de reference essai {st['tries']} : {problems or 'OK'}")
            if not problems:
                break
        if st.get("problems"):
            raise SystemExit(f"image de reference refusee : {st['problems']} (voir {candidate})")
        shutil.move(candidate, path)

    # ── keyframes ──
    def floor_text(self, toys):
        if not toys:
            return "The floor is completely clear: no toys on the floor at all."
        return ("On the floor there are only: " + ", ".join(self.toys[t] for t in toys) +
                ". Nothing else on the floor.")

    def wait_keyframe(self, key):
        """Attend qu'une image clé servant de reference soit terminee (validee ou essais epuises)."""
        path = os.path.join(self.dir, "keyframes", f"{key}.png")
        while not (self.state.get("keyframes", {}).get(key, {}).get("done") and os.path.exists(path)):
            time.sleep(10)
        return path

    def make_keyframe(self, key, description, toys=None, sec=None):
        st = self.state.setdefault("keyframes", {}).setdefault(key, {"tries": 0})
        path = os.path.join(self.dir, "keyframes", f"{key}.png")
        if (st.get("ok") or st.get("done")) and os.path.exists(path):
            st["done"] = True
            return path
        # reference d'origine (tous les jouets par terre) ou chambre rangee (on ajoute les jouets restants
        # par le texte : un generateur ajoute plus facilement un objet qu'il n'en retire un)
        clean = os.path.join(self.dir, "reference_clean.png")
        all_toys = toys is not None and set(toys) == set(self.toys)
        ref = os.path.join(self.dir, "reference.png") if all_toys or not os.path.exists(clean) else clean
        if sec and sec.get("ref_from"):  # on part d'une image clé deja validee (l'etat de la chambre suit)
            ref = self.wait_keyframe(sec["ref_from"])
        elif sec and sec.get("ref_image"):  # ou d'une image d'un autre episode (ex. la chambre de Nino)
            ref = os.path.normpath(os.path.join(self.dir, sec["ref_image"]))
        while st["tries"] < MAX_KEYFRAME_TRIES:
            st["tries"] += 1
            missing = [self.toys[t] + " on the floor" for t in self.toys if toys is not None and t not in toys]
            r = submit(["-X", "POST", f"{SERVER}/api/image/generate", "-F", "size=1344x768",
                        "-F", f"reference_image=@{ref}",
                        "-F", f"negative_prompt={', '.join([self.neg] + missing)}",
                        "-F", f"prompt={self.ep['style']} {description} "
                              f"{self.floor_text(toys) if toys is not None else ''} {self.rules} "
                              f"Setting: {self.ep['setting']} Characters (each appears only once): {self.chars()}"])
            run(["cp", wait_task_file(r["dir_name"], "final_image.png"), path])
            problems = self.judge([path], toys=toys, sec=sec, need_lulu=key != "s1_start")
            st.update(ok=not problems, problems=problems)
            self.save()
            log(f"image {key} essai {st['tries']} : {problems or 'OK'}")
            if not problems:
                break
        st["done"] = True
        self.save()
        return path

    def step_keyframes(self):
        if self.redo:
            return  # reparation : les images clés existent deja
        jobs = [("s1_start", self.ep["sections"][0]["start_frame"], list(self.toys) if self.toys else None)]
        # « cut » : la section commence par une coupe franche, sur sa propre image de debut (changement de piece)
        jobs += [(f"s{s['id']}_start", s["start_frame"], s.get("floor_toys_after"), s)
                 for s in self.ep["sections"][1:] if s.get("cut")]
        jobs += [(f"s{s['id']}_end", s["end_frame"], s.get("floor_toys_after"), s) for s in self.ep["sections"]]
        with cf.ThreadPoolExecutor(max_workers=3) as ex:
            list(ex.map(lambda j: self.make_keyframe(*j), jobs))

    # ── clips ──
    def end_target(self, k, sid):
        """Image de fin visee par le plan `sid`.

        En reparation, si le plan suivant est garde, on vise la derniere image reelle de l'ancien plan :
        le plan suivant part exactement de cette image, la coupe reste invisible."""
        planned = os.path.join(self.dir, "keyframes", f"s{sid}_end.png")
        nxt = self.ep["sections"][k + 1]["id"] if k + 1 < len(self.ep["sections"]) else None
        old_end = os.path.join(self.dir, "keyframes", f"s{sid}_actual_end.png")
        target = os.path.join(self.dir, "keyframes", f"s{sid}_target.png")
        if not self.redo or nxt is None or nxt in self.redo or not os.path.exists(old_end):
            return planned
        if not os.path.exists(target):
            problems = self.judge([old_end], need_lulu=True)
            shutil.copy(old_end if not problems else planned, target)
            log(f"plan {sid} : fin visee = {'ancienne derniere image' if not problems else 'image prevue'}"
                f"{' (' + '; '.join(problems) + ')' if problems else ''}")
        return target

    def step_clips(self):
        prev_end = os.path.join(self.dir, "keyframes", "s1_start.png")
        for k, (sec, timing) in enumerate(zip(self.ep["sections"], self.state["sections"])):
            sid = sec["id"]
            st = self.state.setdefault("clips", {}).setdefault(str(sid), {"tries": 0})
            length = timing["end"] - timing["start"]
            gen_dur = min(DURATIONS, key=lambda d: abs(d - length))
            actual_end = os.path.join(self.dir, "keyframes", f"s{sid}_actual_end.png")
            if sec.get("cut"):
                # un fondu entre deux pieces fait apparaitre deux Nino : on coupe et on repart de l'image de debut
                prev_end = os.path.join(self.dir, "keyframes", f"s{sid}_start.png")
            if not self.redo or sid in self.redo:
                end_img = self.end_target(k, sid)
                while not st.get("ok") and st["tries"] < MAX_TRIES:
                    st["tries"] += 1
                    attempt = os.path.join(self.dir, "clips", f"s{sid}_try{st['tries']}.mp4")
                    r = submit(["-X", "POST", f"{SERVER}/api/tasks/simple", "-F", "mode=keyframes",
                                "-F", f"duration={gen_dur}", "-F", "video_width=1280", "-F", "video_height=720",
                                "-F", f"seed={random.randint(1, 2**31 - 1)}",
                                "-F", f"reference_image=@{prev_end}",
                                "-F", f"end_frame_image=@{end_img}",
                                "-F", f"negative_prompt={self.neg}",
                                "-F", f"prompt={self.ep['style']} {sec['motion']} Smooth continuous motion, same "
                                      f"characters and same room from start to end, no cuts, no talking. "
                                      f"{self.chars()}"])
                    run(["cp", wait_task_file(r["dir_name"], "final_video.mp4"), attempt])
                    frames = []
                    raw_dur = duration(attempt)  # le generateur rend parfois moins que demande (17 s pour 20)
                    for t in SAMPLE_POINTS:
                        fr = os.path.join(self.dir, "frames", f"s{sid}_{int(t * 100)}.jpg")
                        run(["ffmpeg", "-v", "error", "-y", "-ss", f"{raw_dur * t:.2f}", "-i", attempt, "-frames:v",
                             "1", "-vf", "scale=640:-1", fr])
                        frames.append(fr)
                    # pendant un plan, la camera bouge : on verifie les personnages, pas les jouets
                    # (l'etat final de la chambre est garanti par l'image clé de fin, deja validee)
                    problems = self.judge(frames, sec={"teddy_bears": sec.get("teddy_bears")},
                                          need_lulu=not sec.get("lulu_hidden_ok"))
                    log(f"plan {sid} ({length:.1f} s, genere en {gen_dur} s) essai {st['tries']} : {problems or 'OK'}")
                    # on garde le meilleur essai (le moins de problemes), pas forcement le dernier
                    if not (st.get("raw") and os.path.exists(st["raw"])) or len(problems) <= len(st["problems"]):
                        st.update(raw=attempt, problems=problems, gen_duration=gen_dur)
                    st["ok"] = not st["problems"]
                    self.save()
            if st.get("raw") and os.path.exists(st["raw"]):
                prev_end = last_frame(st["raw"], actual_end)
            elif os.path.exists(actual_end):
                prev_end = actual_end  # plan d'origine absent (autre machine) : on garde sa derniere image
            else:
                raise SystemExit(f"plan {sid} introuvable : relancer sans --redo ou avec --redo {sid}")

    # ── montage ──
    def frame_counts(self):
        # meme arrondi que ffmpeg -t a 24 i/s : chaque section dure round(duree x 24) images
        return [round((t["end"] - t["start"]) * FPS) for t in self.state["sections"]]

    def write_srt(self, path, windows=None):
        """Paroles en sous-titres ; avec `windows` [(debut, fin)], seulement ce qui tombe dans ces fenetres."""
        n = 0
        sung = [l for l in self.state["song"]["lines"] if l.get("sung", True)]
        with open(path, "w", encoding="utf-8") as f:
            for i, l in enumerate(sung):
                # la ligne reste un peu apres le chant, mais jamais en meme temps que la suivante
                # (libass empilerait les deux lignes a chaque changement)
                end = min(l["end"] + 0.3, sung[i + 1]["start"]) if i + 1 < len(sung) else l["end"] + 0.3
                for a, b in windows or [(0.0, math.inf)]:
                    s, e = max(l["start"], a), min(end, b)
                    if e - s > 0.02:
                        n += 1
                        f.write(f"{n}\n{srt_ts(s)} --> {srt_ts(e)}\n{wrap(l['text'])}\n\n")
        return path

    def step_assemble(self):
        if self.redo:
            return  # reparation : voir step_patch
        parts = []
        for sec, timing, frames in zip(self.ep["sections"], self.state["sections"], self.frame_counts()):
            st = self.state["clips"][str(sec["id"])]
            part = os.path.join(self.dir, "clips", f"s{sec['id']}_fit.mp4")
            # le plan est accelere/ralenti pour tomber pile sur la duree de sa section
            run(["ffmpeg", "-v", "error", "-y", "-i", st["raw"], "-an", "-vf",
                 fit_filter(timing["end"] - timing["start"], duration(st["raw"]), frames),
                 "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p", part])
            parts.append(part)
        lst = os.path.join(self.dir, "clips", "list.txt")
        open(lst, "w").writelines(f"file '{p}'\n" for p in parts)
        concat = os.path.join(self.dir, "clips", "concat.mp4")
        run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", concat])
        srt = self.write_srt(os.path.join(self.dir, "paroles.srt"))
        final = self.final_path()
        run(["ffmpeg", "-v", "error", "-y", "-i", concat, "-i", self.state["song"]["file"],
             "-vf", f"subtitles={srt}:force_style='{SUB_STYLE}'", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
             "-map", "0:v", "-map", "1:a", "-shortest", "-c:v", "libx264", "-crf", "18", "-preset", "medium",
             "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", final])
        self.make_preview(final)
        self.state["final"] = final
        self.save()
        log(f"montage : {final}")

    def make_preview(self, final):
        preview = os.path.join(self.dir, f"{self.ep['slug']}_apercu.mp4")
        run(["ffmpeg", "-v", "error", "-y", "-i", final, "-vf", "scale=1280:720", "-c:v", "libx264", "-crf", "28",
             "-c:a", "copy", "-movflags", "+faststart", preview])

    def step_patch(self):
        """Remplace les plans refaits dans la video montee, sans toucher au reste (ni au son).

        Les plans d'origine ne sont pas sur GitHub (trop lourds) : on decoupe la video finale existante."""
        if not self.redo:
            return
        final = self.final_path()
        src = os.path.join(self.dir, "clips", "avant_reparation.mp4")
        if not os.path.exists(src):
            shutil.copy(final, src)
        pieces, windows, f0 = [], [], 0
        for sec, timing, n in zip(self.ep["sections"], self.state["sections"], self.frame_counts()):
            sid = sec["id"]
            piece = os.path.join(self.dir, "clips", f"s{sid}_piece.mkv")
            if sid in self.redo:
                raw = self.state["clips"][str(sid)]["raw"]
                vf, inp = fit_filter(timing["end"] - timing["start"], duration(raw), n), raw
                windows.append((f0 / FPS, (f0 + n) / FPS))
            else:
                vf, inp = f"trim=start_frame={f0}:end_frame={f0 + n},setpts=PTS-STARTPTS,setsar=1", src
            # morceaux intermediaires sans perte : la video n'est recompressee qu'une fois, a la fin
            run(["ffmpeg", "-v", "error", "-y", "-i", inp, "-an", "-vf", vf, "-c:v", "libx264", "-qp", "0",
                 "-preset", "ultrafast", "-pix_fmt", "yuv420p", piece])
            pieces.append(piece)
            f0 += n
        lst = os.path.join(self.dir, "clips", "patch_list.txt")
        open(lst, "w").writelines(f"file '{p}'\n" for p in pieces)
        # paroles incrustees seulement sur les plans refaits (les autres les ont deja)
        srt = self.write_srt(os.path.join(self.dir, "clips", "patch.srt"), windows)
        run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", src,
             "-vf", f"subtitles={srt}:force_style='{SUB_STYLE}'", "-map", "0:v", "-map", "1:a",
             "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "copy",
             "-movflags", "+faststart", final])
        for piece in pieces:  # morceaux sans perte : ~1 Go, inutiles une fois la video refaite
            os.remove(piece)
        self.make_preview(final)
        self.state.setdefault("patches", []).append({"sections": sorted(self.redo),
                                                     "date": time.strftime("%Y-%m-%d %H:%M")})
        self.state["final"] = final
        self.save()
        log(f"video reparee (plans {sorted(self.redo)}) : {final}")

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
        sim = self.song_score(self.state["song"]["lines"])
        with open(os.path.join(self.dir, "youtube.md"), "w", encoding="utf-8") as f:
            f.write(f"# {yt['title']}\n\n## Titre\n```\n{yt['title']}\n```\n\n## Description\n```\n{desc}\n```\n\n"
                    f"## Tags\n```\n{', '.join(yt['tags'])}\n```\n\n## Réglages\n"
                    "- Audience : Oui, conçue pour les enfants\n- Contenu modifié ou synthétique : Non (dessin animé)\n"
                    "- Catégorie : Éducation\n- Langue : Français\n\n## Contrôle qualité\n"
                    f"- Chanson : paroles reconnues à {sim:.0%}\n")
            for sid, st in sorted(clips.items(), key=lambda x: int(x[0])):
                f.write(f"- Plan {sid} : {st['tries']} essai(s), {'; '.join(st.get('problems', [])) or 'OK'}\n")
            for p in self.state.get("patches", []):
                f.write(f"- Réparation du {p['date']} : plans {', '.join(map(str, p['sections']))} refaits\n")
        log("fiche YouTube ecrite")


STEPS = ["song", "reference", "keyframes", "clips", "assemble", "patch", "publish"]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("episode_dir")
    p.add_argument("--only", choices=STEPS)
    p.add_argument("--redo", help="plans a refaire dans une video deja montee, ex. 4,7")
    a = p.parse_args()
    ep = Episode(a.episode_dir)
    if a.redo:
        ep.redo = {int(x) for x in a.redo.split(",")}
        pending = ep.state.get("redo")
        if pending != sorted(ep.redo):  # nouvelle demande : on oublie les anciens essais de ces plans
            for sid in ep.redo:
                ep.state.setdefault("clips", {})[str(sid)] = {"tries": 0}
                target = os.path.join(ep.dir, "keyframes", f"s{sid}_target.png")
                if os.path.exists(target):
                    os.remove(target)
            ep.state["redo"] = sorted(ep.redo)
            ep.save()
    for step in STEPS:
        if not a.only or a.only == step:
            log(f"=== {step}")
            getattr(ep, f"step_{step}")()
    if a.redo and not a.only:
        ep.state.pop("redo", None)  # reparation terminee
        ep.save()


if __name__ == "__main__":
    main()
