#!/usr/bin/env python3
"""Genere la chanson d'un episode avec ACE-Step 1.5 (open source, Apache 2.0), en local.

Usage : python gen_song.py paroles.txt sortie_dir --duration 100 --bpm 100 [--batch 2] [--lm]
Tourne sur CPU (lent), GPU CUDA ou Mac Apple Silicon (MPS).
"""

import argparse
import os
import sys
import time

ACESTEP_DIR = os.environ.get("ACESTEP_DIR", os.path.expanduser("~/acestep"))
sys.path.insert(0, ACESTEP_DIR)

import torch  # noqa: E402
from acestep.handler import AceStepHandler  # noqa: E402
from acestep.inference import GenerationConfig, GenerationParams, generate_music  # noqa: E402
from acestep.llm_inference import LLMHandler  # noqa: E402

CAPTION = ("French children's nursery rhyme, cheerful and playful, warm gentle young female lead vocal singing "
           "clearly in French, ukulele, glockenspiel, soft piano, light percussion, hand claps, simple catchy "
           "melody, major key, bright and cozy, preschool song")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("lyrics")
    p.add_argument("out")
    p.add_argument("--duration", type=float, default=100)
    p.add_argument("--bpm", type=int, default=100)
    p.add_argument("--batch", type=int, default=2)
    p.add_argument("--caption", default=CAPTION)
    p.add_argument("--lm", action="store_true", help="utilise le modele de langage 5Hz (meilleur, plus lent)")
    p.add_argument("--seed", type=int, default=-1)
    a = p.parse_args()

    device = "cuda" if torch.cuda.is_available() else ("mps" if torch.backends.mps.is_available() else "cpu")
    ckpt = os.path.join(ACESTEP_DIR, "checkpoints")
    t0 = time.time()
    dit = AceStepHandler()
    print(dit.initialize_service(project_root=ACESTEP_DIR, config_path="acestep-v15-turbo", device=device))
    llm = LLMHandler()
    if a.lm:
        print(llm.initialize(checkpoint_dir=ckpt, lm_model_path="acestep-5Hz-lm-1.7B", backend="pt", device=device))
    print(f"modeles charges en {time.time() - t0:.0f} s sur {device}")

    with open(a.lyrics, encoding="utf-8") as f:
        lyrics = f.read()
    params = GenerationParams(caption=a.caption, lyrics=lyrics, vocal_language="fr", bpm=a.bpm,
                              duration=a.duration, keyscale="C major", timesignature="4",
                              thinking=a.lm, seed=a.seed)
    config = GenerationConfig(batch_size=a.batch, audio_format="wav")
    os.makedirs(a.out, exist_ok=True)
    t0 = time.time()
    res = generate_music(dit, llm, params, config, save_dir=a.out)
    print(f"generation en {time.time() - t0:.0f} s, succes={res.success} {res.error or ''}")
    for au in res.audios or []:
        print("AUDIO", au.get("path"))


if __name__ == "__main__":
    main()
