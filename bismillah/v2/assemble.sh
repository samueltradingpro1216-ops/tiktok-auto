#!/usr/bin/env bash
# Assemble les 7 scenes chantees en une video YouTube 1920x1080 avec le son natif.
# - mise a l'echelle 1280x704 -> 1920x1080 (leger recadrage vertical)
# - fondu audio de 0,15 s en debut/fin de chaque scene (pas de clic aux coupes)
# - volume egalise (loudnorm -14 LUFS, standard YouTube)
# - paroles incrustees depuis paroles.srt
set -euo pipefail
cd "$(dirname "$0")"
TMP=$(mktemp -d)
for i in 1 2 3 4 5 6 7; do
  ffmpeg -v error -y -i "scenes/scene_$i.mp4" \
    -vf "scale=1964:1080:flags=lanczos,crop=1920:1080,setsar=1,fps=24" \
    -af "afade=t=in:d=0.15,afade=t=out:st=9.85:d=0.15,aresample=48000" \
    -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -ac 2 \
    "$TMP/s$i.mp4"
  echo "file '$TMP/s$i.mp4'" >> "$TMP/list.txt"
done
ffmpeg -v error -y -f concat -safe 0 -i "$TMP/list.txt" -c copy "$TMP/concat.mp4"
ffmpeg -v error -y -i "$TMP/concat.mp4" \
  -vf "subtitles=paroles.srt:force_style='FontName=DejaVu Sans,Bold=1,Fontsize=22,PrimaryColour=&H00FFFFFF,OutlineColour=&H00402080,BorderStyle=1,Outline=3,Shadow=1,Alignment=2,MarginV=28'" \
  -af "loudnorm=I=-14:TP=-1.5:LRA=11" \
  -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart \
  bismillah_comptine_youtube.mp4
rm -rf "$TMP"
echo "OK -> bismillah_comptine_youtube.mp4"
