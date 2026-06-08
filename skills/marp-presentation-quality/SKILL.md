---
name: marp-presentation-quality
description: |
  Validate and fix Marp presentation slides for visual quality. Detects text
  overflow, underused space, inconsistent styling, and content density issues
  using pixel analysis and markdown heuristics. This skill should be used when
  the user asks to check, validate, fix, review, or ensure quality of a Marp
  presentation.
---

# marp-presentation-quality

## Scripts

- `scripts/analyze_slides.py` — Render a Marp markdown file to PDF, convert to
  images, and analyze pixel content for overflow/underuse. Exits with code 1
  if any overflow detected.

## References

- `references/slide-rules.md` — Full constraint definitions (dimensions, typography,
  safe limits, overflow detection, theme-specific rules)
- `references/presentation-best-practices.md` — General good presentation design rules

## Workflow

When asked to validate or fix a Marp presentation:

### 1. Analyze slides for overflow

```bash
python3 scripts/analyze_slides.py presentation.md
```

This will:
- Convert to PDF via `npx @marp-team/marp-cli`
- Render pages to PNG via `pdftoppm`
- Scan pixels for content proximity to edges
- Report per-slide: ✅ OK, ❌ OVERFLOW, ⚠ UNDERUSED

### 2. Fix common styling inconsistencies

Use `references/slide-rules.md` to check:

| Check | Target | How to fix |
|---|---|---|
| Font sizes match theme | h1=40pt, h2=28pt, body=20pt (cargobeamer) | Update scoped styles |
| Bottom margin safe | >10pt from bottom | Reduce font size or content |
| Color consistency | Matches brand palette | Replace hex values |
| Bullet density | ≤9 per slide (cargobeamer) | Split slide or condense |
| Table headers styled | `#B6E3FF` (cargobeamer) / `#295A97` (unihalle) | Add scoped styles |
| Card borders | `0.75px solid #6EC8FF` (cargobeamer) | Check card scoped styles |

### 3. Run fix scripts for known patterns

For UJM slide layout fixes in Abschlusspresentation:
```bash
python3 Tools/slide-fixes/fix_slides.py
python3 Tools/slide-fixes/fix_slides2.py
```

### 4. Check icon placement

If the presentation uses decorative icons, verify:

| Check | Rule |
|---|---|
| Icons not on title slides | No `background-image` with icons on `section.title` |
| Icon positioning | Use `calc(100% - Npx)` from right, never `position: absolute` |
| No footer clash | Icons positioned at `50%` vertical, not bottom |
| Color matches theme | SVG hardcodes brand color or uses `currentColor` with parent `color` |

### 5. Generate quality report

After analysis, provide:
- Per-slide overflow warnings (❌)
- Per-slide underuse warnings (⚠)  
- Font/color inconsistencies
- Content density flags (too many bullets/words)

### 5. Overflow detection explained

The `analyze_slides.py` script uses these thresholds:
- **Slide dimensions**: 960x540pt (Marp default 16:9)
- **Content area**: ~870pt after subtracting header/footer/padding
- **Overflow**: content bottom margin < 10pt → text will be cut
- **Underuse**: bottom margin > 60pt → text could be larger
- **Density warning**: >18 estimated rendered lines per slide
