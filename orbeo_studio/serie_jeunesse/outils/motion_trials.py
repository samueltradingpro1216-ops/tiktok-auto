"""Essai du style laine en mouvement (Agnes video v2.0, image vers video, 10 s)."""
import asyncio, os, sys, time
sys.path.insert(0, os.path.expanduser("~/agnes-video-generator"))
os.environ.setdefault("AGNES_API_KEY", open(os.path.expanduser("~/.agnes_key")).read().strip())
from core.api.agnes_video import AgnesVideoAPI

D = sys.argv[1]
STYLE = "Needle-felted wool stop-motion animation, soft fuzzy wool textures, handmade miniature set, cozy night."
JOBS = [
    ("mvt_jardin_luciole", "jardin_luciole.png",
     f"{STYLE} Fixed camera, same garden from start to end. The little firefly on the clover leaf slowly lifts off, "
     "hovers in a small gentle circle above the pond and lands back on the leaf, her lantern belly glowing softly. "
     "Only one firefly, she keeps exactly the same size and design. Calm, slow motion. No text, no talking."),
    ("mvt_chambre_nino", "chambre_nino_luciole.png",
     f"{STYLE} Fixed camera, same bedroom from start to end. The boy sitting on his bed waves gently at the firefly at "
     "the round window; the firefly blinks her glowing belly twice and wiggles her antennae. Exactly one boy and one "
     "firefly, both keep the same size and design. Calm, slow motion. No text, no talking."),
]

async def main():
    api = AgnesVideoAPI(api_key=os.environ["AGNES_API_KEY"], model="agnes-video-v2.0")
    for name, ref, prompt in JOBS:
        path = os.path.join(D, f"{name}.mp4")
        if os.path.exists(path):
            continue
        t = time.time()
        try:
            v = await api.generate_single_video(prompt=prompt, reference_image_paths=[os.path.join(D, ref)],
                                                duration=10, width=1280, height=720)
            await v.save(path)
            print(f"{name} ok {time.time() - t:.0f}s", flush=True)
        except Exception as e:
            print(f"{name} ECHEC {e}", flush=True)

asyncio.run(main())
