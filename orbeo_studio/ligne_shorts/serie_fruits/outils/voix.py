#!/usr/bin/env python3
"""Voix constantes : convertit la voix d'un plan vers la voix de reference du personnage (OpenVoice V2, MIT),
en gardant exactement le rythme (donc les levres generees par Agnes restent synchronisees).

Usage :
  python voix.py convertir source.wav reference1.wav[,reference2.wav] sortie.wav [--tau 0.3]
  python voix.py ressemblance [--json] a.wav b.wav [c.wav ...]   # empreinte vocale (Resemblyzer), 1 = meme voix
  python voix.py hauteur a.wav                    # hauteur mediane de la voix (Hz)
  python voix.py decaler source.wav sortie.wav -3  # baisse (ou monte) la voix de N demi-tons, meme duree
Variables : OPENVOICE_SRC (code source OpenVoice), OPENVOICE_CKPT (dossier converter/).
"""
import os
import sys
import types

import numpy as np


def converter():
    src = os.environ.get("OPENVOICE_SRC")
    sys.path.insert(0, src)
    # le module texte d'OpenVoice (pour sa propre synthese vocale) n'est pas utile a la conversion
    stub = types.ModuleType("openvoice.text")
    stub.text_to_sequence = lambda *a, **k: []
    sys.modules["openvoice.text"] = stub
    from openvoice.api import OpenVoiceBaseClass, ToneColorConverter
    ck = os.environ.get("OPENVOICE_CKPT")
    # sans filigrane audio (wavmark) : le constructeur d'OpenVoice ne sait pas le desactiver proprement
    tc = ToneColorConverter.__new__(ToneColorConverter)
    OpenVoiceBaseClass.__init__(tc, os.path.join(ck, "config.json"), device="cpu")
    tc.watermark_model = None
    tc.version = getattr(tc.hps, "_version_", "v1")
    tc.load_ckpt(os.path.join(ck, "checkpoint.pth"))
    return tc


def convertir(source, refs, out, tau=0.3):
    tc = converter()
    src_se = tc.extract_se([source])
    tgt_se = tc.extract_se(refs)
    tc.convert(audio_src_path=source, src_se=src_se, tgt_se=tgt_se, output_path=out, tau=tau)
    return out


def ressemblance(paths):
    from resemblyzer import VoiceEncoder, preprocess_wav
    enc = VoiceEncoder("cpu")
    embs = [enc.embed_utterance(preprocess_wav(p)) for p in paths]
    m = np.array([[float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))) for b in embs] for a in embs])
    return m


def hauteur(path):
    import librosa
    y, sr = librosa.load(path, sr=16000)
    f0, voiced, _ = librosa.pyin(y, fmin=60, fmax=600, sr=sr, frame_length=1024)
    f0 = f0[voiced & ~np.isnan(f0)]
    return float(np.median(f0)) if len(f0) else 0.0


def decaler(source, out, demi_tons):
    import subprocess
    ratio = 2 ** (float(demi_tons) / 12)
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", source, "-af",
                    f"rubberband=pitch={ratio:.5f}:formant=preserved:pitchq=quality", out], check=True)
    return out


if __name__ == "__main__":
    if sys.argv[1] == "hauteur":
        print(f"{hauteur(sys.argv[2]):.1f}")
    elif sys.argv[1] == "decaler":
        print(decaler(sys.argv[2], sys.argv[3], sys.argv[4]))
    elif sys.argv[1] == "convertir":
        tau = float(sys.argv[sys.argv.index("--tau") + 1]) if "--tau" in sys.argv else 0.3
        print(convertir(sys.argv[2], sys.argv[3].split(","), sys.argv[4], tau))
    elif sys.argv[1] == "ressemblance":
        paths = [p for p in sys.argv[2:] if p != "--json"]
        m = ressemblance(paths)
        if "--json" in sys.argv:
            import json
            print(json.dumps([[round(float(x), 4) for x in row] for row in m]))
            sys.exit(0)
        names = [os.path.basename(p) for p in paths]
        for n, row in zip(names, m):
            print(f"{n[:28]:28} " + " ".join(f"{x:.3f}" for x in row))
