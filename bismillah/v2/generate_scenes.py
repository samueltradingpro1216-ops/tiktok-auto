#!/usr/bin/env python3
"""Bismillah v2 : 7 scenes chantees en 16:9 avec le son natif d'Agnes Video 2.0.

Pour chaque scene : image de depart (avec l'image de reference des personnages),
puis clip image->video de 10 s dont le prompt contient les paroles chantees.
Le modele genere la voix et la musique, avec la bouche synchronisee.

Usage : python3 generate_scenes.py reference.png [numeros de scenes...]
(serveur Agnes Video Generator lance sur http://localhost:8765)
"""

import json
import os
import subprocess
import sys
import time

SERVER = os.environ.get("AGNES_SERVER", "http://localhost:8765")
HERE = os.path.dirname(os.path.abspath(__file__))
WORKDIR = os.environ.get("AGNES_WORKDIR", os.path.expanduser("~/agnes-video-generator/.working_dir"))

STYLE = ("Pixar-style 3D animation, soft pastel colors, warm golden light, "
         "Muslim family children's cartoon, wide 16:9 framing, no text.")
CHARACTERS = (
    "Amina: 4-year-old girl, caramel skin, big brown eyes, very curly black hair with a knotted "
    "yellow headband, pale yellow pajamas with little lilac moons and stars. "
    "Mother: gentle young woman ALWAYS wearing a light beige hijab fully covering her hair and neck, "
    "long lilac dress with puffy sleeves. "
    "Fennec: small cream fennec fox with big ears and a turquoise scarf."
)
MUSIC = ("Cheerful Islamic nursery-rhyme song for kids in French, simple catchy melody, "
         "soft daf drum, light xylophone and hand claps, clear lip-sync singing.")
NEGATIVE = ("text, subtitles, letters, watermark, deformed face, extra fingers, "
            "mother without hijab, uncovered hair on the mother, adult male")

SCENES = [
    {"image": None,  # scene 1 : on part directement de l'image de reference
     "action": "In the cozy mint-green living room, Amina looks up at her mother and sings with a sweet "
               "little-girl voice: \"Maman, pourquoi on dit toujours Bismillah ?\" Her mother, in her beige "
               "hijab, smiles tenderly and sings back softly: \"Parce qu'Allah met la baraka dans tout ce "
               "que tu fais !\" The fennec wags its tail. Slow camera push-in."},
    {"image": "Amina's pastel bedroom in the morning, sunbeams through the window. Amina sits up in her bed "
              "stretching her arms happily, the fennec jumps on the bed next to her.",
     "action": "Amina stretches, yawns, then raises her arms joyfully and sings with a sweet little-girl voice: "
               "\"Je me réveille, je me lève, j'ai faim... mais avant tout, Bismillah !\" The fennec bounces "
               "on the bed. Gentle camera move."},
    {"image": "Pastel bathroom, Amina standing on a small wooden stool at the sink, water running, shiny soap "
              "bubbles floating around, the fennec watching from the side.",
     "action": "Amina washes her hands under sparkling water, soap bubbles float, and she sings with a sweet "
               "little-girl voice: \"Je me lave les mains, toutes propres, toutes bien... mais avant tout, "
               "Bismillah !\" Close shots on her smile and the bubbles."},
    {"image": "Warm kitchen at noon, table with dates, bread, steaming soup and fruits. Amina sits at the "
              "table, her mother in beige hijab serves her with a smile, the fennec sits nearby.",
     "action": "Amina puts her hands together, smiles at her mother and sings with a sweet little-girl voice: "
               "\"Quand je mange à midi, je dis merci... mais avant tout, Bismillah !\" Then she picks a date "
               "with her right hand. Her mother, in her beige hijab, strokes her head."},
    {"image": "Bright flowery garden under a blue sky with butterflies. Amina dances and spins, her mother in "
              "beige hijab claps her hands, the fennec jumps around them.",
     "action": "Joyful chorus: Amina spins and dances with the fennec while her mother, in her beige hijab, "
               "claps along; Amina and her mother sing together happily: \"Bismillah, Bismillah, Bismillah au "
               "nom d'Allah ! Bismillah, Bismillah, au nom d'Allah !\" Circular camera move, butterflies."},
    {"image": "Cozy playroom: Amina sits on a colorful rug with a glass of water, an open picture book, "
              "crayons and a ball, the fennec playing with the ball.",
     "action": "Amina drinks some water, opens a picture book, draws with a crayon, then rolls the ball to the "
               "fennec, singing rhythmically with a sweet little-girl voice: \"Avant de boire, avant de lire, "
               "avant d'écrire, avant de jouer... Bismillah !\""},
    {"image": "Night, Amina's bedroom, starry sky and golden crescent moon through the window. Amina lies in "
              "bed, her mother wearing her beige hijab sits beside her and tucks her in, the fennec curled up "
              "at the foot of the bed, soft twinkling stars.",
     "action": "Soft lullaby: the mother, wearing her beige hijab, tucks Amina in and they sing gently "
               "together: \"N'oublie jamais, n'oublie jamais... Bismillah, au nom d'Allah.\" Amina closes "
               "her eyes smiling, her mother kisses her forehead. Slow camera pull back to the starry window."},
]


def curl_json(args):
    out = subprocess.run(["curl", "-s", "-m", "300", *args], capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def wait_file(dir_name, filename, timeout=3600):
    path = os.path.join(WORKDIR, dir_name, filename)
    state = os.path.join(WORKDIR, dir_name, "task_state.json")
    start = time.time()
    while time.time() - start < timeout:
        if os.path.exists(path):
            return path
        if os.path.exists(state):
            with open(state, encoding="utf-8") as f:
                s = json.load(f)
            if s.get("status") == "failed":
                raise RuntimeError(f"{dir_name} failed: {s.get('error_message') or s.get('error')}")
        time.sleep(15)
    raise TimeoutError(dir_name)


def main():
    ref = sys.argv[1]
    wanted = [int(x) for x in sys.argv[2:]] or list(range(1, len(SCENES) + 1))
    video_jobs = {}
    for n in wanted:
        scene = SCENES[n - 1]
        start_image = ref
        if scene["image"]:
            r = curl_json(["-X", "POST", f"{SERVER}/api/image/generate", "-F", "size=1344x768",
                           "-F", f"reference_image=@{ref}",
                           "-F", f"prompt={STYLE} {scene['image']} {CHARACTERS}"])
            start_image = wait_file(r["dir_name"], "final_image.png")
            print(f"scene {n}: image {start_image}", flush=True)
        r = curl_json(["-X", "POST", f"{SERVER}/api/tasks/simple", "-F", "mode=i2v", "-F", "duration=10",
                       "-F", "video_width=1280", "-F", "video_height=720",
                       "-F", f"reference_image=@{start_image}", "-F", f"negative_prompt={NEGATIVE}",
                       "-F", f"prompt={STYLE} {MUSIC} {scene['action']} {CHARACTERS}"])
        video_jobs[n] = r["dir_name"]
        print(f"scene {n}: video task {r['dir_name']}", flush=True)

    os.makedirs(os.path.join(HERE, "scenes"), exist_ok=True)
    for n, dir_name in video_jobs.items():
        src = wait_file(dir_name, "final_video.mp4")
        dst = os.path.join(HERE, "scenes", f"scene_{n}.mp4")
        subprocess.run(["cp", src, dst], check=True)
        print(f"scene {n}: done -> {dst}", flush=True)


if __name__ == "__main__":
    main()
