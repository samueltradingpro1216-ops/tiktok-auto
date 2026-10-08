"""Recherche preliminaire de marques dans TMview (INPI, EUIPO, OMPI et autres offices). Pas un avis juridique.

Usage : python tmview.py Nom1 Nom2 ... (resultats aussi dans tmview_resultats.json, ou TMVIEW_OUT)
"""
import json, os, sys, time

import requests
URL = "https://www.tmdn.org/tmview/api/search/results?translate=true"
H = {"Content-Type": "application/json", "Accept": "application/json, text/plain, */*",
     "Origin": "https://www.tmdn.org", "Referer": "https://www.tmdn.org/tmview/",
     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"}
CLASSES = {"9", "16", "25", "28", "41"}
OFFICES = {"FR", "EM", "WO", "BX", "GB", "US", "ES", "IT", "DE", "CA", "CH", "BE"}
DEAD = ("expired", "ended", "withdrawn", "refused", "rejected", "cancelled", "surrendered", "lapsed", "invalid")

def search(term, pages=2):
    out = []
    for page in range(1, pages + 1):
        body = {"page": str(page), "pageSize": "100", "criteria": "C", "basicSearch": term, "fOffices": [],
                "fields": ["ST13", "tmName", "tmOffice", "applicationDate", "tradeMarkStatus", "niceClass", "applicantName"]}
        for attempt in range(3):
            try:
                r = requests.post(URL, headers=H, json=body, timeout=60)
                d = r.json()
                break
            except Exception as e:
                time.sleep(5)
        else:
            return None
        out += d.get("tradeMarks", [])
        if page >= d.get("totalPages", 0):
            break
        time.sleep(1)
    return out

res = {}
for term in sys.argv[1:]:
    tms = search(term)
    if tms is None:
        res[term] = {"error": True}
        continue
    live = []
    for t in tms:
        status = str(t.get("tradeMarkStatus", "")).lower()
        classes = {str(c) for c in (t.get("niceClass") or [])}
        if any(k in status for k in DEAD):
            continue
        hit = sorted(classes & CLASSES, key=int)
        if hit and t.get("tmOffice") in OFFICES:
            live.append({"name": t.get("tmName"), "office": t.get("tmOffice"), "classes": hit,
                         "status": t.get("tradeMarkStatus"), "owner": (t.get("applicantName") or [""])[0] if isinstance(t.get("applicantName"), list) else t.get("applicantName"),
                         "date": t.get("applicationDate"), "id": t.get("ST13")})
    res[term] = {"total": len(tms), "live_in_classes": live}
    print(f"{term:20} total={len(tms):4} vivantes(9/16/25/28/41)={len(live):3}  " +
          "; ".join(f"{l['name']} [{l['office']} {','.join(l['classes'])}]" for l in live[:6]), flush=True)
    time.sleep(1.5)
json.dump(res, open(os.environ.get("TMVIEW_OUT", "tmview_resultats.json"), "w"), ensure_ascii=False, indent=1)
