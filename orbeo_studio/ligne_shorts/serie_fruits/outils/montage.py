#!/usr/bin/env python3
"""Monte un episode de la serie fruits a partir de produire.py : video verticale 1080x1920.

- chaque plan est coupe autour de sa replique (mots reperes par whisper), en coupe franche ;
- Agnes incruste de faux sous-titres illisibles vers 75 a 86 % de la hauteur : ils sont reperes image par image,
  la zone est floutee en fondu et un degrade sombre couvre le bas ; nos sous-titres sont plus haut (couper le bas
  obligeait a zoomer x2, l'image devenait floue) ;
- voix constantes (voix/pXX.wav), bruitages et ambiances fabriques ici, musique par ambiance qui suit l'histoire,
  baissee automatiquement sous les voix ;
- sous-titres mot a mot, accroche en haut pendant 3,5 s, badge d'episode, notification, appel video, chiffres,
  publication incrustee, carte « PARTIE 2 » a la fin.

Usage : ~/agnes-video-generator/.venv/bin/python montage.py ../episodes/01_la_bague
Sorties dans l'episode : final.mp4, final_sans_musique.mp4 (pour ajouter un son tendance dans TikTok), apercu.jpg
"""
import difflib
import json
import os
import re
import subprocess
import sys
import unicodedata

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H, FPS, SR = 1080, 1920, 24, 48000
FONTS = os.path.expanduser("~/fonts")
BLACK = os.path.join(FONTS, "Montserrat-Black.ttf")
XBOLD = os.path.join(FONTS, "Montserrat-ExtraBold.ttf")
SEMI = os.path.join(FONTS, "Montserrat-SemiBold.ttf")
EMOJI = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"
CAPTION_Y = 1340  # bas des sous-titres : au-dessus de la legende et des boutons TikTok
NOMS = {"cerise": "Cerise", "citron": "Citron", "peche": "Pêche", "kiwi": "Kiwi", "prune": "Mamie Prune"}


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(f"{' '.join(cmd[:6])}... : {r.stderr[-1500:]}")
    return r.stdout


def norm(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "", t)


# ── texte avec emojis (Pillow) ──────────────────────────────────────────────

def is_emoji(ch):
    o = ord(ch)
    return o >= 0x1F000 or 0x2600 <= o <= 0x27BF or o in (0xFE0F, 0x200D)


def emoji_img(ch, size):
    f = ImageFont.truetype(EMOJI, 109)
    im = Image.new("RGBA", (136, 128), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((0, 0), ch, font=f, embedded_color=True)
    im = im.crop(im.getbbox() or (0, 0, 1, 1))
    return im.resize((size, int(size * im.height / max(im.width, 1))), Image.LANCZOS)


def text_runs(text):
    runs, cur, emo = [], "", None
    for ch in text:
        e = is_emoji(ch)
        if ch == "️":
            continue
        if emo is None or e == emo:
            cur += ch
        else:
            runs.append((emo, cur))
            cur = ch
        emo = e
    if cur:
        runs.append((emo, cur))
    return runs


def measure(text, font):
    w = 0
    for emo, s in text_runs(text):
        w += len(s) * int(font.size * 1.1) if emo else font.getlength(s)
    return w


def draw_text(img, xy, text, font, fill, stroke=0, stroke_fill=(0, 0, 0)):
    x, y = xy
    d = ImageDraw.Draw(img)
    for emo, s in text_runs(text):
        if emo:
            for ch in s:
                e = emoji_img(ch, int(font.size * 1.0))
                img.alpha_composite(e, (int(x), int(y + font.size * 0.1)))
                x += int(font.size * 1.1)
        else:
            d.text((x, y), s, font=font, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)
            x += font.getlength(s)


def wrap(text, font, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if measure(t, font) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = w
    return lines + [cur] if cur else lines


# ── incrustations ──────────────────────────────────────────────────────────

def png_title(text, path):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    f = ImageFont.truetype(BLACK, 58)
    lines = wrap(text, f, 860)
    lh = 74
    bw = max(measure(l, f) for l in lines) + 70
    bh = lh * len(lines) + 44
    x0, y0 = (W - bw) / 2, 300
    ImageDraw.Draw(img).rounded_rectangle((x0, y0, x0 + bw, y0 + bh), 26, fill=(255, 255, 255, 245))
    for i, l in enumerate(lines):
        draw_text(img, ((W - measure(l, f)) / 2, y0 + 20 + i * lh), l, f, (10, 10, 10))
    img.save(path)


def png_badge(text, path):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    f = ImageFont.truetype(BLACK, 34)
    w = measure(text, f) + 40
    ImageDraw.Draw(img).rounded_rectangle((40, 210, 40 + w, 266), 14, fill=(220, 20, 60, 235))
    draw_text(img, (60, 216), text, f, (255, 255, 255))
    img.save(path)


def png_notif(de, texte, path):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    x0, y0, x1, y1 = 50, 960, W - 50, 1130
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle((x0, y0 + 8, x1, y1 + 8), 36, fill=(0, 0, 0, 110))
    img.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(12)))
    d.rounded_rectangle((x0, y0, x1, y1), 36, fill=(250, 250, 250, 245))
    d.rounded_rectangle((x0 + 24, y0 + 35, x0 + 124, y0 + 135), 24, fill=(52, 199, 89))
    d.ellipse((x0 + 44, y0 + 58, x0 + 104, y0 + 104), fill="white")
    d.polygon([(x0 + 54, y0 + 96), (x0 + 50, y0 + 116), (x0 + 72, y0 + 102)], fill="white")
    draw_text(img, (x0 + 150, y0 + 28), de, ImageFont.truetype(BLACK, 40), (15, 15, 15))
    draw_text(img, (x0 + 150, y0 + 84), texte, ImageFont.truetype(SEMI, 40), (30, 30, 30))
    f = ImageFont.truetype(SEMI, 28)
    d.text((x1 - 30 - f.getlength("maintenant"), y0 + 34), "maintenant", font=f, fill=(130, 130, 130))
    img.save(path)


def png_appel(nom, pip_src, path):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    grad = Image.new("RGBA", (W, 520), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grad)
    for y in range(520):
        gd.line((0, y, W, y), fill=(0, 0, 0, int(140 * (1 - y / 520))))
    img.alpha_composite(grad, (0, 0))
    draw_text(img, (50, 300), nom, ImageFont.truetype(BLACK, 52), (255, 255, 255), 2, (0, 0, 0))
    ImageDraw.Draw(img).ellipse((52, 380, 72, 400), fill=(52, 199, 89))
    ImageDraw.Draw(img).text((84, 370), "appel vidéo", font=ImageFont.truetype(SEMI, 34), fill="white",
                             stroke_width=2, stroke_fill="black")
    if pip_src and os.path.exists(pip_src):
        pip = Image.open(pip_src).convert("RGB")
        pw, ph = 250, 400
        r = max(pw / pip.width, ph / pip.height)
        pip = pip.resize((int(pip.width * r), int(pip.height * r)), Image.LANCZOS)
        pip = pip.crop(((pip.width - pw) // 2, 0, (pip.width - pw) // 2 + pw, ph))
        mask = Image.new("L", (pw, ph), 0)
        ImageDraw.Draw(mask).rounded_rectangle((0, 0, pw, ph), 28, fill=255)
        frame = Image.new("RGBA", (pw + 8, ph + 8), (255, 255, 255, 230))
        fm = Image.new("L", (pw + 8, ph + 8), 0)
        ImageDraw.Draw(fm).rounded_rectangle((0, 0, pw + 8, ph + 8), 32, fill=255)
        img.paste(frame, (W - pw - 54, 296), fm)
        img.paste(pip, (W - pw - 50, 300), mask)
    img.save(path)


def png_chiffre(texte, path):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    f = ImageFont.truetype(BLACK, 104)
    lines = wrap(texte, f, 960)
    for i, l in enumerate(lines):
        draw_text(img, ((W - measure(l, f)) / 2, 1040 + i * 120), l, f, (255, 214, 0), 10, (0, 0, 0))
    img.save(path)


def png_post(post, photo, decor, avatar, base_path, stamp_path):
    bg = Image.open(decor).convert("RGB")
    r = max(W / bg.width, H / bg.height)
    bg = bg.resize((int(bg.width * r), int(bg.height * r)), Image.LANCZOS).crop((0, 0, W, H))
    bg = bg.filter(ImageFilter.GaussianBlur(18)).point(lambda v: int(v * 0.45)).convert("RGBA")
    x0, y0, cw = 110, 300, W - 220
    ch = 1220
    d = ImageDraw.Draw(bg)
    d.rounded_rectangle((x0, y0, x0 + cw, y0 + ch), 40, fill=(255, 255, 255, 255))
    if avatar and os.path.exists(avatar):
        av = Image.open(avatar).convert("RGB")
        s = min(av.size)
        av = av.crop(((av.width - s) // 2, 0, (av.width + s) // 2, s)).resize((84, 84), Image.LANCZOS)
        m = Image.new("L", (84, 84), 0)
        ImageDraw.Draw(m).ellipse((0, 0, 84, 84), fill=255)
        bg.paste(av, (x0 + 30, y0 + 26), m)
    d.text((x0 + 132, y0 + 34), post["auteur"], font=ImageFont.truetype(BLACK, 38), fill=(15, 15, 15))
    bx = x0 + 132 + ImageFont.truetype(BLACK, 38).getlength(post["auteur"]) + 12
    d.ellipse((bx, y0 + 40, bx + 32, y0 + 72), fill=(32, 150, 243))
    d.line((bx + 8, y0 + 56, bx + 14, y0 + 63, bx + 24, y0 + 49), fill="white", width=5)
    ph = Image.open(photo).convert("RGB")
    pw = cw - 40
    r = pw / ph.width
    ph = ph.resize((pw, int(ph.height * r)), Image.LANCZOS).crop((0, 80, pw, 80 + 780))
    bg.paste(ph, (x0 + 20, y0 + 132))
    yt = y0 + 132 + 780 + 26
    draw_text(bg, (x0 + 30, yt), "♥  12,4 k     💬 2 318", ImageFont.truetype(XBOLD, 34), (220, 20, 60))
    f = ImageFont.truetype(SEMI, 38)
    for i, l in enumerate(wrap(post["texte"], f, cw - 60)):
        draw_text(bg, (x0 + 30, yt + 64 + i * 50), l, f, (20, 20, 20))
    bg.convert("RGB").save(base_path)
    st = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    lay = Image.new("RGBA", (980, 200), (0, 0, 0, 0))
    ld = ImageDraw.Draw(lay)
    ld.rounded_rectangle((10, 10, 970, 190), 24, fill=(220, 20, 40, 240), outline=(255, 255, 255), width=8)
    fs = ImageFont.truetype(BLACK, 84)
    ld.text(((980 - fs.getlength(post["tampon"])) / 2, 48), post["tampon"], font=fs, fill="white")
    lay = lay.rotate(-8, expand=True, resample=Image.BICUBIC)
    st.alpha_composite(lay, ((W - lay.width) // 2, 980))
    st.save(stamp_path)


def png_fin(texte, sous, path):
    img = Image.new("RGB", (W, H), (0, 0, 0)).convert("RGBA")
    f = ImageFont.truetype(BLACK, 170)
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).text(((W - f.getlength(texte)) / 2, 780), texte, font=f, fill=(230, 20, 50, 255))
    img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(22)))
    ImageDraw.Draw(img).text(((W - f.getlength(texte)) / 2, 780), texte, font=f, fill="white")
    fs = ImageFont.truetype(XBOLD, 54)
    draw_text(img, ((W - measure(sous, fs)) / 2, 1010), sous, fs, (230, 230, 230))
    img.convert("RGB").save(path)


# ── faux sous-titres d'Agnes ───────────────────────────────────────────────

def detect_band(clip, a, dur, fps=4, w=352, h=640):
    """Rectangle (x0, y0, x1, y1, en fractions) des faux sous-titres incrustes, ou None."""
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-ss", f"{a:.3f}", "-t", f"{dur:.3f}", "-i", clip, "-vf",
                          f"fps={fps},scale={w}:{h}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                         capture_output=True, check=True).stdout
    F = np.frombuffer(raw, np.uint8).reshape(-1, h, w, 3).astype(np.int16)
    y0 = int(0.6 * h)
    boxes = []
    for f in F:
        reg = f[y0:int(0.97 * h)]
        white = (reg.min(-1) > 215) & ((reg.max(-1) - reg.min(-1)) < 40)
        dark = reg.mean(-1) < 70
        near = np.zeros_like(dark)
        for dy, dx in ((2, 0), (-2, 0), (0, 2), (0, -2)):  # trait blanc borde de noir : du texte
            near |= np.roll(np.roll(dark, dy, 0), dx, 1)
        txt = white & near
        rows = np.where(txt.sum(1) >= 6)[0]
        if len(rows) >= 3:
            cols = np.where(txt[rows].sum(0) > 0)[0]
            boxes.append(((cols.min()) / w, (rows.min() + y0) / h, (cols.max()) / w, (rows.max() + y0) / h))
    if len(boxes) < 2:
        return None
    b = np.array(boxes)
    return float(b[:, 0].min()), float(b[:, 1].min()), float(b[:, 2].max()), float(b[:, 3].max())


def png_mask(w, h, r, path):
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rectangle((r, r, w - r, h - r), fill=255)
    m.filter(ImageFilter.GaussianBlur(r / 2)).save(path)


def png_gradient(path, start=0.66, ramp=0.12, alpha=165):
    g = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(g)
    for y in range(int(H * start), H):
        d.line((0, y, W, y), fill=(0, 0, 0, int(alpha * min(1, (y - H * start) / (H * ramp)))))
    g.save(path)


# ── son ────────────────────────────────────────────────────────────────────

def load(path, a=0.0, d=None, af=None):
    cmd = ["ffmpeg", "-loglevel", "error", "-ss", f"{a:.3f}"] + (["-t", f"{d:.3f}"] if d else []) + \
          ["-i", path, "-vn"] + (["-af", af] if af else []) + ["-ac", "1", "-ar", str(SR), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, dtype=np.float32).copy()


def rms(x):
    return float(np.sqrt(np.mean(x ** 2) + 1e-12))


def place(bus, x, t, gain=1.0):
    i = int(t * SR)
    if i >= len(bus) or len(x) == 0:
        return
    n = min(len(x), len(bus) - i)
    bus[i:i + n] += x[:n] * gain


def fade(x, fin=0.01, fout=0.01):
    n1, n2 = int(fin * SR), int(fout * SR)
    if n1:
        x[:n1] *= np.linspace(0, 1, n1)
    if n2:
        x[-n2:] *= np.linspace(1, 0, n2)
    return x


def sfx(kind, rng=np.random.default_rng(7)):
    t = lambda d: np.arange(int(d * SR)) / SR  # noqa: E731
    if kind == "ding":
        tt = t(0.9)
        return (0.5 * np.sin(2 * np.pi * 1318 * tt) * np.exp(-tt * 6) +
                0.4 * np.sin(2 * np.pi * 1760 * tt) * np.exp(-np.clip(tt - 0.12, 0, None) * 6) * (tt > 0.12))
    if kind == "whoosh":
        n = rng.standard_normal(int(0.55 * SR))
        env = np.sin(np.linspace(0, np.pi, len(n))) ** 2
        spec = np.fft.rfft(n * env)
        f = np.fft.rfftfreq(len(n), 1 / SR)
        spec *= np.exp(-((f - 1200) / 900) ** 2) + 0.3 * np.exp(-((f - 400) / 300) ** 2)
        return 0.6 * np.fft.irfft(spec, len(n)) / (np.abs(np.fft.irfft(spec, len(n))).max() + 1e-9)
    if kind == "boom":
        tt = t(1.6)
        sweep = 2 * np.pi * np.cumsum(np.linspace(90, 38, len(tt))) / SR
        return 0.95 * np.sin(sweep) * np.exp(-tt * 2.6) + 0.15 * rng.standard_normal(len(tt)) * np.exp(-tt * 30)
    if kind == "battement":
        tt = t(0.32)
        thump = np.sin(2 * np.pi * 55 * tt) * np.exp(-tt * 18)
        out = np.zeros(int(1.0 * SR))
        out[:len(thump)] += thump
        out[int(0.24 * SR):int(0.24 * SR) + len(thump)] += 0.8 * thump
        return 0.9 * out
    if kind == "pluie":
        n = rng.standard_normal(int(4.0 * SR))
        spec = np.fft.rfft(n)
        f = np.fft.rfftfreq(len(n), 1 / SR)
        spec *= 1 / np.sqrt(np.maximum(f, 50)) * (f > 300) * np.exp(-(f / 9000) ** 2)
        x = np.fft.irfft(spec, len(n))
        drops = (rng.random(len(n)) > 0.9993) * rng.standard_normal(len(n)) * 3
        x = x / (np.abs(x).max() + 1e-9) + np.convolve(drops, np.exp(-np.arange(200) / 30), "same") * 0.05
        return x / (np.abs(x).max() + 1e-9)
    if kind == "salle":  # ton de piece : souffle tres grave
        n = rng.standard_normal(int(4.0 * SR))
        spec = np.fft.rfft(n)
        f = np.fft.rfftfreq(len(n), 1 / SR)
        spec *= (f < 400) / np.sqrt(np.maximum(f, 20))
        x = np.fft.irfft(spec, len(n))
        return x / (np.abs(x).max() + 1e-9)
    raise ValueError(kind)


def loop_to(x, n):
    if len(x) >= n:
        return x[:n].copy()
    reps = int(np.ceil(n / len(x)))
    xf = x.copy()
    k = int(0.2 * SR)
    xf[:k] *= np.linspace(0, 1, k)
    xf[-k:] *= np.linspace(1, 0, k)
    return np.tile(xf, reps)[:n]


def music_start(x):
    """Debut utile d'une musique generee (saute un debut trop calme)."""
    win = int(0.25 * SR)
    e = np.array([rms(x[i:i + win]) for i in range(0, max(len(x) - win, 1), win)])
    if not len(e):
        return 0.0
    thr = 0.5 * np.median(e)
    k = int(np.argmax(e >= thr))
    return k * 0.25


# ── sous-titres ────────────────────────────────────────────────────────────

def align_times(tokens, ref):
    """Temps (debut, fin) de chaque mot de « tokens », pris sur « ref » = [(mot, debut, fin)]."""
    a = [norm(t) for t in tokens]
    b = [norm(r[0]) for r in ref]
    out = [None] * len(tokens)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            for k in range(i2 - i1):
                out[i1 + k] = (ref[j1 + k][1], ref[j1 + k][2])
        elif op == "replace":
            s, e = ref[j1][1], ref[j2 - 1][2]
            step = (e - s) / (i2 - i1)
            for k in range(i2 - i1):
                out[i1 + k] = (s + k * step, s + (k + 1) * step)
    for i in range(len(out)):  # mots sans correspondance : colles au voisin
        if out[i] is None:
            prev = next((out[j] for j in range(i - 1, -1, -1) if out[j]), None)
            nxt = next((out[j] for j in range(i + 1, len(out)) if out[j]), None)
            t = prev[1] if prev else (nxt[0] if nxt else 0.0)
            out[i] = (t, t + 0.2)
    return out


def ass_time(t):
    t = max(t, 0)
    return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}"


def ass_escape(s):
    return s.replace("{", "(").replace("}", ")")


def write_ass(words, path):
    """words : [(texte, debut, fin)] sur la ligne de temps finale ; groupes de 3 mots, mot courant en jaune."""
    head = ("[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\nWrapStyle: 0\n\n[V4+ Styles]\n"
            "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, "
            "Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, "
            "MarginL, MarginR, MarginV, Encoding\n"
            f"Style: Cap,Montserrat Black,78,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,0,0,1,7,2,2,"
            f"60,60,{H - CAPTION_Y},1\n\n[Events]\n"
            "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n")
    groups, cur = [], []
    for w in words:
        cur.append(w)
        if len(cur) == 3 or re.search(r"[.!?…,:]$", w[0]) or (len(cur) == 2 and len(cur[0][0] + w[0]) > 16):
            groups.append(cur)
            cur = []
    if cur:
        groups.append(cur)
    ev = []
    for gi, g in enumerate(groups):
        g_end = g[-1][2] + 0.15
        if gi + 1 < len(groups):
            g_end = min(g_end + 0.35, groups[gi + 1][0][1])
        for k, w in enumerate(g):
            s = w[1]
            e = g[k + 1][1] if k + 1 < len(g) else g_end
            if e <= s:
                continue
            txt = " ".join(("{\\c&H0000E1FF&}" + ass_escape(x[0]) + "{\\c&H00FFFFFF&}") if j == k else ass_escape(x[0])
                           for j, x in enumerate(g))
            ev.append(f"Dialogue: 0,{ass_time(s)},{ass_time(e)},Cap,,0,0,0,,{txt}")
    open(path, "w", encoding="utf-8").write(head + "\n".join(ev) + "\n")


# ── montage ────────────────────────────────────────────────────────────────

def main():
    d = os.path.abspath(sys.argv[1])
    ep = json.load(open(os.path.join(d, "episode.json"), encoding="utf-8"))
    state = json.load(open(os.path.join(d, "state.json")))
    work = os.path.join(d, "montage")
    os.makedirs(work, exist_ok=True)
    ident = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "identite")
    reglages = ep.get("montage", {})
    # vitesse : chaque plan (image et son ensemble, donc les levres restent synchronisees) est accelere ; les
    # references parlent 4 a 7 mots par seconde de parole, nos clips 2,3 a 2,8
    V = float(reglages.get("vitesse", 1.0))
    # voix plus chaudes et plus pleines (les notres etaient aigues et brillantes : 1750 Hz contre 1200 Hz de
    # centre spectral dans les references), compression facon doublage
    VOIX_AF = (f"atempo={V},highpass=f=70,lowshelf=f=180:g=3,equalizer=f=3000:t=q:w=1.2:g=-2,"
               "highshelf=f=6500:g=-5,acompressor=threshold=-24dB:ratio=3:attack=5:release=90:makeup=2"
               if reglages.get("voix_chaudes") else f"atempo={V}")

    def img_of(pid):
        p = os.path.join(d, "images", f"p{pid:02d}_cadre.png")
        return p if os.path.exists(p) else os.path.join(d, "images", f"p{pid:02d}.png")

    # 1. ligne de temps
    segs, t = [], 0.0
    for p in ep["plans"]:
        pid = p["id"]
        if p.get("type") == "post":
            segs.append({"p": p, "kind": "post", "a": 0, "dur": p.get("duree", 2.6), "src_dur": p.get("duree", 2.6),
                         "start": t})
            t += segs[-1]["dur"]
            continue
        st = state.get("clips", {}).get(str(pid), {})
        if not st.get("done"):
            print(f"plan {pid} absent : saute")
            continue
        best = next(x for x in st["tries"] if x.get("file") == st["best"])
        cdur = best["duration"]
        clip_path, voice_src = os.path.join(d, "clips", f"p{pid:02d}.mp4"), None
        # clip recale sur la voix clonee (caler.py) : il remplace le clip d'origine, image et voix
        cale_info = os.path.join(d, "controle", f"p{pid:02d}_cale.json")
        if p.get("parle") and reglages.get("voix_clonees") and os.path.exists(cale_info):
            info = json.load(open(cale_info))
            best = {**best, "words": info["words"], "speech": info["speech"], "duration": info["duration"]}
            cdur = info["duration"]
            clip_path = voice_src = os.path.join(d, "clips", f"p{pid:02d}_cale.mp4")
        if p.get("parle") and best.get("speech"):
            s0, s1 = best["speech"]
            a = max(0.0, s0 - (0.02 if not segs else 0.10))
            b = min(cdur - 0.05, s1 + 0.28)
        else:
            a = 0.4
            b = min(cdur - 0.05, a + p.get("duree", 2.5))
        segs.append({"p": p, "kind": "clip", "a": a, "dur": round((b - a) / V, 3), "src_dur": round(b - a, 3),
                     "start": t, "best": best, "clip": clip_path, "voice": voice_src})
        t += segs[-1]["dur"]
    fin_dur = 2.0
    total = t + fin_dur
    print(f"duree : {total:.1f} s, {len(segs)} plans")

    # 2. images d'incrustation
    png_title(ep["accroche"], os.path.join(work, "titre.png"))
    png_badge(f"{ep['badge']} · {ep['titre'].split(',')[0].upper()}", os.path.join(work, "badge.png"))
    png_fin(ep["fin"], "La suite très vite 🍒 Abonne-toi", os.path.join(work, "fin.png"))

    # 3. segments video
    vf_clip = (f"setpts=(PTS-STARTPTS)/{V},scale={W}:-2:flags=lanczos,crop={W}:{H}:0:(ih-{H})/2,unsharp=5:5:0.45:5:5:0,fps={FPS},"
               "setsar=1,format=yuv420p")
    png_gradient(os.path.join(work, "degrade.png"))
    files = []
    for k, s in enumerate(segs):
        p = s["p"]
        out = os.path.join(work, f"seg{k:02d}.mp4")
        files.append(out)
        if s["kind"] == "post":
            base, stamp = os.path.join(work, "post.png"), os.path.join(work, "post_tampon.png")
            png_post(p["post"], img_of(p["post"]["photo_plan"]), os.path.join(d, "decors", f"{p['decor']}.png"),
                     os.path.join(ident, "citron.png"), base, stamp)
            n = int(s["dur"] * FPS)
            run(["ffmpeg", "-loglevel", "error", "-y", "-loop", "1", "-i", base, "-loop", "1", "-i", stamp,
                 "-filter_complex",
                 f"[0]scale={W * 2}:{H * 2},zoompan=z='1+0.05*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
                 f"d=1:s={W}x{H}:fps={FPS}[b];[b][1]overlay=enable='gte(t,0.9)',format=yuv420p",
                 "-t", f"{s['dur']:.3f}", "-r", str(FPS), "-c:v", "libx264", "-crf", "17", "-preset", "medium", out])
            continue
        inputs = ["-ss", f"{s['a']:.3f}", "-t", f"{s['src_dur']:.3f}", "-i", s["clip"]]
        band = detect_band(s["clip"], s["a"], s["src_dur"]) if p.get("parle") else None
        s["band"] = band
        if band:
            sw, sh = map(int, run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries",
                                   "stream=width,height", "-of", "csv=p=0", s["clip"]]).strip().split(","))
            bx0, by0 = max(0, int((band[0] - 0.05) * sw)), max(0, int((band[1] - 0.03) * sh))
            bx1, by1 = min(sw, int((band[2] + 0.05) * sw)), min(sh, int((band[3] + 0.03) * sh))
            bw, bh = (bx1 - bx0) // 2 * 2, (by1 - by0) // 2 * 2
            mask = os.path.join(work, f"masque{k:02d}.png")
            png_mask(bw, bh, 14, mask)
            inputs += ["-loop", "1", "-i", mask]
            chain = (f"[0:v]split[m][c];[c]crop={bw}:{bh}:{bx0}:{by0},gblur=sigma=26,format=rgba[cb];"
                     f"[1:v]format=gray,scale={bw}:{bh}[mk];[cb][mk]alphamerge[pt];"
                     f"[m][pt]overlay={bx0}:{by0}:shortest=1,{vf_clip}[v0]")
            n_in = 2
        else:
            chain = f"[0:v]{vf_clip}[v0]"
            n_in = 1
        last = "v0"
        for ov in p.get("incrust", []):
            png = os.path.join(work, f"p{p['id']:02d}_{ov['type']}.png")
            enable, ypos = "1", "0"
            if ov["type"] == "notif":
                png_notif(ov["de"], ov["texte"], png)
                ypos = "if(lt(t,0.25),300-300*t/0.25,0)"
            elif ov["type"] == "appel":
                png_appel(ov["nom"], img_of(7), png)
            elif ov["type"] == "chiffre":
                png_chiffre(ov["texte"], png)
                words = s["best"].get("words", [])
                tw = next((w["start"] for w in words if norm(ov["mot"]) in norm(w["word"])), None)
                tw = (tw - s["a"]) / V if tw is not None else 0.3
                enable = f"gte(t,{max(tw - 0.15, 0):.2f})"
                s["chiffre_t"] = s["start"] + max(tw - 0.15, 0)
            inputs += ["-loop", "1", "-i", png]
            chain += f";[{last}][{n_in}:v]overlay=x=0:y='{ypos}':enable='{enable}':shortest=1[v{n_in}]"
            last = f"v{n_in}"
            n_in += 1
        run(["ffmpeg", "-loglevel", "error", "-y", *inputs, "-filter_complex", chain, "-map", f"[{last}]",
             "-t", f"{s['dur']:.3f}", "-r", str(FPS), "-an", "-c:v", "libx264", "-crf", "17", "-preset", "medium",
             out])
    fin = os.path.join(work, "seg_fin.mp4")
    run(["ffmpeg", "-loglevel", "error", "-y", "-loop", "1", "-i", os.path.join(work, "fin.png"), "-vf",
         f"fade=in:0:6,format=yuv420p,fps={FPS}", "-t", f"{fin_dur}", "-c:v", "libx264", "-crf", "17", fin])
    files.append(fin)
    lst = os.path.join(work, "liste.txt")
    open(lst, "w").write("".join(f"file '{f}'\n" for f in files))
    raw = os.path.join(work, "video_brute.mp4")
    run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", raw])

    # 4. sous-titres
    words = []
    for s in segs:
        p = s["p"]
        if s["kind"] != "clip" or not p.get("parle"):
            continue
        ref = [(w["word"], w["start"], w["end"]) for w in s["best"].get("words", [])]
        spoken = p["replique"].split()
        if not ref:
            continue
        times = align_times(spoken, ref)
        shown = p.get("sous_titre", p["replique"]).split()
        times = align_times(shown, [(w, a, b) for w, (a, b) in zip(spoken, times)]) if shown != spoken else times
        for w, (a, b) in zip(shown, times):
            ta, tb = s["start"] + (a - s["a"]) / V, s["start"] + (b - s["a"]) / V
            if tb > s["start"] and ta < s["start"] + s["dur"]:
                words.append((w, max(ta, s["start"]), min(tb, s["start"] + s["dur"])))
    write_ass(words, os.path.join(work, "sous_titres.ass"))

    # 5. son
    n = int(total * SR) + SR
    voice, fx, music = np.zeros(n), np.zeros(n), np.zeros(n)
    for s in segs:
        p = s["p"]
        if s["kind"] == "clip" and p.get("parle"):
            src = s.get("voice") or os.path.join(d, "voix", f"p{p['id']:02d}.wav")
            src = src if os.path.exists(src) else s["clip"]
            x = load(src, s["a"], s["src_dur"], VOIX_AF)
            x = fade(x * (0.1 / max(rms(x), 1e-4)), 0.01, 0.04)
            place(voice, x, s["start"])
        elif s["kind"] == "clip":  # plan sans parole : le son du clip (pas, foule...) en fond
            x = load(s["clip"], s["a"], s["src_dur"], f"atempo={V}")
            place(fx, fade(x * (0.04 / max(rms(x), 1e-4)), 0.05, 0.1), s["start"])
    # ambiances par lieu
    amb = {"rue": ("pluie", 0.05), "cuisine": ("pluie", 0.012), "appart": ("salle", 0.01),
           "chambre_peche": ("salle", 0.008)}
    for s in segs:
        a = amb.get(s["p"]["decor"])
        if a and s["kind"] == "clip":
            place(fx, fade(loop_to(sfx(a[0]), int(s["dur"] * SR)) * a[1], 0.03, 0.03), s["start"])
    # bruitages
    first = {}
    for s in segs:
        first.setdefault(s["p"]["decor"], s["start"])
    by_id = {s["p"]["id"]: s for s in segs}
    hits = []
    if 1 in by_id:
        hits.append(("ding", by_id[1]["start"] + 0.05, 0.35))
    for s in segs:
        if s is not segs[0] and s["start"] == first.get(s["p"]["decor"]) and s["p"]["decor"] != "chambre_peche":
            hits.append(("whoosh", s["start"] - 0.25, 0.35))
        if s.get("chiffre_t"):
            hits.append(("whoosh", s["chiffre_t"] - 0.1, 0.25))
        if s["kind"] == "post":
            hits.append(("ding", s["start"] + 0.1, 0.3))
            hits.append(("boom", s["start"] + 0.9, 0.6))
    if 24 in by_id:
        hits.append(("boom", by_id[24]["start"], 0.9))
    if 29 in by_id:
        hits.append(("battement", by_id[29]["start"] + 0.1, 0.9))
    hits.append(("boom", total - fin_dur, 0.8))
    for kind, at, g in hits:
        place(fx, sfx(kind), max(at, 0), g)
    # musique : chaque ambiance demarre a son plan et dure jusqu'a la suivante (fondus courts sur les coupes)
    unique = reglages.get("musique_unique")  # un seul fond continu, comme le funk des videos de reference
    cues = [(0.0, unique)] if unique else [(s["start"], s["p"]["musique"]) for s in segs if s["p"].get("musique")]
    stops = {}  # coupures franches : la musique s'arrete net quand les portes s'ouvrent, puis repart
    if 24 in by_id:
        stops[by_id[24]["start"]] = unique or "revanche"
    for at, name in stops.items():
        cues.append((at + 0.6, name))
    cues.sort()
    end_music = by_id[29]["start"] if 29 in by_id else total - fin_dur
    prises = ep.get("musique_prise", {})
    for i, (at, name) in enumerate(cues):
        until = cues[i + 1][0] if i + 1 < len(cues) else end_music
        if at in [c + 0.6 for c in stops]:
            until = end_music
        if until <= at:
            continue
        path = os.path.join(d, "musique", name, f"prise_{prises.get(name, 1)}.wav")
        if not os.path.exists(path):
            print(f"musique {name} absente")
            continue
        full = load(path)
        off = music_start(full)
        x = loop_to(full[int(off * SR):], int((until - at + 0.3) * SR))
        x = x * (0.12 / max(rms(x), 1e-4))
        sharp = any(abs(until - c) < 0.01 for c in stops)
        fade(x, 0.25 if i else 0.02, 0.05 if sharp else 0.4)
        place(music, x, at)
    # la musique baisse sous les voix
    win = int(0.03 * SR)
    env = np.sqrt(np.convolve(voice ** 2, np.ones(win) / win, "same"))
    target = np.where(env > 0.015, 0.32, 1.0)
    g = np.empty_like(target)
    g[0] = 1.0
    att, rel = np.exp(-1 / (0.03 * SR)), np.exp(-1 / (0.35 * SR))
    for i in range(1, len(target)):  # suiveur d'enveloppe (rapide pour baisser, lent pour remonter)
        c = att if target[i] < g[i - 1] else rel
        g[i] = c * g[i - 1] + (1 - c) * target[i]
    mix = voice + fx + music * g
    mix_nm = voice + fx
    peak = max(np.abs(mix).max(), 1e-6)
    for name, m in (("mix.wav", mix), ("mix_sans_musique.wav", mix_nm)):
        y = (m / peak * 0.89).astype(np.float32)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-",
                        os.path.join(work, name)], input=y.tobytes(), check=True)

    # 6. assemblage final
    ass = os.path.join(work, "sous_titres.ass").replace(":", "\\:")
    for name, audio in (("final.mp4", "mix.wav"), ("final_sans_musique.mp4", "mix_sans_musique.wav")):
        run(["ffmpeg", "-loglevel", "error", "-y", "-i", raw, "-i", os.path.join(work, audio),
             "-loop", "1", "-i", os.path.join(work, "titre.png"), "-loop", "1", "-i", os.path.join(work, "badge.png"),
             "-loop", "1", "-i", os.path.join(work, "degrade.png"),
             "-filter_complex",
             f"[0:v][4:v]overlay=0:0:enable='lt(t,{total - fin_dur:.2f})':shortest=1[g];"
             f"[g]subtitles='{ass}':fontsdir='{FONTS}'[s];"
             f"[2:v]format=rgba,fade=out:st=3.2:d=0.3:alpha=1[ti];"
             f"[s][ti]overlay=0:0:enable='lt(t,3.5)':shortest=1[s2];"
             f"[s2][3:v]overlay=0:0:enable='lt(t,{total - fin_dur:.2f})':shortest=1,format=yuv420p[v];"
             "[1:a]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]",
             "-map", "[v]", "-map", "[a]", "-t", f"{total:.3f}", "-c:v", "libx264", "-crf", "18", "-preset", "slow",
             "-profile:v", "high", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart",
             os.path.join(d, name)])
        print("OK", name)

    # 7. apercu : une image par plan
    thumbs = []
    for k, s in enumerate(segs):
        fr = os.path.join(work, f"apercu_{k:02d}.jpg")
        run(["ffmpeg", "-loglevel", "error", "-y", "-ss", f"{s['start'] + s['dur'] * 0.6:.2f}", "-i",
             os.path.join(d, "final.mp4"), "-frames:v", "1", "-vf", "scale=270:480", fr])
        thumbs.append(fr)
    cols = 10
    sheet = Image.new("RGB", (270 * cols, 480 * ((len(thumbs) + cols - 1) // cols)), "black")
    for k, f in enumerate(thumbs):
        sheet.paste(Image.open(f), ((k % cols) * 270, (k // cols) * 480))
    sheet.save(os.path.join(d, "apercu.jpg"), quality=85)
    json.dump({"duree": round(total, 2), "plans": [{"id": s["p"]["id"], "debut": round(s["start"], 2),
                                                     "duree": s["dur"]} for s in segs]},
              open(os.path.join(work, "timeline.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
