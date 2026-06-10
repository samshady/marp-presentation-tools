---
description: Search and fetch icons for Marp presentations from Iconify (free, 275k+ icons) or Noun Project
---
Find icons for Marp presentations. The script is at `$MARAP_ROOT/tools/icons/find-icon.py`. Set `$MARAP_ROOT` to point to this repo:
```bash
export MARP_ROOT=~/Development/marp-presentation-tools
```

Depends on `requests_oauthlib` for Noun Project — `pip install requests_oauthlib`.

## Search icons
/find-icon search <query> [--limit N] [--source iconify|noun|both]
Runs: python3 $MARAP_ROOT/tools/icons/find-icon.py search <query> ...

## Fetch/download an icon
/find-icon fetch <icon-id> [--source iconify|noun] [--color #HEX]
Runs: python3 $MARAP_ROOT/tools/icons/find-icon.py fetch <icon-id> --source <src>

## After fetching
```bash
sed -i 's/currentColor/#6EC8FF/g' icons/*.svg          # color to brand
sed -i 's|src="icons/|src="'$(pwd)'/icons/|g' *.md      # absolute paths for Marp
```

## Collections
/find-icon collections

Iconify: Free, no attribution required, 275k+ icons across 200+ sets.
Noun Project: Attribution required (creative-commons-attribution), OAuth1 auth.
