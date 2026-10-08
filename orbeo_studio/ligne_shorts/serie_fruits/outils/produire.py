#!/usr/bin/env python3
"""Fabrique un episode de la serie fruits a partir de son episode.json (reprise automatique par state.json).

Etapes :
  tenues   les tenues de l'episode (robe de soiree, sweat...) a partir des fiches d'identite
  decors   un decor vide par lieu (2 candidats, le premier sans personnage ni texte est garde)
  images   l'image cle de chaque plan : le decor, puis un seul personnage ajoute par passe (fiche en reference),
           verifiee par le juge visuel (bon personnage, une seule copie, pas de texte, pas de deformation)
  cadrage  la camera se rapproche (gros plan « gp » ou plan rapproche « pm ») en repartant de l'image cle : les
           images cles gardent le cadre large du decor, or les emotions et les levres se lisent en gros plan
  clips    un clip Agnes v2.0 par plan : le personnage dit sa replique en francais, les levres bougent ;
           controle par whisper (replique reconnue) et par le juge visuel ; jusqu'a 3 essais, le meilleur gagne
  voix     chaque replique est convertie vers une voix de reference par personnage (OpenVoice) : voix constante
  montage  voir montage.py

Usage : ~/agnes-video-generator/.venv/bin/python produire.py ../episodes/01_la_bague [--only images] [--redo 4,7]
Variables : WHISPER_PYTHON (python avec faster-whisper), VOIX_PYTHON (python avec OpenVoice et Resemblyzer),
OPENVOICE_SRC, OPENVOICE_CKPT (voir voix.py).
"""
import argparse
import asyncio
import json
import os
import random
import re
import shutil
import subprocess
import sys
import threading
import time
import unicodedata
import difflib

sys.path.insert(0, os.path.expanduser("~/agnes-video-generator"))
os.environ.setdefault("AGNES_API_KEY", open(os.path.expanduser("~/.agnes_key")).read().strip())
from core.api.agnes_chat import AgnesChatAPI  # noqa: E402
from core.api.agnes_image import AgnesImageAPI  # noqa: E402
from core.api.agnes_video import AgnesVideoAPI  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
IDENTITE = os.path.join(HERE, "..", "identite")
WHISPER_PYTHON = os.environ.get("WHISPER_PYTHON", os.path.expanduser("~/ace-venv/bin/python"))
VOIX_PYTHON = os.environ.get("VOIX_PYTHON", os.path.expanduser("~/ace-venv/bin/python"))
KEY = os.environ["AGNES_API_KEY"]
IMG_SIZE = "768x1344"  # Agnes rend 736x1312
VID_W, VID_H = 720, 1280  # Agnes rend 704x1280
MAX_IMG_TRIES = 4
MAX_CLIP_TRIES = 3
NEG_VIDEO = ("subtitles, captions, on-screen text, letters, words, watermark, logo, extra characters, duplicate "
             "character, second copy of the character, camera zoom, camera movement, music, deformed face, extra "
             "fingers, morphing, face changing")
SAMPLE_POINTS = (0.2, 0.5, 0.85)


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw).stdout


def normalize(text):
    text = unicodedata.normalize("NFD", text.lower())
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return " ".join(re.sub(r"[^a-z0-9 ]+", " ", text).split())


def similarity(a, b):
    return difflib.SequenceMatcher(None, normalize(a), normalize(b)).ratio()


def parse_json(text):
    text = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.M).strip()
    return json.loads(text[text.find("{"): text.rfind("}") + 1])


def duration(path):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]))


def pronoun(perso):
    return "she" if perso.split("_")[0] in ("cerise", "peche", "prune") else "he"


class Episode:
    def __init__(self, d, redo=()):
        self.dir = os.path.abspath(d)
        self.ep = json.load(open(os.path.join(self.dir, "episode.json"), encoding="utf-8"))
        self.state_path = os.path.join(self.dir, "state.json")
        self.state = json.load(open(self.state_path)) if os.path.exists(self.state_path) else {}
        self.lock = threading.Lock()
        self.redo = set(redo)
        for sub in ("decors", "images", "clips", "voix", "controle"):
            os.makedirs(os.path.join(self.dir, sub), exist_ok=True)
        self.chat = AgnesChatAPI(api_key=KEY)

    def save(self):
        with self.lock:
            tmp = self.state_path + ".tmp"
            json.dump(self.state, open(tmp, "w"), ensure_ascii=False, indent=1)
            os.replace(tmp, self.state_path)

    def ident(self, perso):
        return os.path.join(IDENTITE, f"{perso}.png")

    # ── juge visuel ──
    def judge(self, frame, perso, cadre, crowd=False):
        """Problemes trouves sur une image (vide = OK). Compare au personnage de reference."""
        q = ("Image 1 is a frame from a 3D animated film. Image 2 is the reference sheet of the main character. "
             f"Expected shot: {cadre} Count only characters that are clearly visible and in focus"
             f"{', ignoring the blurred guests in the background' if crowd else ''}. Return JSON: "
             '{"characters_in_focus": int, "same_character_as_reference": bool (same skin color, hair, face and '
             'clothes as image 2), "copies_of_reference_character": int, "visible_text_or_letters": bool, '
             '"deformed_face_or_hands": bool, "matches_expected_shot": bool}')
        try:
            v = parse_json(self.chat.chat_multimodal("You are a strict quality checker. Answer only JSON.", q,
                                                     [frame, self.ident(perso)], max_tokens=300))
        except Exception as e:  # juge indisponible : on ne bloque pas
            log(f"juge indisponible ({e})")
            return []
        p = []
        if int(v.get("characters_in_focus", 1)) > 1 and not crowd:
            p.append(f"{v['characters_in_focus']} personnages")
        if int(v.get("characters_in_focus", 1)) == 0:
            p.append("personnage absent")
        if v.get("same_character_as_reference") is False:
            p.append("ne ressemble pas a la fiche")
        if int(v.get("copies_of_reference_character", 1)) > 1:
            p.append(f"{v['copies_of_reference_character']} copies du personnage")
        if v.get("visible_text_or_letters"):
            p.append("texte visible")
        if v.get("deformed_face_or_hands"):
            p.append("deformation")
        if v.get("matches_expected_shot") is False:
            p.append("cadrage different")
        return p

    # ── tenues ──
    async def step_tenues(self):
        api = AgnesImageAPI(api_key=KEY)

        async def one(name, t):
            path = os.path.join(IDENTITE, f"{name}.png")
            if os.path.exists(path):
                return
            for k in range(1, MAX_IMG_TRIES + 1):
                cand = os.path.join(IDENTITE, "candidats", f"{name}_{k}.png")
                os.makedirs(os.path.dirname(cand), exist_ok=True)
                img = await api.generate_single_image(
                    prompt=f"{t['consigne']} Full body, front view, standing, centered, plain light grey studio "
                           "background, character reference, exactly one single character, no text. Pixar-style 3D "
                           "animated character, cinematic soft lighting.",
                    reference_image_paths=[self.ident(t["de"])], size="1024x1024")
                await img.save(cand)
                problems = await asyncio.to_thread(self.judge, cand, t["de"], "Full body character reference.")
                problems = [x for x in problems if x != "ne ressemble pas a la fiche"]  # la tenue change
                log(f"tenue {name} essai {k} : {problems or 'OK'}")
                if not problems:
                    shutil.copy(cand, path)
                    return
            raise SystemExit(f"tenue {name} refusee")

        await asyncio.gather(*[one(n, t) for n, t in self.ep.get("tenues", {}).items()])

    # ── decors ──
    async def step_decors(self):
        api = AgnesImageAPI(api_key=KEY)
        q = ('Look at this image. Return JSON: {"people_or_characters_in_focus": int, '
             '"visible_text_or_letters": bool}')

        async def one(name, d):
            path = os.path.join(self.dir, "decors", f"{name}.png")
            if os.path.exists(path):
                return
            for k in range(1, MAX_IMG_TRIES + 1):
                cand = os.path.join(self.dir, "decors", f"{name}_cand{k}.png")
                img = await api.generate_single_image(
                    prompt=f"{self.ep['style']}. {d['consigne']} "
                           f"{'' if d.get('foule') else 'Empty set: no character in the picture. '}No text, no "
                           "letters, no signs with writing.", size=IMG_SIZE)
                await img.save(cand)
                try:
                    v = parse_json(await asyncio.to_thread(self.chat.chat_multimodal, "Answer only JSON.", q,
                                                           [cand], 200))
                except Exception:
                    v = {}
                ok = ((d.get("foule") or int(v.get("people_or_characters_in_focus", 0)) == 0)
                      and not v.get("visible_text_or_letters"))
                log(f"decor {name} essai {k} : {'OK' if ok else v}")
                if ok:
                    shutil.copy(cand, path)
                    return
            shutil.copy(cand, path)  # le dernier faute de mieux, signale
            log(f"decor {name} : garde sans validation")

        await asyncio.gather(*[one(n, d) for n, d in self.ep["decors"].items()])

    # ── images cles ──
    def plan_ids(self):
        return [p["id"] for p in self.ep["plans"]]

    def plan(self, pid):
        return next(p for p in self.ep["plans"] if p["id"] == pid)

    async def make_image(self, api, p):
        key = str(p["id"])
        st = self.state.setdefault("images", {}).setdefault(key, {"tries": 0})
        path = os.path.join(self.dir, "images", f"p{p['id']:02d}.png")
        if st.get("done") and os.path.exists(path) and p["id"] not in self.redo:
            return
        if p["id"] in self.redo:
            st.update(tries=0, done=False)
        base = os.path.join(self.dir, "decors", f"{p['decor']}.png")
        missing = [f for f in [base] + [self.ident(x) for x in p["persos"]] if not os.path.exists(f)]
        if missing:
            log(f"image plan {p['id']} : en attente de {', '.join(os.path.basename(f) for f in missing)}")
            return
        crowd = bool(self.ep["decors"][p["decor"]].get("foule"))
        best = None
        while st["tries"] < MAX_IMG_TRIES:
            st["tries"] += 1
            cur = base
            problems = []
            for i, perso in enumerate(p["persos"]):
                desc = self.ep["persos"][perso]
                prompt = (f"{self.ep['style']}. Image 1 shows the location, image 2 shows the character. Create a "
                          "new frame set in exactly this location (same decor, same colors and lighting) with "
                          "exactly this character, who keeps exactly the same face, skin color, hair and clothes "
                          f"as in image 2: {desc}. {p['cadre']} Vertical composition: the face is in the upper half "
                          "of the frame, nothing important in the bottom fifth. Exactly one main character in the "
                          "picture. No text, no letters, no subtitles.")
                img = await api.generate_single_image(prompt=prompt, reference_image_paths=[cur, self.ident(perso)],
                                                      size=IMG_SIZE)
                out = os.path.join(self.dir, "images", f"p{p['id']:02d}_t{st['tries']}_{i}.png")
                await img.save(out)
                cur = out
                problems = await asyncio.to_thread(self.judge, out, perso, p["cadre"], crowd)
                if problems:
                    break
            st["problems"] = problems
            log(f"image plan {p['id']} essai {st['tries']} : {problems or 'OK'}")
            if best is None or len(problems) < best[0]:
                best = (len(problems), cur)
            self.save()
            if not problems:
                break
        shutil.copy(best[1], path)
        st["done"] = True
        self.save()

    async def reframe(self, api, p):
        key = str(p["id"])
        st = self.state.setdefault("cadrage", {}).setdefault(key, {"tries": 0})
        src = os.path.join(self.dir, "images", f"p{p['id']:02d}.png")
        path = os.path.join(self.dir, "images", f"p{p['id']:02d}_cadre.png")
        if st.get("done") and os.path.exists(path) and p["id"] not in self.redo:
            return
        if p["id"] in self.redo:
            st.update(tries=0, done=False)
        frame = ("a close-up shot: the face, hair and shoulders fill most of the vertical frame, the face in the upper "
                 "half, the background softly blurred" if p["recadrage"] == "gp" else
                 "a medium close-up shot from the waist up: the character fills most of the vertical frame, the face "
                 "in the upper third, the background softly blurred")
        perso = p["persos"][0]
        prompt = (f"{self.ep['style']}. Same scene, same character, same clothes, same lighting and same style as the "
                  f"image, but the camera is much closer: {frame}. The character: {self.ep['persos'][perso]}. "
                  f"{p['cadre']} Exactly one character. No text.")
        crowd = bool(self.ep["decors"][p["decor"]].get("foule"))
        best = None
        while st["tries"] < 3:
            st["tries"] += 1
            out = os.path.join(self.dir, "images", f"p{p['id']:02d}_cadre_t{st['tries']}.png")
            img = await api.generate_single_image(prompt=prompt, reference_image_paths=[src], size=IMG_SIZE)
            await img.save(out)
            problems = await asyncio.to_thread(self.judge, out, perso, f"{frame}. {p['cadre']}", crowd)
            log(f"cadrage plan {p['id']} essai {st['tries']} : {problems or 'OK'}")
            if best is None or len(problems) < best[0]:
                best = (len(problems), out)
            st["problems"] = problems
            self.save()
            if not problems:
                break
        shutil.copy(best[1], path)
        st["done"] = True
        self.save()

    async def step_cadrage(self):
        api = AgnesImageAPI(api_key=KEY)
        sem = asyncio.Semaphore(4)

        async def guarded(p):
            async with sem:
                try:
                    await self.reframe(api, p)
                except Exception as e:
                    log(f"cadrage plan {p['id']} ECHEC {e}")

        await asyncio.gather(*[guarded(p) for p in self.ep["plans"] if p.get("recadrage")])

    async def step_images(self):
        api = AgnesImageAPI(api_key=KEY)
        sem = asyncio.Semaphore(4)

        async def guarded(p):
            async with sem:
                try:
                    await self.make_image(api, p)
                except Exception as e:
                    log(f"image plan {p['id']} ECHEC {e}")

        await asyncio.gather(*[guarded(p) for p in self.ep["plans"] if p.get("persos")])

    # ── clips ──
    def clip_prompt(self, p):
        perso = p["persos"][0]
        pr = pronoun(perso)
        desc = self.ep["persos"][perso]
        cam = "Locked-off static camera, the framing does not change, no zoom. "
        if p.get("parle"):
            voix = self.ep["voix"][p["parle"]]
            say = (f"{p['jeu']}, in French, with {voix}, spoken aloud only, never written on screen: "
                   f"{p['replique']} {pr.capitalize()} {'speaks' if pr else ''} with clear lip movements in sync "
                   f"with every word. Only {'her' if pr == 'she' else 'him'} speaks. Only the voice, quiet "
                   "background, no music. ")
        else:
            say = f"{p['jeu']}. No one speaks. {self.ep['decors'][p['decor']].get('son', '')} sound, no music. "
            cam = "" if "walk" in p["jeu"] or "run" in p["jeu"] else cam
        return (f"{cam}{desc}. {say}Clean image with no on-screen text: no subtitles, no captions, no letters "
                f"anywhere. {self.ep['style']}.")

    def transcribe(self, paths):
        script = os.path.join(HERE, "transcrire.py")
        return json.loads(run([WHISPER_PYTHON, script, *paths]))

    def check_clip(self, p, path):
        """Score d'un clip : replique reconnue (whisper) et images conformes (juge)."""
        ctrl = os.path.join(self.dir, "controle", os.path.basename(path)[:-4])
        os.makedirs(ctrl, exist_ok=True)
        dur = duration(path)
        frames = []
        for t in SAMPLE_POINTS:
            fr = os.path.join(ctrl, f"f{int(t * 100)}.jpg")
            run(["ffmpeg", "-loglevel", "error", "-y", "-ss", f"{dur * t:.2f}", "-i", path, "-frames:v", "1", fr])
            frames.append(fr)
        problems = []
        crowd = bool(self.ep["decors"][p["decor"]].get("foule"))
        bad = 0
        for fr in frames:
            pr = self.judge(fr, p["persos"][0], p["cadre"], crowd)
            pr = [x for x in pr if x not in ("cadrage different", "texte visible")]  # faux sous-titres masques
            if pr:
                bad += 1
                problems.append(f"{os.path.basename(fr)}: {', '.join(pr)}")
        res = {"problems": problems, "bad_frames": bad, "duration": dur}
        if p.get("parle"):
            wav = os.path.join(ctrl, "voix.wav")
            run(["ffmpeg", "-loglevel", "error", "-y", "-i", path, "-vn", "-ac", "1", "-ar", "16000", wav])
            tr = self.transcribe([wav])[0]
            words = tr["words"]
            text = " ".join(w["word"] for w in words)
            res.update(text=text, sim=round(similarity(text, p["replique"]), 2), words=words)
            if words:
                res.update(speech=[words[0]["start"], words[-1]["end"]])
        else:
            res["sim"] = 1.0
        res["score"] = round(res["sim"] - 0.25 * bad, 3)
        return res

    async def make_clip(self, api, p):
        key = str(p["id"])
        st = self.state.setdefault("clips", {}).setdefault(key, {"tries": []})
        path = os.path.join(self.dir, "clips", f"p{p['id']:02d}.mp4")
        if st.get("done") and os.path.exists(path) and p["id"] not in self.redo:
            return
        if p["id"] in self.redo:
            st.update(done=False)
        img = os.path.join(self.dir, "images", f"p{p['id']:02d}_cadre.png")
        if not os.path.exists(img):
            img = os.path.join(self.dir, "images", f"p{p['id']:02d}.png")
        n_words = len(normalize(p.get("replique") or "").split())
        secs = 10 if n_words > 12 else 5
        while len(st["tries"]) < MAX_CLIP_TRIES * (2 if p["id"] in self.redo else 1):
            k = len(st["tries"]) + 1
            out = os.path.join(self.dir, "clips", f"p{p['id']:02d}_t{k}.mp4")
            t0 = time.time()
            try:
                v = await asyncio.wait_for(api.generate_single_video(
                    self.clip_prompt(p), reference_image_paths=[img], duration=secs, width=VID_W, height=VID_H,
                    seed=random.randint(1, 10 ** 6), negative_prompt=NEG_VIDEO), timeout=1800)
                await v.save(out)
            except Exception as e:
                log(f"clip plan {p['id']} essai {k} ECHEC {repr(e)[:200]}")
                st["tries"].append({"file": None, "error": repr(e)[:200]})
                self.save()
                await asyncio.sleep(30)
                continue
            res = await asyncio.to_thread(self.check_clip, p, out)
            res["file"] = os.path.basename(out)
            res["gen_s"] = round(time.time() - t0)
            st["tries"].append(res)
            self.save()
            log(f"clip plan {p['id']} essai {k} : sim={res['sim']} images ratees={res['bad_frames']} "
                f"« {res.get('text', '')} » {res['problems'][:2]}")
            if res["sim"] >= 0.8 and res["bad_frames"] == 0:
                break
        good = [t for t in st["tries"] if t.get("file")]
        if not good:
            log(f"clip plan {p['id']} : aucun clip")
            return
        best = max(good, key=lambda t: t["score"])
        shutil.copy(os.path.join(self.dir, "clips", best["file"]), path)
        st.update(done=True, best=best["file"])
        self.save()

    async def step_clips(self):
        api = AgnesVideoAPI(KEY, model="agnes-video-v2.0", max_retries=3, retry_base_delay=30.0)
        sem = asyncio.Semaphore(int(os.environ.get("CLIPS_PARALLELE", "3")))

        async def guarded(p):
            async with sem:
                try:
                    await self.make_clip(api, p)
                except Exception as e:
                    log(f"clip plan {p['id']} ECHEC {repr(e)[:300]}")

        await asyncio.gather(*[guarded(p) for p in self.ep["plans"] if p.get("persos")])

    # ── voix constantes ──
    def step_voix(self):
        """Pour chaque personnage : la prise de reference est celle qui ressemble le plus aux autres (ou celle
        fixee dans episode.json « voix_ref »), et toutes les autres repliques sont converties vers elle."""
        voix = os.path.join(HERE, "voix.py")
        by_char = {}
        for p in self.ep["plans"]:
            if not p.get("parle"):
                continue
            st = self.state.get("clips", {}).get(str(p["id"]), {})
            if not st.get("done"):
                continue
            src = os.path.join(self.dir, "voix", f"p{p['id']:02d}_orig.wav")
            if not os.path.exists(src) or p["id"] in self.redo:
                run(["ffmpeg", "-loglevel", "error", "-y", "-i", os.path.join(self.dir, "clips", f"p{p['id']:02d}.mp4"),
                     "-vn", "-ac", "1", "-ar", "24000", src])
            by_char.setdefault(p["parle"], []).append((p["id"], src))
        report = self.state.setdefault("voix", {})
        for char, items in by_char.items():
            paths = [s for _, s in items]
            sims = json.loads(run([VOIX_PYTHON, voix, "ressemblance", "--json", *paths])) if len(paths) > 1 else [[1]]
            ref_id = self.ep.get("voix_ref", {}).get(char)
            if ref_id is None:
                mean = [sum(r) / len(r) for r in sims]
                ref_id = items[mean.index(max(mean))][0]
            ref = os.path.join(self.dir, "voix", f"p{ref_id:02d}_orig.wav")
            for pid, src in items:
                dst = os.path.join(self.dir, "voix", f"p{pid:02d}.wav")
                if os.path.exists(dst) and pid not in self.redo and report.get(char, {}).get("ref") == ref_id:
                    continue
                if pid == ref_id:
                    shutil.copy(src, dst)
                else:
                    run([VOIX_PYTHON, voix, "convertir", src, ref, dst, "--tau", "0.3"])
            conv = [os.path.join(self.dir, "voix", f"p{pid:02d}.wav") for pid, _ in items]
            after = json.loads(run([VOIX_PYTHON, voix, "ressemblance", "--json", *conv])) if len(conv) > 1 else [[1]]

            def avg(m):
                vals = [m[i][j] for i in range(len(m)) for j in range(len(m)) if i != j]
                return round(sum(vals) / len(vals), 3) if vals else 1.0

            report[char] = {"ref": ref_id, "avant": avg(sims), "apres": avg(after), "plans": [i for i, _ in items]}
            log(f"voix {char} : reference plan {ref_id}, ressemblance {report[char]['avant']} -> {report[char]['apres']}")
        self.save()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ep")
    ap.add_argument("--only", choices=["tenues", "decors", "images", "cadrage", "clips", "voix"])
    ap.add_argument("--redo", default="")
    a = ap.parse_args()
    e = Episode(a.ep, [int(x) for x in a.redo.split(",") if x])
    steps = [a.only] if a.only else ["tenues", "decors", "images", "cadrage", "clips", "voix"]
    for s in steps:
        log(f"== {s} ==")
        if s == "voix":
            e.step_voix()
        else:
            asyncio.run(getattr(e, f"step_{s}")())


if __name__ == "__main__":
    main()
