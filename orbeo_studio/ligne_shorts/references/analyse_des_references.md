# Ce que font les histoires IA qui percent : analyse de 4 vidéos (8 octobre 2026)

**Méthode :**
1. `outils/tiktok_fetch.py` télécharge la vidéo et ses chiffres (vues, likes, son, légende).
2. `outils/analyse_reference.py` produit :
   - une image par plan et les 3 premières secondes ;
   - la transcription minutée des voix (faster-whisper) ;
   - la musique reconnue (Shazam).

**Ce qui n'est pas dans ce dépôt public :** les vidéos et leurs transcriptions complètes, qui appartiennent à leurs
auteurs. Elles restent dans le dossier de travail de la session et se retéléchargent à partir des liens.

## Les 4 vidéos

| Vidéo | Vues | Likes | Durée | Plans | Parole | Musique |
|---|---|---|---|---|---|---|
| [@premierchapiitre, « Son kebab cachait un lourd secret », épisode 3](https://vm.tiktok.com/ZN8kWR8WF/) | 719 k | 54,7 k | 82 s | 44 (un toutes les 1,9 s) | 89 % du temps | « TREND DAS FRUTAS », Dj Rhamon Dm (+ « BONDE DO PP DA NORTE ») |
| [@patricktv07, « partie 1 #drame »](https://vm.tiktok.com/ZN8kWAwfj/) | 1,2 M | 84,6 k | 63 s | 16 (un toutes les 3,9 s) | 96 % | « TREND DAS FRUTAS » (+ « BONDE DO PP DA NORTE ») |
| [@dragonfruitsaga, « Partie 2, Dragono participe à un tournoi de force »](https://vm.tiktok.com/ZN8kWFh4F/) | 2,3 M | 186 k | 85 s | changement de cadre toutes les 3 à 4 s (le détecteur a raté des coupes, les fonds se ressemblent) | 69 % | son original |
| [@une.histoire.ia2, « Kiwi avait honte de fraise, partie 2 »](https://www.tiktok.com/@une.histoire.ia2/video/7682857082701352225) | 6,9 M | 1 M | 75 s | 13 | 99 % | « Камин » (Kamin), EMIN & JONY |

## Les ressorts communs

1. **La première réplique tombe à 0,0 ou 0,1 seconde, en plein conflit.** Pas d'introduction : on arrive au milieu
   d'une scène tendue. Exemples :
   - une insulte ;
   - un ordre crié (« Poussez plus vite ! ») ;
   - une image choc : un chariot rempli de rongeurs marqué « viande à kebab ».
2. **On parle tout le temps.** 69 à 99 % de la durée est couverte par des dialogues, entre 28 et 46 répliques en
   une minute et quart, et jamais plus de 2 à 4 secondes de silence.
3. **Un moteur émotionnel simple et fort**, toujours une injustice :
   - le pauvre gentil contre le riche odieux : le fils qui doit payer les médicaments de sa mère malade, face à un
     millionnaire capricieux ;
   - le petit contre le géant : Dragono contre Titano au tournoi ;
   - l'humiliation puis la revanche : Fraise moquée pour son corps, transformation, puis « Laisse-la briller » ;
   - un secret qui fait peur : la viande du kebab et le contrôle sanitaire.

   Le spectateur reste pour voir **la justice arriver**.
4. **Un méchant clair**, qui triche ou humilie (« Je vais tout faire pour te nuire ! »). Le public réagit dans les
   commentaires.
5. **Des enjeux chiffrés à l'écran** :
   - la fortune de chaque personnage affichée sur son front (« 20 000 € », « 10 000 000 000 € ») ;
   - les poids sur les barres (200, 300, 500 kg) ;
   - le score du tournoi (« Épreuves 2/5 »).

   On comprend la hiérarchie en une demi-seconde, sans le son.
6. **Un rebondissement toutes les 10 à 15 secondes :**
   - on saute directement aux 500 kg ;
   - le rival sabote le camion ;
   - l'ex revient avec des fleurs ;
   - le contrôleur ouvre le frigo.
7. **Une fin coupée en plein suspense**, et une série numérotée (« Partie 1, 2… », « Épisode 3 ») :
   - « Il y a un truc qui me bloque. J'arrive pas à avancer. »
   - « Le jeu commence maintenant ! »
   - une porte « condamnée »… « Ah bah plus maintenant ».
8. **Une musique de fond brésilienne (funk) commune au genre :** « TREND DAS FRUTAS » de Dj Rhamon Dm, souvent
   mélangée à « BONDE DO PP DA NORTE ». C'est le son « des fruits IA ».
9. **Les sous-titres** : petits, mot à mot, au centre ou en bas, souvent un seul mot à la fois.
10. **L'image** : couleurs saturées, décors riches (palais doré, colisée, cuisine de kebab), personnages très typés
    (le gros riche, le musclé, le gringalet), gros plans d'émotion. Le style va du 3D façon Pixar au quasi
    photoréaliste.
11. **Les comptes gagnent de l'argent autrement :** la vidéo du kebab contient une **publicité intégrée** pour un
    outil de vidéos IA (TrendStory.io, « crée des vidéos IA virales en 5 minutes »), au milieu et à la fin. Des
    outils payants vendent déjà ce format clés en main.

## Ce que notre essai de la boulangerie n'avait pas (et pourquoi il était mauvais)

| Les vidéos qui percent | L'essai de la boulangerie |
|---|---|
| 60 à 85 s, 28 à 46 répliques | 15 s, 2 répliques |
| un conflit dès 0,0 s, une injustice, un méchant | une petite remarque sans enjeu |
| un rebondissement toutes les 10 à 15 s, une fin en suspense | aucune histoire |
| des enjeux chiffrés à l'écran | rien |
| un nouveau plan toutes les 2 à 4 s | 3 plans |
| la musique du genre, sans arrêt | pas de musique |

C'était un test technique (est-ce qu'Agnes sait faire parler deux personnages en français ?), pas une
proposition créative. La réponse technique est oui. L'histoire, elle, est entièrement à construire sur ces
ressorts.

## Ce que ça change pour la ligne ado-adulte

- Le concept « Les Crache-Pluie » (comédie calme en faux documentaire) ne colle pas à ces mécaniques : peu de
  conflit, rythme lent. Il faut le revoir ou le remplacer par un format de **mélodrame à épisodes** (injustice,
  méchant, revanche, suspense), en gardant ce qui fait une marque à nous : une troupe fixe, un univers reconnaissable
  et des noms déposables.
- **Musique :** la publication automatique par Metricool ne peut pas ajouter un son TikTok (sauf les 100 titres
  commerciaux les plus utilisés), et une musique protégée intégrée au fichier peut être coupée. **Solution :**
  Metricool envoie la vidéo en notification (publication manuelle), et le propriétaire ajoute le son tendance dans
  l'application TikTok avant de publier. C'est 30 secondes par vidéo.
- **Prochaine étape :** analyser 15 à 20 vidéos de plus (celles qui plaisent au propriétaire, et quelques-unes qui
  ne marchent pas), en tirer une « formule » seconde par seconde, puis fabriquer **un épisode d'essai au niveau de
  ces vidéos** avant de valider un concept.
