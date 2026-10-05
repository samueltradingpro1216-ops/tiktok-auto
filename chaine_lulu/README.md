# Lulu la Luciole : chaîne YouTube de comptines (état du projet)

## Identité
- Chaîne : **Lulu la Luciole** (à confirmer), identifiant visé `@LuluLaLuciole`
- Mascotte : Lulu, petite luciole (nœud rose, antennes à pompons, ventre lumineux) → `identite/lulu_reference.png`
- Photo de profil : `identite/photo_profil.png`
- Personnage récurrent : Nino, 4 ans, pyjama bleu à étoiles
- Public : 1 à 5 ans, français. Vidéos « conçues pour les enfants ».

## Fabrication d'un épisode (`pipeline/`)
1. `episodes/<nn_nom>/paroles.txt` + `episode.json` (sections calées sur les paroles, image de fin et mouvement de
   chaque section, état de la chambre, fiche YouTube)
2. `gen_song.py` : chanson avec ACE-Step 1.5 (open source, Apache 2.0) en local, 3 prises
   (`extend_song.py` pour prolonger une fin coupée)
3. `make_episode.py` : choix de la meilleure prise (lignes reconnues), images clés validées par un juge visuel,
   plans enchaînés (chaque plan part de la dernière image du précédent), montage 1080p, miniature, `youtube.md`

Prérequis : agnes-video-generator lancé (clé `AGNES_API_KEY`), ACE-Step installé dans `~/acestep`
(modèles `checkpoints/`), faster-whisper (`WHISPER_PYTHON`), ffmpeg.

## Épisodes
| # | Titre | État |
|---|---|---|
| 01 | La chanson du rangement | terminé (1 min 52), à publier |

## Prochaines étapes
- Connecter YouTube à Claude (vidIQ et/ou Metricool, plans gratuits) pour la recherche de mots-clés,
  les statistiques et la programmation des publications
- Bannière de chaîne, épisode 02, rythme de publication (2 vidéos / semaine + Shorts extraits des refrains)
