# Essais de dessin du 8 octobre 2026

Ce sont des **pistes générées par IA** pour choisir une direction, pas des dessins définitifs. Pour que le
personnage soit protégeable, la fiche modèle finale doit être redessinée ou retouchée par un humain (le
propriétaire ou un illustrateur avec une cession de droits écrite), et datée par une enveloppe e-Soleau.
Toutes les images ont été faites avec Agnes image (agnes-image-2.5-flash), à environ 12 s par image.

## 1. Deux styles pour les mêmes 6 personnages

| Piste | Planche | Ce qui marche | Ce qui ne va pas |
|---|---|---|---|
| **A, laine feutrée façon stop-motion** | `planche_laine.jpg` | Très chaleureuse, faite main, loin du « Pixar » des chaînes IA. Le personnage à l'écran ressemble déjà au doudou qu'on pourra vendre. Les silhouettes se distinguent bien. | Le loir ressemble à un écureuil, à corriger : gris-brun clair, masque sombre autour des yeux, queue qui traîne derrière. |
| B, 3D douce façon jouet en vinyle | `planche_douce3d.jpg` | Nette, lisible, moderne. | Plus proche de ce que font les autres ; même défaut sur le loir. |

**Ma recommandation : la piste A.**
- Elle différencie la série au premier coup d'œil.
- Elle rend la promesse du doudou évidente.
- Elle colle à l'ambiance calme du soir.

À confirmer par le test vidéo : la texture de laine doit rester stable d'une image à l'autre, sans « bouillir ».

**La nouvelle luciole** reprend ce qui fait son identité :
- un corps-lanterne au ventre jaune lumineux ;
- une cape bleu nuit étoilée (des élytres, comme une vraie luciole) ;
- deux antennes courtes à perles lumineuses ;
- ni nœud, ni ailes transparentes, ni cils.

Nino a un pyjama corail avec une lune, au lieu des étoiles qui rappelaient PJ Masks.

## 2. Les personnages dans leur décor (`planche_scenes.jpg`)

Méthode : on génère d'abord le décor vide (le jardin, la chambre), puis on ajoute les personnages en donnant
l'image du décor et l'image d'identité de chacun.

- **Le jardin et la chambre** sont réussis et cohérents avec le style : la lanterne-fleur, la souche, la mare, la
  fenêtre ronde.
- **La luciole seule dans le jardin** et **Nino avec la luciole dans la chambre** sont fidèles aux fiches.
- **La luciole et la hérissonne ensemble : défaut.** La hérissonne a pris les antennes à perles de la luciole
  (`zoom_picotine3.jpg`). C'est le même mélange d'attributs que les ailes sur Nino dans l'ancienne série.

## 3. Deux parades testées (`planche_parades.jpg`)

| Parade | Résultat |
|---|---|
| (a) Écrire l'interdiction : « la hérissonne n'a pas d'antennes, seule la luciole en a » | 1 image propre sur 2 ; dans l'autre, c'est la luciole qui a pris les piquants de la hérissonne |
| (b) **Ajouter les personnages un par un** : décor + hérissonne, puis cette image + la luciole (« garde l'image telle quelle, ajoute la luciole ») | **2 images propres sur 2** |

**Règle de production retenue : un seul personnage ajouté par passage**, chacun avec sa seule image d'identité.
Le juge visuel vérifie en plus, pour chaque personnage, les attributs qui ne sont pas les siens :
- des antennes sur la hérissonne, le loir, la chouette ou Nino ;
- des piquants sur la luciole ;
- des ailes sur un autre personnage que Bzou.

## Fichiers

- `identite_laine/` et `identite_douce3d/` : fiches de face de chaque personnage, qui servent d'images
  d'identité. Les PNG en pleine résolution sont gardés pour la luciole, Nino et Picotine.
- `scenes/` : décors vides, scènes et essais de parades.
- Scripts : `../outils/design_trials.py`, `scene_trials.py`, `leak_trials.py`.
