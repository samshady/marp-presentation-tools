#!/usr/bin/env python3
"""
Icon search and download tool for Marp presentations.
Supports Iconify (free, no auth) and Noun Project (requires API key).

Usage:
  python3 find-icon.py search <query> [--limit N] [--source iconify|noun]
  python3 find-icon.py fetch <icon-id> [--source iconify|noun] [--format svg|png] [--color #HEX] [--output path]
  python3 find-icon.py search-iconify <query>
  python3 find-icon.py search-noun <query>
  python3 find-icon.py fetch-iconify <prefix/name> [--output path]
  python3 find-icon.py fetch-noun <icon-id> [--color #HEX] [--output path]
"""

import argparse
import json
import os
import re
import sys
import urllib.request
import urllib.parse

# ── Noun Project API ──────────────────────────────────────────────────────────
NOUN_KEY = "99ce1dae67a0483aa9d628ca6dc3ff49"
NOUN_SECRET = "a0fa3af69fb144bcb1721bc36f5285e6"
_NOUN_AUTH = None

def _noun_auth():
    global _NOUN_AUTH
    if _NOUN_AUTH is None:
        try:
            from requests_oauthlib import OAuth1
            _NOUN_AUTH = OAuth1(NOUN_KEY, NOUN_SECRET)
        except ImportError:
            sys.exit("requests_oauthlib required for Noun Project: pip install requests_oauthlib")
    return _NOUN_AUTH

def _noun_get(path, params=None):
    import requests
    url = f"https://api.thenounproject.com{path}"
    r = requests.get(url, auth=_noun_auth(), params=params)
    if r.status_code != 200:
        sys.exit(f"Noun Project API error {r.status_code}: {r.text[:200]}")
    return r.json()

def search_noun(query, limit=10):
    data = _noun_get("/v2/icon", {"query": query, "limit": limit, "include_svg": 1})
    return data.get("icons", []), data.get("usage_limits")

def fetch_noun(icon_id, color=None):
    params = {}
    if color:
        params["color"] = color.lstrip("#")
    data = _noun_get(f"/v2/icon/{icon_id}", params)
    icon = data.get("icon", {})
    # For SVG, use the download endpoint
    dl_params = {"filetype": "svg"}
    if color:
        dl_params["color"] = color.lstrip("#")
    dl = _noun_get(f"/v2/icon/{icon_id}/download", dl_params)
    svg_b64 = dl.get("base64_encoded_file", "")
    import base64
    svg_data = base64.b64decode(svg_b64) if svg_b64 else b""
    return {
        "term": icon.get("term", ""),
        "attribution": icon.get("attribution", ""),
        "license": icon.get("license_description", ""),
        "svg_data": svg_data,
        "permalink": icon.get("permalink", ""),
    }

# ── Iconify API ───────────────────────────────────────────────────────────────

ICONIFY_API = "https://api.iconify.design"

def _iconify_get(path):
    url = f"{ICONIFY_API}{path}"
    req = urllib.request.Request(url, headers={"User-Agent": "Marp-Icon-Tool/1.0"})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode())

def search_iconify(query, limit=10):
    data = _iconify_get(f"/search?query={urllib.parse.quote(query)}&limit={limit}")
    icons = data.get("icons", [])
    # Parse prefix/name format
    results = []
    for icon in icons:
        if ":" in icon:
            prefix, name = icon.split(":", 1)
        else:
            prefix, name = "", icon
        results.append({"id": icon, "prefix": prefix, "name": name})
    return results, data.get("collections", {})

def fetch_iconify(icon_id):
    with urllib.request.urlopen(f"{ICONIFY_API}/{icon_id}.svg") as r:
        svg_data = r.read()
    return {"svg_data": svg_data, "id": icon_id}

def list_iconify_collections(limit=20):
    data = _iconify_get("/collections")
    items = list(data.items())[:limit]
    return [{"id": k, "name": v.get("name", ""), "prefix": k} for k, v in items]

# ── CLI ───────────────────────────────────────────────────────────────────────

def cmd_search(args):
    if args.source == "iconify" or args.source == "both":
        results, _ = search_iconify(args.query, args.limit)
        print(f"\n=== Iconify ({len(results)} results) ===")
        for r in results:
            coll = f"[{r['prefix']}]" if r['prefix'] else ""
            print(f"  {coll} {r['id']}")
        print(f"\n  Fetch: python3 find-icon.py fetch '{results[0]['id']}' --source iconify")

    if args.source == "noun" or args.source == "both":
        results, usage = search_noun(args.query, args.limit)
        print(f"\n=== Noun Project ({len(results)} results) ===")
        print(f"  Monthly usage: {usage}")
        for r in results:
            styles = ", ".join(s["style"] for s in r.get("styles", [])) if r.get("styles") else "—"
            print(f"  ID {r['id']}: {r['term']} [{styles}] — {r.get('attribution','')}")
        print(f"\n  Fetch: python3 find-icon.py fetch {results[0]['id']} --source noun")
        print(f"  Attribution required: {results[0].get('license_description','')}")

def cmd_fetch(args):
    out = args.output or "."
    os.makedirs(out, exist_ok=True)

    if args.source == "iconify":
        result = fetch_iconify(args.icon)
        ext = ".svg"
        fname = re.sub(r'[^a-zA-Z0-9_-]', '_', args.icon.replace("/", "_")) + ext
        path = os.path.join(out, fname)
        with open(path, "wb") as f:
            f.write(result["svg_data"])
        print(f"Saved: {path} ({len(result['svg_data'])} bytes)")

    elif args.source == "noun":
        result = fetch_noun(args.icon, args.color)
        ext = ".svg" if result["svg_data"] else ".txt"
        fname = f"noun_{args.icon}{ext}"
        path = os.path.join(out, fname)
        with open(path, "wb") as f:
            f.write(result["svg_data"])
        print(f"Saved: {path} ({len(result['svg_data'])} bytes)")
        if result.get("attribution"):
            print(f"Attribution: {result['attribution']} ({result.get('license','')})")

def cmd_collections(args):
    cols = list_iconify_collections(args.limit)
    print(f"\nIconify Collections ({len(cols)}):")
    for c in cols:
        print(f"  {c['id']}: {c['name']}")
    print("\nSearch within a collection via: python3 find-icon.py search 'query' --limit 5")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Icon search & download for Marp presentations")
    sp = p.add_subparsers(dest="cmd")

    sp_search = sp.add_parser("search", help="Search icons")
    sp_search.add_argument("query")
    sp_search.add_argument("--limit", type=int, default=10)
    sp_search.add_argument("--source", choices=["iconify", "noun", "both"], default="both")

    sp_fetch = sp.add_parser("fetch", help="Download an icon")
    sp_fetch.add_argument("icon", help="Icon ID (Iconify: prefix/name, Noun: numeric ID)")
    sp_fetch.add_argument("--source", choices=["iconify", "noun"], default="iconify")
    sp_fetch.add_argument("--color", help="Color for Noun Project icons, e.g. #295A97")
    sp_fetch.add_argument("--output", "-o", default=".", help="Output directory")

    sp_cols = sp.add_parser("collections", help="List Iconify collections")
    sp_cols.add_argument("--limit", type=int, default=20)

    # Legacy subcommands
    sp_si = sp.add_parser("search-iconify")
    sp_si.add_argument("query")
    sp_si.add_argument("--limit", type=int, default=10)

    sp_sn = sp.add_parser("search-noun")
    sp_sn.add_argument("query")
    sp_sn.add_argument("--limit", type=int, default=10)

    sp_fi = sp.add_parser("fetch-iconify")
    sp_fi.add_argument("icon")
    sp_fi.add_argument("--output", "-o", default=".")

    sp_fn = sp.add_parser("fetch-noun")
    sp_fn.add_argument("icon")
    sp_fn.add_argument("--color")
    sp_fn.add_argument("--output", "-o", default=".")

    args = p.parse_args()

    if args.cmd == "search":
        cmd_search(args)
    elif args.cmd == "fetch":
        cmd_fetch(args)
    elif args.cmd == "collections":
        cmd_collections(args)
    elif args.cmd == "search-iconify":
        args.source = "iconify"
        cmd_search(args)
    elif args.cmd == "search-noun":
        args.source = "noun"
        cmd_search(args)
    elif args.cmd == "fetch-iconify":
        args.source = "iconify"
        cmd_fetch(args)
    elif args.cmd == "fetch-noun":
        args.source = "noun"
        cmd_fetch(args)
    else:
        p.print_help()
