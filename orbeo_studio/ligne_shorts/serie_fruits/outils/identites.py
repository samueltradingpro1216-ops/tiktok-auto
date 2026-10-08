"""Fiches d'identite des personnages fruits (Agnes image, une image par personnage, plusieurs variantes)."""
import asyncio, os, sys, time
sys.path.insert(0, os.path.expanduser("~/agnes-video-generator"))
os.environ.setdefault("AGNES_API_KEY", open(os.path.expanduser("~/.agnes_key")).read().strip())
from core.api.agnes_image import AgnesImageAPI

OUT = sys.argv[1]
VARIANTS = int(sys.argv[2]) if len(sys.argv) > 2 else 2
STYLE = "Pixar-style 3D animated character, cinematic soft lighting, highly detailed, very expressive face"
COMMON = ("Full body, front view, standing, centered, plain light grey studio background, character reference, "
          "exactly one single character, no text, no logo.")
# v5 (8 octobre, apres retour du proprietaire : « trop fades ») : des physiques extravagants, pousses au maximum
# comme dans les videos IA qui percent, et des visages marquants. Limites gardees : toujours habilles (pas de
# lingerie ni de nudite), pas de pose ni de cadrage sur le corps, des visages clairement adultes (25 a 30 ans).
STYLE = ("Stylized semi-realistic 3D CGI character, glamorous high-budget animated movie look, cinematic studio "
         "lighting, highly detailed skin and hair, striking attractive face")
CHARS = {
    "cerise": "a stunning glamorous adult woman, 25 years old, with a mature adult face; her skin is deep "
              "cherry-red everywhere, smooth satin finish; voluptuous exaggerated hourglass figure: large full "
              "bust, very narrow waist, wide hips and a big round curvy backside; long voluminous wavy dark-red hair "
              "with two small cherries and a leaf as a hair clip; striking face: big almond-shaped hazel eyes with "
              "long lashes, full glossy lips, high cheekbones, glamorous makeup; wearing a tight white low-cut V-neck "
              "crop t-shirt showing cleavage and her midriff, a small mustard-yellow waitress apron tied at the "
              "hips, tight high-waisted blue jeans and white sneakers; confident standing pose.",
    "citron": "a hugely muscular, very handsome adult man, 28 years old; his skin is bright lemon-yellow everywhere "
              "with a subtle peel texture, his head slightly lemon-shaped with a small tip on top; bodybuilder "
              "physique: massive broad shoulders, huge pecs, visible six-pack abs, huge arms, V-shaped torso; "
              "chiseled square jaw, light stubble, intense arrogant eyes, cocky smirk, slicked-back golden-yellow "
              "hair; wearing an open black leather jacket over his bare chest showing his pecs and abs, a thick gold "
              "chain, tight black jeans and designer sneakers; confident standing pose.",
    "peche": "a stunning glamorous adult influencer woman, 26 years old, with a mature adult face; her skin is vivid "
             "peach orange everywhere with deep pink-red blush on the cheeks, like a ripe peach fruit; voluptuous "
             "exaggerated hourglass figure: large full bust, tiny waist, wide hips and a big round curvy backside; "
             "long glossy wavy brown hair with a green peach leaf clipped in it; striking face: big eyes with long "
             "lashes, full glossy pink lips, contoured glamorous makeup, arrogant smile; wearing a tight pink "
             "bodycon mini dress with a deep V neckline showing cleavage, big gold hoop earrings, holding a "
             "smartphone with a pink case; confident standing pose.",
    "kiwi": "a hugely muscular, very handsome adult man, 27 years old; his skin is olive-green everywhere with a "
            "fine fuzzy kiwi texture; athletic bodybuilder physique: massive shoulders, huge pecs, visible "
            "six-pack abs, big arms; short curly dark-brown hair, bright kiwi-green eyes, chiseled jaw, warm "
            "charming smile; wearing a backwards green cap, a tight white cropped tank top with a small kiwi slice "
            "logo showing his abs and big arms, an open green delivery jacket, black cargo pants and sneakers; "
            "confident standing pose.",
    "prune": "an old grandmother character whose head and body are one deep purple wrinkled prune, small round "
             "glasses, kind but mischievous eyes, wearing a knitted beige shawl, a small knitted hat, a long floral "
             "dress and slippers, holding a wooden spoon.",
}

async def main():
    api = AgnesImageAPI(api_key=os.environ["AGNES_API_KEY"])
    for name, desc in CHARS.items():
        for k in range(1, VARIANTS + 1):
            path = os.path.join(OUT, f"{name}_{k}.png")
            if os.path.exists(path):
                continue
            t = time.time()
            try:
                img = await api.generate_single_image(prompt=f"{STYLE}. {desc} {COMMON}", size="1024x1024")
                await img.save(path)
                print(f"{name}_{k} ok {time.time() - t:.0f}s", flush=True)
            except Exception as e:
                print(f"{name}_{k} ECHEC {e}", flush=True)

asyncio.run(main())
