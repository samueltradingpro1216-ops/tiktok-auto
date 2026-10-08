#!/usr/bin/env python3
"""Analyse une video de reference (TikTok, Reel, Short) : plans, images, script minute, musique.

Usage : python analyse_reference.py video.mp4 [--whisper-python ~/ace-venv/bin/python]
Produit a cote de la video : <nom>_planche.jpg (une image par plan), <nom>_debut.jpg (les 3 premieres secondes),
<nom>_analyse.json et <nom>_analyse.md (plans, rythme, script avec temps, musique reconnue).
"""
import argparse
import asyncio
import json
import os
import re
import subprocess
import sys


def run(cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True)


def duration(path):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]).stdout)


def cuts(path, threshold=0.3):
    """Instants des changements de plan (detection de scene ffmpeg)."""
    p = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-vf", f"select='gt(scene,{threshold})',showinfo",
                        "-f", "null", "-"], capture_output=True, text=True)
    return [float(t) for t in re.findall(r"pts_time:([0-9.]+)", p.stderr)]


def sheet(path, times, out, cols=6, w=180):
    frames = []
    for i, t in enumerate(times):
        f = f"{out}_f{i:03d}.jpg"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", path, "-frames:v", "1",
                        "-vf", f"scale={w}:-2,drawtext=text='{t:.1f}s':x=4:y=4:fontsize=16:fontcolor=yellow:"
                        "borderw=2", f], check=False)
        if os.path.exists(f):
            frames.append(f)
    if not frames:
        return None
    rows = (len(frames) + cols - 1) // cols
    inputs = sum((["-i", f] for f in frames), [])
    pad = cols * rows - len(frames)
    fc = "".join(f"[{i}]" for i in range(len(frames)))
    if pad:
        fc = ";".join([f"color=c=black:s={w}x{int(w * 16 / 9)}:d=1[p{j}]" for j in range(pad)]) + ";" + fc + \
             "".join(f"[p{j}]" for j in range(pad))
    fc += f"xstack=inputs={len(frames) + pad}:layout=" + "|".join(
        f"{'+'.join(['w0'] * (k % cols)) or '0'}_{'+'.join(['h0'] * (k // cols)) or '0'}" for k in range(len(frames) + pad))
    subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", fc, "-frames:v", "1", out + ".jpg"],
                   check=False)
    for f in frames:
        os.remove(f)
    return out + ".jpg" if os.path.exists(out + ".jpg") else None


def transcribe(path, whisper_python):
    code = ("import json,sys\nfrom faster_whisper import WhisperModel\n"
            "m=WhisperModel('small',device='cpu',compute_type='int8')\n"
            "segs,info=m.transcribe(sys.argv[1],language=None,vad_filter=True)\n"
            "print(json.dumps({'langue':info.language,'segments':[{'debut':round(s.start,1),'fin':round(s.end,1),"
            "'texte':s.text.strip()} for s in segs]},ensure_ascii=False))")
    r = subprocess.run([whisper_python, "-c", code, path], capture_output=True, text=True)
    try:
        return json.loads(r.stdout.strip().splitlines()[-1])
    except Exception:
        return {"erreur": r.stderr[-500:]}


async def shazam(path, dur):
    """Essaie de reconnaitre la musique sur plusieurs extraits de 12 s."""
    try:
        from shazamio import Shazam
    except ImportError:
        return {"erreur": "shazamio absent"}
    sh, found = Shazam(), []
    for start in [max(0, dur * f) for f in (0.05, 0.35, 0.65, 0.9)]:
        clip = f"{path}.shz_{int(start)}.ogg"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{start:.1f}", "-t", "12", "-i", path, "-vn",
                        "-ac", "1", "-ar", "16000", clip], check=False)
        try:
            r = await sh.recognize(clip)
            t = r.get("track")
            if t:
                found.append({"a": round(start), "titre": t.get("title"), "artiste": t.get("subtitle")})
        except Exception as e:
            found.append({"a": round(start), "erreur": str(e)[:80]})
        finally:
            if os.path.exists(clip):
                os.remove(clip)
    return found


def main():
    p = argparse.ArgumentParser()
    p.add_argument("video")
    p.add_argument("--whisper-python", default=os.path.expanduser("~/ace-venv/bin/python"))
    a = p.parse_args()
    v = os.path.abspath(a.video)
    base = os.path.splitext(v)[0]
    dur = duration(v)
    cs = cuts(v)
    shots = [0.0] + cs
    lengths = [b - a_ for a_, b in zip(shots, shots[1:] + [dur])]
    planche = sheet(v, [s + 0.3 for s in shots][:48], base + "_planche")
    debut = sheet(v, [0.1, 0.6, 1.2, 1.8, 2.4, 3.0], base + "_debut", cols=6, w=240)
    tr = transcribe(v, a.whisper_python)
    music = asyncio.run(shazam(v, dur))
    meta = {}
    if os.path.exists(base + ".json"):
        meta = json.load(open(base + ".json", encoding="utf-8"))
    res = {"video": v, "duree_s": round(dur, 1), "plans": len(shots),
           "duree_moyenne_plan_s": round(dur / len(shots), 2), "plans_debuts_s": [round(s, 1) for s in shots],
           "plus_long_plan_s": round(max(lengths), 1), "transcription": tr, "musique_reconnue": music, "meta": meta}
    json.dump(res, open(base + "_analyse.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    lines = [f"# Analyse de {os.path.basename(v)}", ""]
    if meta:
        st = meta.get("stats") or {}
        lines += [f"- Auteur : @{meta.get('auteur')} ; légende : {meta.get('legende')}",
                  f"- Vues : {st.get('playCount')} ; likes : {st.get('diggCount')} ; commentaires : "
                  f"{st.get('commentCount')} ; partages : {st.get('shareCount')} ; enregistrements : {st.get('collectCount')}",
                  f"- Son TikTok : {meta.get('son', {}).get('titre')} / {meta.get('son', {}).get('auteur')}"]
    lines += [f"- Durée : {res['duree_s']} s ; {res['plans']} plans ; un plan toutes les {res['duree_moyenne_plan_s']} s "
              f"en moyenne (le plus long : {res['plus_long_plan_s']} s)",
              f"- Musique reconnue (Shazam) : {music}", "", "## Script minuté", ""]
    for s in tr.get("segments", []):
        lines.append(f"- {s['debut']:>5.1f} à {s['fin']:>5.1f} s : {s['texte']}")
    lines += ["", f"Planche : {os.path.basename(planche or '')} ; début : {os.path.basename(debut or '')}"]
    open(base + "_analyse.md", "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
