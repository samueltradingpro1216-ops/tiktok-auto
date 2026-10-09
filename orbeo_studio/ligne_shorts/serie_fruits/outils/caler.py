#!/usr/bin/env python3
"""Recale chaque clip sur sa nouvelle voix (voix clonee) : le personnage prononcait chaque mot a un moment donne
dans le clip d'origine ; on deforme le temps de l'image, morceau par morceau, pour que chaque mot tombe au moment
ou la nouvelle voix le dit. Les levres restent ainsi synchronisees, au debit de la nouvelle voix.

Usage : ~/agnes-video-generator/.venv/bin/python caler.py ../episodes/01_la_bague [--plans 1,4]
Entrees : clips/pXX.mp4, state.json (mots du clip), voix/pXX_clone.wav, controle/voix_clonees.json (mots de la voix)
Sorties : clips/pXX_cale.mp4 (image recalee + voix clonee), controle/pXX_cale.json (mots et duree)

Rythme (episode.json, « montage ») : « tempo_voix » ralentit la voix sans changer sa hauteur (0.85 = 15 % plus lent ;
un nombre, ou par personnage {"*": 0.85, "prune": 1.0}), « pauses » ajoute un temps de respiration apres la
ponctuation (« … », « . », « ? », « , »), et « effets_voix » ajoute un filtre ffmpeg par personnage (ex. un leger
tremblement pour la grand-mere).
"""
import argparse, difflib, json, os, re, subprocess, unicodedata

import numpy as np

FPS = 24
SR = 24000
LEAD, TAIL = 0.12, 0.45  # secondes gardees avant le premier mot et apres le dernier
PAUSES = {"…": 0.32, "?": 0.24, "!": 0.24, ".": 0.24, ":": 0.16, ";": 0.16, ",": 0.12}  # silence ajoute (s)


def norm(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "", t)


def script_times(tokens, words):
    """Debut de chaque mot du script dans une liste de mots minutes (None si non retrouve)."""
    a = [norm(t) for t in tokens]
    b = [norm(w["word"]) for w in words]
    out = [None] * len(tokens)
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == "equal":
            for k in range(i2 - i1):
                out[i1 + k] = (words[j1 + k]["start"], words[j1 + k]["end"])
    return out


def anchors(tokens, src_words, new_words):
    s, n = script_times(tokens, src_words), script_times(tokens, new_words)
    pts = [(nw[0], sw[0]) for sw, nw in zip(s, n) if sw and nw]
    if src_words and new_words:
        pts.append((new_words[-1]["end"], src_words[-1]["end"]))
        pts.insert(0, (new_words[0]["start"], src_words[0]["start"]))
    pts = sorted(set(pts))
    clean = []
    for t_new, t_src in pts:  # temps croissants des deux cotes, et vitesse locale raisonnable (0,4x a 3x)
        if clean:
            dn, ds = t_new - clean[-1][0], t_src - clean[-1][1]
            if dn <= 0.04 or ds <= 0 or not (0.4 <= ds / dn <= 3.0):
                continue
        clean.append((t_new, t_src))
    return clean


def respirer(wav, out, tokens, words, tempo, pauses, effet=""):
    """Ralentit la voix (hauteur gardee) et ajoute un silence apres chaque mot suivi d'une ponctuation.
    Rend les mots avec leurs nouveaux temps."""
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", wav, "-af",
                          f"rubberband=tempo={tempo}:pitchq=quality" + (f",{effet}" if effet else ""),
                          "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True).stdout
    audio = np.frombuffer(raw, np.float32)
    words = [{**w, "start": w["start"] / tempo, "end": w["end"] / tempo} for w in words]
    cuts = []  # (instant de coupe, duree du silence)
    if pauses:
        for (tok, t), nxt in zip(zip(tokens, script_times(tokens, words)), tokens[1:]):
            mark = next((m for m in PAUSES if tok.endswith(m) or nxt == m), None)
            if not t or not mark:
                continue
            after = [w["start"] for w in words if w["start"] >= t[1] - 0.01]
            if after:
                cuts.append(((t[1] + after[0]) / 2, PAUSES[mark]))
    pieces, pos = [], 0
    for cut, dur in sorted(cuts):
        k = int(cut * SR)
        pieces += [audio[pos:k], np.zeros(int(dur * SR), np.float32)]
        pos = k
    pieces.append(audio[pos:])
    shift = lambda t: t + sum(dur for cut, dur in cuts if t >= cut)  # noqa: E731
    words = [{**w, "start": shift(w["start"]), "end": shift(w["end"])} for w in words]
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", out],
                   input=np.concatenate(pieces).tobytes(), check=True)
    return [{**w, "start": round(w["start"], 3), "end": round(w["end"], 3)} for w in words]


def bornes(wav, debut, fin, seuil_db=-30, trou=0.05, max_fin=0.3):
    """Debut et fin reels de la voix autour des temps whisper : whisper place souvent le premier mot trop tard, et
    couper l'attaque d'un mot le rend incomprehensible (« Cerise » entendu « Riz »). On prolonge tant que la voix
    reste au-dessus du seuil sans trou de plus de 50 ms (une respiration isolee ou un bruit apres la phrase ne
    comptent pas) ; la fin n'est jamais prolongee de plus de 0,3 s."""
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", wav, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.float32)
    hop = SR // 100
    rms = np.sqrt(np.mean(x[:len(x) // hop * hop].reshape(-1, hop) ** 2, axis=1))
    on = rms > rms.max() * 10 ** (seuil_db / 20)
    gap = int(trou * 100)

    def walk(k, step, limit):  # avance de k vers limit (incluse) tant que la voix continue
        last, miss = k, 0
        while k != limit:
            k += step
            if on[k]:
                last, miss = k, 0
            else:
                miss += 1
                if miss > gap:
                    break
        return last

    k0 = min(max(int(debut * 100), 0), len(on) - 1)
    k1 = min(max(int(fin * 100), 0), len(on) - 1)
    d = walk(k0, -1, 0) / 100
    f = (walk(k1, 1, min(len(on) - 1, k1 + int(max_fin * 100))) + 1) / 100
    return min(debut, d), max(fin, f)


def frames(path, w, h):
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", path, "-vf", f"fps={FPS}", "-f", "rawvideo",
                          "-pix_fmt", "rgb24", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, h, w, 3)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ep")
    ap.add_argument("--plans", default="")
    a = ap.parse_args()
    d = os.path.abspath(a.ep)
    ep = json.load(open(os.path.join(d, "episode.json"), encoding="utf-8"))
    st = json.load(open(os.path.join(d, "state.json")))
    clones = json.load(open(os.path.join(d, "controle", "voix_clonees.json")))
    reglages = ep.get("montage", {})
    tempos, pauses = reglages.get("tempo_voix", 1.0), bool(reglages.get("pauses"))
    if not isinstance(tempos, dict):
        tempos = {"*": tempos}
    effets = reglages.get("effets_voix", {})
    only = {int(x) for x in a.plans.split(",") if x}
    for p in ep["plans"]:
        key = str(p["id"])
        if not p.get("parle") or key not in clones or (only and p["id"] not in only):
            continue
        cs = st["clips"].get(key, {})
        best = next((t for t in cs.get("tries", []) if t.get("file") == cs.get("best")), None)
        clip = os.path.join(d, "clips", f"p{p['id']:02d}.mp4")
        wav = os.path.join(d, "voix", f"p{p['id']:02d}_clone.wav")
        if not best or not best.get("words") or not os.path.exists(clip) or not os.path.exists(wav):
            continue
        tokens = p["replique"].split()
        new_words = clones[key]["words"]
        tempo = float(tempos.get(p["parle"], tempos.get("*", 1.0)))
        if tempo != 1.0 or pauses or effets.get(p["parle"]):
            wav_lent = os.path.join(d, "voix", f"p{p['id']:02d}_clone_rythme.wav")
            new_words = respirer(wav, wav_lent, tokens, new_words, tempo, pauses, effets.get(p["parle"], ""))
            wav = wav_lent
        new_words = [dict(w) for w in new_words]
        new_words[0]["start"], new_words[-1]["end"] = bornes(wav, new_words[0]["start"], new_words[-1]["end"])
        pts = anchors(tokens, best["words"], new_words)
        if len(pts) < 2:  # repliques tres courtes : on cale au moins le debut et la fin de la parole
            sw, nw = best["words"], new_words
            if nw[-1]["end"] > nw[0]["start"] and sw[-1]["end"] > sw[0]["start"]:
                pts = [(nw[0]["start"], sw[0]["start"]), (nw[-1]["end"], sw[-1]["end"])]
        if len(pts) < 2:
            print(f"plan {p['id']} : pas assez de reperes, saute")
            continue
        w, h = map(int, subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries",
                                        "stream=width,height", "-of", "csv=p=0", clip],
                                       capture_output=True, text=True, check=True).stdout.strip().split(","))
        src = frames(clip, w, h)
        src_dur = len(src) / FPS
        t0 = max(0.0, new_words[0]["start"] - LEAD)
        t1 = new_words[-1]["end"] + TAIL
        n_out = int(round((t1 - t0) * FPS))
        tn = np.array([q[0] for q in pts])
        ts = np.array([q[1] for q in pts])
        out_frames = []
        for k in range(n_out):
            t = t0 + k / FPS
            if t <= tn[0]:
                s = ts[0] - (tn[0] - t)
            elif t >= tn[-1]:
                s = ts[-1] + (t - tn[-1])
            else:
                s = float(np.interp(t, tn, ts))
            out_frames.append(src[min(max(int(round(s * FPS)), 0), len(src) - 1)])
        out = os.path.join(d, "clips", f"p{p['id']:02d}_cale.mp4")
        enc = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
                                "-s", f"{w}x{h}", "-r", str(FPS), "-i", "-", "-ss", f"{t0:.3f}", "-t",
                                f"{t1 - t0:.3f}", "-i", wav, "-map", "0:v", "-map", "1:a", "-c:v", "libx264",
                                "-crf", "16", "-preset", "medium", "-pix_fmt", "yuv420p", "-af", "apad", "-c:a", "aac",
                                "-b:a", "192k", "-t", f"{n_out / FPS:.3f}", out], stdin=subprocess.PIPE)
        # duree exacte : la voix peut finir avant la marge de fin, on complete par du silence (sinon le clip est
        # plus court que prevu et le montage se decale)
        enc.stdin.write(np.stack(out_frames).tobytes())
        enc.stdin.close()
        enc.wait()
        words = [{"word": x["word"], "start": round(x["start"] - t0, 2), "end": round(x["end"] - t0, 2)}
                 for x in new_words]
        info = {"words": words, "speech": [words[0]["start"], words[-1]["end"]], "duration": round(n_out / FPS, 3),
                "reperes": len(pts), "vitesse_moyenne": round((ts[-1] - ts[0]) / max(tn[-1] - tn[0], 0.1), 2),
                "source_s": round(src_dur, 2)}
        json.dump(info, open(os.path.join(d, "controle", f"p{p['id']:02d}_cale.json"), "w"), ensure_ascii=False)
        print(f"plan {p['id']} : {len(pts)} reperes, image x{info['vitesse_moyenne']} -> {info['duration']} s", flush=True)


if __name__ == "__main__":
    main()
