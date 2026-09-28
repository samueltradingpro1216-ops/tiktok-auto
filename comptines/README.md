# Comptines islamiques animées : pipeline automatique

Transforme un **script de comptine** (`specs/*.json`) en **vidéo YouTube 1080p chantée**, avec paroles en
sous-titres, miniature et fiche YouTube, en validant automatiquement la qualité.

## Comment une comptine est créée

1. **Recherche d'inspiration** (YouTube) : on cherche des comptines très vues mais peu copiées en français,
   on récupère leurs captures (planches d'images YouTube) et leurs paroles, puis on écrit une **nouvelle**
   comptine (nouvelle histoire, nouvelles paroles) inspirée du thème. Les infos sont gardées dans
   `inspiration` de la spec.
2. **Script** (`specs/<nom>.json`) : personnages (apparence fixe), style, musique, et scène par scène
   (10 s chacune) : image de départ, action, paroles chantées et qui chante.
3. **Pipeline** (`pipeline/comptine.py`) :

| Étape | Ce qui est fait | Critère de validation |
|---|---|---|
| review | contrôle anti-copie (aucune suite de 5 mots identique aux paroles d'origine) + note par un LLM | aucune copie, toutes les notes ≥ 7/10 (cohérence, attrait enfants, simplicité, justesse islamique, valeur éducative) |
| scenes | image de référence, image de départ de chaque scène, clip chanté de 10 s (Agnes Video 2.0, son natif + lèvres synchronisées) | image : juge visuel (nombre de personnages, hijab, pas de texte) ; clip : chant transcrit (Whisper) ≥ 55 % identique aux paroles, son ≥ -40 dB, juge visuel sur 3 images |
| (auto) | scène rejetée → régénérée (nouvelle graine, nouvelle image si problème de personnages), jusqu'à 3 essais | |
| assemble | montage 1920×1080, fondus audio, volume -14 LUFS (standard YouTube), paroles incrustées calées sur le chant | |
| publish | miniature 1280×720 + `youtube.md` (titre, description avec chapitres et paroles, tags, réglages, rapport qualité) | |

Chaque étape reprend là où elle s'est arrêtée (`output/<slug>/state.json`).

## Lancer

Prérequis : [agnes-video-generator](https://github.com/lcy362/agnes-video-generator) lancé
(`./start.sh`, clé `AGNES_API_KEY`), ffmpeg, et un venv avec `faster-whisper`.

```bash
export AGNES_API_KEY="ta-cle"
export AGNES_DIR=~/agnes-video-generator
export WHISPER_PYTHON=~/whisper-venv/bin/python
~/agnes-video-generator/.venv/bin/python pipeline/comptine.py specs/mon_coran.json
```

Résultats dans `output/<slug>/` : `<slug>_youtube.mp4` (à publier), `<slug>_apercu.mp4` (léger),
`miniature_youtube.jpg`, `youtube.md`, `paroles.srt`, `scenes/`.

## Règles de contenu

- Pas de récitation du Coran générée par IA (risque d'erreur sur un texte sacré) : paroles en français,
  formules courtes seulement (Bismillah, SubhanAllah, MashaAllah, Allahu Akbar, Alhamdulillah).
- Aucune représentation de prophète.
- Les femmes portent toujours le hijab.
- Paroles originales : on s'inspire d'un thème, jamais des paroles d'une autre chaîne.
