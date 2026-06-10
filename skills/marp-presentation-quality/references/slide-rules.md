# Marp Slide Constraints & Visual Rules

## Slide Dimensions

Default Marp slide (16:9):
- **Width:** 1920px (1280px at 1x scale)
- **Height:** 1080px (720px at 1x scale)
- **Aspect ratio:** 16:9

## Content Area

With default padding of 50px on each side:
| Area | Start (from top) | End (from bottom) | Available height |
|---|---|---|---|
| Content | 50px from top | 50px from bottom | 980px |
| Title area (with header) | ~120px from top | — | ~910px |

**Marp auto-reserves:**
- ~70px for header (when enabled)
- ~40px for footer/pagination (when enabled)

## Content Formatting Rules

- **RULE-CF-01:** Never use em dashes (---) or en dashes (--) in slide content. Use a regular hyphen (-) or colon (:) instead.
- **RULE-CF-02:** Bullet spacing: the theme handles `::before` pseudo-element spacing via `padding-right: 8px`. Do not add inline `padding-left` or `margin-left` overrides on `ul` or `li::before` in scoped styles — they do not override theme pseudo-element selectors.

## Typography Rules

### Font size guidelines (content slides)

| Content type | Recommended size | Max lines before overflow risk |
|---|---|---|
| Title (h1) | 36-44pt (cargobeamer: 40pt, unihalle: 1.4em ~34pt) | 1 line |
| Subtitle (h2) | 28-34pt (cargobeamer: 32pt, unihalle: 1.1em ~26pt) | 1-2 lines |
| Section header (h3) | 24-28pt | 1-2 lines |
| Body text | 20-24pt (cargobeamer: 24pt, unihalle: 0.9em ~22pt) | 12-15 lines |
| Bullet lists | 20-24pt | 10-12 items |
| Code blocks | 16-20pt | 15-20 lines |
| Table content | 18-22pt | 5-8 rows |
| Footnotes | 14-16pt | — |

### 7-Level Hierarchy Scale

| Level | Size (pt) | Weight | Line Height | Letter Spacing | Usage |
|-------|-----------|--------|-------------|----------------|-------|
| Large Title | 48 | 700 | 1.1 | 0 | Deck title only |
| Title 1 (h1) | 40 | 700 | 1.1 | 0 | Slide headings |
| Title 2 (h2) | 28 | 600 | 1.15 | 0.01em | Section subheadings |
| Headline (h3) | 22 | 500 | 1.2 | 0.01em | Card titles |
| Body | 18-20 | 400 | 1.5 | 0.02em | Main content |
| Caption | 14 | 400 | 1.4 | 0.03em | Notes, footnotes |
| Small | 12 | 400 | 1.3 | 0 | Decorative, legal |

### Typography Hard Rules
- **RULE-TY-01:** Body text must be ≥14px and ≤24px
- **RULE-TY-02:** Heading-to-body contrast ratio must be ≥2:1 (size) or weight difference ≥200
- **RULE-TY-03:** Max 3 font families per deck
- **RULE-TY-04:** Line height must be 1.4–1.6× for body, 1.1–1.3× for headings
- **RULE-TY-05:** No text under 10px anywhere on slide (FAIL)
- **RULE-TY-06:** Max line length ≤75ch for multi-line body text
- **RULE-TY-07:** Avoid light font weights (<400) on projected slides (thin text disappears in bright rooms)

### Safe content limits per slide

| Scenario | Recommended max | Overflow risk |
|---|---|---|
| Body text only (scannable) | 40-60 words | >80 words |
| Bullet list (no sub-items) | 5-6 items | >8 items |
| Nested lists | 3-4 top-level items | >6 top-level items |
| Text + table | 100 words + 5 rows | — |
| Code block | 15-20 lines (80 char width) | >25 lines |
| Image full-width | 1 image | >1 image + text |
| Quote block | 50-80 words | >120 words |

## Layout Rules

### Bento Grid Layout Templates

| # | Template | Columns | Best For |
|---|----------|---------|----------|
| 1 | Full-bleed (no grid) | 1 | Hero/title slides, section dividers |
| 2 | 2-column symmetric | 2 equal | Compare-contrast |
| 3 | 2-column asymmetric | 60:40 or 70:30 | Content + supporting visual |
| 4 | 3-column | 3 equal | Data dashboards, feature lists |
| 5 | 4-card bento (2×2) | 2×2 grid | Dense information quadrants |
| 6 | 6-card bento (3×2) | 3×2 grid | Gallery, team, use cases |
| 7 | Center-aligned single | 1 center | Quotes, key numbers, CTAs |

### Visual Hierarchy Rules
- **Z-pattern**: Top-left to bottom-right natural reading. Key message in top-left.
- **F-pattern**: For text-heavy slides, users scan top line then left edge. Bold/color leading words.
- **Rule of thirds**: Place focal points at imaginary 3×3 grid intersections.
- **Whitespace**: Minimum 10% of slide area empty. Aim for 30-40% title slides, 15-25% content.

### Layout Hard Rules
- **RULE-LY-01:** All slides must be 16:9 ratio (1280×720 minimum)
- **RULE-LY-02:** Left/right margins ≥40px on content slides
- **RULE-LY-03:** Top/bottom margins ≥30px on content slides
- **RULE-LY-04:** Card/container border-radius must be consistent (±2px within deck)
- **RULE-LY-05:** No elements overflowing slide bounds (FAIL)
- **RULE-LY-06:** Whitespace must occupy ≥10% of slide area
- **RULE-LY-07:** Max 5+/-2 content items per slide (FAIL if >8)

### First line proximity to top
- First content after header should start **120-160px** from slide top edge
- If closer than 100px: text too large or padding insufficient
- If further than 200px: text too small or excessive padding

### Last line proximity to bottom
- Content should end **80-120px** from slide bottom edge (above footer)
- If content extends below 60px from bottom → **overflow risk** (text will be cut in PDF)
- If more than 150px space at bottom: text could be larger

## Color & Contrast Rules

### Palette Structure
- Base (1 color) — slide background
- Surface (1-2 colors) — card/container backgrounds
- Primary (1-2 colors) — main brand color, used sparingly
- Accent (1-2 colors) — highlights, CTAs, data emphasis
- Text (3 colors) — high-contrast body, medium secondary, low decorative

### Color Hard Rules
- **RULE-CO-01:** All text-background pairs must pass WCAG AA (4.5:1 body, 3:1 large text)
- **RULE-CO-02:** No red-green pairs for data differentiation (protanopia/deuteranopia)
- **RULE-CO-03:** Color palette must have ≤5 distinct colors per slide (decorative gradients excluded)

## Density Rules

- **RULE-DE-01:** Per-page card budget: max 4 cards, max 4 items per card
- **RULE-DE-02:** Per-page chart budget: max 1-2 complex charts per slide
- **RULE-DE-03:** Decoration elements ≤ 20% of total DOM nodes on the page

## Text Overflow Detection Heuristic

```python
SLIDE_HEIGHT = 1080
HEADER_HEIGHT = 70
FOOTER_HEIGHT = 40
PADDING_TOP = 50
PADDING_BOTTOM = 50
CONTENT_AREA = SLIDE_HEIGHT - HEADER_HEIGHT - FOOTER_HEIGHT - PADDING_TOP - PADDING_BOTTOM  # ~870px

def estimate_content_height(text_content, font_size_pt, line_height):
    lines = count_rendered_lines(text_content, font_size_pt)
    return lines * font_size_pt * line_height * 1.33  # pt to px

def is_overflowing(content_height):
    return (CONTENT_AREA - content_height) < 60  # less than 60px margin = overflow

def is_too_small(content_height):
    return (CONTENT_AREA - content_height) > 150  # more than 150px empty = too small
```

## CSS Safety Measures

```css
section {
  overflow: hidden;
}

section {
  font-size: clamp(18pt, 2.5vw, 28pt);
}

h1 {
  font-size: clamp(28pt, 4vw, 44pt);
}
```

## Failure Mode Catalog (Anti-Patterns)

| ID | Failure Mode | Detection Method |
|----|-------------|-----------------|
| F1 | **Underfill** — Not enough content for page density budget | Pixel analysis: too few DOM elements, large empty areas |
| F2 | **Overfill** — Content exceeds available space, overflow/cutoff | CSS overflow detection, pixel analysis at edges |
| F3 | **Decorative substitution** — Decorative elements replacing content cards | DOM audit: decoration count vs content card count |
| F4 | **Inconsistent spacing** — Different margins/padding on similar elements | CSS computed style comparison across cards |
| F5 | **Font size creep** — Body text too large/small relative to hierarchy | CSS cascade audit against defined scale |
| F6 | **Contrast failure** — Text-background below WCAG threshold | Color contrast computation from CSS variables |
| F7 | **Card misalignment** — Grid items not aligned to layout spec | Bounding box comparison from rendered layout |
| F8 | **Narrative disconnect** — Slides don't form coherent story arc | Sequential content analysis via LLM |

## Theme-Specific Constraints

### cargobeamer
- **Padding:** 50px all sides
- **Body font:** Axiforma 24pt, line-height 1.6
- **h1:** 40pt with bottom border
- **Logo:** background-image top-left (150px wide, 30px offset)
- **Max bullet items:** 8-9 per slide
- **Card border:** 0.75px solid #6EC8FF
- **Table header:** #B6E3FF bg, black text

### unihalle
- **Padding:** 50px all sides
- **Body font:** Helvetica 0.9em (~22pt), line-height 1.4
- **h1:** 1.4em (~34pt), color #9FBF47
- **h2:** 1.1em (~26pt), color #295A97
- **Max bullet items:** 10-12 per slide (more compact)
- **Table header:** #295A97 bg, white text

## AI Prompt Template for Slide Generation

```
Create a slide with the following constraints:
- Theme: {cargobeamer|unihalle}
- Layout template: {bento-1|bento-2sym|bento-2asym|bento-3|bento-4|bento-6|bento-center}
- Slide type: {title|content|section-break|table|cards|quote|agenda}
- Max content: {content_limit}
- Font sizes: h1={h1_size}, h2={h2_size}, body={body_size}
- Padding: 50px all sides
- Ensure at least 60px margin from bottom edge
- Use at most {max_lines} lines of body text
- Bullet points should be concise (1 line each max)
- Max {max_bullets} bullet items per slide
```
