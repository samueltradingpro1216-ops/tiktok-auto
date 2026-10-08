# « Rue des Fruits » (titre de travail) : mélodrame à épisodes pour TikTok, Reels et Shorts

Série ado-adulte d'Orbeo Studio, construite sur la formule tirée de 22 vidéos de référence
(`../references/formule.md`). Elle remplace la proposition « Les Crache-Pluie ».

## Le concept
- **Une bande fixe d'un même quartier**, qui revient d'un épisode à l'autre : c'est ce qui marche le mieux dans les
  références (Dragono, « Les flockos de Paname », « Kiwi et Fraise »).
- **Des arcs de 3 à 5 parties** sur un moteur fort (la tromperie, le père indigne, le riche déguisé, la revanche de
  l'humiliée), puis une nouvelle histoire avec les mêmes personnages.
- **Des histoires très françaises :** le quartier, la famille, l'argent qui manque, le travail.
- **Chaque épisode** dure 72 à 80 s, avec une première réplique à 0,0 s, un rebondissement vers 25 à 35 s, une
  escalade toutes les 10 s environ et une fin coupée net (« PARTIE 2 »).

## La troupe

| Personnage | Rôle | Caractère | Voix (consigne) |
|---|---|---|---|
| **Cerise** | l'héroïne, 20 ans, serveuse dans un café du quartier | gentille, un peu naïve, puis déterminée ; on s'attache à elle | jeune femme douce, légèrement voilée, qui tremble quand elle a mal et se raffermit quand elle se relève |
| **Citron** | son copain | menteur, frimeur, méprisant ; le méchant clair | jeune homme, voix grave et posée, sûr de lui, arrogant |
| **Pêche** | la meilleure amie de Cerise, influenceuse | jalouse, moqueuse, vit pour ses abonnés | jeune femme, voix aiguë, traînante, moqueuse |
| **Kiwi** | ami d'enfance de Cerise, livreur en scooter | drôle, loyal, amoureux de Cerise en secret | jeune homme chaleureux, léger accent de quartier |
| **Mamie Prune** | la grand-mère de Cerise | sage, piquante, répliques cash ; le public la cite | vieille dame, voix cassée, chaleureuse et malicieuse |

**Personnages de réserve :** Papi Figue (le grand-père riche), la famille Ananas (les voisins snobs), Banane (le
notaire en lunettes).

## Le style visuel
- 3D façon film d'animation, lumière de cinéma, décors riches et très éclairés.
- **Des corps humains, la peau et la couleur du fruit**, une petite feuille ou une queue de fruit dans les cheveux,
  un détail du fruit sur la tenue. C'est le style de « Kiwi et Fraise » (6,9 M de vues).
- **Le physique** est extravagant, comme chez la concurrence. Niveau demandé par le propriétaire le 8 octobre :
  « 6 sur 10 » en sexy.
  - **Femmes :**
    - silhouette en sablier très marquée (poitrine, taille fine, hanches, fesses) ;
    - lèvres pulpeuses et maquillage glamour ;
    - tenues moulantes avec décolleté plongeant ;
    - poses de mannequin (main sur la hanche, hanche déhanchée).
  - **Hommes :** carrure de bodybuilder (épaules, pectoraux, abdos visibles), torse nu sous la veste ouverte,
    mâchoire sculptée.
  - **Limites gardées :**
    - toujours habillés : pas de lingerie, de body ni de maillot, pas de nudité ;
    - pas de pose explicite, et pas de caméra qui s'attarde sur une partie du corps ;
    - des visages clairement adultes (25 à 30 ans).

    Le public compte beaucoup de mineurs. TikTok peut retirer du fil « Pour toi » ce qu'il juge suggestif, et les
    marques s'en éloignent. À surveiller sur les premières vidéos.
- **Fiches d'identité** (`identite/`, troupe complète dans `identite/troupe.jpg`) :
  - une image de référence validée par personnage et par tenue, réutilisée à chaque plan ;
  - premier jet par `outils/identites.py`, puis retouches par l'image. Le générateur efface souvent la couleur de
    fruit quand on retouche la tenue : on la remet ensuite par une retouche « couleur de peau seulement ».

## Les règles de fabrication (apprises sur les essais)
- **Image clé de chaque plan :** le décor d'abord, puis **un seul personnage ajouté par passe**, avec sa fiche
  d'identité comme référence. À deux personnages dans une même passe, ils se mélangent.
- **Les personnages sont décrits par leur apparence** dans les consignes, jamais par leur nom seul.
- **Un plan = une réplique = un personnage qui parle**, en gros plan ou plan moyen, caméra fixe. Agnes v2.0 dit la
  réplique en français et fait bouger les lèvres du seul personnage qui parle.
- **Une voix constante :** chaque réplique est convertie vers la voix de référence du personnage (`outils/voix.py`,
  OpenVoice). Le rythme est gardé, donc le mouvement des lèvres reste juste. La ressemblance entre clips est mesurée
  (Resemblyzer, au moins 0,85 visé).
- **Contrôle :** chaque clip est retranscrit (whisper) et comparé au script ; les images sont vérifiées (bon
  personnage, une seule copie, pas de texte parasite). Un clip raté est refait.
- **Au montage :**
  - la bande de faux sous-titres d'Agnes est masquée ;
  - nos sous-titres sont mot à mot ;
  - l'accroche est affichée en haut pendant 3 s, avec un badge « ÉP. 1 » ;
  - les messages, publications et montants sont incrustés en gros ;
  - « PARTIE 2 » s'affiche sur fond noir à la fin.

## La musique
- Une **musique originale par épisode**, découpée en ambiances qui suivent l'histoire : tension, chute triste,
  chaleur, montée de la revanche, fête, coupure. Les changements tombent sur les coupes du montage.
- **Deux fichiers sont livrés :**
  - la version complète (voix, musique, bruitages) pour Reels, Shorts et TikTok ;
  - une version sans musique, pour ajouter dans l'application un son tendance (« TREND DAS FRUTAS », « Камин »)
    quand on veut suivre la mode.
- La musique est générée par IA : elle doit être déclarée sur YouTube.

## Les épisodes
| N° | Titre | Moteur | Statut |
|---|---|---|---|
| 1 | « La bague » (partie 1) | la tromperie, puis la revanche | en fabrication, épisode d'essai |
