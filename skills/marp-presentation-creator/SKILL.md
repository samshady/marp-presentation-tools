---
name: marp-presentation-creator
description: |
  Create or modify Marp markdown presentations for CargoBeamer (cargobeamer
  theme) or MLU Halle-Wittenberg (unihalle theme). Also handles adding icons
  and visual assets to existing presentations by detecting the theme from
  frontmatter. Supports scoped styles for common slide layouts (title, agenda,
  cards, tables), brand-aligned colors and typography, slide structure best
  practices, and exporting to PDF and PPTX. This skill should be used when the
  user asks to create, write, generate, or add icons/assets to a Marp
  presentation for either CargoBeamer or university.
---

# marp-presentation-creator

## Assets

- `assets/cargobeamer.css` — The cargobeamer Marp theme (synced from repo)
- `assets/unihalle.css` — The unihalle Marp theme (synced from repo)

## References

- `references/cargobeamer-palette.md` — Official brand color palette and typography
- `references/unihalle-palette.md` — MLU brand color palette
- `references/slide-rules.md` — Slide structure constraints

## Workflow

When asked to create a Marp presentation:

### 1. Determine theme from context

| If user mentions | Use theme | Logo |
|---|---|---|
| CargoBeamer, CB, claims, business, confidential | `cargobeamer` | Auto via CSS background |
| MLU, Uni Halle, university, seminar, Projektseminar | `unihalle` | Auto via CSS `background-image` on section |

### 2. Create the markdown file

**cargobeamer** — logo auto-embedded:
```yaml
---
marp: true
theme: cargobeamer
paginate: true
footer: "Confidential and Proprietary"
---
```

**unihalle** — logo auto-embedded via CSS `background-image` on section (hidden on title slides):
```yaml
---
marp: true
theme: unihalle
paginate: true
header: "Martin-Luther-Universität Halle-Wittenberg"
footer: "Seminar: [Title] | SS-26"
---
```

Use `<!-- _class: title -->` on the first slide to hide the logo.

### 3. Slide structure constraints

Refer to `references/slide-rules.md` for:
- Max words per slide: 200-250
- Max bullet items: 8-9 (cargobeamer), 10-12 (unihalle)
- Font sizes: h1=40pt/1.4em, h2=28pt/1.1em, body=20pt/0.9em
- Bottom margin should be >10pt (use overflow: hidden on sections)
- Use `<style scoped>` for per-slide layout overrides

### 4. Scoped style templates for common layouts

#### Title slide (any theme)
```html
<style scoped>
section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}
</style>
```

#### Cards layout (cargobeamer)
Use cards with `#FAFAFB` background, `0.75px solid #6EC8FF` border, rounded corners.

#### Table layout
For cargobeamer: table header `#B6E3FF` bg, black text.
For unihalle: table header `#295A97` bg, white text.

#### Agenda slide
Use scoped styles with `.focus-text` spans for descriptions under each agenda item.

### 5. Rendering

**VS Code** — themes are registered globally via VS Code settings (remote URLs), so any `.md` with `theme: cargobeamer` or `theme: unihalle` just works.

**CLI** — use `--theme-set` pointing to the local CSS:
```bash
# PDF with cargobeamer (from anywhere)
npx @marp-team/marp-cli --pdf --theme-set ~/Development/marp-presentation-tools/themes/cargobeamer.css presentation.md

# PDF with unihalle
npx @marp-team/marp-cli --pdf --theme-set ~/Development/marp-presentation-tools/themes/unihalle.css --allow-local-files presentation.md

# PPTX
npx @marp-team/marp-cli --pptx --image-scale 4 --theme-set ~/Development/marp-presentation-tools/themes/cargobeamer.css presentation.md
```

### 6. Icons and visual assets

When asked to add icons to an existing presentation, **detect the theme from the file's frontmatter** and use the correct primary color automatically:

| Theme | Frontmatter `theme:` | Primary accent color |
|---|---|---|
| `cargobeamer` | `theme: cargobeamer` | `#6EC8FF` (Light Blue) |
| `unihalle` | `theme: unihalle` | `#9FBF47` (MLU Green) |
| `default` | `theme: default` | Ask or use `#295A97` |

Use the icon tool to search and download icons. Requires `requests_oauthlib` for Noun Project: `pip install requests_oauthlib`. The tool supports two sources:

**Iconify** (free, 275k+ icons, 200+ sets, no attribution needed):
```bash
# Search
python3 ~/Development/marp-presentation-tools/tools/icons/find-icon.py search robot --limit 5

# Fetch SVG
python3 ~/Development/marp-presentation-tools/tools/icons/find-icon.py fetch tabler:robot --source iconify

# Fetch and save to a specific dir
python3 ~/Development/marp-presentation-tools/tools/icons/find-icon.py fetch mdi:computer --source iconify -o ./icons
```

**Noun Project** (requires attribution, supports custom colors):
```bash
python3 ~/Development/marp-presentation-tools/tools/icons/find-icon.py search train --source noun
python3 ~/Development/marp-presentation-tools/tools/icons/find-icon.py fetch 12345 --source noun --color #295A97
```

**Coloring icons**: Edit the downloaded SVG — replace `currentColor` with the theme's primary hex:
- `fill="currentColor"` → `fill="#6EC8FF"` (cargobeamer) or `fill="#9FBF47"` (unihalle)
- `stroke="currentColor"` → `stroke="#6EC8FF"` (cargobeamer) or `stroke="#9FBF47"` (unihalle)

Then place them as decorative background-images via scoped `<style>` — one per slide, never on title slides:

```markdown
<style scoped>
section {
  background-image: url("icons/tabler_robot.svg");
  background-repeat: no-repeat;
  background-position: calc(100% - 60px) 50%;
  background-size: 80px;
}
</style>

## Slide Heading

- Content here...
```

**Icon placement rules**:
- Read the `theme:` from frontmatter to pick the primary color automatically
- Hardcode the brand color into the SVG (`fill`/`stroke` — not `currentColor`)
- Use `background-image` on `section` via scoped `<style>` — not `<img>` tags
- Position with `calc(100% - 60px) 50%` (right side, vertically centered) or `60px 60%` (left side)
- Size: 70-80px for content slides
- Never add decorative icons to title slides (check for `<!-- _class: title -->` or skip the first slide)
- Never use `position: absolute` — it clashes with headers/footers/pagination

### 7. Slide limits per section type

| Type | Max bullets | Max words | Notes |
|---|---|---|---|
| Title | 0 | 15 | Just title + subtitle + author |
| Agenda | 5-7 | 80 | Use .focus-text for descriptions |
| Content | 8-9 | 250 | Split if more content needed |
| Table | 6 rows | 100 | Keep columns to 4 max |
| Cards | 5 cards | 200 | 3-5 points per card |
