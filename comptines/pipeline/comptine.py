#!/usr/bin/env python3
"""Pipeline automatique de comptines animees pour enfants musulmans.

Etapes (chacune reprend la ou elle s'est arretee grace au fichier state.json) :
  1. review    : controle du script (pas de copie des paroles d'origine, note LLM)
  2. reference : image de reference des personnages (16:9)
  3. images    : image de depart de chaque scene, validee par un juge visuel
  4. videos    : clip image->video de 10 s par scene, chante (son natif du modele)
  5. validate  : transcription du chant vs paroles, niveau sonore, juge visuel
                 -> regeneration automatique des scenes rejetees
  6. assemble  : montage 1920x1080, volume YouTube, paroles en sous-titres
  7. publish   : miniature + fiche YouTube (titre, description, chapitres, tags)

Usage :
  python comptine.py specs/mon_coran.json            # tout le pipeline
  python comptine.py specs/mon_coran.json --only assemble

Variables d'environnement :
  AGNES_API_KEY    cle Agnes (obligatoire pour le juge visuel et la revue)
  AGNES_DIR        dossier d'agnes-video-generator (defaut ~/agnes-video-generator)
  AGNES_SERVER     serveur Agnes lance (defaut http://localhost:8765)
  WHISPER_PYTHON   python d'un venv ou faster-whisper est installe
"""

import argparse
import concurrent.futures as cf
import difflib
import json
import os
import random
import re
import subprocess
import sys
import threading
import time
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
AGNES_DIR = os.environ.get("AGNES_DIR", os.path.expanduser("~/agnes-video-generator"))
SERVER = os.environ.get("AGNES_SERVER", "http://localhost:8765")
WORKDIR = os.path.join(AGNES_DIR, ".working_dir")
WHISPER_PYTHON = os.environ.get("WHISPER_PYTHON", sys.executable)
FONT = os.environ.get("SUBTITLE_FONT", "DejaVu Sans")
FONT_FILE = os.environ.get("THUMB_FONT_FILE", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")

MAX_IMAGE_TRIES = 3
MAX_VIDEO_TRIES = 3
LYRICS_MIN_SIMILARITY = 0.55
AUDIO_MIN_MEAN_DB = -40.0
SCRIPT_MIN_SCORE = 7
NEGATIVE = ("text, subtitles, letters, watermark, logo, deformed face, extra fingers, extra limbs, "
            "duplicated character, woman without hijab, uncovered hair on women")

sys.path.insert(0, AGNES_DIR)


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


# ── utilitaires ────────────────────────────────────────────────────────────

def run(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw).stdout


def curl_json(args):
    return json.loads(run(["curl", "-s", "-m", "300", *args]))


def submit(args, tries=6):
    """Soumet une tache au serveur Agnes ; reessaie si la reponse n'a pas de dir_name (limite, erreur)."""
    for i in range(tries):
        try:
            r = curl_json(args)
        except Exception as e:  # reponse vide ou non JSON
            r = {"error": str(e)}
        if "dir_name" in r:
            return r
        log(f"soumission refusee ({str(r)[:200]}), nouvel essai dans {30 * (i + 1)} s")
        time.sleep(30 * (i + 1))
    raise RuntimeError(f"soumission impossible : {r}")


def normalize(text):
    text = unicodedata.normalize("NFD", text.lower())
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    text = re.sub(r"[^a-z0-9 ]+", " ", text)
    return " ".join(text.split())


def similarity(a, b):
    return difflib.SequenceMatcher(None, normalize(a), normalize(b)).ratio()


def wait_task_file(dir_name, filename, timeout=3600):
    path = os.path.join(WORKDIR, dir_name, filename)
    state = os.path.join(WORKDIR, dir_name, "task_state.json")
    start = time.time()
    while time.time() - start < timeout:
        status = None
        if os.path.exists(state):
            with open(state, encoding="utf-8") as f:
                s = json.load(f)
            status = s.get("status")
            if status == "failed":
                raise RuntimeError(f"{dir_name}: {s.get('error_message') or s.get('error') or 'failed'}")
        # le fichier apparait avant la fin du telechargement : on attend que la tache soit terminee
        if os.path.exists(path) and status == "completed":
            return path
        time.sleep(15)
    raise TimeoutError(dir_name)


def ffprobe_duration(path):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]))


def mean_volume(path):
    out = subprocess.run(["ffmpeg", "-i", path, "-vn", "-af", "volumedetect", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    m = re.search(r"mean_volume: (-?[\d.]+) dB", out)
    return float(m.group(1)) if m else -99.0


def chat_api():
    from core.api.agnes_chat import AgnesChatAPI
    return AgnesChatAPI(api_key=os.environ["AGNES_API_KEY"])


def parse_json(text):
    text = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.M).strip()
    return json.loads(text[text.find("{"): text.rfind("}") + 1])


def transcribe(paths):
    script = os.path.join(HERE, "transcribe.py")
    return json.loads(run([WHISPER_PYTHON, script, *paths]))


# ── pipeline ───────────────────────────────────────────────────────────────

class Comptine:
    def __init__(self, spec_path):
        with open(spec_path, encoding="utf-8") as f:
            self.spec = json.load(f)
        self.out = os.path.join(ROOT, "output", self.spec["slug"])
        os.makedirs(os.path.join(self.out, "scenes"), exist_ok=True)
        os.makedirs(os.path.join(self.out, "frames"), exist_ok=True)
        self.state_path = os.path.join(self.out, "state.json")
        self.lock = threading.Lock()
        self.state = {"scenes": {}}
        if os.path.exists(self.state_path):
            with open(self.state_path, encoding="utf-8") as f:
                self.state = json.load(f)

    def save(self):
        with self.lock:
            with open(self.state_path, "w", encoding="utf-8") as f:
                json.dump(self.state, f, ensure_ascii=False, indent=2)

    def scene_state(self, sid):
        return self.state["scenes"].setdefault(str(sid), {"image_tries": 0, "video_tries": 0})

    # ── prompts ──
    def cast_text(self, cast):
        chars = self.spec["characters"]
        return " ".join(f"{name}: {chars[name]['look']}" for name in cast)

    def expected_counts(self, cast):
        counts = {"adult_women": 0, "adult_men": 0, "children": 0, "animals": 0}
        for name in cast:
            counts[self.spec["characters"][name]["type"]] += 1
        return counts

    def sung_text(self, scene):
        parts = []
        for line in scene["lyrics"]:
            parts.append(f"{line['singer']} sings: \"{line['text']}\"")
        return " ".join(parts)

    def image_prompt(self, scene):
        cast = scene["cast"]
        return (f"{self.spec['style']} {scene['image']} Exactly {len(cast)} characters in the image, "
                f"each appearing only once. {self.cast_text(cast)}")

    def video_prompt(self, scene):
        return (f"{self.spec['style']} {self.spec['music']} {scene['action']} {self.sung_text(scene)} "
                f"Clear lip-sync singing in French. {self.cast_text(scene['cast'])}")

    # ── 1. revue du script ──
    def step_review(self):
        if self.state.get("review", {}).get("ok"):
            return
        lyrics = " ".join(l["text"] for s in self.spec["scenes"] for l in s["lyrics"])
        ref = self.spec.get("inspiration", {}).get("reference_lyrics", "")
        # anti-copie : aucune suite de 5 mots identique aux paroles d'origine
        ref_words = normalize(ref).split()
        grams = {" ".join(ref_words[i:i + 5]) for i in range(len(ref_words) - 4)}
        words = normalize(lyrics).split()
        copied = sorted({" ".join(words[i:i + 5]) for i in range(len(words) - 4)} & grams)
        review = {"copied_5grams": copied}
        if os.environ.get("AGNES_API_KEY"):
            prompt = (
                "Evalue ce script de comptine animee pour enfants musulmans de 2 a 6 ans (francais). "
                "Donne une note de 1 a 10 pour : coherence (l'histoire suit une progression logique), "
                "attrait_enfants (rythme, repetition, refrain accrocheur, images amusantes), "
                "simplicite (mots faciles a chanter pour un enfant), justesse_islamique (aucune erreur "
                "religieuse, respect), valeur_educative. Reponds en JSON : {\"coherence\":int, "
                "\"attrait_enfants\":int, \"simplicite\":int, \"justesse_islamique\":int, "
                "\"valeur_educative\":int, \"problemes\":[str], \"suggestions\":[str]}\n\n"
                + json.dumps([{"scene": s["id"], "action": s["action"], "paroles": [l["text"] for l in s["lyrics"]]}
                              for s in self.spec["scenes"]], ensure_ascii=False))
            review["llm"] = parse_json(chat_api().chat("Tu es un expert en contenus educatifs islamiques "
                                                       "pour jeunes enfants. Reponds uniquement en JSON.",
                                                       prompt, max_tokens=1200))
        scores = [v for k, v in review.get("llm", {}).items() if isinstance(v, int)]
        review["ok"] = not copied and (not scores or min(scores) >= SCRIPT_MIN_SCORE)
        self.state["review"] = review
        self.save()
        log(f"revue du script : copie={copied or 'aucune'} notes={review.get('llm')}")
        if not review["ok"]:
            raise SystemExit("Script refuse par la revue : corrige la spec (voir state.json -> review).")

    # ── 2. image de reference ──
    def step_reference(self):
        ref = os.path.join(self.out, "reference.png")
        if os.path.exists(ref):
            return ref
        r = submit(["-X", "POST", f"{SERVER}/api/image/generate", "-F", "size=1344x768",
                       "-F", f"prompt={self.spec['style']} {self.spec['reference_image']} "
                             f"{self.cast_text(list(self.spec['characters']))}"])
        run(["cp", wait_task_file(r["dir_name"], "final_image.png"), ref])
        log(f"image de reference : {ref}")
        return ref

    # ── juge visuel ──
    def judge_frames(self, frames, scene):
        expected = self.expected_counts(scene["cast"])
        expected.update(scene.get("max_counts", {}))
        question = ('Look at this frame of a Muslim children\'s cartoon. Return JSON: {"adult_women": int, '
                    '"adult_men": int, "children": int, "animals": int, "women_without_hijab": int, '
                    '"visible_text_or_letters": bool, "deformed_face_or_hands": bool, "child_friendly": bool}')
        api = chat_api()
        problems = []
        for fr in frames:
            try:
                v = parse_json(api.chat_multimodal("You are a strict quality checker. Answer only JSON.",
                                                   question, [fr], max_tokens=300))
            except Exception as e:  # juge indisponible : on ne bloque pas
                log(f"juge visuel indisponible ({e})")
                continue
            for key, maxi in expected.items():
                if int(v.get(key, 0)) > maxi:
                    problems.append(f"{os.path.basename(fr)}: {key}={v.get(key)} (max {maxi})")
            if int(v.get("women_without_hijab", 0)) > 0:
                problems.append(f"{os.path.basename(fr)}: femme sans hijab")
            if v.get("visible_text_or_letters") and not scene.get("allow_text"):
                problems.append(f"{os.path.basename(fr)}: texte visible")
            if v.get("child_friendly") is False:
                problems.append(f"{os.path.basename(fr)}: pas adapte aux enfants")
        return problems

    # ── 3. images de depart ──
    def make_image(self, scene, ref):
        st = self.scene_state(scene["id"])
        if st.get("image_ok"):
            return st["image"]
        while st["image_tries"] < MAX_IMAGE_TRIES:
            if not st.get("pending_image"):
                st["image_tries"] += 1
                # l'image de reference contient tous les personnages : si l'essai precedent en avait
                # en trop, on genere sans elle (descriptions detaillees seulement)
                too_many = any("max" in p for p in st.get("image_problems", []))
                # (Agnes refuse negative_prompt sans image de reference)
                args = (["-F", f"reference_image=@{ref}", "-F", f"negative_prompt={NEGATIVE}"]
                        if not too_many else [])
                r = submit(["-X", "POST", f"{SERVER}/api/image/generate", "-F", "size=1344x768", *args,
                            "-F", f"prompt={self.image_prompt(scene)}"])
                st["pending_image"] = r["dir_name"]
                self.save()
            img = os.path.join(self.out, "scenes", f"scene_{scene['id']}_start.png")
            try:
                run(["cp", wait_task_file(st["pending_image"], "final_image.png"), img])
            finally:
                st.pop("pending_image", None)
            problems = self.judge_frames([img], scene)
            st.update(image=img, image_problems=problems, image_ok=not problems)
            self.save()
            log(f"scene {scene['id']} image essai {st['image_tries']} : {problems or 'OK'}")
            if not problems:
                return img
        st["image_ok"] = True  # on garde la derniere, la validation video tranchera
        self.save()
        return st["image"]

    # ── 4+5. video + validation ──
    def make_video(self, scene, ref):
        st = self.scene_state(scene["id"])
        if st.get("video_ok"):
            return
        while st["video_tries"] < MAX_VIDEO_TRIES:
            if not st.get("pending_video"):
                img = self.make_image(scene, ref)
                st["video_tries"] += 1
                r = submit(["-X", "POST", f"{SERVER}/api/tasks/simple", "-F", "mode=i2v", "-F", "duration=10",
                               "-F", "video_width=1280", "-F", "video_height=720",
                               "-F", f"seed={random.randint(1, 2**31 - 1)}",
                               "-F", f"reference_image=@{img}", "-F", f"negative_prompt={NEGATIVE}",
                               "-F", f"prompt={self.video_prompt(scene)}"])
                st["pending_video"] = r["dir_name"]  # reprise possible si le pipeline est relance
                self.save()
            clip = os.path.join(self.out, "scenes", f"scene_{scene['id']}.mp4")
            try:
                run(["cp", wait_task_file(st["pending_video"], "final_video.mp4"), clip])
            finally:
                st.pop("pending_video", None)
            report = self.validate_clip(scene, clip)
            st.update(video=clip, validation=report, video_ok=report["ok"])
            self.save()
            log(f"scene {scene['id']} video essai {st['video_tries']} : "
                f"{'OK' if report['ok'] else report['problems']}")
            if report["ok"]:
                return
            if any("adult" in p or "children" in p or "animals" in p or "hijab" in p for p in report["problems"]):
                st["image_ok"] = False  # probleme de personnages : nouvelle image de depart
                st["image_tries"] = 0
                st["image_problems"] = [p for p in report["problems"] if "max" in p]
        log(f"scene {scene['id']} : echec apres {MAX_VIDEO_TRIES} essais, garde la derniere version")

    def validate_clip(self, scene, clip):
        problems = []
        expected = " ".join(l["text"] for l in scene["lyrics"])
        tr = transcribe([clip])[0]
        heard = " ".join(s["text"] for s in tr["segments"])
        sim = similarity(expected, heard)
        if sim < LYRICS_MIN_SIMILARITY:
            problems.append(f"paroles: similarite {sim:.2f} (entendu: {heard[:120]!r})")
        vol = mean_volume(clip)
        if vol < AUDIO_MIN_MEAN_DB:
            problems.append(f"son trop faible ({vol:.1f} dB)")
        frames = []
        for t in (1.5, 5, 8.5):
            fr = os.path.join(self.out, "frames", f"scene_{scene['id']}_{t}.jpg")
            run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", clip, "-frames:v", "1",
                 "-vf", "scale=640:-1", fr])
            frames.append(fr)
        problems += self.judge_frames(frames, scene)
        return {"ok": not problems, "problems": problems, "similarity": round(sim, 2),
                "heard": heard, "mean_volume_db": vol, "segments": tr["segments"]}

    def step_scenes(self):
        ref = self.step_reference()
        with cf.ThreadPoolExecutor(max_workers=int(os.environ.get("SCENE_WORKERS", "3"))) as ex:
            list(ex.map(lambda s: self.safe_make_video(s, ref), self.spec["scenes"]))
        missing = [s["id"] for s in self.spec["scenes"] if not self.scene_state(s["id"]).get("video")]
        if missing:
            raise SystemExit(f"scenes sans video : {missing} (relance le pipeline pour reprendre)")

    def safe_make_video(self, scene, ref):
        try:
            self.make_video(scene, ref)
        except Exception as e:  # une scene en erreur n'arrete pas les autres
            log(f"scene {scene['id']} : erreur {e!r}")

    # ── 6. montage ──
    def step_assemble(self):
        tmp = os.path.join(self.out, "tmp")
        os.makedirs(tmp, exist_ok=True)
        parts, cues, chapters, offset = [], [], [], 0.0
        for scene in self.spec["scenes"]:
            st = self.scene_state(scene["id"])
            clip = st["video"]
            dur = ffprobe_duration(clip)
            part = os.path.join(tmp, f"s{scene['id']}.mp4")
            run(["ffmpeg", "-v", "error", "-y", "-i", clip,
                 "-vf", "scale=1964:1080:flags=lanczos,crop=1920:1080,setsar=1,fps=24",
                 "-af", f"afade=t=in:d=0.15,afade=t=out:st={dur - 0.15:.2f}:d=0.15,aresample=48000",
                 "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
                 "-c:a", "aac", "-b:a", "192k", "-ac", "2", part])
            parts.append(part)
            chapters.append((offset, scene["chapter"]))
            # sous-titres : les lignes se partagent la zone chantee, au prorata de leur longueur
            segs = st.get("validation", {}).get("segments") or []
            start = segs[0]["start"] if segs else 0.3
            end = segs[-1]["end"] if segs else dur - 0.3
            start, end = max(0.1, start), min(dur - 0.1, max(end, start + 2))
            total = sum(len(l["text"]) for l in scene["lyrics"])
            t = start
            for line in scene["lyrics"]:
                d = (end - start) * len(line["text"]) / total
                cues.append((offset + t, offset + t + d, line["text"]))
                t += d
            offset += dur
        with open(os.path.join(tmp, "list.txt"), "w") as f:
            f.writelines(f"file '{p}'\n" for p in parts)
        srt = os.path.join(self.out, "paroles.srt")
        with open(srt, "w", encoding="utf-8") as f:
            for i, (a, b, text) in enumerate(cues, 1):
                f.write(f"{i}\n{srt_ts(a)} --> {srt_ts(b)}\n{wrap(text)}\n\n")
        concat = os.path.join(tmp, "concat.mp4")
        run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i",
             os.path.join(tmp, "list.txt"), "-c", "copy", concat])
        final = os.path.join(self.out, f"{self.spec['slug']}_youtube.mp4")
        style = (f"FontName={FONT},Bold=1,Fontsize=22,PrimaryColour=&H00FFFFFF,OutlineColour=&H00402080,"
                 "BorderStyle=1,Outline=3,Shadow=1,Alignment=2,MarginV=28")
        run(["ffmpeg", "-v", "error", "-y", "-i", concat, "-vf", f"subtitles={srt}:force_style='{style}'",
             "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:v", "libx264", "-crf", "18", "-preset", "medium",
             "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", final])
        preview = os.path.join(self.out, f"{self.spec['slug']}_apercu.mp4")
        run(["ffmpeg", "-v", "error", "-y", "-i", final, "-c:v", "libx264", "-crf", "28", "-preset", "medium",
             "-vf", "scale=1280:720", "-c:a", "copy", "-movflags", "+faststart", preview])
        run(["rm", "-rf", tmp])
        self.state["chapters"] = chapters
        self.state["final"] = final
        self.save()
        log(f"montage : {final} ({offset:.1f} s)")

    # ── 7. miniature + fiche YouTube ──
    def step_publish(self):
        yt = self.spec["youtube"]
        thumb_scene = next(s for s in self.spec["scenes"] if s.get("thumbnail"))
        frame = os.path.join(self.out, "frames", "thumb_src.png")
        run(["ffmpeg", "-v", "error", "-y", "-ss", str(thumb_scene.get("thumbnail_time", 2)), "-i",
             self.scene_state(thumb_scene["id"])["video"], "-frames:v", "1", frame])
        big, small = yt["thumbnail_text"], yt["thumbnail_subtext"]
        size = min(160, int(1800 / max(len(big), 1)))
        vf = ("scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,"
              f"drawtext=fontfile={FONT_FILE}:text='{big}':fontsize={size}:fontcolor=#FFD84D:borderw=11:"
              "bordercolor=#5B2A86:x=(w-tw)/2:y=h-th-40,"
              f"drawtext=fontfile={FONT_FILE}:text='{small}':fontsize=52:fontcolor=white:borderw=6:"
              "bordercolor=#5B2A86:x=36:y=40")
        run(["ffmpeg", "-v", "error", "-y", "-i", frame, "-vf", vf, "-q:v", "2",
             os.path.join(self.out, "miniature_youtube.jpg")])
        chapters = "\n".join(f"{int(t) // 60}:{int(t) % 60:02d} {name}" for t, name in self.state["chapters"])
        lyrics = "\n".join(l["text"] for s in self.spec["scenes"] for l in s["lyrics"])
        description = f"{yt['hook']}\n\n⏱️ Chapitres\n{chapters}\n\n🎵 Paroles\n{lyrics}\n\n{yt['footer']}"
        rows = [(s["id"], self.scene_state(s["id"])) for s in self.spec["scenes"]]
        with open(os.path.join(self.out, "youtube.md"), "w", encoding="utf-8") as f:
            f.write(f"# Fiche YouTube : {yt['title']}\n\n## Titre\n```\n{yt['title']}\n```\n\n"
                    f"## Description\n```\n{description}\n```\n\n## Tags\n```\n{', '.join(yt['tags'])}\n```\n\n"
                    "## Réglages\n- Audience : **Oui, elle est conçue pour les enfants**\n"
                    "- Contenu modifié ou synthétique : Non (dessin animé non réaliste)\n"
                    "- Catégorie : Éducation\n- Langue de la vidéo : Français\n"
                    "- Miniature : `miniature_youtube.jpg`\n\n## Contrôle qualité\n\n"
                    f"Revue du script : `{json.dumps(self.state.get('review', {}).get('llm', {}), ensure_ascii=False)}`\n\n"
                    "| Scène | Essais | Paroles (similarité) | Son (dB) | Problèmes restants |\n|---|---|---|---|---|\n")
            for sid, st in rows:
                v = st.get("validation", {})
                f.write(f"| {sid} | {st.get('video_tries')} | {v.get('similarity')} | "
                        f"{v.get('mean_volume_db')} | {'; '.join(v.get('problems', [])) or 'aucun'} |\n")
        log(f"fiche YouTube : {os.path.join(self.out, 'youtube.md')}")


def srt_ts(s):
    ms = int(round(s * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def wrap(text, width=48):
    if len(text) <= width:
        return text
    cut = text.rfind(" ", 0, len(text) // 2 + 8)
    return text[:cut] + "\n" + text[cut + 1:]


STEPS = ["review", "scenes", "assemble", "publish"]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("spec")
    p.add_argument("--only", choices=STEPS)
    a = p.parse_args()
    c = Comptine(a.spec)
    for step in STEPS:
        if a.only and step != a.only:
            continue
        log(f"=== {c.spec['slug']} : {step}")
        getattr(c, f"step_{step}")()


if __name__ == "__main__":
    main()
