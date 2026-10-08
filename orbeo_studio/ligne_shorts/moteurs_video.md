# Les moteurs vidéo pour la série fruits : alternatives à Agnes (8 octobre 2026)

Agnes est lent : 2 à 4 minutes par clip, des files saturées, et du faux texte incrusté sur environ un clip sur deux.
Cette note rassemble :
- trois recherches (modèles open source ; services gratuits par API ; GPU gratuits ou peu chers) ;
- mes tests sur les images de l'épisode 1.

**Légende :**
- **[V]** : vérifié sur la page officielle ;
- **[T]** : testé ici ;
- **[R]** : rapporté par un tiers ;
- **[E]** : estimation.

## 1. Ce que j'ai testé [T]

Les mêmes plans de l'épisode 1 (Cerise, Citron), une réplique française de 3 s :

| Moteur | Où | Temps | Résultat |
|---|---|---|---|
| Agnes v2.0 (actuel) | API Agnes | 2 à 4 min par clip, plus l'attente | réplique juste ; faux sous-titres sur 10 clips de 5 s sur 17 ; voix de Citron trop aiguë (175 Hz) |
| **LTX-2.3** | Space officiel `Lightricks/LTX-2-3` (GPU gratuits Hugging Face) | **17 s** | réplique reconnue, avec un mot parasite ; Cerise fidèle ; aucun faux texte ; 576×1024 |
| **LTX-2 TURBO**, voix native | Space `alexnasa/ltx-2-TURBO` | 42 s | réplique exacte ; voix de Citron vraiment grave (125 Hz) ; 1152×2048 ; mais la veste de Citron a disparu (le juge le refuse) |
| **LTX-2 TURBO**, **notre fichier voix** | même Space, paramètre `audio_path` | 37 s | lèvres synchronisées sur notre audio, émotion juste, 1152×2048 |

**Ce qu'il faut retenir :**
- LTX fait le même travail qu'Agnes, 5 à 10 fois plus vite et sans faux texte.
- Avec notre propre fichier voix, on choisit les voix, et elles restent les mêmes d'un épisode à l'autre.
- `produire.py` essaie maintenant LTX-2.3, puis TURBO, puis Agnes en secours.

## 2. Les quotas qui décident [V]

**Hugging Face ZeroGPU** (huggingface.co/docs/hub/spaces-zerogpu) :

| Compte | GPU par jour |
|---|---|
| sans compte | 2 min |
| **gratuit** | **5 min** (3 ou 4 clips : mes 4 tests l'ont épuisé) |
| **PRO, 9 $/mois** | **40 min**, puis 1 $ les 10 min |

- Le Space LTX-2.3 réserve 75 s de GPU par appel.
- En PRO, cela fait au moins 30 clips par jour, et peut-être beaucoup plus si seul le temps réellement utilisé est décompté (environ 15 s par clip). À mesurer.

**Agnes** (wiki.agnes-ai.com) :
- **`agnes-video-v2.0` est officiellement retiré depuis le 25 septembre 2026.** Il marche encore, mais peut s'arrêter à tout moment.
- Une clé gratuite n'exécute réellement **qu'une vidéo par minute**. C'est pour cela qu'en lancer 3 en parallèle ne sert à rien.
- **Token Plan :**
  - 5 vidéos par minute et 500 s de vidéo par jour, sur `agnes-video-2.5-flash` [V] ;
  - environ 4 $ par mois [R].
- `agnes-video-2.5-flash` :
  - gratuit pour un temps limité ;
  - 720×1280, de 4 à 12 s ;
  - parole française : pas encore vérifiable. Mon test du 8 octobre a échoué après 3 essais en 284 s, file
    saturée [T], comme lors de mes essais précédents sur ce modèle.
- Plusieurs clés du même compte partagent la même réserve : en créer plusieurs ne sert à rien, et ce n'est pas permis.

**Modal** (modal.com/pricing) :
- 30 $ de calcul offerts chaque mois.
- On y installe soi-même LTX-2.3 ou LongCat [E] :
  - 30 clips en 6 à 12 min ;
  - 1,5 à 3,7 $ par épisode ;
  - soit 8 à 30 épisodes gratuits par mois.

**À écarter :**
- Kaggle : gratuit, mais 1 à 5 h par épisode.
- Colab gratuit : pas automatisable dans les règles.
- Google Veo, Runway, Luma, Kling, Pollinations, fal : pas de palier gratuit par API.
- Kling : pas de français dans sa voix native.

## 3. Les modèles open source qui comptent [V]

| Modèle | Ce qu'il fait | Licence |
|---|---|---|
| **LTX-2.3 / 2.5** (Lightricks) | image + texte → vidéo avec la voix ; ou image + **notre audio** → vidéo synchronisée (Spaces `linoyts/LTX-2-3-sync`, `multimodalart/ltx2-audio-to-video`, `alexnasa/ltx-2-TURBO`) | gratuite sous 10 M$ de chiffre d'affaires ; contenu à étiqueter IA |
| **LongCat-Video-Avatar 1.5** (Meituan, mai 2026) | image + notre audio → personnage qui parle ; annonce l'anime et les animaux ; Space officiel | **MIT** ; le Space demande le PRO (240 s réservées, 480 s de quota) |
| InfiniteTalk, SkyReels-V3-A2V | même principe | Apache-2.0 / commercial autorisé ; pas de Space utilisable |
| **Chatterbox Multilingual V3**, **VoxCPM2**, Qwen3-TTS | voix française clonée, une par personnage | MIT / Apache-2.0 |

**Exclus à cause de leur licence :**
- **MiniMax H3** et **HunyuanVideo / HunyuanVideo-Avatar** ne s'appliquent pas dans l'Union européenne, y compris pour les vidéos produites.
- XTTS-v2, F5-TTS, Fish S2 et Wav2Lip ne sont pas utilisables commercialement.

## 4. Recommandation

1. **Tout de suite, gratuit :**
   - LTX-2.3 d'abord (compte Hugging Face gratuit, 3 ou 4 clips par jour), Agnes ensuite.
   - Retester Agnes 2.5-flash plus tard. Il était saturé le 8 octobre, et il remplacera v2.0 quand celui-ci
     s'arrêtera, s'il parle français.
2. **Le meilleur rapport, 9 $/mois : Hugging Face PRO.**
   - 40 min de GPU par jour, soit un épisode en environ 15 à 20 minutes au lieu d'1 h 30 [E].
   - L'accès à LongCat-Avatar.
   - Aucun travail d'installation : c'est déjà branché.
3. **Ensuite, la voix choisie et constante :**
   1. une voix de référence par personnage (Chatterbox V3 ou VoxCPM2) ;
   2. chaque réplique dite par cette voix ;
   3. l'animation par LTX-2.3 en mode audio, ou par LongCat.
4. **Si le volume grandit** (plusieurs épisodes par jour) : installer LTX-2.3 sur Modal (30 $ de crédits par mois offerts). Compter une demi-journée de mise en place.

## 5. Ce que le propriétaire doit faire

- **Fait :** compte Hugging Face et jeton en lecture (`~/.hf_token`, hors du dépôt). À régénérer après les tests, car il est passé dans la conversation.
- **À décider :** Hugging Face PRO, à 9 $/mois.
- **En option :**
  - Token Plan Agnes, environ 4 $/mois ;
  - compte Modal, avec les secrets `MODAL_TOKEN_ID` et `MODAL_TOKEN_SECRET`.
- **À vérifier :** les conditions d'usage commercial d'Agnes. La page des conditions ne s'affiche qu'avec JavaScript ; elle n'a pas pu être lue.
