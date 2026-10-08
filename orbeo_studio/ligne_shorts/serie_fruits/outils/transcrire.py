#!/usr/bin/env python3
"""Transcrit des repliques (faster-whisper small, francais) avec le temps de chaque mot ; JSON sur stdout."""
import json
import sys

from faster_whisper import WhisperModel

model = WhisperModel("small", device="cpu", compute_type="int8")
out = []
for path in sys.argv[1:]:
    segs, _ = model.transcribe(path, language="fr", word_timestamps=True, vad_filter=False, beam_size=5)
    words = [{"word": w.word.strip(), "start": round(w.start, 2), "end": round(w.end, 2), "p": round(w.probability, 2)}
             for s in segs for w in (s.words or [])]
    out.append({"file": path, "words": words})
print(json.dumps(out, ensure_ascii=False))
