# Épisode 2 · « La métamorphose », partie 1 · Maxi-prompt de production

*Le réalisateur, 15 octobre 2026 · **v3**, après la deuxième relecture du chef (la v2 avait recalé le minutage sur
nos voix réelles, le tempo à 0,90, le P21 sur les quais, l'image clé propre au P28, « cent jours » et le badge sans
numéro). Ce document sert aux générateurs d'images, de vidéos et de voix, puis au montage. Il suit plan par plan le
script v3 (`script.md`) et n'en change aucune réplique.*

**Ce qui change en v3.**
- **Le bouquet du P17 a son bloc figé** (roses jaunes, papier kraft brun) dans `cadre`, l'image, la vidéo et la
  variante.
- **Coco est redessiné sans trait caricatural** : peau brun clair chaud à bourre de coco, touffe de fibres sèches
  sur le crâne, sourire en coin ; plus de grandes dents blanches ni de crâne rasé. « Oh, Citron ! » remplace « Wesh ».
- **Le P1 cible a la bande en amorce** (4 essais) ; le P1 sans amorce devient le repli (`repli_sans_amorce`).
- **L'écart avant / après se renforce** : stylo, carnet et épaules voûtées aux P1, P4, P6, P8 ; lunettes de soleil
  dorées, ondulations glamour et petit sac rouge cerise au retour (P22, P25).
- **Le trou de la métamorphose est rempli** : « Quoi ?! » hors champ de Myrtille au P23, murmures de foule au P22.
- **Le carton du P22 monte dans le tiers haut** ; la coupe de secours du P22 passe en dernier.
- **Répliques :** P9 « Sans moi, Cerise ? », P10 « je t'affiche partout », P29 « Lâche l'affaire. Il te reste que
  le zeste. ».
- **Cadrages et regards :** Mamie assise, qui remue son thé, en plan rapproché taille (P12) ; Myrtille regarde
  Citron (P29) ; regard caméra écrit au P30 ; plus de buée à l'aube (P19, P20) ; fenêtre gardée du P21 précisée.
- **L'annexe dit que `make_image` et `reframe` composent l'image avec `cadre`**, pas avec `prompts.image`.

**L'épisode en une ligne.** Devant ses potes de salle, Citron renie Cerise : « juste la serveuse ». Elle le quitte,
revient cent jours plus tard, rayonnante, et c'est lui qui a honte. Le public, lui, sait déjà ce qu'elle ignore :
Citron vit de ses pourboires.

| Repère | Valeur |
|---|---|
| Durée | **78,6 s estimés** : 30 plans de 1,2 à 5,0 s, plus 1,2 s de carte de fin. Estimation au débit de référence ; la durée réelle se fixe sur les voix mesurées (voir « Le minutage », plus bas) |
| Plans | 26 avec voix : 23 parlés à l'image, plus 3 voix hors champ (P1 Coco, P21 Kiwi, P23 Myrtille, sur la réaction n° 3) ; 4 entièrement muets : 2 réactions (P4, P16), la course (P20) et le défilé (P22) |
| Répliques | 56 phrases courtes en 26 prises de parole ; **181 mots**, 9 au plus par réplique (10 au P15 et au P28, 11 pour Mamie au P12) ; 2,3 mots/s sur l'ensemble |
| Accroche | **IL L'A RENIÉE DEVANT SES POTES 💔** (en haut, de 0 à 3 s) |
| Badge | **LA MÉTAMORPHOSE · PARTIE 1** (le numéro d'épisode reste interne) |
| Légende | Cerise, « juste la serveuse » ? 🍒 Partie 1 #fruitstory #histoiredefruit #tiktokfrance🇨🇵 #brainrot #france |
| Fin | **PARTIE 2**, sur fond noir |
| Fichier machine | `episode.json`, même format que l'ép. 1, prompts complets compris |

**Comment s'en servir.**
1. **La bible (§ B) et les décors (§ C)** donnent les blocs fixes. Ils se collent tels quels, au mot près : un mot
   ajouté suffit à changer un personnage.
2. **Le plan par plan (§ D)** donne, pour chacun des 30 plans, la fiche de tournage, puis quatre textes prêts à
   coller :
   - le prompt d'image clé ;
   - le prompt vidéo ;
   - la variante « animée sur notre voix » ;
   - le champ négatif.
3. **Le montage (§ E) et la liste de contrôle (§ F)** ferment la boucle avant publication.
4. **Les prompts sont en anglais, sauf les répliques**, qui restent en français entre guillemets. Les prénoms ne
   servent qu'à l'équipe : dans les prompts, chaque personnage est décrit par son apparence.

**Le minutage (correction du chef, bloquante).**
- **La durée d'un plan parlé est celle de sa voix.** `montage.py` coupe chaque plan parlé 0,10 s avant le premier
  mot et 0,28 s après le dernier : c'est la voix réelle qui fait la durée, pas le champ `duree`.
- **Les voix se font donc avant les clips** (Annexe, étape 5). On mesure chaque voix, puis `duree` = parole
  mesurée + 0,4 s, et seulement ensuite on génère les clips à cette durée.
- **Les durées de ce document sont des estimations** au débit de référence : celui que le chef a mesuré sur nos
  voix clonées de l'ép. 1 (tempo 0,85 : Cerise 3,1 ; Citron 2,85 ; Kiwi 3,5 ; Mamie 2,0 mots/s), porté au tempo
  0,90 (Cerise 3,3 ; Citron, Coco et Myrtille 3,0 ; Kiwi 3,7 mots/s), avec Mamie à 5,0 s imposées. Résultat :
  **78,9 s** (78,6 s en durées arrondies au dixième).
- **Estimation prudente : 83,6 s.** Recomptés en mots du script (la même unité que le budget de 185 mots) sur les
  mêmes fichiers de l'ép. 1, nos voix parlent un peu moins vite : Cerise 2,95 ; Citron 2,7 ; Kiwi 3,1 mots/s au
  tempo 0,85, soit Cerise 3,1 ; Citron 2,8 ; Kiwi 3,25 au tempo 0,90. Si la mesure dépasse 80 s,
  on applique les **coupes de secours**, déjà écrites et classées (`episode.json` → `minutage`, et script § 6.1) :
  elles ramènent l'estimation prudente à 79,0 s.

**Les décisions du réalisateur** (v2 : les n° 2, 3, 9 et 10 sont celles du chef) :
1. **La voix hors champ du P1 est gardée.** C'est la version cible, avec la moquerie à 0,0 s sur le visage de
   Cerise. Le repli est écrit et prêt : P1 muet de 1,5 s, plus un plan de Coco (§ D, fin), pour 80,1 s estimés.
2. **Le tempo des voix est de 0,90 au plus** (décision du chef, qui annule le 0,95 proposé en v1), Mamie
   inchangée à 1,25, pauses de 0,15 à 0,25 s. Le propriétaire a demandé des voix plus lentes à l'ép. 1 v4 : le
   rythme se gagne en coupant du texte, pas en accélérant les voix.
3. **Le badge est « LA MÉTAMORPHOSE · PARTIE 1 ».** Le numéro d'épisode reste interne : un numéro à l'écran,
   « Partie 1 » dans la légende et « PARTIE 2 » à la fin, c'était confus pour qui arrive par « Pour toi ».
4. **Les blocs d'apparence** reprennent mot pour mot les blocs de l'ép. 1, plus un complément figé, l'âge adulte.
   Chaque bloc fait ainsi 40 à 70 mots, et la règle des visages adultes est écrite dans chaque prompt.
5. **Le style vidéo** est le style d'image de l'ép. 1, où seul « movie still » devient « film ».
6. **Le pot à pourboires est peint dans le décor du salon** : on retouche `appart.png` de l'ép. 1. On ne le demande
   pas dans la passe du personnage. C'est ainsi le même pot, net, au P9 et au P10.
7. **Kiwi en tenue chic garde sa veste verte de livreur sur l'épaule.** C'est son accessoire signature, et c'est ce
   qui rend lisible le « Le livreur ?! » de Citron.
8. **Les gestes après la dernière réplique ne sont pas demandés aux moteurs.** Le montage ne garde que 0,3 s après
   le dernier mot. Les coups à la porte et la porte qui claque se racontent donc par le son.
9. **Le texte a été coupé, pas accéléré** : 221 mots en v1, 182 en v2, 181 en v3 (voix hors champ comprises).
   Aucune réplique ne dépasse 9 mots, sauf deux de 10 mots, l'étendard (P15) et la menace (P28), et Mamie (P12 : 11 mots en 5,0 s).
10. **P27 et P28 ont chacun leur image clé.** Le P27 regarde et pointe vers la gauche en plan rapproché ; le P28
    regarde la caméra en gros plan, index vers l'objectif. L'option « une seule génération » est abandonnée.
11. **La musique de la version complète reprend les prises de l'ép. 1** (`tension` 3, `triste` 1, `revanche` 3) :
    même identité sonore, et aucune génération à refaire.
12. **v3 : le P1 cible montre la bande en amorce** (décision du chef). 12 accroches sur 13 du corpus montrent les
    oppresseurs ; sans eux, la serveuse souriante ne dit pas l'injustice sans le son.
13. **v3 : le fruit de Coco se lit par la matière, jamais par des traits de visage.** Aucune dent ni lèvre
    surlignée sur le seul personnage à peau brune : le public compte beaucoup de mineurs.
14. **v3 : les blocs de l'ép. 1 ne bougent pas.** L'« avant » se renforce dans la partie variable (P1, P4, P6,
    P8) ; l'« après », dans le bloc `cerise_glow`, propre à l'ép. 2. En gros plan, le carnet est hors cadre : les
    prompts vidéo de P4, P6 et P8 ne gardent que le stylo et les épaules, pour rester sous 180 mots.
15. **v3 : toute correction d'image se fait dans `cadre`.** C'est lui que `make_image` et `reframe` envoient
    (annexe).

## A. Intention et ton

**La promesse.** En 80 secondes, une injustice qui se lit sans le son, une femme qui se relève sans crier, une
revanche servie dans l'épisode, puis une menace qui rouvre tout. On sort avec l'envie de voir la partie 2 et de
citer Mamie.

**Le ton.**
- **Un mélodrame de quartier, joué au premier degré.** Les émotions sont vraies : la honte, la dignité, la fierté.
  Le second degré vient des fruits : le citron réduit à son zeste, la cerise qui mûrit au soleil.
- **Le méchant est clair et puni à l'écran.** Il a honte du métier de Cerise. Il ne se moque jamais de son corps.
- **Cerise ne gagne pas par la beauté, mais par la tenue** : celle qu'elle porte et celle qu'elle a. Sa silhouette
  reste la même du premier au dernier plan. Seuls changent le style, la posture, la lumière et le regard.
- **La caméra reste près des visages.** Gros plans et plans rapprochés, un seul personnage par plan, des regards
  hors champ qui se répondent.

**Ce que le spectateur doit ressentir, seconde par seconde.**

| Temps (s) | Plans | Ce qu'il voit et entend | Ce qu'il doit ressentir | Le levier |
|---|---|---|---|---|
| 0,0–2,4 | P1 | Une serveuse pleine d'espoir tend une gamelle cerise au milieu des bodybuilders. Une voix la raille. | Un malaise immédiat. Elle est touchante, et on se moque d'elle avant qu'elle ait dit un mot. | L'injustice se lit sans le son : la bande floue en amorce, de dos, rit au premier plan (version cible) ; accroche en haut ; rires de la bande. |
| 2,4–5,4 | P2 | Son copain la renie : « juste la serveuse du café ». | L'indignation : « il a osé ». | Réplique choc, zoom lent sur le méprisant. |
| 5,4–8,1 | P3 | Un pote en rajoute. | La colère contre la meute. | Rires, doigt pointé. |
| 8,1–9,6 | P4 | Le sourire de Cerise se brise, en silence. | Un pincement : on veut la protéger. | Le silence, après trois répliques. |
| 9,6–12,3 | P5 | Le copain, mielleux, lui demande d'enlever son tablier. | Le dégoût : il a honte d'elle. | L'hypocrisie à voix basse. |
| 12,3–15,1 | P6 | Elle retourne son mot contre lui et le quitte. | Un premier soulagement, de la fierté. | La musique se coupe net : impact. |
| 15,1–17,5 | P7 | Il lui demande de parler moins fort : tout le monde regarde. | Le mépris : il n'a pensé qu'à son image. | Sourire figé, regards fuyants. |
| 17,5–20,3 | P8 | « Cent jours. Je reviens ici… et t'auras honte. » | Une promesse à voir tenue : on a rendez-vous. | **100 JOURS** à l'écran : c'est le minuteur de l'épisode. |
| 20,3–25,7 | P9, P10 | Seul chez lui : « Sans moi, Cerise ? Tu tiendras pas une semaine ! », et pour commencer, il va l'afficher partout. | De l'aversion, et l'avance de l'œil attentif sur ce pot cerise plein de billets. | L'aparté face caméra ; l'indice net, sans un mot. |
| 25,7–28,5 | P11 | 48 000 vues pour la vidéo moqueuse : la menace est déjà tenue. Elle doute. | De la compassion : l'humiliation est devenue publique. | Notification et chiffre ; piano. |
| 28,5–33,5 | P12 | Mamie : « Une cerise, ça mûrit au soleil… » | Un sourire et du réconfort. On a envie de la citer en commentaire. | La réplique-culte, puis on frappe. |
| 33,5–38,7 | P13, P14 | Il revient avec des roses jaunes : « Pardon, mon cœur… T'as besoin de moi. » | La méfiance : on reconnaît l'emprise et on lui crie « ne cède pas ». | Le bouquet, la voix douce. |
| 38,7–43,6 | P15, P16 | « Mon tablier, c'est pas ma honte. Ma honte, c'est toi. » Porte claquée. | Un frisson de fierté, puis la jubilation de voir la porte lui claquer au nez. | La phrase-étendard, musique coupée, porte qui claque. |
| 43,6–50,0 | P17, P18 | Seul sur le palier : « La porte au nez… À moi ?! » Il est sûr qu'elle reviendra, puis avoue payer sa salle avec ses pourboires. | Le choc, et l'envie de prévenir Cerise. C'est ce qui fera écrire dans les commentaires. | L'ironie dramatique : le public sait, elle non. |
| 50,0–54,7 | P19 à P21 | Kiwi la coache à l'aube, sur les quais : course, enchaînement de coups ; « Plus fort, Cerise ! » | L'élan et la tendresse : elle se construit, et elle n'est pas seule. | `revanche` démarre ; plans courts ; la voix de Kiwi coupe le passage muet. |
| 54,7–57,3 | P22 | « 100 JOURS PLUS TARD » : elle entre au ralenti, dans le même cadre qu'au début. | Un frisson : « la revoilà ». | Rime visuelle avec le P1, flash, ralenti, témoins qui se retournent dans des murmures ; le carton passe au-dessus d'elle, dans le tiers haut. |
| 57,3–62,2 | P23, P24 | Citron se décompose sous un « Quoi ?! » hors champ ; Coco la drague avec la phrase de Citron. | Satisfaction, puis un rire : l'ironie de la phrase recyclée. | La réplique-miroir. |
| 62,2–67,6 | P25, P26 | « La serveuse a fini son service. » Kiwi l'attend : « Ce soir, c'est toi qu'on sert. » | Le triomphe tranquille, puis l'émotion : « enfin lui ». | Le motif du service, retourné deux fois. |
| 67,6–76,2 | P27 à P29 | Retenu par ses potes, Citron menace : « Un seul pour te faire tomber ! » Myrtille le lâche avec le zeste. | De l'inquiétude, puis un rire moqueur. | La menace en un seul jour ; le calembour. |
| 76,2–78,6 | P30, fin | « Jamais ! », coupe sèche, PARTIE 2. | Une frustration voulue : il faut la suite. | La coupe au noir, le coup sourd. |

**La courbe d'ensemble :** malaise, indignation, compassion, fierté, aversion, élan, jubilation, inquiétude. Chaque
creux est suivi d'une remontée dans les 6 secondes. Ces temps sont estimés : après la mesure des voix, ils bougent
d'une ou deux secondes, mais l'ordre et la courbe restent.

**Les trois répliques à citer :**
- Mamie (P12) : « Une cerise, ça mûrit au soleil… Pas à l'ombre d'un citron. »
- Cerise (P15) : « Mon tablier, c'est pas ma honte. Ma honte, c'est toi. »
- Cerise (P25) : « La serveuse a fini son service. »

**Ce que l'épisode ne doit jamais faire ressentir :**
- que le corps de Cerise posait problème ;
- qu'elle « mérite » Kiwi parce qu'elle est devenue belle. Kiwi est là dès le jour 1 ;
- que la violence est une réponse. La lutte du P27 reste hors champ, et personne ne frappe personne ;
- que la caméra regarde les corps plutôt que les visages.

## B. Bible visuelle

**Le principe :** chaque prompt est un assemblage de blocs fixes, plus une partie variable par plan.
- **Les blocs fixes :** le style, la caméra, le personnage, le décor, la voix, l'accessoire et le champ négatif. Ils
  sont recopiés au mot près par le code, depuis `episode.json`. Personne ne les reformule.
- **La partie variable :** la taille de plan, le geste, la réplique coupée en segments, la consigne de jeu et le son.
- **Le prénom d'un personnage n'apparaît jamais seul dans un prompt.** Le moteur ne le relie à rien, et nos essais
  ont montré qu'il mélange alors les personnages.

### B.1 Les blocs fixes de l'épisode

**BLOC STYLE, image** (identique à `episode.json` → `style`, mot pour mot, en tête de chaque prompt d'image) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame
```

**BLOC STYLE, vidéo** (même texte, seul « movie still » devient « film », car une *still* est une image fixe ; `episode.json` → `style_video`) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame
```

**BLOC CAMÉRA** (après la taille de plan, dans chaque prompt vidéo) :

```text
on a locked-off static camera; the framing never changes.
```

**BLOC LÈVRES** (après la réplique, plans parlés) :

```text
Only she speaks, her lips moving in sync with every word, and the camera holds the frame during the pauses.
Only he speaks, his lips moving in sync with every word, and the camera holds the frame during the pauses.
```

**BLOC MUET** (plans sans parole, à la place de la réplique) :

```text
She does not speak and her lips stay closed. No one speaks.
He does not speak and his lips stay closed. No one speaks.
```

**CHAMP NÉGATIF DE BASE** : la liste du rapport, recopiée telle quelle, puis les quatre interdits de la série (règle physique). Chaque plan y ajoute ses interdits propres (§ D). Dans les décors à foule, « extra people » est retiré et remplacé par « sharp faces in the crowd ».

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face
```

**Les règles de physique** (validées par le propriétaire, niveau « 6 sur 10 ») :
- **Les femmes :** voluptueuses, décolleté, lèvres pleines, maquillage glamour, tenues ajustées.
- **Les hommes :** très musclés, torse nu sous une veste ou un sweat ouvert, ou en débardeur de salle.
- **Toujours habillés :** ni lingerie, ni maillot, ni nudité.
- **Aucune pose explicite,** et aucune caméra qui s'attarde sur une partie du corps. À la salle de sport, on cadre
  le visage et le buste ; on ne fait ni plan de dos ni pose penchée.
- **Des visages clairement adultes,** de 25 à 30 ans. L'âge est écrit dans chaque bloc d'apparence.

**Les règles de composition** (leçons de l'ép. 1) :
- **Un seul personnage visible, et c'est lui qui parle.** Les figurants sont petits, loin et flous, et seulement
  dans les décors « foule ».
- **Le visage est dans la moitié haute du cadre.** Rien d'important dans le cinquième bas : c'est là qu'Agnes
  incruste ses faux sous-titres, que le montage floute.
- **Derrière un gros plan, un fond simple :** briques, fenêtre floue, mur. Jamais de miroir, de tableau, d'affiche
  ni de reflet : ils font apparaître un visage en double au recadrage.
- **Aucun texte dans l'image :** ni enseigne, ni écran lisible, ni chiffre sur les poids, ni étiquette. SMS,
  chiffres, publications et carton sont incrustés au montage.
- **La caméra reste fixe pendant la génération.** Les zooms et le ralenti se font au montage, avec un facteur de
  1,25 au plus.
- **Plans de 2 à 5 s à la génération,** 4 s au minimum chez Agnes. Le montage coupe autour de la réplique.

### B.2 Les personnages

| Personnage | Fruit, couleur | Rôle dans l'épisode | Tenues (fiches) | Accessoire signature | Voix | Plans à l'image |
|---|---|---|---|---|---|---|
| Cerise | cerise, rouge profond | l'héroïne reniée, qui revient | `cerise`, `cerise_maison`, `cerise_sport`, `cerise_glow` | les deux cerises et la feuille dans les cheveux | clone `cerise` | P1, P4, P6, P8, P11, P13, P15, P20 à P22, P25 |
| Citron | citron, jaune vif | le copain qui a honte d'elle, deux apartés | `citron_salle`, `citron` | la grosse chaîne en or | clone `citron` | P2, P5, P7, P9, P10, P14, P16 à P18, P23, P27, P28, P30 |
| Coco | noix de coco, brun clair fibreux | le pote rigolard, puis dragueur recalé | `coco` | la serviette blanche au cou | **à créer** : `coco` | P24 (voix hors champ au P1) |
| Myrtille | myrtille, bleu indigo | le pote moqueur, qui lâche Citron à la fin | `myrtille` | le grand casque blanc au cou | **à créer** : `myrtille` | P3, P29 (voix hors champ au P23) |
| Mamie Prune | prune, violet | le creux et la réplique à citer | `prune` | les petites lunettes rondes et le châle beige | voix décrite `prune` | P12 |
| Kiwi | kiwi, vert olive | le coach, puis celui qui l'attend | `kiwi`, `kiwi_chic` | la veste verte de livreur | clone `kiwi` | P19, P26 (voix hors champ au P21) |
| Pêche | pêche, rose pêche | hors champ : sa publication s'affiche | (`peche`) | les créoles en or et la feuille | clone `peche` | aucun |

Chaque fiche ci-dessous donne :
- le bloc d'apparence de chaque tenue, en anglais, à coller tel quel ;
- l'accessoire signature ;
- le bloc voix (jeu) ;
- le prompt de la fiche d'identité, portrait en pied sur fond neutre.

Pour les personnages et tenues existants, ce prompt est celui qui a produit la fiche (`outils/identites.py`) :
**on ne régénère pas une fiche validée**, le prompt sert seulement à la refaire en cas de perte. Pour les tenues,
c'est le texte exact que `produire.py --only tenues` envoie, avec la fiche de base en référence.

#### Cerise · l'héroïne, 25 ans, serveuse

- **Caractère :** gentille, blessée, puis déterminée ; elle ne crie jamais, sa force est le calme.
- **Les quatre tenues, et l'histoire qu'elles racontent :**
  - `cerise`, en tablier moutarde, à la salle : P1 à P8. C'est **l'« avant »**, renforcé dans la partie variable
    des P1, P4, P6 et P8 : un stylo-bille derrière l'oreille, un petit carnet de commandes dans la poche du tablier,
    les épaules un peu voûtées ;
  - `cerise_maison`, sweat crème et pyjama à cerises, chez Mamie et à la porte : P11, P13 et P15. C'est le creux ;
  - `cerise_sport`, veste zippée blanche à liserés cerise, sur les quais, à la course et aux coups dans les
    pattes d'ours de Kiwi (hors champ) : P20 et P21. C'est l'effort ;
  - `cerise_glow`, robe-blazer ivoire à boutons dorés et pendentif cerise, de grandes lunettes de soleil dorées
    relevées dans les cheveux, des ondulations glamour fraîchement coiffées et, sur la fiche et au P22, un petit sac
    structuré rouge cerise, pour le défilé et la réplique : P22 et P25. C'est **l'« après »**.
- **Accessoire signature :** les deux petites cerises et la feuille dans les cheveux, dans toutes les tenues. Le
  pendentif cerise en or et les lunettes de soleil dorées s'y ajoutent dans `cerise_glow`. Jamais de créoles dorées :
  c'est la signature de Pêche.
- **Regard :** toujours hors champ vers la **droite**, sauf au P20, où elle court vers la caméra.
- **Cheveux :** toujours lâchés. Une queue de cheval changerait son identité.

**Bloc d'apparence `cerise`** (53 mots, à coller tel quel) :

```text
a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing a tight white deep V-neck crop top, a tiny mustard-yellow waitress apron and tight ripped blue jeans, with an adult 25-year-old face
```

**Bloc d'apparence `cerise_maison`** (50 mots, à coller tel quel) :

```text
a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing an oversized cream hoodie with a small embroidered red cherry and cherry-print pajama trousers, with an adult 25-year-old face
```

**Bloc d'apparence `cerise_sport`** (53 mots, à coller tel quel) :

```text
a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing a white zip-up track jacket with thin cherry-red stripes over a cherry-red tank top and black leggings, with an adult 25-year-old face
```

**Bloc d'apparence `cerise_glow`** (64 mots, à coller tel quel) :

```text
a glamorous voluptuous young woman with deep cherry-red skin, long voluminous dark-red hair in freshly styled glossy Hollywood waves with two small cherries and a leaf clipped in it, oversized gold-rimmed sunglasses pushed up in her hair, full glossy red lips, glamorous makeup, wearing a tailored ivory-white blazer mini dress with gold buttons and a small gold cherry pendant, with an adult 25-year-old face
```

**Bloc voix (jeu)** : `a soft, sweet young woman's voice, slightly husky`. Clone Voicebox `cerise`. Jeu : douce et voilée ; elle tremble quand elle a mal (P6, P11) et se raffermit dès le P6 ; au retour (P25), posée, amusée, jamais agressive.

**Prompt de la fiche d'identité** (portrait en pied, fond neutre) :

```text
Stylized semi-realistic 3D CGI character, glamorous high-budget animated movie look, cinematic studio lighting, highly detailed skin and hair, striking attractive face. a stunning glamorous adult woman, 25 years old, with a mature adult face; her skin is deep cherry-red everywhere, smooth satin finish; voluptuous exaggerated hourglass figure: large full bust, very narrow waist, wide hips and a big round curvy backside; long voluminous wavy dark-red hair with two small cherries and a leaf as a hair clip; striking face: big almond-shaped hazel eyes with long lashes, full glossy lips, high cheekbones, glamorous makeup; wearing a tight white low-cut V-neck crop t-shirt showing cleavage and her midriff, a small mustard-yellow waitress apron tied at the hips, tight high-waisted blue jeans and white sneakers; confident standing pose. Full body, front view, standing, centered, plain light grey studio background, character reference, exactly one single character, no text, no logo.
```

**Fiche de la tenue `cerise_maison`** (référence : `identite/cerise.png` ; c'est le texte exact que `produire.py --only tenues` envoie) :

```text
the same woman, same face, same full red lips and glamorous makeup, same deep cherry-red skin, same voluptuous hourglass figure, same long wavy dark-red hair with the cherries and leaf, now wearing an oversized soft cream hoodie with a small red cherry embroidered on the chest, the sleeves pulled over her hands, loose red-and-white cherry-print pajama trousers and fluffy white socks. Full body, front view, standing, centered, plain light grey studio background, character reference, exactly one single character, no text. Pixar-style 3D animated character, cinematic soft lighting.
```

**Fiche de la tenue `cerise_sport`** (référence : `identite/cerise.png` ; c'est le texte exact que `produire.py --only tenues` envoie) :

```text
the same woman, same face, same full red lips and glamorous makeup, same deep cherry-red skin, same voluptuous hourglass figure, same long wavy dark-red hair with the cherries and leaf, now wearing a fitted white zip-up track jacket with thin cherry-red stripes on the sleeves, zipped up to the chest over a cherry-red tank top, high-waisted black leggings, white sneakers and a white sweatband on one wrist. Full body, front view, standing, centered, plain light grey studio background, character reference, exactly one single character, no text. Pixar-style 3D animated character, cinematic soft lighting.
```

**Fiche de la tenue `cerise_glow`** (référence : `identite/cerise.png` ; c'est le texte exact que `produire.py --only tenues` envoie) :

```text
the same woman, same face, same full red lips and glamorous makeup, same deep cherry-red skin, same voluptuous hourglass figure, same long voluminous dark-red hair with the cherries and leaf, now in freshly styled glossy Hollywood waves, with oversized gold-rimmed sunglasses pushed up in her hair, wearing a tailored ivory-white blazer mini dress with gold buttons and a deep but closed V neckline, a thin gold belt at the waist, nude high heels, a small gold cherry pendant on a fine chain and a small structured cherry-red handbag on her arm; confident model pose, one hand on her hip. Full body, front view, standing, centered, plain light grey studio background, character reference, exactly one single character, no text. Pixar-style 3D animated character, cinematic soft lighting.
```

#### Citron · le méchant, 28 ans, frimeur de salle

- **Caractère :** frimeur, lâche devant ses potes, mielleux en tête-à-tête, mesquin en secret.
- **Les deux tenues :**
  - `citron_salle`, sweat de salle noir sans manches, ouvert : P2, P5, P7, P23 et P27 à P30 ;
  - `citron`, veste de cuir noire ouverte, de l'ép. 1 : le salon et le palier, P9, P10 et P14 à P18.
- **Accessoire signature :** la grosse chaîne en or, dans les deux tenues.
- **Regard :** hors champ vers la **gauche**. Il regarde la caméra dans ses apartés (P9, P10, P17 et P18), puis au
  P28 et au P30.
- **Sa silhouette** est celle de la fiche, de bout en bout : sa punition est sociale, pas physique.

**Bloc d'apparence `citron`** (42 mots, à coller tel quel) :

```text
a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black leather jacket on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble
```

**Bloc d'apparence `citron_salle`** (43 mots, à coller tel quel) :

```text
a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black sleeveless gym hoodie on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble
```

**Bloc voix (jeu)** : `a deep, smooth, confident young man's voice, arrogant`. Clone Voicebox `citron`, hauteur ramenée vers 125 Hz (`voix_hauteur`). Grave, posé, arrogant ; mielleux au P5 et au P14 ; il crie dans les derniers plans (P27 à P30).

**Prompt de la fiche d'identité** (portrait en pied, fond neutre) :

```text
Stylized semi-realistic 3D CGI character, glamorous high-budget animated movie look, cinematic studio lighting, highly detailed skin and hair, striking attractive face. a hugely muscular, very handsome adult man, 28 years old; his skin is bright lemon-yellow everywhere with a subtle peel texture, his head slightly lemon-shaped with a small tip on top; bodybuilder physique: massive broad shoulders, huge pecs, visible six-pack abs, huge arms, V-shaped torso; chiseled square jaw, light stubble, intense arrogant eyes, cocky smirk, slicked-back golden-yellow hair; wearing an open black leather jacket over his bare chest showing his pecs and abs, a thick gold chain, tight black jeans and designer sneakers; confident standing pose. Full body, front view, standing, centered, plain light grey studio background, character reference, exactly one single character, no text, no logo.
```

**Fiche de la tenue `citron_salle`** (référence : `identite/citron.png` ; c'est le texte exact que `produire.py --only tenues` envoie) :

```text
the same man, same face, same bright lemon-yellow skin, same slicked-back golden hair, same huge muscular bodybuilder build, same thick gold chain, now wearing an open black sleeveless gym hoodie on his bare muscular chest and abs, black joggers and black-and-white sneakers. Full body, front view, standing, centered, plain light grey studio background, character reference, exactly one single character, no text. Pixar-style 3D animated character, cinematic soft lighting.
```

#### Coco · nouveau, la noix de coco, 28 ans

- **Rôle :** le pote rigolard. Sa voix hors champ ouvre l'épisode (P1). Au P24, il drague Cerise avec la phrase
  de Citron et se fait recaler.
- **Il ne se dit jamais à voix haute :** personne ne prononce « Coco ».
- **Accessoire signature :** la serviette blanche autour du cou.
- **Regard :** hors champ vers la **gauche**.
- **Il doit se lire comme une noix de coco, par la matière et jamais par des traits de visage :** peau brun clair
  chaud couverte d'une fine bourre fibreuse, comme l'enveloppe d'une coco, et une courte touffe hérissée de fibres
  sèches sur le dessus du crâne. Sourcils épais et sourire en coin, rien de plus.
- **Aucun trait caricatural (correction bloquante du chef).** La v2 cumulait, sur le seul personnage à peau brun
  foncé, de grandes dents blanches, un crâne rasé, une voix forte et rieuse, « Wesh » et le rôle du dragueur recalé :
  c'est un trope caricatural connu, et le public compte beaucoup de mineurs. On retire les dents et le crâne rasé,
  la peau passe au brun clair de la bourre de coco, et « Wesh » devient « Oh ». Au juge visuel, refuser toute fiche
  où la texture fibreuse ne se voit pas, et toute fiche qui surligne les dents ou les lèvres.
- **La drague reste légère :** un sourire, un clin d'œil raté. Jamais de geste vers elle, jamais de sifflet.

**Bloc d'apparence `coco`** (59 mots, à coller tel quel) :

```text
a hugely muscular handsome young man with warm tan-brown skin covered in a fine fibrous fuzz like a coconut husk, a short spiky tuft of dry coconut fibers on top of his head, thick eyebrows and a cocky grin, wearing a tight white sleeveless gym tank top and a white towel around his neck, with an adult 28-year-old face
```

**Bloc voix (jeu)** : `a loud, hoarse, laughing young man's voice`. **À créer** : profil Voicebox `coco`. On prend une voix de référence avec `voix_reference.py`, sinon une voix décrite. `voix_hauteur` est à 115 Hz. Rauque, rieur, fort ; il doit se distinguer à l'oreille de Citron, grave et posé.

**Prompt de la fiche d'identité** (portrait en pied, fond neutre) :

```text
Stylized semi-realistic 3D CGI character, glamorous high-budget animated movie look, cinematic studio lighting, highly detailed skin and hair, striking attractive face. a hugely muscular, very handsome adult man, 28 years old, with a mature adult face; his skin is warm tan-brown everywhere, covered with a fine short fibrous fuzz like a coconut husk; bodybuilder physique: massive shoulders, huge arms, big chest; a short spiky tuft of dry coconut fibers on top of his head, thick eyebrows, a cocky grin; wearing a tight white sleeveless gym tank top, black joggers, white sneakers and a white towel around his neck; confident standing pose. Full body, front view, standing, centered, plain light grey studio background, character reference, exactly one single character, no text, no logo.
```

#### Myrtille · nouveau, la myrtille, 26 ans

- **Rôle :** le pote moqueur. Il en rajoute au début (P3). Son « Quoi ?! » hors champ tombe sur la réaction de
  Citron au retour de Cerise (P23). À la fin (P29), il lâche Citron avec le calembour du zeste.
- **Il ne se dit jamais à voix haute.**
- **Accessoire signature :** le grand casque audio blanc autour du cou.
- **Regard :** hors champ vers la **gauche**, sauf au P29 : il regarde vers la **droite**, vers Citron qu'il vient
  de lâcher.
- **Son bleu indigo mat**, avec une pruine poudrée comme celle d'une myrtille, se lit même en silhouette, à côté du
  jaune de Citron et du brun de Coco.

**Bloc d'apparence `myrtille`** (49 mots, à coller tel quel) :

```text
a tall muscular handsome young man with deep indigo-blue matte skin with a soft dusty bloom like a blueberry, a styled navy-blue quiff and a teasing smirk, wearing a light-grey sleeveless gym hoodie with the hood down and big white headphones around his neck, with an adult 26-year-old face
```

**Bloc voix (jeu)** : `a nasal, teasing, slightly high-pitched young man's voice`. **À créer** : profil Voicebox `myrtille`. Nasal, taquin, un peu aigu. Pas de `voix_hauteur` : la chaîne ne fait que baisser une voix. Tester « frérot » à whisper.

**Prompt de la fiche d'identité** (portrait en pied, fond neutre) :

```text
Stylized semi-realistic 3D CGI character, glamorous high-budget animated movie look, cinematic studio lighting, highly detailed skin and hair, striking attractive face. a tall muscular, very handsome adult man, 26 years old, with a mature adult face; his skin is deep indigo-blue everywhere with a soft dusty matte bloom like a blueberry; athletic muscular physique: broad shoulders, big arms, flat abs; a styled navy-blue quiff, a teasing smirk with one raised eyebrow; wearing a light-grey sleeveless gym hoodie with the hood down, black joggers, white sneakers and big white headphones around his neck; confident standing pose. Full body, front view, standing, centered, plain light grey studio background, character reference, exactly one single character, no text, no logo.
```

#### Mamie Prune · la grand-mère de Cerise

- **Rôle :** le creux et la réplique à citer (P12). Elle parle au public : regard caméra par-dessus ses
  lunettes.
- **Tenue :** `prune`, de l'ép. 1 : chapeau tricoté, châle beige, robe fleurie.
- **Accessoire signature :** les petites lunettes rondes et le châle beige. La cuillère en bois de la fiche n'est
  pas utilisée ici : au P12, elle remue son thé à la petite cuillère.

**Bloc d'apparence `prune`** (44 mots, à coller tel quel) :

```text
a small old grandmother with deep purple wrinkled skin, white hair, small round glasses, a knitted hat, a knitted beige shawl and a floral dress, with a round deeply wrinkled face, kind mischievous eyes and a small warm smile, clearly a very old woman
```

**Bloc voix (jeu)** : `a crackly old woman's voice, warm and mischievous`. Voix décrite (Qwen VoiceDesign), profil `prune`, tempo 1,25 et léger vibrato (`effets_voix`). Lente, chaude, malicieuse, avec une vraie pause sur « soleil… ».

**Prompt de la fiche d'identité** (portrait en pied, fond neutre) :

```text
Stylized semi-realistic 3D CGI character, glamorous high-budget animated movie look, cinematic studio lighting, highly detailed skin and hair, striking attractive face. an old grandmother character whose head and body are one deep purple wrinkled prune, small round glasses, kind but mischievous eyes, wearing a knitted beige shawl, a small knitted hat, a long floral dress and slippers, holding a wooden spoon. Full body, front view, standing, centered, plain light grey studio background, character reference, exactly one single character, no text, no logo.
```

#### Kiwi · l'ami d'enfance, livreur

- **Rôle :** le coach pendant les cent jours (P19, puis sa voix hors champ au P21), et celui qui l'attend à la
  porte (P26). Il est là
  **avant** la métamorphose : c'est ce qui donne son sens à la fin.
- **Les deux tenues :**
  - `kiwi`, veste verte de livreur ouverte, de l'ép. 1 : P19 ;
  - `kiwi_chic`, chemise de lin blanche ouverte et fine chaîne d'argent, la veste verte de livreur sur l'épaule :
    P26.
- **Accessoire signature :** la veste verte de livreur. Dans `kiwi_chic`, elle rend lisible le « Le livreur ?! » de
  Citron.
- **Regard :** hors champ vers la **gauche**. Il n'est jamais dans le même cadre que Cerise.
- **Le titre ne dit jamais « Kiwi et Cerise »,** trop proche d'une série concurrente.

**Bloc d'apparence `kiwi`** (40 mots, à coller tel quel) :

```text
a hugely muscular handsome young man with olive-green fuzzy skin, short curly dark-brown hair, bright green eyes, wearing an open green delivery jacket on his bare muscular chest with six-pack abs, with an adult 27-year-old face and a warm smile
```

**Bloc d'apparence `kiwi_chic`** (53 mots, à coller tel quel) :

```text
a hugely muscular handsome young man with olive-green fuzzy skin, short curly dark-brown hair, bright green eyes, wearing an open white linen shirt on his bare muscular chest with six-pack abs, a thin silver chain and his green delivery jacket slung over one shoulder, with an adult 27-year-old face and a warm smile
```

**Bloc voix (jeu)** : `a warm, friendly young man's voice with a slight Parisian street accent`. Clone Voicebox `kiwi`, hauteur vers 135 Hz. Chaleureux, léger accent de quartier ; énergique au P19 et au P21 (hors champ), doux au P26.

**Prompt de la fiche d'identité** (portrait en pied, fond neutre) :

```text
Stylized semi-realistic 3D CGI character, glamorous high-budget animated movie look, cinematic studio lighting, highly detailed skin and hair, striking attractive face. a hugely muscular, very handsome adult man, 27 years old; his skin is olive-green everywhere with a fine fuzzy kiwi texture; athletic bodybuilder physique: massive shoulders, huge pecs, visible six-pack abs, big arms; short curly dark-brown hair, bright kiwi-green eyes, chiseled jaw, warm charming smile; wearing a backwards green cap, a tight white cropped tank top with a small kiwi slice logo showing his abs and big arms, an open green delivery jacket, black cargo pants and sneakers; confident standing pose. Full body, front view, standing, centered, plain light grey studio background, character reference, exactly one single character, no text, no logo.
```

**Fiche de la tenue `kiwi_chic`** (référence : `identite/kiwi.png` ; c'est le texte exact que `produire.py --only tenues` envoie) :

```text
the same man, same face, same olive-green fuzzy skin, same short curly dark-brown hair, same bright green eyes, same huge muscular build, now wearing an open white linen shirt with rolled-up sleeves on his bare muscular chest and abs, dark-green tailored trousers, white sneakers and a thin silver chain, with his green delivery jacket slung over one shoulder. Full body, front view, standing, centered, plain light grey studio background, character reference, exactly one single character, no text. Pixar-style 3D animated character, cinematic soft lighting.
```

#### Pêche · hors champ dans cet épisode

- **Rôle :** c'est elle qui a publié la vidéo moqueuse. On ne la voit pas : sa publication s'affiche en
  notification au P11 (`peche.officielle 🍑`, 48 000 vues).
- **Son bloc est gardé** pour la bible et pour la partie 2.

**Bloc d'apparence `peche`** (51 mots, à coller tel quel) :

```text
a glamorous voluptuous young woman with peach-pink skin and rosy cheeks, long glossy wavy brown hair with a green leaf clipped in it, very full glossy pink lips, bold glamorous makeup, big gold hoop earrings, wearing a tight hot-pink satin mini dress with a plunging neckline, with an adult 26-year-old face
```

**Bloc voix (jeu)** : `a high-pitched, drawling, mocking young woman's voice`. Clone Voicebox `peche`, non utilisé dans cet épisode.

**Prompt de la fiche d'identité** (portrait en pied, fond neutre) :

```text
Stylized semi-realistic 3D CGI character, glamorous high-budget animated movie look, cinematic studio lighting, highly detailed skin and hair, striking attractive face. a stunning glamorous adult influencer woman, 26 years old, with a mature adult face; her skin is vivid peach orange everywhere with deep pink-red blush on the cheeks, like a ripe peach fruit; voluptuous exaggerated hourglass figure: large full bust, tiny waist, wide hips and a big round curvy backside; long glossy wavy brown hair with a green peach leaf clipped in it; striking face: big eyes with long lashes, full glossy pink lips, contoured glamorous makeup, arrogant smile; wearing a tight pink bodycon mini dress with a deep V neckline showing cleavage, big gold hoop earrings, holding a smartphone with a pink case; confident standing pose. Full body, front view, standing, centered, plain light grey studio background, character reference, exactly one single character, no text, no logo.
```

### B.3 La transformation : fiche « avant », fiche « après »

**La règle :** le même visage, la même espèce, le même accessoire et la même silhouette. Le style change, et
c'est au montage qu'on passe de l'un à l'autre, jamais dans un plan.

| | « Avant » : `identite/cerise.png` | « Après » : `identite/cerise_glow.png` |
|---|---|---|
| Plans | P1, P4, P6, P8 | P22, P25 |
| Visage | le même : yeux noisette en amande, lèvres pleines rouges, visage adulte de 25 ans | **identique** |
| Peau | rouge cerise profond partout | **identique** ; si le générateur l'a effacée, faire la retouche « peau seulement » ci-dessous |
| Cheveux | longs, ondulés, rouge sombre, lâchés | **mêmes longueur et couleur**, en ondulations glamour (Hollywood waves) brillantes, fraîchement coiffées |
| Accessoire | deux petites cerises et une feuille dans les cheveux ; un stylo-bille derrière l'oreille et un petit carnet de commandes dans la poche du tablier (partie variable des P1, P4, P6, P8) | cerises et feuille **identiques**, plus un petit pendentif cerise en or, de grandes lunettes de soleil à monture dorée relevées dans les cheveux (bloc) et un petit sac structuré rouge cerise (fiche, et `cadre` du P22). Pas de créoles : c'est la signature de Pêche |
| Silhouette | celle de la fiche | **identique** |
| Tenue | crop top blanc, petit tablier moutarde, jean déchiré, baskets | robe-blazer ivoire à boutons dorés, ceinture fine dorée, escarpins nude |
| Posture, regard | épaules légèrement voûtées qui retombent, sourire inquiet | menton levé, épaules ouvertes, regard assuré |
| Lumière | heure dorée douce de fin d'après-midi | contre-jour doré plus chaud, cheveux qui brillent |

Les deux étapes du milieu, `cerise_maison` (le creux) et `cerise_sport` (l'effort), suivent la même règle.

**Pourquoi ces signes (correction du chef).** Le bloc `cerise` de l'ép. 1 est déjà glamour (crop top, maquillage) :
sans signe lisible, l'écart reposait sur la seule tenue, alors que la référence avait un écart extrême. On renforce
les deux bouts avec des détails qui se lisent en miniature sur un téléphone, sans toucher aux blocs de l'ép. 1 :
le stylo, le carnet et les épaules voûtées de la serveuse, puis les lunettes de soleil, les ondulations et le sac.

**Fiche « avant »** : on garde la fiche validée `identite/cerise.png`. Son prompt est donné au § B.2 (Cerise).

**Fiche « après »** : `produire.py --only tenues` la fabrique depuis `identite/cerise.png`, avec la consigne de la
tenue `cerise_glow` (texte exact au § B.2). Valider à l'œil, côte à côte avec la fiche « avant », sur les points
du tableau.

**Retouche « peau seulement »**, à faire si la couleur de fruit a disparu (défaut connu, voir la bible). La fiche
fautive est en référence :

```text
Same image, same character, same face, same clothes, same pose and same framing. Only restore the skin color: her skin is deep cherry-red everywhere, smooth satin finish, like a ripe cherry. Keep the two small cherries and the leaf in her hair. No text.
```

**Les interdits :**
- aucun morphing ni changement de tenue à l'intérieur d'un plan ;
- aucune image « avant / après » côte à côte dans la vidéo ;
- aucun chiffre de poids ni de taille ;
- aucun conseil d'alimentation.

### B.4 Les accessoires (blocs figés, sans aucun texte)

| Accessoire | Plans | Description | Bloc anglais à coller |
|---|---|---|---|
| Gamelle cerise | P1, P4 | petite boîte repas rouge brillante en forme de cerise, courte anse verte en queue | `a small glossy red cherry-shaped lunch box with a short green stem handle` |
| Shaker | P2 | shaker de protéines noir mat, opaque, sans marque | `a plain matte black protein shaker` |
| Pot à pourboires (l'indice) | P9, P10 | gros bocal en verre rouge en forme de cerise, couvercle vert en queue, plein de pièces et de billets pliés, sans étiquette | `a big plain unlabeled red glass jar shaped like a cherry, with a green stem-shaped lid, packed with coins and folded paper money` |
| Bouquet de roses jaunes | P14 à P17 | gros bouquet de roses jaunes dans un papier kraft brun uni (le jaune = la jalousie, et la couleur de Citron) ; cité en entier à chaque plan, même quand il pend au bout du bras (P17) | `a big bouquet of yellow roses wrapped in plain brown kraft paper` |
| Stylo et carnet (l'« avant ») | P1, P4, P6, P8 | stylo-bille derrière l'oreille, petit carnet de commandes dans la poche du tablier, épaules un peu voûtées ; en gros plan, les prompts vidéo n'en gardent que le stylo et les épaules (le carnet est hors cadre) | `a ballpoint pen tucked behind her ear, a small order notepad in her apron pocket, shoulders slightly hunched` (`accessoires.serveuse`) |
| Sac (l'« après ») | P22 | petit sac structuré rouge cerise, au bras ; il est aussi sur la fiche `cerise_glow` | `a small structured cherry-red handbag` (`accessoires.sac`) |

**Le sac de frappe n'est plus un accessoire.** Il reste dans le décor `salle`, en arrière-plan, mais personne ne
le frappe : Cerise ne peut pas s'entraîner dans la salle de Citron sans que la bande la voie. Le P21 se tourne
donc sur les quais : elle frappe vers la droite, dans des pattes d'ours tenues par Kiwi hors champ, sans aucun
contact visible ; l'impact s'ajoute au montage.

### B.5 Axes de caméra et regards

On ne met jamais deux personnages dans le même cadre. Le dialogue se fait en champ et contre-champ, et chaque côté
d'un lieu a son propre décor : le moteur garde l'orientation de l'image du décor. Les regards sont fixes, pour que
les coupes se répondent.

| Lieu | Côté (décor) | Personnages | Regard |
|---|---|---|---|
| Salle de sport | `salle` (fenêtres, briques) | Cerise | hors champ vers la **droite** |
| Salle de sport | `salle_rack` (racks, briques) | Citron, Coco, Myrtille | hors champ vers la **gauche** ; caméra pour Citron aux P28 et P30 ; **exception : Myrtille au P29 regarde vers la droite**, vers Citron qu'il vient de lâcher |
| Entrée de la salle | `salle_entree` (portes, foule floue) | Cerise (P1, P22), Kiwi (P26) | Cerise vers la droite ; Kiwi vers la gauche |
| Salon de Citron | `appart` | Citron | **caméra** (aparté) |
| Cuisine de Mamie | `cuisine` | Cerise (P11), Mamie (P12) | Cerise vers la droite (vers Mamie) ; Mamie vers la caméra |
| Porte de Mamie | `porte` (vue du palier) | Cerise | vers la droite (vers le palier) |
| Palier | `palier` (vu de chez Mamie) | Citron | vers la gauche (vers la porte), puis caméra (P17, P18) |
| Quais | `quais` | Kiwi (P19), Cerise (P20, P21) | Kiwi vers la gauche ; Cerise court vers la caméra (P20), puis frappe vers la droite (P21) |

**Les contacts sont remplacés par du hors champ :**
- la gamelle est tendue vers la droite ;
- le bouquet est serré contre sa poitrine, jamais tendu à quelqu'un ;
- la porte claque hors champ ;
- les potes qui retiennent Citron sont hors champ, avec un bruit de lutte ;
- les pattes d'ours que Kiwi tend à Cerise sont hors champ, avec un bruit d'impact (P21) ;
- la main de Kiwi est tendue vers la gauche ;
- Myrtille lâche Citron hors champ, à droite (P29).

## C. Décors

Huit décors : six nouveaux et deux repris de l'ép. 1.

**Les règles communes :**
- **La lumière :** l'heure dorée pour la salle et les quais, la nuit chaude pour les intérieurs.
- **Les motifs de fruits** des habitants des lieux : les serviettes jaune citron de la salle, le papier peint
  fleuri de Mamie.
- **Aucun texte :** ni miroir, ni affiche, ni écran, ni néon, ni chiffre, ni plaque.

**La fabrication :**
- `produire.py --only decors` génère chaque décor vide. On prévoit 4 essais.
- Les décors existants sont copiés. On n'en régénère aucun.
- Les figurants n'existent que dans le décor `salle_entree` (`foule: true`) : ils sont petits, loin et flous, et
  leurs couleurs diffèrent de celles de la troupe (vert pomme, mandarine, framboise).
- **Une seule exception :** l'amorce de la bande, **version cible au P1** et variante au P22. Trois silhouettes floues,
  de dos et sans visage, aux couleurs de Citron, Coco et Myrtille (jaune citron, brun coco, bleu indigo), sur les
  bords gauche et droit à mi-hauteur. Elles s'ajoutent par retouche de `salle_entree.png`, jamais dans le décor de
  base (§ D, P1 et P22).

| Décor | Lieu | Moment | Plans | Fabrication |
|---|---|---|---|---|
| `salle` | salle de sport, côté Cerise | heure dorée | P4, P6, P8, P25 | nouveau |
| `salle_rack` | salle de sport, côté de la bande | heure dorée | P2, P3, P5, P7, P23, P24, P27 à P30 | nouveau |
| `salle_entree` | entrée de la salle, avec foule floue | heure dorée, contre-jour | P1, P22, P26 | nouveau, `foule: true` ; retouche « amorce » : version cible au P1, variante au P22 |
| `appart` | salon de Citron, avec le pot à pourboires | nuit | P9, P10 | **retouche** de `appart.png` (ép. 1) |
| `cuisine` | cuisine de Mamie Prune | nuit, pluie | P11, P12 | **copie** de `cuisine.png` (ép. 1) |
| `porte` | porte de Mamie, vue du palier | nuit | P13, P15 | nouveau |
| `palier` | palier, vu de chez Mamie | nuit | P14, P16 à P18 | nouveau |
| `quais` | quais de Seine | lever du soleil | P19, P20, P21 | nouveau |

Pour chaque décor ci-dessous :
- le bloc descriptif ;
- le repère court, collé dans les prompts vidéo ;
- le son ;
- le prompt d'image du décor vide en 9:16, qui est le texte exact envoyé par la chaîne.

### C.1 `salle` · la salle de sport, côté Cerise

| Élément | Contenu |
|---|---|
| Lieu | Salle de sport de quartier dans un ancien loft industriel parisien : le territoire de Citron. C'est l'axe A, celui de Cerise. |
| Moment | Fin d'après-midi, à l'heure dorée (scène A et retour). |
| Objets repères | 1. murs de briques rouges ; 2. hautes fenêtres cintrées à châssis noir ; 3. banc de musculation noir ; 4. sac de frappe en cuir rouge ; 5. serviettes jaune citron pliées. |
| Lumière | Chaude : le soleil couchant orange entre par les fenêtres. Froide : des ombres bleutées douces. |
| Couleurs | rouge brique, noir, orange doré, jaune citron, vert des plantes. |
| Ambiance sonore | cliquetis de fonte, brouhaha lointain. |
| Plans | P4, P6, P8, P25. |


**Repère court pour les prompts vidéo** (2 ou 3 repères, `decors.salle.court`) :

```text
In a sunlit loft gym at golden hour, red brick and arched windows blurred behind
```

**Son dans le prompt vidéo** : `gym ambiance, distant clanking weights`.

**Prompt d'image du décor vide, 9:16** (texte exact envoyé par `produire.py --only decors`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. A spacious neighbourhood gym in a converted Paris industrial loft at golden hour: exposed red brick walls, tall arched black steel-framed windows with warm orange sunset light pouring in, a black rubber floor, a padded black weight bench in the middle, a rack of plain unmarked chrome dumbbells, a red leather punching bag hanging from a chain, green plants, lemon-yellow towels folded on a shelf. No mirrors, no posters, no screens, no writing and no numbers anywhere. Empty set: no character in the picture. No text, no letters, no signs with writing.
```

Derrière les gros plans de Cerise, le fond reste simple : briques et fenêtres floues. Refuser tout candidat avec un miroir, une affiche, un écran ou un chiffre sur les poids. Le sac de frappe rouge reste un objet du décor, en arrière-plan : personne ne le frappe dans cet épisode.

### C.2 `salle_rack` · la salle de sport, côté de la bande

| Élément | Contenu |
|---|---|
| Lieu | La même salle, vue de l'autre côté. C'est l'axe B, le contre-champ de Citron, Coco et Myrtille. |
| Moment | Heure dorée. |
| Objets repères | 1. mur de briques rouges ; 2. racks à squat noirs ; 3. disques noirs sans marquage sur leurs supports ; 4. plyo box en bois ; 5. serviettes jaune citron suspendues. |
| Lumière | Le soleil couchant arrive de la gauche, dans une brume dorée légère. |
| Couleurs | noir, rouge brique, or, jaune citron. |
| Ambiance sonore | cliquetis de fonte, brouhaha lointain. |
| Plans | P2, P3, P5, P7, P23, P24, P27 à P30, plus le P1 bis en repli. |


**Repère court pour les prompts vidéo** (2 ou 3 repères, `decors.salle_rack.court`) :

```text
By black squat racks on a red brick wall, warm golden light from the left
```

**Son dans le prompt vidéo** : `gym ambiance, distant clanking weights`.

**Prompt d'image du décor vide, 9:16** (texte exact envoyé par `produire.py --only decors`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. The same industrial loft gym at golden hour seen from the other side: a red brick wall lined with black squat racks and plain unmarked black weight plates stacked on pegs, a wooden plyo box, lemon-yellow towels hanging on the racks, warm sunset light coming from the left, a soft golden haze in the air. No mirrors, no posters, no screens, no writing and no numbers anywhere. Empty set: no character in the picture. No text, no letters, no signs with writing.
```

C'est le décor le plus utilisé (11 plans) : valider le meilleur candidat avec soin, sans aucun chiffre sur les disques.

### C.3 `salle_entree` · l'entrée de la salle, avec foule floue

| Élément | Contenu |
|---|---|
| Lieu | L'entrée de la salle vue de l'intérieur : les grandes portes métalliques noires sont ouvertes sur une rue ensoleillée. C'est le seuil de l'humiliation (P1) et du retour (P22). |
| Moment | Heure dorée, en contre-jour. |
| Objets repères | 1. double porte en acier noir grande ouverte ; 2. rue ensoleillée derrière ; 3. murs de briques rouges ; 4. racks d'haltères sur les côtés ; 5. figurants flous de dos, aux bords du cadre. |
| Lumière | Un contre-jour doré puissant, avec un halo autour des silhouettes. |
| Couleurs | or, noir, rouge brique, touches vert pomme, mandarine et framboise (les figurants). |
| Ambiance sonore | brouhaha de la salle, rue lointaine ; au P22, le brouhaha laisse place aux murmures de la foule qui se retourne. |
| Plans | P1, P22 (même cadre), P26. |


**Repère court pour les prompts vidéo** (2 ou 3 repères, `decors.salle_entree.court`) :

```text
Inside the open steel doors of a loft gym, golden backlight, blurred gym-goers at the edges
```

**Son dans le prompt vidéo** : `gym hall murmurs, distant street`.

**Prompt d'image du décor (avec figurants flous), 9:16** (texte exact envoyé par `produire.py --only decors`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. The entrance of a Paris industrial loft gym at golden hour seen from inside: tall black steel double doors wide open onto a sunny street, warm golden backlight pouring in, red brick walls, plain unmarked dumbbell racks along the sides. A few gym-goers seen from behind and blurred at the edges of the frame are fruit people with colorful fruit-colored skin (apple green, tangerine orange, raspberry pink). The doorway itself is empty. No mirrors, no posters, no writing and no numbers anywhere. No text, no letters, no signs with writing.
```

`foule: true` : les figurants sont petits, loin, flous et de dos. Leurs couleurs ne doivent être ni brun, ni bleu, ni jaune, ni rouge cerise, ni vert olive. L'embrasure reste vide sur l'image du décor : Cerise et Kiwi y sont ajoutés.

**Exception, l'amorce (version cible au P1, variante au P22) :** une retouche de ce décor ajoute la bande, floue, de dos et sans visage (jaune citron, brun coco, bleu indigo), sur les bords gauche et droit à mi-hauteur, jamais dans le cinquième bas. Le décor de base, lui, ne change pas. Les prompts de retouche sont dans les fiches du P1 et du P22.

### C.4 `appart` · le salon de Citron, avec le pot à pourboires

| Élément | Contenu |
|---|---|
| Lieu | Le petit salon parisien de Citron (décor de l'ép. 1), avec l'indice : le pot à pourboires en forme de cerise. |
| Moment | Nuit. |
| Objets repères | 1. canapé gris et coussins ; 2. table basse en bois ; 3. **le pot cerise plein de pièces et de billets, net, sur la table basse** ; 4. lampadaire trépied et guirlande lumineuse ; 5. grande fenêtre sur les toits de Paris. |
| Lumière | Chaude : la lampe et les guirlandes. Froide : la nuit bleue par la fenêtre. |
| Couleurs | crème, gris, orange chaud, bleu nuit, rouge du pot. |
| Ambiance sonore | ambiance appartement nuit. |
| Plans | P9, P10. |


**Repère court pour les prompts vidéo** (2 ou 3 repères, `decors.appart.court`) :

```text
In a cozy Paris living room at night, warm lamp light, blue city window
```

**Son dans le prompt vidéo** : `quiet apartment at night`.

**Prompt d'image du décor vide, 9:16** (texte exact envoyé par `produire.py --only decors`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. A small cozy modern Paris apartment living room at night: a grey sofa with cushions, a coffee table, a warm floor lamp, string lights, plants, a big window with Paris rooftops and city lights at night. Warm lamp light and cool blue night light from the window. In the foreground, on the wooden coffee table, stands a big plain unlabeled red glass jar shaped like a cherry, with a green stem-shaped lid, packed with coins and folded paper money. Empty set: no character in the picture. No text, no letters, no signs with writing.
```

**Fabrication par retouche, pas par génération.**
1. Copier `episodes/01_la_bague/decors/appart.png` dans un fichier de travail.
2. Le retoucher (image de référence : ce PNG) avec le prompt ci-dessous.
3. Enregistrer le résultat sous `episodes/02_la_metamorphose/decors/appart.png`.

Le prompt « décor vide » ci-dessus ne sert qu'en dernier recours. Prompt de retouche :

```text
Same image, same room, same lighting, same colors and same framing. Only add, on the wooden coffee table in the foreground, a big plain unlabeled red glass jar shaped like a cherry, with a green stem-shaped lid, packed with coins and folded paper money. The jar is sharp and clearly visible, at about two thirds of the image height. No text, no label, no people.
```

### C.5 `cuisine` · la cuisine de Mamie Prune

| Élément | Contenu |
|---|---|
| Lieu | La petite cuisine à l'ancienne de Mamie Prune (décor de l'ép. 1). Cerise dort chez elle depuis la rupture. |
| Moment | Nuit, pluie à la fenêtre. |
| Objets repères | 1. papier peint fleuri ; 2. casseroles en cuivre suspendues ; 3. vieille cuisinière ; 4. table ronde à nappe à carreaux et théière ; 5. fenêtre ruisselante. |
| Lumière | Chaude : la suspension jaune. Froide : le bleu de la pluie à la fenêtre. |
| Couleurs | bois miel, rose des fleurs, cuivre, rouge du tapis, bleu nuit. |
| Ambiance sonore | cuisine, pluie lointaine. |
| Plans | P11, P12. |


**Repère court pour les prompts vidéo** (2 ou 3 repères, `decors.cuisine.court`) :

```text
In a warm old-fashioned grandmother's kitchen at night, floral wallpaper, copper pans, rainy window
```

**Son dans le prompt vidéo** : `kitchen room tone, soft rain`.

**Prompt d'image du décor vide, 9:16** (texte exact envoyé par `produire.py --only decors`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. A small warm old-fashioned grandmother's kitchen at night: wooden cupboards, floral wallpaper, copper pans hanging, a pot on an old stove, a round table with a checkered tablecloth and a teapot, a warm yellow ceiling lamp, a window with rain outside. Empty set: no character in the picture. No text, no letters, no signs with writing.
```

**Copie, pas de génération :** `episodes/01_la_bague/decors/cuisine.png` vers `episodes/02_la_metamorphose/decors/cuisine.png`. Son papier peint fleuri fait le raccord avec le décor `porte`.

### C.6 `porte` · la porte de Mamie, vue du palier

| Élément | Contenu |
|---|---|
| Lieu | La porte d'entrée de Mamie, ouverte, vue depuis le palier ; derrière, sa petite entrée. |
| Moment | Nuit. |
| Objets repères | 1. porte en bois ouverte ; 2. papier peint fleuri de l'entrée ; 3. portemanteau avec un châle beige tricoté ; 4. étagère avec une plante ; 5. petite lampe chaude. |
| Lumière | La lampe chaude de l'entrée éclaire Cerise de face ; le palier est plus sombre. |
| Couleurs | bois, rose fleuri, beige, ambre. |
| Ambiance sonore | appartement calme, horloge. |
| Plans | P13, P15. |


**Repère court pour les prompts vidéo** (2 ou 3 repères, `decors.porte.court`) :

```text
In an open wooden front door at night, a warm hall with floral wallpaper behind
```

**Son dans le prompt vidéo** : `quiet hallway, ticking clock`.

**Prompt d'image du décor vide, 9:16** (texte exact envoyé par `produire.py --only decors`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. An open wooden apartment front door at night seen from the landing: inside, a small warm entrance hall with floral wallpaper, a coat rack with a knitted beige shawl hanging on it, a small shelf with a plant and a warm lamp. The doorway itself is empty. No mirrors, no paintings, no writing anywhere. Empty set: no character in the picture. No text, no letters, no signs with writing.
```

Ni numéro de porte, ni plaque, ni miroir dans l'entrée.

### C.7 `palier` · le palier, vu de chez Mamie

| Élément | Contenu |
|---|---|
| Lieu | Le palier d'un immeuble haussmannien, vu depuis la porte ouverte de Mamie : c'est le contre-champ de `porte`. |
| Moment | Nuit. |
| Objets repères | 1. escalier en bois usé ; 2. rampe en fer forgé courbe ; 3. carrelage noir et blanc ; 4. applique en laiton chaude ; 5. paillasson. |
| Lumière | Ambrée : l'applique. Des ombres bleues douces. |
| Couleurs | crème, noir et blanc, ambre, bois. |
| Ambiance sonore | cage d'escalier la nuit, minuterie. |
| Plans | P14, P16, P17, P18. |


**Repère court pour les prompts vidéo** (2 ou 3 repères, `decors.palier.court`) :

```text
On an old Paris stairwell landing at night, wrought-iron banister, warm brass lamp
```

**Son dans le prompt vidéo** : `echoing stairwell at night`.

**Prompt d'image du décor vide, 9:16** (texte exact envoyé par `produire.py --only decors`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. The landing of an old Paris Haussmann apartment building at night, seen from inside an open apartment doorway: a worn wooden staircase with a curved wrought-iron banister, a black and white tiled floor, a warm brass wall lamp, cream walls with moldings, a doormat. Warm amber light and soft blue shadows. The landing is empty, no writing anywhere. Empty set: no character in the picture. No text, no letters, no signs with writing.
```

Derrière Citron, un mur crème et la rampe : aucun cadre, aucun miroir. Pour les apartés (P17, P18), l'axe reste le même : c'est Citron qui se tourne vers la caméra.

### C.8 `quais` · les quais de Seine à l'aube

| Élément | Contenu |
|---|---|
| Lieu | Les quais de Seine en pierre : le terrain d'entraînement de Cerise et Kiwi, loin de la salle de Citron (course, puis coups dans les pattes d'ours). |
| Moment | Lever du soleil : le jour 1 (« Jour un »), puis les matins d'entraînement. |
| Objets repères | 1. pavés mouillés ; 2. platanes ; 3. pont de pierre ; 4. immeubles haussmanniens dans la brume ; 5. bancs vides. |
| Lumière | Chaude : le soleil levant, rose et orange. Froide : la brume du matin. |
| Couleurs | rose, orange, gris pierre, vert des platanes, bleu pâle de l'eau. |
| Ambiance sonore | quais au petit matin, oiseaux, clapotis. |
| Plans | P19, P20, P21. |


**Repère court pour les prompts vidéo** (2 ou 3 repères, `decors.quais.court`) :

```text
On the stone quays of the Seine at sunrise, wet cobblestones, golden mist
```

**Son dans le prompt vidéo** : `riverside at dawn, birds, lapping water`.

**Prompt d'image du décor vide, 9:16** (texte exact envoyé par `produire.py --only decors`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. The stone quays of the Seine in Paris at sunrise: wet cobblestones, plane trees, a stone bridge and Haussmann buildings in a soft golden mist, warm pink and orange light, empty benches, calm water. Empty, no signs, no writing anywhere. Empty set: no character in the picture. No text, no letters, no signs with writing.
```

Ni péniche portant un nom, ni panneau, ni plaque de rue. Le matin est doux : ni buée ni souffle visible, puisque
Kiwi est torse nu sous sa veste ouverte. Au P21, ni pattes d'ours, ni main de Kiwi dans le cadre : il est hors champ, à droite.

## D. Plan par plan

**Comment lire une fiche.**
- **Le tableau** est la fiche de tournage, en français.
- **L'image clé** se compose en image fixe :
  - image 1 = le décor ;
  - image 2 = la fiche de la tenue ;
  - un seul personnage ajouté par passe ;
  - puis, si c'est indiqué, le recadrage en gros plan (`gp`) ou en plan rapproché (`pm`).
- **Le prompt vidéo** anime l'image clé. C'est un seul paragraphe au présent :
  - style en tête ;
  - caméra fixe ;
  - décor réduit à ses repères ;
  - bloc personnage ;
  - geste ;
  - réplique en segments ;
  - bloc lèvres ;
  - son à la fin.
- **La variante « animée sur notre voix »** sert quand le clip est animé directement sur le fichier de voix clonée
  (LTX-2 TURBO, mode audio). La réplique est retirée : c'est la voix fournie qui dicte les mots.
- **Le champ négatif** reprend la base (§ B.1), plus les interdits propres au plan.

**Les règles de génération, pour tous les plans :**
- **La durée :** 4 s au minimum chez Agnes, 4 à 5 s pour LTX. Le montage coupe autour de la réplique, que whisper
  repère. Les durées des fiches sont des durées à l'écran, **estimées** : avant de générer les clips, elles sont
  remplacées par la parole mesurée de notre voix + 0,4 s (Annexe, étape 5).
- **Les moteurs, dans l'ordre :** LTX-2.3, puis LTX-2 TURBO (animé sur notre voix), puis Agnes 2.5-flash.
- **Le contrôle :** on garde la prise la mieux reconnue par whisper (similarité d'au moins 0,8), sans image ratée
  au juge. Les faux sous-titres sont floutés au montage.
- **Les voix finales sont nos clones,** générées **avant** les clips et posées après coup. Les lèvres sont recalées
  (`caler.py`). La voix dite par le moteur ne sert qu'au calage. Avec LTX-2 TURBO, le clip est animé directement sur
  notre fichier de voix, qui doit donc exister avant.

### Scène A · La salle de sport, fin d'après-midi (0,0–20,3 s)

#### Plan 1 · La gamelle · 0,0–2,4 s (2,4 s)

| Champ | Consigne |
|---|---|
| Décor | `salle_entree` (entrée de la salle, foule floue), **retouché avec la bande en amorce** : `decors/salle_entree_amorce_p1.png` |
| Personnage, tenue | Cerise, `cerise` ; **muet à l'image**. L'« avant » se lit au premier coup d'œil : stylo-bille derrière l'oreille, petit carnet de commandes dans la poche du tablier, épaules légèrement voûtées. |
| Cadrage | Plan en pied, caméra à hauteur de poitrine. Sans contre-plongée ; contre-jour doré, figurants flous aux bords du cadre ; elle regarde hors champ vers la droite, la tête dans la moitié haute. **Version cible (4 essais au plus) :** au premier plan, flous, de dos et sans visage, trois costauds aux couleurs de la bande (jaune citron, brun coco, bleu indigo), sur les bords gauche et droit à mi-hauteur. Recadrage : aucun (on garde le cadre de l'image clé). |
| Caméra | fixe pendant toute la génération (locked-off). Aucun effet : ce cadre doit pouvoir être comparé au P22. |
| Geste avant la réplique | Juste passé les portes, elle tend à deux mains la gamelle cerise, grand sourire plein d'espoir ; quand la moquerie tombe, le sourire vacille. Au premier plan, les trois silhouettes floues se penchent l'une vers l'autre et rient, de dos. |
| Réplique | aucune (plan muet). **Voix hors champ :** Coco (profil `coco`) : « Oh, Citron ! Ta cantinière est là ! » (6 mots, environ 2,0 s de voix), posée dès 0,0 s ; criée de loin, rauque et hilare, « cantinière » appuyé. Sous-titres tirés de la voix clonée. |
| Émotion | espoir, puis malaise |
| Son dans le clip | `gym hall murmurs, distant street`, pas de musique. |
| Bruitages (montage) | Rires de la bande (3 ou 4 voix d'hommes, hors champ) sous la voix off, de 0,3 s à la fin du plan. |
| Incrustation de montage | Accroche **« IL L'A RENIÉE DEVANT SES POTES 💔 »** en haut, de 0 à 3 s ; badge **« LA MÉTAMORPHOSE · PARTIE 1 »** en haut à gauche, tout l'épisode ; sous-titres de la voix off. |
| Musique (version complète) | `tension` démarre à 0,0 s, baissée sous la voix. |
| Transition vers la suite | Coupe franche sur Citron (contre-champ). |
| Dernière image | Cerise, sourire vacillant, la gamelle encore tendue vers la droite, entre les dos flous de la bande. |

**Pourquoi l'amorce est la version cible (correction du chef).** 12 accroches sur 13 du corpus montrent les
oppresseurs dès la première image. Sans eux, une serveuse souriante qui tend sa gamelle ne dit pas l'injustice sans
le son. Avec trois dos musclés qui rient au premier plan, le rapport de force se lit muet. On retouche d'abord le
décor (une seule passe), puis on ajoute Cerise comme d'habitude. **Repli :** le P1 sans amorce, plus bas, si aucun
des 4 essais ne passe le § F.2 (silhouette nette, visage visible, visage en double).

**À savoir pour la chaîne :** `make_image` charge `decors/<decor>.png`, ici `salle_entree.png`. Pour la version
cible, il doit prendre le décor retouché, premier fichier de `prompts.references` (voir l'annexe), sinon on compose
l'image clé à la main avec les prompts ci-dessous. Le `cadre` du plan, que `make_image` envoie, est déjà celui de la
version cible.

**Cadre de la version cible** (`cadre`, le texte que `make_image` envoie avec le style et le bloc `cerise`) :

```text
Eye-level full-body shot, camera at chest height, she stands alone, a ballpoint pen tucked behind her ear, a small order notepad in her apron pocket, shoulders slightly hunched, holding out a small glossy red cherry-shaped lunch box with a short green stem handle in both hands toward someone off-screen to the right, a big hopeful smile; three blurred muscular figures seen from behind stay out of focus at the left and right edges, at mid-height, their faces never visible.
```

**1. Retouche du décor** (référence : `decors/salle_entree.png` ; sortie : `decors/salle_entree_amorce_p1.png`) :

```text
Same image, same gym entrance, same lighting, same colors and same framing. Only add, in the blurred foreground, two hugely muscular young men at the left edge of the frame and one at the right edge, at mid-height, seen from behind and out of focus, facing the open doors: one with bright lemon-yellow skin and slicked-back golden hair, one with warm tan-brown fibrous skin and a short spiky tuft of coconut fibers on his head, one with deep indigo-blue matte skin and a navy-blue quiff. Their faces are not visible; they lean toward each other, shoulders shaking with laughter. The doorway and the center of the frame stay empty, and nothing is in the bottom fifth of the image. No text, no letters.
```

**2. Image clé** (références : image 1 = `decors/salle_entree_amorce_p1.png`, image 2 = `identite/cerise.png`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Eye-level full-body shot, camera at chest height, vertical 9:16 composition. Inside the open steel doors of a loft gym, golden backlight, blurred gym-goers at the edges, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing a tight white deep V-neck crop top, a tiny mustard-yellow waitress apron and tight ripped blue jeans, with an adult 25-year-old face stands alone, a ballpoint pen tucked behind her ear, a small order notepad in her apron pocket, shoulders slightly hunched, holding out a small glossy red cherry-shaped lunch box with a short green stem handle in both hands toward someone off-screen to the right, a big hopeful smile. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus; in the blurred foreground, three muscular figures seen from behind at the left and right edges, at mid-height, stay out of focus, their faces never visible. No text, no letters, no logos, no subtitles.
```

**3. Prompt vidéo** (180 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Eye-level full-body shot, camera at chest height, on a locked-off static camera; the framing never changes. Inside the open steel doors of a loft gym, golden backlight, blurred gym-goers at the edges, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing a tight white deep V-neck crop top, a tiny mustard-yellow waitress apron and tight ripped blue jeans, with an adult 25-year-old face stands alone, a ballpoint pen tucked behind her ear, a small order notepad in her apron pocket, shoulders slightly hunched. She holds out a small glossy red cherry-shaped lunch box with a short green stem handle toward the right; her hopeful smile falters. Blurred figures seen from behind laugh at the edges. She does not speak and her lips stay closed. No one speaks. Audio: gym hall murmurs, distant street, no music.
```

**Variante animée sur notre voix** : sans objet (plan muet) ; la voix hors champ se pose au montage, les lèvres restent fermées.

**4. Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, sharp faces in the crowd, mirror, poster, banner, screen, numbers on weights, faces on the foreground figures, foreground figures turning around, sharp foreground figures
```

**Rime visuelle :** ce cadre est repris à l'identique au P22. L'image clé validée du P1 sert de modèle de composition pour celle du P22 (même décor, même axe, caméra à hauteur de poitrine) ; avec l'amorce validée ici, le P22 teste d'abord sa propre variante d'amorce. Le plan en pied reste à hauteur d'œil : jamais de contre-plongée sur la tenue (règle physique).

##### Repli · le P1 sans amorce (`prompts.repli_sans_amorce`)

Même plan, sans les trois silhouettes. Le stylo, le carnet et les épaules voûtées restent.

**Cadre** (à mettre dans `cadre` si on bascule sur le repli : c'est lui que `make_image` envoie) :

```text
Eye-level full-body shot, camera at chest height, she stands alone, a ballpoint pen tucked behind her ear, a small order notepad in her apron pocket, shoulders slightly hunched, holding out a small glossy red cherry-shaped lunch box with a short green stem handle in both hands toward someone off-screen to the right, a big hopeful smile.
```

**Image clé** (références : image 1 = `decors/salle_entree.png`, image 2 = `identite/cerise.png`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Eye-level full-body shot, camera at chest height, vertical 9:16 composition. Inside the open steel doors of a loft gym, golden backlight, blurred gym-goers at the edges, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing a tight white deep V-neck crop top, a tiny mustard-yellow waitress apron and tight ripped blue jeans, with an adult 25-year-old face stands alone, a ballpoint pen tucked behind her ear, a small order notepad in her apron pocket, shoulders slightly hunched, holding out a small glossy red cherry-shaped lunch box with a short green stem handle in both hands toward someone off-screen to the right, a big hopeful smile. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus, only a few small blurred gym-goers far away at the edges. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (177 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Eye-level full-body shot, camera at chest height, on a locked-off static camera; the framing never changes. Inside the open steel doors of a loft gym, golden backlight, blurred gym-goers at the edges, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing a tight white deep V-neck crop top, a tiny mustard-yellow waitress apron and tight ripped blue jeans, with an adult 25-year-old face stands alone, a ballpoint pen tucked behind her ear, a small order notepad in her apron pocket, shoulders slightly hunched. She holds out a small glossy red cherry-shaped lunch box with a short green stem handle in both hands toward the right, smiling with hope; then her smile falters. She does not speak and her lips stay closed. No one speaks. Audio: gym hall murmurs, distant street, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, sharp faces in the crowd, mirror, poster, banner, screen, numbers on weights
```

#### Plan 2 · Il la renie · 2,4–5,4 s (3,0 s)

| Champ | Consigne |
|---|---|
| Décor | `salle_rack` (salle de sport, côté de la bande) |
| Personnage, tenue | Citron, `citron_salle` |
| Cadrage | Plan rapproché taille. Regard hors champ vers la gauche (vers Cerise). Fond : briques et racks, aucun miroir. Recadrage : `pm`. |
| Caméra | fixe pendant toute la génération (locked-off). Au montage : zoom avant progressif 1,0 → 1,15 sur tout le plan. |
| Geste avant la réplique | Un shaker noir contre le torse, il ricane et la désigne d'un coup de menton (hors champ, à gauche). |
| Réplique | « Ma copine ? Nan… Juste la serveuse du café. » (8 mots) |
| Segments et jeu | « Ma copine ? » → *[He laughs and shakes his head]* → « Nan… Juste la serveuse du café. » |
| Consigne de voix | Profil Voicebox `citron`. Grave, posé, frimeur ; petit rire de mépris avant « Nan… » ; « serveuse » appuyé. |
| Émotion | mépris, frime |
| Son dans le clip | `gym ambiance, distant clanking weights`, `a short scornful laugh`, pas de musique. |
| Bruitages (montage) | Rires de la bande, bas, sous la fin de la réplique. |
| Incrustation de montage | — |
| Musique (version complète) | `tension` continue. |
| Transition vers la suite | Coupe franche. |
| Dernière image | Citron, menton levé, sourire de mépris, regard hors champ à gauche. |


**Image clé** (références : image 1 = `decors/salle_rack.png`, image 2 = `identite/citron_salle.png`, puis recadrage `pm`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up, vertical 9:16 composition. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black sleeveless gym hoodie on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone, hugging a plain matte black protein shaker against his chest, chin raised, looking off-screen to the left with a scornful smirk. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (177 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black sleeveless gym hoodie on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone. He hugs a plain matte black protein shaker against his chest and smirks toward the left. He speaks in French, in a deep, smooth, confident young man's voice, arrogant, mocking and showing off, "Ma copine ?" He laughs and shakes his head, "Nan… Juste la serveuse du café." Only he speaks, his lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: gym ambiance, distant clanking weights, a short scornful laugh, no music.
```

**Variante animée sur notre voix** (LTX-2 TURBO, mode audio ; réplique retirée, 161 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black sleeveless gym hoodie on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone. He hugs a plain matte black protein shaker against his chest and smirks toward the left. He speaks in French, mocking and showing off; his lips move in sync with the provided voice, and in the pause he laughs and shakes his head. Only he speaks. The camera holds the frame. Audio: gym ambiance, distant clanking weights, a short scornful laugh, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, mirror, poster, banner, screen, numbers on weights
```

#### Plan 3 · La meute · 5,4–8,1 s (2,7 s)

| Champ | Consigne |
|---|---|
| Décor | `salle_rack` (salle de sport, côté de la bande) |
| Personnage, tenue | Myrtille, `myrtille` |
| Cadrage | Plan rapproché taille. Regard hors champ vers la gauche. Recadrage : `pm`. |
| Caméra | fixe pendant toute la génération (locked-off). Aucun effet au montage. |
| Geste avant la réplique | Adossé à un rack, il éclate de rire, puis pointe l'index hors champ vers la gauche. |
| Réplique | « Hé, serveuse ! Les cuisines, c'est en face ! » (7 mots) |
| Segments et jeu | « Hé, serveuse ! » → *[He bursts out laughing and points to the left]* → « Les cuisines, c'est en face ! » |
| Consigne de voix | Profil Voicebox `myrtille`. Nasal, hilare, lancé pour toute la salle ; vrai éclat de rire entre les deux phrases. |
| Émotion | moquerie hilare |
| Son dans le clip | `gym ambiance, distant clanking weights`, `his loud laughter`, pas de musique. |
| Bruitages (montage) | Rires de la bande sur tout le plan. |
| Incrustation de montage | — |
| Musique (version complète) | `tension` continue. |
| Transition vers la suite | Coupe franche sur Cerise. |
| Dernière image | Myrtille plié de rire, l'index encore pointé vers la gauche. |


**Image clé** (références : image 1 = `decors/salle_rack.png`, image 2 = `identite/myrtille.png`, puis recadrage `pm`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up, vertical 9:16 composition. By black squat racks on a red brick wall, warm golden light from the left, a tall muscular handsome young man with deep indigo-blue matte skin with a soft dusty bloom like a blueberry, a styled navy-blue quiff and a teasing smirk, wearing a light-grey sleeveless gym hoodie with the hood down and big white headphones around his neck, with an adult 26-year-old face stands alone, leaning back against a black squat rack, laughing, one hand on his white headphones, looking off-screen to the left. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (174 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. By black squat racks on a red brick wall, warm golden light from the left, a tall muscular handsome young man with deep indigo-blue matte skin with a soft dusty bloom like a blueberry, a styled navy-blue quiff and a teasing smirk, wearing a light-grey sleeveless gym hoodie with the hood down and big white headphones around his neck, with an adult 26-year-old face stands alone. He leans on a squat rack, laughing. He speaks in French, in a nasal, teasing, slightly high-pitched young man's voice, loud and gleeful, "Hé, serveuse !" He bursts out laughing and points to the left, "Les cuisines, c'est en face !" Only he speaks, his lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: gym ambiance, distant clanking weights, his loud laughter, no music.
```

**Variante animée sur notre voix** (LTX-2 TURBO, mode audio ; réplique retirée, 159 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. By black squat racks on a red brick wall, warm golden light from the left, a tall muscular handsome young man with deep indigo-blue matte skin with a soft dusty bloom like a blueberry, a styled navy-blue quiff and a teasing smirk, wearing a light-grey sleeveless gym hoodie with the hood down and big white headphones around his neck, with an adult 26-year-old face stands alone. He leans on a squat rack, laughing. He speaks in French, loud and gleeful; his lips move in sync with the provided voice, and in the pause he bursts out laughing and points to the left. Only he speaks. The camera holds the frame. Audio: gym ambiance, distant clanking weights, his loud laughter, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, mirror, poster, banner, screen, numbers on weights
```

#### Plan 4 · Réaction n° 1 · 8,1–9,6 s (1,5 s)

| Champ | Consigne |
|---|---|
| Décor | `salle` (salle de sport, côté Cerise) |
| Personnage, tenue | Cerise, `cerise`, avec stylo-bille derrière l'oreille, carnet dans la poche du tablier (hors cadre en gros plan) et épaules un peu voûtées ; **muet à l'image** |
| Cadrage | Gros plan, visage et épaules. Regard hors champ vers la droite. Fond : briques et grandes fenêtres floues. Recadrage : `gp`. |
| Caméra | fixe pendant toute la génération (locked-off). Aucun effet au montage. |
| Geste avant la réplique | **Muet.** Son sourire se brise ; elle serre la gamelle contre elle, les yeux brillants, toujours tournée vers la droite. |
| Réplique | aucune (plan muet) |
| Émotion | humiliation |
| Son dans le clip | `gym ambiance, distant clanking weights`, `the murmurs fading`, pas de musique. |
| Bruitages (montage) | Les rires s'éteignent en fondu sur 1 s. |
| Incrustation de montage | — |
| Musique (version complète) | `tension` continue, plus bas. |
| Transition vers la suite | Coupe franche. |
| Dernière image | Gros plan de Cerise, gamelle serrée contre elle, larmes retenues. |


**Image clé** (références : image 1 = `decors/salle.png`, image 2 = `identite/cerise.png`, puis recadrage `gp`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders, vertical 9:16 composition. In a sunlit loft gym at golden hour, red brick and arched windows blurred behind, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing a tight white deep V-neck crop top, a tiny mustard-yellow waitress apron and tight ripped blue jeans, with an adult 25-year-old face stands alone, a ballpoint pen tucked behind her ear, a small order notepad in her apron pocket, shoulders slightly hunched, hugging a small glossy red cherry-shaped lunch box with a short green stem handle against her chest, her smile breaking, eyes glistening, looking off-screen to the right. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (169 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders on a locked-off static camera; the framing never changes. In a sunlit loft gym at golden hour, red brick and arched windows blurred behind, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing a tight white deep V-neck crop top, a tiny mustard-yellow waitress apron and tight ripped blue jeans, with an adult 25-year-old face stands alone, a ballpoint pen tucked behind her ear, shoulders slightly hunched. Her hopeful smile breaks; she slowly hugs a small glossy red cherry-shaped lunch box with a short green stem handle against her chest, eyes glistening with held-back tears. She does not speak and her lips stay closed. No one speaks. Audio: gym ambiance, distant clanking weights, the murmurs fading, no music.
```

**Variante animée sur notre voix** : sans objet (plan muet).

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, mirror, poster, banner, screen, numbers on weights
```

#### Plan 5 · L'hypocrite · 9,6–12,3 s (2,7 s)

| Champ | Consigne |
|---|---|
| Décor | `salle_rack` (salle de sport, côté de la bande) |
| Personnage, tenue | Citron, `citron_salle` |
| Cadrage | Gros plan, visage et épaules. Regard hors champ vers la gauche. Recadrage : `gp`. |
| Caméra | fixe pendant toute la génération (locked-off). Aucun effet au montage. |
| Geste avant la réplique | Il se penche vers la gauche (vers elle), jette un coup d'œil par-dessus son épaule, sourire mielleux forcé, et baisse la voix. |
| Réplique | « Mon cœur… Enlève ce tablier. Tu m'affiches. » (7 mots) |
| Segments et jeu | « Mon cœur… » → *[He forces a sweet smile]* → « Enlève ce tablier. » → *[He glances back again]* → « Tu m'affiches. » |
| Consigne de voix | Profil Voicebox `citron`. Voix baissée, mielleuse, fausse ; « Tu m'affiches. » presque entre les dents. |
| Émotion | hypocrisie mielleuse |
| Son dans le clip | `gym ambiance, distant clanking weights`, pas de musique. |
| Bruitages (montage) | — |
| Incrustation de montage | — |
| Musique (version complète) | `tension`, baissée de 3 dB. |
| Transition vers la suite | Coupe franche. |
| Dernière image | Citron, sourire forcé, les yeux qui guettent par-dessus l'épaule. |


**Image clé** (références : image 1 = `decors/salle_rack.png`, image 2 = `identite/citron_salle.png`, puis recadrage `gp`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders, vertical 9:16 composition. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black sleeveless gym hoodie on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone, leaning slightly toward the left of the frame and glancing over his shoulder, a forced sweet smile. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (170 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders on a locked-off static camera; the framing never changes. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black sleeveless gym hoodie on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone. He leans toward the left and glances quickly over his shoulder. He speaks in French, in a deep, smooth, confident young man's voice, arrogant, low and falsely sweet, "Mon cœur…" He forces a sweet smile, "Enlève ce tablier." He glances back again, "Tu m'affiches." Only he speaks, his lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: gym ambiance, distant clanking weights, no music.
```

**Variante animée sur notre voix** (LTX-2 TURBO, mode audio ; réplique retirée, 155 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders on a locked-off static camera; the framing never changes. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black sleeveless gym hoodie on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone. He leans toward the left and glances quickly over his shoulder. He speaks in French, low and falsely sweet; his lips move in sync with the provided voice, and in the pauses he forces a sweet smile, then glances back again. Only he speaks. The camera holds the frame. Audio: gym ambiance, distant clanking weights, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, mirror, poster, banner, screen, numbers on weights
```

#### Plan 6 · Elle le quitte · 12,3–15,1 s (2,8 s)

| Champ | Consigne |
|---|---|
| Décor | `salle` (salle de sport, côté Cerise) |
| Personnage, tenue | Cerise, `cerise`, avec stylo-bille derrière l'oreille, carnet dans la poche du tablier (hors cadre en gros plan) et épaules un peu voûtées |
| Cadrage | Gros plan, visage et épaules. Regard hors champ vers la droite. Recadrage : `gp`. |
| Caméra | fixe pendant toute la génération (locked-off). Au montage : coup de zoom 1,0 → 1,2 sur « te quitte ». |
| Geste avant la réplique | Les larmes montent ; puis sa mâchoire se serre et elle se redresse. |
| Réplique | « Juste la serveuse ? La serveuse te quitte, Citron. » (8 mots) |
| Segments et jeu | « Juste la serveuse ? » → *[Her jaw tightens and she straightens up]* → « La serveuse te quitte, Citron. » |
| Consigne de voix | Profil Voicebox `cerise`. Tremblante sur « Juste la serveuse ? », puis ferme et posée ; « te quitte » net. |
| Émotion | blessure, puis fermeté |
| Son dans le clip | `gym ambiance, distant clanking weights`, pas de musique. |
| Bruitages (montage) | — |
| Incrustation de montage | — |
| Musique (version complète) | `tension`, **coupée 0,3 s après « quitte »**. |
| Transition vers la suite | Coupe franche, dans le silence. |
| Dernière image | Cerise redressée, mâchoire serrée, une larme retenue. |


**Image clé** (références : image 1 = `decors/salle.png`, image 2 = `identite/cerise.png`, puis recadrage `gp`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders, vertical 9:16 composition. In a sunlit loft gym at golden hour, red brick and arched windows blurred behind, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing a tight white deep V-neck crop top, a tiny mustard-yellow waitress apron and tight ripped blue jeans, with an adult 25-year-old face stands alone, a ballpoint pen tucked behind her ear, a small order notepad in her apron pocket, shoulders slightly hunched, tears welling up in her eyes, looking off-screen to the right. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (180 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders on a locked-off static camera; the framing never changes. In a sunlit loft gym at golden hour, red brick and arched windows blurred behind, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing a tight white deep V-neck crop top, a tiny mustard-yellow waitress apron and tight ripped blue jeans, with an adult 25-year-old face stands alone, a ballpoint pen tucked behind her ear, shoulders slightly hunched, tears welling up. She speaks in French, in a soft, sweet young woman's voice, slightly husky, trembling, then firm, "Juste la serveuse ?" Her jaw tightens and she straightens up, "La serveuse te quitte, Citron." Only she speaks, her lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: gym ambiance, distant clanking weights, no music.
```

**Variante animée sur notre voix** (LTX-2 TURBO, mode audio ; réplique retirée, 164 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders on a locked-off static camera; the framing never changes. In a sunlit loft gym at golden hour, red brick and arched windows blurred behind, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing a tight white deep V-neck crop top, a tiny mustard-yellow waitress apron and tight ripped blue jeans, with an adult 25-year-old face stands alone, a ballpoint pen tucked behind her ear, shoulders slightly hunched, tears welling up. She speaks in French, trembling, then firm; her lips move in sync with the provided voice, and in the pause her jaw tightens and she straightens up. Only she speaks. The camera holds the frame. Audio: gym ambiance, distant clanking weights, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, mirror, poster, banner, screen, numbers on weights
```

#### Plan 7 · Il minimise · 15,1–17,5 s (2,4 s)

| Champ | Consigne |
|---|---|
| Décor | `salle_rack` (salle de sport, côté de la bande) |
| Personnage, tenue | Citron, `citron_salle` |
| Cadrage | Plan rapproché taille. Regard hors champ vers la gauche, yeux qui fuient sur les côtés. Recadrage : `pm`. |
| Caméra | fixe pendant toute la génération (locked-off). Aucun effet au montage. |
| Geste avant la réplique | Sourire figé, une main ouverte levée à hauteur de poitrine ; il regarde autour de lui, gêné. |
| Réplique | « Moins fort… Tout le monde regarde. » (6 mots) |
| Segments et jeu | « Moins fort… » → *[He glances around, embarrassed]* → « Tout le monde regarde. » |
| Consigne de voix | Profil Voicebox `citron`. Entre les dents, gêné, presque chuchoté. |
| Émotion | gêne, honte |
| Son dans le clip | `gym ambiance, distant clanking weights`, pas de musique. |
| Bruitages (montage) | — |
| Incrustation de montage | — |
| Musique (version complète) | `tension` repart (reprise de la piste). |
| Transition vers la suite | Coupe franche. |
| Dernière image | Citron, sourire figé, regard fuyant. |


**Image clé** (références : image 1 = `decors/salle_rack.png`, image 2 = `identite/citron_salle.png`, puis recadrage `pm`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up, vertical 9:16 composition. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black sleeveless gym hoodie on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone, a frozen smile, one open hand raised at chest height, eyes darting sideways. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (164 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black sleeveless gym hoodie on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone. With a frozen smile, he raises one open hand at chest height. He speaks in French, in a deep, smooth, confident young man's voice, arrogant, through clenched teeth, "Moins fort…" He glances around, embarrassed, "Tout le monde regarde." Only he speaks, his lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: gym ambiance, distant clanking weights, no music.
```

**Variante animée sur notre voix** (LTX-2 TURBO, mode audio ; réplique retirée, 150 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black sleeveless gym hoodie on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone. With a frozen smile, he raises one open hand at chest height. He speaks in French, through clenched teeth; his lips move in sync with the provided voice, and in the pause he glances around, embarrassed. Only he speaks. The camera holds the frame. Audio: gym ambiance, distant clanking weights, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, mirror, poster, banner, screen, numbers on weights
```

#### Plan 8 · Le défi daté · 17,5–20,3 s (2,8 s)

| Champ | Consigne |
|---|---|
| Décor | `salle` (salle de sport, côté Cerise) |
| Personnage, tenue | Cerise, `cerise`, avec stylo-bille derrière l'oreille, carnet dans la poche du tablier (hors cadre en gros plan) et épaules un peu voûtées |
| Cadrage | Gros plan, visage et épaules. Regard hors champ vers la droite. Recadrage : `gp`. |
| Caméra | fixe pendant toute la génération (locked-off). Au montage : zoom lent 1,0 → 1,15. |
| Geste avant la réplique | Elle relève le menton, essuie une larme du bout du doigt et plante son regard dans le sien. |
| Réplique | « Cent jours. Je reviens ici… et t'auras honte. » (8 mots) |
| Segments et jeu | « Cent jours. » → *[She narrows her eyes]* → « Je reviens ici… et t'auras honte. » |
| Consigne de voix | Profil Voicebox `cerise`. Calme, basse, détachée ; pas de cri ; « honte » posé lourd. |
| Émotion | détermination |
| Son dans le clip | `gym ambiance, distant clanking weights`, pas de musique. |
| Bruitages (montage) | Coup sourd (`boom`) sur « honte » ; whoosh automatique à l'apparition du chiffre. |
| Incrustation de montage | Chiffre **« 100 JOURS »** (jaune, gros, au centre bas) à partir du mot « jours ». |
| Musique (version complète) | `tension` continue. |
| Transition vers la suite | Coupe franche, whoosh (changement de lieu, automatique). |
| Dernière image | Cerise, regard planté vers la droite, déterminée. |


**Image clé** (références : image 1 = `decors/salle.png`, image 2 = `identite/cerise.png`, puis recadrage `gp`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders, vertical 9:16 composition. In a sunlit loft gym at golden hour, red brick and arched windows blurred behind, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing a tight white deep V-neck crop top, a tiny mustard-yellow waitress apron and tight ripped blue jeans, with an adult 25-year-old face stands alone, a ballpoint pen tucked behind her ear, a small order notepad in her apron pocket, shoulders slightly hunched, chin up, a tear on her cheek, staring off-screen to the right with determination. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (180 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders on a locked-off static camera; the framing never changes. In a sunlit loft gym at golden hour, red brick and arched windows blurred behind, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing a tight white deep V-neck crop top, a tiny mustard-yellow waitress apron and tight ripped blue jeans, with an adult 25-year-old face stands alone, a ballpoint pen tucked behind her ear, shoulders slightly hunched. She wipes a tear, lifts her chin. She speaks in French, in a soft, sweet young woman's voice, slightly husky, calm, determined, "Cent jours." She narrows her eyes, "Je reviens ici… et t'auras honte." Only she speaks, her lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: gym ambiance, distant clanking weights, no music.
```

**Variante animée sur notre voix** (LTX-2 TURBO, mode audio ; réplique retirée, 164 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders on a locked-off static camera; the framing never changes. In a sunlit loft gym at golden hour, red brick and arched windows blurred behind, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing a tight white deep V-neck crop top, a tiny mustard-yellow waitress apron and tight ripped blue jeans, with an adult 25-year-old face stands alone, a ballpoint pen tucked behind her ear, shoulders slightly hunched. She wipes a tear, lifts her chin. She speaks in French, calm, determined; her lips move in sync with the provided voice, and in the pause she narrows her eyes. Only she speaks. The camera holds the frame. Audio: gym ambiance, distant clanking weights, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, mirror, poster, banner, screen, numbers on weights
```

Le script prévoit qu'elle regarde vers la sortie en fin de plan. Le montage ne garde que 0,3 s après le dernier mot : ce geste n'est donc pas demandé au moteur. Si une prise le fait d'elle-même, la garder.

### Scène B · Premier aparté : le salon de Citron, la nuit (20,3–25,7 s)

#### Plan 9 · Premier aparté · 20,3–23,3 s (3,0 s)

| Champ | Consigne |
|---|---|
| Décor | `appart` (salon de Citron, pot à pourboires) |
| Personnage, tenue | Citron, `citron` |
| Cadrage | Plan moyen. **Face caméra (aparté).** Le pot cerise est net au premier plan, sur la table basse, entre 60 et 78 % de la hauteur (au-dessus de la bande du bas). Recadrage : aucun (on garde le cadre de l'image clé). |
| Caméra | fixe pendant toute la génération (locked-off). Aucun effet au montage. |
| Geste avant la réplique | Il ricane devant son téléphone (écran de dos), puis lève les yeux vers nous. |
| Réplique | « Sans moi, Cerise ? Tu tiendras pas une semaine ! » (8 mots). Elle dit enfin ce qu'elle ne tiendra pas : sans lui. Le P18 la retournera (« Sans ses pourboires… ») : c'est lui qui ne tient pas sans elle. |
| Segments et jeu | « Sans moi, Cerise ? » → *[He laughs]* → « Tu tiendras pas une semaine ! » |
| Consigne de voix | Profil Voicebox `citron`. Moqueur, détendu, adressé au public ; il répond à Cerise absente, comme si elle était devant lui. |
| Émotion | mépris amusé |
| Son dans le clip | `quiet apartment at night`, `a mocking laugh`, pas de musique. |
| Bruitages (montage) | — |
| Incrustation de montage | — |
| Musique (version complète) | `tension` continue. |
| Transition vers la suite | Coupe franche (même décor, plus serré). |
| Dernière image | Citron, sourire suffisant face caméra ; le pot cerise net devant lui. |


**Image clé** (références : image 1 = `decors/appart.png`, image 2 = `identite/citron.png`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium shot, vertical 9:16 composition. In a cozy Paris living room at night, warm lamp light, blue city window, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black leather jacket on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble sits alone on a grey sofa, holding a smartphone with its screen turned away from the camera, smirking; in the sharp foreground on the coffee table stands a big plain unlabeled red glass jar shaped like a cherry, with a green stem-shaped lid, packed with coins and folded paper money. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (168 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium shot on a locked-off static camera; the framing never changes. In a cozy Paris living room at night, warm lamp light, blue city window, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black leather jacket on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble sits alone on a grey sofa. The cherry jar stays sharp on the table. He sneers at his phone, then looks into the lens. He speaks in French, in a deep, smooth, confident young man's voice, arrogant, contemptuous, "Sans moi, Cerise ?" He laughs, "Tu tiendras pas une semaine !" Only he speaks, his lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: quiet apartment at night, a mocking laugh, no music.
```

**Variante animée sur notre voix** (LTX-2 TURBO, mode audio ; réplique retirée, 152 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium shot on a locked-off static camera; the framing never changes. In a cozy Paris living room at night, warm lamp light, blue city window, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black leather jacket on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble sits alone on a grey sofa. The cherry jar stays sharp on the table. He sneers at his phone, then looks into the lens. He speaks in French, contemptuous; his lips move in sync with the provided voice, and in the pause he laughs. Only he speaks. The camera holds the frame. Audio: quiet apartment at night, a mocking laugh, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, readable phone screen, label on the jar
```

**L'indice caché :** le pot ne porte ni étiquette ni texte. Personne n'en parle : seuls les spectateurs attentifs le remarquent.

#### Plan 10 · La menace · 23,3–25,7 s (2,4 s)

| Champ | Consigne |
|---|---|
| Décor | `appart` (salon de Citron, pot à pourboires) |
| Personnage, tenue | Citron, `citron` |
| Cadrage | Plan rapproché taille. **Face caméra (aparté).** Le pot reste visible en bas du cadre, au-dessus de la bande des sous-titres. Recadrage : `pm`. |
| Caméra | fixe pendant toute la génération (locked-off). Au montage : coup de zoom 1,0 → 1,2 sur « partout ». |
| Geste avant la réplique | Penché vers la caméra, il pose deux doigts sur le couvercle du pot cerise, sourire mauvais. |
| Réplique | « Et pour commencer… je t'affiche partout. » (6 mots) |
| Segments et jeu | « Et pour commencer… » → *[He taps the jar twice]* → « je t'affiche partout. » |
| Consigne de voix | Profil Voicebox `citron`. Bas, lent, menaçant ; un sourire dans la voix ; « partout » appuyé. |
| Émotion | menace |
| Son dans le clip | `quiet apartment at night`, `two soft taps on glass`, pas de musique. |
| Bruitages (montage) | — |
| Incrustation de montage | — |
| Musique (version complète) | `tension`, **coupée net à la fin du plan**. |
| Transition vers la suite | Coupe sèche, sans musique, sur la cuisine. |
| Dernière image | Citron, deux doigts sur le pot, sourire mauvais face caméra. |


**Image clé** (références : image 1 = `decors/appart.png`, image 2 = `identite/citron.png`, puis recadrage `pm`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up, vertical 9:16 composition. In a cozy Paris living room at night, warm lamp light, blue city window, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black leather jacket on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble sits on the grey sofa, two fingers resting on the lid of a big plain unlabeled red glass jar shaped like a cherry, with a green stem-shaped lid, packed with coins and folded paper money on the coffee table, a wicked smile, looking into the lens. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (173 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. In a cozy Paris living room at night, warm lamp light, blue city window, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black leather jacket on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble sits on the grey sofa. He leans toward the camera, two fingers on the lid of the cherry-shaped jar. He speaks in French, in a deep, smooth, confident young man's voice, arrogant, low, slow and menacing, "Et pour commencer…" He taps the jar twice, "je t'affiche partout." Only he speaks, his lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: quiet apartment at night, two soft taps on glass, no music.
```

**Variante animée sur notre voix** (LTX-2 TURBO, mode audio ; réplique retirée, 159 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. In a cozy Paris living room at night, warm lamp light, blue city window, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black leather jacket on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble sits on the grey sofa. He leans toward the camera, two fingers on the lid of the cherry-shaped jar. He speaks in French, low, slow and menacing; his lips move in sync with the provided voice, and in the pause he taps the jar twice. Only he speaks. The camera holds the frame. Audio: quiet apartment at night, two soft taps on glass, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, readable phone screen, label on the jar
```

**La menace est tenue tout de suite.** « Je t'affiche partout » retourne le « Tu m'affiches » du P5 : il avait honte
d'être vu avec elle, il va la montrer à tout le monde. La vidéo du P11 (48 000 vues) en découle : Citron et Pêche
sont liés sans que personne le dise, piste de la partie 2. La réplique remplace « je te pourris la vie », qui faisait
écho au sens d'une réplique de la référence.

### Scène C · Le creux : la cuisine de Mamie Prune (25,7–33,5 s)

#### Plan 11 · 48 000 vues · 25,7–28,5 s (2,8 s)

| Champ | Consigne |
|---|---|
| Décor | `cuisine` (cuisine de Mamie) |
| Personnage, tenue | Cerise, `cerise_maison` |
| Cadrage | Plan rapproché taille. Regard hors champ vers la droite (vers Mamie). Recadrage : `pm`. |
| Caméra | fixe pendant toute la génération (locked-off). Aucun effet au montage. |
| Geste avant la réplique | Assise à la table, téléphone en main (écran de dos), les yeux rouges, la voix brisée ; elle lève les yeux vers Mamie (droite) pour la question. |
| Réplique | « Mamie… Quarante-huit mille vues. Et s'il avait raison ? » (8 mots) |
| Segments et jeu | « Mamie… Quarante-huit mille vues. » → *[She looks up to the right]* → « Et s'il avait raison ? » |
| Consigne de voix | Profil Voicebox `cerise`. Brisée, petite voix, au bord des larmes ; « vues » qui retombe. |
| Émotion | honte, doute |
| Son dans le clip | `kitchen room tone, soft rain`, pas de musique. |
| Bruitages (montage) | `ding` à l'arrivée de la notification. |
| Incrustation de montage | Notification **« peche.officielle 🍑 a publié · Quand la serveuse se trompe de salle 😂🍒 »** dès le début du plan, retirée au mot « vues » ; puis chiffre **« 48 000 VUES »** à partir de « vues ». |
| Musique (version complète) | `triste` démarre (piano). |
| Transition vers la suite | Coupe franche sur Mamie. |
| Dernière image | Cerise, yeux rouges, regard perdu vers la droite. |


**Image clé** (références : image 1 = `decors/cuisine.png`, image 2 = `identite/cerise_maison.png`, puis recadrage `pm`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up, vertical 9:16 composition. In a warm old-fashioned grandmother's kitchen at night, floral wallpaper, copper pans, rainy window, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing an oversized cream hoodie with a small embroidered red cherry and cherry-print pajama trousers, with an adult 25-year-old face sits alone at the kitchen table, holding a smartphone with its screen turned away from the camera, eyes red, looking off-screen to the right. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (176 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. In a warm old-fashioned grandmother's kitchen at night, floral wallpaper, copper pans, rainy window, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing an oversized cream hoodie with a small embroidered red cherry and cherry-print pajama trousers, with an adult 25-year-old face sits alone at the kitchen table. She holds her phone, screen turned away, eyes red. She speaks in French, in a soft, sweet young woman's voice, slightly husky, broken, close to tears, "Mamie… Quarante-huit mille vues." She looks up to the right, "Et s'il avait raison ?" Only she speaks, her lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: kitchen room tone, soft rain, no music.
```

**Variante animée sur notre voix** (LTX-2 TURBO, mode audio ; réplique retirée, 160 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. In a warm old-fashioned grandmother's kitchen at night, floral wallpaper, copper pans, rainy window, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing an oversized cream hoodie with a small embroidered red cherry and cherry-print pajama trousers, with an adult 25-year-old face sits alone at the kitchen table. She holds her phone, screen turned away, eyes red. She speaks in French, broken, close to tears; her lips move in sync with the provided voice, and in the pause she looks up to the right. Only she speaks. The camera holds the frame. Audio: kitchen room tone, soft rain, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, readable phone screen
```

#### Plan 12 · La réplique de Mamie · 28,5–33,5 s (5,0 s)

| Champ | Consigne |
|---|---|
| Décor | `cuisine` (cuisine de Mamie) |
| Personnage, tenue | Mamie Prune, `prune` |
| Cadrage | Plan rapproché taille, assise à la table de la cuisine. **Regard caméra** (Mamie parle au public). Recadrage : `pm`, comme le dit le `cadre` (« Medium close-up from the waist up ») et les prompts. |
| Caméra | fixe pendant toute la génération (locked-off). Aucun effet au montage. |
| Geste avant la réplique | Assise à la table, elle remue lentement son thé, calme et malicieuse, et regarde la caméra par-dessus ses lunettes. On frappe juste après sa réplique. Un seul geste, petit et lent : les lèvres restent faciles à caler, et le plan ne répète plus le P13 de l'ép. 1 (fourneau, thé versé). |
| Réplique | « Une cerise, ça mûrit au soleil… Pas à l'ombre d'un citron. » (11 mots) |
| Segments et jeu | « Une cerise, ça mûrit au soleil… » → *[She raises one eyebrow]* → « Pas à l'ombre d'un citron. » |
| Consigne de voix | Profil Voicebox `prune`. Voix décrite (Qwen VoiceDesign), tempo 1,25 et léger vibrato ; lente, chaude, malicieuse ; pause de 0,25 s sur « soleil… » ; dernier mot avec un sourire. La parole doit tenir en 4,6 s. |
| Émotion | sagesse piquante |
| Son dans le clip | `kitchen room tone, soft rain`, `a teacup clink`, pas de musique. |
| Bruitages (montage) | **Deux coups frappés à la porte** juste après « citron » (vers 33,3 s) ; ils débordent sur la coupe vers le P13. |
| Incrustation de montage | — |
| Musique (version complète) | `triste` continue. |
| Transition vers la suite | Coupe franche sur la porte. |
| Dernière image | Mamie, sourire malicieux, un sourcil levé, regard caméra ; les coups à la porte tombent sur la coupe. |


**Image clé** (références : image 1 = `decors/cuisine.png`, image 2 = `identite/prune.png`, puis recadrage `pm`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up, vertical 9:16 composition. In a warm old-fashioned grandmother's kitchen at night, floral wallpaper, copper pans, rainy window, a small old grandmother with deep purple wrinkled skin, white hair, small round glasses, a knitted hat, a knitted beige shawl and a floral dress, with a round deeply wrinkled face, kind mischievous eyes and a small warm smile, clearly a very old woman sits alone at the kitchen table, slowly stirring her tea, looking at the camera over her small round glasses with a mischievous look. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (177 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. In a warm old-fashioned grandmother's kitchen at night, floral wallpaper, copper pans, rainy window, a small old grandmother with deep purple wrinkled skin, white hair, small round glasses, a knitted hat, a knitted beige shawl and a floral dress, with a round deeply wrinkled face, kind mischievous eyes and a small warm smile, clearly a very old woman sits alone at the kitchen table. She slowly stirs her tea, then looks at the camera over her glasses. She speaks in French, in a crackly old woman's voice, warm and mischievous, slow and knowing, "Une cerise, ça mûrit au soleil…" She raises one eyebrow, "Pas à l'ombre d'un citron." Only she speaks, her lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: kitchen room tone, soft rain, a teacup clink, no music.
```

**Variante animée sur notre voix** (LTX-2 TURBO, mode audio ; réplique retirée, 158 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. In a warm old-fashioned grandmother's kitchen at night, floral wallpaper, copper pans, rainy window, a small old grandmother with deep purple wrinkled skin, white hair, small round glasses, a knitted hat, a knitted beige shawl and a floral dress, with a round deeply wrinkled face, kind mischievous eyes and a small warm smile, clearly a very old woman sits alone at the kitchen table. She slowly stirs her tea, then looks at the camera over her glasses. She speaks in French, slow and knowing; her lips move in sync with the provided voice, and in the pause she raises one eyebrow. Only she speaks. The camera holds the frame. Audio: kitchen room tone, soft rain, a teacup clink, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face
```

**Réplique à citer de l'épisode.** Elle annonce l'image de la revanche : le soleil, c'est l'heure dorée du défilé (P22). Le script lui fait regarder vers la porte en fin de plan : geste facultatif, car le montage coupe 0,3 s après le dernier mot ; les coups frappés font le lien.

**Durée : 5,0 s** (décision du chef), soit 4,6 s de parole pour 11 mots. La voix de Mamie mesurée à l'ép. 1 parle à 2 mots/s environ : si sa voix mesurée dépasse 4,6 s, `duree` prend la mesure + 0,4 s, et le clip se fait en LTX-2 TURBO sur notre voix (un clip de 5 s ne suffit plus).

### Scène D · La porte et les roses jaunes (33,5–43,6 s)

#### Plan 13 · Perdu, Citron ? · 33,5–36,0 s (2,5 s)

| Champ | Consigne |
|---|---|
| Décor | `porte` (porte de Mamie, vue du palier) |
| Personnage, tenue | Cerise, `cerise_maison` |
| Cadrage | Plan rapproché taille. Dans l'embrasure ; regard hors champ vers la droite (vers le palier). Recadrage : `pm`. |
| Caméra | fixe pendant toute la génération (locked-off). Aucun effet au montage. |
| Geste avant la réplique | Elle entrouvre la porte, surprise, puis croise les bras, froide. |
| Réplique | « Perdu, Citron ? La salle, c'est pas ici. » (7 mots) |
| Segments et jeu | « Perdu, Citron ? » → *[She crosses her arms]* → « La salle, c'est pas ici. » |
| Consigne de voix | Profil Voicebox `cerise`. Froide, ironique, un peu lasse. |
| Émotion | méfiance ironique |
| Son dans le clip | `quiet hallway, ticking clock`, `the creak of the door`, pas de musique. |
| Bruitages (montage) | — |
| Incrustation de montage | — |
| Musique (version complète) | `triste`, bas. |
| Transition vers la suite | Coupe franche (contre-champ sur le palier). |
| Dernière image | Cerise bras croisés dans l'embrasure, regard froid. |


**Image clé** (références : image 1 = `decors/porte.png`, image 2 = `identite/cerise_maison.png`, puis recadrage `pm`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up, vertical 9:16 composition. In an open wooden front door at night, a warm hall with floral wallpaper behind, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing an oversized cream hoodie with a small embroidered red cherry and cherry-print pajama trousers, with an adult 25-year-old face stands alone in the doorway, one hand on the edge of the half-open door, surprised, looking off-screen to the right. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (178 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. In an open wooden front door at night, a warm hall with floral wallpaper behind, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing an oversized cream hoodie with a small embroidered red cherry and cherry-print pajama trousers, with an adult 25-year-old face stands alone in the doorway. She pulls the door half open, surprised, looking to the right. She speaks in French, in a soft, sweet young woman's voice, slightly husky, cold and ironic, "Perdu, Citron ?" She crosses her arms, "La salle, c'est pas ici." Only she speaks, her lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: quiet hallway, ticking clock, the creak of the door, no music.
```

**Variante animée sur notre voix** (LTX-2 TURBO, mode audio ; réplique retirée, 163 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. In an open wooden front door at night, a warm hall with floral wallpaper behind, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing an oversized cream hoodie with a small embroidered red cherry and cherry-print pajama trousers, with an adult 25-year-old face stands alone in the doorway. She pulls the door half open, surprised, looking to the right. She speaks in French, cold and ironic; her lips move in sync with the provided voice, and in the pause she crosses her arms. Only she speaks. The camera holds the frame. Audio: quiet hallway, ticking clock, the creak of the door, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, door number, nameplate
```

#### Plan 14 · Les roses jaunes · 36,0–38,7 s (2,7 s)

| Champ | Consigne |
|---|---|
| Décor | `palier` (palier de l'immeuble) |
| Personnage, tenue | Citron, `citron` |
| Cadrage | Plan rapproché taille. Regard hors champ vers la gauche (vers la porte). Recadrage : `pm`. |
| Caméra | fixe pendant toute la génération (locked-off). Aucun effet au montage. |
| Geste avant la réplique | Il serre contre sa poitrine le gros bouquet de roses jaunes ; voix grave et douce, sourire charmeur. |
| Réplique | « Pardon, mon cœur… T'as besoin de moi. » (7 mots) |
| Segments et jeu | « Pardon, mon cœur… » → *[He tilts his head, tender]* → « T'as besoin de moi. » |
| Consigne de voix | Profil Voicebox `citron`. Grave, doux, charmeur ; « T'as besoin de moi » murmuré, possessif. Coco reprendra cette phrase au P24 : la dire avec la même mélodie. |
| Émotion | manipulation charmeuse |
| Son dans le clip | `echoing stairwell at night`, pas de musique. |
| Bruitages (montage) | Clic de la minuterie de l'escalier au début du plan (facultatif). |
| Incrustation de montage | — |
| Musique (version complète) | `triste` continue. |
| Transition vers la suite | Coupe franche. |
| Dernière image | Citron, bouquet contre la poitrine, sourire charmeur. |


**Image clé** (références : image 1 = `decors/palier.png`, image 2 = `identite/citron.png`, puis recadrage `pm`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up, vertical 9:16 composition. On an old Paris stairwell landing at night, wrought-iron banister, warm brass lamp, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black leather jacket on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone, holding a big bouquet of yellow roses wrapped in plain brown kraft paper against his chest with both arms, a charming smile, looking off-screen to the left. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (173 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. On an old Paris stairwell landing at night, wrought-iron banister, warm brass lamp, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black leather jacket on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone. He holds a big bouquet of yellow roses wrapped in plain brown kraft paper against his chest and smiles charmingly to the left. He speaks in French, in a deep, smooth, confident young man's voice, arrogant, soft and charming, "Pardon, mon cœur…" He tilts his head, tender, "T'as besoin de moi." Only he speaks, his lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: echoing stairwell at night, no music.
```

**Variante animée sur notre voix** (LTX-2 TURBO, mode audio ; réplique retirée, 158 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. On an old Paris stairwell landing at night, wrought-iron banister, warm brass lamp, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black leather jacket on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone. He holds a big bouquet of yellow roses wrapped in plain brown kraft paper against his chest and smiles charmingly to the left. He speaks in French, soft and charming; his lips move in sync with the provided voice, and in the pause he tilts his head, tender. Only he speaks. The camera holds the frame. Audio: echoing stairwell at night, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face
```

#### Plan 15 · La phrase-étendard · 38,7–42,1 s (3,4 s)

| Champ | Consigne |
|---|---|
| Décor | `porte` (porte de Mamie, vue du palier) |
| Personnage, tenue | Cerise, `cerise_maison` |
| Cadrage | Gros plan, visage et épaules. Regard hors champ vers la droite. Recadrage : `gp`. |
| Caméra | fixe pendant toute la génération (locked-off). Au montage : zoom lent 1,0 → 1,15. |
| Geste avant la réplique | Elle relève le menton, calme et ferme, la main sur le bord de la porte. |
| Réplique | « Mon tablier, c'est pas ma honte. Ma honte, c'est toi. » (10 mots) |
| Segments et jeu | « Mon tablier, c'est pas ma honte. » → *[She holds his gaze]* → « Ma honte, c'est toi. » |
| Consigne de voix | Profil Voicebox `cerise`. Calme, ferme, digne ; pas de cri ; un temps avant « Ma honte, c'est toi. » |
| Émotion | dignité |
| Son dans le clip | `quiet hallway, ticking clock`, pas de musique. |
| Bruitages (montage) | — |
| Incrustation de montage | — |
| Musique (version complète) | `triste`, **coupée sur « c'est toi »**. |
| Transition vers la suite | Coupe franche sur le palier, dans le silence. |
| Dernière image | Cerise, menton levé, regard dur, la main sur la porte. |


**Image clé** (références : image 1 = `decors/porte.png`, image 2 = `identite/cerise_maison.png`, puis recadrage `gp`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders, vertical 9:16 composition. In an open wooden front door at night, a warm hall with floral wallpaper behind, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing an oversized cream hoodie with a small embroidered red cherry and cherry-print pajama trousers, with an adult 25-year-old face stands alone in the doorway, chin raised, calm and firm, one hand on the edge of the door, looking off-screen to the right. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (177 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders on a locked-off static camera; the framing never changes. In an open wooden front door at night, a warm hall with floral wallpaper behind, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing an oversized cream hoodie with a small embroidered red cherry and cherry-print pajama trousers, with an adult 25-year-old face stands alone in the doorway. She lifts her chin, perfectly calm, one hand on the door. She speaks in French, in a soft, sweet young woman's voice, slightly husky, calm, firm and dignified, "Mon tablier, c'est pas ma honte." She holds his gaze, "Ma honte, c'est toi." Only she speaks, her lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: quiet hallway, ticking clock, no music.
```

**Variante animée sur notre voix** (LTX-2 TURBO, mode audio ; réplique retirée, 159 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders on a locked-off static camera; the framing never changes. In an open wooden front door at night, a warm hall with floral wallpaper behind, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing an oversized cream hoodie with a small embroidered red cherry and cherry-print pajama trousers, with an adult 25-year-old face stands alone in the doorway. She lifts her chin, perfectly calm, one hand on the door. She speaks in French, calm, firm and dignified; her lips move in sync with the provided voice, and in the pause she holds his gaze. Only she speaks. The camera holds the frame. Audio: quiet hallway, ticking clock, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, door number, nameplate
```

**Phrase-étendard de l'épisode.** Le script la fait reculer pour fermer la porte : on ne le demande pas au moteur (un battant qui traverse le cadre déforme l'image). La fermeture se raconte par le son et par la réaction du P16.

#### Plan 16 · Réaction n° 2 · 42,1–43,6 s (1,5 s)

| Champ | Consigne |
|---|---|
| Décor | `palier` (palier de l'immeuble) |
| Personnage, tenue | Citron, `citron` ; **muet à l'image** |
| Cadrage | Plan rapproché taille. Face à la porte, donc face à la caméra. Recadrage : `pm`. |
| Caméra | fixe pendant toute la génération (locked-off). Aucun effet au montage. |
| Geste avant la réplique | **Muet.** La porte lui claque au nez (hors champ) : il sursaute, cligne des yeux, bouche entrouverte, le bouquet contre lui. |
| Réplique | aucune (plan muet) |
| Émotion | stupeur vexée |
| Son dans le clip | `echoing stairwell at night`, `a heavy door slamming shut`, pas de musique. |
| Bruitages (montage) | **Porte qui claque** sur la première image. |
| Incrustation de montage | — |
| Musique (version complète) | Silence musical. |
| Transition vers la suite | Coupe franche. |
| Dernière image | Citron figé, bouche entrouverte, le bouquet contre lui. |


**Image clé** (références : image 1 = `decors/palier.png`, image 2 = `identite/citron.png`, puis recadrage `pm`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up, vertical 9:16 composition. On an old Paris stairwell landing at night, wrought-iron banister, warm brass lamp, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black leather jacket on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone facing the camera, holding a big bouquet of yellow roses wrapped in plain brown kraft paper against his chest, flinching, eyes blinking, mouth half open in offended disbelief. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (149 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. On an old Paris stairwell landing at night, wrought-iron banister, warm brass lamp, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black leather jacket on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone facing the camera. He holds the yellow roses to his chest; suddenly he flinches back and blinks hard, mouth falling open, as if a door just slammed in his face. He does not speak and his lips stay closed. No one speaks. Audio: echoing stairwell at night, a heavy door slamming shut, no music.
```

**Variante animée sur notre voix** : sans objet (plan muet).

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face
```

### Scène E · Deuxième aparté : le palier (43,6–50,0 s)

#### Plan 17 · Elle reviendra · 43,6–46,6 s (3,0 s)

| Champ | Consigne |
|---|---|
| Décor | `palier` (palier de l'immeuble) |
| Personnage, tenue | Citron, `citron` |
| Cadrage | Plan rapproché taille. Il fixe la porte (juste à gauche de l'objectif), puis **regarde la caméra (aparté)**. Recadrage : `pm`. |
| Caméra | fixe pendant toute la génération (locked-off). Aucun effet au montage. |
| Geste avant la réplique | Le gros bouquet de roses jaunes, dans son papier kraft brun, pend au bout de son bras ; il pointe la porte de l'index, rage contenue, puis se tourne vers nous. |
| Réplique | « La porte au nez… À moi ?! Elle reviendra. » (8 mots) |
| Segments et jeu | « La porte au nez… » → *[He points at the door]* → « À moi ?! » → *[He turns to the camera]* → « Elle reviendra. » |
| Consigne de voix | Profil Voicebox `citron`. Outré puis glacé ; « À moi ?! » plus aigu ; « Elle reviendra. » lent et sûr. |
| Émotion | orgueil blessé |
| Son dans le clip | `echoing stairwell at night`, pas de musique. |
| Bruitages (montage) | — |
| Incrustation de montage | — |
| Musique (version complète) | `tension` repart, basse et grave. |
| Transition vers la suite | Coupe franche (plus serré). |
| Dernière image | Citron fixe l'objectif, sourire froid. |


**Image clé** (références : image 1 = `decors/palier.png`, image 2 = `identite/citron.png`, puis recadrage `pm`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up, vertical 9:16 composition. On an old Paris stairwell landing at night, wrought-iron banister, warm brass lamp, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black leather jacket on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone, a big bouquet of yellow roses wrapped in plain brown kraft paper hanging upside down from one hand, glaring just left of the camera. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (180 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. On an old Paris stairwell landing at night, wrought-iron banister, warm brass lamp, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black leather jacket on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone. The big bouquet of yellow roses wrapped in plain brown kraft paper hangs from one hand; he glares just left of the camera. He speaks in French, in a deep, smooth, confident young man's voice, arrogant, outraged, then coldly smug, "La porte au nez…" He points at the door, "À moi ?!" He turns to the camera, "Elle reviendra." Only he speaks, his lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: echoing stairwell at night, no music.
```

**Variante animée sur notre voix** (LTX-2 TURBO, mode audio ; réplique retirée, 164 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. On an old Paris stairwell landing at night, wrought-iron banister, warm brass lamp, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black leather jacket on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone. The big bouquet of yellow roses wrapped in plain brown kraft paper hangs from one hand; he glares just left of the camera. He speaks in French, outraged, then coldly smug; his lips move in sync with the provided voice, and in the pauses he points at the door, then turns to the camera. Only he speaks. The camera holds the frame. Audio: echoing stairwell at night, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face
```

#### Plan 18 · L'aveu · 46,6–50,0 s (3,4 s)

| Champ | Consigne |
|---|---|
| Décor | `palier` (palier de l'immeuble) |
| Personnage, tenue | Citron, `citron` |
| Cadrage | Gros plan, visage et épaules. **Face caméra (aparté).** Recadrage : `gp`. |
| Caméra | fixe pendant toute la génération (locked-off). Au montage : coup de zoom 1,0 → 1,25 sur « ma salle ». |
| Geste avant la réplique | Il s'approche de l'objectif : il commence à voix basse et finit en criant. |
| Réplique | « Sans ses pourboires… je paie comment ma salle, moi ?! » (9 mots) |
| Segments et jeu | « Sans ses pourboires… » → *[His smile drops]* → « je paie comment ma salle, moi ?! » |
| Consigne de voix | Profil Voicebox `citron`. Commence chuchoté (confidence), finit crié ; « moi ?! » aigu et mesquin. |
| Émotion | aveu, rage mesquine |
| Son dans le clip | `echoing stairwell at night`, pas de musique. |
| Bruitages (montage) | — |
| Incrustation de montage | — |
| Musique (version complète) | `tension`, **coupure sèche** à la fin du plan. |
| Transition vers la suite | Coupe sèche, 0,1 s de silence, puis l'aube. |
| Dernière image | Très près, Citron crie, les yeux exorbités. |


**Image clé** (références : image 1 = `decors/palier.png`, image 2 = `identite/citron.png`, puis recadrage `gp`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders, vertical 9:16 composition. On an old Paris stairwell landing at night, wrought-iron banister, warm brass lamp, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black leather jacket on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone, leaning in close to the camera, looking straight into the lens, conspiratorial. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (164 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders on a locked-off static camera; the framing never changes. On an old Paris stairwell landing at night, wrought-iron banister, warm brass lamp, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black leather jacket on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone. He leans close to the camera and looks into the lens, like a confession. He speaks in French, in a deep, smooth, confident young man's voice, arrogant, whispering, then shouting, "Sans ses pourboires…" His smile drops, "je paie comment ma salle, moi ?!" Only he speaks, his lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: echoing stairwell at night, no music.
```

**Variante animée sur notre voix** (LTX-2 TURBO, mode audio ; réplique retirée, 147 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders on a locked-off static camera; the framing never changes. On an old Paris stairwell landing at night, wrought-iron banister, warm brass lamp, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black leather jacket on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone. He leans close to the camera and looks into the lens, like a confession. He speaks in French, whispering, then shouting; his lips move in sync with the provided voice, and in the pause his smile drops. Only he speaks. The camera holds the frame. Audio: echoing stairwell at night, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face
```

**L'ironie dramatique :** le public sait désormais que Citron vit des pourboires de Cerise ; elle, non. C'est le moteur de la partie 2.

### Scène F · Cent jours (50,0–57,3 s)

#### Plan 19 · Jour un · 50,0–51,7 s (1,7 s)

| Champ | Consigne |
|---|---|
| Décor | `quais` (quais de Seine à l'aube) |
| Personnage, tenue | Kiwi, `kiwi` |
| Cadrage | Plan rapproché taille. Regard hors champ vers la gauche (vers Cerise). Recadrage : `pm`. |
| Caméra | fixe pendant toute la génération (locked-off). Aucun effet au montage. |
| Geste avant la réplique | Il tape dans ses mains, grand sourire ; il montre le quai du pouce. Pas de buée : le matin est doux, et il est torse nu sous sa veste. |
| Réplique | « Jour un, Cerise ! On court ! » (5 mots) |
| Segments et jeu | « Jour un, Cerise ! » → *[He points down the quay]* → « On court ! » |
| Consigne de voix | Profil Voicebox `kiwi`. Énergique, chaleureux, accent de quartier ; sourire dans la voix. |
| Émotion | énergie, tendresse |
| Son dans le clip | `riverside at dawn, birds, lapping water`, `one hand clap`, pas de musique. |
| Bruitages (montage) | — |
| Incrustation de montage | — |
| Musique (version complète) | `revanche` démarre. |
| Transition vers la suite | Coupe franche. |
| Dernière image | Kiwi, pouce tendu vers le quai, grand sourire. |


**Image clé** (références : image 1 = `decors/quais.png`, image 2 = `identite/kiwi.png`, puis recadrage `pm`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up, vertical 9:16 composition. On the stone quays of the Seine at sunrise, wet cobblestones, golden mist, a hugely muscular handsome young man with olive-green fuzzy skin, short curly dark-brown hair, bright green eyes, wearing an open green delivery jacket on his bare muscular chest with six-pack abs, with an adult 27-year-old face and a warm smile stands alone, clapping his hands, a big grin, looking off-screen to the left. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (163 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. On the stone quays of the Seine at sunrise, wet cobblestones, golden mist, a hugely muscular handsome young man with olive-green fuzzy skin, short curly dark-brown hair, bright green eyes, wearing an open green delivery jacket on his bare muscular chest with six-pack abs, with an adult 27-year-old face and a warm smile stands alone. He claps once and grins to the left. He speaks in French, in a warm, friendly young man's voice with a slight Parisian street accent, energetic and warm, "Jour un, Cerise !" He points down the quay, "On court !" Only he speaks, his lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: riverside at dawn, birds, lapping water, one hand clap, no music.
```

**Variante animée sur notre voix** (LTX-2 TURBO, mode audio ; réplique retirée, 146 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. On the stone quays of the Seine at sunrise, wet cobblestones, golden mist, a hugely muscular handsome young man with olive-green fuzzy skin, short curly dark-brown hair, bright green eyes, wearing an open green delivery jacket on his bare muscular chest with six-pack abs, with an adult 27-year-old face and a warm smile stands alone. He claps once and grins to the left. He speaks in French, energetic and warm; his lips move in sync with the provided voice, and in the pause he points down the quay. Only he speaks. The camera holds the frame. Audio: riverside at dawn, birds, lapping water, one hand clap, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, street sign, boat name
```

#### Plan 20 · La course · 51,7–53,2 s (1,5 s)

| Champ | Consigne |
|---|---|
| Décor | `quais` (quais de Seine à l'aube) |
| Personnage, tenue | Cerise, `cerise_sport` ; **muet à l'image** |
| Cadrage | Plan moyen large. Le visage reste lisible ; pas d'insistance sur le corps (règle physique). Recadrage : aucun (on garde le cadre de l'image clé). |
| Caméra | fixe pendant toute la génération (locked-off). Aucun effet au montage. |
| Geste avant la réplique | **Muet.** Elle court vers la caméra, régulière, le regard droit devant. |
| Réplique | aucune (plan muet) |
| Émotion | effort, détermination |
| Son dans le clip | `riverside at dawn, birds, lapping water`, `running footsteps and steady breathing`, pas de musique. |
| Bruitages (montage) | — |
| Incrustation de montage | — |
| Musique (version complète) | `revanche` monte. |
| Transition vers la suite | Coupe franche, sur le mouvement. |
| Dernière image | Cerise arrive près de l'objectif, regard droit devant. |


**Image clé** (références : image 1 = `decors/quais.png`, image 2 = `identite/cerise_sport.png`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium-wide shot, vertical 9:16 composition. On the stone quays of the Seine at sunrise, wet cobblestones, golden mist, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing a white zip-up track jacket with thin cherry-red stripes over a cherry-red tank top and black leggings, with an adult 25-year-old face runs alone along the quay, toward the camera, focused. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (142 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium-wide shot on a locked-off static camera; the framing never changes. On the stone quays of the Seine at sunrise, wet cobblestones, golden mist, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing a white zip-up track jacket with thin cherry-red stripes over a cherry-red tank top and black leggings, with an adult 25-year-old face runs alone along the quay. She runs straight toward the camera at a steady pace, focused. She does not speak and her lips stay closed. No one speaks. Audio: riverside at dawn, birds, lapping water, running footsteps and steady breathing, no music.
```

**Variante animée sur notre voix** : sans objet (plan muet).

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, slow motion, camera shake, street sign
```

#### Plan 21 · Les coups · 53,2–54,7 s (1,5 s)

| Champ | Consigne |
|---|---|
| Décor | `quais` (quais de Seine à l'aube) |
| Personnage, tenue | Cerise, `cerise_sport` ; **muet à l'image** |
| Cadrage | Plan rapproché taille. Visage et buste ; regard et coups vers la droite (vers Kiwi, hors champ). Aucune main, patte d'ours ni sac dans le cadre. Recadrage : `pm`. |
| Caméra | fixe pendant toute la génération (locked-off). Aucun effet au montage. |
| Fenêtre gardée (montage) | On génère 4 s et on garde **1,5 s : les deux derniers coups, puis la garde baissée et le sourire** (`fenetre_clip` : début indicatif à 2,0 s du clip, relu sur la prise retenue pour commencer 0,1 s avant l'avant-dernier coup). |
| Geste avant la réplique | **Muet à l'image.** Elle enchaîne une série de coups rapides vers la droite, dans les pattes d'ours que Kiwi tient hors champ ; aucun contact visible. Puis elle baisse la garde, essoufflée, et sourit, fière. |
| Réplique | aucune (plan muet). **Voix hors champ :** Kiwi (profil `kiwi`) : « Plus fort, Cerise ! » (3 mots, environ 0,8 s de voix), posée à 0,2 s. **Obligatoire dès que `voix_off` est codé** : elle coupe le silence du montage d'effort. Tant que `voix_off` n'existe pas, le plan reste muet. |
| Émotion | force, fierté |
| Son dans le clip | `riverside at dawn, birds, lapping water`, `sharp breaths with each punch`, pas de musique. |
| Bruitages (montage) | Deux impacts secs (`impact`), calés sur les deux coups visibles de la fenêtre gardée (vers 0,15 et 0,45 s du plan, à relire sur la prise) : le bruit dit le contact que l'image ne montre pas. |
| Incrustation de montage | — |
| Musique (version complète) | `revanche` monte. |
| Transition vers la suite | **Flash blanc de 0,15 s et whoosh**, puis carton. |
| Dernière image | Cerise essoufflée et fière, garde baissée, sourire. |


**Image clé** (références : image 1 = `decors/quais.png`, image 2 = `identite/cerise_sport.png`, puis recadrage `pm`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up, vertical 9:16 composition. On the stone quays of the Seine at sunrise, wet cobblestones, golden mist, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing a white zip-up track jacket with thin cherry-red stripes over a cherry-red tank top and black leggings, with an adult 25-year-old face stands alone on the quay, fists raised in a boxing guard toward the right of the frame, focused, out of breath. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (172 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. On the stone quays of the Seine at sunrise, wet cobblestones, golden mist, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous wavy dark-red hair with two small cherries and a leaf clipped in it, full glossy red lips, glamorous makeup, wearing a white zip-up track jacket with thin cherry-red stripes over a cherry-red tank top and black leggings, with an adult 25-year-old face stands alone on the quay. She throws a fast combination of punches toward the right of the frame, at off-screen focus mitts; her fists never touch anything in the frame. Then she lowers her guard, out of breath, and smiles with pride. She does not speak and her lips stay closed. No one speaks. Audio: riverside at dawn, birds, lapping water, sharp breaths with each punch, no music.
```

**Variante animée sur notre voix** : sans objet (plan muet) ; la voix hors champ se pose au montage, les lèvres restent fermées.

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, visible focus mitts, punching bag, hands entering the frame, street sign
```

**Pourquoi les quais (correction du chef) :** Cerise ne peut pas s'entraîner cent jours dans la salle de Citron : la bande la verrait, ce qui tuerait la révélation et la promesse « Je reviens ici ». Elle s'entraîne donc dehors, avec Kiwi. Les pattes d'ours restent hors champ : aucun contact à générer.

#### Plan 22 · Le défilé · 54,7–57,3 s (2,6 s)

| Champ | Consigne |
|---|---|
| Décor | `salle_entree` (entrée de la salle, foule floue) |
| Personnage, tenue | Cerise, `cerise_glow` (lunettes de soleil dorées relevées dans les cheveux) et le petit sac rouge cerise au bras ; **muet à l'image** |
| Cadrage | Plan en pied, caméra à hauteur de poitrine. **Même cadre que le P1** (même décor, même axe, même hauteur, sans contre-plongée) ; contre-jour doré. Recadrage : aucun (on garde le cadre de l'image clé). |
| Caméra | fixe pendant toute la génération (locked-off). Ralenti × 1,4 au montage. |
| Geste avant la réplique | **Muet.** Elle franchit les portes et marche vers la caméra, assurée, les cheveux qui ondulent ; les sportifs flous aux bords se retournent. |
| Réplique | aucune (plan muet) |
| Émotion | assurance rayonnante |
| Son dans le clip | `gym hall murmurs, distant street`, `confident heel steps`, pas de musique. |
| Bruitages (montage) | Whoosh sur le flash ; **murmures de la foule qui montent** dès 0,3 s, en fondu d'entrée sur 1 s, pendant que les témoins se retournent ; les pas restent discrets, la musique porte. |
| Incrustation de montage | Carton **« 100 JOURS PLUS TARD »** dans le tiers haut (y ≈ 380 à 520 px, sous le badge), pendant les 1,2 premières secondes, avec flash blanc et whoosh (voir § E). Elle est encore loin, dans l'embrasure : le carton passe au-dessus de sa tête et ne masque pas la révélation. |
| Musique (version complète) | Sommet de `revanche`. |
| Transition vers la suite | Coupe franche sur Citron. |
| Dernière image | Cerise au premier plan, regard assuré vers la droite. |


**Image clé** (références : image 1 = `decors/salle_entree.png`, image 2 = `identite/cerise_glow.png`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Eye-level full-body shot, camera at chest height, vertical 9:16 composition. Inside the open steel doors of a loft gym, golden backlight, blurred gym-goers at the edges, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous dark-red hair in freshly styled glossy Hollywood waves with two small cherries and a leaf clipped in it, oversized gold-rimmed sunglasses pushed up in her hair, full glossy red lips, glamorous makeup, wearing a tailored ivory-white blazer mini dress with gold buttons and a small gold cherry pendant, with an adult 25-year-old face appears alone in the open doorway, a small structured cherry-red handbag on her arm, backlit, chin up, a calm confident look. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus, only a few small blurred gym-goers far away at the edges. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (176 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Eye-level full-body shot, camera at chest height, on a locked-off static camera; the framing never changes. Inside the open steel doors of a loft gym, golden backlight, blurred gym-goers at the edges, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous dark-red hair in freshly styled glossy Hollywood waves with two small cherries and a leaf clipped in it, oversized gold-rimmed sunglasses pushed up in her hair, full glossy red lips, glamorous makeup, wearing a tailored ivory-white blazer mini dress with gold buttons and a small gold cherry pendant, with an adult 25-year-old face appears alone in the open doorway. She walks in and straight toward the camera with slow, confident steps, chin up, her hair moving; at the edges the blurred gym-goers turn their heads toward her. She does not speak and her lips stay closed. No one speaks. Audio: gym hall murmurs, distant street, confident heel steps, no music.
```

**Variante animée sur notre voix** : sans objet (plan muet).

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, sharp faces in the crowd, mirror, poster, banner, screen, numbers on weights
```

**La métamorphose se lit sans le son :** même cadre que le P1, mais tenue ivoire et or, ondulations brillantes, lunettes de soleil dorées dans les cheveux, petit sac rouge cerise, menton levé, lumière plus chaude. La silhouette ne change pas. La caméra reste à hauteur de poitrine : le ralenti en pied ne doit jamais se lire comme une caméra qui s'attarde sur le corps.

**Variante à tester en premier : la bande en amorce**, puisque le P1 cible a la sienne (rime). Mêmes trois silhouettes floues, de dos et sans visage, aux mêmes places, mais la tête tournée vers elle, figées. **Repli :** le P22 ci-dessus.

##### Variante à tester · la bande en amorce (P22, 4 essais au plus)

**1. Retouche du décor** (référence : `decors/salle_entree.png` ; sortie : `decors/salle_entree_amorce_p22.png`) :

```text
Same image, same gym entrance, same lighting, same colors and same framing. Only add, in the blurred foreground, two hugely muscular young men at the left edge of the frame and one at the right edge, at mid-height, seen from behind and out of focus, facing the open doors: one with bright lemon-yellow skin and slicked-back golden hair, one with warm tan-brown fibrous skin and a short spiky tuft of coconut fibers on his head, one with deep indigo-blue matte skin and a navy-blue quiff. Their faces are not visible; their heads are turned toward the open doorway, frozen. The doorway and the center of the frame stay empty, and nothing is in the bottom fifth of the image. No text, no letters.
```

**2. Image clé** (références : image 1 = `decors/salle_entree_amorce_p22.png`, image 2 = `identite/cerise_glow.png`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Eye-level full-body shot, camera at chest height, vertical 9:16 composition. Inside the open steel doors of a loft gym, golden backlight, blurred gym-goers at the edges, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous dark-red hair in freshly styled glossy Hollywood waves with two small cherries and a leaf clipped in it, oversized gold-rimmed sunglasses pushed up in her hair, full glossy red lips, glamorous makeup, wearing a tailored ivory-white blazer mini dress with gold buttons and a small gold cherry pendant, with an adult 25-year-old face appears alone in the open doorway, a small structured cherry-red handbag on her arm, backlit, chin up, a calm confident look. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus; in the blurred foreground, three muscular figures seen from behind at the left and right edges, at mid-height, stay out of focus, their heads turned toward her, their faces never visible. No text, no letters, no logos, no subtitles.
```

**3. Prompt vidéo** (180 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Eye-level full-body shot, camera at chest height, on a locked-off static camera; the framing never changes. Inside the open steel doors of a loft gym, golden backlight, blurred gym-goers at the edges, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous dark-red hair in freshly styled glossy Hollywood waves with two small cherries and a leaf clipped in it, oversized gold-rimmed sunglasses pushed up in her hair, full glossy red lips, glamorous makeup, wearing a tailored ivory-white blazer mini dress with gold buttons and a small gold cherry pendant, with an adult 25-year-old face appears alone in the open doorway. She walks straight toward the camera with slow, confident steps, chin up, hair moving; the blurred gym-goers turn their heads toward her. Three blurred figures seen from behind stay frozen at the edges. She does not speak and her lips stay closed. No one speaks. Audio: gym hall murmurs, distant street, heel steps, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, sharp faces in the crowd, mirror, poster, banner, screen, numbers on weights, faces on the foreground figures, foreground figures turning around, sharp foreground figures
```

### Scène G · Le retour (57,3–67,6 s)

#### Plan 23 · Réaction n° 3 · 57,3–58,8 s (1,5 s)

| Champ | Consigne |
|---|---|
| Décor | `salle_rack` (salle de sport, côté de la bande) |
| Personnage, tenue | Citron, `citron_salle` ; **muet à l'image** |
| Cadrage | Gros plan, visage et épaules. Regard hors champ vers la gauche. Recadrage : `gp`. |
| Caméra | fixe pendant toute la génération (locked-off). Aucun effet au montage. |
| Geste avant la réplique | **Muet.** Son sourire de frimeur se décompose ; il ouvre la bouche, puis déglutit. |
| Réplique | aucune à l'image. **Voix hors champ :** Myrtille (profil `myrtille`) : « Quoi ?! » (1 mot, environ 0,4 s), posée à 0,3 s. Interjection banale, autorisée par la règle de droit : elle rend le battement de stupeur de la référence et coupe le silence de la métamorphose. Tant que `voix_off` n'existe pas, le plan reste muet. |
| Émotion | sidération |
| Son dans le clip | `gym ambiance, distant clanking weights`, `the gym going quiet`, pas de musique. |
| Bruitages (montage) | — (sous-titres du « Quoi ?! » tirés de la voix clonée) |
| Incrustation de montage | — |
| Musique (version complète) | `revanche` continue. |
| Transition vers la suite | Coupe franche. |
| Dernière image | Citron bouche bée. |


**Image clé** (références : image 1 = `decors/salle_rack.png`, image 2 = `identite/citron_salle.png`, puis recadrage `gp`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders, vertical 9:16 composition. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black sleeveless gym hoodie on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone, his cocky smile collapsing, mouth falling open, looking off-screen to the left. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (140 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders on a locked-off static camera; the framing never changes. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black sleeveless gym hoodie on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone. He stares to the left; his cocky smile slowly collapses, his mouth falls open and he swallows hard. He does not speak and his lips stay closed. No one speaks. Audio: gym ambiance, distant clanking weights, the gym going quiet, no music.
```

**Variante animée sur notre voix** : sans objet (plan muet).

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, mirror, poster, banner, screen, numbers on weights
```

#### Plan 24 · La réplique-miroir · 58,8–62,2 s (3,4 s)

| Champ | Consigne |
|---|---|
| Décor | `salle_rack` (salle de sport, côté de la bande) |
| Personnage, tenue | Coco, `coco` |
| Cadrage | Plan rapproché taille. Regard hors champ vers la gauche. Recadrage : `pm`. |
| Caméra | fixe pendant toute la génération (locked-off). Aucun effet au montage. |
| Geste avant la réplique | La serviette blanche au cou, il passe la main sur sa touffe de fibres de coco et s'avance d'un pas avec un sourire charmeur raté. |
| Réplique | « Cerise ?! Pas besoin de lui. T'as besoin de moi ! » (9 mots) |
| Segments et jeu | « Cerise ?! » → *[He grins clumsily]* → « Pas besoin de lui. T'as besoin de moi ! » |
| Consigne de voix | Profil Voicebox `coco`. Rauque, ébahi sur « Cerise ?! », puis dragueur lourd et content de lui. Même mélodie que la fin du P14. |
| Émotion | drague lourde |
| Son dans le clip | `gym ambiance, distant clanking weights`, pas de musique. |
| Bruitages (montage) | — |
| Incrustation de montage | — |
| Musique (version complète) | `revanche`, plus bas. |
| Transition vers la suite | Coupe franche. |
| Dernière image | Coco, clin d'œil raté, sourire figé. |


**Image clé** (références : image 1 = `decors/salle_rack.png`, image 2 = `identite/coco.png`, puis recadrage `pm`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up, vertical 9:16 composition. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with warm tan-brown skin covered in a fine fibrous fuzz like a coconut husk, a short spiky tuft of dry coconut fibers on top of his head, thick eyebrows and a cocky grin, wearing a tight white sleeveless gym tank top and a white towel around his neck, with an adult 28-year-old face stands alone, rubbing the coconut-fiber tuft on his head with one hand, jaw dropped, looking off-screen to the left. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (178 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with warm tan-brown skin covered in a fine fibrous fuzz like a coconut husk, a short spiky tuft of dry coconut fibers on top of his head, thick eyebrows and a cocky grin, wearing a tight white sleeveless gym tank top and a white towel around his neck, with an adult 28-year-old face stands alone. He rubs his coconut-fiber tuft, looking to the left. He speaks in French, in a loud, hoarse, laughing young man's voice, amazed, then flirting, "Cerise ?!" He grins clumsily, "Pas besoin de lui. T'as besoin de moi !" Only he speaks, his lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: gym ambiance, distant clanking weights, no music.
```

**Variante animée sur notre voix** (LTX-2 TURBO, mode audio ; réplique retirée, 162 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with warm tan-brown skin covered in a fine fibrous fuzz like a coconut husk, a short spiky tuft of dry coconut fibers on top of his head, thick eyebrows and a cocky grin, wearing a tight white sleeveless gym tank top and a white towel around his neck, with an adult 28-year-old face stands alone. He rubs his coconut-fiber tuft, looking to the left. He speaks in French, amazed, then flirting; his lips move in sync with the provided voice, and in the pause he grins clumsily. Only he speaks. The camera holds the frame. Audio: gym ambiance, distant clanking weights, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, mirror, poster, banner, screen, numbers on weights
```

**Réplique-miroir :** « T'as besoin de moi » reprend mot pour mot la fin du P14. Coco n'était pas sur le palier, mais le public a tout entendu. La drague reste légère : ni geste, ni sifflet.

#### Plan 25 · Fin de service · 62,2–65,0 s (2,8 s)

| Champ | Consigne |
|---|---|
| Décor | `salle` (salle de sport, côté Cerise) |
| Personnage, tenue | Cerise, `cerise_glow` |
| Cadrage | Gros plan, visage et épaules. Regard hors champ vers la droite. Recadrage : `gp`. |
| Caméra | fixe pendant toute la génération (locked-off). Au montage : zoom lent 1,0 → 1,15. |
| Geste avant la réplique | Sourire en coin, un sourcil levé ; elle remet une mèche derrière son oreille. |
| Réplique | « Désolée, messieurs… La serveuse a fini son service. » (8 mots) |
| Segments et jeu | « Désolée, messieurs… » → *[She tucks a strand behind her ear]* → « La serveuse a fini son service. » |
| Consigne de voix | Profil Voicebox `cerise`. Posée, amusée, souveraine ; jamais agressive. |
| Émotion | triomphe tranquille |
| Son dans le clip | `gym ambiance, distant clanking weights`, pas de musique. |
| Bruitages (montage) | — |
| Incrustation de montage | — |
| Musique (version complète) | `revanche` **respire** (−4 dB sous la réplique). |
| Transition vers la suite | Coupe franche. |
| Dernière image | Cerise, sourire en coin. |


**Image clé** (références : image 1 = `decors/salle.png`, image 2 = `identite/cerise_glow.png`, puis recadrage `gp`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders, vertical 9:16 composition. In a sunlit loft gym at golden hour, red brick and arched windows blurred behind, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous dark-red hair in freshly styled glossy Hollywood waves with two small cherries and a leaf clipped in it, oversized gold-rimmed sunglasses pushed up in her hair, full glossy red lips, glamorous makeup, wearing a tailored ivory-white blazer mini dress with gold buttons and a small gold cherry pendant, with an adult 25-year-old face stands alone, a half smile, one eyebrow raised, looking off-screen to the right. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (179 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders on a locked-off static camera; the framing never changes. In a sunlit loft gym at golden hour, red brick and arched windows blurred behind, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous dark-red hair in freshly styled glossy Hollywood waves with two small cherries and a leaf clipped in it, oversized gold-rimmed sunglasses pushed up in her hair, full glossy red lips, glamorous makeup, wearing a tailored ivory-white blazer mini dress with gold buttons and a small gold cherry pendant, with an adult 25-year-old face stands alone. She speaks in French, in a soft, sweet young woman's voice, slightly husky, calm, amused and confident, "Désolée, messieurs…" She tucks a strand behind her ear, "La serveuse a fini son service." Only she speaks, her lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: gym ambiance, distant clanking weights, no music.
```

**Variante animée sur notre voix** (LTX-2 TURBO, mode audio ; réplique retirée, 176 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders on a locked-off static camera; the framing never changes. In a sunlit loft gym at golden hour, red brick and arched windows blurred behind, a glamorous voluptuous young woman with deep cherry-red skin, long voluminous dark-red hair in freshly styled glossy Hollywood waves with two small cherries and a leaf clipped in it, oversized gold-rimmed sunglasses pushed up in her hair, full glossy red lips, glamorous makeup, wearing a tailored ivory-white blazer mini dress with gold buttons and a small gold cherry pendant, with an adult 25-year-old face stands alone. She looks to the right with a half smile and one eyebrow raised. She speaks in French, calm, amused and confident; her lips move in sync with the provided voice, and in the pause she tucks a strand behind her ear. Only she speaks. The camera holds the frame. Audio: gym ambiance, distant clanking weights, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, mirror, poster, banner, screen, numbers on weights
```

Troisième réplique à citer, sur le motif du métier.

#### Plan 26 · Le livreur · 65,0–67,6 s (2,6 s)

| Champ | Consigne |
|---|---|
| Décor | `salle_entree` (entrée de la salle, foule floue) |
| Personnage, tenue | Kiwi, `kiwi_chic` |
| Cadrage | Plan rapproché taille. Regard hors champ vers la gauche (vers Cerise). La veste verte de livreur sur l'épaule doit se voir : c'est elle qui rend « Le livreur ?! » lisible. Recadrage : `pm`. |
| Caméra | fixe pendant toute la génération (locked-off). Aucun effet au montage. |
| Geste avant la réplique | Dans l'embrasure, en contre-jour, il lui tend la main (hors champ, à gauche), sourire doux. |
| Réplique | « Viens, Cerise. Ce soir, c'est toi qu'on sert. » (8 mots) |
| Segments et jeu | « Viens, Cerise. » → *[He holds out his hand]* → « Ce soir, c'est toi qu'on sert. » |
| Consigne de voix | Profil Voicebox `kiwi`. Chaleureux, doux, un brin taquin ; « c'est toi qu'on sert » souriant. |
| Émotion | tendresse |
| Son dans le clip | `gym hall murmurs, distant street`, pas de musique. |
| Bruitages (montage) | — |
| Incrustation de montage | — |
| Musique (version complète) | Dernière note chaude de `revanche`. |
| Transition vers la suite | Coupe franche, retour brutal à la tension. |
| Dernière image | Kiwi, main tendue, sourire doux, contre-jour. |


**Image clé** (références : image 1 = `decors/salle_entree.png`, image 2 = `identite/kiwi_chic.png`, puis recadrage `pm`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up, vertical 9:16 composition. Inside the open steel doors of a loft gym, golden backlight, blurred gym-goers at the edges, a hugely muscular handsome young man with olive-green fuzzy skin, short curly dark-brown hair, bright green eyes, wearing an open white linen shirt on his bare muscular chest with six-pack abs, a thin silver chain and his green delivery jacket slung over one shoulder, with an adult 27-year-old face and a warm smile leans alone in the open doorway, softly backlit, one open hand held out toward the left of the frame, a soft smile. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus, only a few small blurred gym-goers far away at the edges. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (180 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. Inside the open steel doors of a loft gym, golden backlight, blurred gym-goers at the edges, a hugely muscular handsome young man with olive-green fuzzy skin, short curly dark-brown hair, bright green eyes, wearing an open white linen shirt on his bare muscular chest with six-pack abs, a thin silver chain and his green delivery jacket slung over one shoulder, with an adult 27-year-old face and a warm smile leans alone in the open doorway. He smiles softly to the left. He speaks in French, in a warm, friendly young man's voice with a slight Parisian street accent, warm and gentle, "Viens, Cerise." He holds out his hand, "Ce soir, c'est toi qu'on sert." Only he speaks, his lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: gym hall murmurs, distant street, no music.
```

**Variante animée sur notre voix** (LTX-2 TURBO, mode audio ; réplique retirée, 160 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. Inside the open steel doors of a loft gym, golden backlight, blurred gym-goers at the edges, a hugely muscular handsome young man with olive-green fuzzy skin, short curly dark-brown hair, bright green eyes, wearing an open white linen shirt on his bare muscular chest with six-pack abs, a thin silver chain and his green delivery jacket slung over one shoulder, with an adult 27-year-old face and a warm smile leans alone in the open doorway. He smiles softly to the left. He speaks in French, warm and gentle; his lips move in sync with the provided voice, and in the pause he holds out his hand. Only he speaks. The camera holds the frame. Audio: gym hall murmurs, distant street, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, sharp faces in the crowd, mirror, poster, banner, screen, numbers on weights
```

### Scène H · Le cliffhanger (67,6–78,6 s)

#### Plan 27 · Retenu · 67,6–69,1 s (1,5 s)

| Champ | Consigne |
|---|---|
| Décor | `salle_rack` (salle de sport, côté de la bande) |
| Personnage, tenue | Citron, `citron_salle` |
| Cadrage | Plan rapproché taille. Regard hors champ vers la gauche. **Aucune main ni aucun bras d'un autre personnage dans le cadre.** Recadrage : `pm`. |
| Caméra | fixe pendant toute la génération (locked-off). Aucun effet au montage. |
| Geste avant la réplique | Penché en avant comme retenu par des bras hors champ, il force, les veines du cou saillantes, et pointe la sortie. |
| Réplique | « Le livreur ?! Lâchez-moi ! » (3 mots) |
| Segments et jeu | « Le livreur ?! » → *[He points furiously to the left]* → « Lâchez-moi ! » |
| Consigne de voix | Profil Voicebox `citron`. Crié, jaloux, essoufflé par la lutte. |
| Émotion | rage, jalousie |
| Son dans le clip | `gym ambiance, distant clanking weights`, `sneakers scuffling on rubber`, pas de musique. |
| Bruitages (montage) | Bruit de lutte hors champ (souffles, semelles qui crissent). |
| Incrustation de montage | — |
| Musique (version complète) | `tension` revient d'un coup. |
| Transition vers la suite | Coupe franche, plus serré (le P28 a sa propre image clé). |
| Dernière image | Citron penché en avant, doigt pointé à gauche. |


**Image clé** (références : image 1 = `decors/salle_rack.png`, image 2 = `identite/citron_salle.png`, puis recadrage `pm`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up, vertical 9:16 composition. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black sleeveless gym hoodie on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone, leaning hard forward as if straining against an unseen restraint, neck tense, pointing toward the left of the frame. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (167 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black sleeveless gym hoodie on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone. He lunges forward against an unseen restraint, his neck muscles tense. He speaks in French, in a deep, smooth, confident young man's voice, arrogant, shouting with jealous rage, "Le livreur ?!" He points furiously to the left, "Lâchez-moi !" Only he speaks, his lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: gym ambiance, distant clanking weights, sneakers scuffling on rubber, no music.
```

**Variante animée sur notre voix** (LTX-2 TURBO, mode audio ; réplique retirée, 156 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black sleeveless gym hoodie on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone. He lunges forward against an unseen restraint, his neck muscles tense. He speaks in French, shouting with jealous rage; his lips move in sync with the provided voice, and in the pause he points furiously to the left. Only he speaks. The camera holds the frame. Audio: gym ambiance, distant clanking weights, sneakers scuffling on rubber, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, hands on his shoulders, arms holding him, mirror, poster, banner, screen, numbers on weights
```

#### Plan 28 · La menace finale · 69,1–72,8 s (3,7 s)

| Champ | Consigne |
|---|---|
| Décor | `salle_rack` (salle de sport, côté de la bande) |
| Personnage, tenue | Citron, `citron_salle` |
| Cadrage | Gros plan, visage et épaules. **Regard caméra**, index pointé vers l'objectif. Image clé propre, distincte de celle du P27 (qui regarde et pointe vers la gauche, en plan rapproché). Recadrage : `gp`. |
| Caméra | fixe pendant toute la génération (locked-off). Au montage : coup de zoom jusqu'au très gros plan (1,0 → 1,25) sur « Un seul ». |
| Geste avant la réplique | Les yeux exorbités, les dents serrées, il pointe la caméra de l'index. |
| Réplique | « Cent jours pour monter… Un seul pour te faire tomber ! » (10 mots) |
| Segments et jeu | « Cent jours pour monter… » → *[He jabs his finger at the lens]* → « Un seul pour te faire tomber ! » |
| Consigne de voix | Profil Voicebox `citron`. Bas et menaçant, puis crié sur « te faire tomber », le « te » appuyé : c'est elle qu'il vise. |
| Émotion | menace |
| Son dans le clip | `gym ambiance, distant clanking weights`, pas de musique. |
| Bruitages (montage) | — |
| Incrustation de montage | — |
| Musique (version complète) | `tension`. |
| Transition vers la suite | Coupe franche. |
| Dernière image | Très gros plan, index pointé vers l'objectif. |


**Image clé** (références : image 1 = `decors/salle_rack.png`, image 2 = `identite/citron_salle.png`, puis recadrage `gp`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders, vertical 9:16 composition. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black sleeveless gym hoodie on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone, eyes wide, teeth clenched, pointing his index finger straight at the camera. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (175 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders on a locked-off static camera; the framing never changes. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black sleeveless gym hoodie on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone. He glares into the lens, eyes wide, and points his finger at the camera. He speaks in French, in a deep, smooth, confident young man's voice, arrogant, low and threatening, then shouting, "Cent jours pour monter…" He jabs his finger at the lens, "Un seul pour te faire tomber !" Only he speaks, his lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: gym ambiance, distant clanking weights, no music.
```

**Variante animée sur notre voix** (LTX-2 TURBO, mode audio ; réplique retirée, 157 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Close-up of the face and shoulders on a locked-off static camera; the framing never changes. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black sleeveless gym hoodie on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone. He glares into the lens, eyes wide, and points his finger at the camera. He speaks in French, low and threatening, then shouting; his lips move in sync with the provided voice, and in the pause he jabs his finger at the lens. Only he speaks. The camera holds the frame. Audio: gym ambiance, distant clanking weights, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, hands on his shoulders, arms holding him, mirror, poster, banner, screen, numbers on weights
```

**Image clé propre (correction du chef) :** le P28 se génère depuis sa propre image clé, en gros plan, regard caméra et index vers l'objectif. Il ne réutilise pas celle du P27, qui regarde et pointe vers la gauche en plan rapproché : les deux cadrages sont incompatibles. **La menace est claire :** « te faire tomber » vise Cerise ; ce n'est pas une plainte de Citron sur lui-même.

#### Plan 29 · Le zeste · 72,8–76,2 s (3,4 s)

| Champ | Consigne |
|---|---|
| Décor | `salle_rack` (salle de sport, côté de la bande) |
| Personnage, tenue | Myrtille, `myrtille` |
| Cadrage | Plan rapproché taille. Regard hors champ **vers la droite**, vers Citron qu'il vient de lâcher : c'est la seule exception de la bande (§ B.5). Recadrage : `pm`. |
| Caméra | fixe pendant toute la génération (locked-off). Aucun effet au montage. |
| Geste avant la réplique | Il lâche Citron (hors champ, à droite), recule les mains levées, hausse les épaules et secoue la tête, moqueur, un sourcil levé. |
| Réplique | « Frérot… Lâche l'affaire. Il te reste que le zeste. » (9 mots) |
| Segments et jeu | « Frérot… » → *[He shrugs and shakes his head]* → « Lâche l'affaire. Il te reste que le zeste. » |
| Consigne de voix | Profil Voicebox `myrtille`. Nasal, moqueur, détendu ; « Il te reste que le zeste » lâché comme la chute d'une blague. |
| Émotion | dérision |
| Son dans le clip | `gym ambiance, distant clanking weights`, pas de musique. |
| Bruitages (montage) | — |
| Incrustation de montage | — |
| Musique (version complète) | `tension`, basse. |
| Transition vers la suite | Coupe franche. |
| Dernière image | Myrtille hausse les épaules, sourcil levé. |


**Image clé** (références : image 1 = `decors/salle_rack.png`, image 2 = `identite/myrtille.png`, puis recadrage `pm`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up, vertical 9:16 composition. By black squat racks on a red brick wall, warm golden light from the left, a tall muscular handsome young man with deep indigo-blue matte skin with a soft dusty bloom like a blueberry, a styled navy-blue quiff and a teasing smirk, wearing a light-grey sleeveless gym hoodie with the hood down and big white headphones around his neck, with an adult 26-year-old face stands alone, stepping back as he lets go of someone off-screen to the right, both open hands raised at shoulder height, one eyebrow raised, looking off-screen to the right. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (180 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. By black squat racks on a red brick wall, warm golden light from the left, a tall muscular handsome young man with deep indigo-blue matte skin with a soft dusty bloom like a blueberry, a styled navy-blue quiff and a teasing smirk, wearing a light-grey sleeveless gym hoodie with the hood down and big white headphones around his neck, with an adult 26-year-old face stands alone. He lets go of someone off-screen to the right and steps back, open hands raised, looking to the right. He speaks in French, in a nasal, teasing, slightly high-pitched young man's voice, mocking, "Frérot…" He shrugs and shakes his head, "Lâche l'affaire. Il te reste que le zeste." Only he speaks, his lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: gym ambiance, distant clanking weights, no music.
```

**Variante animée sur notre voix** (LTX-2 TURBO, mode audio ; réplique retirée, 163 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. By black squat racks on a red brick wall, warm golden light from the left, a tall muscular handsome young man with deep indigo-blue matte skin with a soft dusty bloom like a blueberry, a styled navy-blue quiff and a teasing smirk, wearing a light-grey sleeveless gym hoodie with the hood down and big white headphones around his neck, with an adult 26-year-old face stands alone. He lets go of someone off-screen to the right and steps back, open hands raised, looking to the right. He speaks in French, mocking; his lips move in sync with the provided voice, and in the pause he shrugs and shakes his head. Only he speaks. The camera holds the frame. Audio: gym ambiance, distant clanking weights, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, mirror, poster, banner, screen, numbers on weights
```

Le calembour du zeste : la bande lâche Citron. Il ne recycle plus la réplique-signature de Mamie à l'ép. 1
(« Un citron… ça finit toujours pressé »), et n'a aucun écho avec la référence.

#### Plan 30 · Jamais ! · 76,2–77,4 s (1,2 s)

| Champ | Consigne |
|---|---|
| Décor | `salle_rack` (salle de sport, côté de la bande) |
| Personnage, tenue | Citron, `citron_salle` |
| Cadrage | Très gros plan du visage. **Regard caméra** (« looking straight into the lens », écrit dans le `cadre`, l'image clé et les prompts vidéo). Recadrage : `gp`. |
| Caméra | fixe pendant toute la génération (locked-off). Au montage : zoom fixe 1,25. |
| Geste avant la réplique | Il hurle ; coupe sèche sur le dernier mot. |
| Réplique | « Jamais ! » (1 mot) |
| Segments et jeu | « Jamais ! » |
| Consigne de voix | Profil Voicebox `citron`. Hurlé, une seule syllabe tenue ; coupe sèche sur la fin du mot. |
| Émotion | rage |
| Son dans le clip | `gym ambiance, distant clanking weights`, `his scream echoing`, pas de musique. |
| Bruitages (montage) | Coup sourd sur la coupe, puis noir. |
| Incrustation de montage | — |
| Musique (version complète) | `tension` coupée net avec le mot. |
| Transition vers la suite | **Coupe sèche au noir.** |
| Dernière image | Bouche grande ouverte sur « -mais », puis noir. |


**Image clé** (références : image 1 = `decors/salle_rack.png`, image 2 = `identite/citron_salle.png`, puis recadrage `gp`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Extreme close-up of the face, vertical 9:16 composition. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black sleeveless gym hoodie on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone, looking straight into the lens, mouth wide open in a furious scream, eyes wide. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (158 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Extreme close-up of the face on a locked-off static camera; the framing never changes. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black sleeveless gym hoodie on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone. He throws his head toward the camera, furious, looking straight into the lens. He speaks in French, in a deep, smooth, confident young man's voice, arrogant, screaming with rage, "Jamais !" Only he speaks, his lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: gym ambiance, distant clanking weights, his scream echoing, no music.
```

**Variante animée sur notre voix** (LTX-2 TURBO, mode audio ; réplique retirée, 145 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Extreme close-up of the face on a locked-off static camera; the framing never changes. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with bright lemon-yellow skin, slicked-back golden-yellow hair, chiseled jaw, wearing an open black sleeveless gym hoodie on his bare muscular chest with six-pack abs and a thick gold chain, with an adult 28-year-old face and light stubble stands alone. He throws his head toward the camera, furious, looking straight into the lens. He speaks in French, screaming with rage; his lips move in sync with the provided voice. Only he speaks. The camera holds the frame. Audio: gym ambiance, distant clanking weights, his scream echoing, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, mirror, poster, banner, screen, numbers on weights
```

Plan d'un seul mot : un moteur qui dit lui-même une réplique trop courte rend souvent du charabia. **Préférer la variante animée sur notre voix** (TURBO), ou recaler la voix clonée sur un clip muet.

### Carte de fin · 77,4–78,6 s (1,2 s)

| Champ | Consigne |
|---|---|
| Image | Fond noir. **PARTIE 2** en grand, blanc, avec un halo rouge. Dessous : « La suite très vite 🍒 Abonne-toi ». Fabriquée par le montage (`png_fin`), rien n'est généré. |
| Son | Le coup sourd de la coupe du P30 résonne. Pas de musique. |
| Durée | 1,2 s (champ `montage.fin_duree`). Le code actuel met 2,0 s : l'épisode ferait alors 79,4 s. |

### Plan de repli · P1 bis (si la voix hors champ n'est pas prête)

**Quand s'en servir :** tant que `montage.py` ne sait pas poser une voix hors champ. Les modifications sont
alors :
- le **P1 devient muet**, avec une durée de 1,5 s ; on garde la même image clé et le même prompt ;
- on **insère ce plan juste après lui** : Coco seul, dans `salle_rack`, dit la réplique ;
- la **durée totale passe à 80,1 s estimés**, au-dessus de la cible : on applique alors une coupe de secours (script
  § 6.1), et la première réplique tombe à 1,5 s au lieu de 0,0 s ;
- les **P21 et P23 restent muets** : les voix hors champ de Kiwi et de Myrtille attendent que `voix_off` soit codé.

Dans `episode.json`, ce plan est rangé dans `repli_voix_off.plan` (id 31). Il faut le déplacer dans `plans`, juste
après le plan 1.

| Champ | Consigne |
|---|---|
| Temps | 1,5–3,9 s (2,4 s estimés : sa voix mesurée + 0,4 s) |
| Décor | `salle_rack` |
| Personnage, tenue | Coco, `coco` |
| Cadrage | Plan rapproché taille ; regard hors champ vers la gauche ; recadrage `pm` |
| Geste | Une main en porte-voix, il rit et lance sa moquerie à travers la salle. |
| Réplique | « Oh, Citron ! Ta cantinière est là ! » (6 mots) |
| Voix | Profil `coco` : rauque, hilare, crié de loin. |
| Bruitages | Rires de la bande. |

**Image clé** (références : `decors/salle_rack.png`, `identite/coco.png`, puis recadrage `pm`) :

```text
Stylized semi-realistic 3D CGI animated movie still, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up, vertical 9:16 composition. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with warm tan-brown skin covered in a fine fibrous fuzz like a coconut husk, a short spiky tuft of dry coconut fibers on top of his head, thick eyebrows and a cocky grin, wearing a tight white sleeveless gym tank top and a white towel around his neck, with an adult 28-year-old face stands alone, laughing, one hand cupped by his mouth as if calling across the gym, looking off-screen to the left. The face is in the upper half of the frame and nothing important is in the bottom fifth. Exactly one character in focus. No text, no letters, no logos, no subtitles.
```

**Prompt vidéo** (179 mots) :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with warm tan-brown skin covered in a fine fibrous fuzz like a coconut husk, a short spiky tuft of dry coconut fibers on top of his head, thick eyebrows and a cocky grin, wearing a tight white sleeveless gym tank top and a white towel around his neck, with an adult 28-year-old face stands alone. He cups one hand by his mouth and laughs, looking to the left. He speaks in French, in a loud, hoarse, laughing young man's voice, shouting across the gym, "Oh, Citron !" He laughs, "Ta cantinière est là !" Only he speaks, his lips moving in sync with every word, and the camera holds the frame during the pauses. Audio: gym ambiance, distant clanking weights, no music.
```

**Variante animée sur notre voix** :

```text
Stylized semi-realistic 3D CGI animated film, glamorous high-budget look, cinematic lighting, rich detailed set, saturated colors, very expressive attractive faces, vertical 9:16 frame. Medium close-up from the waist up on a locked-off static camera; the framing never changes. By black squat racks on a red brick wall, warm golden light from the left, a hugely muscular handsome young man with warm tan-brown skin covered in a fine fibrous fuzz like a coconut husk, a short spiky tuft of dry coconut fibers on top of his head, thick eyebrows and a cocky grin, wearing a tight white sleeveless gym tank top and a white towel around his neck, with an adult 28-year-old face stands alone. He cups one hand by his mouth and laughs, looking to the left. He speaks in French, shouting across the gym; his lips move in sync with the provided voice, and in the pause he laughs. Only he speaks. The camera holds the frame. Audio: gym ambiance, distant clanking weights, no music.
```

**Champ négatif** :

```text
subtitles, captions, on-screen text, letters, words, watermark, logo, second character, duplicate character, extra people, camera zoom, camera pan, scene cut, transition, music, morphing, face changing, deformed face, distorted, fused fingers, extra fingers, bad anatomy, motion artifacts, low quality, worst quality, nudity, lingerie, swimsuit, childlike face, mirror, poster, banner, screen, numbers on weights
```

## E. Montage

### E.1 Le format et le rythme
- **Le format :** 1080 × 1920, 24 i/s, coupes franches, sans fondu enchaîné.
- **Les durées des plans :** de 1,2 s (P30, un mot) à 5,0 s (P12, Mamie), 2,6 s en moyenne. Chaque plan parlé est
  coupé 0,10 s avant le premier mot et 0,28 s après le dernier : c'est la voix qui fait sa durée.
- **Le minutage se fixe sur les voix,** pas l'inverse : voix clonées, tempo et pauses, mesure, puis `duree` = parole
  + 0,4 s, puis seulement les clips (Annexe, étape 5).
- **Les changements de lieu :** un whoosh court, que le montage ajoute tout seul.
- **Le montage d'effort (P19 à P21) :** on coupe sur le mouvement. Puis viennent le flash blanc et le carton.
- **Le silence :** hors métamorphose, moins de 2 s entre deux voix, aux réactions muettes (P4 avec les rires qui
  s'éteignent, P16 avec la porte qui claque). Pendant la métamorphose, la voix hors champ de Kiwi au P21 (« Plus
  fort, Cerise ! ») laisse environ 2,0 s sans voix (fin du P19, P20). Puis, de la fin de sa voix au « Quoi ?! » de
  Myrtille (P23, à 0,3 s), 3,4 s passent sans réplique, dont 2,3 s couvertes par les murmures de la foule qui
  montent (P22) : le plus long passage sans aucune voix humaine tombe à 0,8 s. La v2 en avait 4,7 s, la v1 7,7 s
  d'un bloc ; la référence en a 6,1 s.
- **La parole** couvre 58,6 s sur 78,6 s (75 %, comme à l'ép. 1). On ne l'augmente pas en accélérant les voix : on
  remplit les plans muets (rires, murmures, « Quoi ?! », impacts).
- **La durée cible :** de 75 à 80 s, carte de fin comprise. Estimation : 78,6 s (78,9 s sans arrondi), 83,6 s au
  débit prudent. Avec le code actuel, qui fait une carte de fin de 2 s : 79,4 s. Avec le repli du P1 : 80,1 s. Au-delà
  de 80 s mesurés, on applique les coupes de secours, dans l'ordre (script § 6.1, `episode.json` → `minutage`).

### E.2 Les sous-titres
- **Le style :** mot à mot, en Montserrat Black 78 px, blanc avec un contour noir. Le mot en cours passe en jaune.
  Ils vont par groupes de 3 mots au plus (code `write_ass`).
- **La position :** le bas des sous-titres est à y = 1340 px, au-dessus des boutons TikTok, dans le tiers bas. Ils
  ne passent jamais sur un visage, puisque les visages sont dans la moitié haute.
- **Les chiffres s'écrivent en chiffres** (champ `sous_titre`) : P8, P11 et P28, comme « 100 jours » et
  « 48 000 vues ».
- **Les voix hors champ (P1, P21, P23) sont sous-titrées,** à partir des mots de la voix clonée.
- **Deux exports :** avec et sans sous-titres. Les cinq meilleures vidéos du corpus n'en avaient pas, alors on
  compare les deux versions sur les premières publications.

### E.3 L'accroche, le badge et la légende
- **L'accroche :** **IL L'A RENIÉE DEVANT SES POTES 💔**, dans un cadre blanc arrondi en haut (y = 300). Elle reste
  de 0 à 3 s, puis disparaît en fondu (le code actuel la garde jusqu'à 3,5 s).
- **Le badge :** **LA MÉTAMORPHOSE · PARTIE 1**, rouge, en haut à gauche. Il reste sur tout l'épisode, sauf sur la
  carte de fin. Le numéro d'épisode reste interne : le spectateur qui arrive par « Pour toi » lit un titre et une
  partie, ce qui annonce la suite (« PARTIE 2 ») sans le perdre.
- **La légende TikTok :** Cerise, « juste la serveuse » ? 🍒 Partie 1 #fruitstory #histoiredefruit
  #tiktokfrance🇨🇵 #brainrot #france
- **La couverture :** l'image du P1 (Cerise et sa gamelle face à la salle), avec l'accroche. Ne jamais montrer
  `cerise_glow` en couverture : ce serait dévoiler la fin.

### E.4 Les incrustations (toutes ajoutées au montage, jamais générées)

| Plan | Incrustation | Quand | Type (`incrust`) |
|---|---|---|---|
| P1 | Accroche et badge | 0 à 3 s, puis badge permanent | titre et badge |
| P8 | **100 JOURS**, jaune, gros, au centre bas | à partir du mot « jours » | `chiffre` |
| P11 | Notification **peche.officielle 🍑 a publié · Quand la serveuse se trompe de salle 😂🍒**, avec un `ding` | du début du plan au mot « vues », où elle est retirée | `notif`, avec `jusqu_au_mot` (à coder) |
| P11 | **48 000 VUES** | à partir du mot « vues » | `chiffre` |
| P22 | Carton **100 JOURS PLUS TARD**, blanc, **dans le tiers haut** (y ≈ 380 à 520 px, sous le badge ; champ `y_px`), jamais au centre : il masquerait le début de la révélation | 1,2 premières secondes, avec un flash blanc de 0,15 s et un whoosh | `carton` (à coder) ; repli actuel : `chiffre`, posé aujourd'hui à y = 1040 par `png_chiffre`, à remonter à `y_px` |
| fin | **PARTIE 2**, avec « La suite très vite 🍒 Abonne-toi » | 1,2 s sur fond noir | carte de fin |

**Attention au P11 :** dans le code actuel, la notification (y = 960 à 1130) et le chiffre (y = 1040 à 1280) se
chevauchent. Il faut le champ `jusqu_au_mot` ou, à défaut, une notification remontée de 300 px.

### E.5 Les effets (zoom, ralenti, flash, lumière)

| Plan | Effet | Réglage (`zoom`, `ralenti`) |
|---|---|---|
| P2 | zoom avant progressif | 1,0 → 1,15 sur tout le plan |
| P6 | coup de zoom | 1,0 → 1,2 sur « quitte » |
| P8 | zoom lent | 1,0 → 1,15 |
| P10 | coup de zoom | 1,0 → 1,2 sur « partout » |
| P15 | zoom lent | 1,0 → 1,15 |
| P18 | coup de zoom | 1,0 → 1,25 sur « salle » |
| P21 → P22 | flash blanc | 0,15 s, retour à l'image en 0,1 s |
| P22 | ralenti | × 1,4 (image seulement ; le son du clip est remplacé) |
| P25 | zoom lent | 1,0 → 1,15 |
| P28 | coup de zoom jusqu'au très gros plan | 1,0 → 1,25 sur « seul » |
| P30 | zoom fixe | 1,25 |

- **Le zoom ne dépasse jamais 1,25.** La source fait 704 × 1280 et elle est déjà agrandie en 1080 × 1920.
- **Lumière (facultatif) :** la scène A un peu plus froide et désaturée (−10 % de saturation), les scènes F et G
  un peu plus chaudes (+5 % de rouge et de jaune). Le retour paraît ainsi plus solaire que le départ, dans le même
  décor.

### E.6 Les voix
- **Le tempo :** 0,90 au plus pour tous (décision du chef) ; Mamie inchangée à 1,25, avec un vibrato léger
  (`montage.tempo_voix`, `effets_voix`). C'est un peu plus vif que l'ép. 1 v4 (0,85), et jamais au-delà : le
  propriétaire a demandé des voix plus lentes. Le rythme vient des coupes dans le texte.
- **Les pauses** sont ajoutées par `caler.py`. On demande 0,15 à 0,25 s : passer « … » de 0,32 à 0,25 s dans
  `PAUSES`.
- **Les hauteurs** (`voix_hauteur`) : Citron 125 Hz, Kiwi 135 Hz, Mamie 200 Hz, Coco 115 Hz.
- **Les prises :** au moins 3 par réplique (`voix_clonees.py --essais 3`). On garde la mieux reconnue par whisper
  et la plus proche de la voix de référence.
- **La prononciation :** si whisper entend mal « Cerise » en début de réplique (« Kerise », « Riz »), on écrit
  « Serise » dans `replique_tts`, comme à l'ép. 1. Les sous-titres ne changent pas.
- **« Cent jours » :** whisper peut écrire « 100 jours », voire « sans jour ». On compare en normalisant les
  chiffres ; si la voix dit autre chose que « cent », on refait la prise.
- **Les voix hors champ** se posent sur des clips muets, qui ne sont pas recalés : Coco à 0,0 s au P1, Kiwi à 0,2 s
  au P21, Myrtille à 0,3 s au P23.

### E.7 Les bruitages

| Plan | Bruitage | Placement | Volume |
|---|---|---|---|
| P1 à P3 | `rires` de la bande (3 ou 4 voix d'hommes) | sous les répliques | moyen, sous la voix |
| P4 | les rires s'éteignent | fondu de 1 s | bas |
| P8 | `boom` | sur « honte » | moyen |
| P11 | `ding` | arrivée de la notification | moyen |
| P12 → P13 | `toc` : deux coups à la porte | juste après « citron », jusque sur la coupe | moyen |
| P14 | `minuterie` : clic de l'escalier | début du plan | bas, facultatif |
| P16 | `porte_claque` | première image | fort |
| P21 | `impact` : coups dans les pattes d'ours (hors champ) | sur les deux coups visibles de la fenêtre gardée (vers 0,15 et 0,45 s) | moyen |
| P22 | `whoosh` | sur le flash | moyen |
| P22 | `murmures` de la foule qui montent | dès 0,3 s, fondu d'entrée sur 1 s, jusqu'à la coupe | bas à moyen |
| P27 | `lutte` : souffles, semelles | sous la réplique | moyen |
| P30 | `boom` | sur la coupe au noir | fort |

- **Ce qui existe déjà :** `ding`, `whoosh`, `boom`, `battement`, `pluie`, `salle`.
- **Ce qui est à ajouter :** `rires`, `toc`, `porte_claque`, `impact`, `murmures`, `lutte` et `minuterie`. On les prend
  libres de droits, en petits fichiers.

### E.8 La musique
**Version complète** (`final.mp4`) : notre musique originale, découpée par ambiance. On copie les prises de l'ép. 1
(`musique_prise` : tension 3, triste 1, revanche 3).

| De | À | Ambiance | Coupures |
|---|---|---|---|
| P1 (0,0 s) | P6 | `tension` | coupée 0,3 s après « quitte » |
| P7 | P10 | `tension`, qui repart | coupée net à la fin du P10 |
| P11 | P15 | `triste` (piano) | coupée sur « c'est toi » ; silence au P16 |
| P17 | P18 | `tension`, basse et grave | coupure sèche à la fin du P18 |
| P19 | P26 | `revanche` | sommet au P22 ; elle respire sous le P25 |
| P27 | P30 | `tension` | coupée net avec « Jamais ! » |

La musique baisse automatiquement sous les voix : le montage la ramène à environ un tiers.

**Version sans musique** (`final_sans_musique.mp4`) : c'est celle qu'on publie sur TikTok, avec le **son tendance
ajouté dans l'application**.
- **Le son :** le son mélancolique qui monte, tendance au moment de publier, du type « Камин ». On le choisit dans
  la bibliothèque TikTok le jour même, sans jamais l'intégrer à nos fichiers.
- **Le volume, dans l'éditeur TikTok :**
  - son d'origine (nos voix et bruitages) à **100 %** ;
  - son ajouté à **15 à 20 %**, jamais plus de 25 %.
  - Les répliques doivent rester parfaitement compréhensibles au téléphone, à volume moyen.
- **Le calage :** on choisit le passage du son pour que sa montée tombe sur le carton (54,7 s estimés), sinon sur le
  P19 (50,0 s). On relit ces deux temps sur le montage réel, après la mesure des voix.
- **La vérification :** en aperçu, aucune parole chantée ne doit couvrir les trois répliques à citer (P12, P15,
  P25). Sinon, on prend un autre passage, ou on descend à 12 %.

### E.9 La fin
Au P30, « Jamais ! » est hurlé et la coupe tombe sèche au noir sur la fin du mot, avec un `boom`. Puis la carte
**PARTIE 2** s'affiche 1,2 s. Rien ne vient après : pas de générique, pas de plan bonus.

### E.10 Les exports et la publication
- **Deux fichiers :**
  - `final.mp4` (voix, bruitages, musique), pour Reels et Shorts ;
  - `final_sans_musique.mp4`, pour TikTok et son tendance.
- **Les versions sous-titrées :** chaque fichier existe avec et sans sous-titres.
- **Le son :** −14 LUFS intégrés, crête à −1,5 dB (réglage actuel du montage).
- **La publication :** le soir, entre 20 h et 22 h, avec l'étiquette « contenu généré par IA » activée. Sur
  YouTube, la musique générée est déclarée.

## F. Contrôle qualité avant publication

Chaque case se coche. Un seul « non » bloque la publication du plan concerné, qu'on refait.

### F.1 Avant de générer
- [ ] Les fiches `coco` et `myrtille` sont validées, avec au moins 4 candidats chacune. Coco se lit comme une noix
  de coco, Myrtille comme une myrtille.
- [ ] La fiche Coco n'a **aucun trait caricatural** (dents ou lèvres surlignées) : son fruit se lit par la matière
  (bourre fibreuse brun clair, touffe de fibres sur le crâne).
- [ ] Les 5 tenues sont validées : `cerise_maison`, `cerise_sport`, `cerise_glow`, `citron_salle` et `kiwi_chic`.
  La couleur de fruit est présente partout ; sinon, retouche « peau seulement ».
- [ ] La fiche « après » est comparée à la fiche « avant » : même visage, même peau, mêmes cerises et feuille, même
  silhouette. Elle a les lunettes de soleil dorées relevées dans les cheveux, les ondulations et le petit sac rouge
  cerise, sans créoles.
- [ ] Les 8 décors sont dans `02_la_metamorphose/decors/`, sans texte, miroir ni chiffre :
  - `cuisine` est une copie ;
  - `appart` est retouché, avec le pot net et sans étiquette ;
  - les 6 autres sont nouveaux.
- [ ] Les profils Voicebox `coco` et `myrtille` sont créés et testés à whisper.
- [ ] **Les voix sont faites avant les clips** : prises, tempo et pauses appliqués, parole mesurée, et `duree` =
  parole + 0,4 s reportée dans `episode.json`. Le total est entre 75 et 80 s, sinon on applique les coupes de
  secours dans l'ordre.
- [ ] Le code est adapté, ou le repli est choisi (voir l'annexe). Le montage de l'ép. 1 avait des numéros de plans
  écrits en dur.

### F.2 Chaque image clé
- [ ] Un seul personnage net. Pour `salle_entree`, des figurants flous seulement ; avec l'amorce (P1 cible, P22 en variante),
  les trois silhouettes de la bande restent floues, de dos, sans visage, et hors du cinquième bas.
- [ ] C'est le bon personnage, dans la bonne tenue, avec son accessoire signature visible :
  - Cerise : cerises et feuille ;
  - Citron : chaîne en or ;
  - Coco : serviette ;
  - Myrtille : casque blanc ;
  - Mamie : lunettes rondes et châle ;
  - Kiwi : veste verte de livreur.
- [ ] Le regard va dans le bon sens (§ B.5) : Cerise vers la droite, la bande vers la gauche (sauf Myrtille au P29,
  vers la droite), les apartés, la menace du P28 et le « Jamais ! » du P30 vers la caméra.
- [ ] Le visage est dans la moitié haute, et rien d'important n'est dans le cinquième bas.
- [ ] Aucun texte, logo, chiffre, miroir, tableau ni reflet. Pas de visage en double au recadrage.
- [ ] Le personnage est habillé et a un visage adulte. Ni pose penchée, ni cadrage sur le corps.
- [ ] Les accessoires sont présents et sans texte : la gamelle (P1, P4), le shaker (P2), le pot (P9, P10), le
  bouquet de roses jaunes dans son kraft brun (P14 à P17, y compris au P17), le stylo et le carnet (P1, P4, P6, P8 ; le
  carnet seulement si le cadre le montre), les lunettes de soleil dorées (P22, P25) et le sac rouge cerise (P22). Au P21, ni patte d'ours, ni main, ni sac dans le cadre.
- [ ] Les plans en pied (P1, P22) sont à hauteur de poitrine, sans contre-plongée.

### F.3 Chaque clip
- [ ] Seul le personnage visible bouge les lèvres. Au P1, les lèvres de Cerise restent fermées.
- [ ] Ni morphing, ni changement de visage ou de tenue, ni personnage qui apparaît.
- [ ] La caméra reste fixe. Le mouvement vient du personnage seulement (course P20, marche P22).
- [ ] La réplique est reconnue par whisper (similarité d'au moins 0,8), ou le clip est recalé sur la voix clonée.
- [ ] Les faux sous-titres d'Agnes sont détectés et floutés, ou bien on prend une autre prise.
- [ ] Le clip couvre la voix mesurée + 0,4 s (la `duree` de l'étape 5), sans plan figé à la fin.

### F.4 Les voix
- [ ] Chaque personnage garde la même voix d'un plan à l'autre (ressemblance Resemblyzer).
- [ ] Le tempo est à 0,90 au plus (Mamie à 1,25), et les pauses durent 0,15 à 0,25 s.
- [ ] Les chiffres sont bien dits : « Cent », « Quarante-huit mille ». Les noms aussi : « Cerise », « Citron ».
- [ ] Coco et Myrtille ne sont jamais nommés à voix haute.
- [ ] Au P24, Coco reprend « T'as besoin de moi » avec la même mélodie que Citron au P14.

### F.5 Le montage
- [ ] La durée totale mesurée est entre 75 et 80 s, carte de fin comprise (78,6 s estimés ; 79,4 s avec la carte
  de fin du code actuel ; 80,1 s en repli, qui demande une coupe de secours).
- [ ] La première voix tombe à 0,0 s (voix hors champ), ou à 1,5 s en repli. La voix de Kiwi tombe au P21, le « Quoi ?! » de Myrtille au P23.
- [ ] Le badge **LA MÉTAMORPHOSE · PARTIE 1** et l'accroche sont là (0 à 3 s), sans faute ; l'émoji 💔
  s'affiche.
- [ ] Les incrustations tombent sur le bon mot : « jours » au P8, « vues » au P11. Le carton s'affiche 1,2 s au P22, dans le tiers haut, sans toucher sa tête.
  Rien ne se chevauche au P11.
- [ ] Les sous-titres correspondent au texte, chiffres en chiffres, et ne passent sur aucun visage.
- [ ] Les zooms sont aux plans prévus, sans dépasser 1,25, et le ralenti du P22 est à × 1,4.
- [ ] Les bruitages sont en place : rires, toc, porte qui claque, impacts du P21 calés sur les coups visibles,
  murmures du P22, lutte, booms.
- [ ] Les coupures de musique tombent juste aux P6, P10, P15, P18 et P30.
- [ ] Le son est à −14 LUFS, et la musique ne couvre aucune réplique.
- [ ] La fin est coupée sèche au noir, puis vient **PARTIE 2**.
- [ ] Au P22, on voit le même cadre qu'au P1 : la rime visuelle se voit.

### F.6 Les règles de fond
- [ ] Aucune moquerie du corps, aucun chiffre de poids, aucun conseil d'alimentation.
- [ ] Aucune violence à l'image : la lutte du P27 reste hors champ, aucune arme, personne n'est frappé.
- [ ] La drague du P24 reste légère : pas de geste vers Cerise, pas de sifflet.
- [ ] La règle de droit est tenue.
  - Aucune réplique de la vidéo de référence, ni paraphrase proche.
  - Vérifier le texte final avec la liste interne de phrases interdites (notes de l'équipe, hors dépôt).
  - Seuls les mots banals « Jamais ! », « Quoi ?! », « mon cœur » et « Lâchez-moi ! » sont communs avec elle.
- [ ] Ni marque, ni personne réelle, ni mineur. Le titre ne contient pas « Kiwi et Cerise ».

### F.7 La publication
- [ ] L'étiquette « contenu généré par IA » est activée.
- [ ] La légende et les hashtags sont exacts. La couverture montre le P1, sans dévoiler `cerise_glow`.
- [ ] Le son tendance est ajouté dans TikTok à 15–20 %, et aucune parole chantée ne couvre une réplique.
- [ ] La publication se fait entre 20 h et 22 h. La version complète part sur Reels et Shorts.

## Annexe · `episode.json`, code à adapter et ordre de fabrication

### Ce que contient `episode.json`
Il a le **même format que l'ép. 1**, avec les mêmes clés :
- au premier niveau : `titre`, `accroche`, `badge`, `fin`, `legende`, `style`, `tenues`, `persos`, `voix`, `decors`,
  `musique`, `plans`, `voix_hauteur`, `musique_prise`, `montage` ;
- pour chaque plan : `id`, `decor`, `persos`, `cadre`, `parle`, `jeu`, `replique`, `musique`, `incrust`,
  `recadrage`.

`produire.py` le lit donc sans modification. Des champs facultatifs s'y ajoutent. Le code actuel les ignore, et ils
servent aux adaptations ci-dessous.

| Où | Champ | Rôle |
|---|---|---|
| premier niveau | `style_video` | le style des prompts vidéo (« film ») |
| premier niveau | `fiches` | les prompts des fiches de Coco et Myrtille, à ajouter à `identites.py` |
| premier niveau | `accessoires`, `negatif` | les blocs figés des accessoires (dont `serveuse` et `sac`, ajoutés en v3) et le champ négatif de base |
| premier niveau | `repli_voix_off` | le plan de repli (id 31) et sa règle d'insertion |
| premier niveau | `minutage` | la règle « `duree` = parole mesurée + 0,4 s », les débits de référence et prudents, les estimations et les coupes de secours classées |
| `montage` | `fin_duree` | 1,2 s pour la carte de fin (2,0 s en dur aujourd'hui) |
| `decors.*` | `court`, `audio` | le repère court et le son des prompts vidéo |
| `plans[*]` | `duree`, `segments`, `camera`, `fin_de_plan` | les champs du gabarit 2 du rapport |
| `plans[*]` | `prompts` | `image`, `video`, `video_sur_notre_voix`, `negatif` et `references` : les textes exacts du § D |
| `plans[*].prompts` | `variante_amorce` | au P22 : la retouche du décor, l'image, la vidéo et le négatif de la variante « bande en amorce » (4 essais au plus) |
| `plans[0].prompts` | `retouche_decor`, `decor_retouche`, `essais_max`, `repli_sans_amorce` | au P1, l'amorce est la version cible : ses prompts sont les prompts principaux, le décor retouché est le premier fichier de `references`, et le plan sans amorce (`cadre` compris) est rangé dans `repli_sans_amorce` |
| `plans[*]` | `voix_off` | les voix hors champ : Coco au P1, Kiwi au P21, Myrtille au P23 |
| `plans[*]` | `fenetre_clip` | au P21 : la fenêtre de 1,5 s gardée dans le clip de 4 s (début indicatif, contenu, règle) |
| `carton`, `incrust` | `y_px` | au P22 : la hauteur du carton, 380 à 520 px |
| `plans[*]` | `zoom`, `ralenti`, `carton`, `sfx`, `coupe_musique` | les effets, le carton, les bruitages et les coupures de musique, plan par plan |
| `incrust` | `jusqu_au_mot`, `repli_carton` | retirer la notification au P11 ; marquer le chiffre qui tient lieu de carton au P22 |

### Le code à adapter avant le montage
**Dans `montage.py`, des valeurs propres à l'ép. 1 sont écrites en dur.** Sans correction, l'ép. 2 se monte de
travers :
- un `ding` sur le plan 1 ;
- un `boom` et un arrêt de la musique sur le plan 24, ce qui couperait la musique en pleine drague de Coco ;
- un `battement` et la fin de la musique sur le plan 29, ce qui l'arrêterait vers 72,8 s ;
- la vignette d'appel prise au plan 7 ;
- l'avatar `citron.png` des publications ;
- les ambiances par décor ;
- `NOMS`, sans Coco ni Myrtille.

**À ajouter à `montage.py`, par ordre d'utilité :**
1. `voix_off` : poser la voix clonée sur un plan muet, sans recaler l'image (P1, P21, P23).
2. `carton`, avec le flash, le whoosh et la hauteur `y_px` (tiers haut), et `jusqu_au_mot` pour la notification.
3. `zoom` et `ralenti` par plan.
4. `sfx` et `coupe_musique` par plan, à la place des numéros écrits en dur.
5. `fin_duree`.
6. `fenetre_clip` : pour un plan muet, prendre le début du clip dans `fenetre_clip.debut_s` au lieu de 0,4 s (P21).

**Ailleurs dans la chaîne :**
- **`produire.py` compose les images avec `cadre`, pas avec `prompts.image`.** `make_image` assemble le style, le
  bloc `persos` du personnage et le `cadre` du plan ; `reframe` assemble sa consigne de recadrage, le bloc `persos`
  et le `cadre`. Les `prompts.image` du § D servent à composer à la main. **Toute correction d'image doit donc être
  faite dans `cadre`**, sinon il faut adapter `produire.py` pour lire `prompts.image`. En v3, chaque correction
  d'image (P1, P4, P6, P8, P12, P17, P19, P20, P22, P24, P29, P30) est écrite dans `cadre` et dans `prompts.image`.
- **Au P1, `make_image` doit charger le décor retouché** (`decors/salle_entree_amorce_p1.png`, premier fichier de
  `prompts.references`) au lieu de `decors/<decor>.png`. Sans cette adaptation, composer l'image clé du P1 à la main.
- **`produire.py`** assemble encore ses propres prompts vidéo, avec la réplique « d'un souffle », sans segments.
  Quand `plans[*].prompts.video` existe, l'utiliser tel quel, et `video_sur_notre_voix` pour TURBO.
- **`identites.py`** : ajouter `coco` et `myrtille` à `CHARS` (textes au § B.2 et dans `fiches`).
- **`caler.py`** : `PAUSES["…"]` passe de 0,32 à 0,25 s. Ajouter un mode `--voix-seules` : appliquer le tempo, les
  pauses et les effets (`respirer`) à chaque voix sans clip, puis écrire la parole mesurée de chaque plan (premier
  et dernier mot, `bornes`) dans `controle/voix_durees.json`. Aujourd'hui, `caler.py` saute les plans sans clip.
- **`voix_clonees.py`** : créer d'abord les profils Voicebox `coco` et `myrtille`. Les voix hors champ du P1, du
  P21 et du P23 doivent aussi être générées ; le script, lui, ne traite que les plans qui ont `parle`.

### L'ordre de fabrication
1. **Les fiches :** ajouter `coco` et `myrtille` à `identites.py`, générer 4 candidats chacun, puis les valider. On
   obtient `identite/coco.png` et `identite/myrtille.png`.
2. **Les tenues :** `produire.py ../episodes/02_la_metamorphose --only tenues`, puis valider les fiches, avec la
   retouche « peau seulement » si besoin.
3. **Les décors :**
   - copier `cuisine.png` ;
   - retoucher `appart.png` (§ C.4) ;
   - lancer `produire.py … --only decors` pour les 6 autres ;
   - retoucher `salle_entree.png` en `salle_entree_amorce_p1.png` (version cible du P1) et, en variante,
     `salle_entree_amorce_p22.png`
     (la bande en amorce, prompts au § D, P1 et P22).
4. **Les images clés et les recadrages :** `--only images`, puis `--only cadrage`. Relire chaque image avec le
   § F.2. Au P1, la version cible a l'amorce (4 essais au plus) ; si aucun essai ne passe le § F.2, on bascule sur
   `repli_sans_amorce` en copiant son `cadre` dans `cadre`. Au P22, tester ensuite la variante d'amorce ; sinon, on garde
   le plan sans amorce.
5. **Les voix, avant les clips** (correction du chef) :
   - `voix_clonees.py --essais 3`, voix hors champ comprises (P1, P21, P23) ;
   - le tempo (0,90, Mamie 1,25) et les pauses de `caler.py` (mode `--voix-seules`) ;
   - mesurer la parole de chaque voix, du premier au dernier mot ;
   - fixer dans `episode.json` `duree` = parole mesurée + 0,4 s, plan par plan (P1, P21 et P23 : voix hors champ +
     0,4 s, au moins 1,5 s) ;
   - additionner : entre 75 et 80 s carte de fin comprise, on continue ; au-delà, on applique les coupes de secours
     dans l'ordre (`minutage.coupes_de_secours`), on refait les voix touchées et on remesure.
6. **Les clips :** `--only clips`, à la `duree` de l'étape 5. Les moteurs passent dans l'ordre LTX-2.3, TURBO, puis
   Agnes. LTX-2 TURBO anime directement l'image sur notre fichier de voix : c'est recommandé au P30 (un seul mot) et
   au P12 si la voix de Mamie dépasse 4,6 s. Puis `caler.py` recale les lèvres des autres clips sur nos voix.
7. **La musique :** copier depuis l'ép. 1 la prise retenue de chaque ambiance (`tension/prise_3.wav`,
   `triste/prise_1.wav`, `revanche/prise_3.wav`, environ 15 Mo).
8. **Le montage :** `montage.py`, après les adaptations ci-dessus. Puis la liste de contrôle du § F.

**Le disque :** il reste environ 2 Go libres. On purge au fil de l'eau les essais rejetés : `images/*_t*.png`,
`clips/*_t*.mp4` et les images de `controle/`.
