# Production d'une série IA quotidienne de 60 à 90 s en français (TikTok, Reels, Shorts) : outils, tests Agnes, coûts et stack recommandée (état au 2026-10-08)

Notes de recherche et de tests du 2026-10-08 pour Orbeo Studio (une personne et des agents IA, France), ligne « non jeunesse ». Cible : épisodes verticaux 9:16 en 1080p, 3 à 6 personnages récurrents qui parlent français, lip-sync, rythme comique, sous-titres incrustés, publication par Metricool.

Conventions :
- **[TEST LOCAL]** : mesuré ici le 2026-10-08 (conteneur CPU, 15 Go de RAM). J'ai regardé moi-même les images extraites. Toutes les sorties et les scripts sont dans `/tmp/claude-0/-home-user-tiktok-auto/c3103019-a176-5027-8bcf-8e27361d44f5/scratchpad/tests_tiktok/`.
- **[notes 10-06]** : résultat repris des notes du 2026-10-06 (`research_notes/Franchise jeunesse IA Orbeo/briques_image_video.md` et `briques_voix_musique_lipsync.md`). Je ne l'ai pas refait.
- **[vendeur]** : page d'un éditeur qui vend l'outil ou un accès à l'outil. **[agrégateur]** : reprise de seconde main. **[non vérifié]** : affirmation que je n'ai pas pu confirmer.
- Aucune source de cette note n'est antérieure à 2025, sauf mention **[ancien]**.
- La clé Agnes a été lue depuis `~/.agnes_key` sans être affichée. J'ai vérifié qu'elle n'apparaît dans aucun fichier de sortie.

---

## 1. Qu'utilisent les séries IA en tête (Fruit Love Island, L'Île de la Skibidi Tentafruit, sitcoms et micro-dramas IA), et combien de temps prend un épisode ?

### Takeaway
Les deux séries de référence de 2026 sont artisanales. Chacune est faite par une ou deux personnes anonymes, qui n'ont jamais publié leur stack exacte.

- **Fruit Love Island** : environ **3 h par épisode de 2 min**, publié presque chaque jour.
- **Skibidi Tentafruit** (version française) : **environ 7 h par épisode**, pour « quelques dizaines d'euros ».

Les outils cités par la presse, souvent de seconde main, sont les suivants :
- un LLM (ChatGPT, Gemini) pour les dialogues ;
- **Nano Banana 2** (Gemini) pour la cohérence des personnages ;
- **Veo, Kling** (et Sora, dont l'application aurait fermé) pour l'animation ;
- une **voix de synthèse** ;
- **Final Cut, Premiere ou CapCut** pour le montage ;
- **FL Studio** pour la musique.

Leur point faible est connu. Le créateur de Fruit Love Island s'est plaint que « la génération d'images et d'animation devient si mauvaise » qu'il refaisait sans cesse des plans. Ensuite, 12 épisodes sur 22 ont été retirés de TikTok, et la série s'est arrêtée au bout de 15 jours.

### Cited Findings

**Fruit Love Island (États-Unis, TikTok @ai.cinema021)**
- Lancement le 13 mars 2026. Épisodes de 2 à 4 min, 28 épisodes sur 2 saisons. Plus de 3 millions d'abonnés en 9 jours et plus de 300 millions de vues, avec en moyenne plus de 10 millions de vues par épisode (CNN, WSJ). Production arrêtée le 28 mars 2026, après une série de messages du créateur en story (Gizmodo). Fin de série, épisodes retirés par TikTok ; le créateur a promis de continuer sur YouTube (NBC). — [Wikipedia, Fruit Love Island](https://en.wikipedia.org/wiki/Fruit_Love_Island)
- « each two-minute episode takes around three hours to make ». Les épisodes sont mis en ligne « pretty much daily ». Au 23 mars 2026 : 19 épisodes, plus de 3 M d'abonnés, plus de 10 M de vues en moyenne par épisode. — [Dexerto, 2026-03-23](https://www.dexerto.com/tiktok/fruit-love-island-is-the-internets-new-obsession-as-ai-videos-get-millions-of-views-3339289/)
- Citations du créateur :
  - « Guys I'm losing motivation. These videos take so long and the image and animation gen is getting so bad! » ;
  - « All my videos banned I make no money ».

  Au 31 mars, 12 épisodes sur 22 ne sont plus visibles et le compte YouTube a lui aussi été supprimé. La cause est floue : signalements de masse, ou règles de TikTok sur la propriété intellectuelle (parodie de *Love Island*). L'épisode le plus vu atteint 38,7 M de vues. — [Fast Company via Yahoo Tech, 2026-03-31](https://tech.yahoo.com/ai/articles/fruit-love-island-tiktok-most-163000352.html)
- Le site officiel présente la série comme l'œuvre de « AI Cinema », un créateur indépendant qui utilise des outils IA. Une seule personne prend toutes les décisions créatives. — [fruitloveisland.ai/about](https://fruitloveisland.ai/about/) (lu via un extrait de recherche, page non ouverte)
- Méthode rapportée par New York Magazine, et reprise par L'ADN : les personnages sont créés avec « Object Talk », un GPT personnalisé, puis animés sur une plateforme comme **OpenArt**. — [L'ADN, 2026-03-26](https://www.ladn.eu/media-mutants/lile-de-la-skibidi-tentafruit-le-short-drama-ia-le-plus-viral-du-tiktok-francais/)
- Le créateur du dérivé *Fruit Paternity Court* (étudiant britannique de 20 ans) dit à WIRED utiliser « Google Veo, Kling AI, or Sora ». Le même texte indique qu'OpenAI a annoncé la fermeture prochaine de Sora. — [WIRED, republié par winzheng.com](https://www.winzheng.com/en/article/dark-side-viral-ai-fruit-videos) **[agrégateur : republication, date non visible]**

**L'Île de la Skibidi Tentafruit (France, compte OnlyMoviesFr)**
- Équipe : deux étudiants français. Épisodes de **1 à 6 min**. Temps de production : « environ sept heures de travail » par épisode. Coût : « quelques dizaines d'euros par épisode ». Outils cités :
  - **ChatGPT et Gemini** pour les dialogues (références Gen Z et « Gen Alpha ») ;
  - **Nano Banana 2** pour la cohérence graphique des personnages ;
  - **Final Cut Pro et Premiere Pro** pour le montage ;
  - **FL Studio** pour les thèmes musicaux.

  Audience : 266 M de vues sur TikTok. Revenus estimés par le magazine (non confirmés) : 130 000 à 260 000 € via le programme de récompenses de TikTok. Partenariat Oasis. Article modifié le 19 avril 2026. — [75secondes](https://www.75secondes.fr/?p=182873)
- Selon L'ADN : vidéos d'environ 5 min, une présentatrice-poire résume chaque épisode, jusqu'à 9 M de vues par épisode. Le créateur n'a pas répondu à la demande d'entretien. La bio du compte renvoie vers des vidéos payantes promettant de « gagner sa vie sur TikTok ». — [L'ADN, 2026-03-26](https://www.ladn.eu/media-mutants/lile-de-la-skibidi-tentafruit-le-short-drama-ia-le-plus-viral-du-tiktok-francais/)
- Selon Blog-ia : « Une voix de synthèse assure ensuite les dialogues ». Les clips sont assemblés « avec sous-titres et transitions ». « Un abonnement de quelques dizaines d'euros par mois suffit pour produire régulièrement. » Audience : près de 3 M d'abonnés en une dizaine de jours, plus de 100 M de vues. Page mise à jour le 6 octobre 2026. — [Blog-ia](https://blog-ia.com/skibidi-tentafruit-ia/)
- Les sources divergent sur le temps de travail : environ 7 h par épisode selon 75secondes, 3 h selon Blog-ia (d'après un résumé de recherche ; je n'ai pas retrouvé ce chiffre en lisant la page), « quelques heures » selon Siècle Digital (page en 403, lue seulement via un extrait). — [75secondes](https://www.75secondes.fr/?p=182873) ; [Siècle Digital](https://siecledigital.fr/2026/03/31/tiktok-ce-que-lon-sait-sur-le-phenomene-de-lile-de-la-skibidi-tentafruit/)
- Copies françaises (AFP, 30 mars 2026) :
  - épisodes d'environ 1 min, qui finissent tous par un teaser « bientôt disponible » ;
  - placements de produits (crème, cigarette électronique, protéines) chez docteur.einstein ;
  - formations vendues de 40 à 150 €.

  — [CB News / AFP](https://www.cbnews.fr/cb/tiktok-juteux-business-videos-fruits-sexistes-generees-ia)

**Micro-dramas IA en général (sources surtout éditeurs)**
- Chaîne en cinq étapes décrite dans un reportage vietnamien :
  1. script avec ChatGPT ou Claude ;
  2. personnages avec Midjourney, Flux ou Gemini ;
  3. vidéo avec Seedance, Kling ou Veo ;
  4. voix et musique avec ElevenLabs ou Suno ;
  5. finition sous Premiere ou CapCut.

  — [SGGP](https://en.sggp.org.vn/ai-rewrites-microdrama-production-line-post130111.html)
- Répartition proposée par Minionarts : Kling 3.0 « default for action beats », Seedance 2.0 pour les dialogues (lip-sync), ElevenLabs pour la couche voix et lip-sync, un modèle image pour fixer personnages et lieux. — [Minionarts](https://www.minionarts.com/blogs/best-ai-tools-make-microdramas-2026) **[vendeur, environ 4 mois]**
- Recette de continuité proposée par invideo : « start every scene with a wide establishing shot, then generate each subsequent shot using the previous video as a spatial layout reference » (Seedance 2.0 en mode référence → vidéo). Format type : 60 à 120 s par épisode, saisons de 60 à 100 épisodes. — [invideo](https://invideo.io/blog/how-to-make-ai-micro-drama/) **[vendeur]**
- Programme IMDA (Singapour) et TikTok, 1er octobre 2026 : séries de 50 à 100 épisodes de 1 à 3 min, avec Seedance 2.5 de ByteDance. — [TNGlobal](https://technode.global/2026/10/01/imda-partners-tiktok-to-develop-local-microdrama-expertise-and-fuel-a-new-pipeline-of-original-ip)

### Inferences
- Le « standard » des séries virales tient en cinq éléments : LLM, image Nano Banana, clip Veo ou Kling, voix de synthèse, montage manuel. Il produit un épisode en **3 à 7 h de travail humain**, surtout pour relancer les plans ratés. Un rythme quotidien suppose donc soit 3 à 7 h par jour, soit beaucoup d'automatisation et un **contrôle qualité automatique** (whisper, juge visuel).
- **Deux risques à retenir pour Orbeo** :
  - **Propriété intellectuelle** : parodier une émission connue a sans doute contribué aux retraits de Fruit Love Island (cause non confirmée). Orbeo doit garder des concepts originaux, comme ce test croissant/baguette.
  - **Lassitude de la qualité** : le créateur a abandonné quand la génération « devenait mauvaise ». Le pipeline doit pouvoir changer de fournisseur sans tout refaire.
- La forme commune à toutes ces séries est : épisode court, cliffhanger final, teaser « prochain épisode », sous-titres incrustés, numérotation. C'est cohérent avec la cible de 60 à 90 s.

### Gaps
- Aucune interview de premier plan ne détaille la stack exacte de Fruit Love Island ou de Skibidi Tentafruit : TikTok et Instagram ne sont pas lisibles ici, et Le Temps et Siècle Digital ont répondu 403.
- Je ne sais pas si les voix françaises de Skibidi Tentafruit sont l'audio natif du modèle vidéo (Veo, Kling) ou un TTS ajouté au montage.
- Je n'ai trouvé aucune source sur des comptes de sitcom ou de soap IA français autres que les fruits (temps, outils, revenus).
- Je n'ai trouvé aucune source fiable sur Hailuo (MiniMax) en 2026 pour ce type de série.

---

## 2. [TEST LOCAL] L'API gratuite Agnes peut-elle produire une scène de dialogue français convaincante à 2 personnages, en 9:16 ?

### Takeaway
**Oui pour l'audio, presque pour l'image, avec un défaut bloquant à contourner.**

`agnes-video-v2.0` en image → vidéo vertical (704×1280, 24 i/s) produit en **113 à 164 s** un clip où :
- les **deux personnages disent chacun leur réplique française**, transcrite **exactement** par whisper sur le premier clip ;
- les **voix sont distinctes** (F0 médiane 198-246 Hz pour le croissant contre 372-421 Hz pour la baguette) ;
- **seul le personnage qui parle bouge la bouche** (3 clips sur 3) ;
- le jeu comique est bon (froncement, yeux au ciel sur demande).

Mais **3 clips sur 3 contiennent des pseudo-sous-titres incrustés illisibles** (« Onccr etraled Biggute!! »), malgré « no subtitles » dans le prompt, un prompt négatif et une réplique sans guillemets. Il faut les masquer au montage. Une bande floutée sous nos propres sous-titres marche bien (testé).

Autres défauts :
- dérive de cadrage et recomposition du décor sur le premier clip ;
- croissant souriant au lieu de grognon au début des plans larges ;
- légère variation de la voix d'un même personnage d'un clip à l'autre ;
- « Hmm… » improvisés ;
- un mot déformé (« métière »).

`agnes-video-2.5-flash` est resté inutilisable : file pleine (503) puis 429, aucun travail créé en 417 s.

### Cited Findings
Toutes les données ci-dessous sont **[TEST LOCAL]**. Scripts : `tiktok_dialogue_test.py`, `tiktok_closeup_img2.py`, `assemble_episode.py`, `asr_dialogue.py`, `words.py` (copiés dans `tests_tiktok/`). Client utilisé : `~/agnes-video-generator/core/api` (sans le serveur :8765). Transcription : faster-whisper `small`, CPU int8.

**A. Images clés (agnes-image-2.5-flash, texte → image, 768×1344 demandé, 736×1312 obtenu)**
- 2 images en parallèle, **12 s** chacune.
- Prompt : boulangerie parisienne, « Gaston » le croissant grognon (sourcils broussailleux), une baguette anxieuse, plan moyen à deux.
- Résultat : 2/2 propres. Exactement 2 personnages, designs lisibles, style 3D cohérent, bouches visibles. Défaut : charabia sur l'ardoise. Fichiers `kf_bakery_1.png`, `kf_bakery_2.png`, planche `kf_compare.jpg`.
- **Inversion d'identité** : avec « medium close-up of Gaston the grumpy croissant » et la scène comme seule référence, on obtient **2/2 baguettes avec le visage et les bras croisés du croissant**. Le nom propre n'est pas relié au bon personnage. Fichier `kf_closeup_compare.jpg`.
- Correction : référence 1 = scène, référence 2 = **recadrage isolé du croissant**, et un prompt descriptif sans nom propre (« the golden croissant character only (a croissant, NOT a baguette) »). On obtient **2/2 croissants corrects et fidèles**, en 19 et 24 s. Le cadrage reste plus large que le gros plan demandé. Fichier `kf_closeup2_compare.jpg`. La règle « scène + une seule référence d'identité » des [notes 10-06] est ainsi confirmée.

**B. Clips vidéo (3 générations lancées, 1 sans travail créé)**

| Clip | Modèle et mode | Attente | Sortie | Audio (whisper, langue fr p = 1,0) | Image (10 vignettes regardées) |
|---|---|---|---|---|---|
| A | 2.5-flash, « reference », 1 image, 9:16, 8 s | **417 s, échec** | — | — | `HTTP 503 video_queue_full` répété, puis `429 rate limit`, puis « max retries exceeded ». Aucun travail créé |
| B | v2.0, image → vidéo, `kf_bakery_2`, 10 s, 2 répliques entre guillemets | **164 s** | 704×1280, 24 i/s, 10,04 s, AAC stéréo 48 kHz | « Encore en retard, baguette ! » (0,0-3,9 s) / « Pardon ! Le four m'a fait peur ! » (3,9-7,2 s) : **transcription exacte**. F0 croissant 246 Hz, baguette 372 Hz | Bonne attribution des bouches. **Zoom avant puis recadrage** ; vers 5 s la scène est recomposée (ardoise en charabia, **baguette supplémentaire posée** sur le comptoir). Croissant **souriant** au début. **Pseudo-sous-titres** « Onccr etraled Biggute!! », « Darl! Borid Sage!! », plus un texte parasite final |
| C | v2.0, même image, prompt « locked-off… never zooms », voix « very deep, gravelly old man », **prompt négatif** (subtitles, captions, text, zoom, extra characters…) | **141 s** | idem | « Hmm… » ajouté (2,0-2,9 s), puis « Encore en retard Baguette ! » (2,9-6,4 s) et « Pardon ! Le four **me m'a** fait peur ! » (6,4-10,0 s, fin de réplique **collée à la fin du clip**). F0 croissant 198 Hz, baguette 421 Hz | **Caméra quasi fixe** (net progrès). Bouches correctes. Croissant de nouveau souriant au début. **Pseudo-sous-titres toujours présents** (« Oncce ertrad, Bagute! ») |
| D | v2.0, image clé gros plan du croissant seul, 5 s, réplique **sans guillemets** (« spoken aloud only, never written on screen ») et même prompt négatif | **113 s** | 704×1280, 5,04 s | « Hmm… 10 ans de **métière** et toujours pas de respect ! » (« métier » déformé, ou erreur de whisper). F0 208 Hz | **Meilleur clip** : caméra fixe, identité stable, jeu demandé respecté (froncement, **yeux au ciel**), bouche bien articulée. **Pseudo-sous-titres encore là** (« Dix ans of metich, », « etfruyus pa sxpect! ») |

- Planches : `sheetB.jpg`, `sheetC.jpg`, `sheetD.jpg`. F0 mesurée par autocorrélation (`scratchpad/scripts/f0.py`) sur chaque réplique isolée (`f0B/`, `f0C/`, `f0D/`).
- Constance de la voix d'un même personnage : le croissant est à **246 Hz** (clip B, « deep grumpy male voice »), puis **198 Hz** et **208 Hz** (clips C et D, même description « very deep, gravelly old man »). La voix reste assez proche à description identique (environ 1 demi-ton entre C et D), mais elle n'est **pas verrouillée**. Aucune de ces valeurs n'est « grave » (une voix d'homme grave tourne autour de 85-130 Hz) : il s'agit de mesures F0 brutes, sans écoute humaine.
- Position des pseudo-sous-titres : toujours en bas au centre, entre **environ 75 et 87 % de la hauteur**, et **seulement pendant la parole**.

**C. Montage automatisé de démonstration (`assemble_episode.py`, ffmpeg + libass + faster-whisper)**
Étapes du script :
1. couper le silence initial de C ;
2. passer chaque clip en 1080×1920 (Lanczos) ;
3. **flouter la bande 73,5-88,5 % de la hauteur** pour masquer les pseudo-sous-titres ;
4. concaténer C et D ;
5. ajouter une **carte de fin de 2 s** (dernière image assombrie et floutée, texte « DEMAIN : Baguette démissionne ?! ÉP. 2 · abonne-toi ») ;
6. ajouter un **titre d'accroche** en haut de 0 à 1,6 s (« IL A 10 ANS DE MÉTIER… ET ZÉRO PATIENCE ») et un badge « ÉP. 1 · LA BOULANGERIE » ;
7. incruster des **sous-titres mot par mot** (3 mots maximum, mot courant en jaune et agrandi). Les sous-titres reprennent le **texte du script**, calé sur les horodatages whisper par `difflib` (18 mots sur 19 alignés). Les erreurs de transcription comme « métière » n'apparaissent donc jamais à l'écran ;
8. normaliser le son (`loudnorm` à −14 LUFS, −13,5 LUFS mesurés).

- Résultat : `montage/episode_test.mp4`, 1080×1920, 15,1 s, H.264 et AAC. **39 à 43 s de calcul CPU** pour 15 s de vidéo, whisper compris.
- Contrôle visuel (`episode_sheet2.jpg`, `episode_sheet3.jpg`) : le charabia est masqué et nos sous-titres sont propres.
- Deux bugs de découpage des sous-titres ont été corrigés en cours de test : morceaux à cheval sur deux répliques, et chevauchement de deux morceaux.
- Limites constatées :
  - la police DejaVu n'affiche pas les emojis (il faut Noto Color Emoji) ;
  - la bande floutée se voit un peu, comme un « verre dépoli ».

### Inferences
- **Verdict pour Orbeo** : Agnes v2.0 est **utilisable gratuitement** pour une série comique de dialogues, à quatre conditions :
  1. masquer systématiquement la bande des pseudo-sous-titres sous nos propres sous-titres (bande floutée, ou boîte opaque de style CapCut) ;
  2. préférer le **champ / contre-champ** (un personnage par plan, gros plan, 5 s). Le clip D est nettement meilleur que les plans à deux, et un locuteur par plan est aussi ce que conseille la doc LTX (§4) ;
  3. couper au montage les silences et les « Hmm » de début ;
  4. contrôler chaque réplique avec whisper (taux d'erreur proche de 0 attendu) et relancer si besoin.
- Le dialogue à deux dans un même plan **fonctionne** (attribution des bouches correcte 2/2), mais il expose davantage à la recomposition du décor et aux objets parasites (baguette supplémentaire en B).
- La **voix native varie** d'un clip à l'autre pour un même personnage. Pour une vraie constance sur des centaines d'épisodes, il faut soit verrouiller le timbre en post-production par **conversion de voix par personnage** (RVC/Applio, MIT, CPU possible d'après les [notes 10-06]), soit passer par TTS fixe + lip-sync (§4). Le client Agnes n'expose **aucune entrée audio** (aucun paramètre audio dans `agnes_video.py`). Avec Agnes, la seule voie est donc l'audio natif, suivi d'une conversion de voix.
- `agnes-video-2.5-flash` ne doit pas être une brique du chemin critique. Il a échoué aujourd'hui comme le 2026-10-06 (1 réussite sur 5 soumissions au total).
- Pour le nom des personnages : décrire l'espèce et l'apparence dans chaque prompt (« the golden croissant »), et ne pas compter sur un nom propre.

### Gaps
- Pas d'écoute humaine : je n'ai pas jugé le naturel, le comique ni l'accent français. Je n'ai que la transcription et la F0.
- Échantillon minuscule (3 clips, une seule graine) : les taux sont indicatifs.
- Je n'ai pas testé l'effacement des pseudo-sous-titres par inpainting vidéo, ni un prompt qui place volontairement les personnages plus haut dans le cadre. Je n'ai pas non plus testé le lip-sync sur des répliques plus longues (plus de 4 s) ni l'enchaînement de 8 à 10 plans.
- Le test de conversion de voix RVC sur l'audio natif reste à faire.

---

## 3. Cohérence des personnages sur des centaines d'épisodes : meilleures pratiques 2026 pour des personnages comiques non humains

### Takeaway
La pratique dominante en 2026 suit trois étapes :
1. **dessiner chaque personnage une fois** dans un modèle image (Nano Banana Pro ou 2 chez les créateurs payants) ;
2. garder une **bibliothèque de références** : une image d'identité propre par personnage, plus le décor ;
3. générer chaque plan en **référence → vidéo** ou image → vidéo depuis une image clé où le personnage est déjà correct.

Côté payant : Kling 3.0 « Elements » (1 à 4 images étiquetées personnage, objet ou décor), Seedance 2.x en référence → vidéo, Veo 3.1 (jusqu'à 3 images de référence, 9:16 natif depuis janvier 2026).

Côté libre : Qwen-Image-Edit-2511 ou FLUX.2 klein 4B (Apache) pour les images clés, LTX-2.5 Ingredients pour les clips, puis un **LoRA par personnage** quand un jeu d'images propres existe.

Pour des personnages-objets comme des viennoiseries, le risque principal n'est pas le visage mais la **confusion entre personnages** (inversion d'identité vue au §2) et l'apparition d'**objets en double**. Une référence isolée par personnage, un prompt descriptif et un juge visuel automatique restent indispensables.

### Cited Findings
- **Nano Banana Pro** : jusqu'à 14 images de référence et 5 sujets préservés, sortie jusqu'en 4K. Limites citées : l'identité vaut pour l'image seulement et « doesn't carry into video » ; la cohérence se dégrade quand on empile les retouches ou les grands changements de pose ; les petits détails dérivent. — [Flick.art](https://flick.art/blog/img2img-consistent-character/nano-banana) **[vendeur]**
- Même modèle : fidélité meilleure avec 6 références ou moins ; références d'au moins 1024×1024, 3 à 6 angles. Prix API d'environ 0,134 $ par image en 1K pour Pro et environ 0,067 $ pour Nano Banana 2. — [Laozhang](https://blog.laozhang.ai/en/posts/nano-banana-pro-face-consistency-guide) **[agrégateur]**. Les sources se contredisent sur la limite (8, 14 ou « illimité »). — [SelfieLab](https://selfielabstudio.com/blog/nano-banana-pro-multi-ref-character-workflow-guide-20260313)
- **Kling 3.0 Elements** : 1 à 4 images de référence par génération, chacune étiquetée personnage, objet ou décor. — [GlobalGPT](https://www.glbgpt.com/hub/kling-ai-character-consistency-explained/) **[agrégateur]**
- Kling 3.0 Omni : « video element reference and element voice control ». Le nombre d'« Elements » qu'on peut créer dépend du plan : 30 (gratuit), 50 (Standard), 150 (Pro et Premier), 500 (Ultra). — [Kling, guide officiel des crédits 3.0, 2026-07-28](https://kling.ai/blog/kling-video-3-0-credit-cost-guide)
- Un testeur juge Kling 3.0 cohérent sur un clip de 15 s, mais « weaker than Runway's reference system » pour le multi-scènes. — [StackSheriff](https://stacksheriff.com/ai-tools/kling-3-review/)
- **Veo 3.1** :
  - la mise à jour du 13 janvier 2026 permet la vidéo verticale native à partir d'images de référence — [TechCrunch](https://www.techcrunch.com/2026/01/13/googles-update-for-veo-3-1-lets-users-create-vertical-videos-through-reference-images/) ;
  - mais des développeurs rapportent des erreurs (« Unsupported output video aspect ratio » en 9:16 avec références, ou cas d'usage « not supported ») — [Google AI forum](https://discuss.ai.google.dev/t/veo-3-1-reference-images-docs-say-available-api-says-not-supported/111853) ; [Adobe Community, juillet 2026](https://community.adobe.com/questions-404/an-aspect-ratio-of-16-9-and-a-duration-of-8-seconds-is-required-to-generate-when-using-reference-images-with-veo-31-1632143).
- **Seedance 2.0** : « multi-person lip sync matching » reste un problème ouvert, et les meilleurs résultats viennent de prompts à un seul personnage et phrases courtes. — [Cutout.pro, guide audio Seedance 2.0](https://www.cutout.pro/learn/?p=2903) **[vendeur]**
- **Libre** (d'après les [notes 10-06], sources primaires Hugging Face) :
  - Qwen-Image-Edit-2511 (Apache-2.0, « improved character consistency », plusieurs images en entrée) ;
  - FLUX.2 klein 4B (Apache-2.0, multi-références, environ 13 Go de VRAM) ;
  - LTX-2.5 IC-LoRA « Ingredients » (planche personnages + décor sur fond noir, clips d'environ 5 s) ;
  - SkyReels-V3 R2V, BindWeave, Phantom (référence → vidéo) ;
  - ai-toolkit pour entraîner des LoRA sur Qwen-Image-Edit, FLUX.2 klein, Wan 2.2 et LTX-2.5.

  — [HF Qwen-Image-Edit-2511](https://huggingface.co/Qwen/Qwen-Image-Edit-2511) ; [HF LTX-2.5 Ingredients](https://huggingface.co/Lightricks/LTX-2.5-22b-IC-LoRA-Ingredients) ; [GitHub ostris/ai-toolkit](https://github.com/ostris/ai-toolkit)
- **[notes 10-06]** Agnes image : une **planche multi-poses** donnée en référence **duplique** le personnage (4/4). La configuration « scène + une seule image d'identité » donne 2/2 images propres. **[TEST LOCAL 10-08]** : sans référence isolée, un nom propre seul provoque une inversion d'identité (2/2) ; avec le recadrage isolé, 2/2 sont corrects (§2).

### Inferences
- **Recette conseillée pour Orbeo** (personnages-objets, 3 à 6 personnages) :
  1. **Bible visuelle** : pour chaque personnage, une image d'identité de face, sur fond neutre, une seule pose, et une description textuelle figée de 30 à 50 mots, réutilisée mot pour mot dans chaque prompt (espèce, couleur, signe distinctif). Pas de nom propre seul.
  2. **Décors fixes** : 3 à 5 lieux récurrents (boulangerie, arrière-boutique, rue), chacun avec une image « plan large » de référence.
  3. **Images clés par plan** : scène ou décor en référence 1, identité du personnage en référence 2 (un personnage par plan en champ / contre-champ). Le juge visuel vérifie l'espèce et le nombre de personnages.
  4. **Clips** : image → vidéo depuis l'image clé (Agnes v2.0 aujourd'hui ; LTX-2.5 Ingredients ou Kling Elements demain).
  5. **LoRA** par personnage (ai-toolkit, GPU loué) une fois 20 à 40 images validées réunies. Ce nombre est une hypothèse, sans source primaire (voir les [notes 10-06]).
- Des personnages **simples et graphiques** (silhouette d'objet, sourcils marqués, une couleur dominante) dérivent moins que des personnages détaillés : c'est un argument de design. Je ne l'ai pas mesuré ; c'est un raisonnement tiré des tests.

### Gaps
- Je n'ai trouvé aucune comparaison indépendante de la cohérence multi-épisodes (sur 100 épisodes ou plus) entre Kling Elements, Seedance et Veo pour des personnages non humains.
- Aucun modèle ouvert n'a été testé ici (pas de GPU).
- Le nombre de références de Seedance 2.0 (9 selon une synthèse de vendeur) n'est pas vérifié.

---

## 4. Voix françaises distinctes et constantes : audio natif du modèle vidéo, ou TTS + lip-sync ?

### Takeaway
Deux architectures existent.

**(a) Audio natif** (Agnes v2.0, Veo 3.1, Kling 3.0, Seedance 2.x, LTX-2.5) :
- le lip-sync est gratuit et parfait par construction, et le jeu est souvent bon ;
- mais la voix n'est **pas verrouillée** d'un clip à l'autre (variation mesurée au §2) et le texte peut être improvisé (« Hmm », mot déformé) ;
- pour le français, Veo 3.1 est dit « English-centric » et les langues listées pour Kling 3.0 et Seedance 2.0 n'incluent pas le français. **Agnes v2.0 parle français correctement (testé)**.

**(b) TTS fixe + lip-sync** :
- voix verrouillées par clonage et émotions dirigées (ElevenLabs v3 avec balises `[laughs]`, `[sighs]` et endpoint dialogue multi-locuteurs, ou Qwen3-TTS VoiceDesign + clone en libre) ;
- mais il faut une brique de lip-sync pilotée par l'audio, qui demande un GPU (InfiniteTalk, LongCat-Video-Avatar, LTX-2.5 audio → vidéo) ou un service payant.

**Recommandation** : à court terme, **(a) + conversion de voix par personnage** (RVC). À moyen terme, (b) quand un GPU est disponible.

### Cited Findings
- **Veo 3.1** : audio natif, lip-sync contextuel, « English-centric », sans paramètre de langue, clips de 8 s.
  **Kling 3.0** : « multilingual lip sync » en anglais, chinois, japonais, coréen et espagnol (le français n'est pas listé), 10 s, environ 0,095 $/s (Pro).
  **Vidu Q3** : 16 s, environ 0,06 $/s.
  — [Atlas Cloud, comparatif audio natif (mis à jour le 2026-02-28)](https://www.atlascloud.ai/blog/guides/ai-video-models-native-audio-compared) **[vendeur]**
- Kling officiel : « multilingual dialogue » sans liste de langues. Clips de 3 à 15 s. — [Kling, 2026-07-28](https://kling.ai/blog/kling-video-3-0-credit-cost-guide)
- **Seedance 2.0** : lip-sync dans « 8+ languages », dont l'anglais, le mandarin, le japonais et le coréen. Le mandarin est le plus constant ; le multi-personnage reste un problème ouvert. Le français n'est cité que pour Seedance 2.5, par un site tiers. — [Cutout.pro](https://www.cutout.pro/learn/?p=2903) **[vendeur]** ; [Seedance.tv, langues de Seedance 2.5](https://www.seedance.tv/blog/seedance-2-5-supported-languages) **[vendeur]**
- **LTX-2.5 Pro** (audio natif) :
  - mettre les mots prononcés entre guillemets et nommer la langue (« speaking in French ») ;
  - un locuteur par réplique pour un lip-sync propre ;
  - ajouter « no music », sinon le modèle met souvent de la musique ;
  - l'audio vient uniquement du prompt.

  — [Runware, LTX-2.5 Pro native audio](https://runware.ai/docs/models/lightricks-ltx-2-5-pro/guides/native-audio.md). Un mode audio → vidéo (une image + une piste audio → lip-sync) existe aussi. — [Runware, audio-driven](https://runware.ai/docs/models/lightricks-ltx-2-5-pro/guides/audio-driven)
- Date de LTX-2.5 : les poids ouverts seraient sortis le 11 août 2026 selon ComfyUI-Wiki, alors que la fiche HF lue le 2026-10-06 donnait le 23 juillet 2026. **Les deux sources se contredisent.** — [ComfyUI-Wiki](https://comfyui-wiki.com/en/news/2026-08-11-ltx-2-5-open-weights-release) ; [notes 10-06]
- **ElevenLabs** (page tarifs lue le 2026-10-08) :

  | Plan | Prix par mois | Crédits par mois (environ min de TTS) | Remarques |
  |---|---|---|---|
  | Free | 0 $ | 10 k (environ 10 min) | sans licence commerciale |
  | Starter | 6 $ | 30 k (environ 30 min) | licence commerciale, clonage instantané |
  | Creator | 22 $ | 121 k (environ 121 min) | clonage professionnel |
  | Pro | 99 $ | 600 k | — |

  Le TTS coûte 1 crédit par caractère. La page mentionne des promotions « Eleven v4 ». — [ElevenLabs pricing](https://elevenlabs.io/pricing)
- **Eleven v3** :
  - disponible en version générale ;
  - balises inline en minuscules entre crochets (émotions, direction, réactions comme `[laughs]`, `[clears throat]`, `[sighs]`) ;
  - le choix de la voix est « the most important parameter » ;
  - les prompts de plus de 250 caractères sont plus constants ;
  - endpoint « Create dialogue » (tableau de tours de parole avec `speaker_id`).

  — [ElevenLabs docs, prompting v3](https://elevenlabs.io/docs/best-practices/prompting) ; [blog audio tags](https://elevenlabs.io/blog/v3-audiotags). Exemple français de la page FR : « [chuchote] Quelque chose arrive… [soupire] Je le sens. » — [ElevenLabs FR](https://elevenlabs.io/fr/blog/v3-audiotags)
- **Qwen3-TTS contre ElevenLabs** (test en portugais, pas en français) : Qwen3 1.7B est « good enough to ship », mais monotone sur la durée. ElevenLabs reste devant sur la prosodie et les balises d'émotion, et va plus vite. — [AkitaOnRails, 2026-04-09](https://akitaonrails.com/en/2026/04/09/how-elevenlabs-was-not-killed-by-qwen3-tts)
- Un développeur qui clonait en **français** est passé de Qwen3-TTS à **Chatterbox**, car certaines requêtes Qwen3 renvoyaient un audio « garbled ». — [archy.net](https://archy.net/from-qwen3-tts-to-chatterbox-finally-getting-voice-cloning-right/)
- **Chatterbox Multilingual V3** (0,5B) : le français fait partie des 20+ langues, sans modèle français dédié. Un paramètre d'exagération règle l'émotion ; il n'y a pas de conception de voix par description. — [Resemble AI](https://resemble.ai/learn/models/chatterbox-multilingual)
- **[notes 10-06]** :
  - Qwen3-TTS : Apache-2.0, 10 langues dont le français, VoiceDesign puis clonage Base ;
  - Chatterbox : MIT, filigrane Perth ;
  - Pocket TTS : CPU, CC-BY-4.0, 27 voix françaises intégrées, environ 1,7× le temps réel sur 4 vCPU ;
  - RVC/Applio : MIT, environ 10 min de données, inférence CPU possible ;
  - lip-sync audio → vidéo ouvert pour un cartoon non humain : LongCat-Video-Avatar 1.5 (MIT, « anime, animals »), InfiniteTalk et Wan2.2-S2V (Apache-2.0), tous sur GPU.

  — [GitHub QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) ; [HF LongCat-Video-Avatar-1.5](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5)
- **[TEST LOCAL]** Agnes v2.0 : français exact sur B (sans aucune erreur), un mot déformé et un « me » en trop sur C et D, des « Hmm » ajoutés. Voix du croissant à 246, 198 et 208 Hz selon les clips (§2).

### Inferences
- **Banque de voix Orbeo** (une par personnage, figée) : créer chaque voix avec Qwen3-TTS VoiceDesign (libre) ou ElevenLabs Voice Design (payant), sans imiter personne. Générer 10 à 15 min de répliques variées avec cette voix et en faire **la cible d'un modèle RVC par personnage**. Le jeu de données est légalement propre : aucune voix réelle.
  - **Route A (aujourd'hui, gratuite, CPU)** : audio natif Agnes, puis séparation voix / ambiance (Demucs, testé le 10-06), puis RVC du personnage (conversion du stem voix), puis remixage. Le lip-sync reste celui du modèle, et le timbre devient constant. À tester.
  - **Route B (GPU)** : TTS du personnage (Qwen3-TTS clone ou Chatterbox, émotion par réplique), puis lip-sync audio → vidéo (LTX-2.5 audio-driven ou InfiniteTalk) sur l'image clé. Elle offre le contrôle total du texte et du timing comique, mais coûte une brique GPU de plus.
- **ElevenLabs** n'est pas indispensable. C'est le **meilleur repère de qualité** pour l'émotion comique en français, et le plan Creator (22 $/mois, environ 121 min) couvre largement 30 épisodes de 60 à 90 s, y compris les reprises (calcul au §7).
- Le rythme comique se règle **au montage**, plus que dans le modèle : couper les silences, ajouter des « beats » de réaction (gros plan muet de 0,5 à 1 s), des bruitages et des sous-titres qui « tombent » sur le mot drôle.

### Gaps
- Je n'ai trouvé aucun test d'écoute indépendant en **français** comparant Qwen3-TTS, Chatterbox et ElevenLabs.
- Le support officiel du français par Kling 3.x, Seedance 2.x et Veo 3.1 n'est pas confirmé.
- La conversion de voix RVC sur l'audio natif Agnes n'a pas été testée (pas de modèle RVC entraîné ; disque limité à environ 3,6 Go).

---

## 5. Automatisation du montage (ffmpeg, sous-titres, accroche, numérotation, carte de fin) et de la publication (Metricool, cadence, mentions IA)

### Takeaway
Le montage complet est **entièrement automatisable sur CPU** avec ffmpeg, libass et faster-whisper. C'est testé ici : environ 40 s de calcul pour 15 s de vidéo 1080×1920, avec sous-titres mot par mot calés sur le script, titre d'accroche, badge d'épisode, carte de fin et normalisation à −14 LUFS.

La publication passe par l'API ou le MCP Metricool. Les champs de déclaration IA existent pour les trois réseaux : TikTok `isAigc`, Instagram `isAiGenerated`, YouTube `isAiGeneratedContent`. La publication est automatique par défaut (`autoPublish: true`). La couverture se règle par `videoCoverMilliseconds` ou `videoThumbnailUrl`, mais seulement pour les comptes TikTok Business.

Depuis le 2 août 2026, l'article 50 de l'AI Act impose un étiquetage clair : cocher le drapeau natif **et** ajouter une mention dans la légende.

### Cited Findings
- **[TEST LOCAL]** `assemble_episode.py` (§2 C) :
  - durée de l'épisode test 15,1 s, temps total 39-43 s (user 1 min 31 s sur 4 vCPU), sortie 1080×1920 à 24 i/s, −13,5 LUFS intégrés ;
  - sous-titres ASS avec mot surligné (`\c` + `\fscx112`), 3 mots maximum, une réplique à la fois ;
  - alignement `difflib` entre le texte du script et les mots whisper : 18 sur 19 alignés, le dernier interpolé.
- Schéma de l'outil Metricool `createScheduledPost` (MCP connecté à cette session, lu le 2026-10-08) :
  - `autoPublish` (true = publication automatique par l'API) ;
  - `tiktokData.isAigc` : « declares that the video was generated or significantly edited by AI » ;
  - `tiktokData.autoAddMusic`, `privacyOption`, `title`, `disableDuet` et `disableStitch` ;
  - `instagramData.type` = REEL ou TRIAL_REEL, `isAiGenerated`, et `audioConfiguration` (musique du catalogue Instagram, comptes Business seulement) ;
  - `youtubeData.type` = short, `madeForKids`, `isAiGeneratedContent` ;
  - `videoCoverMilliseconds` et `videoThumbnailUrl` (pour TikTok, comptes Business seulement, ignorés sur un compte personnel) ;
  - `firstCommentText`.

  — schéma de l'outil MCP Metricool (voir aussi [Glama, Metricool MCP post_Schedule_Post](https://glama.ai/mcp/servers/@metricool/mcp-metricool/tools/post_Schedule_Post))
- Côté interface Metricool, les réglages « AI-generated content » existent pour Instagram, TikTok (vidéos, comptes personnels et Business) et YouTube (web seulement). L'article cite l'article 50 de l'AI Act, « enforceable since August 2, 2026 ». Il recommande une mention en début ou fin de légende, hors des hashtags, éventuellement avec les icônes UE. Le drapeau natif « does not by itself guarantee legal compliance ». — [Metricool Help, étiquetage IA](https://help.metricool.com/how-to-label-ai-generated-content-for-eu-ai-act-compliance-8a1j8)
- API REST Metricool : `POST /v2/scheduler/posts`, avec `userId` et `blogId` en paramètres et `X-Mc-Auth` en en-tête. — [Metricool Help, scheduler endpoint](https://help.metricool.com/wli-scheduler-endpoint-example-on-a-custom-backend-proxy-frko7)
- TikTok applique deux étiquettes : « creator labeled as AI-generated » (réglage, ou `is_aigc` de la Content Posting API) et une étiquette automatique « AI-generated » si le fichier porte des Content Credentials C2PA. L'étiquette automatique n'est pas supprimable. — [Adaptly](https://adaptlypost.com/blog/tiktok-ai-generated-label) **[agrégateur, non confirmé sur la page TikTok, rendue en JavaScript]**
- **YouTube** :
  - politique « inauthentic content » (renommée en juillet 2025) : le contenu « that looks like it's made with a template » ou répétitif n'est pas monétisable ; un format récurrent est accepté si « the substance of each video should be materially varied » ;
  - clarification de juillet 2026 : sont visés les vidéos génériques, le « même script re-rendu avec d'autres noms » et les personas IA présentés comme experts.

  — [Android Headlines, juillet 2026](https://www.androidheadlines.com/2026/07/youtube-monetization-rules-ai-slop-inauthentic-content.html) ; [YouTube Help, monétisation](https://support.google.com/youtube/answer/1311392)
- À partir du 1er février 2027, le partage de revenus des Shorts exigera **10 M de vues Shorts qualifiées sur 90 jours**. — [exchange4media](https://www.exchange4media.com/industry-briefing-news/youtube-sets-10-million-shorts-views-for-monetisation-from-2027-157245.html)
- **[notes 10-06]** YouTube : la déclaration IA vise le contenu **réaliste**. Une animation clairement irréaliste n'a pas à être signalée, mais il est prudent de cocher la case.

### Inferences
- **Gabarit d'épisode automatique** (tout en ffmpeg et ASS, à partir d'un JSON par épisode) :
  - **0-1,5 s** : accroche visuelle (gros plan sur une réplique choc) et titre-question en haut. L'épisode commence directement sur la parole : couper les silences et les « Hmm » de début.
  - Badge « ÉP. N · titre » permanent en haut à gauche, hors des zones de l'interface TikTok (barre droite et légende en bas).
  - Sous-titres mot par mot, en capitales, mot drôle surligné. Ils sont placés dans la bande où le modèle incruste ses pseudo-sous-titres (73-88 % de la hauteur) avec un flou ou une boîte opaque. Cette zone est souvent recouverte par la légende TikTok : à vérifier sur téléphone, sinon générer des plans plus serrés en haut et remonter les sous-titres vers environ 65-70 %.
  - Carte de fin de 1,5 à 2 s : cliffhanger écrit (« DEMAIN : … ») et numéro du prochain épisode. Fond : dernière image floutée.
  - Musique et bruitages : bibliothèque maison (ACE-Step 1.5 en MIT, d'après les [notes 10-06]) mixée sous les voix. Les sons tendance TikTok ne peuvent pas être ajoutés par l'API : `autoAddMusic` laisse TikTok choisir.
- **Cadence et publication** : un épisode par jour à heure fixe, choisie avec `getBestTimeToPostByNetwork` de Metricool. Publication sur TikTok, puis le même fichier en Reel et en Short. Drapeaux IA à `true` partout et mention « Série animée créée avec l'IA » dans la légende. Programmer à J+1 pour garder une marge de relecture humaine. Le mode `draft` ou la revue Metricool peut servir de point de validation.
- La règle YouTube sur le contenu « inauthentique » pèse plus lourd qu'une simple formalité : l'intrigue, les gags et le décor doivent **réellement varier** d'un épisode à l'autre, sans gabarit de script dont seuls les noms changent.

### Gaps
- Je n'ai pas lu la page officielle TikTok sur l'étiquetage IA (rendue en JavaScript) ni ses règles de récompenses créateurs pour le contenu IA.
- Je n'ai trouvé aucune donnée chiffrée sur les styles de sous-titres des meilleurs comptes (police, taille, position). Les choix ci-dessus suivent l'usage courant, sans source.
- Le comportement exact de `isAigc` avec un compte TikTok personnel connecté à Metricool n'a pas été testé : aucune publication réelle n'a été faite.

---

## 6. Quels outils payants sont vraiment irremplaçables, et quel budget mensuel minimum pour une série quotidienne de bonne qualité ?

### Takeaway
**Aucun outil payant n'est strictement irremplaçable pour cette ligne.** Le test prouve qu'Agnes v2.0 (gratuit) + ffmpeg + whisper produisent déjà un dialogue français à lip-sync correct en 9:16.

Le gratuit a deux faiblesses : la **fiabilité** (Agnes 2.5-flash saturé, aucune garantie de service) et le **contrôle de la voix**. Les briques payantes qui achètent le plus de qualité par euro sont :
1. **un modèle vidéo commercial de secours** (Kling 3.0 en abonnement, ou Veo 3.1 Fast/Lite à la seconde) ;
2. **ElevenLabs Creator** (22 $/mois) comme référence de voix ;
3. **quelques heures de GPU loué** (Vast ou RunPod à 0,2-0,5 $/h, ou les 30 $ gratuits de Modal) pour RVC, Qwen3-TTS, LTX-2.5 et les LoRA.

Budget minimum crédible :
- **0 à 30 €/mois** en mode Agnes + libre ;
- **environ 60 à 120 €/mois** avec un filet de sécurité (Kling Pro ou Premier, ou ElevenLabs Creator + GPU) ;
- **plus de 400 €/mois** si tout passe par Veo 3.1 Fast ou Seedance à l'API, rerolls compris.

### Cited Findings
- **Kling** (officiel, 2026-07-28) :

  | Plan | Prix par mois (première souscription) | Renouvellement | Crédits par mois |
  |---|---|---|---|
  | Basic | 0 $ | — | sans usage commercial |
  | Standard | 6,99 $ | 8,8 $ | 660 |
  | Pro | 25,99 $ | 32,56 $ | 3 000 |
  | Premier | 64,99 $ | 80,96 $ | 8 000 |
  | Ultra | 127,99 $ | 159,99 $ | 26 000 |

  Les crédits d'abonnement expirent à la fin de chaque cycle. — [Kling](https://kling.ai/blog/kling-video-3-0-credit-cost-guide)
- Coûts Kling par clip, selon Magic Hour : 5 s en Standard = 10 crédits ; 10 s en Pro = 70 crédits ; 10 s en Pro avec audio natif ≈ 80 crédits. — [StackSheriff](https://stacksheriff.com/ai-tools/kling-3-review/) **[agrégateur]**
- **Veo 3.1** (API Gemini, prix lus le 2026-09-11) :

  | Tier | 720p | 1080p | 4K |
  |---|---|---|---|
  | Standard | 0,40 $/s | 0,40 $/s | 0,60 $/s |
  | Fast | 0,10 $/s | 0,12 $/s | 0,30 $/s |
  | Lite | 0,05 $/s | 0,08 $/s | — |

  Pas de palier gratuit. — [BenchLM, d'après la page de tarifs Google](https://benchlm.ai/md/media-pricing/veo.md) **[agrégateur]**
- **Seedance 2.0** : les prix varient beaucoup selon le fournisseur :
  - environ 1 yuan/s (environ 0,14 $) chez Volcengine ;
  - environ 0,112 $/s (standard) dans le guide Atlas ;
  - 0,0113 $/s (Mini, 480p) dans le communiqué Atlas de septembre 2026 ;
  - environ 0,30 $/s en 720p avec audio chez fal.

  — [Atlas Cloud, coût par seconde](https://www.atlascloud.ai/blog/guides/seedance-2-cost-per-second) **[vendeur]** ; [communiqué Atlas, Daily Tribune](https://www.daily-tribune.com/online_features/press_releases/atlas-cloud-announces-the-lowest-seedance-2-0-api-prices-worldwide-starting-at-0-0113/article_14517629-a1bd-5455-963e-06b2ab34cea7.html)
- **Nano Banana** : environ 0,134 $ par image 1K (Pro) et environ 0,067 $ (Nano Banana 2). — [Laozhang](https://blog.laozhang.ai/en/posts/nano-banana-pro-face-consistency-guide) **[agrégateur]**
- **ElevenLabs** : Starter 6 $ (30 k crédits), Creator 22 $ (121 k crédits). — [ElevenLabs pricing](https://elevenlabs.io/pricing)
- **[notes 10-06]** GPU :
  - Vast.ai : RTX 3090 vérifiée à 0,16-0,21 $/h, RTX 4090 à 0,36-0,47 $/h ;
  - RunPod Community : 3090 à 0,22 $/h, 4090 à 0,34 $/h ;
  - Modal : 30 $ par mois de crédits gratuits.

  — [Modal pricing](https://modal.com/pricing) ; [RunPod pricing](https://www.runpod.io/pricing)
- Les créateurs de Skibidi Tentafruit annoncent « quelques dizaines d'euros par épisode ». — [75secondes](https://www.75secondes.fr/?p=182873). « Un abonnement de quelques dizaines d'euros par mois suffit » selon — [Blog-ia](https://blog-ia.com/skibidi-tentafruit-ia/)

### Inferences
Calculs de coût (mes hypothèses) : un épisode de 75 s, environ 75 s de vidéo utile, **un facteur de relance de 2,5** (le créateur de Fruit Love Island se plaint de devoir refaire ses plans), soit environ 190 s générées par épisode et 30 épisodes par mois.

| Option vidéo | Coût par épisode | Coût par mois (30 épisodes) | Commentaire |
|---|---|---|---|
| Agnes v2.0 | 0 € | 0 € | aucune garantie de service (gratuit, file partagée) |
| Veo 3.1 Lite 1080p (0,08 $/s) | environ 15 $ | environ 450 $ | français « English-centric » à tester |
| Veo 3.1 Fast 1080p (0,12 $/s) | environ 23 $ | environ 680 $ | idem |
| Veo 3.1 Standard (0,40 $/s) | environ 76 $ | environ 2 300 $ | idem |
| Kling 3.0 Pro avec audio (environ 8 crédits/s) | environ 1 500 crédits | environ 46 000 crédits | presque 2 abonnements Ultra (environ 260-320 $) ; en Standard sans audio (environ 2 crédits/s) + voix externe, environ 11 400 crédits, soit Premier + un complément |
| Seedance 2.0 (0,11-0,30 $/s) | environ 21-57 $ | environ 630-1 700 $ | prix très variables selon le fournisseur |
| GPU loué (LTX-2.5 ou Wan sur 4090 à environ 0,4 $/h) | hypothèse de 1 à 3 h par épisode : environ 0,4-1,2 $ | environ 12-36 $ | non mesuré |

- **Voix ElevenLabs** : environ 900 caractères de dialogue par épisode × 3 prises ≈ 2 700 crédits par épisode, soit environ 81 k par mois. Le plan **Creator à 22 $** suffit ; Starter (30 k) ne suffit pas.
- **Budget minimum « bonne qualité »** :
  - **Palier 0 (0 à 10 €/mois)** : Agnes v2.0, Pocket TTS ou voix natives, ffmpeg et whisper, Metricool (abonnement existant), LLM (déjà disponible via les agents).
  - **Palier 1 (environ 50 à 80 €/mois, recommandé)** : palier 0, plus Kling Pro ou Premier comme **filet de sécurité** quand Agnes échoue ou pour les plans d'action, plus environ 10 à 20 € de GPU (RVC, Qwen3-TTS, essais LTX-2.5, LoRA), plus ElevenLabs Starter ou Creator si les tests de voix libres déçoivent.
  - **Palier 2 (400 € ou plus par mois)** : tout en Veo 3.1 Fast ou Seedance par API. C'est injustifiable avant d'avoir une audience.
- **Rien n'est irremplaçable**, mais deux briques sont **difficiles à remplacer sans GPU** : un lip-sync piloté par l'audio (route B du §4) et une voix comique française de niveau ElevenLabs. Ces deux points se décident par un test d'écoute, pas par la documentation.

### Gaps
- Je n'ai pas vérifié en conditions réelles les crédits Kling consommés par seconde en mode Pro avec audio (chiffre d'agrégateur), ni les prix Seedance officiels pour l'Europe.
- Vitesse réelle de LTX-2.5 et de Wan sur un GPU loué : non mesurée, donc le coût GPU par épisode est une hypothèse.
- Je n'ai trouvé aucune donnée sur les revenus réels d'une série IA française à 60-90 s (les chiffres de Skibidi Tentafruit sont une estimation de magazine).

---

## 7. Plan de production : stack par étape, coût et temps par épisode, stack recommandée

### Takeaway
Stack recommandée, organisée en « fournisseurs » interchangeables pilotés par l'orchestrateur Python existant :
1. LLM (script + juge) ;
2. **Agnes image 2.5-flash** (images clés : scène + une identité) ;
3. **Agnes v2.0 image → vidéo** (plans de 5 à 10 s, un personnage par plan quand c'est possible, audio natif français) ;
4. contrôle whisper (texte attendu contre texte entendu) et juge visuel (espèce, nombre de personnages, texte parasite) ;
5. **ffmpeg + libass** (masquage des pseudo-sous-titres, sous-titres, accroche, carte de fin, −14 LUFS) ;
6. **Metricool** (`isAigc`, `isAiGenerated`, `isAiGeneratedContent` à true, programmation à J+1).

Améliorations par ordre de priorité :
- RVC par personnage, pour verrouiller les voix ;
- Kling Pro ou Premier comme fournisseur de secours ;
- GPU loué pour Qwen3-TTS, LTX-2.5 Ingredients et audio → vidéo, puis un LoRA par personnage.

Temps estimé : **environ 1 h à 1 h 30 de calcul** et **30 à 45 min de travail humain** par épisode de 75 s, contre 3 à 7 h pour les séries virales faites à la main.

### Cited Findings
Synthèse des sections 1 à 6 (sources dans chaque section). Colonnes dans l'ordre : qualité → coût → vitesse → automatisation → difficulté → licence → résultat réel.

| Étape | Ce qu'utilisent les créateurs en tête (payant) | Équivalent gratuit ou libre | Qualité | Coût | Vitesse | Automatisation | Difficulté | Licence | Résultat réel |
|---|---|---|---|---|---|---|---|---|---|
| Script | ChatGPT, Gemini (§1) | LLM des agents Orbeo + relecture humaine | bonne si bible et gags fournis | inclus | secondes | totale | faible | conditions du fournisseur | non testé ici (hors périmètre) |
| Design des personnages | Nano Banana 2 / Pro (§1, §3) | Agnes image 2.5-flash ; Qwen-Image-Edit-2511, FLUX.2 klein 4B | bonne (Agnes) | 0 $ / environ 0,07-0,13 $ par image (Nano Banana) | 12-24 s par image (Agnes) | API | faible | service tiers ; Apache-2.0 (Qwen, klein 4B) | **[TEST LOCAL]** 2/2 images propres ; inversion d'identité sans référence isolée |
| Images clés | idem | Agnes image (scène + une identité) | bonne | 0 | environ 20 s | API | faible | service tiers | **[TEST LOCAL]** 2/2 corrects avec le recadrage isolé |
| Animation | Veo 3.1, Kling 3.0, Seedance 2.x, Sora (fermé) (§1, §6) | Agnes v2.0 ; LTX-2.5, Wan 2.2 (GPU) | Agnes : bonne en gros plan, dérive en plan large | 0 / 0,05-0,40 $/s | 113-164 s par clip (Agnes) | API | faible à moyenne | service tiers ; LTX gratuit sous 10 M$, Wan Apache | **[TEST LOCAL]** 3/3 lip-sync attribué correctement ; 3/3 pseudo-sous-titres ; 2.5-flash : 0/1 |
| Voix | ElevenLabs, voix natives Veo/Kling (§1, §4) | Audio natif Agnes ; Qwen3-TTS, Chatterbox, Pocket TTS ; RVC | Agnes : français exact sur 1 clip, petites dérives sur 2 | 0 / 22 $/mois (Creator) | inclus dans le clip | totale | faible (native) à moyenne (RVC) | Apache, MIT, CC-BY | **[TEST LOCAL]** F0 du même personnage : 198-246 Hz selon le clip |
| Lip-sync | natif (Veo, Kling, Seedance), Hedra, Kling lip-sync | natif Agnes ; LTX-2.5 audio → vidéo, InfiniteTalk, LongCat-Avatar (GPU) | bonne (natif Agnes) | 0 | — | totale | faible (natif) / moyenne (GPU) | MIT, Apache, LTX | **[TEST LOCAL]** natif OK ; GPU non testé |
| Musique et bruitages | FL Studio, Suno, ElevenLabs (§1) | ambiance native ; ACE-Step 1.5 (MIT) | correcte | 0 | — | totale | faible | MIT | ambiance native présente ; ACE-Step testé le 10-06 |
| Montage | Final Cut, Premiere, CapCut (§1) | ffmpeg + libass + whisper | bonne (gabarit fixe) | 0 | environ 40 s de CPU pour 15 s | totale | moyenne (une fois) | LGPL/GPL (outils) | **[TEST LOCAL]** épisode test 1080×1920 propre |
| Sous-titres | CapCut auto-captions (inférence) | faster-whisper + ASS calé sur le script | bonne | 0 | inclus | totale | faible | MIT | **[TEST LOCAL]** 18/19 mots alignés, aucune erreur ASR affichée |
| Couverture | Nano Banana, CapCut (inférence) | image clé Agnes + texte ffmpeg ; `videoCoverMilliseconds` | correcte | 0 | secondes | totale | faible | — | non testé (couverture TikTok seulement en Business) |
| Publication | outils natifs, planificateurs | Metricool API/MCP | — | abonnement existant | — | totale | faible | — | schéma lu ; pas de publication réelle |

### Inferences
**Temps par épisode de 75 s** (estimation tirée des mesures du jour) :
- Script et découpage par le LLM : moins de 2 min de calcul, **10 à 15 min de relecture humaine** (gags, rythme).
- Images clés : 10 plans × 2 essais × environ 20 s, soit environ 7 min (en parallèle : environ 3 min).
- Clips Agnes v2.0 : 10 plans de 5 à 10 s × un facteur de 2 de relance × environ 140 s, soit environ 47 min en série, ou **environ 25 min avec 2 travaux en parallèle** (B et C ont tourné en parallèle sans erreur ; la limite de parallélisme n'est pas documentée).
- Contrôle whisper et juge visuel : environ 2 à 3 min de CPU.
- Montage automatique : environ 3 à 4 min de CPU (40 s pour 15 s mesurées).
- **Revue humaine** du rendu final : **10 à 20 min**, plus 5 min de programmation Metricool.
- **Total : environ 1 h à 1 h 30 de calcul, 30 à 45 min de travail humain.** Une série quotidienne reste donc tenable par une personne.

**Règles de production issues des tests** :
1. Un personnage par plan quand le dialogue compte (champ / contre-champ), avec des plans à deux en ouverture et pour les réactions.
2. Description textuelle figée par personnage, sans nom propre seul. Images clés en « scène + une identité ».
3. Prompt vidéo : « Locked-off static tripod shot… never zooms » ; une ou deux répliques courtes de 4 s au plus ; « no music ».
4. Masquage systématique de la bande à 73-88 % de la hauteur, et nos sous-titres par-dessus.
5. Contrôle whisper par réplique et relance au-delà d'environ 10 % d'erreur ; couper les « Hmm » de début.
6. Pipeline multi-fournisseurs : Agnes v2.0 en principal, Kling en secours payant, LTX-2.5 et Wan sur GPU en libre.

**Feuille de route** :
- **Semaine 1** : passer le gabarit `assemble_episode.py` en module d'épisode (JSON → mp4) et produire 3 épisodes pilotes de 60 à 90 s avec Agnes v2.0.
- **Semaine 2** : banque de voix (Qwen3-TTS VoiceDesign via GPU ou Space avec jeton) et un modèle RVC par personnage ; test de la route A sur 10 répliques.
- **Semaine 3** : compte Kling Pro et test du français natif de Kling 3.0 et de Veo 3.1 Lite sur les mêmes plans, jugés à l'oreille.
- **Plus tard** : LTX-2.5 Ingredients + audio → vidéo, et un LoRA par personnage.

### Gaps
- Le pipeline complet (10 plans, 75 s) n'a pas été exécuté de bout en bout : seuls 3 clips et un montage de 15 s l'ont été.
- Je n'ai pas de mesure de rétention ou d'audience pour ce format chez Orbeo. L'efficacité de l'accroche et des sous-titres doit être mesurée après publication (statistiques Metricool).
- Toutes les briques GPU (LTX-2.5, Wan, Qwen3-TTS, RVC, InfiniteTalk) restent à tester sur un GPU loué.
