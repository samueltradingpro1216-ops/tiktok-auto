"""Orbeo TikTok line test: 2 original characters, French dialogue, vertical 9:16, Agnes API.
Usage: AGNES_API_KEY=... python tiktok_dialogue_test.py img | vid <model> <image> <name> [seconds]
Never prints the key."""
import asyncio, json, os, sys, time
sys.path.insert(0, "/root/agnes-video-generator")
os.chdir("/root/agnes-video-generator")
from core.api.agnes_image import AgnesImageAPI  # noqa: E402
from core.api.agnes_video import AgnesVideoAPI  # noqa: E402

O = "/tmp/claude-0/-home-user-tiktok-auto/c3103019-a176-5027-8bcf-8e27361d44f5/scratchpad/tests_tiktok"
KEY = os.environ["AGNES_API_KEY"]

STYLE = ("Stylized 3D animated comedy, bright cinematic lighting, expressive cartoon faces with clearly visible mouths, "
         "vertical 9:16 framing, no text, no subtitles, no logo.")
CROISSANT = ("GASTON: a grumpy golden croissant character, chubby crescent body with flaky layers, thick bushy dark "
             "eyebrows frowning, small round eyes, a big expressive mouth, short arms crossed, tiny legs.")
BAGUETTE = ("BAGUETTE: an anxious, tall thin baguette character standing upright, light-brown crust with diagonal "
            "scores, huge worried eyes, raised eyebrows, wide nervous mouth, thin arms, tiny legs.")
SCENE = ("Inside a small Parisian bakery at early morning, warm light, wooden shelves with bread loaves, a chalkboard "
         "and a window on a Paris street in the soft-focus background. On the marble counter in the foreground, "
         "exactly two characters face each other in a medium two-shot, both fully visible, same scale as each other "
         "(the baguette is twice as tall as the croissant): " + CROISSANT + " " + BAGUETTE + " Exactly one croissant "
         "and exactly one baguette, no other characters. ")

DIALOGUE = (
    "Static camera, locked-off tripod shot, the framing does not change, the two characters keep the same size. "
    "Comedic short-form sketch. Gaston the grumpy croissant (left) turns to the baguette and says in French, with a deep "
    "grumpy male voice: \"Encore en retard, Baguette !\" Then the anxious baguette (right) answers in French, with a "
    "fast, high-pitched, panicked male voice: \"Pardon ! Le four m'a fait peur !\" Only the character who is speaking "
    "moves his mouth. Ambient bakery sound, no music. " )


async def gen_image(name, prompt, refs=(), size="768x1344"):
    api = AgnesImageAPI(KEY, model="agnes-image-2.5-flash")
    t = time.time()
    try:
        out = await api.generate_single_image(prompt, reference_image_paths=list(refs), size=size)
        path = f"{O}/{name}.png"
        await out.save(path)
        print(json.dumps({"name": name, "ok": True, "s": round(time.time() - t, 1)}), flush=True)
    except Exception as e:  # noqa: BLE001
        print(json.dumps({"name": name, "ok": False, "err": str(e)[:300], "s": round(time.time() - t, 1)}), flush=True)


async def gen_video(name, model, prompt, refs, seconds=8):
    api = AgnesVideoAPI(KEY, model=model, max_retries=2, retry_base_delay=20.0)
    t = time.time()
    try:
        out = await asyncio.wait_for(api.generate_single_video(prompt, reference_image_paths=refs, duration=seconds,
                                     width=720, height=1280, seed=4242), timeout=1500)
        path = f"{O}/{name}.mp4"
        await out.save(path)
        print(json.dumps({"name": name, "model": model, "ok": True, "s": round(time.time() - t, 1)}), flush=True)
    except Exception as e:  # noqa: BLE001
        print(json.dumps({"name": name, "model": model, "ok": False, "err": repr(e)[:400],
                          "s": round(time.time() - t, 1)}), flush=True)


if __name__ == "__main__" and sys.argv[1] in ("img", "vid"):
    step = sys.argv[1]
    if step == "img":
        p = SCENE + STYLE
        async def _m():
            await asyncio.gather(gen_image("kf_bakery_1", p), gen_image("kf_bakery_2", p))
        asyncio.run(_m())
    elif step == "vid":
        model, img, name = sys.argv[2], sys.argv[3], sys.argv[4]
        secs = int(sys.argv[5]) if len(sys.argv) > 5 else 8
        asyncio.run(gen_video(name, model, DIALOGUE + SCENE + STYLE, [img], secs))

# ---- Variant C: anti-subtitle negative prompt, tighter camera wording, explicit voice casting ----
DIALOGUE_C = (
    "Locked-off static tripod shot: the camera never moves, never zooms, the framing stays exactly like the first frame. "
    "Comedic short-form sketch in a Parisian bakery. Gaston the grumpy croissant (left) keeps frowning angrily and says in "
    "French, with a very deep, low, gravelly old man's voice: \"Encore en retard, Baguette !\" Then the anxious baguette "
    "(right) answers in French, with a fast, high-pitched, panicked young voice: \"Pardon ! Le four m'a fait peur !\" "
    "Only the character who is speaking moves his mouth. Ambient bakery sound, no music. "
    "Clean image with no on-screen text: no subtitles, no captions, no letters anywhere. ")
SCENE_C = ("Small Parisian bakery, warm morning light, wooden shelves with bread loaves, window on a Paris street. On the "
           "marble counter, exactly two characters face each other, both fully visible: " + CROISSANT + " " + BAGUETTE +
           " Exactly one croissant and exactly one baguette character, no other characters. ")
NEG_C = ("subtitles, captions, on-screen text, letters, words, watermark, logo, chalkboard writing, extra characters, "
         "duplicate characters, extra baguette, camera zoom, camera push-in, camera movement, smiling croissant")

if __name__ == "__main__" and sys.argv[1] == "vidc":
    async def _c():
        api = AgnesVideoAPI(KEY, model="agnes-video-v2.0", max_retries=2, retry_base_delay=20.0)
        t = time.time()
        try:
            out = await api.generate_single_video(DIALOGUE_C + SCENE_C + STYLE, reference_image_paths=[sys.argv[2]],
                                                  duration=10, width=720, height=1280, seed=4242, negative_prompt=NEG_C)
            await out.save(f"{O}/vidC_v20_neg.mp4")
            print(json.dumps({"name": "vidC_v20_neg", "ok": True, "s": round(time.time() - t, 1)}), flush=True)
        except Exception as e:  # noqa: BLE001
            print(json.dumps({"name": "vidC_v20_neg", "ok": False, "err": repr(e)[:400], "s": round(time.time() - t, 1)}), flush=True)
    asyncio.run(_c())

# ---- Variant D: single-speaker close-up (shot/reverse-shot style), line given without quotation marks ----
PROMPT_D = (
    "Locked-off static tripod shot, the camera never moves. Medium close-up of the grumpy golden croissant character "
    "(chubby crescent body with flaky layers, bushy dark eyebrows, arms crossed) standing on a marble bakery counter. "
    "He frowns the whole time, rolls his eyes, then grumbles in French with a very deep, low, gravelly old man's voice, "
    "spoken aloud only, never written on screen: Dix ans de métier, et toujours pas de respect ! "
    "His mouth moves in sync with the words. Ambient bakery sound, no music. Clean image, no text of any kind. " + STYLE)

if __name__ == "__main__" and sys.argv[1] == "vidd":
    async def _d():
        api = AgnesVideoAPI(KEY, model="agnes-video-v2.0", max_retries=2, retry_base_delay=20.0)
        t = time.time()
        try:
            out = await api.generate_single_video(PROMPT_D, reference_image_paths=[sys.argv[2]], duration=5,
                                                  width=720, height=1280, seed=4242, negative_prompt=NEG_C)
            await out.save(f"{O}/vidD_v20_closeup.mp4")
            print(json.dumps({"name": "vidD_v20_closeup", "ok": True, "s": round(time.time() - t, 1)}), flush=True)
        except Exception as e:  # noqa: BLE001
            print(json.dumps({"name": "vidD_v20_closeup", "ok": False, "err": repr(e)[:400], "s": round(time.time() - t, 1)}), flush=True)
    asyncio.run(_d())
