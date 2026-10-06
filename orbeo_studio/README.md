# Orbeo Studio : la marque des vidéos IA

Orbeo Studio est le nom commun de toutes les vidéos créées avec l'IA (compte orbeo.studio@gmail.com).
Deux lignes de contenu, rangées chacune à sa place :

| Ligne | Contenu | Où | Public |
|---|---|---|---|
| **Lulu la Luciole** | comptines animées originales (`chaine_lulu/`) | chaîne YouTube actuelle (`UCShPnzacZLkyH4nHZmDZkSg`), vidéos + Shorts des refrains | enfants 1-5 ans (« conçue pour les enfants ») |
| **Shorts IA** | vidéos courtes verticales (9:16, moins de 60 s) | Instagram Reels, TikTok, chaîne YouTube « Orbeo Studio » (à créer) | grand public |

## Pourquoi deux chaînes YouTube plutôt qu'une chaîne avec deux playlists
- Une vidéo « conçue pour les enfants » perd les commentaires, les notifications et la publicité ciblée ; la
  chaîne enfants doit le rester entièrement pour que YouTube la recommande aux bons spectateurs (parents, tout-petits).
- Des Shorts grand public sur la même chaîne mélangeraient deux publics qui ne regardent pas la même chose : les
  abonnés de l'un ne regardent pas l'autre, ce qui fait baisser les recommandations des deux.
- Les deux chaînes peuvent appartenir au même compte Google (YouTube → Paramètres → Ajouter ou gérer vos chaînes
  → Créer une chaîne).
- Metricool : la chaîne Lulu est connectée à la marque `7251650`. Pour publier aussi les Shorts, il faudra
  connecter Instagram, TikTok et la chaîne Orbeo Studio ; vérifier si le plan Metricool permet une 2e marque
  (une marque = une seule chaîne YouTube).

## Identifiants à réserver
`@orbeostudio` sur YouTube, Instagram et TikTok (libre sur YouTube d'après vidIQ le 6 octobre 2026, à confirmer).
Repli : `@orbeo.studio` (Instagram, TikTok) ou `@orbeostudiofr`.

## Biographies
Instagram (150 caractères max) :
```
✨ Petites histoires animées créées avec l'IA
🌙 Les comptines de Lulu la Luciole
🎬 Une nouvelle vidéo chaque semaine
```
TikTok (80 caractères max) :
```
Petites histoires animées créées avec l'IA ✨ Comptines de Lulu la Luciole 🌙
```
Chaîne YouTube Orbeo Studio :
```
Orbeo Studio crée de petites histoires animées avec l'intelligence artificielle : des scènes douces, drôles ou
magiques, en format court, une nouvelle chaque semaine.

Pour les tout-petits, retrouve nos comptines sur la chaîne Lulu la Luciole !
```

## Règles de publication
- Déclarer le contenu IA là où le réseau le demande : TikTok (`isAigc`), Instagram (`isAiGenerated`). Sur YouTube, le
  dessin animé n'entre pas dans la déclaration « contenu modifié ou synthétique » (réservée au contenu réaliste).
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
