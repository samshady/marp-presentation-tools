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
- `references/slide-rules.md` — Slide structure constraints, typography scale, layout templates, failure modes

## Workflow

When asked to create a Marp presentation:

### 0. Determine narrative structure and slide count

Before generating slides, plan the deck structure. Use the SCQA framework for executive/strategy decks, or a storytelling arc for narrative-heavy presentations.

**Slide count heuristic**: 1 slide per ~2 minutes. A 30-minute talk = 15-18 slides. Plan to this constraint.

**SCQA Structure** (use for business/strategy):
| Phase | Slides | Purpose |
|-------|--------|---------|
| Situation | 1 (title) | Context we all agree on |
| Complication | 1-2 | What changed / the problem |
| Question + Answer | 2-3 | How we solve it |
| Supporting arguments | 5-8 | Evidence in pyramidal structure |
| Close | 1-2 | Summary, next steps, CTA |

**Storytelling Arc** (use for narrative-heavy):
| Arc Stage | Slide Mapping |
|-----------|---------------|
| Exposition | Context / background |
| Rising action | Challenge / problem details |
| Climax | Key insight / solution reveal |
| Falling action | Implementation details |
| Resolution | Outcome / next steps |

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
- 7 bento grid layout templates available
- Failure mode catalog (F1-F8) for anti-pattern avoidance
- Typography hard rules (RULE-TY-01 through RULE-TY-07)
- Use `<style scoped>` for per-slide layout overrides

### 4. Bento grid layout templates

Choose the layout template that matches the slide's content type:

| # | Template | CSS Grid | Best For |
|---|----------|----------|----------|
| 1 | Full-bleed (no grid) | — | Title, section dividers |
| 2 | 2-col symmetric | `grid-template-columns: 1fr 1fr` | Compare-contrast |
| 3 | 2-col asymmetric 60:40 | `grid-template-columns: 3fr 2fr` | Content + supporting visual |
| 4 | 3-column | `grid-template-columns: 1fr 1fr 1fr` | Feature lists, dashboards |
| 5 | 4-card bento 2×2 | `grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr` | Dense info quadrants |
| 6 | 6-card bento 3×2 | `grid-template-columns: 1fr 1fr 1fr; grid-template-rows: 1fr 1fr` | Gallery, team, use cases |
| 7 | Center single column | `place-items: center; text-align: center` | Quotes, key numbers, CTAs |

```html
<style scoped>
/* 2-col symmetric example */
section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}
/* 4-card bento example */
section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 16px;
}
section > * {
  background: var(--surface, #FAFAFB);
  border: 0.75px solid var(--primary, #6EC8FF);
  border-radius: 8px;
  padding: 16px;
}
</style>
```

### 5. Typography system

Use the 7-level hierarchy scale from `references/slide-rules.md`. Hard rules:
- Body text: ≥14px and ≤24px, line-height 1.4-1.6
- Max 3 font families per deck
- No text under 10px
- Max line length ≤75ch for body text
- Avoid light font weights (<400) on projected slides

### 6. Scoped style templates for common layouts

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

#### Cards layout (unihalle)
Use cards with `#F5F7FA` background, `0.75px solid #295A97` border, rounded corners.

#### Table layout
For cargobeamer: table header `#B6E3FF` bg, black text.
For unihalle: table header `#295A97` bg, white text.

#### Agenda slide
Use scoped styles with `.focus-text` spans for descriptions under each agenda item.

#### Data callout slide
```html
<style scoped>
section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.big-number {
  font-size: 72pt;
  font-weight: 700;
  color: var(--primary, #6EC8FF);
  line-height: 1;
}
.context {
  font-size: 18pt;
  color: var(--text-secondary);
  margin-top: 16px;
}
</style>

<span class="big-number">2.3M</span>
<span class="context">users onboarded in Q1 2026</span>
```

### 7. Rendering

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

### 8. Icons and visual assets

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

### 9. Slide limits per section type

| Type | Max bullets | Max words | Notes |
|---|---|---|---|
| Title | 0 | 15 | Just title + subtitle + author |
| Agenda | 5-7 | 80 | Use .focus-text for descriptions |
| Content | 8-9 | 250 | Split if more content needed |
| Table | 6 rows | 100 | Keep columns to 4 max |
| Cards | 5 cards | 200 | 3-5 points per card |
| Data callout | 0 | 20 | Big number + context line |
| Quote | 0 | 80 | Attribution required |
