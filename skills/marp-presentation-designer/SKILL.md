---
name: marp-presentation-designer
description: |
  Generate and manage visual design contracts for Marp presentations. Creates
  a formal theme-contract.json encoding the full design system (typography,
  spacing, colors, layout templates, chart palettes) for a deck. Can extract
  a contract from existing Marp theme CSS files or generate one from brand
  guidelines. The contract is consumed by marp-presentation-creator for
  consistent per-slide generation and by marp-presentation-quality for
  quantitative CSS/DOM rule checking.
---

# marp-presentation-designer

## References

- `skills/marp-presentation-creator/references/slide-rules.md` — Layout templates, hierarchy scale, spacing rules
- `skills/marp-presentation-creator/references/cargobeamer-palette.md` — Brand colors for cargobeamer
- `skills/marp-presentation-creator/references/unihalle-palette.md` — Brand colors for unihalle

## Workflow

When asked to define, configure, or enforce a visual design system for a presentation:

### 1. Determine the theme / brand

Ask the user or detect from context:
- **cargobeamer** — corporate blue (#6EC8FF primary), Axiforma font, dark text on light bg
- **unihalle** — MLU green (#9FBF47 primary), Helvetica font, dark text on light bg
- **custom** — user provides brand colors, fonts, or a reference

### 2. Generate theme-contract.json

Create a JSON file encoding the full design system. This contract is written to the presentation directory and referenced by both the creator and quality skills.

```json
{
  "theme_name": "cargobeamer|unihalle|custom",
  "slide_size": {"width": 1280, "height": 720, "ratio": "16:9"},
  "typography": {
    "families": ["Axiforma", "Helvetica", "system-ui"],
    "scale": [
      {"name": "display", "size": 48, "weight": 700, "line_height": 1.1},
      {"name": "heading_1", "size": 40, "weight": 700, "line_height": 1.1},
      {"name": "heading_2", "size": 28, "weight": 600, "line_height": 1.15},
      {"name": "heading_3", "size": 22, "weight": 500, "line_height": 1.2},
      {"name": "body", "size": 20, "weight": 400, "line_height": 1.5},
      {"name": "caption", "size": 14, "weight": 400, "line_height": 1.4},
      {"name": "small", "size": 12, "weight": 400, "line_height": 1.3}
    ],
    "min_size_px": 12,
    "contrast_ratio": {"body": 4.5, "large_text": 3.0}
  },
  "spacing": {
    "grid": 8,
    "margin_h": 48,
    "margin_v": 36,
    "card_padding": 24,
    "gap": 16
  },
  "colors": {
    "background": "#FFFFFF",
    "surface": "#FAFAFB",
    "surface_elevated": "#F0F2F5",
    "primary": "#6EC8FF",
    "accent": "#295A97",
    "text_primary": "#1A1A2E",
    "text_secondary": "#6B7280",
    "text_decorative": "#9CA3AF"
  },
  "layouts": {
    "available": ["2-col", "3-col", "bento-4", "bento-6", "hero", "center-single"],
    "card_radius": 8,
    "card_shadow": "0 2px 8px rgba(0,0,0,0.08)"
  },
  "decoration_budget": "medium",
  "chart_palette": ["#6EC8FF", "#295A97", "#9FBF47", "#F59E0B", "#EF4444", "#8B5CF6"]
}
```

For **unihalle** swap primary to `#9FBF47`, accent to `#295A97`, text to dark, background to white.

### 3. Select layout templates per slide type

Based on the planned slide types (from the narrative structure), assign bento grid layouts:

| Slide Content | Recommended Layout | Notes |
|---------------|-------------------|-------|
| Title | Full-bleed (no grid) | Centered, minimal |
| Agenda | 2-col symmetric | Left: items, right: descriptions |
| Section header | Full-bleed | Large headline only |
| Content with text | 2-col asymmetric 60:40 | Main content + supporting visual |
| Content text-only | Center single column | Bullet list, narrow width |
| Feature comparison | 3-column | One feature per column |
| Data dashboard | 4-card bento 2×2 | KPI cards in quadrants |
| Team / gallery | 6-card bento 3×2 | Photo + name + role per card |
| Key insight / quote | Center single column | Large text, centered |
| Data callout | Center single column | Big number + context |

### 4. Write the contract file

Output `theme-contract.json` to the presentation's working directory. Reference this file in the slide generation prompt so all slides share the same design system.

### 5. Verify contract against theme CSS

If the theme already exists as a CSS file, verify the contract matches the actual CSS values:

```bash
# Check that contract colors exist in the theme CSS
grep -E '#[0-9A-Fa-f]{6}' themes/cargobeamer.css | head -10
# Verify font families match
grep 'font-family' themes/cargobeamer.css
```

Flag any discrepancies between the contract and the actual theme CSS.
