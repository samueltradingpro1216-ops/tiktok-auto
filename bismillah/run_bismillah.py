#!/usr/bin/env python3
"""Genere la comptine "Bismillah" (7 scenes x 10 s) avec Agnes Video Generator.

Prerequis :
  1. git clone https://github.com/lcy362/agnes-video-generator.git
  2. cd agnes-video-generator && export AGNES_API_KEY="ta-cle" && ./start.sh
  3. Dans un autre terminal : python3 run_bismillah.py

Le script envoie une tache "Creative" au serveur local (http://localhost:8765),
puis affiche la progression jusqu'a la video finale.
"""

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

SERVER = os.environ.get("AGNES_SERVER", "http://localhost:8765")
HERE = os.path.dirname(os.path.abspath(__file__))
SCENE_COUNT = 7
SCENE_SECONDS = 10


def post_form(path, fields):
    data = urllib.parse.urlencode(fields).encode()
    req = urllib.request.Request(SERVER + path, data=data, method="POST")
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def get_json(path):
    with urllib.request.urlopen(SERVER + path, timeout=60) as resp:
        return json.load(resp)


def main():
    with open(os.path.join(HERE, "idee.txt"), encoding="utf-8") as f:
        idea = f.read()

    fields = {
        "idea": idea,
        "creative_name": "bismillah_comptine",
        "style": "Animation 3D style Pixar, douce, couleurs pastel, dessin anime pour enfants",
        "chaining_mode": "keyframes",
        "video_width": 768,
        "video_height": 1152,
        "duration_source": "manual",
        "scene_count": SCENE_COUNT,
        "uniform_duration": "true",
        "scene_durations_json": json.dumps([SCENE_SECONDS] * SCENE_COUNT),
        "audio_enabled": "true",
        "audio_voice": os.environ.get("BISMILLAH_VOICE", "fr-FR-EloiseNeural"),
        "audio_rate": "-5%",
        "audio_lang": "fr",
        "subtitle_enabled": "true",
        "subtitle_position": "bottom",
    }

    try:
        task = post_form("/api/tasks/creative", fields)
    except urllib.error.HTTPError as e:
        sys.exit(f"Erreur a la creation de la tache ({e.code}) : {e.read().decode()}")
    except urllib.error.URLError:
        sys.exit(f"Serveur injoignable sur {SERVER} : lance d'abord ./start.sh")

    task_id = task["task_id"]
    print(f"Tache creee : {task_id} (dossier {task.get('dir_name')})")

    while True:
        state = get_json(f"/api/tasks/{task_id}")
        status = state.get("current_status") or state.get("status")
        progress = state.get("current_progress") or 0
        print(f"[{time.strftime('%H:%M:%S')}] {status} {progress:.0%}", flush=True)
        final = state.get("final_video_path") or state.get("final_video_file")
        if final:
            print(f"\nVideo finale : {final}")
            return
        if status in ("failed", "stopped"):
            sys.exit("La generation a echoue : regarde les logs du terminal de start.sh")
        time.sleep(20)


if __name__ == "__main__":
    main()
