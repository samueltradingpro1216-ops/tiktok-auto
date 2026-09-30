#!/usr/bin/env python3
"""Transcrit une chanson mot par mot (faster-whisper) : JSON {"text", "words": [{"w", "start", "end"}]}."""

import json
import sys

from faster_whisper import WhisperModel

model = WhisperModel(sys.argv[2] if len(sys.argv) > 2 else "small", device="cpu", compute_type="int8")
segments, _ = model.transcribe(sys.argv[1], language="fr", word_timestamps=True, vad_filter=False)
words, text = [], []
for s in segments:
    text.append(s.text.strip())
    for w in s.words or []:
        words.append({"w": w.word.strip(), "start": round(w.start, 2), "end": round(w.end, 2)})
print(json.dumps({"text": " ".join(text), "words": words}, ensure_ascii=False))
