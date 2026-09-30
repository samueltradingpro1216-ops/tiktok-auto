#!/usr/bin/env python3
"""Prolonge la fin d'une chanson ACE-Step (repaint de la fin sur un audio rallonge de silence).

Usage : python extend_song.py chanson.wav paroles.txt sortie.wav --repaint-from 88 --total 112 --bpm 92
"""
import argparse
import os
import subprocess
import sys

ACESTEP_DIR = os.environ.get("ACESTEP_DIR", os.path.expanduser("~/acestep"))
sys.path.insert(0, ACESTEP_DIR)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_song import CAPTION, device  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("src"); p.add_argument("lyrics"); p.add_argument("out")
p.add_argument("--repaint-from", type=float, required=True)
p.add_argument("--total", type=float, required=True)
p.add_argument("--bpm", type=int, default=92)
p.add_argument("--caption", default=CAPTION)
a = p.parse_args()

padded = a.out + ".padded.wav"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", a.src, "-af", f"apad=whole_dur={a.total}", padded], check=True)
from acestep.handler import AceStepHandler  # noqa: E402
from acestep.inference import GenerationConfig, GenerationParams, generate_music  # noqa: E402
dev = device()
dit = AceStepHandler()
if dev == "cpu":  # encodage/decodage par petits morceaux : evite de saturer la memoire
    dit._get_auto_decode_chunk_size = lambda: 32
    _enc = dit.tiled_encode
    dit.tiled_encode = lambda audio, chunk_size=None, overlap=None, offload_latent_to_cpu=True: _enc(
        audio, chunk_size=48000 * 4, overlap=1920 * 10, offload_latent_to_cpu=offload_latent_to_cpu)
print(dit.initialize_service(project_root=ACESTEP_DIR, config_path="acestep-v15-turbo", device=dev))
params = GenerationParams(task_type="repaint", src_audio=padded, repainting_start=a.repaint_from,
                          repainting_end=-1, chunk_mask_mode="explicit", caption=a.caption,
                          lyrics=open(a.lyrics, encoding="utf-8").read(), vocal_language="fr", bpm=a.bpm,
                          keyscale="C major", timesignature="4", duration=a.total, thinking=False,
                          use_cot_caption=False, use_cot_language=False, use_cot_metas=False)
res = generate_music(dit, None, params, GenerationConfig(batch_size=1, audio_format="wav"),
                     save_dir=os.path.dirname(os.path.abspath(a.out)))
os.replace(res.audios[0]["path"], a.out)
os.remove(padded)
print("AUDIO", a.out)
