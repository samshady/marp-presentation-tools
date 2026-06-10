---
name: marp-presentation-pipeline
description: |
  Orchestrate a structured multi-agent pipeline for end-to-end Marp presentation
  creation. Runs 5 stages (Interview → Plan → Style → Generate → QA) with JSON
  contract passing between stages, subagent isolation, and stateless resume.
  Produces a polished, QA-validated Marp markdown presentation ready for PDF/PPTX
  export. This skill should be used when the user wants a polished, QA-validated
  presentation created from scratch using a structured multi-stage workflow.
---

# marp-presentation-pipeline

## Project root

All paths reference `$MARAP_ROOT` which points to the repo:
```bash
export MARP_ROOT=~/Development/marp-presentation-tools
```

## Stages

The pipeline runs as 5 independent stages. Each stage produces artifacts on disk.
If the pipeline is interrupted, resuming reuses existing artifacts.

```
Stage 0: Interview     → output/requirements.json
Stage 1: Plan          → output/plan.json
Stage 2: Style         → output/theme-contract.json
Stage 3: Generate      → output/presentation.md
Stage 4: QA            → output/qa-report.json
```

## References

- `skills/marp-presentation-creator/SKILL.md` — Per-slide generation, icons, scoped styles
- `skills/marp-presentation-designer/SKILL.md` — Theme contract generation, layout selection
- `skills/marp-presentation-quality/SKILL.md` — CSS/DOM rules, VLM audit, failure modes

## Workflow

When asked to create a full presentation using the pipeline:

### Stage 0 — Interview (Requirements Gathering)

Ask the user these structured questions. Write answers to `output/requirements.json`:

```json
{
  "audience": "executives|technical|academic|general",
  "context": "what is this presentation about?",
  "tone": "formal|conversational|persuasive|informative",
  "duration_minutes": 15,
  "data_sources": ["paths or descriptions of source documents"],
  "brand": "cargobeamer|unihalle|custom",
  "output_format": "pdf|pptx|both",
  "key_message": "one-sentence takeaway"
}
```

If user provides minimal input, use defaults:
- audience: "general"
- tone: "informative"
- duration: 15 minutes
- brand: detect from context (cargobeamer or unihalle)
- output: pdf

### Stage 1 — Plan (Narrative Structure & Slide Planning)

Read `output/requirements.json`. Generate a full deck plan to `output/plan.json`:

```json
{
  "title": "Deck Title",
  "duration_minutes": 15,
  "target_slide_count": 8,
  "narrative_structure": "SCQA|storytelling|informative",
  "slides": [
    {
      "id": 1,
      "type": "title",
      "heading": "Deck Title",
      "content": "Subtitle, author, date",
      "layout": "full-bleed",
      "time_budget_minutes": 1.5,
      "narrative_role": "situation|hook"
    },
    {
      "id": 2,
      "type": "agenda",
      "heading": "Agenda",
      "items": ["Introduction", "Problem", "Solution", "Evidence", "Next Steps"],
      "layout": "2-col-symmetric",
      "time_budget_minutes": 1
    }
  ]
}
```

**Slide count heuristic**: `target_slide_count = max(3, round(duration_minutes / 2))`.
**Narrative structure**: Use SCQA for business/executive, storytelling arc for narrative, informative for academic.

### Stage 2 — Style (Design Contract Generation)

Read `output/plan.json`. Generate a `theme-contract.json` following the marp-presentation-designer skill.

Output to `output/theme-contract.json`. This encodes the full design system (typography, spacing, colors, layouts, chart palette) that every slide will reference.

### Stage 3 — Generate (Per-Slide Generation)

Read `output/plan.json` and `output/theme-contract.json`. Generate each slide as Marp markdown following the marp-presentation-creator skill:

1. Write the YAML frontmatter (theme, paginate, footer)
2. For each slide in plan.json:
   - Apply the assigned bento grid layout via scoped `<style>`
   - **CRITICAL for card layouts**: set `section { display: block; }` and use a `<div class="card-row">` wrapper with flexbox (never set `section { display: flex; }` directly)
   - Use the theme-contract typography scale for all font sizes
   - Use theme-contract colors for all brand elements
   - Follow content limits from slide-rules.md (40-60 words per slide, 5-6 bullets max)
   - Add `<!-- _class: title -->` for the first slide
   - Never use em dashes or en dashes in content text
   - Vary layout types across slides (mix: flat lists, tables, flex cards, icon + list)
   - Keep bullets short - under 10 words each, scannable phrases not full sentences
3. **Source and add decorative icons (MANDATORY)**: For decks with 6+ slides, add background-image icons on at least 50% of content slides. Save icons to `./icons/` relative to the output markdown file:
   ```bash
   mkdir -p icons
   # Search for relevant icons per slide topic
   python3 $MARAP_ROOT/tools/icons/find-icon.py search "lightbulb" --source iconify --limit 3
   python3 $MARAP_ROOT/tools/icons/find-icon.py fetch material-symbols:lightbulb --source iconify -o icons
   # Color all icons with the PRIMARY/ACCENT brand color (e.g. #6EC8FF for cargobeamer)
   # Use the light accent color, NOT the dark text color - icons need to pop on white bg
   sed -i 's/currentColor/#6EC8FF/g' icons/*.svg
   # Use $(pwd) to make absolute paths for Marp
   sed -i 's|src="icons/|src="'$(pwd)'/icons/|g' output/presentation.md
   sed -i 's|url("icons/|url("'$(pwd)'/icons/|g' output/presentation.md
   # Vary icon placement across slides - use inline img tags for 2-col layouts,
   # background-image for decoration, small icons inside cards
   ```
4. Output to `output/presentation.md`

### Stage 4 — Quality Assurance

Run Stage 4 after Stage 3 completes. Two passes:

**Pass A — Quantitative (CSS/DOM Inspection)**:
```bash
# Run pixel analysis
python3 $MARAP_ROOT/tools/presentation-quality/analyze_slides.py output/presentation.md --json > output/qa-report.json
```

Check all hard rules from marp-presentation-quality:
- RULE-TY-01 through TY-07 (typography)
- RULE-LY-01 through LY-07 (layout)
- RULE-CO-01 through CO-03 (color/contrast)
- RULE-DE-01 through DE-03 (density)
- Cross-reference failures against the F1-F8 failure mode catalog

**Pass B — Semantic (VLM Audit)**:
Use a vision-capable model on rendered slide screenshots (from the analyze_slides.py pipeline) with the structured VLM prompts from the quality skill.

**Fix loop**: For any QA failures, regenerate the affected slides in Stage 3 and re-run Stage 4. Loop up to 3 iterations maximum.

**Cleanup**: After the final iteration passes QA, clean up temporary artifacts (but keep the output):
```bash
rm -f icons/*.svg
rmdir icons 2>/dev/null; true
```

### Output

On success:
- `output/presentation.md` — Final Marp markdown
- `output/qa-report.json` — Quality report (all rules PASS)
- `output/plan.json` — Deck plan
- `output/theme-contract.json` — Design contract
- `output/requirements.json` — Original requirements

Then render to PDF/PPTX using the CLI commands from the creator skill.

### Stateless Resume

Each stage checks if its output file already exists before running. To re-run a specific stage, delete its output file and re-invoke the pipeline.

| Stage | Output File | Delete to re-run |
|-------|-------------|------------------|
| 0 | `output/requirements.json` | `rm output/requirements.json` |
| 1 | `output/plan.json` | `rm output/plan.json` |
| 2 | `output/theme-contract.json` | `rm output/theme-contract.json` |
| 3 | `output/presentation.md` | `rm output/presentation.md` |
| 4 | `output/qa-report.json` | `rm output/qa-report.json` |
