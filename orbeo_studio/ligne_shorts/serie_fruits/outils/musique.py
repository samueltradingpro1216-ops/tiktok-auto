#!/usr/bin/env python3
"""Genere les ambiances musicales d'un episode (ACE-Step 1.5, local, instrumental), une par entree « musique ».

Usage : ~/ace-venv/bin/python musique.py EPISODE_DIR [--takes 1]
Les fichiers sortent dans EPISODE_DIR/musique/<ambiance>/prise_N.wav ; le montage choisit et cale.
"""
import argparse, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(HERE, "..", "..", "..", "..", "chaine_lulu", "pipeline", "gen_song.py")

p = argparse.ArgumentParser()
p.add_argument("ep")
p.add_argument("--takes", type=int, default=1)
a = p.parse_args()
ep = json.load(open(os.path.join(a.ep, "episode.json"), encoding="utf-8"))
txt = os.path.join(a.ep, "musique", "instrumental.txt")
os.makedirs(os.path.dirname(txt), exist_ok=True)
open(txt, "w").write("[Instrumental]\n")
for name, m in ep["musique"].items():
    out = os.path.join(a.ep, "musique", name)
    if all(os.path.exists(os.path.join(out, f"prise_{i + 1}.wav")) for i in range(a.takes)):
        continue
    bpm = int(next((w for w in m["style"].replace(",", " ").split() if w.isdigit()), 90))
    subprocess.run([sys.executable, GEN, txt, out, "--duration", str(m["duree"]), "--bpm", str(bpm),
                    "--key", m.get("tonalite", "A minor"), "--takes", str(a.takes), "--caption", m["style"],
                    "--no-lm"], check=True)
    print("MUSIQUE", name, "ok", flush=True)
