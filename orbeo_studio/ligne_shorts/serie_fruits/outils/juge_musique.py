#!/usr/bin/env python3
"""Classe les prises de chaque ambiance musicale sans les ecouter : CLAP (LAION, Apache 2.0) mesure l'accord entre
l'audio et la description voulue, et penalise les defauts (voix chantee, bruit, saturation, silence).

Usage : ~/ace-venv/bin/python juge_musique.py EPISODE_DIR   -> ecrit musique/classement.json
"""
import glob
import json
import os
import sys

import numpy as np
import torch
from transformers import ClapModel, ClapProcessor

d = sys.argv[1]
ep = json.load(open(os.path.join(d, "episode.json"), encoding="utf-8"))
model = ClapModel.from_pretrained("laion/clap-htsat-unfused").eval()
proc = ClapProcessor.from_pretrained("laion/clap-htsat-unfused")
DEFAUTS = ["a person singing, vocals, lyrics", "harsh noise, distorted glitchy audio", "silence"]


def load(path):
    import subprocess
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", path, "-ac", "1", "-ar", "48000", "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32)


res = {}
for name, m in ep["musique"].items():
    texts = [m["style"]] + DEFAUTS
    with torch.no_grad():
        te = model.get_text_features(**proc(text=texts, return_tensors="pt", padding=True))
    te = te / te.norm(dim=-1, keepdim=True)
    scores = []
    for p in sorted(glob.glob(os.path.join(d, "musique", name, "prise_*.wav"))):
        x = load(p)
        chunks = [x[i:i + 48000 * 10] for i in range(0, max(len(x) - 48000 * 5, 1), 48000 * 10)]
        with torch.no_grad():
            ae = model.get_audio_features(**proc(audios=chunks, sampling_rate=48000, return_tensors="pt"))
        ae = ae / ae.norm(dim=-1, keepdim=True)
        sim = (ae @ te.T).mean(0).tolist()
        clip = float(np.mean(np.abs(x) > 0.99))
        score = sim[0] - 0.5 * max(sim[1] - sim[0] + 0.05, 0) - 0.3 * max(sim[2] - sim[0] + 0.05, 0) - 5 * clip
        scores.append({"prise": os.path.basename(p), "style": round(sim[0], 3), "voix": round(sim[1], 3),
                       "bruit": round(sim[2], 3), "silence": round(sim[3], 3), "sature": round(clip, 4),
                       "score": round(score, 3)})
    scores.sort(key=lambda s: -s["score"])
    res[name] = scores
    print(name, json.dumps(scores, ensure_ascii=False), flush=True)
json.dump(res, open(os.path.join(d, "musique", "classement.json"), "w"), ensure_ascii=False, indent=1)
