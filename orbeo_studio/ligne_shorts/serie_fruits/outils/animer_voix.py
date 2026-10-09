#!/usr/bin/env python3
"""Anime un plan directement sur sa voix clonee : LTX-2 TURBO (Space Hugging Face alexnasa/ltx-2-TURBO, GPU gratuits)
recoit l'image du plan et notre fichier voix, et fait bouger les levres sur cette voix. Pas de deformation du temps
comme dans caler.py : utile quand la replique a change et que le clip d'origine ne dit plus les memes mots.

Usage : ~/agnes-video-generator/.venv/bin/python animer_voix.py ../episodes/01_la_bague --plans 23 [--essais 1]
        [--image clips/p23_ancien.mp4@0.75]  (premiere image : un fichier, ou une image d'un clip a l'instant donne)
Entrees : images/pXX_cadre.png (ou pXX.png), voix/pXX_clone.wav, controle/voix_clonees.json, episode.json
Sorties : clips/pXX_cale.mp4 et controle/pXX_cale.json, comme caler.py (le montage les prend tels quels)
Quand le quota du jour est epuise, le script attend le delai annonce par le Space (« Try again in h:mm:ss »).
"""
import argparse, json, os, re, shutil, subprocess, sys, time

from caler import FPS, LEAD, TAIL, respirer

SPACE = "alexnasa/ltx-2-TURBO"
W, H = 576, 1024


def prompt(ep, p):
    desc = ep["persos"][p["persos"][0]]
    return (f"Static camera, the framing does not change. {desc}. {p['jeu']}, in French, with "
            f"{ep['voix'][p['parle']]}. The lips move in sync with the voice. Only this character speaks. "
            f"No subtitles, no text. {ep['style']}.")


def attendre_quota(msg):
    m = re.search(r"Try again in (\d+):(\d+):(\d+)", msg)
    secs = (int(m[1]) * 3600 + int(m[2]) * 60 + int(m[3]) + 60) if m else 900
    print(f"quota Hugging Face epuise, nouvel essai dans {secs // 60} min", flush=True)
    time.sleep(secs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ep")
    ap.add_argument("--plans", required=True)
    ap.add_argument("--essais", type=int, default=1)
    ap.add_argument("--image", default="", help="premiere image (chemin relatif a l'episode, ou clip.mp4@secondes)")
    a = ap.parse_args()
    d = os.path.abspath(a.ep)
    ep = json.load(open(os.path.join(d, "episode.json"), encoding="utf-8"))
    clones = json.load(open(os.path.join(d, "controle", "voix_clonees.json")))
    reglages = ep.get("montage", {})
    tempos = reglages.get("tempo_voix", 1.0)
    tempos = tempos if isinstance(tempos, dict) else {"*": tempos}
    effets = reglages.get("effets_voix", {})

    from gradio_client import Client, handle_file
    tok = os.environ.get("HF_TOKEN") or open(os.path.expanduser("~/.hf_token")).read().strip()
    client = Client(SPACE, token=tok, verbose=False)

    for pid in [int(x) for x in a.plans.split(",")]:
        p = next(q for q in ep["plans"] if q["id"] == pid)
        key = str(pid)
        img = os.path.join(d, "images", f"p{pid:02d}_cadre.png")
        if not os.path.exists(img):
            img = os.path.join(d, "images", f"p{pid:02d}.png")
        if a.image:
            src, _, at = a.image.partition("@")
            img = os.path.join(d, src)
            if at:  # une image d'un clip existant (meme personnage, meme decor, deja valides)
                frame = os.path.join(d, "images", f"p{pid:02d}_depart.png")
                subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", at, "-i", img, "-frames:v", "1", frame],
                               check=True)
                img = frame
        wav = os.path.join(d, "voix", f"p{pid:02d}_clone.wav")
        # 1. la voix au rythme de l'episode, avec la marge avant et apres la parole
        tempo = float(tempos.get(p["parle"], tempos.get("*", 1.0)))
        lent = os.path.join(d, "voix", f"p{pid:02d}_clone_rythme.wav")
        words = respirer(wav, lent, p["replique"].split(), clones[key]["words"], tempo, bool(reglages.get("pauses")),
                         effets.get(p["parle"], ""))
        t0 = max(0.0, words[0]["start"] - LEAD)
        n_out = int(round((words[-1]["end"] + TAIL - t0) * FPS))
        dur = n_out / FPS
        voix = os.path.join(d, "voix", f"p{pid:02d}_anime.wav")
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", f"{t0:.3f}", "-i", lent, "-af", "apad",
                        "-t", f"{dur:.3f}", "-ar", "48000", voix], check=True)
        # 2. la video, levres sur cette voix
        for k in range(a.essais):
            out = os.path.join(d, "clips", f"p{pid:02d}_turbo{k + 1}.mp4")
            t = time.time()
            for essai in range(8):
                try:
                    f = handle_file(img)
                    v = client.predict(f, f, prompt(ep, p), None, "Image-to-Video", False, 0, True, H, W, "Static",
                                       handle_file(voix), api_name="/generate_video")
                    break
                except Exception as e:
                    if "quota" in str(e).lower():
                        attendre_quota(str(e))
                    elif essai < 7:  # ce Space masque ses erreurs (souvent le quota) : on reessaie plus tard
                        print(f"erreur du Space ({type(e).__name__}), nouvel essai dans 10 min", flush=True)
                        time.sleep(600)
                        client = Client(SPACE, token=tok, verbose=False)
                    else:
                        raise
            v = v.get("video") if isinstance(v, dict) else v
            shutil.copy(v, out)
            print(f"plan {pid} essai {k + 1} : {time.time() - t:.0f} s -> {out}", flush=True)
        # 3. le meme format que caler.py : image du premier essai, notre voix, duree exacte
        final = os.path.join(d, "clips", f"p{pid:02d}_cale.mp4")
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", os.path.join(d, "clips", f"p{pid:02d}_turbo1.mp4"),
                        "-i", voix, "-map", "0:v", "-map", "1:a", "-vf", f"fps={FPS},tpad=stop_mode=clone:stop_duration=1",
                        "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "aac",
                        "-b:a", "192k", "-t", f"{dur:.3f}", final], check=True)
        w2 = [{"word": x["word"], "start": round(x["start"] - t0, 2), "end": round(x["end"] - t0, 2)} for x in words]
        info = {"words": w2, "speech": [w2[0]["start"], w2[-1]["end"]], "duration": round(dur, 3),
                "moteur": "ltx-2-turbo sur la voix", "essais": a.essais}
        json.dump(info, open(os.path.join(d, "controle", f"p{pid:02d}_cale.json"), "w"), ensure_ascii=False)
        # le plan devient « fait » pour le montage (state.json), avec ce clip comme meilleur essai
        sp = os.path.join(d, "state.json")
        st = json.load(open(sp))
        cs = st.setdefault("clips", {}).setdefault(key, {"tries": []})
        cs["tries"].append({"file": f"p{pid:02d}_turbo1.mp4", "engine": "turbo-voix", "duration": round(dur, 3),
                            "words": w2, "speech": info["speech"], "sim": 1.0, "bad_frames": 0, "score": 1.0})
        cs.update(done=True, best=f"p{pid:02d}_turbo1.mp4")
        json.dump(st, open(sp, "w"), ensure_ascii=False, indent=1)
        print(f"plan {pid} : {dur:.2f} s, clip pret ({final})", flush=True)


if __name__ == "__main__":
    sys.exit(main())
