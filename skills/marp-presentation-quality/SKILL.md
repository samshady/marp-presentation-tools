---
name: marp-presentation-quality
description: |
  SUB-SKILL: validates and fixes Marp presentation visual quality. Used
  internally by marp-presentation-pipeline in Stage 4. Can be loaded
  directly when the user says "check this presentation", "run QA", or
  "fix the slides". Detects overflow, underuse, enforces typography rules,
  WCAG contrast, layout constraints, and failure modes (F1-F8).
---

# marp-presentation-quality

## Project root

This repository lives at `~/Development/marp-presentation-tools`. Set `$MARAP_ROOT` to point there:
```bash
export MARP_ROOT=~/Development/marp-presentation-tools
```

## Scripts

The analysis script is at `$MARAP_ROOT/tools/presentation-quality/analyze_slides.py`. Run it from any directory:
```bash
python3 $MARAP_ROOT/tools/presentation-quality/analyze_slides.py presentation.md
python3 $MARAP_ROOT/tools/presentation-quality/analyze_slides.py presentation.md --json
```

## References

- `references/slide-rules.md` — Full constraint definitions (dimensions, typography,
  safe limits, overflow detection, theme-specific rules), bento grid layouts,
  7-level hierarchy scale, WCAG contrast rules, failure mode catalog (F1-F8)
- `references/presentation-best-practices.md` — Mayer's principles, SCQA narrative,
  data viz decision framework, color psychology, WCAG rules

## Workflow

When asked to validate or fix a Marp presentation:

### 1. Analyze slides for overflow

```bash
python3 $MARAP_ROOT/tools/presentation-quality/analyze_slides.py presentation.md
```

For machine-readable output (pipeline consumption):
```bash
python3 $MARAP_ROOT/tools/presentation-quality/analyze_slides.py presentation.md --json > qa-report.json
```

This will:
- Convert to PDF via `npx @marp-team/marp-cli`
- Render pages to PNG via `pdftoppm`
- Scan pixels for content proximity to edges
- Report per-slide: ✅ OK, ❌ OVERFLOW, ⚠ UNDERUSED

### 2. Run quantitative CSS/DOM inspection checks

Use `references/slide-rules.md` to verify these hard rules. Check each by inspecting the rendered HTML output (`npx @marp-team/marp-cli --html presentation.md -o presentation.html` then inspect with Puppeteer/jsdom or manually via browser DevTools):

#### Content Formatting (RULE-CF-01, RULE-CF-02)
| Rule | Check | Target | Fix |
|------|-------|--------|-----|
| CF-01 | Em dash usage | Zero em dashes (---) or en dashes (--) in slide content | Replace with hyphen (-) or colon (:) |
| CF-02 | Bullet spacing | Theme handles via `::before { content: "-- " }` | Do not override in scoped styles |

#### Typography (RULE-TY-01 through RULE-TY-07)
| Rule | Check | Target | Fix |
|------|-------|--------|-----|
| TY-01 | Body text size | ≥14px and ≤24px | Adjust font-size in scoped style |
| TY-02 | Heading-body contrast | ≥2:1 size ratio or ≥200 weight diff | Increase heading size/weight |
| TY-03 | Font family count | ≤3 families per deck | Consolidate fonts |
| TY-04 | Line height | Body: 1.4-1.6, Headings: 1.1-1.3 | Set unitless line-height in CSS |
| TY-05 | Minimum text size | No text <10px (FAIL) | Remove or enlarge tiny elements |
| TY-06 | Line length | ≤75ch for multi-line body | Narrow column width |
| TY-07 | Font weight on projection | ≥400 (Regular) | Avoid Light/Thin weights |

#### Layout (RULE-LY-01 through RULE-LY-07)
| Rule | Check | Target | Fix |
|------|-------|--------|-----|
| LY-01 | Aspect ratio | 16:9 (1280×720 minimum) | Check Marp config |
| LY-02 | Side margins | ≥40px on content slides | Adjust section padding |
| LY-03 | Top/bottom margins | ≥30px on content slides | Adjust section padding |
| LY-04 | Border radius consistency | ±2px across cards | Unify border-radius value |
| LY-05 | Overflow | No elements outside bounds (FAIL) | Reduce content or font size |
| LY-06 | Whitespace | ≥10% of slide area empty | Add spacing or reduce content |
| LY-07 | Item count | Max 5±2 per slide (FAIL if >9) | Split slide or condense |

#### Color & Contrast (RULE-CO-01 through RULE-CO-03)
| Rule | Check | Target | Fix |
|------|-------|--------|-----|
| CO-01 | Text-background contrast | WCAG AA: 4.5:1 body, 3:1 large text | Darken text or lighten bg |
| CO-02 | CVD-safe colors | No red-green data pairs | Use blue-orange or patterns |
| CO-03 | Color count | ≤5 distinct colors per slide | Consolidate to palette |

#### Density (RULE-DE-01 through RULE-DE-03)
| Rule | Check | Target | Fix |
|------|-------|--------|-----|
| DE-01 | Card budget | ≤5 content cards | Merge or remove cards |
| DE-02 | Chart budget | ≤2 charts per slide | Move charts to separate slides |
| DE-03 | Decoration ratio | ≤20% of DOM nodes | Remove excess decorative elements |

### 3. Run fix scripts for known patterns

For UJM slide layout fixes in Abschlusspresentation:
```bash
python3 $MARAP_ROOT/tools/slide-fixes/fix_slides.py
python3 $MARAP_ROOT/tools/slide-fixes/fix_slides2.py
```

### 4. Check failure modes (F1-F8 catalog)

Cross-reference detected issues against the failure mode catalog:
| Issue Pattern | Likely Failure Mode | Fix Protocol |
|---|---|---|
| Too much whitespace, sparse content | F1 Underfill | Add content or merge slides |
| Text cut off, overflow warnings | F2 Overfill | Reduce font or content count |
| Decorative icons with no data cards | F3 Decorative substitution | Replace decoration with content |
| Different margins on similar cards | F4 Inconsistent spacing | Normalize CSS values |
| Body text larger/smaller than scale | F5 Font size creep | Align to hierarchy scale |
| Low contrast detected | F6 Contrast failure | Adjust colors per WCAG |
| Cards misaligned in grid | F7 Card misalignment | Fix grid-template/place-items |
| Disjointed story across slides | F8 Narrative disconnect | Restructure with SCQA/arc |

### 5. Check visual variety

After running all quantitative checks, verify the deck has adequate visual variety:

| Check | Target | Fix |
|-------|--------|-----|
| At least 50% of content slides have decorative icons | Yes | Add background-image icons on alternating slides |
| More than 1 color used across slides | Yes | Use brand color variants (h1=#6EC8FF, h2=#00132B, cards=#FAFAFB, borders=#6EC8FF, accent borders=#00132B) |
| No boxes/borders on all slides | Not every slide should have card borders | Mix flat bullet list slides with card grid slides |
| Slide layouts vary (not all same format) | At least 3 different layout types | Alternate: flat list, table, flex cards, icon + list |

### 6. Run structured VLM quality audit

For semantic checks that pixel/rule analysis can't catch, use a vision-capable model on rendered slide screenshots.

**Stage A - Per-Slide Visual Audit** (after rendering each slide):

```
Evaluate this presentation slide screenshot. Respond ONLY with JSON:
{
  "visual_balance": "good|cluttered_left|cluttered_right|top_heavy|bottom_heavy",
  "text_readability": "good|too_small|too_dense|low_contrast",
  "color_harmony": "good|mismatched|too_many_colors|muddy",
  "whitespace_usage": "good|cramped|wasteful",
  "data_visualization_clarity": "good|confusing|overstyled|unnecessary",
  "content_density": "underfilled|appropriate|overfilled",
  "specific_issues": ["up to 3 actionable issues"],
  "repair_priority": "none|low|medium|high"
}
```

**Stage B — Deck-Wide Narrative Audit** (after all slides):

```
Evaluate this full slide deck for narrative coherence. Check:
1. Does the deck have a clear narrative arc (beginning, middle, end)?
2. Is there a logical progression of ideas?
3. Are there transition gaps (jumps between unrelated concepts)?
4. Is the pacing consistent?
5. Does the title slide set proper expectations?

Respond ONLY with JSON:
{
  "narrative_arc": "PASS|WARN|FAIL",
  "logical_progression": "PASS|WARN|FAIL",
  "transition_gaps": ["specific gaps"],
  "pacing_consistency": "PASS|WARN|FAIL",
  "title_slide_alignment": "PASS|WARN|FAIL",
  "suggested_restructuring": "description of changes"
}
```

**VLM QA integration**: Save the VLM output as `qa-report.json`. Feed failures back into the agent context for targeted slide regeneration. Use VLM for **semantic** checks only (balance, harmony, narrative) — never for quantitative measurements (that's what CSS inspection is for).

### 7. Generate quality report

After analysis, provide:
- Per-slide overflow warnings (❌)
- Per-slide underuse warnings (⚠)
- Content formatting violations (RULE-CF-01: em dash, RULE-CF-02: bullet spacing)
- Typography rule violations (RULE-TY-*)
- Layout rule violations (RULE-LY-*)  
- Color/contrast violations (RULE-CO-*)
- Density violations (RULE-DE-*)
- Failure mode matches (F1-F8)
- Visual variety check (icons on 50%+ slides, layout diversity)
- VLM semantic audit results
- Content density flags (too many bullets/words/long sentences)

### 8. Overflow detection explained

The `analyze_slides.py` script uses these thresholds:
- **Slide dimensions**: 960x540pt (Marp default 16:9)
- **Content area**: ~870pt after subtracting header/footer/padding
- **Overflow**: content bottom margin < 10pt → text will be cut
- **Underuse**: bottom margin > 60pt → text could be larger
- **Density warning**: >18 estimated rendered lines per slide
