---
name: marp-presentation-creator
description: |
  SUB-SKILL: generates individual slides for Marp presentations. Used
  internally by marp-presentation-pipeline. Not typically loaded directly
  unless the user only needs to modify an existing slide's layout, add
  icons, or regenerate a single slide. Handles scoped styles, 10 layout
  templates, icon fetching, brand colors, and PowerPoint/PDF export.
  Supports cargobeamer and unihalle themes.
---

# marp-presentation-creator

## Project root

This repository lives at `~/Development/marp-presentation-tools`. All paths below reference `$MARAP_ROOT = ~/Development/marp-presentation-tools`. When using these skills from a terminal, you can set:
```bash
export MARP_ROOT=~/Development/marp-presentation-tools
```
Or replace `$MARAP_ROOT` with the actual path to this repo wherever it is cloned.

## Assets

- `assets/cargobeamer.css` — The cargobeamer Marp theme (synced from repo)
- `assets/unihalle.css` — The unihalle Marp theme (synced from repo)

## References

- `references/cargobeamer-palette.md` — Official brand color palette and typography
- `references/unihalle-palette.md` — MLU brand color palette
- `references/slide-rules.md` — Slide structure constraints, typography scale, layout templates, failure modes

## Workflow

When asked to create a Marp presentation:

### 0. Content formatting rules (MANDATORY)

These rules apply to every piece of text in every slide:

- **Never use em dashes (---) or en dashes (--) in content text.** Use a regular hyphen (-) or a colon (:) instead. Example: write "Cognitive Load Theory - Mayer's 12 principles" not "Cognitive Load Theory --- Mayer's 12 principles".
- **Use concise bullet points** - one line each, under 10 words per bullet where possible
- **Vary content density across slides** - mix dense content slides with lighter slides containing icons or whitespace

### 1. Determine narrative structure and slide count

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

### 2. Determine theme from context

| If user mentions | Use theme | Logo |
|---|---|---|
| CargoBeamer, CB, claims, business, confidential | `cargobeamer` | Auto via CSS background |
| MLU, Uni Halle, university, seminar, Projektseminar | `unihalle` | Auto via CSS `background-image` on section |

### 3. Create the markdown file

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

### 4. Slide structure constraints

Refer to `references/slide-rules.md` for:
- Max words per slide: 40-60 for content slides (short, scannable bullets), up to 100 for data slides
- Max bullet items: 5-6 per slide, never more than 7
- Font sizes: h1=40pt/1.4em, h2=28pt/1.1em, body=20pt/0.9em
- Bottom margin should be >10pt (use overflow: hidden on sections)
- 7 bento grid layout templates available
- Failure mode catalog (F1-F8) for anti-pattern avoidance
- Typography hard rules (RULE-TY-01 through RULE-TY-07)
- Use `<style scoped>` for per-slide layout overrides
- **Use short scannable bullets** - prefer pipe-separated inline text in cards over stacked bullet lists

### 5. Multi-column card layouts (CRITICAL)

For any slide with cards or multiple columns, you MUST follow this exact pattern. Marp's internal `<section>` rendering breaks nested flexbox/grid layouts unless you reset `section { display: block; }` first.

**CRITICAL RULES for card layouts:**
1. Always set `section { display: block; }` in the scoped style when using card rows
2. Wrap cards in a `<div class="card-row">` container, NOT a `<section>`
3. Use `display: flex` with `flex: 1` and `min-width: 0` on cards
4. Set `width: 100%` on the row container
5. Never override `section` display to `flex` or `grid` for multi-card layouts - Marp's h1 header and logo clash with it

**Card row pattern (2-4 cards, equal width):**
```html
<div class="card-row">

<div class="card">
<h3>Title</h3>
Compact content here | Use pipes | For short items
</div>

<div class="card">
<h3>Title</h3>
More compact | Content | Here
</div>

</div>

<style scoped>
section { display: block; }
.card-row {
  display: flex;
  gap: 14px;
  width: 100%;
  margin-top: 20px;
}
.card {
  flex: 1 1 0;
  min-width: 0;
  background: #FAFAFB;
  border: 0.75px solid #6EC8FF;
  border-radius: 8px;
  padding: 14px;
  font-size: 15pt;
  line-height: 1.5;
}
.card h3 {
  font-size: 20pt;
  font-weight: 600;
  color: #6EC8FF;
  margin: 0 0 8px 0;
}
</style>
```

**Content limits per card layout:**

| Number of cards | Max items per card | Best for |
|----------------|-------------------|----------|
| 2 cards | 5 items each | Compare and contrast |
| 3 cards | 4 items each | Pipeline stages, feature sets |
| 4 cards | 3 items each | Roadmap phases, quadrants |
| Grid 2x2 (4 cards) | 3 items each | Dense information |

### 6. Callout / emphasis layout (alternative to card rows)

For highlighting a single key finding or recommendation, use a centered callout box with optional supporting mini-cards below:

```html
# Slide Title

<div class="callout">

<span class="big-number">Key Finding</span>
<span class="callout-text">One sentence explaining the key finding or recommendation.</span>

</div>

<div class="callout-row">

<div class="mini-card">
  <span class="label">Supporting Point 1</span>
  Brief explanation here
</div>

<div class="mini-card">
  <span class="label">Supporting Point 2</span>
  Brief explanation here
</div>

</div>

<style scoped>
section { display: block; }
.callout {
  text-align: center;
  margin: 24px 0 20px 0;
  padding: 24px;
  background: #FAFAFB;
  border: 1.5px solid #6EC8FF;
  border-radius: 12px;
}
.big-number {
  display: block;
  font-size: 36pt;
  font-weight: 700;
  color: #6EC8FF;
  line-height: 1.2;
  margin-bottom: 10px;
}
.callout-text {
  display: block;
  font-size: 17pt;
  line-height: 1.5;
  color: #000;
}
.callout-row {
  display: flex;
  gap: 14px;
  width: 100%;
}
.mini-card {
  flex: 1 1 0;
  background: #FAFAFB;
  border: 0.75px solid #B6E3FF;
  border-radius: 8px;
  padding: 14px;
  font-size: 14pt;
  line-height: 1.4;
}
.label {
  display: block;
  font-size: 11pt;
  font-weight: 700;
  color: #00132B;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 6px;
}
</style>
```

Use this layout when you have 1 key message + 2 supporting details. Best for: findings, recommendations, conclusions, call-to-action slides.

### 7. Stat-row layout (data-focused)

For presenting key metrics or WCAG criteria, use a top row of stat cards + optional blockquote + bottom row of detail cards:

```html
# Slide Title

<div class="data-row">

<div class="data-card">
  <span class="stat">4.5:1</span>
  <span class="stat-label">WCAG AA body contrast</span>
</div>

<div class="data-card">
  <span class="stat">3:1</span>
  <span class="stat-label">Large text minimum</span>
</div>

</div>

><span style="color:#6EC8FF; font-weight:700">Principle:</span> Key guidance text here.

<div class="vis-row">

<div class="vis-card">
  <img src="icons/icon.svg" width="40" />
  <h4>Category</h4>
  <p>Brief description</p>
</div>

<div class="vis-card">
  <img src="icons/icon.svg" width="40" />
  <h4>Category</h4>
  <p>Brief description</p>
</div>

</div>

<style scoped>
section { display: block; }
.data-row {
  display: flex;
  gap: 20px;
  width: 100%;
  margin-bottom: 20px;
}
.data-card {
  flex: 1 1 0;
  text-align: center;
  background: #FAFAFB;
  border: 0.75px solid #6EC8FF;
  border-radius: 10px;
  padding: 16px;
}
.stat {
  display: block;
  font-size: 42pt;
  font-weight: 700;
  color: #6EC8FF;
  line-height: 1;
  margin-bottom: 6px;
}
.stat-label {
  display: block;
  font-size: 13pt;
  line-height: 1.3;
  color: #00132B;
}
blockquote {
  margin: 0 0 18px 0;
}
.vis-row {
  display: flex;
  gap: 14px;
  width: 100%;
}
.vis-card {
  flex: 1 1 0;
  background: #FAFAFB;
  border: 0.75px solid #B6E3FF;
  border-radius: 8px;
  padding: 14px;
}
.vis-card h4 {
  font-size: 14pt;
  font-weight: 700;
  color: #00132B;
  margin: 6px 0 4px 0;
}
.vis-card p {
  font-size: 12pt;
  margin: 0;
  line-height: 1.4;
  color: #000;
}
</style>
```

Use this layout for data-heavy content: metrics, specifications, criteria, benchmarks.

### 8. Asymmetric callout + stacked cards layout

For pairing a main emphasis point with supporting details on the side:

```html
# Slide Title

<div class="asym-row">

<div class="asym-main">
  <span class="asym-number">SCQA</span>
  <span class="asym-desc">Situation > Complication > Question > Answer</span>
  <hr class="asym-divider" />
  <span class="asym-number">1:2</span>
  <span class="asym-desc">Pacing ratio - 1 slide per 2 minutes</span>
</div>

<div class="asym-side">
  <div class="asym-card">
    <span class="card-id">F2</span>
    <span class="card-name">Overfill</span>
    <span class="card-fix">Reduce content</span>
  </div>
  <div class="asym-card">
    <span class="card-id">F6</span>
    <span class="card-name">Contrast Failure</span>
    <span class="card-fix">Adjust colors</span>
  </div>
</div>

</div>

<style scoped>
section { display: block; }
.asym-row {
  display: flex;
  gap: 24px;
  width: 100%;
  margin-top: 10px;
}
.asym-main {
  flex: 2;
  padding: 24px;
  background: #FAFAFB;
  border: 1.5px solid #6EC8FF;
  border-radius: 12px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.asym-number {
  display: block;
  font-size: 36pt;
  font-weight: 700;
  color: #6EC8FF;
  line-height: 1.1;
}
.asym-desc {
  display: block;
  font-size: 15pt;
  line-height: 1.4;
  margin-top: 6px;
  color: #000;
}
.asym-divider {
  border: none;
  border-top: 1px solid #B6E3FF;
  margin: 16px auto;
  width: 60%;
}
.asym-side {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.asym-card {
  flex: 1;
  background: #FAFAFB;
  border-radius: 8px;
  padding: 12px;
  border-left: 4px solid #6EC8FF;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.card-id {
  font-size: 11pt;
  font-weight: 700;
  color: #00132B;
}
.card-name {
  font-size: 16pt;
  font-weight: 600;
  color: #000;
}
.card-fix {
  font-size: 12pt;
  color: #666;
}
</style>
```

Use this for: process breakdowns, concept + examples, principle + failure modes, question + answers.

### 9. 3x2 Bento grid layout (6-card principle grid)

For presenting 6 related items of equal importance (principles, features, team members):

```html
# Slide Title

<div class="principle-grid">

<div class="principle-card">
  <span class="principle-icon">🧠</span>
  <h3>Title</h3>
  <p>Brief description</p>
</div>

<!-- repeat for 5 more cards -->

</div>

<style scoped>
section { display: block; }
.principle-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 14px;
  margin-top: 16px;
}
.principle-card {
  background: #FAFAFB;
  border: 0.75px solid #6EC8FF;
  border-radius: 10px;
  padding: 16px;
  text-align: center;
}
.principle-icon {
  font-size: 32pt;
  display: block;
  margin-bottom: 6px;
}
.principle-card h3 {
  font-size: 16pt;
  font-weight: 700;
  color: #00132B;
  margin: 0 0 4px 0;
}
.principle-card p {
  font-size: 12pt;
  line-height: 1.4;
  margin: 0;
  color: #000;
}
</style>
```

Use for: feature lists, principle grids, gallery items, key points. Content limit: 1 short title + 1 short sentence per card.

### 10. Horizontal process flow layout

For showing a sequence of steps or pipeline stages:

```html
# Slide Title

<div class="process-flow">

<div class="step">
  <div class="step-number">1</div>
  <h3>Stage A</h3>
  <p>Description of step 1</p>
</div>

<div class="step-arrow">→</div>

<div class="step">
  <div class="step-number">2</div>
  <h3>Stage B</h3>
  <p>Description of step 2</p>
</div>

<div class="step-arrow">→</div>

<div class="step">
  <div class="step-number">3</div>
  <h3>Output</h3>
  <p>Description of result</p>
</div>

</div>

<div class="callout-box">
  <span class="label">Key Insight</span>
  <span class="callout-text">Supporting detail below the flow.</span>
</div>

<style scoped>
section { display: block; }
.process-flow {
  display: flex;
  align-items: center;
  gap: 10px;
  width: 100%;
  margin-top: 24px;
}
.step {
  flex: 1;
  background: #FAFAFB;
  border: 0.75px solid #6EC8FF;
  border-radius: 12px;
  padding: 18px;
  text-align: center;
}
.step-number {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  background: #6EC8FF;
  color: white;
  font-size: 18pt;
  font-weight: 700;
  border-radius: 50%;
  margin-bottom: 10px;
}
.step h3 {
  font-size: 16pt;
  font-weight: 700;
  color: #00132B;
  margin: 0 0 6px 0;
}
.step p {
  font-size: 12pt;
  line-height: 1.4;
  margin: 0;
  color: #000;
}
.step-arrow {
  font-size: 28pt;
  color: #6EC8FF;
  font-weight: 700;
  flex-shrink: 0;
}
.callout-box {
  margin-top: 20px;
  padding: 16px;
  background: #FAFAFB;
  border-left: 4px solid #6EC8FF;
  border-radius: 6px;
}
.callout-box .label {
  display: block;
  font-size: 10pt;
  font-weight: 700;
  color: #6EC8FF;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 4px;
}
.callout-box .callout-text {
  display: block;
  font-size: 14pt;
  line-height: 1.5;
  color: #000;
}
</style>
```

Use for: pipeline stages, workflows, step-by-step processes, timelines. Max 4 steps (3 with arrows), plus optional bottom callout. Content limit: 1 short title + 1 short sentence per step.

### 11. Image + sidebar layout

Pairs a visual (chart, diagram, photo) with supporting commentary. Based on research guidelines:

- **Spatial Contiguity** (Mayer): place related text and graphics near each other. 2-col layout with image on one side, text on the other.
- **Consistent styling**: all images same border radius and border color within a deck.
- **Captions**: directly beneath image, italic, smaller font.
- **Size**: images 50-70% of slide width for content slides. Full-bleed only for hero/section dividers.
- **No 3D or overstyled charts** per Tufte — high data-ink ratio.
- **Absolute paths required**: use full paths like `/home/sam/Development/marp-presentation-tools/output/image.png` (Marp resolves relative paths from CWD, not the markdown file).

```html
# Slide Title

<div class="image-slide">

<div class="image-container">
  <img src="/absolute/path/to/image.png" class="slide-image" />
  <span class="image-caption">Descriptive caption</span>
</div>

<div class="image-sidebar">

<h3>Key Point</h3>
<p>Supporting text related to the visual.</p>

</div>

</div>

<style scoped>
section { display: block; }
.image-slide {
  display: flex;
  gap: 24px;
  margin-top: 14px;
  align-items: flex-start;
}
.image-container { flex: 2; }
.slide-image {
  width: 100%;
  border: 0.75px solid #6EC8FF;
  border-radius: 10px;
  display: block;
}
.image-caption {
  display: block;
  font-size: 11pt;
  color: #666;
  font-style: italic;
  margin-top: 6px;
  text-align: center;
}
.image-sidebar {
  flex: 1;
  background: #FAFAFB;
  border: 0.75px solid #6EC8FF;
  border-radius: 10px;
  padding: 18px;
}
.image-sidebar h3 {
  font-size: 15pt;
  font-weight: 700;
  color: #00132B;
  margin: 0 0 6px 0;
}
.image-sidebar p {
  font-size: 13pt;
  line-height: 1.5;
  margin: 0 0 16px 0;
  color: #000;
}
.image-sidebar p:last-child { margin-bottom: 0; }
</style>
```

Content limit: 1 image + caption, 2-3 text blocks in sidebar.

### 12. Typography system

Use the 7-level hierarchy scale from `references/slide-rules.md`. Hard rules:
- Body text: &gt;=14px and &lt;=24px, line-height 1.4-1.6
- Max 3 font families per deck
- No text under 10px
- Max line length &lt;=75ch for body text
- Avoid light font weights (&lt;400) on projected slides

### 13. Scoped style templates for common layouts

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

### 14. Rendering

**VS Code** — themes are registered globally via VS Code settings (remote URLs), so any `.md` with `theme: cargobeamer` or `theme: unihalle` just works. No local theme files needed.

**CLI** — use `--theme-set` pointing to the repo's theme CSS:
```bash
# PDF with cargobeamer (from anywhere)
npx @marp-team/marp-cli --pdf --theme-set $MARAP_ROOT/themes/cargobeamer.css presentation.md

# PDF with unihalle
npx @marp-team/marp-cli --pdf --theme-set $MARAP_ROOT/themes/unihalle.css --allow-local-files presentation.md

# PPTX
npx @marp-team/marp-cli --pptx --image-scale 4 --theme-set $MARAP_ROOT/themes/cargobeamer.css presentation.md
```

Note: the theme CSS files are pulled from this repo (themes/cargobeamer.css and themes/unihalle.css). Both include the correct logo backgrounds loaded from GitHub URLs, so the logo renders from any directory.

### 15. Icons and visual assets

Icons are REQUIRED for visual variety. Every deck with 6+ slides should have decorative icons on at least 50% of content slides (not title slides). Use the icon search tool to find relevant icons for each slide's topic.

**Important for paths**: Marp resolves `<img src="...">` and `url("...")` relative to its CWD, not the markdown file location. When referencing icons or images:

- If running `marp` from the same directory as your markdown: use `src="./icons/icon.svg"` (relative)
- If running `marp` from a different directory: use `--allow-local-files` and absolute paths
- Best practice: Save icons to `./icons/` next to your `.md` file, and set `sed` to fix paths after fetching

After fetching icons with the find-icon tool, fix the references with:
```bash
# Replace relative paths with absolute ones for Marp
sed -i 's|src="icons/|src="'$(pwd)'/icons/|g' presentation.md
sed -i 's|url("icons/|url("'$(pwd)'/icons/|g' presentation.md
```

When asked to add icons to an existing presentation or create a new one, **detect the theme from the file's frontmatter** and use the correct primary color automatically:

When asked to add icons to an existing presentation or create a new one, **detect the theme from the file's frontmatter** and use the correct primary color automatically:

| Theme | Frontmatter `theme:` | Primary accent color |
|---|---|---|
| `cargobeamer` | `theme: cargobeamer` | `#6EC8FF` (Light Blue) |
| `unihalle` | `theme: unihalle` | `#9FBF47` (MLU Green) |
| `default` | `theme: default` | Ask or use `#295A97` |

Use the icon tool to search and download icons. The tool is at `$MARAP_ROOT/tools/icons/find-icon.py`. Requires `requests_oauthlib` for Noun Project: `pip install requests_oauthlib`. The tool supports two sources:

**Iconify** (free, 275k+ icons, 200+ sets, no attribution needed):
```bash
# Search (from anywhere)
python3 $MARAP_ROOT/tools/icons/find-icon.py search robot --limit 5

# Fetch SVG (save to ./icons directory)
mkdir -p icons
python3 $MARAP_ROOT/tools/icons/find-icon.py fetch tabler:robot --source iconify -o ./icons

# Batch color and fix paths
sed -i 's/currentColor/#6EC8FF/g' icons/*.svg
sed -i 's|src="icons/|src="'$(pwd)'/icons/|g' *.md
```

**Noun Project** (requires attribution, supports custom colors):
```bash
python3 $MARAP_ROOT/tools/icons/find-icon.py search train --source noun
python3 $MARAP_ROOT/tools/icons/find-icon.py fetch 12345 --source noun --color #295A97
```

**Coloring icons**: Edit the downloaded SVG using sed. Use `#6EC8FF` (primary light blue) for cargobeamer icons so they pop on the white background - NOT `#00132B` which looks nearly black. For unihalle use `#9FBF47`:
```bash
# After fetching, hardcode the brand color (use the light/accent color, not dark)
sed -i 's/currentColor/#6EC8FF/g' icons/*.svg
# Verify: check the fill attribute changed
head -1 icons/*.svg | grep -o 'fill="[^"]*"'
```

Then place icons on slides using one of these two methods. **Vary the method across slides** to avoid every slide looking the same:

**Method A - Background-image** (ONLY for subtle decorative accents, not for visible icons):
```markdown
<style scoped>
section {
  background-image: url("icons/material-symbols_lightbulb.svg");
  background-repeat: no-repeat;
  background-position: calc(100% - 60px) 50%;
  background-size: 80px auto;
}
</style>
```
WARNING: background-image places icons BEHIND text. Only use this for very faint decorative elements (opacity 0.1-0.2) or when the icon is not critical to see. For visible icons always use Method B.

**Method B - Inline img tag (PREFERRED for visible icons)** - creates a 2-col layout with icon clearly visible beside text:
```markdown
<div class="two-col">

<div class="main">
- Bullet text here
- More bullets
</div>

<div class="side-icon">
  <img src="icons/material-symbols_lightbulb.svg" width="120" />
</div>

</div>

<style scoped>
.two-col { display: flex; gap: 30px; margin-top: 10px; }
.main { flex: 3; }
.side-icon { flex: 1; display: flex; align-items: center; justify-content: center; }
</style>
```

**Icon placement rules**:
- Read the `theme:` from frontmatter to pick the primary color automatically
- Hardcode the brand color into the SVG using sed. Use the **primary/accent brand color** (e.g. `#6EC8FF` for cargobeamer, `#9FBF47` for unihalle) not the dark text color - icons need to visually pop on white backgrounds
- **VARY icon placement across slides** - use inline `<img>` on some, background-image on others, alternate left/right positioning
- **VARY icon sizes** - use 100-140px for 2-col layouts, 70-100px for background-image, 40-50px inside cards
- Place icons on **every content slide** (not just alternating) - Mayer's Coherence principle says every visual must serve the message, and properly themed icons always do
- Never add decorative icons to title slides (check for `<!-- _class: title -->` or skip the first slide)
- For card layouts, include the icon **inside the card** as a small `<img>` (40-50px) at the top
- Use `flex: 1 1 0` not `flex: 1` on flexbox card children to ensure equal column widths

### 16. Slide limits per section type

| Type | Max items | Max words | Notes |
|---|---|---|---|
| Title | 0 | 15 | Full-bleed, centered |
| Agenda | 5-6 rows | 60 | Table format |
| Content (2-col) | 5-6 bullets | 60 | Short scannable bullets |
| Stat-row | 3 stat cards | 50 | Metrics + blockquote + vis cards |
| Asymmetric | 3 stacked cards | 60 | Main callout left + details right |
| Table | 6 rows | 80 | Keep columns to 4 max |
| Cards (flex row) | 3-5 cards | 40 | 3-4 short items per card |
| **3x2 Bento grid** | **6 cards** | **30** | **1 title + 1 sentence per card** |
| **Process flow** | **3 steps** | **50** | **Horizontal steps + optional callout** |
| Callout / emphasis | 2 mini-cards | 50 | Centered key finding + support |
| Data callout | 0 | 20 | Big number + context line |
| Quote | 0 | 30 | Attribution required |

**Layout variety rule**: Use at least 6 different layout types in any deck of 10+ slides. Never have more than 2 consecutive slides with the same layout. The deck should feel varied, not formulaic.
