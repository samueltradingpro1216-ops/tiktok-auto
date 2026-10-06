#!/usr/bin/env bash
# Installe les outils de fabrication d'un episode sur une machine Linux neuve (session cloud, sans GPU).
# Duree : ~5 min (dont ~7 Go de modeles ACE-Step). Peut servir de script de configuration de l'environnement.
#   ~/acestep               ACE-Step 1.5 (chanson) + modeles dans ~/acestep/checkpoints
#   ~/ace-venv              python pour ACE-Step et faster-whisper (WHISPER_PYTHON)
#   ~/agnes-video-generator serveur images/videos Agnes (demande la cle AGNES_API_KEY)
set -e

# ACE-Step sur CPU occupe ~13,7 Go alors que la session est limitee a ~14,3 Go de memoire vive : sans
# fichier d'echange, le moindre programme lance en parallele fait tuer la generation de la chanson.
if ! swapon --show | grep -q /root/swapfile; then
  [ -f /root/swapfile ] || { fallocate -l 6G /root/swapfile && chmod 600 /root/swapfile && mkswap /root/swapfile >/dev/null; }
  swapon /root/swapfile || echo "swap indisponible : ne rien lancer d'autre pendant la generation d'une chanson"
fi

[ -d ~/acestep ] || git clone -q --depth 1 https://github.com/ace-step/ACE-Step-1.5 ~/acestep
if [ ! -x ~/ace-venv/bin/python ]; then
  python3 -m venv ~/ace-venv
  ~/ace-venv/bin/pip install -q --upgrade pip
  ~/ace-venv/bin/pip install -q torch torchaudio --index-url https://download.pytorch.org/whl/cpu
  ~/ace-venv/bin/pip install -q "transformers>=4.51.0,<4.58.0" diffusers scipy soundfile loguru einops accelerate \
    numba vector-quantize-pytorch "torchao>=0.16.0,<0.17.0" toml modelscope diskcache safetensors peft matplotlib \
    xxhash huggingface_hub faster-whisper pytorch_wavelets PyWavelets
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
# polices des Shorts et des miniatures (Google Fonts). libass ne lit pas la Fredoka « variable » (il retombe sur
# DejaVu) : on en tire une version fixe en gras pour les paroles
mkdir -p ~/fonts
[ -f ~/fonts/LuckiestGuy.ttf ] || curl -sSfL -o ~/fonts/LuckiestGuy.ttf \
  https://raw.githubusercontent.com/google/fonts/main/apache/luckiestguy/LuckiestGuy-Regular.ttf
[ -f ~/fonts/Fredoka.ttf ] || curl -sSfL -o ~/fonts/Fredoka.ttf \
  "https://raw.githubusercontent.com/google/fonts/main/ofl/fredoka/Fredoka%5Bwdth%2Cwght%5D.ttf"
[ -f ~/fonts/Fredoka-Bold.ttf ] || ~/ace-venv/bin/python - <<'PY'
import os
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
f = TTFont(os.path.expanduser("~/fonts/Fredoka.ttf"))
f = instancer.instantiateVariableFont(f, {a.axisTag: 700 if a.axisTag == "wght" else a.defaultValue
                                          for a in f["fvar"].axes})
names = {1: "Fredoka", 16: "Fredoka", 2: "Bold", 17: "Bold", 4: "Fredoka Bold", 6: "Fredoka-Bold"}
for rec in f["name"].names:
    rec.string = names.get(rec.nameID, rec.string)
f["OS/2"].usWeightClass = 700
f["OS/2"].fsSelection = (f["OS/2"].fsSelection & ~0x40) | 0x20
f["head"].macStyle |= 1
f.save(os.path.expanduser("~/fonts/Fredoka-Bold.ttf"))
PY
echo "Installation terminee."
