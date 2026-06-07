# Marp Presentation Tools

A collection of tools, themes, documentation, and AI agent skills for creating,
validating, and exporting Marp markdown presentations.

## Repository Structure

```
marp-presentation-tools/
├── themes/                         # Marp CSS theme files
│   ├── cargobeamer.css            # CargoBeamer brand theme
│   └── unihalle.css               # MLU Halle-Wittenberg theme
│
├── tools/                          # Python helper scripts
│   ├── presentation-quality/       # Slide overflow detection
│   │   └── analyze_slides.py      # md → PDF → PNG → pixel analysis
│   ├── slide-fixes/                # Automated slide layout fixes
│   │   ├── fix_slides.py           # UJM slide layout v1
│   │   └── fix_slides2.py          # UJM slide layout v2
│   └── bib-format/                 # Bibliography formatting
│       ├── format_apa.py           # APA citation formatter
│       └── format_apa_updated.py   # Improved APA version
│
├── tests/                          # Test inputs and outputs
│   ├── tools/                      # Test markdown/diagram files
│   │   ├── marp-test.md            # Marp theme visual test
│   │   ├── mermaid-test.md         # Mermaid flowchart test
│   │   ├── test-pandoc.md          # Pandoc reveal.js test
│   │   ├── test.puml               # PlantUML test
│   │   ├── excalidraw-test.excalidraw
│   │   └── drawio-test.drawio.svg
│   └── format-tests/               # Output artifacts (pptx, pdf, html)
│
├── docs/                           # Documentation
│   └── slide-rules.md              # Layout constraints & best practices
│
├── skills/                         # Kilo/Claude AI agent skills
│   ├── marp-presentation-creator/  # Skill: create Marp presentations
│   └── marp-presentation-quality/  # Skill: validate slide quality
│
├── .marprc                         # Global Marp CLI config (for reference)
├── .vscode/                        # VS Code workspace settings
│   └── settings.json
└── README.md                       # This file
```

## Quick Start

### Themes

Two Marp themes are available:

| Theme | Usage | Brand |
|---|---|---|
| `cargobeamer` | Business presentations | CargoBeamer (blue/dark navy palette) |
| `unihalle` | University presentations | MLU Halle-Wittenberg (green/blue palette) |

Add to your Marp frontmatter:
```yaml
---
marp: true
theme: cargobeamer   # or: unihalle
paginate: true
---
```

### Installation (one-time)

To use themes from anywhere:

**VS Code** — Add to `~/.config/Code/User/settings.json`:
```json
"markdown.marp.themes": [
  "https://raw.githubusercontent.com/samshady/marp-vs-code-css-styles/refs/heads/master/cargobeamer.css",
  "https://raw.githubusercontent.com/samshady/marp-vs-code-css-styles/refs/heads/master/unihalle.css"
]
```

**CLI** — Create `~/.marprc`:
```yaml
themeSet:
  - https://raw.githubusercontent.com/samshady/marp-vs-code-css-styles/refs/heads/master/cargobeamer.css
  - https://raw.githubusercontent.com/samshady/marp-vs-code-css-styles/refs/heads/master/unihalle.css
html: true
```

Now `theme: cargobeamer` or `theme: unihalle` works from **any directory**.

### Export

```bash
# PDF
npx @marp-team/marp-cli --pdf --allow-local-files presentation.md

# PPTX (use --image-scale 4 for crisp output)
npx @marp-team/marp-cli --pptx --image-scale 4 --allow-local-files presentation.md
```

### Validate slide quality

```bash
python3 tools/presentation-quality/analyze_slides.py presentation.md
```

Output:
```
── Slide 1 ──
  ✅ OK
     Content height: 420px
     Bottom margin:  42.0pt

── Slide 2 ──
  ❌ OVERFLOW: Content too close to bottom edge!
     Bottom margin: 4.0pt (min 10pt)
```

## Brand Colors

### CargoBeamer (`cargobeamer.css`)

| Role | Hex | Usage |
|---|---|---|
| Dark Blue | `#00132B` | h2-h6 headings |
| Light Blue 01 | `#6EC8FF` | h1, borders, links, accents |
| Light Blue 02 | `#B6E3FF` | Table header bg |
| Light Grey | `#FAFAFB` | Card bg, code bg, alt rows |
| Black | `#000000` | Body text |

Font: **Axiforma** (20pt body, 40pt h1, 28pt h2)

### MLU Halle (`unihalle.css`)

| Role | Hex | Usage |
|---|---|---|
| Green | `#9FBF47` | h1, blockquote border |
| Blue | `#295A97` | h2, strong, table header |
| Grey | `#928781` | header, footer |
| Text | `#282828` | Body |

Font: **Helvetica/Arial** (0.9em body, 1.4em h1)

## AI Agent Skills

Two Kilo-compatible skills are in `skills/`:

1. **marp-presentation-creator** — Creates Marp presentations with the correct
   theme, frontmatter, scoped styles for common slide layouts, brand-aligned
   colors, and export commands. Trigger: "create a [cargobeamer|unihalle] presentation"

2. **marp-presentation-quality** — Validates slides for overflow, underuse,
   inconsistent styling, and content density issues. Trigger: "check/validate/fix
   this presentation"

Install: copy to `~/.kilo/skills/` or reference in your agent config.

## Slide Constraints

See `docs/slide-rules.md` for full details. Key limits:

| Metric | cargobeamer | unihalle |
|---|---|---|
| Body font | 20pt | 0.9em (~22pt) |
| Max words/slide | 200-250 | 200-250 |
| Max bullets | 8-9 | 10-12 |
| Body line height | 1.5 | 1.4 |
| Min bottom margin | 10pt | 10pt |

## Related Repositories

- **Theme CSS** → `samshady/marp-vs-code-css-styles` — canonical theme files
  hosted on GitHub Pages
- **Branding assets** → `~/Development/branding/` — local mirror with logo PNGs

## Development

To modify a theme:
1. Edit the `.css` file in `themes/`
2. Copy to `~/Development/branding/` (the git repo for `marp-vs-code-css-styles`)
3. Push to GitHub
4. Test with a local `.md` file and `npx @marp-team/marp-cli`
