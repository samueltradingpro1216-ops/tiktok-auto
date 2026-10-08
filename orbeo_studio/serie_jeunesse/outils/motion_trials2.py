"""Essai 2 : sans le mot « firefly » dans la consigne (v2.0), et en 2.5-flash avec la fiche en reference."""
import asyncio, os, sys, time
sys.path.insert(0, os.path.expanduser("~/agnes-video-generator"))
os.environ.setdefault("AGNES_API_KEY", open(os.path.expanduser("~/.agnes_key")).read().strip())
from core.api.agnes_video import AgnesVideoAPI

D = sys.argv[1]
STYLE = "Needle-felted wool stop-motion animation, soft fuzzy wool textures, handmade miniature set, cozy night."
HER = ("the little round lantern-shaped wool character with a glowing yellow belly, a night-blue cape speckled with "
       "star dots and two short antennae with glowing beads (she has no wings)")
JOBS = [
    ("v20", "mvt2_chambre_nino", ["chambre_nino_luciole.png"],
     f"{STYLE} Fixed camera, the camera does not move, same bedroom from start to end. The boy sitting on his bed "
     f"waves gently at {HER}, who stands at the round window and blinks her glowing belly twice. Both keep exactly "
     "the same size and design as in the image. Calm, slow motion. No text, no talking."),
    ("v20", "mvt2_jardin_luciole", ["jardin_luciole.png"],
     f"{STYLE} Fixed camera, the camera does not move, same garden from start to end. {HER[0].upper() + HER[1:]} "
     "sits on the clover leaf near the pond, looks around, then her glowing belly pulses softly three times. She "
     "keeps exactly the same size and design as in the image. Calm, slow motion. No text, no talking."),
    ("25flash", "mvt2_25flash_chambre", ["chambre_nino_luciole.png"],
     f"{STYLE} Fixed camera. In this cozy wool bedroom, the boy in coral pajamas sitting on his bed waves gently at "
     f"{HER}, who stands at the round window and blinks her glowing belly twice. Keep both characters exactly as in "
     "the reference image. Calm, slow motion. No text, no talking."),
]

async def main():
    apis = {"v20": AgnesVideoAPI(api_key=os.environ["AGNES_API_KEY"], model="agnes-video-v2.0", max_retries=2),
            "25flash": AgnesVideoAPI(api_key=os.environ["AGNES_API_KEY"], model="agnes-video-2.5-flash", max_retries=2)}
    for model, name, refs, prompt in JOBS:
        path = os.path.join(D, f"{name}.mp4")
        if os.path.exists(path):
            continue
        t = time.time()
        try:
            v = await apis[model].generate_single_video(prompt=prompt, reference_image_paths=[os.path.join(D, r) for r in refs],
                                                        duration=10, width=1280, height=720)
            await v.save(path)
            print(f"{name} ok {time.time() - t:.0f}s", flush=True)
        except Exception as e:
            print(f"{name} ECHEC {str(e)[:200]}", flush=True)

asyncio.run(main())
