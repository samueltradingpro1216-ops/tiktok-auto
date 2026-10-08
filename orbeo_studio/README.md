# Orbeo Studio : le studio et ses deux séries

Orbeo Studio est le studio qui fabrique, avec l'IA, deux séries qui ne se mélangent jamais (compte
orbeo.studio@gmail.com). **Mise à jour du 8 octobre 2026 :** les deux lignes ont été repensées après deux études ;
rien de nouveau n'est produit tant que leur plan n'est pas validé.

| Ligne | Ce que c'est | Où | Public | Statut |
|---|---|---|---|---|
| **Série jeunesse** (titre de travail « Lucinou, la petite veilleuse du jardin ») | série courte d'avant le coucher (5 à 7 min) avec une héroïne luciole muette, une chanson par épisode, un rituel « on éteint l'écran » ; remplace la chaîne de comptines « Lulu la Luciole » | YouTube (« conçue pour les enfants »), puis audio | 3-5 ans et leurs parents | **priorité n°1** : conception en cours (`serie_jeunesse/`), test sur carte graphique semaine du 13 octobre |
| **Série ado-adulte** (proposition : « Les Crache-Pluie », les gargouilles d'une église de Paris) | comédie à épisodes de 61 à 90 s, troupe fixe, faux documentaire, 3 épisodes par semaine | TikTok (compte personnel), Instagram Reels, YouTube Shorts (nouvelle chaîne) | 18-34 ans | **en conception seulement** ; lancement au plus tôt le 23 novembre, après 5 critères (`reports/Ligne vidéo IA TikTok Orbeo.md`) |

Les épisodes de « Lulu la Luciole » déjà programmés (jusqu'au 16 octobre) sortent comme tests, puis passeront en
« non répertorié » quand la nouvelle série sera en ligne.

Documents de référence :
- `reports/Franchise jeunesse IA Orbeo.md` : le modèle de la série jeunesse ;
- `reports/Ligne vidéo IA TikTok Orbeo.md` : le modèle de la série ado-adulte et la priorité entre les deux ;
- `orbeo_studio/strategie.md` : la première étude de différenciation (6 octobre).

## Pourquoi deux chaînes et des comptes séparés
- Une vidéo « conçue pour les enfants » perd les commentaires, les notifications et la publicité ciblée. La chaîne
  enfants doit le rester entièrement pour que YouTube la recommande aux bons spectateurs.
- Un public de tout-petits et un public ado-adulte ne regardent pas la même chose : les mélanger fait baisser les
  recommandations des deux.
- Les comptes de la série ado-adulte ne parlent jamais de la série jeunesse, et inversement. Seule la mention « Une
  série Orbeo Studio » les relie.
- Les deux chaînes YouTube peuvent appartenir au même compte Google (YouTube, puis Paramètres, puis Ajouter ou
  gérer vos chaînes, puis Créer une chaîne).
- Metricool : la chaîne jeunesse est connectée à la marque `7251650`. La série ado-adulte demandera une 2e marque
  (une marque = une seule chaîne YouTube) : vérifier que l'abonnement le permet.

## Identifiants à réserver
- Série jeunesse : le nom choisi (voir `serie_jeunesse/noms.md`), par exemple `@lucinou.tv`. Domaines lucinou.com
  et lucinou.fr libres le 8 octobre.
- Série ado-adulte : par exemple `@lescrachepluie` (à vérifier). Domaines crachepluie.com et lescrachepluie.com
  libres le 8 octobre.
- Studio : `@orbeostudio` pour les coulisses, si besoin.

## Biographies
À réécrire une fois les noms choisis. Règles :
- une bio par série ;
- jamais de mélange des deux publics ;
- toujours « Une série Orbeo Studio » ;
- une mention « créé avec l'IA » là où le réseau le demande.

## Règles de publication
- Déclarer le contenu IA là où le réseau le demande : TikTok (`isAigc`), Instagram (`isAiGenerated`), YouTube
  (`isAiGeneratedContent` dans Metricool, `youtube_api.py video ID --synthetic oui`). Sur YouTube, un dessin animé seul
  n'a pas à être déclaré, mais **une musique générée par IA au cœur de la vidéo, si** (« AI generated music » est dans
  la liste des exemples, support.google.com/youtube/answer/14328491) : toutes les comptines de Lulu sont donc
  déclarées. YouTube précise que la déclaration ne limite ni l'audience ni la monétisation. Corrigé le 6 octobre pour
  l'ép. 02 publié et les 5 publications programmées.
- Les comptines restent sur la chaîne Lulu (vidéos et Shorts des refrains), toujours « conçues pour les enfants ».
- Signature des descriptions : « Une création Orbeo Studio ».

## Accès complet à la chaîne YouTube (API officielle)
Metricool publie et vidIQ modifie les vidéos et lit les statistiques, mais aucun des deux ne touche à la chaîne
elle-même (description, mots-clés, bannière, playlists). `youtube_api.py` le fait par l'API YouTube Data v3, avec
une connexion « appareil » qui marche depuis une session cloud (aucun mot de passe dans le chat).

Les serveurs MCP open source existants ([pauling-ai/youtube-mcp-server](https://github.com/pauling-ai/youtube-mcp-server),
[dyay108/youtube-mcp](https://github.com/dyay108/youtube-mcp)…) demandent une connexion par « localhost » : bons
sur un ordinateur, inutilisables dans une session cloud.

Mise en place (une fois, ~10 min, sur https://console.cloud.google.com avec le compte de la chaîne) :
1. Créer un projet « Orbeo Studio ».
2. API et services → Bibliothèque → activer **YouTube Data API v3**.
3. Écran de consentement OAuth : type « Externe », nom « Orbeo Studio », e-mail ; ajouter le compte de la chaîne
   comme utilisateur test, puis **Publier l'application** (en mode test, la connexion expire au bout de 7 jours ;
   l'écran « Google n'a pas validé cette application » est normal pour un usage perso : Paramètres avancés →
   Continuer).
4. Identifiants → Créer des identifiants → ID client OAuth → type **TV et périphériques à saisie limitée**.
5. Mettre l'ID client et le code secret dans les variables d'environnement de l'environnement cloud (menu de
   l'environnement dans la barre de titre → Modifier) : `YOUTUBE_CLIENT_ID` et `YOUTUBE_CLIENT_SECRET`.
6. Dans une nouvelle session : `python orbeo_studio/youtube_api.py login` affiche un code à saisir sur
   google.com/device.

Ce que l'API ne permet pas : changer la photo de profil (YouTube Studio uniquement). Les miniatures demandent
toujours la validation de la chaîne par téléphone. Les statistiques détaillées (durée de visionnage, rétention,
sources de trafic) passent par vidIQ et Metricool, déjà connectés.
