# Briques audio open source pour « Lulu la Luciole » : voix, chant, musique, lip-sync (état au 2026-10-06)

Notes de recherche et de tests du 2026-10-06, pour la série « Lulu la Luciole » d'Orbeo Studio : français, CPU seul, automatisation sans surveillance.

Conventions :
- Données antérieures à 2025 : **[ancien]**. Sources tierces ou agrégateurs : **[agrégateur]**.
- Résultats mesurés ici, sur cette machine : **[TEST LOCAL]**. Machine : conteneur 4 vCPU, 15 Go de RAM, pas de GPU. Les sorties sont dans `/tmp/claude-0/-home-user-tiktok-auto/c3103019-a176-5027-8bcf-8e27361d44f5/scratchpad/tests_audio/`.
- Limite de méthode : le quota de recherche web de la session a été épuisé à mi-parcours (limite partagée entre agents). La suite s'appuie sur des pages primaires lues directement : fiches Hugging Face, API Hugging Face des modèles et Spaces, README GitHub, pages de politique. Je n'ai pas pu chercher les sorties d'octobre 2026 les plus récentes au-delà de ce qui apparaît dans ces pages.
- Je ne peux pas *écouter* les sons. Le jugement de qualité passe donc par trois mesures : intelligibilité (transcription faster-whisper small + WER), hauteur de voix (F0 médiane, autocorrélation maison) et vitesse. Le timbre, la chaleur et le caractère « mignon » restent à valider à l'oreille.

---

## 1. Quels TTS français ouverts sont bons en 2026 ? Lesquels gèrent l'émotion et les voix enfantines, et lesquels tournent sur CPU ?

### Takeaway
Pour une production commerciale automatisée sur CPU, deux modèles se détachent :
- **Kyutai Pocket TTS** (100M, poids CC-BY-4.0, code MIT). Testé ici : environ 1,7× le temps réel sur 4 vCPU, 1 Go de RAM, français intelligible (WER 0 sur la phrase test pour 6 sorties sur 8).
- **Piper** en secours ultra-rapide (environ 4 à 18× le temps réel). Ses voix françaises sont plates et leurs licences de données varient.

Pour créer des **voix de personnage** (garçon de 4 ans, petite créature, narratrice) avec contrôle émotionnel, le meilleur candidat ouvert à usage commercial est **Qwen3-TTS** (Apache-2.0, janvier 2026, français inclus) :
- le mode **VoiceDesign** crée une voix à partir d'une description en langage naturel ;
- le modèle **Base** clone ensuite cette voix pour la garder identique d'un épisode à l'autre ;
- il lui faut plutôt un GPU, ou un Space ZeroGPU avec un jeton HF (non testable ici, quota anonyme épuisé).

Chatterbox Multilingual (MIT, 23 langues dont le français, curseur d'« exagération » émotionnelle) est l'alternative. Ses sorties portent un filigrane audio Perth.

Fish Audio S2, Voxtral TTS, Breeze TTS 2, F5-TTS et XTTS-v2 sont **non commerciaux** ou bridés.

### Cited Findings

**Modèles 2025-2026 avec français et licence permettant l'usage commercial**
- **Kyutai Pocket TTS** :
  - 100M paramètres, « ~6x real-time on a CPU of MacBook Air M4 », 2 cœurs CPU, environ 200 ms avant le premier son ;
  - langues : anglais, français, allemand, portugais, italien, espagnol (le GitHub ajoute le néerlandais) ;
  - poids **CC-BY-4.0**. Le dépôt avec clonage vocal est **gated** (accepter les conditions et partager son contact). Usages interdits : « voice impersonation or cloning without explicit and lawful consent » ;
  - code d'entraînement publié en août 2026.
  - Sources : [HF kyutai/pocket-tts](https://huggingface.co/kyutai/pocket-tts) ; [GitHub kyutai-labs/pocket-tts](https://github.com/kyutai-labs/pocket-tts) (licence code MIT).
  - Dépôt créé le 2025-12-29, mis à jour le 2026-10-01. Une variante sans clonage, non gated, est créée le 2026-01-06. — [API HF](https://huggingface.co/api/models/kyutai/pocket-tts-without-voice-cloning)
- **Qwen3-TTS (Alibaba)** :
  - cinq modèles : 1.7B-VoiceDesign, 1.7B-CustomVoice, 1.7B-Base, 0.6B-CustomVoice et 0.6B-Base ;
  - 10 langues dont le **français**. VoiceDesign pilote par instructions « timbre, emotion, and prosody » ;
  - 9 voix préréglées (Vivian, Serena, Uncle_Fu, Dylan, Eric, Ryan, Aiden, Ono_Anna, Sohee), mode streaming à 97 ms ;
  - licence **Apache-2.0**, installation `pip install -U qwen-tts`, GPU avec FlashAttention 2 recommandé, sortie annoncée le 22 janvier 2026.
  - Sources : [GitHub QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) ; [blog Qwen](https://qwen.ai/blog?id=qwen3tts-0115). Dépôts HF créés le 2026-01-21 — [API HF](https://huggingface.co/api/models/Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign).
  - Le Space officiel expose trois endpoints : `/generate_voice_design` (texte, langue « French », description de voix), `/generate_voice_clone` (audio et texte de référence, cible, 0.6B/1.7B) et `/generate_custom_voice` (voix préréglée et instruction). — [Space Qwen/Qwen3-TTS](https://huggingface.co/spaces/Qwen/Qwen3-TTS), API lue via gradio_client
- **Chatterbox (Resemble AI)** :
  - Multilingual V3 : 500M paramètres, 23 langues ou plus dont le français ;
  - curseur d'exagération : 0,5 par défaut, « 0.7+ » pour une voix expressive ou dramatique ;
  - **MIT** ; clonage à partir d'un extrait d'environ 10 s ;
  - toutes les sorties portent le filigrane neuronal **Perth** (« imperceptible neural watermarks ») ;
  - Chatterbox-Nano (110M, « 3x realtime on 8 cores » sur CPU) et Turbo (350M, balises [laugh]…) existent en **anglais seulement**.
  - Sources : [GitHub resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox). Dépôt HF mis à jour le 2026-06-10 — [API HF](https://huggingface.co/api/models/ResembleAI/chatterbox).
- **Supertonic 3 (Supertone)** :
  - environ 99M paramètres en ONNX, 31 langues dont le français ;
  - poids sous **OpenRAIL-M** (usage commercial permis avec restrictions d'usage), code MIT ;
  - voix fixes préréglées. Clonage « zero-shot » limité ; les voix sur mesure passent par le « Voice Builder » payant ;
  - sortie le 2026-05-06. Supertonic 2 (5 langues dont le français) date du 2026-01-06.
  - Sources : [HF Supertone/supertonic-3](https://huggingface.co/Supertone/supertonic-3) ; [API HF](https://huggingface.co/api/models/Supertone/supertonic-3)
- **Fun-CosyVoice3-0.5B-2512 (Alibaba FunAudioLLM)** : **Apache-2.0**, langues zh, en, fr, es, ja, ko, it, ru, de. Créé le 2025-12-11. — [API HF](https://huggingface.co/api/models/FunAudioLLM/Fun-CosyVoice3-0.5B-2512)
- **NVIDIA Magpie TTS Multilingual 357M** :
  - licence « nvidia-open-model-license » (commerciale) ; langues dont le français. Créé le 2025-12-11. — [API HF](https://huggingface.co/api/models/nvidia/magpie_tts_multilingual_357m)
  - Classé 3e modèle ouvert du Speech Arena d'Artificial Analysis (Elo 1071) **[agrégateur]**. — [offlinetts.com](https://offlinetts.com/blog/tts-arena-leaderboard-2026/)
- **Kyutai TTS 1.6B en/fr** : CC-BY-4.0, anglais et français. Clonage limité à des « pre-computed voice embeddings », pas de clonage arbitraire. GPU (pas de mention CPU). Septembre 2025. — [HF kyutai/tts-1.6b-en_fr](https://huggingface.co/kyutai/tts-1.6b-en_fr)
- **Kokoro-82M** : Apache-2.0. Une seule voix française, `ff_siwis` [TEST LOCAL]. Mis à jour le 2025-04-10 **[ancien en partie : v1.0 de début 2025]**. — [HF hexgrad/Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M)
- **Piper** :
  - le paquet `piper-tts` 1.8.0 est sous **GPL-3.0-or-later** (métadonnées du paquet installé). La GPL porte sur le logiciel, pas sur l'audio produit ;
  - chaque voix française a la licence de son jeu de données :
    - `fr_FR-siwis` : **CC-BY 4.0** ;
    - `fr_FR-upmc` (Jessica et Pierre) : **CC-BY-SA 4.0** ;
    - `fr_FR-tom` : **AGPLv3**.
  - Source : fiches MODEL_CARD téléchargées sur [HF rhasspy/piper-voices](https://huggingface.co/rhasspy/piper-voices/tree/main/fr/fr_FR)

**Modèles à écarter pour un usage commercial (licence)**
- **Fish Audio S2 Pro** (mars 2026) :
  - 80+ langues, balises d'émotion [whisper] [laugh] ;
  - **Fish Audio Research License** : recherche et usage non commercial gratuits, licence séparée pour le commercial.
  - Sources : [fish.audio/s2](https://fish.audio/s2/) ; [HF fishaudio/s2-pro](https://huggingface.co/fishaudio/s2-pro)
  - Meilleur modèle ouvert du Speech Arena (Elo 1121) avant Breeze TTS 2 **[agrégateur]**. — [offlinetts.com](https://offlinetts.com/blog/tts-arena-leaderboard-2026/)
- **Mistral Voxtral TTS** (4B, 26 mars 2026) :
  - 9 langues dont le français ;
  - **CC BY-NC 4.0**. Les poids ouverts n'ont que 20 voix préréglées ; le clonage passe par l'API payante (0,016 $ pour 1 000 caractères) ;
  - GPU d'au moins 16 Go.
  - Sources : [HF mistralai/Voxtral-4B-TTS-2603](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603) ; [TechCrunch 2026-03-26](https://techcrunch.com/2026/03/26/mistral-releases-a-new-open-source-model-for-speech-generation/) ; [DataNorth](https://datanorth.ai/news/mistral-releases-voxtral-tts-open-weight-text-to-speech-model)
- **Breeze TTS 2** (25 août 2026) : 1er modèle ouvert du Speech Arena (Elo 1215). « BreezeBlue Research and Non-Commercial License », langues en et zh seulement. — [API HF](https://huggingface.co/api/models/BreezeBlue/Breeze-TTS-2) ; [orcarouter.ai](https://www.orcarouter.ai/blog/breeze-tts-2-tops-open-weights-speech-arena) **[agrégateur]**
- **XTTS-v2** : « coqui-public-model-license » (CPML, non commerciale). Coqui ayant fermé, aucune licence commerciale n'est disponible (déduction) **[ancien, 2023]**. — [API HF coqui/XTTS-v2](https://huggingface.co/api/models/coqui/XTTS-v2)
- **F5-TTS** (poids de base) : **cc-by-nc-4.0**. Les fine-tunes français héritent du NC (déduction ; la fiche du fine-tune RASPIAN5 n'était pas accessible sans authentification). — [API HF SWivid/F5-TTS](https://huggingface.co/api/models/SWivid/F5-TTS)
- **IndexTTS-2** : langues en et zh seulement, pas de licence standard dans les métadonnées. — [API HF IndexTeam/IndexTTS-2](https://huggingface.co/api/models/IndexTeam/IndexTTS-2)
- **VibeVoice-1.5B** (MIT) et **VoxCPM1.5** (Apache-2.0) : en et zh seulement, donc pas de français. — [API HF VibeVoice](https://huggingface.co/api/models/microsoft/VibeVoice-1.5B) ; [API HF VoxCPM1.5](https://huggingface.co/api/models/openbmb/VoxCPM1.5)
- **Orpheus français** (`canopylabs/3b-fr-ft-research_release`) : étiquette Apache-2.0 mais dépôt « gated » et nommé « research release ». Créé en avril 2025. — [API HF](https://huggingface.co/api/models/canopylabs/3b-fr-ft-research_release)

**[TEST LOCAL] (a) Phrase « Coucou les amis ! Ce soir, on se brosse les dents avec Nino ! », CPU 4 vCPU, transcription faster-whisper small int8**

| Modèle / voix | Temps de génération (hors chargement) | Durée audio | Facteur temps réel (RTF) | RAM | WER whisper | F0 médiane | Remarques |
|---|---|---|---|---|---|---|---|
| Piper fr_FR-siwis-medium | 0,51 s | 3,70 s | 0,14 | < 0,5 Go | 0 | 208 Hz (femme) | Chargement 1,4 s |
| Piper fr_FR-upmc spk0 (Jessica) | 0,39 s | 3,80 s | 0,10 | < 0,5 Go | 0,08 (« Mino ») | 220 Hz | CC-BY-SA |
| Piper fr_FR-upmc spk1 (Pierre) | 0,20 s | 3,70 s | 0,055 | < 0,5 Go | 0 | 117 Hz (homme) | CC-BY-SA |
| Piper fr_FR-tom-medium | 0,90 s | 3,96 s | 0,23 | < 0,5 Go | 0,08 (« brose ») | 137 Hz (homme) | Données AGPLv3 |
| Kokoro v1.0 int8 ONNX, ff_siwis | 6,5 s | 3,24 s | **2,0** (lent ici) | 0,5 Go | 0 | 209 Hz | Seule voix FR |
| Pocket TTS fr, voix estelle | 1,7 s (phrase courte) ; 5,8 s pour 10,1 s de récit | 2,6 à 3,8 s | **0,57 à 0,64** | 1,07 Go | 0 (1 tirage sur 2 : « minot ») | 242 à 247 Hz | CLI complet 9 à 12 s avec chargement (3,3 s) |
| Pocket TTS fr, azelma / eponine / fantine / marius | CLI 8,9 à 10,9 s | 2,4 à 4,0 s | ≈ 0,6 | 1,07 Go | 0 | 175 à 235 Hz | 27 voix intégrées : cosette, marius, javert, jean, fantine, eponine, azelma, estelle… |
| Pocket TTS fr, cosette | CLI 8,9 s | 3,4 s | ≈ 0,6 | 1,07 Go | **0,25** (« Coucou les amis » sauté) | 205 Hz | Un raté sur ce tirage |
| Pocket TTS french_24l (aperçu, plus gros) | CLI 23,9 s | 3,72 s | ≈ 2 à 3 (estimé) | 2,6 Go | 0 | 267 Hz | Variante « preview » non distillée |
| Référence : voix chantée de Lulu (stem Demucs de la chanson ACE-Step) | — | 7 s | — | — | — | **329 Hz** | Cible de hauteur « petite voix » |

- Récit long (198 caractères), tous modèles : whisper transcrit « luciole » en « lusiole/usiole » pour Pocket TTS, Piper et Kokoro, et « Lulu » en « Lulule/Lulut » pour Pocket estelle et Piper. Comme l'erreur est commune aux trois moteurs, c'est probablement une limite de whisper-small sur un mot rare, pas forcément du TTS. À vérifier à l'oreille. [TEST LOCAL]
- Test « voix d'enfant » par post-traitement ffmpeg de Pocket estelle (F0 242 Hz) [TEST LOCAL] :
  - `asetrate×1,19` + `atempo` (+3 demi-tons, pitch et formants montés, durée conservée) : **F0 289 Hz, WER 0** ;
  - `×1,26` (+4 demi-tons) : F0 304 Hz, WER 0,08 (« minot ») ;
  - `rubberband=pitch=1.26:formant=shifted` : F0 304 Hz, WER 0,17 (« Nino » devient « une eau »).
  - Conclusion : +3 demi-tons restent intelligibles. Le rendu « enfant » contre « chipmunk » est à juger à l'oreille. Fichiers dans `tests_audio/tts_childshift/`.
- Le clonage vocal Pocket TTS à partir d'un extrait de la voix chantée de Lulu a **échoué** sans jeton HF. Message : « If you want access to the model with voice cloning, go to https://huggingface.co/kyutai/pocket-tts and accept the terms ». [TEST LOCAL]
- Tests via Spaces Hugging Face (Qwen3-TTS VoiceDesign avec trois descriptions de voix, garçon de 4 ans, petite fée et narratrice ; Chatterbox Multilingual en français) : **tous refusés**. Messages : « You have exceeded your ZeroGPU quota (90s requested vs. 0s left)… Authenticate with a Hugging Face token » et « exceeded your ZeroGPU runs limit ». Le quota anonyme est partagé par l'IP du proxy et était déjà à zéro. Le Space CPU `Qwen/Qwen3-TTS-Demo` (voix API dont « Bella / 萌宝 ») n'a pas répondu en 400 s. [TEST LOCAL]

### Inferences
- Aucune voix française testée sur CPU n'est une **voix d'enfant**. Les F0 vont de 175 à 267 Hz (voix de femme), alors qu'un enfant de 4 ans parle plutôt vers 250 à 400 Hz et que la voix chantée de Lulu est à 329 Hz. Il faut donc :
  - soit **concevoir** les voix avec Qwen3-TTS VoiceDesign (GPU ou Space avec jeton) puis les figer par clonage (Base 0.6B/1.7B, ou Pocket TTS gated) ;
  - soit post-traiter (pitch et formants vers le haut) une voix féminine claire comme estelle ou fantine, au risque d'un effet « chipmunk ».
- **Stack TTS recommandée** :
  - **Narrateur** : Pocket TTS (estelle, fantine ou azelma), 100 % CPU, environ 1,7× le temps réel, licence CC-BY (attribution Kyutai à mettre dans les crédits).
  - **Voix de Lulu et de Nino** : Qwen3-TTS (VoiceDesign → banque de 30 à 60 s de référence → clonage Base pour chaque réplique). Instructions d'émotion par réplique.
  - **Secours** : Chatterbox Multilingual (MIT, émotion réglable, filigrane Perth sans gêne pour YouTube).
- Garder Piper pour les maquettes et les tests de minutage. Sa voix est trop « GPS » pour des personnages.

### Gaps
- Qualité perçue (chaleur, mignonnerie, naturel) non évaluée à l'oreille. Pas de classement TTS spécifique au français trouvé (arènes surtout en anglais).
- Vitesse réelle de Qwen3-TTS 0.6B et de Chatterbox Multilingual sur ce CPU : non mesurée. Le disque libre était descendu à 2,5 Go, partagé avec l'autre chercheur, et je n'ai pas téléchargé ces modèles d'environ 2 à 4 Go.
- Qwen3-TTS sait-il produire une vraie voix d'enfant de 4 ans crédible en français ? À tester avec un jeton HF (Space ZeroGPU) ou sur Kaggle/Colab.
- Fiche Kokoro VOICES.md (note de qualité de ff_siwis) non relue. Licence exacte de l'Orpheus français et conditions Llama sous-jacentes : non vérifiées.

---

## 2. Clonage et conversion de voix : comment garder une même voix chantée de Lulu d'une chanson à l'autre ?

### Takeaway
La voie la plus robuste et légalement propre comporte deux étages :
1. **Fixer le chanteur dans ACE-Step 1.5** par un **LoRA** entraîné sur 8 à 10 chansons validées de Lulu. ACE-Step annonce un LoRA en un clic, environ 1 h pour 8 chansons sur RTX 3090.
2. **Uniformiser le timbre en post-production** par conversion de voix chantée sur le stem vocal isolé par Demucs, puis remixer :
   - **RVC/Applio** (MIT, environ 10 min de données, inférence CPU possible) ;
   - ou **Seed-VC** (GPL-3.0, modèle chant 44,1 kHz en zero-shot ; dépôt **archivé** depuis novembre 2025).

La voix « source » doit être une voix **synthétique originale** (créée par ACE-Step ou Qwen3-TTS VoiceDesign), jamais celle d'une personne réelle sans consentement.

### Cited Findings
- **Seed-VC** :
  - **GPL-3.0** ; conversion de voix chantée avec un modèle dédié `seed-uvit-whisper-base` (200M, 44,1 kHz) ;
  - zero-shot avec 1 à 30 s de référence. Fine-tuning possible dès « 1 utterance per speaker », « minimum 100 steps, 2 min on T4 » ;
  - GPU fortement recommandé ;
  - **dépôt archivé le 21 novembre 2025** (lecture seule). Comparaisons avec RVC et SoVITS dans EVAL.md.
  - Source : [GitHub Plachtaa/seed-vc](https://github.com/Plachtaa/seed-vc). La date de la V2 donnée par la page lue (« April 2024 ») semble erronée, sans doute 2025 ; à vérifier.
- **RVC (Retrieval-based Voice Conversion WebUI)** :
  - code **MIT**. Modèles de base entraînés sur VCTK (environ 50 h), « no copyright concerns » ;
  - environ 10 min de voix propre recommandées ; entraînement rapide même sur petite carte ;
  - chant pris en charge ; inférence CPU possible sous Linux. « RVCv3 base model coming soon ».
  - Source : [GitHub RVC-Project](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)
- **OpenVoice V2** : MIT, métadonnées HF en et zh, dernière mise à jour en décembre 2024 **[ancien]**. — [API HF myshell-ai/OpenVoiceV2](https://huggingface.co/api/models/myshell-ai/OpenVoiceV2)
- **ACE-Step 1.5** :
  - entraînement LoRA « one-click in UI ; 8 songs in ~1 hour on 3090 » ;
  - fonctions cover, repaint, vocal-to-BGM et séparation de pistes ;
  - **MIT**.
  - Source : [GitHub ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5)
- **Qwen3-TTS** propose un clonage (`/generate_voice_clone` avec audio et texte de référence) et la création de voix par description, sous Apache-2.0. Cela permet de **concevoir** une voix de Lulu puis de la réutiliser telle quelle. Il s'agit de parole, pas de chant. — [Space Qwen/Qwen3-TTS](https://huggingface.co/spaces/Qwen/Qwen3-TTS) ; [GitHub](https://github.com/QwenLM/Qwen3-TTS)
- [TEST LOCAL] Demucs isole bien une voix exploitable comme référence : stem `vocals.mp3`, F0 médiane 329 Hz. Mais le clonage Pocket TTS depuis ce stem a été bloqué par le gating HF (voir §1).

### Inferences
- Pour une chaîne enfant, la **cohérence de timbre** entre chansons compte plus que la fidélité absolue. Ordre recommandé :
  1. Retenir 1 ou 2 prises ACE-Step où la voix de Lulu plaît.
  2. Les séparer (Demucs ou RoFormer) pour constituer environ 10 min de « voix de Lulu » (plusieurs chansons).
  3. Entraîner un modèle RVC/Applio sur un GPU gratuit (Kaggle ou Colab, environ 30 à 60 min).
  4. Convertir systématiquement chaque nouveau stem vocal avant remixage. L'inférence RVC tourne sur CPU dans la boucle automatique.
- Seed-VC donne un résultat zero-shot immédiat. Mais il est archivé (plus de correctifs) et sous GPL-3.0, ce qui est sans effet sur l'audio produit mais contamine un logiciel redistribué. RVC/Applio (MIT, communauté active) est préférable pour un pipeline durable.
- Le même modèle RVC peut convertir les répliques **parlées** de Lulu (sorties TTS) vers son timbre chanté, donc une seule identité vocale pour la parole et le chant. C'est à tester.

### Gaps
- Pas de test local de RVC ou Seed-VC (disque partagé à 2,5 Go libres, dépendances lourdes). Pas de comparatif 2026 trouvé sur la conversion de voix chantée (Vevo2, YingMusic, SoulX…) avant épuisement du quota de recherche.
- Date de la dernière version d'Applio et sa licence : non vérifiées dans cette session.

---

## 3. Génération de chansons en français (ACE-Step 1.5, YuE, DiffRhythm, SongBloom, LeVo/SongGeneration, HeartMuLa…) et séparation de stems

### Takeaway
**ACE-Step 1.5 reste le meilleur choix pour Orbeo**, pour plusieurs raisons :
- c'est le seul générateur de chansons récent qui cumule licence **MIT**, **50+ langues** de paroles, support **CPU**, LoRA, repaint/cover/vocal-to-BGM et durées de 10 s à 10 min ;
- il est déjà installé ;
- sa variante **XL 4B** (2 avril 2026) améliore la qualité, mais demande au moins 12 Go de VRAM.

Concurrents :
- **HeartMuLa** (Apache-2.0, janvier 2026) : prometteur mais pas annoncé en français.
- **YuE2** (fin septembre 2026) : très bon sur benchmark mais **poids CC BY-NC 4.0** et 24 Go de VRAM.
- **DiffRhythm2** : Apache-2.0, français non documenté.
- **SongGeneration v2** : licence « unknown ».

Pour les stems, **Demucs htdemucs tourne bien sur CPU** : 91 s pour la chanson de 112 s, 1,7 Go de RAM [TEST LOCAL]. **BS-RoFormer / Mel-Band RoFormer** (audio-separator, MIT) donnent de meilleures voix isolées (SDR 12,6 à 12,9).

### Cited Findings
- **ACE-Step 1.5** :
  - **MIT** ; « 50+ languages » de paroles (le français n'est pas cité nommément) ;
  - CPU-only et ROCm supportés ;
  - moins de 2 s par chanson sur A100 (XL sft + LM 4B), moins de 10 s sur RTX 3090. 6 à 8 Go de VRAM suffisent pour 2B turbo + LM 0.6B ;
  - LoRA ; cover, repaint, vocal-to-BGM, séparation de pistes et génération multipiste ; extraction BPM et tonalité ; génération LRC (horodatage des paroles) ;
  - durée de 10 s à 600 s ; API REST et Gradio ;
  - XL (DiT 4B) publié le 2 avril 2026.
  - Source : [GitHub ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5)
  - Dépôt HF créé le 2026-01-23, licence mit. L'ACE-Step v1 3.5B (avril 2025) était Apache-2.0 et listait « fr » parmi ses langues. — [API HF ACE-Step1.5](https://huggingface.co/api/models/ACE-Step/Ace-Step1.5) ; [API HF ACE-Step v1](https://huggingface.co/api/models/ACE-Step/ACE-Step-v1-3.5B)
- Contexte fourni par Orbeo (non re-mesuré) : sur ce CPU, environ 1 h pour 3 prises de 2 min avec ACE-Step 1.5. Sur une T4 gratuite, ce serait environ 100 fois plus rapide, par extrapolation des chiffres GPU ci-dessus (déduction).
- **HeartMuLa** :
  - HeartMuLa-oss-3B publié le 14 janvier 2026, versions RL le 23 janvier, « happy-new-year » le 13 février (version recommandée), MuLaCover (covers et remix) le 16 septembre 2026 ;
  - le 7B n'est pas publié ; jusqu'à 4 min, 48 kHz stéréo ;
  - **Apache-2.0**. « Multilingual support covering almost all languages », mais la fiche HF liste zh, en, ja, ko, es, **pas fr** ;
  - les auteurs disent que leur 7B **interne** est « comparable with Suno ».
  - Sources : [GitHub HeartMuLa/heartlib](https://github.com/HeartMuLa/heartlib) ; [API HF HeartMuLa-oss-3B](https://huggingface.co/api/models/HeartMuLa/HeartMuLa-oss-3B)
- **YuE / YuE2** :
  - YuE2 : article arXiv le 29 septembre 2026, instrumentaux et covers ajoutés le 25 septembre 2026. SongBench moyen 6,96 (best-of-8), annoncé compétitif avec « Suno v5/v6 » ;
  - poids **CC BY-NC 4.0** avec une permission additionnelle : les créateurs individuels peuvent « monetize generated outputs, with no fees or royalties ». Les entreprises doivent demander une licence ;
  - GPU BF16 de 24 Go ; langues non précisées dans la page lue.
  - Sources : [GitHub multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE)
  - YuE v1 (janvier 2025) : s1-7B-anneal-en-cot étiqueté Apache-2.0, langue « en ». — [API HF](https://huggingface.co/api/models/m-a-p/YuE-s1-7B-anneal-en-cot)
- **DiffRhythm2** : Apache-2.0, créé le 2025-10-13. — [API HF ASLP-lab/DiffRhythm2](https://huggingface.co/api/models/ASLP-lab/DiffRhythm2)
- **SongGeneration v2** (collection « LeVo », février-mars 2026) : licence « unknown », README vide. Le dépôt GitHub tencent-ailab/SongGeneration renvoie 404 et le dépôt HF tencent/SongGeneration demande une authentification. — [HF lglg666/SongGeneration-v2-large](https://huggingface.co/lglg666/SongGeneration-v2-large)
- **Séparation de stems** :
  - [TEST LOCAL] Demucs 4.1.0 (`htdemucs`, `--two-stems vocals`, CPU, `-j 1`) sur `chanson_brosse_dents.mp3` (112 s) : **91 s** de bout en bout, modèle d'environ 80 Mo téléchargé compris, pic RAM **1,7 Go**. Paquet sous licence **MIT** (métadonnées du paquet).
    - Whisper sur l'extrait de 7 s (paroles « Petite brosse, petite brosse, fais briller mes petites dents ! Lulu brille… ») : WER 0,40 sur le mix contre 0,53 sur le stem vocal.
    - Le stem n'est donc pas plus intelligible pour whisper. Les mots chantés (« dons » pour « dents », « Loulou ») restent difficiles dans les deux cas.
  - **audio-separator (UVR en Python)** : **MIT**, architectures MDX-Net, VR, Demucs, MDXC/RoFormer et Mel-Band RoFormer. Meilleurs modèles voix : `model_bs_roformer_ep_317_sdr_12.9755` (SDR 12,9) et `vocals_mel_band_roformer` (SDR 12,6). CPU supporté (`[cpu]`) et CLI. — [GitHub nomadkaraoke/python-audio-separator](https://github.com/nomadkaraoke/python-audio-separator)
  - ACE-Step 1.5 propose aussi une « track separation » native. — [GitHub ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5)

### Inferences
- Garder ACE-Step 1.5 (MIT), ajouter un **LoRA « voix et style Lulu »** et migrer la génération vers un GPU gratuit (Kaggle ou Colab) pour passer d'environ 20 min à environ 30 s par prise. Cela permet de générer 8 à 10 prises et de choisir automatiquement par score whisper et durée.
- HeartMuLa est à surveiller : Apache-2.0, et le 7B promis comparable à Suno. Il faut d'abord un test en français.
- YuE2 est utilisable par un créateur individuel pour monétiser les sorties, mais pas par une société sans licence (CC BY-NC avec permission créateur). Orbeo étant une entreprise, c'est à éviter sans accord écrit.
- Pour le lip-sync, utiliser le **stem vocal** (RoFormer de préférence à Demucs) comme entrée audio. Les modèles audio-driven (wav2vec ou Whisper) réagissent aux instruments. LongCat-Video-Avatar 1.5 intègre d'ailleurs un mode « Isolate vocals ».

### Gaps
- Pas de test comparatif ACE-Step contre HeartMuLa ou DiffRhythm2 sur des paroles françaises (pas de GPU, quota de recherche épuisé). SongBloom : page inaccessible.
- La qualité de séparation Demucs contre RoFormer n'a pas été mesurée à l'oreille. RoFormer n'a pas été téléchargé (environ 600 Mo, disque juste).

---

## 4. Lip-sync et animation parlante ou chantante pour un personnage cartoon non humain (luciole à petite bouche)

### Takeaway
Deux familles se distinguent :
- **Video-to-video** (re-synchroniser un clip Agnes existant) : LatentSync 1.6, MuseTalk 1.5, Wav2Lip et InfiniteTalk en mode V2V. La plupart s'appuient sur un **détecteur de visage humain** (InsightFace, S3FD, DWPose). C'est un risque majeur pour une luciole à bouche minuscule.
- **Image-to-video audio-driven** (générer un plan chantant à partir d'une image de Lulu) : les modèles **2025-2026 fondés sur des DiT vidéo** comme Wan2.2-S2V, InfiniteTalk/MultiTalk, **LongCat-Video-Avatar 1.5**, HuMo, OmniAvatar et FantasyTalking. Ils ne dépendent pas d'un détecteur de visage.

Le candidat le plus adapté est **LongCat-Video-Avatar 1.5** (Meituan, mai 2026, **MIT**) : parole **et chant**, styles « anime, animals », mode d'isolation des voix, 480p ou 720p. Il demande toutefois de gros GPU (exemples multi-GPU). Les alternatives sont **Wan2.2-S2V-14B** et **InfiniteTalk** (Apache-2.0).

Je n'ai pas pu valider ces modèles sur Lulu. Tous les Spaces ZeroGPU ont été refusés (quota anonyme à zéro) et le Space officiel Wan2.2-S2V affichait 98 personnes devant et environ 3 h 15 d'attente estimée. Un diagnostic local montre en revanche qu'un lip-sync entraîné sur des humains (**Wav2Lip**) **ne suit pas le chant** sur Lulu : corrélation de +0,18 avec l'énergie vocale, bouche jamais fermée, bas du visage flou.

**Wav2Lip** (non commercial) et **Sonic** (CC BY-NC-SA) sont exclus.

Le **plan B CPU, déterministe et commercial** est **Rhubarb Lip Sync** (MIT). Testé : 1,7 s pour 7 s de chant, 38 formes de bouche. Il produit des cues de formes de bouche qui pilotent des sprites ou des shape keys (Blender) d'une Lulu « riggée ».

### Cited Findings

**Video-to-video**
- **LatentSync (ByteDance)** :
  - v1.6 du 11 juin 2025 en 512×512 (v1.5 en 256×256) ; 8 Go de VRAM pour v1.5, 18 Go pour v1.6 ;
  - **détection de visage InsightFace requise** ; marche sur photoréaliste et **anime** (vidéos anime tirées de VASA-1) ; **video-to-video uniquement** ; chant non mentionné.
  - Licence : README GitHub « Apache-2.0 for code and weights » ([GitHub bytedance/LatentSync](https://github.com/bytedance/LatentSync)) **contredit** par l'étiquette HF « openrail++ » sur LatentSync-1.6 ([API HF](https://huggingface.co/api/models/ByteDance/LatentSync-1.6)). À clarifier ; les deux autorisent a priori l'usage commercial, OpenRAIL avec restrictions d'usage.
- **MuseTalk 1.5** (28 mars 2025) :
  - code MIT et modèles utilisables commercialement, mais dépendances sous leurs propres licences (Whisper, ft-mse-vae, DWPose, S3FD…) ;
  - **détection et alignement de visage requis**, conçu pour des visages humains ; zone visage 256×256 ; 30 fps ou plus sur V100.
  - Source : [GitHub TMElyralab/MuseTalk](https://github.com/TMElyralab/MuseTalk)
- **Wav2Lip** : « any form of commercial use is strictly prohibited » (entraîné sur LRS2) ; renvoie vers Sync Labs **[ancien, 2020]**. — [GitHub Rudrabha/Wav2Lip](https://github.com/Rudrabha/Wav2Lip)

**Image ou vidéo vers vidéo, audio-driven (DiT)**
- **InfiniteTalk (MeiGen/Meituan)** :
  - modes image-to-video et **video-to-video**, streaming en longueur illimitée ; I2V bon jusqu'à environ 1 min ; « lip motion, head movement, body pose and facial expressions » ;
  - **Apache-2.0** ; 40 étapes par défaut, LoRA FusionX (8 étapes, dérive couleur au-delà d'une minute) ou Lightx2v (4 étapes) ;
  - mode faible VRAM `--num_persistent_param_in_dit 0` ; ComfyUI ;
  - encodeur audio Chinese-wav2vec2-base ; sortie le 19 août 2025.
  - Sources : [GitHub MeiGen-AI/InfiniteTalk](https://github.com/MeiGen-AI/InfiniteTalk) ; [HF](https://huggingface.co/api/models/MeiGen-AI/InfiniteTalk)
- **LongCat-Video-Avatar 1.5 (Meituan)** :
  - créé le 2026-05-21, **MIT** ;
  - modes audio-texte vers vidéo, audio-texte-image vers vidéo et continuation vidéo ; **chant et parole** ;
  - styles « anime, animals, and complex real-world conditions » ; mono et multi-personnes ; 480p ou 720p ;
  - inférence distillée en 8 étapes, INT8 ; exemples à 2 GPU ou plus (`--nproc_per_node=2`) ;
  - encodeur audio passé de Wav2Vec2 à **Whisper-Large** (« significantly smoother and more natural lip dynamics »).
  - Sources : [HF meituan-longcat/LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5) ; [API HF](https://huggingface.co/api/models/meituan-longcat/LongCat-Video-Avatar-1.5)
  - Le Space communautaire expose `vocal_mode` : « Clean speech (fast) » ou « Isolate vocals (quality) », plus des accélérations DBCache. — [Space victor/LongCat-Video-Avatar-1.5](https://huggingface.co/spaces/victor/LongCat-Video-Avatar-1.5) (API lue via gradio_client)
- **Wan2.2-S2V-14B** : **Apache-2.0**, créé le 2025-08-25. Le Space officiel tourne en « cpu-basic » et prend une image de référence, un audio et une résolution 480P ou 720P. — [API HF](https://huggingface.co/api/models/Wan-AI/Wan2.2-S2V-14B) ; [Space Wan-AI/Wan2.2-S2V](https://huggingface.co/spaces/Wan-AI/Wan2.2-S2V)
- **Autres** (licences lues dans les métadonnées HF) :
  - **HuMo** (ByteDance) : Apache-2.0, septembre 2025 ;
  - **OmniAvatar-14B** : Apache-2.0, juin 2025 ;
  - **FantasyTalking** : Apache-2.0, avril 2025 ;
  - **StableAvatar** : MIT, août 2025 ;
  - **EchoMimicV3** : Apache-2.0, août 2025, mis à jour en janvier 2026 ;
  - **MultiTalk** : Apache-2.0, juin 2025 ;
  - **Hallo3** : MIT, novembre 2024 **[ancien]**.
  - Sources : [HuMo](https://huggingface.co/api/models/bytedance-research/HuMo), [OmniAvatar](https://huggingface.co/api/models/OmniAvatar/OmniAvatar-14B), [FantasyTalking](https://huggingface.co/api/models/acvlab/FantasyTalking), [StableAvatar](https://huggingface.co/api/models/FrancisRing/StableAvatar), [EchoMimicV3](https://huggingface.co/api/models/BadToBest/EchoMimicV3), [MultiTalk](https://huggingface.co/api/models/MeiGen-AI/MeiGen-MultiTalk), [Hallo3](https://huggingface.co/api/models/fudan-generative-ai/hallo3)
- **Sonic (Tencent)** : **CC BY-NC-SA 4.0** (non commercial ; pour le commercial, Tencent Cloud). Démos anime, GPU de 32 Go, janvier 2025. — [GitHub jixiaozhong/Sonic](https://github.com/jixiaozhong/Sonic)
- **LTX-2 (Lightricks)** :
  - « generate synchronized video and audio within a single model », parole et musique, étiquette « audio-to-video » ;
  - 19B paramètres ; « ltx-2-community-license-agreement » ; LTX-2.3 disponible ; article de janvier 2026 (arXiv 2601.03233).
  - Il pourrait remplacer Agnes pour les plans parlés, mais pas pour suivre une chanson existante sans conditionnement audio vérifié.
  - Source : [HF Lightricks/LTX-2](https://huggingface.co/Lightricks/LTX-2)

**Approche cartoon classique (CPU)**
- **Rhubarb Lip Sync 1.14.0** : MIT, dépendances MIT ou BSD. « The resulting lip sync data belongs to you alone ». — LICENSE.md du binaire téléchargé depuis [GitHub DanielSWolf/rhubarb-lip-sync](https://github.com/DanielSWolf/rhubarb-lip-sync)
- [TEST LOCAL] `rhubarb --recognizer phonetic` (indépendant de la langue) sur l'extrait chanté de 7 s (stem Demucs) : **1,7 s CPU**, **38 cues** de bouche (A à H, X).
  - Exemple : `0.00:B 0.46:C 0.53:B 0.88:F 0.95:H 1.09:C 1.16:B 1.23:A 1.65:B …`
  - Fichier : `tests_audio/lipsync/rhubarb/cues_vocals.json`.

**[TEST LOCAL] (b) Spaces lip-sync, avec `lulu_reference.png` (1024², Lulu de face, petite bouche ouverte) et 7 s de chant (8,8 à 15,8 s : « Petite brosse, petite brosse, fais briller mes petites dents… »)**
- État des Spaces (API HF, 2026-10-06) :
  - **RUNNING en ZeroGPU** : `fffiloni/LatentSync` (vidéo + audio), `meituan-longcat/LongCat-Video-Avatar-1.5-Demo`, `victor/LongCat-Video-Avatar-1.5`, `alexnasa/OmniAvatar`, `acvlab/FantasyTalking`, `multimodalart/MoDA-fast-talking-head`, `fffiloni/EchoMimic` ;
  - **RUNNING en CPU** : `Wan-AI/Wan2.2-S2V` (cpu-basic), `fffiloni/Meigen-MultiTalk` (cpu-basic) ;
  - **en panne** : `artificialguybr/EchoMimicV3-Demo` (BUILD_ERROR), `YinmingHuang/StableAvatar` (RUNTIME_ERROR), `Skywork/skyreels-a1-talking-head` (CONFIG_ERROR), `alexnasa/HuMo_local` (PAUSED).
- Tout appel anonyme à un Space ZeroGPU est refusé immédiatement (quota anonyme de l'IP à 0 s).
- **Wan2.2-S2V (Space officiel, cpu-basic donc pas de quota ZeroGPU) : échec par file d'attente.**
  - 1re tentative (extrait mixé) : aucune réponse en 1 700 s, arrêt par timeout.
  - 2e tentative avec suivi d'état (stem vocal) : `IN_QUEUE rank=98 queue=99 eta=11664 s`, soit environ **3 h 15 d'attente estimée**. Le rang n'a pas bougé en 7 min et la tentative a été abandonnée.
  - Journaux : `tests_audio/lipsync/wan22s2v_log.txt` et `wan22s2v_poll_log.txt`.
  - Conclusion pratique : les Spaces gratuits « vitrines » ne sont pas exploitables pour une production automatisée. Il faut son propre GPU (Kaggle ou Colab) ou un Space dupliqué ou privé.
- **Diagnostic détecteurs de visage sur Lulu** (CPU, `face_alignment` 1.4, S3FD et FAN) :
  - **S3FD** (le détecteur de Wav2Lip, également utilisé dans le prétraitement de MuseTalk) **trouve bien la tête** de Lulu : boîte [373, 298, 627, 588], confiance 1,0 ;
  - les **68 points de repère FAN sont faux** : les points « bouche » s'agglutinent autour du nez et des joues, les yeux sont mal placés (image annotée `tests_audio/lipsync/facedetect/s3fd_fan_landmarks.jpg`) ;
  - conclusion : les outils qui recadrent ou alignent la bouche **par landmarks** (alignement affine type LatentSync/InsightFace, MuseTalk) risquent de cibler la mauvaise zone sur Lulu.
  - Le test MediaPipe n'a pas abouti (API `solutions` absente de la version installée).
- **Diagnostic Wav2Lip GAN sur Lulu** (CPU, local, **licence non commerciale : test de faisabilité uniquement**) :
  - entrées : image fixe, stem vocal de 7 s, boîte S3FD fournie en `--box` ; **12,6 s de calcul** pour 6,9 s de vidéo à 25 fps, 1,1 Go de RAM ;
  - planche de 12 images de la zone bouche : `tests_audio/lipsync/wav2lip_diag/wav2lip_mouth_sheet.jpg` ;
  - visuellement, la bouche bouge un peu (ouverture variable), mais **la bouche ne se ferme jamais** sur les P/B/M ; le bas du visage est **flou** (re-synthèse en 96 px agrandie), avec des artefacts sous la lèvre (t = 3,5 s et 5,65 s) et une couture verticale en bord de boîte ;
  - mesure de l'aire de bouche (pixels rouge sombre) image par image : variation de ±20 % (CV 0,20), mais **corrélation de +0,18 seulement avec l'énergie vocale et de −0,24 avec l'ouverture prévue par Rhubarb**. Aire moyenne 996 px quand Rhubarb prévoit une bouche fermée, contre 878 px pour une bouche ouverte ;
  - **la bouche ne suit pas le chant**. La mesure est grossière (masque couleur) mais va dans le même sens que l'examen visuel.

### Inferences
- Pour Lulu, **éviter les méthodes à détecteur de visage humain** (Wav2Lip, MuseTalk, LatentSync). Le test local le confirme en partie. S3FD détecte la tête, mais les landmarks de bouche sont faux. Wav2Lip, avec la boîte forcée, produit une bouche floue qui ne suit pas le chant (corrélation de +0,18 avec l'énergie vocale). LatentSync et MuseTalk n'ont pas été testés (GPU) ; ils reposent sur les mêmes familles de détecteurs ou landmarks et sont entraînés surtout sur des visages humains.
- La voie la plus prometteuse pour les **plans chantés** est un générateur **image vers vidéo audio-driven**, à lancer plan par plan (5 à 15 s) à partir d'un keyframe de Lulu :
  - LongCat-Video-Avatar 1.5 (MIT, chant, animaux) ;
  - à défaut, Wan2.2-S2V ou InfiniteTalk (Apache-2.0).
  - Le **stem vocal** sert d'entrée audio, la musique complète est remixée ensuite.
  - Cela peut aussi régler la dérive de taille de Lulu, puisque l'image de référence est fixée à chaque plan.
- Pour les **clips Agnes existants**, le mode V2V d'InfiniteTalk (sans détecteur de visage, Apache-2.0) est la seule option V2V crédible pour un non-humain. Elle est à tester sur GPU.
- Le **plan B 100 % CPU et commercial** demande un modèle 3D simple de Lulu (Blender) avec 6 à 9 shape keys de bouche, pilotés par les cues Rhubarb. Il convient aux plans fixes de chanson (karaoké, refrains). Sinon, on peut composer des sprites de bouche sur un plan quasi fixe. C'est robuste et déterministe, mais moins « Pixar » qu'un modèle de diffusion.

### Gaps
- Aucune validation visuelle d'un lip-sync chanté **de qualité production** sur Lulu (LongCat, Wan-S2V, InfiniteTalk…). Les Spaces ZeroGPU étaient refusés et la file d'attente Wan était de plus de 3 h. Seul le diagnostic Wav2Lip, négatif, a pu être fait. Il faudrait un jeton HF gratuit (5 min ZeroGPU par jour) ou une session Kaggle avec InfiniteTalk ou LongCat.
- VRAM réelle de LongCat-Video-Avatar 1.5 sur un seul GPU (INT8) : non documentée dans la page lue. On ne sait pas s'il tient sur une T4 de 16 Go (probablement non pour 720p).
- Comportement réel de ces modèles sur une **bouche minuscule** : aucune source trouvée.

---

## 5. Automatisation et calcul : options GPU gratuites ou peu chères (bref, couvert en détail par le chercheur visuel)

### Takeaway
Sur cette machine CPU, la **voix (Pocket TTS, Piper), la séparation (Demucs) et les cues de lip-sync (Rhubarb)** s'automatisent localement sans GPU. **La musique rapide, la conception de voix (Qwen3-TTS) et le lip-sync par diffusion** demandent un GPU.

Côté **HF ZeroGPU**, le quota est par compte :
- 2 min par jour en anonyme (épuisé ici, IP partagée) ;
- **5 min par jour avec un compte gratuit** ;
- 40 min par jour en PRO, puis 1 $ les 10 min.

Un **jeton HF gratuit** est la première action à faire.

### Cited Findings
- ZeroGPU :
  - GPU NVIDIA RTX Pro 6000 Blackwell (moitié = 48 Go, « large ») ;
  - quotas quotidiens : non authentifié 2 min, compte gratuit 5 min, PRO 40 min (« extensible »), Team 40 min, Enterprise 60 min. Réinitialisation 24 h après le premier usage ;
  - PRO : 8× plus de quota, file prioritaire, crédits à **1 $ pour 10 minutes** ;
  - un compte gratuit (e-mail vérifié, plus de 30 jours) peut **héberger 2 Spaces ZeroGPU**, un compte PRO 10 ;
  - durée par appel de 60 s par défaut, ajustable par `@spaces.GPU(duration=…)`.
  - Source : [HF docs ZeroGPU](https://huggingface.co/docs/hub/spaces-zerogpu)
- [TEST LOCAL] Messages d'erreur reçus : « You have exceeded your ZeroGPU quota (90s requested vs. 0s left)… Authenticate with a Hugging Face token for more quota » et « exceeded your ZeroGPU runs limit ».
- [TEST LOCAL] Ressources mesurées :
  - Pocket TTS : 1,1 Go de RAM ;
  - Pocket french_24l : 2,6 Go ;
  - Demucs : 1,7 Go ;
  - Piper et Kokoro : moins de 0,5 Go ;
  - Rhubarb : négligeable.
  - Tout tient sous la limite de 6 Go fixée pour cohabiter avec les tests visuels. Le **disque** (2,5 Go libres en fin de session) est la vraie contrainte.
- L'outil Agnes local n'a pas d'entrée audio pour le lip-sync : `audio_source` vaut « post_stitch » ou « model ». — fichier `~/agnes-video-generator/models/task.py` (lu localement)

### Inferences
Organisation conseillée :
1. **Local CPU** (cron/agents) : TTS narrateur (Pocket), séparation Demucs, cues Rhubarb, mixage ffmpeg et contrôle qualité whisper.
2. **GPU par lots** (Kaggle ou Colab, ou un Space ZeroGPU privé dupliqué sur le compte Orbeo) : ACE-Step (prises et LoRA), Qwen3-TTS (voix de personnages), RVC (entraînement) et LongCat ou Wan S2V (plans chantés).
3. **Payant si besoin** : crédits HF (1 $ les 10 min sur un GPU de 48 Go). Une chanson de 2 min découpée en plans de 10 s représente probablement 12 appels de 1 à 3 min chacun, soit environ 2 à 4 $ par clip chanté (estimation non mesurée).

### Gaps
- Quotas Kaggle et Colab de 2026, crédits Modal, prix RunPod et Vast : non vérifiés ici (quota de recherche épuisé ; c'est le périmètre du chercheur visuel).

---

## 6. Politiques des plateformes sur la musique IA (Spotify, Deezer, DistroKid, YouTube) et dépôt SACEM

### Takeaway
La musique **faite avec l'IA est admise** sur Spotify et DistroKid si l'on détient les droits, sans usurpation vocale ni spam de masse. Spotify ajoute des crédits IA (DDEX) et un filtre anti-spam.

**Deezer étiquette les titres 100 % IA et les exclut des recommandations algorithmiques et éditoriales**. Pour les DSP, il faut donc une contribution humaine documentée.

Sur **YouTube**, la page de divulgation liste explicitement « AI generated music » parmi les exemples. Mais l'obligation vise le contenu **réaliste** : une animation clairement irréaliste n'a pas à être signalée. Par prudence, cocher « contenu modifié ou synthétique » pour les chansons.

**SACEM** : non vérifié (site inaccessible à l'outil de lecture).

### Cited Findings
- **Spotify** (25 septembre 2025) :
  - « Vocal impersonation is only allowed in music on Spotify when the impersonated artist has authorized the usage » ;
  - filtre anti-spam (envois massifs, doublons, SEO, titres artificiellement courts) ;
  - mentions IA via le standard **DDEX** (voix, instrumentation, post-production) affichées dans les crédits ;
  - « all music is treated equally, regardless of the tools used to make it ».
  - Source : [Spotify newsroom](https://newsroom.spotify.com/2025-09-25/spotify-strengthens-ai-protections/)
- **Deezer** (juin 2025) :
  - premier système d'**étiquetage IA** ; la musique 100 % IA est exclue des recommandations algorithmiques et éditoriales ;
  - environ 70 % des streams de titres 100 % IA jugés frauduleux et non rémunérés ;
  - 18 % des uploads quotidiens (plus de 20 000 titres) entièrement IA, pour environ 0,5 % des écoutes.
  - Source : [Deezer newsroom](https://newsroom-deezer.com/2025/06/deezer-launches-worlds-first-ai-tagging-system-for-music-streaming/)
  - Chiffres plus récents relevés par un autre chercheur : 85 % des streams IA démonétisés ([DJ Mag](https://djmag.com/news/85-of-ai-generated-music-streams-have-been-demonetised-deezer)) ; 44 % des uploads ([DJ Mag](https://djmag.com/news/ai-generated-music-accounts-44-of-uploads-deezer-streaming-platform-reveals)).
- **DistroKid** : accepte la musique faite avec l'IA si l'uploader détient les droits, sans usurpation ni spam, avec un workflow de crédits IA **[source tierce]**. — [Jack Righteous, guide 2026](https://jackrighteous.com/fr/blogs/ai-music-distribution-guide/ai-music-distribution-rules-distrokid-spotify-apple-deezer)
- **YouTube** (page « Disclosing use of altered or synthetic content ») :
  - exemples requérant divulgation, cités tels quels : « AI generated music » et « Creates music that's the main focus of the video » ;
  - n'ont pas à être divulgués : les contenus irréalistes (« fully animated videos ») et le clonage de sa propre voix pour des voix off.
  - Source : [YouTube Help 14328491](https://support.google.com/youtube/answer/14328491)
  - Le contexte exact (réaliste ou non) de l'exemple « AI generated music » n'a pas pu être lu mot à mot. Voir aussi la politique « inauthentic content » documentée par l'autre chercheur ([YouTube Help 1311392](https://support.google.com/youtube/answer/1311392)).
- **SACEM** : la page sacem.fr n'a pas pu être chargée (« unable to fetch from www.sacem.fr »). Aucune source vérifiée dans cette session.

### Inferences
Pour sécuriser la monétisation et les dépôts :
1. **Paroles écrites ou retravaillées par l'humain** (Orbeo).
2. **Mélodie choisie ou éditée** (repaint ACE-Step, choix de prise, arrangement, mixage), documentée avec dates et versions.
3. Voix synthétique **originale** (pas d'imitation d'artiste).
4. Crédits IA déclarés au distributeur (DDEX).
5. Rythme de sortie modéré pour éviter les filtres anti-spam.

### Gaps
- **SACEM** : on ne sait pas ici si une œuvre générée par IA peut être déclarée, ni si une œuvre avec apport humain (paroles) l'est pour la seule part humaine. Le droit français exige l'empreinte de la personnalité de l'auteur, ce qui laisse supposer que seules les parties humaines (paroles, éventuellement arrangement) sont protégeables. **Non vérifié** : à confirmer sur sacem.fr ou auprès de la SACEM.
- Politique DistroKid lue seulement via une source tierce. Politique YouTube spécifique à YouTube Kids pour la musique IA : non trouvée.

---

## 7. Quelle stack audio recommander à Orbeo (synthèse) ?

### Takeaway
1. **Voix parlées** :
   - narrateur avec **Pocket TTS** (CPU, CC-BY, crédit Kyutai) ;
   - Lulu et Nino avec **Qwen3-TTS** VoiceDesign puis clonage (Apache-2.0, GPU par lots), voix figées dans une « banque de voix » versionnée ;
   - secours : Chatterbox Multilingual (MIT, filigrane Perth).
2. **Chansons** : **ACE-Step 1.5** (MIT) avec un **LoRA Lulu**, générées sur GPU gratuit, sélection automatique par whisper.
3. **Stems** : **Demucs** (CPU, testé) ou **Mel-Band/BS-RoFormer** (audio-separator, MIT).
4. **Voix chantée constante** : **RVC/Applio** (MIT) entraîné sur environ 10 min de « voix de Lulu », appliqué à chaque stem.
5. **Lip-sync chanté** : **LongCat-Video-Avatar 1.5** (MIT, chant et animaux), ou **Wan2.2-S2V / InfiniteTalk** (Apache-2.0), plan par plan à partir d'un keyframe de Lulu et du stem vocal. Plan B CPU : **Rhubarb (MIT) avec rig Blender**.
6. **À exclure** pour un usage commercial : Wav2Lip, Sonic, XTTS-v2, F5-TTS, Fish S2, Voxtral, Breeze TTS 2 et YuE2 (pour une entreprise sans licence).

### Cited Findings
- Voir les sections 1 à 6 pour les sources de chaque brique. Tableau récapitulatif (qualité → coût → vitesse → automatisabilité → difficulté → licence) :

| Brique | Qualité (indices) | Coût | Vitesse | Automatisable | Difficulté | Licence (outil / sorties) |
|---|---|---|---|---|---|---|
| Pocket TTS fr | WER 0 (6 sorties sur 8), voix de femme 175 à 267 Hz [TEST] | 0 € (CPU) | ≈ 1,7× temps réel sur 4 vCPU [TEST] | Oui (CLI, Python, serveur FastAPI) | Faible | Code MIT, poids CC-BY-4.0, clonage gated ([HF](https://huggingface.co/kyutai/pocket-tts)) |
| Piper fr | WER 0 à 0,08, voix plates [TEST] | 0 € | 4 à 18× temps réel (RTF 0,055 à 0,23) [TEST] | Oui | Très faible | GPL-3.0 (logiciel) ; voix CC-BY, CC-BY-SA ou AGPL selon la voix ([HF](https://huggingface.co/rhasspy/piper-voices/tree/main/fr/fr_FR)) |
| Kokoro fr | WER 0, une seule voix [TEST] | 0 € | 0,5× temps réel en int8 ici [TEST] | Oui | Faible | Apache-2.0 ([HF](https://huggingface.co/hexgrad/Kokoro-82M)) |
| Qwen3-TTS | VoiceDesign, émotion par instruction (non testé) | GPU gratuit ou ZeroGPU | Non mesuré | Oui (pip, API Space) | Moyenne | Apache-2.0 ([GitHub](https://github.com/QwenLM/Qwen3-TTS)) |
| Chatterbox Multilingual | Exagération émotionnelle, clonage (non testé) | GPU ou CPU lent | Non mesuré | Oui | Moyenne | MIT, filigrane Perth ([GitHub](https://github.com/resemble-ai/chatterbox)) |
| ACE-Step 1.5 | Déjà utilisé, 50+ langues | 0 € | Environ 20 min par prise sur CPU (contexte Orbeo) ; < 10 s sur 3090 | Oui (API REST) | Moyenne | MIT ([GitHub](https://github.com/ace-step/ACE-Step-1.5)) |
| Demucs htdemucs | Stem vocal exploitable [TEST] | 0 € | 91 s pour 112 s [TEST] | Oui | Faible | MIT (paquet) |
| RVC/Applio | Référence communautaire pour le chant | GPU pour l'entraînement | Inférence CPU possible | Oui | Moyenne | MIT ([GitHub](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)) |
| Seed-VC | Chant zero-shot 44 kHz | GPU conseillé | — | Oui | Moyenne | GPL-3.0, archivé en novembre 2025 ([GitHub](https://github.com/Plachtaa/seed-vc)) |
| LongCat-Video-Avatar 1.5 | Chant, anime, animaux (annoncé) | GPU lourd (multi-GPU dans les exemples) | 8 étapes distillées | Oui (script, Space) | Élevée | MIT ([HF](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5)) |
| Wan2.2-S2V-14B | Audio → vidéo depuis une image | GPU lourd ; Space officiel en CPU-proxy saturé (file d'environ 3 h) [TEST] | Non mesurée | Oui | Élevée | Apache-2.0 ([HF](https://huggingface.co/api/models/Wan-AI/Wan2.2-S2V-14B)) |
| InfiniteTalk | I2V et V2V, long | GPU (mode faible VRAM) | 4 à 8 étapes avec LoRA | Oui (ComfyUI) | Élevée | Apache-2.0 ([GitHub](https://github.com/MeiGen-AI/InfiniteTalk)) |
| LatentSync 1.6 | V2V 512², détecteur InsightFace | GPU de 18 Go | — | Oui | Moyenne | Apache-2.0 (GitHub) contre openrail++ (HF) |
| Rhubarb | Cues de bouche fiables, pas d'image | 0 € | 1,7 s pour 7 s [TEST] | Oui (CLI JSON) | Faible, mais rig ou sprites requis | MIT, données de sortie à vous |
| Wav2Lip / Sonic | Wav2Lip sur Lulu : bouche floue, désynchronisée (corrélation +0,18) [TEST] | 0 € (CPU) | 12,6 s pour 7 s [TEST] | Oui | Faible | **Non commercial** ([Wav2Lip](https://github.com/Rudrabha/Wav2Lip), [Sonic](https://github.com/jixiaozhong/Sonic)) |

### Inferences
Ordre de mise en œuvre conseillé, pour un rendement maximal et un risque minimal :
1. Créer un compte et un jeton HF gratuits (ZeroGPU 5 min par jour).
2. Prototyper les voix Lulu et Nino avec le Space Qwen3-TTS.
3. Passer le narrateur à Pocket TTS en local.
4. Demucs et Rhubarb déjà opérationnels.
5. Tester LongCat-Avatar et Wan-S2V sur un refrain de 10 s.
6. Entraîner un LoRA ACE-Step et un RVC Lulu sur Kaggle.

### Gaps
- Pas de validation à l'oreille ni à l'œil des briques GPU (Qwen3-TTS, Chatterbox, LongCat, Wan-S2V…). Les recommandations reposent sur les fiches et licences, pas sur un rendu Lulu observé.
