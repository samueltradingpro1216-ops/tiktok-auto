# La formule des histoires IA qui retiennent (22 vidéos, 8 octobre 2026)

**Matériau :**
- les 22 vidéos envoyées ou trouvées le 8 octobre, entre 0,7 et 77 M de vues ;
- 19 sont en français, publiées entre août et octobre 2026.

**Méthode :** pour chacune, `outils/analyse_reference.py` donne les plans, le script minuté (faster-whisper) et la
musique (Shazam), et `outils/tiktok_fetch.py` donne les chiffres.

**Limites :**
- je n'ai pas les courbes de rétention (TikTok ne les donne qu'à l'auteur) ;
- je ne peux pas écouter : la qualité des voix est jugée par la transcription seulement.

## 1. Les chiffres communs (17 vidéos de 60 à 110 s)

| Mesure | Valeur typique | Fourchette |
|---|---|---|
| Durée | **75 s** | 62 à 99 s, toujours plus d'une minute pour être payé par TikTok |
| Première réplique | **à 0,0 s** (14 vidéos sur 17) | 0,0 à 2 s |
| Temps de parole | **94 % de la vidéo** | 69 à 99 % |
| Répliques | **une toutes les 2,5 s** (environ 30 par vidéo) | 16 à 58 |
| Débit | 2,7 mots par seconde | 2,3 à 4,3 |
| Silence le plus long | 2 à 4 s | — |
| Série numérotée | « Partie 1 », « Épisode 3 », « Épisode 14 » | la moitié des vidéos |

**Les sons :**
- le funk brésilien domine : « TREND DAS FRUTAS » (Dj Rhamon Dm), « BONDE DO PP DA NORTE », « BATIDA FUNK
  MEDLEY », « BLUE WATER CANDY » ;
- « Камин » (« Kamin », EMIN & JONY) accompagne les histoires tristes ;
- une ambiance d'horreur accompagne les histoires qui font peur ;
- les autres vidéos utilisent un « son original » : la voix et la musique mélangées par l'auteur.

**Les légendes :** l'enjeu ou une question au spectateur (« Il s'habille comme un SDF pour tester ses employés
😭💔 », « Vous seriez restée seule avec lui cette nuit ? »), suivis de 3 à 5 hashtags : #fruitstory
#histoiredefruit #tiktokfrance🇨🇵 #brainrot #histoire.

## 2. Les sept moteurs d'histoire (ce qui fait rester)

| Moteur | Exemples dans le lot (vues) | Pourquoi on reste |
|---|---|---|
| **La revanche de l'humilié** | le fils lâché par son **père indigne**, qui rachète tout l'empire du père (1,9 M) ; la fille moquée pour son corps (6,9 M) ; le petit contre le géant au tournoi (2,3 M) | on attend la justice |
| **Le test moral, le riche déguisé** | le patron habillé en SDF qui teste ses employés (1,2 M) ; choisir un mari parmi trois, et c'est le « pauvre » qui a payé l'opération de sa grand-mère (3,6 M) ; le fils pauvre qui doit payer les médicaments de sa mère (1,2 M) | on veut voir les méchants punis et le gentil récompensé |
| **La tromperie, la trahison** | la femme qui exploite son mari puis part « chercher l'homme qu'elle désire vraiment » (6,6 M) ; l'un des trois prétendants ment sur sa fortune (3,6 M) | on veut savoir qui ment et comment ça va éclater |
| **Le danger caché** | un appel aux urgences codé (« Oui maman… ») pendant un enlèvement (3,5 M) ; le beau-père qui « ne cligne jamais des yeux » (1,3 M) ; un chien mystérieux et ses trois règles (2,5 M) ; le secret du kebab (0,7 M) | la peur, et la question « va-t-elle s'en sortir ? » |
| **L'ascension** | le jeune footballeur sans crampons jusqu'à la Ligue des champions (film de 11 min, 1 M) ; le concours d'apnée à 67 M€ juste après un licenciement (0,7 M) | le rêve, la revanche sociale |
| **La rue, le quartier** | « Les flockos de Paname », **épisode 14** (0,9 M) ; une histoire de collège et de grand frère en 7 min (3,3 M) | l'argot et la vie de cité, une série qui revient |
| **L'absurde, le scato** | un pilote qui va aux toilettes en plein vol (1,2 M) ; les toilettes du millionnaire (1,2 M) ; le dernier GTA 6 (2 M) ; le singe qui met une claque à un géant, sans un mot (77 M) | le rire immédiat |

**Ce qui revient partout :**
- un **méchant clair** ;
- une **victime à qui on s'attache** (un pauvre, un enfant, un rejeté) ;
- un **enjeu chiffré** : 500 $ la nuit, 60 000 €, 67 M€, 200 à 500 kg ;
- une **fin coupée net**.

## 3. La structure, seconde par seconde (épisode de 75 s)

| Temps | Ce qui doit se passer | Exemples |
|---|---|---|
| **0 à 2 s** | Le conflit est **déjà en cours** : une phrase choc, une insulte, un ordre, un danger. Jamais d'introduction ni de générique. | « Je dois en lâcher un ! » ; « Choisis ton futur mari » ; « Vous gardez des chiens, non ? Prenez celui-là. » |
| **2 à 10 s** | Le rapport de force est posé : qui est le méchant, qui est la victime, et l'enjeu en chiffres. | « Voilà 500 $ pour une seule nuit » |
| **10 à 25 s** | Première escalade : l'injustice empire, ou une règle étrange apparaît. | « Ne le regardez pas dans les yeux » |
| **25 à 35 s** | **Premier rebondissement** : une révélation partielle. | le chien est sur l'avis de disparition ; Banito trouve une mine de diamants |
| **35 à 60 s** | Une escalade toutes les **10 secondes environ** : la victime se relève, ou le danger se rapproche. | « Un inconnu a racheté toutes mes dettes ? » |
| **60 à 72 s** | Le renversement (la revanche, la vérité) ou le pic de tension. | « Tu ne reconnais pas le fils que tu as lâché dans la mer ? » |
| **dernières 2 à 5 s** | **Coupure en plein suspense**, avec la promesse de l'épisode suivant. | « Ma décision, c'est… » ; « Lequel a osé mentir ? » ; « Regarde ses pattes, elles sont trop longues… » |

**À l'image :**
- un nouveau plan toutes les 2 à 6 s, avec des gros plans d'émotion ;
- des décors riches et très éclairés (palais doré, villa, cité, avion, colisée) ;
- les chiffres affichés à l'écran (une fortune sur le front, des kilos sur la barre, un compteur) ;
- des sous-titres mot à mot.

**Les personnages :**
- 14 vidéos sur 22 utilisent des fruits ou des légumes dans des situations humaines, en 3D façon Pixar ;
- les autres utilisent des humains quasi photoréalistes.

**Ce qui marche le mieux, d'après ce lot :** un **héros qui revient**.
- Dragono (@dragonfruitsaga) : 2 à 3,9 M de vues à chaque épisode.
- « Les flockos de Paname » : 14 épisodes.
- « Kiwi et Fraise » : partie 2, à 6,9 M de vues.

Dans le même genre, les comptes qui changent de personnages à chaque vidéo font moins.

## 4. Exemple de script original construit sur la formule (75 s)

**« Le testament de Papi Figue », partie 1.**

Papi Figue, très riche, fait semblant d'être ruiné pour voir lequel de ses trois enfants l'aidera.

| Temps | Plan | Réplique |
|---|---|---|
| 0,0 s | Gros plan : Pruneau, le fils aîné, en costume, sur le perron d'une villa | « Ruiné ? Alors dégage de MA villa, papa. » |
| 2 s | Papi Figue, valise à la main, sous la pluie | « C'est moi qui te l'ai achetée, cette villa… » |
| 5 s | Clémentine, la fille, au téléphone, ongles parfaits | « Désolée papa, j'ai brunch. Appelle un taxi. » |
| 8 s | À l'écran : « Fortune de Papi Figue : 0 € » (il ment) | Narrateur : « Ce que ses enfants ignorent… » |
| 10 s | Le compteur se retourne : **40 000 000 €** | « …c'est que Papi Figue a tout gardé. » |
| 13 s | Kiwi, le petit dernier, livreur à vélo, trempé | « Papa ? Viens, chez moi c'est petit, mais il y a ta place. » |
| 18 s | Le studio minuscule de Kiwi ; il donne son lit à son père | « Moi je dors sur le canapé, t'inquiète. » |
| 24 s | **Premier rebondissement :** Pruneau et Clémentine en visio, en train de comploter | « S'il meurt chez Kiwi, c'est Kiwi qui hérite. Il faut le récupérer. » |
| 30 s | Clémentine débarque chez Kiwi avec des fleurs et un faux sourire | « Papa d'amour ! Viens vivre chez moi ! » |
| 36 s | Papi Figue regarde Kiwi | « Et Kiwi ? » / Clémentine : « Lui ? Il te nourrit avec des pâtes. » |
| 42 s | Kiwi baisse les yeux. À l'écran : « Salaire de Kiwi : 1 100 € » | Kiwi : « C'est vrai… mais je les partage. » |
| 48 s | Papi Figue sort une enveloppe | « J'ai fait un nouveau testament. » |
| 53 s | Pruneau arrive en courant, essoufflé | « Papa, je suis venu te chercher ! Je t'aime, tu sais ! » |
| 58 s | Les trois enfants face au notaire, une Banane en lunettes | Notaire : « Monsieur Figue lègue ses 40 millions… » |
| 64 s | Gros plan sur Clémentine, qui sourit | « …à celui de ses enfants qui… » |
| 70 s | Le notaire tourne la page. Gros plan sur Kiwi | « …acceptera la condition suivante. » |
| 73 s | Noir, puis « PARTIE 2 » | Pruneau : « Quelle condition ?! » |

- **Légende :** « Il fait semblant d'être ruiné pour tester ses enfants… 💔 Vous auriez fait quoi ? #fruitstory
  #histoiredefruit #tiktokfrance🇨🇵 #histoire ».
- **Son :** un son funk tendance, ajouté dans l'application au moment de publier.
- **Partie 2 :** la condition, une nouvelle épreuve, et un nouveau suspense à la fin.

## 5. Ce que ça change pour Orbeo

- **Le genre fonctionne toujours.** Des comptes inconnus font 1 à 4 M de vues par épisode en septembre et octobre
  2026. La demande est là.
- **Copier tel quel, ce serait un compte de plus parmi des dizaines**, souvent doublés depuis le Brésil ou l'Asie.
- **Notre différence possible :**
  - **une famille ou une bande fixe**, avec des noms à nous, qui revient dans chaque épisode (c'est ce qui marche le
    mieux dans le lot) ;
  - des saisons qui avancent ;
  - une qualité d'image et de voix constante ;
  - des histoires très françaises : la famille, l'héritage, le quartier, le travail.
- **À éviter**, même si ça fait des vues :
  - le sexuel et le scato, qui sont signalés en masse et coupent les marques ;
  - les insultes en boucle ;
  - les copies de séries existantes.
- **Prochaine étape :** choisir le concept (la famille, le décor, la troupe fixe), puis fabriquer **un épisode
  d'essai complet** sur cette structure et le comparer aux références, sur les mêmes mesures.
