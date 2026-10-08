"""Essais de dessin des personnages de la serie (2 styles x 6 personnages), avec Agnes image."""
import asyncio, os, sys, time
sys.path.insert(0, os.path.expanduser("~/agnes-video-generator"))
os.environ.setdefault("AGNES_API_KEY", open(os.path.expanduser("~/.agnes_key")).read().strip())
from core.api.agnes_image import AgnesImageAPI

OUT = sys.argv[1]
STYLES = {
    "laine": "needle-felted wool toy character, stop-motion animation look, soft fuzzy wool texture, handmade, "
             "warm soft studio light",
    "douce3d": "soft 3D animation character, simple rounded shapes, matte clay-like materials, gentle soft light, "
               "very few details",
}
COMMON = ("Full body, front view, standing, centered, plain cream background, character design reference, "
          "one single character only, no text, no logo.")
CHARS = {
    "luciole": "a small round firefly character (a beetle insect, not a fairy, not a human): a round body shaped like "
               "a little paper lantern with a softly glowing warm-yellow belly, night-blue domed wing-cases (elytra) "
               "like a tiny cape speckled with small star dots, two short thick antennae each ending in a tiny "
               "glowing bead, big round dark eyes set low on a cream face, tiny smile, stubby little arms and legs. "
               "No bow, no hair, no transparent wings.",
    "nino": "a 4-year-old boy with a big round head, fluffy chestnut hair, big brown eyes, rosy cheeks, wearing plain "
            "soft coral-red pajamas with one round cream moon patch on the chest, barefoot. No hair accessory.",
    "ronflou": "a chubby dormouse character: pear-shaped body, honey-brown fur, a huge fluffy tail as long as his "
               "body, sleepy half-closed eyes, small round ears, holding a hazelnut.",
    "bzou": "a clumsy moth character: triangular body, big powdery lilac wings shaped like a triangle, two large "
            "feathery antennae, big round surprised eyes, a fluffy white collar.",
    "picotine": "a small round hedgehog girl: a dome of soft rounded spines with a sage-green tint, a cream face, "
                "big worried eyes, tiny paws.",
    "hulotte": "an old grandmother tawny owl: oval body, soft russet-brown feathers, two small ear tufts, kind "
               "half-moon eyes behind small round spectacles.",
}

async def main():
    api = AgnesImageAPI(api_key=os.environ["AGNES_API_KEY"])
    for style, stxt in STYLES.items():
        for name, ctxt in CHARS.items():
            path = os.path.join(OUT, f"{name}_{style}.png")
            if os.path.exists(path):
                continue
            t = time.time()
            try:
                img = await api.generate_single_image(prompt=f"{stxt}. {ctxt} {COMMON}", size="1024x1024")
                await img.save(path)
                print(f"{name}_{style} ok {time.time() - t:.0f}s", flush=True)
            except Exception as e:
                print(f"{name}_{style} ECHEC {e}", flush=True)

asyncio.run(main())
