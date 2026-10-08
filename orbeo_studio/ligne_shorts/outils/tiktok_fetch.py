#!/usr/bin/env python3
"""Telecharge une video TikTok publique et ses informations (vues, likes, son, legende) pour l'analyser.

Usage : python tiktok_fetch.py URL [URL ...] --out dossier
Pour l'analyse seulement (etude de references), jamais pour republier : les videos restent a leurs auteurs.
"""
import argparse
import json
import os
import re
import sys

import requests

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/128.0 Safari/537.36")


def fetch(url, out):
    s = requests.Session()
    s.headers.update({"User-Agent": UA, "Accept-Language": "fr-FR,fr;q=0.9,en;q=0.8"})
    if "vm.tiktok.com" in url or "/t/" in url:  # lien court de partage
        url = s.get(url, allow_redirects=True, timeout=30).url
    h = s.get(url, timeout=30).text
    m = re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__" type="application/json">(.*?)</script>', h, re.S)
    if not m:
        raise RuntimeError("page sans donnees (video privee, supprimee ou blocage)")
    item = json.loads(m.group(1))["__DEFAULT_SCOPE__"]["webapp.video-detail"]["itemInfo"]["itemStruct"]
    vid = item["id"]
    author = item.get("author", {}).get("uniqueId", "inconnu")
    base = os.path.join(out, f"{author}_{vid}")
    v = item["video"]
    for addr in (v.get("playAddr"), v.get("downloadAddr")):
        if not addr:
            continue
        r = s.get(addr, headers={"Referer": "https://www.tiktok.com/"}, timeout=120)
        if r.ok and len(r.content) > 50_000:
            open(base + ".mp4", "wb").write(r.content)
            break
    else:
        raise RuntimeError("fichier video inaccessible")
    info = {
        "url": url, "id": vid, "auteur": author, "abonnes_auteur": item.get("authorStats", {}).get("followerCount"),
        "legende": item.get("desc"), "date": item.get("createTime"), "duree_s": v.get("duration"),
        "stats": item.get("stats"), "son": {"titre": item.get("music", {}).get("title"),
                                           "auteur": item.get("music", {}).get("authorName"),
                                           "original": item.get("music", {}).get("original")},
        "hashtags": [c.get("title") for c in item.get("challenges", [])],
        "etiquette_ia": item.get("IsAigc") or item.get("AIGCDescription"),
    }
    json.dump(info, open(base + ".json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return base, info


def main():
    p = argparse.ArgumentParser()
    p.add_argument("urls", nargs="+")
    p.add_argument("--out", default=".")
    a = p.parse_args()
    os.makedirs(a.out, exist_ok=True)
    for u in a.urls:
        try:
            base, info = fetch(u, a.out)
            st = info["stats"] or {}
            print(f"OK {base}.mp4  {info['duree_s']} s  vues={st.get('playCount')}  likes={st.get('diggCount')}  "
                  f"son={info['son']['titre']} / {info['son']['auteur']}")
        except Exception as e:
            print(f"ECHEC {u} : {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
