"""Parades au melange d'attributs : (a) interdiction explicite, (b) personnages ajoutes un par un."""
import asyncio, os, sys, time
sys.path.insert(0, os.path.expanduser("~/agnes-video-generator"))
os.environ.setdefault("AGNES_API_KEY", open(os.path.expanduser("~/.agnes_key")).read().strip())
from core.api.agnes_image import AgnesImageAPI

D = sys.argv[1]
STYLE = ("needle-felted wool stop-motion animation look, soft fuzzy wool and felt textures, handmade miniature set, "
         "warm soft light, cozy night")
J = lambda n: os.path.join(D, n)

async def gen(api, name, refs, prompt):
    t = time.time()
    img = await api.generate_single_image(prompt=prompt, reference_image_paths=[J(r) for r in refs], size="1344x768")
    await img.save(J(name + ".png"))
    print(f"{name} ok {time.time() - t:.0f}s", flush=True)

async def main():
    api = AgnesImageAPI(api_key=os.environ["AGNES_API_KEY"])
    for k in (1, 2):
        await gen(api, f"parade_a_{k}", ["jardin_vide.png", "luciole_laine.png", "picotine_laine.png"],
                  f"{STYLE}. Same garden as the first image. The firefly from the second image (same design) hovers "
                  "above the little hedgehog from the third image (same design, sage-green rounded spines), who looks "
                  "worried at a big shadow on the tree stump. The hedgehog has NO antennae and nothing on her head: "
                  "only the firefly has antennae. Exactly one firefly and one hedgehog. Wide 16:9 shot, no text.")
    for k in (1, 2):
        await gen(api, f"parade_b_etape1_{k}", ["jardin_vide.png", "picotine_laine.png"],
                  f"{STYLE}. Same garden as the first image. The little hedgehog from the second image (same design, "
                  "sage-green rounded spines) stands near the pond and looks worried at a big shadow on the tree "
                  "stump. Leave empty space in the air above her. Exactly one hedgehog. Wide 16:9 shot, no text.")
        await gen(api, f"parade_b_{k}", [f"parade_b_etape1_{k}.png", "luciole_laine.png"],
                  f"{STYLE}. Keep the first image exactly as it is (same garden, same hedgehog, same pose). Add the "
                  "firefly from the second image (same design) hovering in the air above the hedgehog, glowing softly. "
                  "Do not change the hedgehog. Exactly one firefly and one hedgehog. No text.")

asyncio.run(main())
