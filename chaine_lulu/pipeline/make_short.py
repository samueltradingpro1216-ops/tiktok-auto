#!/usr/bin/env python3
"""Fabrique un Short vertical (1080x1920) a partir d'un episode monte : quelques sections d'affilee.

Mise en page : fond flou tire de la video, video 16:9 au centre, titre en haut, paroles en gros sous la video
(calees sur le chant), nom de la serie en bas. Prend la version sans sous-titres (clips/concat.mp4) si elle
existe, sinon la video finale. Le son vient de la video finale (deja au volume YouTube).

Usage : python make_short.py ../episodes/02_peur_du_noir --sections 2-4 --title "Lulu, Lulu,|allume-toi !"
"""

import argparse
import json
import os
import subprocess

FONTS = os.environ.get("SHORT_FONTS", os.path.expanduser("~/fonts"))  # LuckiestGuy.ttf, Fredoka.ttf


def ass_time(t):
    cs = int(round(t * 100))
    return f"{cs // 360000}:{cs // 6000 % 60:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("episode_dir")
    p.add_argument("--sections", required=True, help="ex. 2-4 (sections incluses)")
    p.add_argument("--title", required=True, help="titre en haut, lignes separees par |")
    p.add_argument("--footer", default="Lulu la Luciole|La comptine en entier sur la chaîne")
    a = p.parse_args()

    d = os.path.abspath(a.episode_dir)
    ep = json.load(open(os.path.join(d, "episode.json"), encoding="utf-8"))
    st = json.load(open(os.path.join(d, "state.json"), encoding="utf-8"))
    first, last = (int(x) for x in a.sections.split("-"))
    secs = {s["id"]: s for s in st["sections"]}
    t0, t1 = secs[first]["start"], secs[last]["end"]
    dur = t1 - t0
    final = os.path.join(d, f"{ep['slug']}_youtube.mp4")
    clean = os.path.join(d, "clips", "concat.mp4")
    video = clean if os.path.exists(clean) else final
    # sans version propre, on coupe la bande du bas ou les paroles sont deja incrustees
    crop = "" if video == clean else "crop=1920:690:0:0,"

    ass = os.path.join(d, "clips", f"short_s{first}-{last}.ass")
    os.makedirs(os.path.dirname(ass), exist_ok=True)
    with open(ass, "w", encoding="utf-8") as f:
        f.write("[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\n\n[V4+ Styles]\n"
                "Format: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, BackColour, Bold, BorderStyle, "
                "Outline, Shadow, Alignment, MarginL, MarginR, MarginV\n"
                "Style: Paroles,Fredoka,70,&H00FFFFFF,&H006B3023,&H80000000,-1,1,6,2,8,60,60,1230\n\n"
                "[Events]\nFormat: Layer, Start, End, Style, Text\n")
        sung = [l for l in st["song"]["lines"] if l.get("sung", True)]
        for i, l in enumerate(sung):
            if l["end"] <= t0 or l["start"] >= t1:
                continue
            nxt = sung[i + 1]["start"] if i + 1 < len(sung) else t1
            # une seule ligne a l'ecran a la fois (sinon libass les empile vers le bas)
            s, e = max(l["start"], t0) - t0, min(l["end"] + 0.3, nxt, t1) - t0
            f.write(f"Dialogue: 0,{ass_time(s)},{ass_time(e)},Paroles,{l['text']}\n")

    title = a.title.split("|")
    foot = a.footer.split("|")
    lg, fr = os.path.join(FONTS, "LuckiestGuy.ttf"), os.path.join(FONTS, "Fredoka.ttf")

    def esc(t):
        return t.replace("\\", "\\\\").replace(":", "\\:").replace("'", "’")

    draw = []
    for i, line in enumerate(title):
        draw.append(f"drawtext=fontfile={lg}:text='{esc(line)}':fontsize=118:fontcolor=#FFD84D:borderw=10:"
                    f"bordercolor=#23306B:x=(w-tw)/2:y={230 + i * 140}")
    draw.append(f"drawtext=fontfile={lg}:text='{esc(foot[0])}':fontsize=76:fontcolor=#FFD84D:borderw=7:"
                f"bordercolor=#23306B:x=(w-tw)/2:y=1680")
    if len(foot) > 1:
        draw.append(f"drawtext=fontfile={fr}:text='{esc(foot[1])}':fontsize=46:fontcolor=white:borderw=5:"
                    f"bordercolor=#23306B:x=(w-tw)/2:y=1780")
    out = os.path.join(d, f"{ep['slug']}_short.mp4")
    fc = (f"[0:v]{crop}split[b][f];[b]scale=-2:1920,crop=1080:1920,boxblur=28:2,eq=brightness=-0.12[bg];"
          f"[f]scale=1080:-2:flags=lanczos[fg];[bg][fg]overlay=0:556,"
          f"subtitles={ass}:fontsdir={FONTS}," + ",".join(draw) +
          f",fade=t=out:st={dur - 0.6:.2f}:d=0.6[v];"
          f"[1:a]afade=t=out:st={dur - 0.8:.2f}:d=0.8[a]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t0:.3f}", "-t", f"{dur:.3f}", "-i", video,
                    "-ss", f"{t0:.3f}", "-t", f"{dur:.3f}", "-i", final, "-filter_complex", fc,
                    "-map", "[v]", "-map", "[a]", "-r", "30", "-c:v", "libx264", "-crf", "20", "-preset", "medium",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out],
                   check=True)
    print(f"{out} ({dur:.1f} s)")


if __name__ == "__main__":
    main()
