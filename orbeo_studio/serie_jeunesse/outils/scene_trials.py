"""Essai de scenes en style laine : decor vide, puis personnages ajoutes avec leur image d'identite."""
import asyncio, os, sys, time
sys.path.insert(0, os.path.expanduser("~/agnes-video-generator"))
os.environ.setdefault("AGNES_API_KEY", open(os.path.expanduser("~/.agnes_key")).read().strip())
from core.api.agnes_image import AgnesImageAPI

D = sys.argv[1]
STYLE = ("needle-felted wool stop-motion animation look, soft fuzzy wool and felt textures, handmade miniature set, "
         "warm soft light, cozy night")
JOBS = [
    ("jardin_vide", [], f"{STYLE}. A small magical garden at night seen at insect height: a big orange physalis "
     "lantern-flower glowing softly, a small pond reflecting a round moon, an old tree stump with a round hole, "
     "tall grass and clover, deep night-blue sky with a few stars. No characters, no text. Wide 16:9 shot."),
    ("chambre_vide", [], f"{STYLE}. A cozy child's bedroom at night: a small wooden bed with a quilt, a round window "
     "showing a night garden and the moon, a little shelf with a few books, a round rug, a soft warm night glow. "
     "No characters, no mirror, no text. Wide 16:9 shot."),
]
SCENES = [
    ("jardin_luciole", ["jardin_vide.png", "luciole_laine.png"],
     f"{STYLE}. Same garden as the first image. The firefly character from the second image (exactly the same "
     "design: night-blue starry wing-cases, glowing yellow lantern belly, two short antennae with glowing beads) "
     "sits on a clover leaf near the pond, glowing softly. Only one firefly. Wide 16:9 shot, no text."),
    ("jardin_luciole_picotine", ["jardin_vide.png", "luciole_laine.png", "picotine_laine.png"],
     f"{STYLE}. Same garden as the first image. The firefly from the second image (same design) hovers above the "
     "little hedgehog from the third image (same design, sage-green rounded spines), who looks worried at a big "
     "shadow on the tree stump. Exactly one firefly and one hedgehog, nothing else. Wide 16:9 shot, no text."),
    ("chambre_nino_luciole", ["chambre_vide.png", "nino_laine.png", "luciole_laine.png"],
     f"{STYLE}. Same bedroom as the first image. The boy from the second image (same design: coral pajamas with a "
     "cream moon patch) sits on his bed and looks at the firefly from the third image (same design), who glows at "
     "the round window. Exactly one boy and one firefly. Wide 16:9 shot, no text."),
]

async def main():
    api = AgnesImageAPI(api_key=os.environ["AGNES_API_KEY"])
    for name, refs, prompt in JOBS + SCENES:
        path = os.path.join(D, f"{name}.png")
        if os.path.exists(path):
            continue
        t = time.time()
        try:
            img = await api.generate_single_image(prompt=prompt, reference_image_paths=[os.path.join(D, r) for r in refs],
                                                  size="1344x768")
            await img.save(path)
            print(f"{name} ok {time.time() - t:.0f}s", flush=True)
        except Exception as e:
            print(f"{name} ECHEC {e}", flush=True)

asyncio.run(main())
