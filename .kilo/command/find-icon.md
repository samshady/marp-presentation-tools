---
description: Search and fetch icons for Marp presentations from Iconify (free, 275k+ icons) or Noun Project
---
Find icons for Marp presentations. Depends on `requests_oauthlib` for Noun Project — `pip install requests_oauthlib`.

## Search icons
/find-icon search <query> [--limit N] [--source iconify|noun|both]

Examples:
- /find-icon search chart
- /find-icon search "user profile" --limit 5
- /find-icon search "user profile" --limit 5 --source noun
- /find-icon collections (list icon sets)

## Fetch/download an icon
/find-icon fetch <icon-id> [--source iconify|noun] [--color #HEX]

Examples:
- /find-icon fetch mdi:chart-bar --source iconify
- /find-icon fetch mdi:account --source iconify -o ./assets
- /find-icon fetch 12345 --source noun --color #295A97

## For Marp presentations
After downloading icons, reference them in your markdown:
![](assets/mdi_chart-bar.svg)
Or embed SVG inline in scoped styles.

Iconify: Free, no attribution required, 275k+ icons across 200+ sets.
Noun Project: Attribution required (creative-commons-attribution), OAuth1 auth.
