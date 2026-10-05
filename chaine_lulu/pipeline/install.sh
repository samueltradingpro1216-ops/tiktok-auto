#!/usr/bin/env bash
# Installe les outils de fabrication d'un episode sur une machine Linux neuve (session cloud, sans GPU).
# Duree : ~5 min (dont ~7 Go de modeles ACE-Step). Peut servir de script de configuration de l'environnement.
#   ~/acestep               ACE-Step 1.5 (chanson) + modeles dans ~/acestep/checkpoints
#   ~/ace-venv              python pour ACE-Step et faster-whisper (WHISPER_PYTHON)
#   ~/agnes-video-generator serveur images/videos Agnes (demande la cle AGNES_API_KEY)
set -e

[ -d ~/acestep ] || git clone -q --depth 1 https://github.com/ace-step/ACE-Step-1.5 ~/acestep
if [ ! -x ~/ace-venv/bin/python ]; then
  python3 -m venv ~/ace-venv
  ~/ace-venv/bin/pip install -q --upgrade pip
  ~/ace-venv/bin/pip install -q torch torchaudio --index-url https://download.pytorch.org/whl/cpu
  ~/ace-venv/bin/pip install -q "transformers>=4.51.0,<4.58.0" diffusers scipy soundfile loguru einops accelerate \
    numba vector-quantize-pytorch "torchao>=0.16.0,<0.17.0" toml modelscope diskcache safetensors peft matplotlib \
    xxhash huggingface_hub faster-whisper
  ~/ace-venv/bin/pip install -q -e ~/acestep --no-deps
fi
~/ace-venv/bin/python - <<'PY'
import os
from huggingface_hub import snapshot_download
d = os.path.expanduser("~/acestep/checkpoints")
snapshot_download("ACE-Step/Ace-Step1.5", local_dir=d,
                  allow_patterns=["acestep-v15-turbo/*", "vae/*", "Qwen3-Embedding-0.6B/*", "config.json"])
snapshot_download("ACE-Step/acestep-5Hz-lm-0.6B", local_dir=os.path.join(d, "acestep-5Hz-lm-0.6B"))
PY

[ -d ~/agnes-video-generator ] || git clone -q --depth 1 https://github.com/lcy362/agnes-video-generator ~/agnes-video-generator
if [ ! -x ~/agnes-video-generator/.venv/bin/python ]; then
  python3 -m venv ~/agnes-video-generator/.venv
  ~/agnes-video-generator/.venv/bin/pip install -q -r ~/agnes-video-generator/requirements.txt
fi
echo "Installation terminee."
