# Briques image et vidéo pour « Lulu la Luciole » : cohérence des personnages, génération vidéo, contrôle, upscaling, automatisation et GPU (état au 2026-10-06)

Notes de recherche et de tests du 2026-10-06 pour Orbeo Studio (une personne et des agents IA, France). Objectif : des épisodes animés de qualité, avec des personnages cohérents (Lulu, Nino), produits de façon aussi automatique que possible, si possible avec des outils libres.

Conventions :
- **[TEST LOCAL]** : mesuré ici, sur cette machine (conteneur 4 vCPU, 15 Go de RAM, pas de GPU). J'ai regardé les images produites (planches de 6 images extraites avec ffmpeg). Toutes les sorties sont dans `/tmp/claude-0/-home-user-tiktok-auto/c3103019-a176-5027-8bcf-8e27361d44f5/scratchpad/tests_visuels/`.
- **[ancien]** : donnée antérieure à 2025. **[non vérifié]** : affirmation que je n'ai pas pu sourcer dans cette session.
- Limite de méthode : le quota WebSearch de la session était déjà épuisé au début de mes recherches (limite partagée entre agents). Tout ce qui suit vient de sources primaires lues directement : fiches de modèles et API du Hub Hugging Face (listes de modèles et de Spaces avec licences et dates), README et fichiers LICENSE GitHub (raw), pages de tarifs des fournisseurs, API publique d'offres Vast.ai. Je n'ai donc **pas** de retours d'utilisateurs Reddit ou forums (r/StableDiffusion, r/comfyui) : le « résultat réel » de chaque brique vient de mes tests ou manque (voir les Gaps).
- Licences : je cite le texte de la licence. Je ne donne pas d'avis juridique. Point crucial pour Orbeo, société française : plusieurs licences « ouvertes » **excluent explicitement l'Union européenne**.

---

## 1. Modèles vidéo ouverts en 2026 : qualité pour un dessin animé 3D ou 2D, cohérence des sujets (référence → vidéo, multi-sujets), VRAM, licence

### Takeaway
En octobre 2026, la famille ouverte la plus sûre juridiquement pour Orbeo reste **Wan 2.x (Apache-2.0)** et ses dérivés de « référence → vidéo » : **VACE**, **Phantom**, **BindWeave** (Apache-2.0) et **MAGREF**. Sur le Hub, Wan-AI n'a publié aucun poids Wan 2.5 ou 2.6 : les nouveautés ouvertes de Wan en 2026 sont **Wan-Animate-2** (août 2026) et **Wan-Dancer** (juillet 2026), tous deux Apache-2.0.

**LTX-2.5** (Lightricks, juillet 2026) est le modèle ouvert le plus complet pour une série :
- multi-plans natif « qui garde l'identité des personnages » ;
- audio natif ;
- IC-LoRA **« Ingredients »**, qui conditionne la vidéo sur une planche de référence (personnages, accessoires, décor) ;
- IC-LoRA **« Layout-to-Render »**, qui transforme une animation de blocage Blender en plan fini.

Sa licence est gratuite pour un usage commercial sous 10 M$ de chiffre d'affaires annuel.

Trois modèles sont **à exclure pour une société française**, parce que leur licence exclut l'UE :
- **HunyuanVideo 1.5** (Tencent) ;
- **MiniMax H3** (qui exclut aussi les États-Unis) ;
- **Qwen-Image 2.1** (licence de recherche non commerciale ; c'est un modèle image, traité au §2).

Tous ces modèles demandent un GPU : 24 Go en pratique, 14 Go au minimum avec déchargement (offload), et environ 70 Go pour MAGREF. Aucun ne tourne raisonnablement sur le CPU de ce conteneur.

### Cited Findings

**Wan (Alibaba), Apache-2.0**
- Liste des modèles Wan-AI sur le Hub, triée par date (requête API du 2026-10-06). Les plus récents sont `Wan2.2-Animate-2-14B` (2026-07/08, Apache-2.0), `Wan-Dancer-14B` (2026-07-10, Apache-2.0), `Wan2.2-Animate-14B` (2025-09), `Wan2.2-S2V-14B` (2025-08), Wan2.2 T2V/I2V-A14B et TI2V-5B (2025-07) et Wan2.1-VACE (2025-05). La liste ne contient **aucun** poids « Wan2.5 » ni « Wan2.6 ». Les dépôts tiers nommés `wan2.6` ou `wan-3-0-video` sont vides (0 téléchargement). — [Hugging Face, organisation Wan-AI](https://huggingface.co/Wan-AI)
- Wan2.2 TI2V-5B : « supports both text-to-video and image-to-video generation at 720P resolution with 24fps and can runs on single consumer-grade GPU such as the 4090 ». « This command can run on a GPU with at least 24GB VRAM (e.g, RTX 4090 GPU) » (avec offload). En 720p, la résolution est `1280*704`. — [HF Wan2.2-TI2V-5B](https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B)
- Wan-Animate-2 (7 août 2026) : « end-to-end character animation framework that directly consumes driving videos … strong identity preservation by eliminating intermediate motion extractors. We further add text-driven viewpoint control ». Une variante « Lite » vise le temps réel. Licence Apache 2.0. — [HF Wan2.2-Animate-2-14B](https://huggingface.co/Wan-AI/Wan2.2-Animate-2-14B)
- Wan-Dancer (13 juillet 2026) : génère de longues vidéos de danse rythmées à partir d'une musique et d'une image de référence. Apache 2.0. Un Space HF existe. — [HF Wan-Dancer-14B](https://huggingface.co/Wan-AI/Wan-Dancer-14B)
- VACE (édition et référence tout-en-un sur Wan2.1) : Wan2.1-VACE-1.3B (~81×480×832) et 14B (~81×720×1280), Apache-2.0. « All models inherit the license of the original model. » — [GitHub ali-vilab/VACE](https://github.com/ali-vilab/VACE)

**Référence → vidéo et multi-sujets (dérivés de Wan)**
- Phantom (ByteDance) : « Subject-Consistent Video Generation via Cross-Modal Alignment ». Phantom-Wan-1.3B en avril 2025, Phantom-Wan-14B le 27 mai 2025, intégré à ComfyUI-WanVideoWrapper. L'équipe a ensuite publié HuMo (10 sept. 2025 : texte + images de référence + audio). — [GitHub Phantom-video/Phantom](https://github.com/Phantom-video/Phantom). Licence Apache-2.0 sur le Hub. — [HF bytedance-research/Phantom](https://huggingface.co/bytedance-research/Phantom)
- MAGREF (ICLR 2026) : « Any-Reference Video Generation ». « The inference consumes around **70 GB** of VRAM, so an 80 GB GPU is recommended ». Nœuds ComfyUI et version FP8 par Kijai. La fiche Hub n'indique aucune licence. — [GitHub MAGREF-Video/MAGREF](https://github.com/MAGREF-Video/MAGREF) ; [HF MAGREF-Video/MAGREF](https://huggingface.co/MAGREF-Video/MAGREF)
- BindWeave (ByteDance, ICLR 2026) : « unified subject-consistent video generation framework for single- and multi-subject prompts, built on an MLLM-DiT ». BindWeave-Wan-14B publié le 4 nov. 2025, version FP8 ComfyUI par Kijai, licence Apache-2.0. — [GitHub bytedance/BindWeave](https://github.com/bytedance/BindWeave) ; [HF ByteDance/BindWeave](https://huggingface.co/ByteDance/BindWeave)
- SkyReels V3 R2V 14B (janvier 2026) : « synthesizes coherent video sequences from 1 to 4 reference images … strong identity fidelity … for characters, objects, and backgrounds ». La fiche décrit un pipeline de données conçu « effectively avoiding the "copy-paste" effect ». Option `--low_vram` pour les GPU de moins de 24 Go (FP8 + offload), sortie 720p. — [HF Skywork/SkyReels-V3-R2V-14B](https://huggingface.co/Skywork/SkyReels-V3-R2V-14B)
- Licence de SkyReels V3 : « The Skywork model supports commercial use. If you plan to use the Skywork model or its derivatives for commercial purposes, you must abide by terms and conditions within Skywork Community License ». Je n'ai pas lu le PDF complet de la licence. — [LICENSE SkyReels-V3-R2V](https://huggingface.co/Skywork/SkyReels-V3-R2V-14B/blob/main/LICENSE)
- Autres modèles 2025-2026 à licence permissive vus sur le Hub (je ne les ai pas testés) :
  - ByteDance Bernini-R (2026-06, image-text-to-video, Apache-2.0) : modes « r2v » (référence → vidéo) et « rv2v » (édition guidée par une référence) — [HF ByteDance/Bernini-R](https://huggingface.co/ByteDance/Bernini-R) ;
  - Video-As-Prompt Wan2.1-14B (2025-10, Apache-2.0) — [HF ByteDance](https://huggingface.co/ByteDance) ;
  - SCAIL-2 (zai-org, 2026-06, MIT) : « end-to-end controlled character animation … supports character replacement and multi-character scenarios », 512p/704p — [HF zai-org/SCAIL-2](https://huggingface.co/zai-org/SCAIL-2).

**LTX-2.5 (Lightricks)**
- LTX-2.5 (poids publiés le 2026-07-23, 22B, versions distillée et complète) : « Native multishot generation — generate connected scenes in a single pass: multiple shots that hold character identity, environment, lighting, voice, and visual style across cuts ». Encodeur de texte Gemma 4 12B, prédicteur de durée, audio natif. Fichiers int8 et NVFP4 pour ComfyUI. Astuce basse VRAM : `--quantization fp8-cast --offload cpu`. La fiche ne chiffre pas la VRAM. — [HF Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)
- Licence LTX-2.x Community : « Under $10M annual revenue: Commercial and production use at no cost … Transfer of fine-tunes may require a paid license ». Au-delà de 10 M$, un accord commercial payant est requis. — [HF Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) ; [LICENSE-2_x](https://github.com/Lightricks/LTX-2/blob/main/LICENSE-2_x)
- IC-LoRA LTX-2.5 « Ingredients » (Reference Sheet Control) : « conditions video generation on a reference sheet — a single composite image inventorying the characters, props, and location of a scene — so that generated videos keep those elements visually consistent ». La planche attendue contient « one clean panel per distinct visual element (each character as a face close-up + body turnaround … one clean location panel), laid out on a black background with no text ». Entraîné en « 768×448, 121 frames, 24 fps », ce qui donne des clips d'environ 5 s. — [HF LTX-2.5-22b-IC-LoRA-Ingredients](https://huggingface.co/Lightricks/LTX-2.5-22b-IC-LoRA-Ingredients)
- IC-LoRA LTX-2.5 « Layout to Render » : « turns a 3D viewport animation into a finished shot. Give it a grey clay viewport, or a blocky playblast of simple shapes, from Blender … It keeps the camera path and the placement of objects from the layout ». Le style vient d'une ou plusieurs images clés : « Take the first frame of the clay animation and give it to any image model to generate the visual you want ». Un workflow ComfyUI est fourni ; 1920×1088 est une taille connue pour bien marcher. — [HF LTX-2.5-22b-IC-LoRA-Layout-To-Render](https://huggingface.co/Lightricks/LTX-2.5-22b-IC-LoRA-Layout-To-Render)
- Lightricks a publié en septembre 2026 d'autres IC-LoRA LTX-2.5 (Restore, Refine-Details, Pixel-Spatial-Upscaler, Clean-Plate, Day-To-Night, Alpha-Gen…). — [HF Lightricks](https://huggingface.co/Lightricks)

**Licences qui excluent l'UE ou interdisent l'usage commercial**
- HunyuanVideo 1.5 (8,3B, 20 nov. 2025) : « runs smoothly on consumer-grade GPUs ». « Minimum GPU Memory: 14 GB (with model offloading enabled) ». Le modèle 480p I2V distillé (5 déc. 2025) génère une vidéo en 75 s sur une RTX 4090. Super-résolution 720p/1080p intégrée. — [HF tencent/HunyuanVideo-1.5](https://huggingface.co/tencent/HunyuanVideo-1.5)
- Licence HunyuanVideo 1.5 : « THIS LICENSE AGREEMENT DOES NOT APPLY IN THE EUROPEAN UNION, UNITED KINGDOM AND SOUTH KOREA ». Elle ajoute : « You must not use, reproduce, modify, distribute, or display the Tencent Hunyuan Works, **Output** or results … outside the Territory ». — [LICENSE HunyuanVideo-1.5](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/master/LICENSE)
- MiniMax H3 (poids publiés le 2026-07-28, environ 3,5 M téléchargements) : vidéo avec audio stéréo, jusqu'au 2K et 15 s. Mode « Omni-reference » : « ≤ 9 images, ≤ 3 clips vidéo, ≤ 3 clips audio ». Transformer dense de 33B ; les exemples utilisent `--num-gpus 4`. — [HF MiniMaxAI/MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)
- Licence MiniMax H3 : « "Excluded Territories" means the European Union, the United Kingdom, the Republic of Korea and the United States of America ». « You may not use … the MiniMax H3 Works or any of their Outputs … outside the Applicable Territory ». Il faut aussi afficher « MiniMax H3 » dans l'interface d'un produit commercial. — [LICENSE MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE)

**Autres modèles vidéo ouverts**
- Kandinsky 6.0 Video (septembre 2026, MIT) : Lite 3B et Pro 29B. « generate 5-second video clips with synchronized 44 kHz audio, including lip-sync » en T2AV et TI2AV, plus un modèle de super-résolution jusqu'au 1080p. Le VAE vidéo indiqué est `AutoencoderKLHunyuanVideo`. — [HF kandinskylab/Kandinsky-6.0-Pro-5s-Diffusers](https://huggingface.co/kandinskylab/Kandinsky-6.0-Pro-5s-Diffusers)
- LongCat-Video (Meituan, 2025-10, MIT). LongCat-Video-Avatar-1.5 (2026-05, MIT) : animation pilotée par l'audio, « accurate lip-synchronization … Robustly generalizes to anime, animals ». Usages listés : « singing … animation, and animal characters ». — [HF meituan-longcat/LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5)
- InfiniteTalk (MeiGen, 2025-08, Apache-2.0) : doublage vidéo sur des images clairsemées, « accurate lip synchronization while simultaneously aligning head movements, body posture, and facial expressions ». — [HF MeiGen-AI/InfiniteTalk](https://huggingface.co/MeiGen-AI/InfiniteTalk)
- Index-AniSora (Bilibili, 2025, Apache-2.0) : variantes de Wan2.1 spécialisées anime ; un GGUF v3.2 existe (2026-03). — [HF IndexTeam/Index-anisora](https://huggingface.co/IndexTeam/Index-anisora)
- Anciens modèles **[ancien]** :
  - CogVideoX-5b (2024-08, licence « other ») et CogVideoX-2b (Apache) — [HF zai-org/CogVideoX-5b](https://huggingface.co/zai-org/CogVideoX-5b) ;
  - Mochi-1-preview (2024-10, Apache-2.0) — [HF genmo/mochi-1-preview](https://huggingface.co/genmo/mochi-1-preview) ;
  - SkyReels-V2 (2025-04, licence Skywork).

**Agnes AI (référence actuelle)**
- **[TEST LOCAL]** `agnes-video-2.5` (non flash) a renvoyé `HTTP 403 insufficient_user_quota … remaining: $0.000000` : ce modèle est payant sur ce compte. `agnes-video-2.5-flash` et `agnes-video-v2.0` ont fonctionné gratuitement. La file 2.5-flash a été saturée (`HTTP 503 video_queue_full`) pendant la plus grande partie de l'après-midi du 2026-10-06. Sur 4 soumissions, 1 seule a abouti (après environ 9 min d'attente). Les 3 autres ont été abandonnées après 900 s, 959 s et 2 458 s sans qu'aucun travail soit créé. Pendant ce temps, `agnes-video-v2.0` répondait en 99 à 206 s.

### Inferences
- Pour Orbeo, la **licence décide avant la qualité**. Les candidats sans risque sont Wan 2.x et ses dérivés Apache (VACE, Phantom, BindWeave, Wan-Animate-2), LTX-2.5 (gratuit sous 10 M$ ; la clause sur le « transfer of fine-tunes » est à lire si Orbeo distribue un jour un LoRA Lulu), Kandinsky 6 et LongCat (MIT). À vérifier pour Kandinsky 6 : le VAE est de type HunyuanVideo. Si les poids de ce VAE sont ceux de Tencent, la clause territoriale de Tencent pourrait s'appliquer ; je n'ai pas vérifié d'où ils viennent.
- Pour un **personnage non humain** comme Lulu, les modèles « avatar » ou « portrait » (InfiniteYou, PuLID, HuMo) sont mal adaptés. Ceux qui acceptent n'importe quel sujet sont mieux placés : Phantom, BindWeave, SkyReels-V3 R2V, LTX-2.5 Ingredients. Ces fiches montrent surtout des humains et des objets ; je n'ai trouvé **aucune démonstration publique** sur une mascotte de type Lulu (voir Gaps).
- Le duo le plus prometteur pour une IP cohérente est **LTX-2.5 Ingredients + Layout-to-Render**, combiné ou non à un blocage Blender. C'est précisément le format « planche personnage + décor » qu'Orbeo peut produire automatiquement (voir §3 : la planche de Lulu générée en 22 s par Agnes est propre). Mais il faut un GPU de 24 Go ou plus, et il faudra un test réel.
- Ne pas attendre de « Wan 2.5/2.6 open source » : rien n'est publié sur le Hub au 2026-10-06.

### Gaps
- Aucun retour d'utilisateurs (Reddit, forums) sur la qualité de ces modèles en cartoon 3D façon Pixar ou en mascotte non humaine : la recherche web n'était plus disponible.
- La VRAM réelle de LTX-2.5 22B (fp8, int8) n'est pas chiffrée sur la fiche. Wan2GP annonce « as little as 6 GB » pour certains modèles sans détail par modèle (voir §6).
- Je n'ai pas lu le PDF complet de la licence Skywork Community, ni vérifié la licence exacte de MAGREF (aucune sur la fiche Hub) ni l'origine du VAE de Kandinsky 6.
- Je n'ai pu tester aucun modèle ouvert en vidéo (quota ZeroGPU, voir §7 ; pas de GPU local).

---

## 2. Modèles image et d'édition pour des planches personnage et des images clés cohérentes (FLUX.1 Kontext dev, Qwen-Image / Qwen-Image-Edit, FLUX.2 klein, OmniGen2, USO, InfiniteYou/PuLID, IP-Adapter, LoRA)

### Takeaway
Pour l'édition multi-images à usage commercial, les meilleurs choix ouverts en 2026 sont :
- **Qwen-Image-Edit-2511** (Apache-2.0, décembre 2025) : « improved character consistency », fusion de plusieurs images, LoRA communautaires intégrés ;
- **FLUX.2 klein 4B** (Apache-2.0, janvier 2026) : édition multi-références, « as little as 13GB VRAM », moins d'une seconde par image.

Les **poids** de FLUX.1 Kontext dev et de FLUX.2 klein 9B / FLUX.2 dev sont non commerciaux. Pour Kontext dev, la licence autorise toutefois l'usage commercial des **images produites**, sous conditions (filtres de contenu, interdiction d'entraîner un modèle concurrent). **Qwen-Image-2.1** (septembre 2026) est le plus capable (jusqu'à 10 références), mais sous licence de **recherche non commerciale** : à éviter.

Un **LoRA Lulu** entraîné sur Qwen-Image-Edit-2511, FLUX.2 klein base 4B ou Wan 2.2 est faisable avec ai-toolkit sur un GPU de 24 Go. Je n'ai trouvé aucune source primaire sur le nombre d'images nécessaire (voir Gaps).

### Cited Findings
- Qwen-Image-Edit-2511 : « mitigate image drift, improved character consistency, integrated LoRA capabilities ». « Qwen-Image-Edit-2511 further enhances consistency in multi-person group photos—enabling high-fidelity fusion of two separate person images into a coherent group shot ». L'exemple diffusers passe `"image": [image1, image2]`. « Qwen-Image is licensed under Apache 2.0 ». Des versions Lightning (accélérées) et GGUF existent (lightx2v, unsloth, décembre 2025). — [HF Qwen/Qwen-Image-Edit-2511](https://huggingface.co/Qwen/Qwen-Image-Edit-2511) ; [HF lightx2v/Qwen-Image-Edit-2511-Lightning](https://huggingface.co/lightx2v/Qwen-Image-Edit-2511-Lightning)
- Qwen-Image-2.1 : modèle unifié de génération et d'édition, « 7B parameters in its visual generation component ». « Support up to **10 reference images** … preserve identity for people and products ». Licence : « Qwen Research License Agreement » : « FOR NON-COMMERCIAL PURPOSES ONLY. You shall not use the Materials for any commercial purpose without obtaining a separate commercial license ». — [HF Qwen/Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1) ; [LICENSE](https://huggingface.co/Qwen/Qwen-Image-2.1/blob/main/LICENSE)
- FLUX.2 klein 4B : « multi-reference editing capabilities », « as little as 13GB VRAM », « end-to-end inference in as low as under a second », Apache 2.0. Le 9B est sous « non-commercial license ». — [HF black-forest-labs/FLUX.2-klein-4B](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B). FLUX.2-dev (2025-11) et FLUX.2-klein-9B affichent une licence « other » sur le Hub. — [HF black-forest-labs](https://huggingface.co/black-forest-labs)
- FLUX.1 Kontext dev : poids sous « FLUX.1 [dev] Non-Commercial License ». Pour les sorties, la licence dit : « You may use Output for any purpose (including for commercial purposes), except as expressly prohibited herein. You may not use the Output to train, fine-tune or distill a model that is competitive with the FLUX.1 [dev] Model ». Elle impose aussi de « implement and maintain content filtering measures ». — [LICENSE FLUX.1-Kontext-dev](https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev/blob/main/LICENSE.md)
- OmniGen2 (2025-06, Apache-2.0), suivi d'OmniGen2-RL (2025-12). — [HF OmniGen2](https://huggingface.co/OmniGen2/OmniGen2)
- USO (ByteDance, 2025-08) : LoRA de style et de sujet, Apache-2.0 sur le dépôt, mais `base_model: black-forest-labs/FLUX.1-dev`. Il faut donc les poids FLUX.1 dev, non commerciaux. — [HF bytedance-research/USO](https://huggingface.co/bytedance-research/USO)
- InfiniteYou (ByteDance, Space FLUX) et PuLID visent l'identité de **visages humains** et reposent sur FLUX.1 dev. Je n'ai pas lu leurs licences en détail. — [HF Space ByteDance/InfiniteYou-FLUX](https://huggingface.co/spaces/ByteDance/InfiniteYou-FLUX)
- Autres modèles image Apache-2.0 récents :
  - Z-Image et Z-Image-Turbo (Tongyi-MAI, 2025-11 et 2026-01) — [HF Tongyi-MAI/Z-Image](https://huggingface.co/Tongyi-MAI/Z-Image) ;
  - LongCat-Image-Edit et Edit-Turbo (Meituan, 2025-12 et 2026-02) — [HF meituan-longcat](https://huggingface.co/meituan-longcat) ;
  - Step1X-Edit v1.2 (2025-11) — [HF stepfun-ai](https://huggingface.co/stepfun-ai).
- HunyuanImage 3.0 (Tencent, 2025-09) : licence « other » sur le Hub. Je ne l'ai pas lue ; la licence Tencent de HunyuanVideo exclut l'UE (§1). — [HF tencent/HunyuanImage-3.0](https://huggingface.co/tencent/HunyuanImage-3.0)
- ai-toolkit (Ostris) : entraînement de LoRA, « Free and open source ». Modèles pris en charge : FLUX.2-dev, FLUX.2-klein-base-4B/9B, Qwen-Image, Qwen-Image-2512, Qwen-Image-Edit-2509/2511, Qwen-Image-2.1, Wan 2.1/2.2 (T2V, I2V, TI2V-5B), LTX-2/2.3/2.5. Exemples de configuration pour 24 Go, modèles RunPod et Modal fournis. — [GitHub ostris/ai-toolkit](https://github.com/ostris/ai-toolkit)
- Des Spaces publics montrent l'usage « personnage » de Qwen-Image-Edit : `linoyts/Qwen-Image-Edit-2511-AnyPose`, `multimodalart/qwen-image-multiple-angles-3d-camera` (2026-08), `linoyts/Qwen-Image-Edit-next-scene`. — [HF API Spaces](https://huggingface.co/spaces/multimodalart/qwen-image-multiple-angles-3d-camera)

### Inferences
- Pour produire automatiquement les **images clés** d'un épisode, une solution ouverte et commerciale serait la suivante. Qwen-Image-Edit-2511 (ou FLUX.2 klein 4B) reçoit **deux entrées** : (1) l'image du plan précédent ou du décor, (2) **une seule** image d'identité de Lulu, une pose, sur fond neutre. C'est exactement la configuration qui a le mieux marché avec Agnes (§3). Ce choix est une inférence tirée de mes tests Agnes, pas un test Qwen (quota ZeroGPU épuisé, §7).
- **LoRA Lulu** : il ne faut pas l'entraîner sur des images contenant déjà des défauts (antennes fines, Lulu « fée », Nino avec un nœud). Il faut constituer un jeu propre : planche, poses validées par le juge, puis recadrées. D'après le §7, le coût d'entraînement sur un GPU loué est de l'ordre de quelques dollars. Je n'ai pas de source sur la durée exacte d'un entraînement.
- **IP-Adapter** et **PuLID/InfiniteYou** sont dépassés pour ce besoin : ils visent les visages humains et dépendent de bases SD/FLUX.1 dev, souvent non commerciales. Je ne les recommande pas.

### Gaps
- Nombre d'images et de pas recommandé pour un LoRA de personnage sur Qwen-Image-Edit-2511, FLUX.2 klein ou Wan 2.2, et durée ou coût d'un entraînement : aucune source primaire trouvée dans cette session.
- Je n'ai pas pu tester Qwen-Image-Edit-2511 (Space bloqué par le quota, §7).
- Licences exactes de PuLID et InfiniteYou : non lues.

---

## 3. [TEST LOCAL] Agnes : plusieurs images de référence (planche de Lulu + scène) gardent-elles Lulu plus cohérente que notre approche à référence unique ?

### Takeaway
**Non, pas telles quelles. La qualité des références compte plus que leur nombre.** Avec agnes-image-2.5-flash (16 images testées), le meilleur résultat vient de **deux références** : (1) l'image de scène (Nino + style + décor), (2) **l'image d'identité de Lulu, une seule pose**. Résultat : 2 images propres sur 2, avec un Lulu plus fidèle qu'avec la scène seule.

Deux configurations ont fait apparaître **deux Lulu** :
- une **planche multi-poses** (turnaround) en référence : 4 images sur 4 ;
- des références « personnage isolé » sans image de scène en premier : 2 sur 2.

Avec 4 références, le modèle a en plus **copié la pose** de la référence de Nino au lieu de suivre le texte.

En vidéo :
- `agnes-video-v2.0` en image → vidéo depuis l'image de référence actuelle reproduit les défauts connus : Lulu grossit d'environ 2 à 3 fois, la caméra avance malgré « static camera », des ailes poussent sur le dos de Nino.
- Le mode **keyframes (début + fin)** de v2.0, même avec deux images clés propres, a **dédoublé Lulu** (4 images échantillonnées sur 6).
- `agnes-video-2.5-flash` en mode « reference » suit beaucoup mieux l'action et la caméra fixe, sans doublon ni hybride. Mais il **recompose la scène** au lieu de partir de l'image : on ne peut pas enchaîner les plans par la dernière image.

### Cited Findings
Toutes les données de cette section sont **[TEST LOCAL]** du 2026-10-06. Les appels passent par le client Python `~/agnes-video-generator/core/api` (le serveur local :8765 n'était pas lancé), avec la clé lue depuis `~/.agnes_key` sans l'afficher. Scripts : `scratchpad/agnes_ref_test.py`, `agnes_round3.py`, `agnes_sandwich.py`, `agnes_flash_retry.py`. Sorties : `tests_visuels/agnes/out/`, planches : `tests_visuels/agnes/*.jpg`.

**Références utilisées** (copiées dans le scratchpad) :
- `lulu_reference.png`, Lulu seule, une pose ;
- `02_peur_du_noir/reference.png`, chambre, Nino et Lulu ;
- `03_brosse_dents/keyframes/reference_noeud.png`, salle de bain ;
- un recadrage de Nino tiré de la référence 02.

Constat en passant : sur la référence de l'épisode 03, **Nino porte un nœud rose** (celui de Lulu). Cette contamination se retrouve ensuite dans toutes les vidéos tirées de cette image.

**A. Planche personnage (turnaround)** : `agnes-image-2.5-flash`, entrée `lulu_reference.png`, 1344×768, **22 s**. On obtient 5 poses propres (face, 3/4, profil, dos, en vol), un design fidèle et une taille constante. Défaut mineur : la vue 3/4 et le profil sont presque identiques. Fichier `out/lulu_sheet.png`.

**B. Images clés, nouveau plan ou changement de pièce** (`agnes-image-2.5-flash`, 1344×768, 14 à 35 s par image ; « n » = nombre d'images générées) :

| Configuration (ordre des références) | n | Lulu en double | Autres défauts | Texte suivi |
|---|---|---|---|---|
| Scène seule (approche actuelle), chambre | 2 | 0/2 | aucun vu | 2/2 |
| 4 réf. : Lulu, planche, Nino recadré, scène ; chambre | 2 | **1/2** (Lulu « peluche » dans un 2e lit) | 2/2 Nino **assis comme sur sa référence** ; 2 lits | 0/2 |
| Scène seule, salle de bain (changement de pièce) | 2 | 0/2 | 1/2 **second Nino** vu de dos dans la fenêtre | 2/2 |
| Scène + planche de Lulu | 2 | **2/2** | — | partiel |
| Planche + Nino recadré | 2 | **2/2** | — | partiel |
| **Scène + `lulu_reference.png` (une pose)** | 2 | **0/2** | aucun vu ; Lulu la plus fidèle (antennes à pompons, nœud, ventre) | 2/2 |
| `lulu_reference.png` + Nino recadré (sans scène) | 2 | **2/2** | — | partiel |
| Édition « Lulu se pose sur l'épaule », réf. : image clé précédente + Lulu | 1 | 0/1 | même cadrage, même pièce, même taille | 1/1 |

Planches : `tests_visuels/agnes/room_compare.jpg`, `bath_compare.jpg`, `bath_round3.jpg`, `sandwich_start_end.jpg`.

**C. Clips vidéo, 5 s, prompt « Lulu vole jusqu'à l'épaule de Nino, caméra fixe »**

| Test | Modèle et mode | Durée | Résultat observé (6 images échantillonnées) |
|---|---|---|---|
| V0 | v2.0, image → vidéo depuis `reference_noeud.png` (comme aujourd'hui) | 162 s | Lulu **grossit d'environ 2 à 3 fois** ; la caméra **avance** ; **ailes sur le dos de Nino** sur 5 images sur 6 ; nœud rose sur Nino (hérité) |
| V1 | v2.0, image → vidéo depuis l'image clé propre (scène + Lulu) | 99 s | pas de doublon ni d'ailes sur Nino ; caméra qui **avance fortement** ; **yeux de Nino devenus bleus** ; action non terminée |
| V2 | v2.0, keyframes : début propre + fin propre (Lulu sur l'épaule) | 206 s | **second Lulu** sur 4 images sur 6 ; une aile de Lulu « collée » à Nino sur 1/6 ; léger zoom |
| V3 | 2.5-flash, « reference », 1 image (`reference_noeud.png`) | 563 s (dont environ 7 min de file) | **action réussie** (Lulu se pose sur l'épaule) ; **caméra fixe** ; pas de doublon ni d'hybride ; Lulu cohérente (taille variant avec la profondeur) ; **mais la pièce est recomposée** (plan plus large, baignoire) au lieu de partir de l'image ; nœud rose encore sur Nino ; 1280×720 |
| V4 | 2.5 (non flash), « reference », 3 images | — | **HTTP 403 `insufficient_user_quota`** : modèle payant |
| V5 | 2.5-flash, « reference », 3 images (scène + Lulu + Nino) | — | **jamais exécuté** : `HTTP 503 video_queue_full` pendant 2 458 s (41 min, de 18:19 à 19:00 UTC), « no job was created ». Un premier essai (4 images) avait déjà échoué après 959 s |

Planches : `tests_visuels/agnes/vid_kf_v20_tile.jpg` (V0), `vid_i2v_cleanstart_v20_tile.jpg` (V1), `vid_sandwich_v20_tile.jpg` (V2), `vid_single_flash_tile.jpg` (V3).

- D'après le code du client, avec 2 images ou plus, les modèles 2.5 basculent en mode « reference » (5 images au plus), car le mode keyframe 2.5 « 固定输出 704x704 正方形 » (sortie carrée fixe 704×704). — `~/agnes-video-generator/core/api/agnes_video.py`, `_submit_video_v25`

### Inferences
- **Règle pratique pour Agnes image** :
  - Toujours mettre **en premier** l'image du plan précédent ou du décor (qui contient déjà Nino et le style).
  - Ajouter **une seule** image d'identité par personnage, **une pose, fond neutre**.
  - Ne **jamais** donner une planche multi-poses : le modèle la lit comme plusieurs personnages.
  - Ne pas donner de recadrage en pose précise : le modèle copie la pose.
  - Cette règle vient de petits échantillons (n=2 par case), mais les écarts sont nets (0/2 contre 2/2).
- **Nettoyer l'image de référence de l'épisode 03** (nœud rose sur Nino) : toute vidéo qui en part hérite du défaut.
- Le **mode keyframes de v2.0 crée des doublons** dès que la position de Lulu diffère beaucoup entre le début et la fin. Le modèle fait apparaître une seconde Lulu au lieu de déplacer la première ; c'est sans doute la même cause que les « deux Nino » lors des changements de pièce. Il vaut mieux des plans courts dont le **début et la fin sont presque identiques** (petit déplacement), ou passer en image → vidéo depuis un départ propre.
- Pour la **dérive caméra** (V0, V1), aucun réglage de prompt n'a suffi avec v2.0. Le 2.5-flash a respecté « caméra fixe ». Un pipeline hybride serait :
  - 2.5-flash « reference » pour les plans d'action isolés, coupés franchement (`"cut": true`), ce qui supprime le besoin de continuité à la dernière image ;
  - v2.0 image → vidéo seulement pour les plans très calmes.
  - Coûts à prendre en compte : la file 2.5-flash est peu fiable (1 soumission sur 4 a abouti, jusqu'à 41 min de file pleine), et 2.5 non flash est payant. Le pipeline doit donc pouvoir retomber sur v2.0 ou sur un autre fournisseur.
- La planche de Lulu (A) reste utile comme **entrée pour LTX-2.5 Ingredients** (qui attend exactement ce format) et pour constituer le **jeu d'entraînement d'un LoRA**. Elle ne doit pas servir de référence directe dans Agnes image.

### Gaps
- Échantillons très petits (1 à 2 essais par condition) et une seule graine en vidéo : les taux sont indicatifs.
- **La question posée (2.5-flash, plusieurs références contre une seule) reste sans réponse en vidéo** : le test multi-références V5 n'a jamais été exécuté (file pleine 41 min). En image, la réponse est nette (§3 B).
- Je n'ai pas testé 2.5-flash avec un départ propre (image clé scène + Lulu) comme référence unique, ni l'effet du mot « static » contre « locked-off tripod shot » sur v2.0.
- Le juge visuel automatique n'a pas été appliqué : le jugement est le mien, image par image, sur les planches.

---

## 4. Routes alternatives qui garantissent la cohérence : personnage 3D riggé dans Blender rendu automatiquement, marionnette 2D, ou hybride (décors IA + personnages riggés). Est-ce plus réaliste pour une IP cohérente ? Coût et difficulté pour un studio d'une personne

### Takeaway
La route 3D riggée est la **seule qui garantit** une Lulu identique à 100 %. Elle est **techniquement automatisable sur ce conteneur** : le wheel `bpy` 5.0.1 s'installe avec pip et fait un rendu sans écran. Mais le rendu CPU est trop lent pour des épisodes : environ 48 s par image en Cycles 720p, et environ 60 à 75 s en EEVEE logiciel, soit environ 38 h pour 2 min à 24 i/s. Il faut donc un GPU loué pour le rendu.

Le vrai coût est **humain** : modéliser, riguer et texturer une Lulu « Pixar » à fourrure, puis animer. Ce sont des compétences d'artiste 3D (ou une commande à un freelance), pas de l'automatisation.

Pour une personne seule, **l'hybride le plus réaliste en 2026** est :
- un blocage 3D grossier dans Blender (formes simples, caméra et positions scriptées en Python) ;
- puis **LTX-2.5 Layout-to-Render** (ou Wan VACE avec contrôle de profondeur ou de pose) pour l'habillage, avec une image clé de style par plan.

On obtient ainsi caméra, positions, tailles et nombre de personnages **déterministes**, avec le rendu d'un modèle IA. Je ne l'ai pas encore testé faute de GPU. En 2D, **Inochi2D** (BSD-2) est une alternative ouverte à Live2D, mais elle exige des illustrations en calques et un rig : l'effort est du même ordre.

### Cited Findings
- **[TEST LOCAL] Blender sans écran** :
  - `pip install bpy` s'est installé en 35 s (`bpy-5.0.1`), et `import bpy` fonctionne sous Python 3.11.
  - Script `scratchpad/blender_test.py` : une Lulu de substitution (sphères, ventre émissif, antennes à pompons, nœud, ailes pivotantes) et une chambre simple, construites et **animées entièrement en Python** (trajectoire, balancement, battement d'ailes par images clés).
  - **Cycles CPU**, 1280×720, 32 échantillons + débruitage, 3 threads : 3 images en 144,4 s, soit **48,1 s par image** (préparation de la scène incluse).
  - **EEVEE** : il a d'abord échoué (`Couldn't open libEGL.so.1`). Après `apt-get install libegl1 libegl-mesa0 libgl1-mesa-dri libgles2`, il fonctionne en rendu logiciel, avec des messages `EGL_BAD_MATCH`, à **environ 60 à 75 s par image** (9 images en 10 min).
  - Images : `tests_visuels/blender_headless/cycles_000*.png`, `eevee_000*.png`. Le personnage est volontairement rudimentaire (formes primitives, sans fourrure) : le test mesure la faisabilité et le temps, pas la qualité.
- LTX-2.5 Layout-to-Render accepte « a blocky animation of simple shapes, from Blender » et « keeps the camera path and the placement of objects from the layout ». L'apparence est fixée par une ou plusieurs images clés générées par un modèle image à partir de la première image du blocage. Clips à 24 i/s, nombre d'images 8k+1 (72 images → 65). — [HF LTX-2.5-22b-IC-LoRA-Layout-To-Render](https://huggingface.co/Lightricks/LTX-2.5-22b-IC-LoRA-Layout-To-Render)
- Wan2GP v17.10 (6 octobre 2026) a intégré « LTX-2.5 Layout to Render: turn a rough viewport animation or playblast into a finished shot. Feed it the layout video plus one appearance reference image ». — [GitHub deepbeepmeep/Wan2GP](https://github.com/deepbeepmeep/Wan2GP)
- Wan-Animate-2 et SCAIL-2 animent un personnage de référence à partir d'une **vidéo de pilotage** ; SCAIL-2 accepte aussi des « animal-driving scenarios » et des rendus de maillage SAM3D-Body. Une animation Blender grossière peut donc servir de source de mouvement. — [HF Wan2.2-Animate-2-14B](https://huggingface.co/Wan-AI/Wan2.2-Animate-2-14B) ; [HF zai-org/SCAIL-2](https://huggingface.co/zai-org/SCAIL-2)
- Inochi2D : « a library for realtime 2D puppet animation and the reference implementation of the Inochi2D Puppet standard … deforming 2D meshes created from layered art at runtime based on parameters ». Inochi Creator est l'outil de rig, « in development ». Licence BSD 2-Clause. — [GitHub Inochi2D/inochi2d](https://github.com/Inochi2D/inochi2d) ; [LICENSE inochi-creator](https://github.com/Inochi2D/inochi-creator/blob/main/LICENSE)

### Inferences
- **Coût et difficulté pour Orbeo** (estimations, non sourcées) :
  - **Blender 100 % 3D** : il faut un modèle Lulu de qualité (commande freelance ou modélisation longue), un rig, un shader de fourrure, des décors et une bibliothèque d'animations réutilisables (vol, atterrissage, sourire). Le rendu GPU d'un épisode de 2 min pourrait coûter quelques dollars sur un GPU loué à 0,2-0,6 $/h (§7), mais la mise en place se compte en semaines. Lip-sync possible par blendshapes pilotés par l'audio (voir les notes audio). **Avantage décisif** : zéro dérive, zéro doublon, zéro hybride, caméra exacte. C'est la seule voie qui supprime par construction les quatre défauts observés. C'est aussi la plus « monstre technique ».
  - **Hybride blocage Blender + LTX-2.5 Layout-to-Render** : le blocage peut être généré **automatiquement** par script à partir du découpage de l'épisode (positions, tailles, caméra), sans artiste. L'IA garde le rendu « Pixar ». La cohérence de design de Lulu reste confiée au modèle et à l'image clé ; un LoRA Lulu sur LTX-2.5 la renforcerait. C'est le meilleur compromis qualité / automatisation / effort, **à valider sur GPU**.
  - **2D Inochi2D** : il faut redessiner Lulu en 2D par calques et la riguer. Cela casse le look 3D actuel de la marque : peu pertinent ici.
- Sur ce conteneur, Blender peut servir **sans GPU** à produire les blocages (rendu Workbench ou EEVEE basse résolution, de quelques secondes à quelques dizaines de secondes par image en 512p). Je n'ai pas mesuré le Workbench.

### Gaps
- Coût réel d'une commande de modèle 3D riggé (Lulu à fourrure) auprès d'un freelance : pas cherché (recherche web épuisée).
- Vitesse de rendu EEVEE et Cycles sur GPU (RTX 4090, L4) : je ne l'ai pas mesurée.
- Je n'ai pas testé Layout-to-Render (GPU 22B nécessaire).

---

## 5. Upscaling et interpolation : Real-ESRGAN, SeedVR2, RIFE, GIMM-VFI, FILM (qualité, vitesse CPU contre GPU, licence)

### Takeaway
Sur CPU, l'upscaling IA est trop lent pour des épisodes complets :
- Real-ESRGAN animevideov3 : environ 9,7 s par image ;
- RealESRGAN x2plus : environ 40 s par image ;
- 2 min d'épisode prendraient donc de 8 à 32 h.

Un simple **Lanczos ffmpeg** de 720p vers 1080p est quasi temps réel et visuellement correct pour ce style. **RIFE v4.26** (MIT, via `ccvfi`) tourne sur CPU à environ 2,2 s par image intermédiaire en 1280×704 : utilisable pour lisser un plan, pas tout un épisode. Il n'est utile que pour passer d'un modèle à 16 i/s à 24 i/s.

**Licences** :
- **GIMM-VFI est non commercial** (S-Lab License) : à exclure.
- **FILM** (Apache-2.0), **RIFE** (MIT), **Real-ESRGAN** (BSD-3), **SeedVR2** (Apache-2.0) conviennent.

SeedVR2 est le meilleur restaurateur diffusion en une passe, mais sa fiche avertit qu'il **sur-accentue les vidéos IA 720p** légèrement dégradées.

### Cited Findings
- **[TEST LOCAL]** Extrait de 48 images (2 s, 1280×704, 24 i/s) de `03_brosse_dents/clips/s9_try1.mp4`, PyTorch CPU 2.x, 3 threads (`scratchpad/vfi_test.py`) :

| Outil | Opération | Vitesse | RAM max | Remarque visuelle |
|---|---|---|---|---|
| RIFE v4.26 heavy (ccvfi, MIT) | ×2 (24 → 48 i/s) | **2,15 s par image interpolée** (47 en 101 s) | 1,98 Go | image intermédiaire propre sur ce passage peu mobile |
| ffmpeg `minterpolate` (mci, aobmc, bidir) | ×2 | 87 s pour 48 images ajoutées (environ 1,8 s par image) | faible | correct sur ce passage peu mobile ; non testé en mouvement rapide |
| Real-ESRGAN `realesr-animevideov3` (via spandrel) | ×4 puis réduction à 1920×1056 | **9,7 s par image** (12 en 116 s) | 1,2 Go | traits plus nets, mais **fourrure lissée** (effet « peint ») |
| `RealESRGAN_x2plus` (tuiles de 352) | ×2 puis réduction | **40 s par image** | 1,1 Go | plus net, fourrure préservée |
| ffmpeg Lanczos | 1280×704 → 1920×1080, clip entier de 17 s | **17,7 s pour 17 s de vidéo** (environ temps réel) | faible | un peu plus doux que les modèles, sans artefacts |

- Fichiers : `tests_visuels/cpu_upscale_interp/upscale_crop_compare.jpg` (de gauche à droite : Lanczos, animevideov3, x2plus), `rife_mid_compare.jpg`, `minterp_mid_compare.jpg`, `rife_48fps.mp4`, `minterpolate_48fps.mp4`.
- ccvfi : « an inference lib for video frame interpolation with VapourSynth support », licence MIT. Poids `RIFE_IFNet_v426_heavy.pkl` et `DRBA_IFNet.pkl` téléchargés depuis les releases GitHub. — [PyPI/GitHub EutropicAI/ccvfi](https://github.com/EutropicAI/ccvfi)
- Licences :
  - RIFE (Practical-RIFE) : MIT — [LICENSE](https://github.com/hzwer/Practical-RIFE/blob/main/LICENSE) ;
  - Real-ESRGAN : BSD 3-Clause — [LICENSE](https://github.com/xinntao/Real-ESRGAN/blob/master/LICENSE) ;
  - FILM (Google) : Apache 2.0 — [LICENSE](https://github.com/google-research/frame-interpolation/blob/main/LICENSE) ;
  - GIMM-VFI : « S-Lab License 1.0 … Redistribution and use for non-commercial purpose » — [LICENSE](https://github.com/GSeanCDAT/GIMM-VFI/blob/main/LICENSE) ; publié en 2024 **[ancien]**.
- SeedVR2 (3B et 7B, juin 2025, Apache 2.0) : « one-step diffusion-based VR model ». Limite citée : « Our methods tend to overly generate details on inputs with very light degradations, e.g., **720p AIGC videos**, leading to oversharpened results occasionally ». Les nœuds ComfyUI (numz/AInVFX) sont très téléchargés (plus de 500 k). — [HF ByteDance-Seed/SeedVR2-3B](https://huggingface.co/ByteDance-Seed/SeedVR2-3B) ; [HF numz/SeedVR2_comfyUI](https://huggingface.co/numz/SeedVR2_comfyUI)
- Alternatives d'upscale intégrées aux modèles vidéo :
  - IC-LoRA LTX-2.5 « Pixel-Spatial-Upscaler », « Refine-Details », « Restore » (2026-08/09) — [HF Lightricks](https://huggingface.co/Lightricks) ;
  - Kandinsky-6.0-VSR (MIT, 2026-09) — [HF kandinskylab](https://huggingface.co/kandinskylab) ;
  - super-résolution 1080p de HunyuanVideo 1.5, exclue dans l'UE.

### Inferences
- **Recommandation** :
  - Garder **Lanczos ffmpeg** (gratuit, instantané) pour passer d'Agnes 720p au 1080p.
  - Si un upscale IA devient nécessaire, le faire **sur GPU** et choisir un modèle qui préserve la fourrure : x2plus, ou un upscaler vidéo cohérent dans le temps (IC-LoRA LTX-2.5, Kandinsky VSR).
  - Éviter animevideov3 sur Lulu : il lisse la fourrure, sa signature visuelle.
- **Interpolation** : inutile si les clips sortent déjà à 24 i/s (Agnes 2.0 et 2.5-flash : 24 i/s mesurés). Pour un modèle à 16 i/s, RIFE (MIT) sur GPU, ou sur CPU pour un plan isolé.
- Coût GPU indicatif : sur une RTX 3090 louée 0,16-0,21 $/h (§7), l'upscale et l'interpolation d'un épisode coûteraient des centimes. Inférence : je n'ai pas mesuré la vitesse GPU.

### Gaps
- Pas de test en mouvement rapide (là où les artefacts d'interpolation apparaissent).
- Vitesse GPU de SeedVR2, RIFE et Real-ESRGAN : non mesurée ici.

---

## 6. Automatisation complète du pipeline (API ComfyUI, workflows)

### Takeaway
**ComfyUI** reste le standard pour enchaîner les modèles ouverts. On exporte un workflow au format API, on le soumet par `POST /prompt`, on suit l'exécution par WebSocket `/ws` ou `GET /history/{prompt_id}`, et on récupère les sorties par `/view`. Les modèles clés ont des nœuds ou des workflows prêts : Wan, VACE, Phantom, MAGREF, BindWeave via ComfyUI-WanVideoWrapper (Kijai), LTX-2.5 avec workflows officiels pour chaque IC-LoRA, SeedVR2.

**Wan2GP** est une alternative « basse VRAM » tout-en-un : très à jour (v17.10 le 6 octobre 2026), avec Wan, LTX-2.5, Qwen Image, TTS et une interface Gradio. Sa vocation reste plutôt l'usage interactif.

Le pipeline Orbeo existant (Python + client Agnes + juge LLM + ffmpeg) peut appeler ComfyUI exactement comme il appelle Agnes : un service de plus, derrière une URL.

### Cited Findings
- Routes du serveur ComfyUI :
  - `POST /prompt` soumet un workflow, renvoie `prompt_id` et la position dans la file, ou des erreurs de validation ;
  - `GET /history/{prompt_id}` donne l'historique ;
  - `GET /view` sert les images ;
  - `POST /upload/image` envoie une image ;
  - `GET /queue` donne l'état de la file ;
  - `WebSocket /ws` envoie les messages `executing`, `progress`, `executed`.

  — [ComfyUI docs, comms_routes](https://docs.comfy.org/development/comfyui-server/comms_routes)
- LTX-2.5 : « ComfyUI official integration », fichiers « Comfy-aligned » ; chaque IC-LoRA fournit son workflow `.json` (par exemple `LTX-2.5_ICLoRA_Layout_To_Render_Two_Stage_Distilled.json`). — [HF Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) ; [HF Layout-To-Render](https://huggingface.co/Lightricks/LTX-2.5-22b-IC-LoRA-Layout-To-Render)
- ComfyUI-WanVideoWrapper (Kijai) prend en charge Phantom, MAGREF et BindWeave (versions FP8 par Kijai). — [GitHub Phantom](https://github.com/Phantom-video/Phantom) ; [GitHub MAGREF](https://github.com/MAGREF-Video/MAGREF) ; [GitHub BindWeave](https://github.com/bytedance/BindWeave)
- Wan2GP :
  - modèles vidéo « Wan 2.1/2.2 … MiniMax H3, LTX-2/2.3/2.5, Hunyuan Video 1/1.5, LongCat, Kandinsky » ; modèles image « Qwen Image, Z-Image, Flux 1/2 (Klein) » ; « Low VRAM requirements: run select models with as little as 6 GB of VRAM » ;
  - v17.00 (6 oct. 2026) : « 15 seconds of H3 video at 1080p used to require 25 GB of VRAM, now you just need 11 GB » ;
  - v17.10 : outils VFX LTX-2.5 (Layout to Render, Alpha Gen, SDR→HDR).

  — [GitHub deepbeepmeep/Wan2GP](https://github.com/deepbeepmeep/Wan2GP)
- **[TEST LOCAL]** `gradio_client` permet d'appeler un Space comme une API : `view_api()` a renvoyé les signatures de `Qwen/Qwen-Image-Edit-2511` (`/infer` : images, prompt, seed, true_guidance_scale, num_inference_steps, height, width, rewrite_prompt) et de `zerogpu-aoti/wan2-2-fp8da-aoti-faster` (`/generate_video` : input_image, prompt, steps=6, duration_seconds=3.5…). Script : `scratchpad/hf_space_test.py`.

### Inferences
- Architecture d'automatisation recommandée : garder l'orchestrateur Python actuel (`make_episode.py`) et ajouter un « fournisseur » ComfyUI. Concrètement :
  - une instance ComfyUI sur un GPU loué à la demande (RunPod, Vast ou Modal) ;
  - les workflows API versionnés dans le dépôt (Qwen-Image-Edit-2511 pour les images clés, LTX-2.5 Ingredients ou Wan-Phantom pour les clips, upscale) ;
  - le même juge visuel qu'aujourd'hui.
- Pas besoin d'un « monstre » : un seul pod GPU démarré par script, 2 à 3 workflows JSON, arrêt automatique en fin d'épisode.

### Gaps
- Je n'ai pas lancé ComfyUI (pas de GPU) ni testé `comfy-cli`. L'export « API format » est documenté ailleurs que sur la page lue.

---

## 7. Où trouver du GPU gratuit ou très bon marché pour des modèles ouverts, de façon automatisée ?

### Takeaway
**Le gratuit n'est pas automatisable de façon fiable** :
- **ZeroGPU anonyme** : 2 min par jour. Mon test a été refusé : `360s requested vs. -180s left`. Le quota est sans doute partagé par l'IP du conteneur.
- **Compte HF gratuit** : 5 min par jour.
- **Colab gratuit** : limites non publiées ; l'usage hors interface notebook est interdit.
- **Kaggle** offre un vrai GPU (T4 ×2 par défaut) **pilotable par CLI** (`kaggle kernels push` / `status` / `output`). C'est la meilleure option gratuite programmable, avec un quota hebdomadaire que je n'ai pas pu vérifier.

**Le très bon marché est la vraie solution**, toutes deux scriptables par API :
- **Vast.ai** : RTX 3090 vérifiée autour de **0,16 à 0,21 $/h**, RTX 4090 autour de **0,36 à 0,47 $/h** (offres en direct du 2026-10-06) ;
- **RunPod** Community : RTX 3090 **0,22 $/h**, RTX 4090 **0,34 $/h**, Serverless 4090 1,10 $/h.

**Modal** offre **30 $ par mois de crédits gratuits** (L4 environ 0,80 $/h, A100 80 Go environ 2,50 $/h), l'option la plus simple à programmer (Python, à la seconde). Ces 30 $ couvrent largement des tests mensuels. **HF PRO** (40 min de ZeroGPU par jour, puis 1 $ les 10 min) convient pour appeler des Spaces existants par `gradio_client`.

### Cited Findings
- ZeroGPU :
  - matériel : « NVIDIA RTX Pro 6000 Blackwell », taille `large` = moitié de GPU, 48 Go ; `xlarge` = 96 Go, coût ×2 ;
  - quota quotidien : « Unauthenticated 2 minutes ; Free account 5 minutes ; PRO account 40 minutes (extensible) ; Team 40 ; Enterprise 60 » ;
  - « Included daily quota resets exactly 24 hours after your first GPU usage » ;
  - au-delà, pour PRO : « pre-paid credits at the rate of $1 per 10 minutes of GPU time » ;
  - hébergement : 2 Spaces ZeroGPU pour un compte gratuit (compte de plus de 30 jours), 10 pour PRO ; Gradio uniquement.

  — [HF docs, Spaces ZeroGPU](https://huggingface.co/docs/hub/spaces-zerogpu)
- **[TEST LOCAL]** `gradio_client` sans jeton :
  - `Qwen/Qwen-Image-Edit-2511` (30 pas, 1344×768) : refus immédiat, « You have exceeded your ZeroGPU quota (**360s requested vs. -180s left**)… Authenticate with a Hugging Face token for more quota » ;
  - `zerogpu-aoti/wan2-2-fp8da-aoti-faster` : `CancelledError` après 3 s.
  - Le conteneur n'a ni variable `HF_TOKEN` ni fichier de jeton. Le quota anonyme était déjà négatif, sans doute consommé par un autre agent sur la même IP.
- Modal : « Starter plan includes $30/month in free compute credits ». Prix à la seconde : T4 0,000164 $ (environ 0,59 $/h), L4 0,000222 $ (environ 0,80 $/h), A10 0,000306 $, L40S 0,000542 $ (environ 1,95 $/h), A100 40 Go 0,000583 $, A100 80 Go 0,000694 $ (environ 2,50 $/h), H100 0,001097 $ (environ 3,95 $/h). — [Modal pricing](https://modal.com/pricing)
- RunPod, prix à l'heure Community / Secure :
  - RTX 3090 0,22 / 0,50 $ ; RTX 4090 0,34 / 0,74 $ ; RTX 5090 0,69 / 0,99 $ ; L4 0,44 / 0,49 $ ; L40S 0,79 / 1,09 $ ; A100 80 Go 1,19 / 1,59 $ ; RTX A5000 0,16 / 0,27 $ ;
  - Serverless flex : 4090 1,10 $/h, L4 0,69 $/h, A100 2,72 $/h ;
  - stockage réseau 0,07 $/Go/mois.

  — [RunPod pricing](https://www.runpod.io/pricing)
- **[TEST LOCAL]** API publique d'offres Vast.ai (`console.vast.ai/api/v0/bundles`, à la demande, 1 GPU, hôtes vérifiés, 2026-10-06), en $/h :

  | GPU | n | min | médiane |
  |---|---|---|---|
  | RTX 3090 | 31 | 0,156 | 0,205 |
  | RTX 4090 | 43 | 0,363 | 0,467 |
  | RTX 5090 | 42 | 0,468 | 0,584 |
  | L40S | 3 | 0,801 | 0,801 |
  | A100 SXM4 | 10 | 0,403 | 0,633 |
  | H100 SXM | 5 | 1,910 | 2,778 |

  Ce sont des prix de marché, qui varient. — [Vast.ai API](https://console.vast.ai/api/v0/bundles/)
- Kaggle CLI :
  - « `kaggle kernels push` … Pushes new code/notebook and metadata to a kernel, then runs the kernel » ;
  - option `--accelerator` : « "NvidiaTeslaT4" (GPU T4 ×2, default GPU), "NvidiaL4", "TpuV5E8" » ;
  - « Accelerators available as of Sep 2026 » : T4 ×2, A100, L4, L4X1, H100, RtxPro6000, TPU, avec la mention « Some of these are only available to participants of specific competitions, and some are only available to Kaggle admins » ;
  - `kaggle kernels status` et `kaggle kernels output` pour suivre un run et récupérer ses fichiers ;
  - champ `enable_internet` dans `kernel-metadata.json`.

  — [GitHub Kaggle/kaggle-api, docs/kernels.md](https://github.com/Kaggle/kaggle-api/blob/main/docs/kernels.md) ; [kernels_metadata.md](https://github.com/Kaggle/kaggle-api/blob/main/docs/kernels_metadata.md)
- Colab :
  - « Colab does not publish specific usage limits … idle timeout periods, maximum VM lifetime, GPU types available … vary over time » ;
  - « notebooks can run for at most 12 hours » ;
  - interdit en gratuit : « Remote control (SSH, remote desktops) », « bypassing the notebook UI to interact primarily via a web UI », « Running distributed computing workers » ;
  - Pro+ : « continuous code execution for up to 24 hours ».

  — [Colab FAQ](https://research.google.com/colaboratory/faq.html)

### Inferences
- **Classement pour un usage automatisé et planifié** :
  1. **Vast.ai ou RunPod Community à la demande** : un pod créé par API, un script ComfyUI ou Python, puis destruction du pod. Le moins cher par heure (0,2-0,5 $/h pour 24 Go). Un épisode estimé à 1-3 h de GPU (inférence) coûterait environ 0,5 à 1,5 $.
  2. **Modal** : l'intégration Python la plus propre, facturé à la seconde, 30 $ gratuits par mois. Plus cher par heure, mais sans gestion de machine.
  3. **Kaggle** : gratuit et scriptable par CLI. À tester pour des tâches longues non urgentes (entraînement de LoRA, rendus Blender par lots). Le quota hebdomadaire et la vérification par téléphone restent à confirmer.
  4. **HF PRO** (prix non vérifié ici) : pratique pour appeler des Spaces existants (Qwen-Image-Edit, Wan, LTX). 40 min par jour suffisent pour environ 20 à 60 images clés par jour, selon le modèle (inférence). Ces Spaces publics changent sans préavis, ce qui est fragile pour une production.
  5. **Colab gratuit** : à exclure pour l'automatisation, en raison de ses conditions d'usage.
- RunPod Serverless (environ 1,10 $/h en 4090, sans facturation à l'arrêt) convient si les appels sont rares et courts. Les démarrages à froid (chargement des modèles de 14 à 22B) mangeront du temps facturé (inférence).

### Gaps
- Quota GPU hebdomadaire de Kaggle (souvent cité à « 30 h/semaine », **[non vérifié]** : la page de documentation Kaggle est rendue en JavaScript et n'a pas pu être lue) et obligation de vérification par téléphone.
- Prix de HF PRO et offres gratuites de Lightning AI : leurs pages n'ont pas pu être lues (rendu JS ou délai d'attente).
- Crédits d'essai RunPod et Vast : non mentionnés sur les pages lues.

---

## 8. Stack recommandée pour Orbeo, par besoin (1 à 7)

### Takeaway
Recommandation en deux temps, pour éviter le « monstre technique ».

**Tout de suite, sans GPU et sans coût**, corriger le pipeline Agnes avec les règles testées au §3 :
- images clés en **scène + une image d'identité de Lulu, une pose** ;
- jamais de planche multi-poses en référence ;
- références d'épisode nettoyées (nœud sur Nino) ;
- plans à petit déplacement en v2.0 ;
- 2.5-flash « reference » pour les plans d'action à caméra fixe, avec des coupes franches ;
- Lanczos pour le 1080p.

**Ensuite, sur GPU loué à 0,2-0,5 $/h** (Vast ou RunPod) ou Modal (30 $ gratuits par mois), via ComfyUI :
- **Qwen-Image-Edit-2511** (Apache) pour les images clés, avec plus tard un **LoRA Lulu** ;
- **LTX-2.5** (gratuit sous 10 M$) avec **Ingredients** (planche personnage + décor) pour les clips ;
- **Layout-to-Render** sur un blocage Blender scripté, pour une caméra et des positions déterministes ;
- **Wan 2.2 / Phantom / BindWeave** (Apache) en plan B ;
- **RIFE** ou **FILM** et **SeedVR2** si besoin.

À **exclure** : HunyuanVideo 1.5, MiniMax H3 (licences hors UE), Qwen-Image-2.1 (non commercial), GIMM-VFI (non commercial), poids FLUX.1/2 dev et klein 9B (non commerciaux).

### Cited Findings
Synthèse des sections 1 à 7 (sources dans chaque section). Ordre des colonnes : qualité → coût → vitesse → automatisation → difficulté → licence → résultat réel.

| Besoin | Brique | Qualité | Coût | Vitesse | Automatisation | Difficulté | Licence (commercial ?) | Résultat réel |
|---|---|---|---|---|---|---|---|---|
| 1. Cohérence des personnages | Agnes image 2.5-flash, scène + 1 identité | bonne | gratuit | 16-35 s par image | API, déjà en place | faible | service tiers | **[TEST LOCAL]** 2/2 propres, contre 4/4 doublons avec une planche |
| 1. Cohérence | LoRA Lulu (ai-toolkit) sur Qwen-Edit-2511, FLUX.2 klein 4B ou LTX-2.5 | élevée attendue | quelques $ de GPU (inférence) | ? | CLI/YAML | moyenne | Apache / Apache / LTX < 10 M$ | non testé |
| 1. Cohérence | Blender riggé | parfaite | modèle 3D à faire ou commander | CPU : 48 s par image (Cycles 720p) | Python `bpy`, sans écran | **élevée** (art 3D) | GPL (outil), contenu à Orbeo | **[TEST LOCAL]** pip + rendu sans écran OK |
| 2. Vidéo | LTX-2.5 (+ Ingredients) | élevée (multi-plans, audio) | GPU 24 Go ou plus | ? | ComfyUI, workflows officiels | moyenne | gratuit < 10 M$ | non testé |
| 2. Vidéo | Wan 2.2 + Phantom / BindWeave / VACE | bonne | GPU 24 Go (5B) ; 14B FP8 | ? | ComfyUI-WanVideoWrapper | moyenne | Apache-2.0 | non testé (quota ZeroGPU) |
| 2. Vidéo | Agnes 2.5-flash « reference » | bonne (action, caméra fixe) | gratuit (2.5 non flash payant) | 1,5-10 min avec la file | API | faible | service tiers | **[TEST LOCAL]** action OK, mais scène recomposée |
| 3. Pose / caméra | Blocage Blender + LTX-2.5 Layout-to-Render | caméra et positions exactes | GPU | ? | script + ComfyUI | moyenne | GPL + LTX | non testé |
| 3. Pose / caméra | Wan-Animate-2 / SCAIL-2 (vidéo de pilotage) | bonne | GPU | ? | scripts | moyenne | Apache / MIT | non testé |
| 4. Multi-références (image) | Qwen-Image-Edit-2511 / FLUX.2 klein 4B | élevée | GPU 13 Go ou plus (klein) | < 1 s (klein, GPU) | ComfyUI / diffusers | faible à moyenne | Apache-2.0 | non testé (quota) |
| 5. Upscale | Lanczos ffmpeg / Real-ESRGAN x2plus / SeedVR2 | correcte / bonne / élevée | 0 / GPU / GPU | temps réel / 40 s par image CPU / ? | ffmpeg / Python | faible | — / BSD-3 / Apache | **[TEST LOCAL]** CPU mesuré |
| 5. Interpolation | RIFE v4.26 (ccvfi) / FILM | bonne | 0 | 2,15 s par image CPU | pip | faible | MIT / Apache | **[TEST LOCAL]** CPU mesuré |
| 6. Automatisation | ComfyUI API (+ Wan2GP en appoint) | — | 0 | — | `POST /prompt`, `/ws` | moyenne | GPL (outil) | non testé |
| 7. GPU | Vast / RunPod / Modal / Kaggle / HF PRO | — | 0,16-0,47 $/h / 30 $ gratuits par mois / gratuit / quota | — | API / API / Python / CLI / gradio_client | faible à moyenne | — | **[TEST LOCAL]** ZeroGPU anonyme refusé |

### Inferences
- **Ordre conseillé** :
  1. Appliquer les règles Agnes du §3 (immédiat, gain mesurable sur les doublons et les hybrides).
  2. Ouvrir un compte Vast ou RunPod, ou Modal (30 $ gratuits), et monter **un** workflow ComfyUI Qwen-Image-Edit-2511 pour les images clés. Comparer avec Agnes sur les mêmes 8 plans, jugés par le juge LLM existant.
  3. Tester LTX-2.5 Ingredients avec la planche de Lulu (`lulu_sheet.png`, une fois remise sur fond noir).
  4. Si la caméra et la taille de Lulu restent instables, ajouter le blocage Blender scripté et Layout-to-Render.
  5. Entraîner un LoRA Lulu (et un LoRA Nino) seulement quand le jeu d'images propres existe.
- Garder Agnes comme fournisseur gratuit tant que sa qualité suffit. Prévoir sa disparition ou sa saturation (3 soumissions 2.5-flash sur 4 refusées pour file pleine, jusqu'à 41 min ; modèle 2.5 payant) en gardant le pipeline multi-fournisseurs.

### Gaps
- Aucun modèle ouvert n'a pu être testé en conditions réelles (pas de GPU, ZeroGPU refusé). Les verdicts de qualité sur les modèles ouverts restent donc **non vérifiés** pour le style de Lulu.
- Pas de retours d'utilisateurs (recherche web épuisée).
