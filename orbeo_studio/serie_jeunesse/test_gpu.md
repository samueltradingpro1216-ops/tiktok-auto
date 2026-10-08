# Test sur carte graphique : protocole (semaine 2 du plan)

**But :** savoir, avant de produire, quel outil garde les personnages **identiques d'un plan à l'autre**, à quel
coût et avec combien de vérification humaine.

**Critère de réussite :** au moins **8 plans sur 10** sans aucun de ces défauts :
- un personnage qui change de forme ou de taille ;
- un personnage en double ;
- un mélange d'attributs entre personnages ;
- un mauvais décor ;
- une texture qui « bout » (la laine qui grouille d'une image à l'autre).

Si aucun outil n'y arrive, on applique le critère d'arrêt du rapport : style 2D plus simple, ou audio d'abord.

## 1. Les 10 plans de test (tirés du pilote 1, style laine)

| # | Lieu | Personnages | Plan | Durée |
|---|---|---|---|---|
| 1 | chambre | Nino | au lit, la couette jusqu'au nez, la porte entrouverte, une grande ombre à pointes sur le mur | 6 s |
| 2 | chambre | Nino | gros plan, les yeux grands ouverts | 4 s |
| 3 | chambre, fenêtre | Lucinou | trois petits coups à la vitre, son ventre s'allume | 5 s |
| 4 | jardin, souche | Picotine | roulée en boule devant la souche, puis le bout du nez | 6 s |
| 5 | jardin, souche | Picotine | l'ombre géante aux griffes sur la souche | 5 s |
| 6 | jardin | Lucinou | sa lumière vacille, elle a peur | 5 s |
| 7 | jardin | Nino (petit) et Lucinou | Nino fait reculer Lucinou, l'ombre rapetisse | 8 s |
| 8 | jardin | Lucinou | le hoquet lumineux (elle clignote en riant) | 4 s |
| 9 | jardin | Nino (petit) et Picotine | ombres chinoises : un oiseau, un lapin | 8 s |
| 10 | chambre | Nino | il fait un oiseau d'ombre à côté du petit dinosaure | 6 s |

Images d'identité : `design/identite_laine/` (luciole, Nino, Picotine). Décors : `design/scenes/jardin_vide.jpg`
et `chambre_vide.jpg`.

## 2. Les concurrents

**Images clés :**
- **Agnes image**, méthode « un personnage par passage » (gratuit, référence actuelle) ;
- **Qwen-Image-Edit-2511** (Apache-2.0, édition à partir de plusieurs images), sur carte graphique louée.

**Plans vidéo :**
- **Agnes v2.0** en image vers vidéo, et en mode début et fin (gratuit) ;
- **Agnes 2.5-flash** en mode référence (gratuit, mais souvent saturé) ;
- **LTX-2.5** avec ses modules complémentaires « Ingredients » (vidéo à partir de la fiche personnage et du décor)
  et « Layout-to-Render » (vidéo à partir d'un placement grossier fait dans Blender, ce qui fixe la caméra et la
  taille de chaque personnage). Gratuit sous 10 M$ de chiffre d'affaires, sur carte graphique louée ;
- **Wan 2.2** et ses dérivés (VACE, Phantom), Apache-2.0, en solution de repli.

## 3. Mesures pour chaque plan et chaque outil

- **défauts :** doublon, mélange, forme ou taille, décor, texture. Juge automatique, puis vérification humaine sur
  une planche ;
- **fidélité :** une note de 1 à 5 pour chaque personnage, comparé à sa fiche ;
- **mouvement :** l'action demandée est-elle faite ? la caméra reste-t-elle fixe quand c'est demandé ?
- **temps de génération et coût :** heures de carte graphique × prix ;
- **temps de vérification humaine.**

Résultat attendu : un tableau outil par outil, et le coût estimé d'un épisode de 5 minutes (environ 40 plans).

## 4. Où faire tourner les modèles open source

| Option | Prix | Pour quoi |
|---|---|---|
| **Modal** | 30 $ offerts chaque mois | les essais, lancés par script |
| **Vast.ai** ou **RunPod** | RTX 4090 à environ 0,35 à 0,50 $/h | la production et les longues séries d'essais |
| Hugging Face (compte gratuit) | 5 min de carte graphique par jour | les petits essais des démonstrations en ligne |
| Kaggle | deux T4 gratuites, quota hebdomadaire | l'entraînement d'un modèle personnalisé de Lucinou (LoRA), plus tard |

**Budget estimé du test :** 3 à 5 heures de RTX 4090, soit environ 2 à 3 $, ou rien du tout avec le crédit Modal.

## 5. Ce qu'il te faut faire avant

1. Créer les comptes : **Hugging Face** (gratuit), **Modal** (gratuit, 30 $ par mois), et **Vast.ai** ou
   **RunPod** avec 10 à 20 $ de crédit.
2. Créer une clé d'accès sur chacun. Sur Hugging Face : un jeton en **lecture**, et accepter les conditions des
   modèles demandés (Pocket TTS de Kyutai).
3. Les ajouter dans les réglages de l'environnement cloud. Dans le menu de l'environnement, dans la barre de titre
   de la session, choisir « Modifier ». Ajouter chaque clé dans la section des secrets réseau (appelée
   « identifiants d'API » dans les anciennes versions de l'application) si elle existe, sinon comme variable
   d'environnement, sous ces noms :
   - `HF_TOKEN`
   - `MODAL_TOKEN_ID` et `MODAL_TOKEN_SECRET`
   - `VAST_API_KEY` ou `RUNPOD_API_KEY`
4. **Ne jamais coller une clé dans le chat.** Une nouvelle session les lit automatiquement ; il suffit alors de me
   dire « lance le test GPU ».
