#!/usr/bin/env python3
"""Genere la chanson d'un episode avec ACE-Step 1.5 (open source, Apache 2.0), en local.

Deux passes dans deux processus separes (le modele de langage et le modele musical ne tiennent pas
ensemble en memoire sur une machine sans GPU) :
  1. modele de langage 5Hz : structure, melodie et "codes audio" a partir des paroles
  2. modele musical (DiT) : rend l'audio a partir de ces codes

Usage : python gen_song.py paroles.txt sortie_dir --duration 100 --bpm 100 [--takes 2] [--no-lm]
Tourne sur CPU (lent), GPU CUDA ou Mac Apple Silicon (MPS).
"""

import argparse
import json
import os
import subprocess
import sys
import time

ACESTEP_DIR = os.environ.get("ACESTEP_DIR", os.path.expanduser("~/acestep"))
sys.path.insert(0, ACESTEP_DIR)

CAPTION = ("French children's nursery rhyme, cheerful and playful, warm gentle young female lead vocal singing "
           "clearly in French, ukulele, glockenspiel, soft piano, light percussion, hand claps, simple catchy "
           "melody, major key, bright and cozy, preschool song")


def device():
    import torch
    return "cuda" if torch.cuda.is_available() else ("mps" if torch.backends.mps.is_available() else "cpu")


def stage_lm(a, codes_path):
    from acestep.llm_inference import LLMHandler
    llm = LLMHandler()
    print(llm.initialize(checkpoint_dir=os.path.join(ACESTEP_DIR, "checkpoints"),
                         lm_model_path=os.environ.get("ACESTEP_LM", "acestep-5Hz-lm-0.6B"),
                         backend="pt", device=device()))
    lyrics = open(a.lyrics, encoding="utf-8").read()
    t0 = time.time()
    res = llm.generate_with_stop_condition(
        caption=a.caption, lyrics=lyrics, infer_type="llm_dit", target_duration=a.duration,
        user_metadata={"bpm": a.bpm, "keyscale": a.key, "timesignature": "4", "duration": int(a.duration)},
        use_cot_caption=False, use_cot_language=False, use_cot_metas=False,
        batch_size=a.takes, seeds=[a.seed + i for i in range(a.takes)] if a.seed >= 0 else None)
    if not res.get("success"):
        raise SystemExit(f"LM : {res.get('error')}")
    codes = res["audio_codes"] if a.takes > 1 else [res["audio_codes"]]
    json.dump({"codes": codes}, open(codes_path, "w"))
    print(f"codes generes en {time.time() - t0:.0f} s")


def stage_dit(a, codes_path):
    from acestep.handler import AceStepHandler
    from acestep.inference import GenerationConfig, GenerationParams, generate_music
    dev = device()
    dit = AceStepHandler()
    # decodage audio par petits morceaux : evite de saturer la memoire sur CPU
    chunk = int(os.environ.get("ACESTEP_DECODE_CHUNK", "32" if dev == "cpu" else "0"))
    if chunk:
        dit._get_auto_decode_chunk_size = lambda: chunk
    print(dit.initialize_service(project_root=ACESTEP_DIR, config_path="acestep-v15-turbo", device=dev))
    lyrics = open(a.lyrics, encoding="utf-8").read()
    codes = json.load(open(codes_path))["codes"] if codes_path else [""] * a.takes
    os.makedirs(a.out, exist_ok=True)
    for i, c in enumerate(codes):
        if os.path.exists(os.path.join(a.out, f"prise_{i + 1}.wav")):
            continue  # prise deja rendue (reprise apres interruption)
        params = GenerationParams(caption=a.caption, lyrics=lyrics, vocal_language="fr", bpm=a.bpm,
                                  keyscale=a.key, timesignature="4", duration=a.duration, thinking=False,
                                  audio_codes=c, use_cot_caption=False, use_cot_language=False,
                                  use_cot_metas=False)
        t0 = time.time()
        res = generate_music(dit, None, params, GenerationConfig(batch_size=1, audio_format="wav"),
                             save_dir=a.out)
        for au in res.audios or []:
            dst = os.path.join(a.out, f"prise_{i + 1}.wav")
            os.replace(au["path"], dst)
            print(f"AUDIO {dst} ({time.time() - t0:.0f} s)")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("lyrics")
    p.add_argument("out")
    p.add_argument("--duration", type=float, default=100)
    p.add_argument("--bpm", type=int, default=100)
    p.add_argument("--key", default="C major")
    p.add_argument("--takes", type=int, default=2)
    p.add_argument("--caption", default=CAPTION)
    p.add_argument("--seed", type=int, default=-1)
    p.add_argument("--no-lm", action="store_true")
    p.add_argument("--stage", choices=["lm", "dit"])
    p.add_argument("--codes")
    a = p.parse_args()

    if a.stage == "lm":
        return stage_lm(a, a.codes)
    if a.stage == "dit":
        return stage_dit(a, a.codes)
    os.makedirs(a.out, exist_ok=True)
    codes = None
    base = [sys.executable, __file__, a.lyrics, a.out, "--duration", str(a.duration), "--bpm", str(a.bpm),
            "--key", a.key, "--takes", str(a.takes), "--caption", a.caption, "--seed", str(a.seed)]
    if not a.no_lm:
        codes = os.path.join(a.out, "codes.json")
        subprocess.run(base + ["--stage", "lm", "--codes", codes], check=True)
    subprocess.run(base + ["--stage", "dit"] + (["--codes", codes] if codes else []), check=True)


if __name__ == "__main__":
    main()
