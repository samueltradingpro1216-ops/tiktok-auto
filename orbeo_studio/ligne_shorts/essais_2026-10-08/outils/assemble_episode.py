"""Automated vertical episode assembly test (ffmpeg + faster-whisper word timings + ASS captions).
Steps: trim/normalize clips -> blur band hiding model-burned pseudo-subtitles -> concat -> end card ->
word-timed karaoke captions aligned on the SCRIPT text -> hook title + episode badge -> loudnorm -> 1080x1920."""
import difflib, json, re, subprocess, sys, time
from faster_whisper import WhisperModel
T0 = time.time()
D = "/tmp/claude-0/-home-user-tiktok-auto/c3103019-a176-5027-8bcf-8e27361d44f5/scratchpad/tests_tiktok"
M = f"{D}/montage"
def sh(cmd):
    subprocess.run(cmd, shell=True, check=True)
W, H = 1080, 1920
# band (fraction of height) where the video model burns gibberish subtitles (measured on 3 clips: 75-87 %)
BY0, BY1 = 0.735, 0.885
NORM = (f"scale={W}:-2:flags=lanczos,crop={W}:{H},fps=24,setsar=1,"
        f"split[a][b];[b]crop={W}:{int((BY1-BY0)*H)}:0:{int(BY0*H)},boxblur=24:3[bl];[a][bl]overlay=0:{int(BY0*H)}")
clips = [("vidC_v20_neg.mp4", 2.0, None), ("vidD_v20_closeup.mp4", 0.0, None)]
parts = []
for i, (f, ss, to) in enumerate(clips):
    out = f"{M}/p{i}.mp4"
    sh(f'ffmpeg -v error -y -ss {ss} -i {D}/{f} -filter_complex "[0:v]{NORM}[v]" -map "[v]" -map 0:a '
       f'-c:v libx264 -preset veryfast -crf 18 -c:a aac -ar 48000 -ac 2 {out}')
    parts.append(out)
# end card: last frame of last clip, darkened, 2 s, with cliffhanger text (rendered later by ASS)
sh(f'ffmpeg -v error -y -sseof -0.1 -i {parts[-1]} -frames:v 1 {M}/last.png')
sh(f'ffmpeg -v error -y -loop 1 -t 2.0 -i {M}/last.png -f lavfi -t 2.0 -i anullsrc=r=48000:cl=stereo '
   f'-vf "fps=24,eq=brightness=-0.25,gblur=sigma=8,format=yuv420p" -c:v libx264 -preset veryfast -crf 18 -c:a aac -shortest {M}/end.mp4')
parts.append(f"{M}/end.mp4")
open(f"{M}/list.txt", "w").write("".join(f"file '{p}'\n" for p in parts))
sh(f"ffmpeg -v error -y -f concat -safe 0 -i {M}/list.txt -c copy {M}/concat.mp4")
dur = float(subprocess.check_output(f"ffprobe -v error -show_entries format=duration -of csv=p=0 {M}/concat.mp4", shell=True))
sh(f"ffmpeg -v error -y -i {M}/concat.mp4 -vn -ac 1 -ar 16000 {M}/concat.wav")
# word timings from ASR, text from SCRIPT (so captions never show ASR errors like 'métière')
SCRIPT = ["Encore en retard, Baguette !", "Pardon ! Le four m'a fait peur !", "Dix ans de métier, et toujours pas de respect !"]
model = WhisperModel("small", device="cpu", compute_type="int8")
segs, _ = model.transcribe(f"{M}/concat.wav", language="fr", word_timestamps=True)
asr = [(w.word.strip(), w.start, w.end) for s in segs for w in s.words]
norm = lambda s: re.sub(r"[^a-zàâçéèêëîïôûùüÿœ0-9]", "", s.lower())
sw = [w for line in SCRIPT for w in line.split() if norm(w)]
line_of = [li for li, line in enumerate(SCRIPT) for w in line.split() if norm(w)]
digits = {"10": "dix"}
a_norm = [digits.get(norm(w), norm(w)) for w, _, _ in asr]
sm = difflib.SequenceMatcher(a=[norm(w) for w in sw], b=a_norm, autojunk=False)
timing = [None] * len(sw)
for blk in sm.get_matching_blocks():
    for k in range(blk.size):
        timing[blk.a + k] = asr[blk.b + k][1:]
for k in range(len(sw)):  # interpolate unmatched words
    if timing[k] is None:
        prev = next((timing[j] for j in range(k - 1, -1, -1) if timing[j]), (0, 0))
        nxt = next((timing[j] for j in range(k + 1, len(sw)) if timing[j]), (prev[1] + 0.4, prev[1] + 0.8))
        timing[k] = (prev[1], max(prev[1] + 0.15, nxt[0]))
matched = sum(1 for b in sm.get_matching_blocks() for _ in range(b.size))
def ts(t):
    t = max(0, t); return f"{int(t//3600)}:{int(t%3600//60):02d}:{t%60:05.2f}"
ass = [
"[Script Info]", "ScriptType: v4.00+", f"PlayResX: {W}", f"PlayResY: {H}", "",
"[V4+ Styles]",
"Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
"Style: Cap,DejaVu Sans,88,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,7,3,2,60,60,300,1",
"Style: Hook,DejaVu Sans,76,&H0000E5FF,&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,0,0,1,7,0,8,60,60,230,1",
"Style: Badge,DejaVu Sans,46,&H00FFFFFF,&H00FFFFFF,&H00000000,&HC0202020,1,0,0,0,100,100,0,0,3,10,0,7,50,50,120,1",
"Style: End,DejaVu Sans,84,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,0,0,1,6,0,5,80,80,0,1",
"", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
ass.append(f"Dialogue: 2,{ts(0)},{ts(dur)},Badge,,0,0,0,,ÉP. 1 · LA BOULANGERIE")
ass.append(f"Dialogue: 3,{ts(0)},{ts(1.6)},Hook,,0,0,0,,{{\\fad(0,250)}}IL A 10 ANS DE MÉTIER...\\NET ZÉRO PATIENCE")
# captions: chunks of <=3 words, current word highlighted in yellow and slightly scaled (TikTok style)
CH = 3
chunks = []
for li in range(len(SCRIPT)):
    idx = [k for k in range(len(sw)) if line_of[k] == li]
    chunks += [idx[i:i + CH] for i in range(0, len(idx), CH)]
for ci, chunk in enumerate(chunks):
    nxt0 = timing[chunks[ci + 1][0]][0] if ci + 1 < len(chunks) else 1e9
    for j in chunk:
        st = timing[j][0]; en = timing[j + 1][0] if j + 1 in chunk else min(timing[j][1] + 0.25, nxt0)
        txt = " ".join(("{\\c&H0000E5FF&\\fscx112\\fscy112}" + sw[k].upper() + "{\\r}") if k == j else sw[k].upper() for k in chunk)
        ass.append(f"Dialogue: 1,{ts(st)},{ts(en)},Cap,,0,0,0,,{txt}")
ass.append(f"Dialogue: 4,{ts(dur-2.0)},{ts(dur)},End,,0,0,0,,{{\\fad(200,0)}}DEMAIN :\\NBaguette démissionne ?!\\N{{\\fs56}}ÉP. 2 · abonne-toi")
open(f"{M}/caps.ass", "w").write("\n".join(ass) + "\n")
sh(f'ffmpeg -v error -y -i {M}/concat.mp4 -vf "ass={M}/caps.ass" -af "loudnorm=I=-14:TP=-1.5:LRA=11" '
   f'-c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -ar 48000 -movflags +faststart {M}/episode_test.mp4')
print(json.dumps({"duration_s": round(dur, 2), "script_words": len(sw), "asr_words": len(asr), "matched": matched,
                  "wall_s": round(time.time() - T0, 1)}))
