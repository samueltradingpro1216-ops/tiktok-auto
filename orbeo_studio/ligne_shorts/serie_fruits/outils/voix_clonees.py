#!/usr/bin/env python3
"""Dit chaque replique de l'episode avec la voix clonee de son personnage (profil Voicebox du meme nom),
plusieurs essais par replique, et garde le meilleur : replique bien reconnue (whisper), voix la plus proche de la
reference (Resemblyzer), debit vif.

Usage : ~/ace-venv/bin/python voix_clonees.py ../episodes/01_la_bague [--essais 2] [--plans 1,4]
Sortie : EPISODE/voix/pXX_clone.wav et EPISODE/controle/voix_clonees.json (mots minutes de chaque replique)
Le serveur Voicebox doit tourner (VOICEBOX_URL, par defaut http://127.0.0.1:17493).
"""
import argparse, difflib, json, os, re, shutil, time, unicodedata

import numpy as np
import requests

VB = os.environ.get("VOICEBOX_URL", "http://127.0.0.1:17493")
REFS = os.environ.get("VOIX_REFERENCES", "")  # dossier des voix de reference (hors depot)


def norm(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return " ".join(re.sub(r"[^a-z0-9 ]+", " ", t).split())


def generate(profile_id, text, seed):
    r = requests.post(f"{VB}/generate", json={"profile_id": profile_id, "text": text, "language": "fr",
                                              "engine": "chatterbox", "seed": seed}, timeout=60).json()
    gid = r["id"]
    for _ in range(400):
        h = requests.get(f"{VB}/history/{gid}", timeout=30).json()
        if h.get("status") in ("completed", "failed", "error"):
            break
        time.sleep(2)
    if h.get("status") != "completed":
        raise RuntimeError(f"generation {gid} : {h.get('status')} {h.get('error')}")
    return requests.get(f"{VB}/audio/{gid}", timeout=60).content


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ep")
    ap.add_argument("--essais", type=int, default=2)
    ap.add_argument("--plans", default="")
    a = ap.parse_args()
    d = os.path.abspath(a.ep)
    ep = json.load(open(os.path.join(d, "episode.json"), encoding="utf-8"))
    os.makedirs(os.path.join(d, "voix"), exist_ok=True)
    os.makedirs(os.path.join(d, "controle"), exist_ok=True)
    profiles = {p["name"]: p["id"] for p in requests.get(f"{VB}/profiles", timeout=30).json()}

    from faster_whisper import WhisperModel
    from resemblyzer import VoiceEncoder, preprocess_wav
    wm = WhisperModel("small", device="cpu", compute_type="int8")
    enc = VoiceEncoder("cpu")
    ref_emb = {}
    for name in profiles:
        p = os.path.join(REFS, f"{name}_reference.wav")
        if os.path.exists(p):
            ref_emb[name] = enc.embed_utterance(preprocess_wav(p))

    report_path = os.path.join(d, "controle", "voix_clonees.json")
    report = json.load(open(report_path)) if os.path.exists(report_path) else {}
    only = {int(x) for x in a.plans.split(",") if x}
    for p in ep["plans"]:
        if not p.get("parle") or (only and p["id"] not in only):
            continue
        key = str(p["id"])
        out = os.path.join(d, "voix", f"p{p['id']:02d}_clone.wav")
        if key in report and os.path.exists(out) and not only:
            continue
        char = p["parle"]
        cands = []
        for k in range(a.essais):
            tmp = os.path.join(d, "voix", f"p{p['id']:02d}_clone_e{k + 1}.wav")
            try:
                open(tmp, "wb").write(generate(profiles[char], p["replique"], seed=1000 + 37 * k + p["id"]))
            except Exception as e:
                print(f"plan {p['id']} essai {k + 1} ECHEC {e}", flush=True)
                continue
            segs, _ = wm.transcribe(tmp, language="fr", word_timestamps=True, beam_size=5)
            words = [{"word": w.word.strip(), "start": round(w.start, 2), "end": round(w.end, 2)}
                     for s in segs for w in (s.words or [])]
            text = " ".join(w["word"] for w in words)
            sim = max(difflib.SequenceMatcher(None, norm(text), norm(p["replique"])).ratio(),
                      difflib.SequenceMatcher(None, norm(text), norm(p.get("sous_titre", p["replique"]))).ratio())
            voix = float(np.dot(enc.embed_utterance(preprocess_wav(tmp)), ref_emb[char])) if char in ref_emb else 0.0
            dur = (words[-1]["end"] - words[0]["start"]) if words else 99
            rate = len(p["replique"].split()) / max(dur, 0.3)
            score = sim + 0.5 * voix + 0.05 * min(rate, 5)
            cands.append({"file": tmp, "sim": round(sim, 2), "voix": round(voix, 3), "mots_s": round(rate, 2),
                          "texte": text, "words": words, "score": round(score, 3)})
            print(f"plan {p['id']} ({char}) essai {k + 1} : sim={sim:.2f} voix={voix:.3f} {rate:.1f} mots/s « {text} »",
                  flush=True)
        if not cands:
            continue
        best = max(cands, key=lambda c: c["score"])
        shutil.copy(best["file"], out)
        report[key] = {k: v for k, v in best.items() if k != "file"}
        report[key]["essais"] = [{k: v for k, v in c.items() if k not in ("words", "file")} for c in cands]
        json.dump(report, open(report_path, "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
