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

### Safe content limits per slide

| Scenario | Recommended max | Overflow risk |
|---|---|---|
| Body text only | 200-250 words | >300 words |
| Bullet list (no sub-items) | 7-9 items | >12 items |
| Nested lists | 5-7 top-level items | >10 top-level items |
| Text + table | 100 words + 5 rows | — |
| Code block | 15-20 lines (80 char width) | >25 lines |
| Image full-width | 1 image | >1 image + text |
| Quote block | 50-80 words | >120 words |

## Layout Rules

### First line proximity to top
- The first content after header should start **120-160px** from the slide top edge
- If closer than 100px: text is too large or padding is insufficient
- If further than 200px: text is too small or excessive padding

### Last line proximity to bottom
- Content should end **80-120px** from the slide bottom edge (above footer)
- If content extends below 60px from bottom → **overflow risk** (text will be cut in PDF)
- If more than 150px space at bottom: text could be larger

## Text Overflow Detection Heuristic

```python
# Pseudocode for overflow detection
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
/* Add to theme CSS to prevent overflow */
section {
  overflow: hidden;
}

/* Responsive font sizing with clamp() */
section {
  font-size: clamp(18pt, 2.5vw, 28pt);
}

h1 {
  font-size: clamp(28pt, 4vw, 44pt);
}
```

## Theme-Specific Constraints

### cargobeamer
- **Padding:** 50px all sides
- **Body font:** Axiforma 24pt, line-height 1.6
- **h1:** 40pt with bottom border
- **Logo:** background-image top-left (150px wide, 30px offset)
- **Max bullet items:** 8-9 per slide

### unihalle
- **Padding:** 50px all sides
- **Body font:** Helvetica 0.9em (~22pt), line-height 1.4
- **h1:** 1.4em (~34pt), color #9FBF47
- **h2:** 1.1em (~26pt), color #295A97
- **Max bullet items:** 10-12 per slide (more compact)

## AI Prompt Template for Slide Generation

```
Create a slide with the following constraints:
- Theme: {cargobeamer|unihalle}
- Slide type: {title|content|section-break}
- Max content: {content_limit}
- Font sizes: h1={h1_size}, h2={h2_size}, body={body_size}
- Padding: 50px all sides
- Ensure at least 60px margin from bottom edge
- Use at most {max_lines} lines of body text
- Bullet points should be concise (1 line each max)
```
