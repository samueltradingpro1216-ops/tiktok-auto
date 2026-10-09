#!/usr/bin/env python3
"""Fabrique la voix de reference d'un personnage a partir d'une voix de synthese partagee par plusieurs comptes
(groupes de voix de grappes.py), et la depose dans Voicebox comme profil clone.

Regles : seulement des voix presentes chez au moins 2 comptes sans lien (donc une voix de generateur, jamais la
vraie voix d'un createur) ; l'audio des autres comptes ne sert que de modele et n'est jamais publie.

Usage : ~/ace-venv/bin/python voix_reference.py DOSSIER_ANALYSE personnage=groupe [personnage=groupe ...]
  DOSSIER_ANALYSE contient repliques.json, voix_partagees.json et sep/htdemucs/<video>/vocals.wav
Sortie : serie_fruits/voix/<personnage>_reference.wav (+ .txt) et un profil Voicebox « <personnage> » (francais).
"""
import json, os, subprocess, sys
import numpy as np, requests

VB = os.environ.get("VOICEBOX_URL", "http://127.0.0.1:17493")
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("VOIX_REFERENCES", os.path.join(HERE, "..", "voix"))  # hors depot de preference
SR = 24000


def load(path, a, b):
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-ss", f"{a:.2f}", "-to", f"{b:.2f}", "-i", path,
                          "-ac", "1", "-ar", str(SR), "-af", "highpass=f=70", "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32)


def main():
    d = sys.argv[1]
    rows = json.load(open(os.path.join(d, "repliques.json")))
    groups = {g["voix"]: g for g in json.load(open(os.path.join(d, "voix_partagees.json")))}
    os.makedirs(OUT, exist_ok=True)
    profiles = {p["name"]: p for p in requests.get(f"{VB}/profiles").json()}
    for spec in sys.argv[2:]:
        name, gid = spec.split("=")
        g = groups[int(gid)]
        assert len(g["comptes"]) >= 2, "voix presente chez un seul compte : refusee"
        idx = g["idx"]
        E = np.array([rows[i]["emb"] for i in idx])
        c = E.mean(0) / np.linalg.norm(E.mean(0))
        # les repliques les plus typiques de la voix d'abord, assez longues et bien voisees
        order = sorted(idx, key=lambda i: -float(np.dot(rows[i]["emb"], c)))
        parts, texts, total = [], [], 0.0
        for i in order:
            r = rows[i]
            if r["fin"] - r["debut"] < 1.5 or not r["f0"]:
                continue
            x = load(os.path.join(d, "sep", "htdemucs", r["video"], "vocals.wav"), r["debut"], r["fin"])
            x = x / (np.sqrt(np.mean(x ** 2)) + 1e-6) * 0.08
            parts += [x, np.zeros(int(0.25 * SR), np.float32)]
            texts.append(r["texte"])
            total += r["fin"] - r["debut"]
            if total >= 12:
                break
        y = np.concatenate(parts)
        y = (y / max(np.abs(y).max(), 1e-6) * 0.9).astype(np.float32)
        wav = os.path.join(OUT, f"{name}_reference.wav")
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-",
                        wav], input=y.tobytes(), check=True)
        text = " ".join(texts)
        open(wav[:-4] + ".txt", "w", encoding="utf-8").write(
            f"voix partagee n°{gid}, comptes : {', '.join(g['comptes'])}\n{text}\n")
        if name in profiles:
            requests.delete(f"{VB}/profiles/{profiles[name]['id']}")
        p = requests.post(f"{VB}/profiles", json={"name": name, "language": "fr", "voice_type": "cloned",
                                                  "default_engine": "chatterbox",
                                                  "description": f"voix partagee {gid}"}).json()
        with open(wav, "rb") as f:
            s = requests.post(f"{VB}/profiles/{p['id']}/samples", files={"file": (os.path.basename(wav), f, "audio/wav")},
                              data={"reference_text": text[:1000]})
        print(f"{name}: {total:.1f} s de reference ({len(texts)} repliques, comptes {', '.join(g['comptes'])}) -> "
              f"profil {p['id']} {s.status_code}", flush=True)


if __name__ == "__main__":
    main()
