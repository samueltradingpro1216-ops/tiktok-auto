import sys
from faster_whisper import WhisperModel
m = WhisperModel("small", device="cpu", compute_type="int8")
for f in sys.argv[1:]:
    segs, info = m.transcribe(f, language="fr", word_timestamps=True, vad_filter=False)
    print("==", f, "lang_prob", round(info.language_probability, 2), "dur", round(info.duration, 2))
    for s in segs:
        print(f"  [{s.start:5.2f}-{s.end:5.2f}] {s.text}  (avg_logprob {s.avg_logprob:.2f}, no_speech {s.no_speech_prob:.2f})")
    segs2, info2 = m.transcribe(f, language=None)
    print("  autodetect:", info2.language, round(info2.language_probability, 2), "|", " ".join(s.text for s in segs2))
