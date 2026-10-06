# Lulu la Luciole : chaîne YouTube de comptines (état du projet)

## Identité
- Chaîne : **Lulu la Luciole** (à confirmer), identifiant visé `@LuluLaLuciole`
- Mascotte : Lulu, petite luciole (nœud rose, antennes à pompons, ventre lumineux) → `identite/lulu_reference.png`
- Photo de profil : `identite/photo_profil.png`
- Personnage récurrent : Nino, 4 ans, pyjama bleu à étoiles
- Public : 1 à 5 ans, français. Vidéos « conçues pour les enfants ».
- Fil rouge : les rituels du soir (ranger, peur du noir, dormir…), Lulu étant une petite lumière dans la nuit.

## Fabrication d'un épisode (`pipeline/`)
1. `episodes/<nn_nom>/paroles.txt` + `episode.json` (sections calées sur les paroles, image de fin et mouvement de
   chaque section, réglages de la chanson, règles et interdits de l'épisode, fiche YouTube)
2. `gen_song.py` : chanson avec ACE-Step 1.5 (open source) en local, 3 prises
   (`extend_song.py` pour prolonger une fin coupée)
3. `make_episode.py` : choix de la meilleure prise (lignes reconnues), image de référence, images clés validées
   par un juge visuel, plans enchaînés (chaque plan part de la dernière image du précédent), montage 1080p,
   miniature, `youtube.md`

```bash
bash chaine_lulu/pipeline/install.sh            # machine neuve : ACE-Step, faster-whisper, Agnes (~5 min)
cd chaine_lulu/episodes/02_peur_du_noir
~/ace-venv/bin/python ../../pipeline/gen_song.py paroles.txt chanson --duration 118 --bpm 84 --key "F major" \
  --takes 3 --caption "$(python3 -c "import json;print(json.load(open('episode.json'))['song']['caption'])")"
(cd ~/agnes-video-generator && ./start.sh &)     # demande AGNES_API_KEY
WHISPER_PYTHON=~/ace-venv/bin/python ~/agnes-video-generator/.venv/bin/python ../../pipeline/make_episode.py .
```

Réparer un épisode déjà monté : `make_episode.py ../01_rangement --redo 4,7` refait seulement ces plans et les
remet dans la vidéo existante (son inchangé ; chaque plan refait finit sur la dernière image de l'ancien, pour que
le plan suivant s'enchaîne sans coupure visible).

Juge visuel (image par image) : un seul garçon, une seule luciole, pas d'adulte ni de créature en plus, pas de
déformation, **pas de fusion** (Nino avec des ailes ou des antennes, jouet ou objet avec des ailes ou des
antennes), Lulu et Nino présents, état de la chambre (jouets, coffre, nounours), plus une question à part sur le
dos de Nino (petites ailes blanches). 5 images contrôlées par plan, prises sur la durée réelle du plan ; on garde
le meilleur essai. Le juge rate encore des défauts : toujours regarder la vidéo finale (planche d'images toutes
les 2 à 3 s) avant de publier.

Changement de pièce : `"cut": true` et un `start_frame` dans la section. Le plan commence alors par une coupe
franche sur sa propre image de début (un seul plan qui passe d'une pièce à l'autre fait apparaître deux Nino).

## Épisodes
| # | Titre | État |
|---|---|---|
| 01 | La chanson du rangement | terminé (1 min 52), plans 4 et 7 réparés ; **programmé le samedi 10 octobre à 10 h**, Short le lundi 12 à 18 h 30 |
| 02 | J'ai peur du noir (Lulu et la peur du noir) | **publié le 6 octobre** : https://www.youtube.com/watch?v=Xx02S1SSlD0 ; Short le jeudi 8 à 18 h 30 |
| 03 | La chanson des dents | terminé (1 min 52), plans 1 et 9 refaits ; **programmé le mercredi 14 octobre à 18 h 30**, Short le vendredi 16 à 18 h 30 |

### Épisode 01 : défauts trouvés au visionnage (réparés)
- Plan 4 (0:33 à 0:39) : Lulu disparaît et Nino a une aile de luciole dans le dos.
- Plan 7 (1:07 à 1:13) : le nounours a les antennes, les ailes et le ventre lumineux de Lulu.
- L'ancien juge ne posait pas ces questions ; c'est corrigé (il repère les 4 images fautives et laisse passer
  les saines). Réparation faite avec `--redo 4,7` : plan 4 du premier coup ; plan 7 après réécriture de son
  mouvement (« Lulu éclaire l'étagère, un nounours apparaît » faisait pousser des ailes au nounours, 4 essais sur
  4). Son identique à l'original, raccords identiques. Reste un détail : deux canards visibles un instant (0:36).
- Le « 24 % » de paroles reconnues de l'ancienne fiche était un chiffre périmé : le vrai score est d'environ 89 %.

### Épisode 02 : pourquoi la peur du noir
- vidIQ (France, octobre 2026) : « comptines pour enfants » 61 700 recherches/mois, « comptine bébé » 38 400,
  **« comptine pour dormir bébé » 37 500**.
- « Je ne peux pas dormir, Maman ! Chanson sur la peur du noir » (Miliki Family, 113 k abonnés) :
  26,6 M de vues en 9 mois. Little Angel : 20 M et 19 M de vues sur le même thème.
- Lulu est une lumière dans le noir : le thème est fait pour elle. Paroles originales, refrain à chanter avec
  Nino : « Lulu, Lulu, allume-toi ! ».
- Lulu est décrite comme une mascotte insecte (pas une petite fille avec des ailes) : dans l'épisode 01, elle
  ressemblait parfois à une fée humaine.

### Épisode 02 : fabrication
- Chanson : prise 3 (la seule qui chante « Lulu, Lulu, allume-toi ! » dans les 4 couplets), fin refaite avec
  `extend_song.py` en ne donnant que les paroles de l'outro (avec toutes les paroles, ACE-Step rechantait le
  refrain). ACE-Step a sauté « Bonne nuit manteau, bonne nuit rideau, bonne nuit coussin, fais dodo » 4 fois sur
  4 : ces lignes sont retirées des paroles affichées. 88 % des lignes reconnues, toutes chantées.
- Images : 9 images clés sur 10 validées du premier coup.
- Plans : « Nino et Lulu dansent ensemble » transformait Lulu en petite fille (ou ajoutait un 2e garçon) ;
  insister sur « minuscule » en faisait un point lumineux. Ce qui marche : Lulu « mascotte luciole avec ses grands
  yeux et son nœud rose » qui tourne autour de Nino à hauteur de son visage. Plan 8 : Lulu n'arrive qu'après
  quelques secondes (gardé). Son : -13,7 LUFS.

## Leçons pour les prochains épisodes
- Ne jamais écrire qu'un objet « apparaît » dans la lumière de Lulu (ép. 01 : le nounours prenait ses ailes) :
  c'est Nino qui prend l'objet, Lulu reste à côté.
- Ne pas faire « danser ensemble » Nino et Lulu : Lulu tourne autour de lui.
- Éviter les énumérations dans les paroles (« bonne nuit X, bonne nuit Y… ») : ACE-Step les saute.
- Ne rien lancer d'autre pendant la génération d'une chanson sans le fichier d'échange (`install.sh` le crée).
- Pas de miroir dans le décor : le reflet double les personnages (ép. 03).
- Nouveau décor : générer d'abord la pièce vide, puis y ajouter Nino et Lulu (partir d'une autre pièce la recopie,
  partir de Lulu seule la rend géante et fait disparaître Nino).
- Le juge vérifie aussi que Nino est bien à l'image.
- Ép. 03, plan 9 : salle de bain → chambre dans un seul plan = deux Nino (3 essais sur 3, dont un accepté par le
  juge). Réglé par une coupe franche (`cut`) sur une image de début dans la chambre de l'ép. 02.
- Ép. 03, plan 1 : l'image de début avait deux petites ailes blanches dans le dos de Nino, recopiées sur tout le
  plan ; le juge ne les voyait pas (0 sur 5). Une question à part sur le dos les trouve (5 sur 5, aucune fausse
  alerte sur 10 images saines), et elle passe maintenant sur toutes les images.
- Sans consigne, la caméra peut partir dans une autre pièce (ép. 03 : salle de bain beige avec toilettes) : écrire
  « caméra fixe, même pièce du début à la fin » quand la pièce ne doit pas changer.
- Agnes rend parfois un plan plus court que demandé (17 s pour 20) : le juge prend ses images sur la vraie durée.
- Paroles : chaque ligne restait 0,3 s de trop et s'empilait sur la suivante (ép. 01 et 02, de courts instants) ;
  corrigé à partir de l'ép. 03.
- Shorts : libass ne lit pas la police Fredoka « variable » et affichait DejaVu ; `install.sh` crée une Fredoka
  grasse fixe. Shorts 01 et 02 refaits et remplacés dans Metricool.

## Publication
- Chaîne : `UCShPnzacZLkyH4nHZmDZkSg` (marque Orbeo Studio, voir `orbeo_studio/README.md`), publiée via Metricool
  (marque `7251650`) ; les vidéos partent d'un lien direct GitHub (dépôt public), Metricool les recopie.
- Shorts : `pipeline/make_short.py` (1080x1920, paroles en gros), programmés comme Shorts « conçus pour les enfants ».
- Miniatures : YouTube les refuse tant que la chaîne n'est pas validée par téléphone (YouTube Studio → Paramètres →
  Chaîne → Éligibilité aux fonctionnalités). Ensuite, vidIQ peut les poser (`vidiq_update_video_thumbnail`).
- Fait par l'API le 6 octobre (`orbeo_studio/youtube_api.py`) : description, mots-clés, pays, langue, bannière,
  playlists « Les comptines du soir de Lulu » (`PLC0bDtupuIzE`, avec l'ép. 02) et « Les Shorts de Lulu »
  (`PLE18-JLtziPs`). À ajouter après publication : ép. 01 et les deux Shorts dans leur playlist.
- Reste à faire dans YouTube Studio : nom de la chaîne (l'API l'ignore), photo de profil, validation par téléphone
  (miniatures personnalisées).
- Les vidéos mises en ligne par l'API d'un projet non audité restent privées : on publie par Metricool.

## Connexions
- vidIQ : connecté et lié à la chaîne (compte orbeo.studio@gmail.com, plan gratuit 150 crédits/mois).
- Metricool : chaîne YouTube connectée (Instagram et TikTok pas encore).
- Agnes (images et vidéos) : la clé `AGNES_API_KEY` doit être ajoutée aux variables de l'environnement cloud.

## Prochaines étapes
- Publier l'épisode 01 (fiche dans `episodes/01_rangement/youtube.md`)
- Créer la chaîne YouTube et la lier à vidIQ et Metricool (statistiques, programmation des publications)
- Publier l'épisode 02 (fiche dans `episodes/02_peur_du_noir/youtube.md`)
- Bannière de chaîne, rythme de publication (2 vidéos / semaine + Shorts extraits des refrains)
