#!/usr/bin/env python3
"""Fiche vocale de chaque replique : hauteur de voix (F0 mediane, Hz), variation, debit, et ressemblance avec les
autres repliques du meme personnage. Sert a verifier le casting sans ecouter (homme grave, femme, vieille dame...)
et a reperer une replique dont la voix change.

Usage : ~/ace-venv/bin/python analyse_voix.py EPISODE_DIR [--converties]
"""
import json
import os
import sys

import librosa
import numpy as np

d = sys.argv[1]
conv = "--converties" in sys.argv
ep = json.load(open(os.path.join(d, "episode.json"), encoding="utf-8"))
st = json.load(open(os.path.join(d, "state.json")))
rows = {}
for p in ep["plans"]:
    if not p.get("parle") or not st.get("clips", {}).get(str(p["id"]), {}).get("done"):
        continue
    best = next(x for x in st["clips"][str(p["id"])]["tries"] if x.get("file") == st["clips"][str(p["id"])]["best"])
    src = os.path.join(d, "voix", f"p{p['id']:02d}.wav") if conv else os.path.join(d, "clips", f"p{p['id']:02d}.mp4")
    if not os.path.exists(src):
        continue
    a, b = best.get("speech", [0, None])
    y, sr = librosa.load(src, sr=16000, offset=max(0, a - 0.05), duration=(b - a + 0.1) if b else None)
    f0, vf, _ = librosa.pyin(y, fmin=60, fmax=600, sr=sr, frame_length=1024)
    f0 = f0[vf & ~np.isnan(f0)]
    words = len(p["replique"].split())
    rows.setdefault(p["parle"], []).append({
        "plan": p["id"], "f0_hz": round(float(np.median(f0)), 1) if len(f0) else None,
        "f0_var": round(float(np.std(np.log2(f0))) * 12, 1) if len(f0) else None,  # en demi-tons
        "mots_s": round(words / max(b - a, 0.1), 2) if b else None, "sim_texte": best.get("sim")})
for char, r in rows.items():
    f0s = [x["f0_hz"] for x in r if x["f0_hz"]]
    print(f"{char:7} F0 mediane {np.median(f0s):6.1f} Hz (de {min(f0s):.0f} a {max(f0s):.0f})  " +
          "  ".join(f"p{x['plan']}:{x['f0_hz']}Hz/{x['mots_s']}m/s" for x in r))
json.dump(rows, open(os.path.join(d, "controle", "voix_analyse" + ("_conv" if conv else "") + ".json"), "w"), indent=1)
