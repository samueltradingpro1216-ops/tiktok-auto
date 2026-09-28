#!/usr/bin/env python3
"""Transcrit le chant de clips video (faster-whisper) et affiche un JSON sur stdout."""

import json
import sys

from faster_whisper import WhisperModel

model = WhisperModel("small", device="cpu", compute_type="int8")
results = []
for path in sys.argv[1:]:
    segments, _ = model.transcribe(path, language="fr", vad_filter=False)
    results.append({"file": path, "segments": [
        {"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip()} for s in segments]})
print(json.dumps(results, ensure_ascii=False))
