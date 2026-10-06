#!/usr/bin/env python3
"""Gestion de la chaine YouTube par l'API officielle (YouTube Data API v3), depuis une session cloud.

Connexion « appareil » (OAuth device flow) : le script affiche un code, on le saisit sur google.com/device,
aucun mot de passe ni secret ne passe par le chat. Portee demandee : https://www.googleapis.com/auth/youtube
(gestion complete de la chaine ; les statistiques detaillees passent par vidIQ et Metricool).

Identifiants : YOUTUBE_CLIENT_ID et YOUTUBE_CLIENT_SECRET, ou le fichier JSON du client OAuth « TV et
peripheriques a saisie limitee » copie dans ~/.youtube_client.json. Le jeton est garde dans ~/.youtube_token.json.
Ni l'un ni l'autre ne vont dans le depot.

Usage :
  python youtube_api.py login
  python youtube_api.py channel                                   # infos + statistiques publiques
  python youtube_api.py videos                                    # vidéos de la chaine (vues, likes)
  python youtube_api.py branding --description-file f.txt --keywords "comptine, ..." --country FR
  python youtube_api.py banner banniere.jpg
  python youtube_api.py playlist "Titre" --description "..." [--videos ID1,ID2]
  python youtube_api.py thumbnail VIDEO_ID image.jpg
  python youtube_api.py video VIDEO_ID [--title ...] [--description-file f.txt] [--tags "a, b"]
"""

import argparse
import json
import os
import sys
import time

import requests

TOKEN = os.path.expanduser("~/.youtube_token.json")
SCOPE = "https://www.googleapis.com/auth/youtube"
API = "https://www.googleapis.com/youtube/v3"
UPLOAD = "https://www.googleapis.com/upload/youtube/v3"


CLIENT_FILE = os.path.expanduser(os.environ.get("YOUTUBE_CLIENT_FILE", "~/.youtube_client.json"))


def client():
    """Identifiants du client OAuth : variables d'environnement, sinon le JSON telecharge depuis Google Cloud
    (copie privee dans ~/.youtube_client.json, jamais dans le depot)."""
    cid, secret = os.environ.get("YOUTUBE_CLIENT_ID"), os.environ.get("YOUTUBE_CLIENT_SECRET")
    if (not cid or not secret) and os.path.exists(CLIENT_FILE):
        c = json.load(open(CLIENT_FILE))
        c = c.get("installed") or c.get("web") or c
        cid, secret = c.get("client_id"), c.get("client_secret")
    if not cid or not secret:
        sys.exit("identifiants absents : YOUTUBE_CLIENT_ID/YOUTUBE_CLIENT_SECRET ou ~/.youtube_client.json")
    return cid, secret


def login():
    cid, secret = client()
    r = requests.post("https://oauth2.googleapis.com/device/code", data={"client_id": cid, "scope": SCOPE}).json()
    if "device_code" not in r:
        sys.exit(f"refus de Google : {r}")
    print(f"Va sur {r['verification_url']} et saisis le code : {r['user_code']}", flush=True)
    interval = r.get("interval", 5)
    while True:
        time.sleep(interval)
        t = requests.post("https://oauth2.googleapis.com/token", data={
            "client_id": cid, "client_secret": secret, "device_code": r["device_code"],
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code"}).json()
        if "access_token" in t:
            t["expires_at"] = time.time() + t["expires_in"] - 60
            fd = os.open(TOKEN, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
            with os.fdopen(fd, "w") as f:
                json.dump(t, f)
            print("Connecte.")
            return
        if t.get("error") == "slow_down":
            interval += 5
        elif t.get("error") != "authorization_pending":
            sys.exit(f"connexion refusee : {t}")


def token():
    if not os.path.exists(TOKEN):
        sys.exit("pas connecte : lancer d'abord `python youtube_api.py login`")
    t = json.load(open(TOKEN))
    if time.time() > t["expires_at"]:
        cid, secret = client()
        n = requests.post("https://oauth2.googleapis.com/token", data={
            "client_id": cid, "client_secret": secret, "refresh_token": t["refresh_token"],
            "grant_type": "refresh_token"}).json()
        if "access_token" not in n:
            sys.exit(f"jeton expire, relancer login : {n}")
        t.update(access_token=n["access_token"], expires_at=time.time() + n["expires_in"] - 60)
        json.dump(t, open(TOKEN, "w"))
    return {"Authorization": f"Bearer {t['access_token']}"}


def call(method, url, **kw):
    r = requests.request(method, url, headers={**token(), **kw.pop("headers", {})}, **kw)
    if r.status_code >= 400:
        sys.exit(f"{method} {url.split('?')[0]} -> {r.status_code} : {r.text[:500]}")
    return r.json() if r.text else {}


def my_channel(parts="snippet,statistics,brandingSettings,contentDetails"):
    return call("GET", f"{API}/channels", params={"part": parts, "mine": "true"})["items"][0]


def cmd_channel(a):
    c = my_channel()
    print(json.dumps({"id": c["id"], "title": c["snippet"]["title"], "description": c["snippet"].get("description"),
                      "statistics": c["statistics"], "branding": c["brandingSettings"].get("channel")},
                     ensure_ascii=False, indent=2))


def cmd_videos(a):
    uploads = my_channel("contentDetails")["contentDetails"]["relatedPlaylists"]["uploads"]
    items = call("GET", f"{API}/playlistItems", params={"part": "contentDetails", "playlistId": uploads,
                                                         "maxResults": 50})["items"]
    ids = ",".join(i["contentDetails"]["videoId"] for i in items)
    if not ids:
        return print("aucune vidéo")
    for v in call("GET", f"{API}/videos", params={"part": "snippet,statistics,status", "id": ids})["items"]:
        s = v["statistics"]
        print(f"{v['id']}  {v['status']['privacyStatus']:8} vues={s.get('viewCount', 0):>6} "
              f"likes={s.get('likeCount', 0):>4}  {v['snippet']['title']}")


def cmd_branding(a):
    c = my_channel("brandingSettings")
    ch = c["brandingSettings"].setdefault("channel", {})
    if a.description_file:
        ch["description"] = open(a.description_file, encoding="utf-8").read().strip()
    if a.keywords:
        ch["keywords"] = " ".join(f'"{k.strip()}"' if " " in k.strip() else k.strip()
                                  for k in a.keywords.split(",") if k.strip())
    if a.title:
        ch["title"] = a.title
    if a.country:
        ch["country"] = a.country
    if a.language:
        ch["defaultLanguage"] = a.language
    # la mise a jour remplace tout brandingSettings : on renvoie l'ensemble (sinon la banniere saute)
    call("PUT", f"{API}/channels", params={"part": "brandingSettings"},
         json={"id": c["id"], "brandingSettings": c["brandingSettings"]})
    print("description et mots-clés de la chaine mis à jour")


def cmd_banner(a):
    with open(a.image, "rb") as f:
        r = call("POST", f"{UPLOAD}/channelBanners/insert", params={"uploadType": "media"},
                 headers={"Content-Type": "image/jpeg" if a.image.lower().endswith(("jpg", "jpeg")) else "image/png"},
                 data=f.read())
    c = my_channel("brandingSettings")
    c["brandingSettings"].setdefault("image", {})["bannerExternalUrl"] = r["url"]
    call("PUT", f"{API}/channels", params={"part": "brandingSettings"},
         json={"id": c["id"], "brandingSettings": c["brandingSettings"]})
    print("bannière posée")


def cmd_playlist(a):
    p = call("POST", f"{API}/playlists", params={"part": "snippet,status"}, json={
        "snippet": {"title": a.title, "description": a.description or "", "defaultLanguage": "fr"},
        "status": {"privacyStatus": "public"}})
    for vid in [v for v in (a.videos or "").split(",") if v]:
        call("POST", f"{API}/playlistItems", params={"part": "snippet"}, json={
            "snippet": {"playlistId": p["id"], "resourceId": {"kind": "youtube#video", "videoId": vid}}})
    print(f"playlist {p['id']} : https://www.youtube.com/playlist?list={p['id']}")


def cmd_thumbnail(a):
    with open(a.image, "rb") as f:
        call("POST", f"{UPLOAD}/thumbnails/set", params={"videoId": a.video_id, "uploadType": "media"},
             headers={"Content-Type": "image/png" if a.image.lower().endswith("png") else "image/jpeg"},
             data=f.read())
    print("miniature posée")


def cmd_video(a):
    v = call("GET", f"{API}/videos", params={"part": "snippet", "id": a.video_id})["items"][0]
    sn = v["snippet"]
    if a.title:
        sn["title"] = a.title
    if a.description_file:
        sn["description"] = open(a.description_file, encoding="utf-8").read().strip()
    if a.tags:
        sn["tags"] = [t.strip() for t in a.tags.split(",") if t.strip()]
    call("PUT", f"{API}/videos", params={"part": "snippet"},
         json={"id": a.video_id, "snippet": {k: sn[k] for k in ("title", "description", "tags", "categoryId",
                                                                 "defaultLanguage") if k in sn}})
    print("vidéo mise à jour")


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("login")
    sub.add_parser("channel")
    sub.add_parser("videos")
    b = sub.add_parser("branding")
    b.add_argument("--description-file")
    b.add_argument("--keywords")
    b.add_argument("--country")
    b.add_argument("--title")
    b.add_argument("--language")
    bn = sub.add_parser("banner")
    bn.add_argument("image")
    pl = sub.add_parser("playlist")
    pl.add_argument("title")
    pl.add_argument("--description")
    pl.add_argument("--videos")
    th = sub.add_parser("thumbnail")
    th.add_argument("video_id")
    th.add_argument("image")
    vd = sub.add_parser("video")
    vd.add_argument("video_id")
    vd.add_argument("--title")
    vd.add_argument("--description-file")
    vd.add_argument("--tags")
    a = p.parse_args()
    if a.cmd == "login":
        return login()
    globals()[f"cmd_{a.cmd}"](a)


if __name__ == "__main__":
    main()
