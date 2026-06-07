---
name: marp-presentation-creator
description: |
  Create Marp markdown presentations for CargoBeamer (cargobeamer theme) or MLU
  Halle-Wittenberg (unihalle theme). Handles frontmatter setup, scoped styles for
  common slide layouts (title, agenda, cards, tables), brand-aligned colors and
  typography, slide structure best practices, and exporting to PDF and PPTX.
  This skill should be used when the user asks to create, write, or generate a
  presentation, slide deck, or slide set for either CargoBeamer or university.
---

# marp-presentation-creator

## Assets

- `assets/cargobeamer.css` — The cargobeamer Marp theme (official brand colors)
- `assets/unihalle.css` — The unihalle Marp theme (MLU brand colors)

## References

- `references/cargobeamer-palette.md` — Official brand color palette and typography
- `references/unihalle-palette.md` — MLU brand color palette

## Workflow

When asked to create a Marp presentation:

### 1. Determine theme from context

| If user mentions | Use theme |
|---|---|
| CargoBeamer, CB, claims, business, confidential | `cargobeamer` |
| MLU, Uni Halle, university, seminar, Projektseminar | `unihalle` |

### 2. Create the markdown file with frontmatter

For **cargobeamer**:
```yaml
---
marp: true
theme: cargobeamer
paginate: true
footer: "Confidential and Proprietary"
---
```

For **unihalle**:
```yaml
---
marp: true
theme: unihalle
paginate: true
header: "Martin-Luther-Universität Halle-Wittenberg"
footer: "Seminar: [Title] | SS-26"
---
```

### 3. Follow slide structure constraints

Refer to `references/slide-rules.md` for:
- Max words per slide: 200-250
- Max bullet items: 8-9 (cargobeamer), 10-12 (unihalle)
- Font sizes: h1=40pt/1.4em, h2=28pt/1.1em, body=20pt/0.9em
- Bottom margin should be >10pt (use overflow: hidden on sections)
- Use `<style scoped>` for per-slide layout overrides

### 4. Use these scoped style templates for common layouts

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
h1 { /* larger for title */ }
</style>
```

#### Cards layout (cargobeamer)
Use cards with `#FAFAFB` background, `0.75px solid #6EC8FF` border, rounded corners.

#### Table layout
For cargobeamer: table header `#B6E3FF` bg, black text.
For unihalle: table header `#295A97` bg, white text.

#### Agenda slide
Use scoped styles with `.focus-text` spans for descriptions under each agenda item.

### 5. Logo handling

- **cargobeamer**: Logo is built into the theme via background-image (no manual placement)
- **unihalle**: Place `![header-logo](uni_halle_logo.jpg)` on each slide, theme positions it

### 6. Export commands

```bash
# PDF
npx @marp-team/marp-cli --pdf --allow-local-files presentation.md

# PPTX (high quality for cargobeamer)
npx @marp-team/marp-cli --pptx --image-scale 4 --allow-local-files presentation.md

# PPTX compression (if too large)
# Downscale PNGs in ppt/media/ to max 2560px width, then repack
```

### 7. Slide limits per section type

| Type | Max bullets | Max words | Notes |
|---|---|---|---|
| Title | 0 | 15 | Just title + subtitle + author |
| Agenda | 5-7 | 80 | Use .focus-text for descriptions |
| Content | 8-9 | 250 | Split if more content needed |
| Table | 6 rows | 100 | Keep columns to 4 max |
| Cards | 5 cards | 200 | 3-5 points per card |
