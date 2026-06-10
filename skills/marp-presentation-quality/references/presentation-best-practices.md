# Presentation Best Practices

## Content Design

1. **One idea per slide** — Each slide should convey exactly one main concept. If a
   slide has two equally important ideas, split it.

2. **The 7x7 rule (relaxed)** — Max 7 bullet points per slide, max 7 words per
   bullet. For cargobeamer (20pt font), max 8-9 bullets is safe.

3. **Title as a headline** — The slide title should be a complete statement or
   question, not a label. Bad: "Results". Good: "Q1 Results Exceeded Targets by 23%".

4. **No paragraphs** — Use concise bullet points, not prose paragraphs. If you need
   paragraphs, use a blockquote or split across multiple slides.

5. **Contrast is king** — Text must have sufficient contrast against background.
   Never put light text on light backgrounds or dark text on dark backgrounds.

6. **Data before decoration** — Charts and tables should be readable first,
   beautiful second. Avoid 3D charts, excessive gradients, or decorative elements
   that obscure data.

## Mayer's 12 Multimedia Principles (Cognitive Load Theory)

Based on 200+ experiments — strongest evidence base for slide design:

| Principle | Rule | Slide Application |
|-----------|------|-------------------|
| **Coherence** | Omit extraneous words, pictures, sounds | Remove decorative clip art, non-essential text. Every element must serve the message. |
| **Signaling** | Highlight essential material | Use color contrast, bold, or position to emphasize key takeaways |
| **Redundancy** | Don't present identical info in multiple modalities | Text + supporting image is fine; avoid text that just restates the image |
| **Spatial Contiguity** | Place related text and graphics near each other | Captions beneath diagrams, labels adjacent to chart elements |
| **Segmenting** | Break complex content into learner-paced chunks | Max 5±2 items per slide. Use progressive disclosure across slides. |
| **Pre-training** | Introduce key concepts first | Title slide + outline with key terminology defined upfront |
| **Modality** | Spoken word > on-screen text for complex explanations | For agent-scripted decks, generate speaker notes that complement rather than duplicate on-slide text |

## Narrative Structure

### SCQA Framework (McKinsey/Pyramid Principle)

Best for executive/strategy decks:

- **Slide 1:** Situation — context we all agree on
- **Slide 2:** Complication — what changed / the problem
- **Slides 3-5:** Question + Answer — how we solve it
- **Slides 6+:** Supporting arguments in pyramidal structure

### Duarte's Sparkline

Create tension by contrasting "What is" (current state) with "What could be" (possible future).

### Storytelling Arc (Narrative-Heavy Decks)

| Arc Stage | Slide Mapping |
|-----------|---------------|
| Exposition | Context / background |
| Rising action | Challenge / problem details |
| Climax | Key insight / solution reveal |
| Falling action | Implementation details |
| Resolution | Outcome / next steps |

### Slide Count Heuristic

- 1 slide per ~2 minutes of talk time
- 15-minute talk = 7-8 slides
- 30-minute talk = 15-18 slides
- Plan to this constraint — don't arbitrarily decide slide count

## Slide Types

| Type | When to use | Key constraints |
|------|-------------|-----------------|
| Title slide | First slide only | Centered content, minimal text |
| Section/chapter | Transitions between major sections | Full-width headline, optionally with image |
| Content slide | Main body | 200-250 words max |
| Table slide | Comparing data | 4 columns max, 6-8 rows max |
| Cards slide | Grouping related items | 3-5 cards, 3-5 points each |
| Quote/blockquote | Emphasizing a statement | Short, impactful |
| Agenda | Overview/table of contents | 5-7 items + optional descriptions |

## Data Visualization Decision Framework

| Data Type | Best Visual | When to Avoid |
|-----------|-------------|---------------|
| Single key number | Callout stat (big number + context) | A chart would dilute the message |
| Comparison (2-5 items) | Horizontal bar chart | Pie chart (hard to compare areas) |
| Trend over time (<10 points) | Line chart | Bar chart (implies discrete categories) |
| Trend over time (>10 points) | Sparkline + callout value | Full-size area chart |
| Composition (parts of whole) | Waffle chart or stacked bar | Pie chart (unless 2-3 segments) |
| Distribution | Box plot or histogram | Donut chart |
| Relationship/Correlation | Scatter plot | 3D charts (distorts perception) |
| Hierarchy/Flow | Sankey diagram or tree map | Any 3D representation |
| Geospatial | Choropleth (simple) | 3D globe (high cognitive load) |
| Icon/data callouts | Icon + numeral (e.g., "2.3M users →") | Full table |

## Color Psychology & Emotional Impact

| Palette Style | Conveys | Best For |
|---------------|---------|----------|
| Dark backgrounds (Linear-style) | Technical sophistication | SaaS, AI, developer audiences |
| Light clean (Apple-style) | Accessibility, clarity, trust | Corporate, enterprise |
| Vibrant saturated (Stripe-style) | Energy, creativity, innovation | Startup, product launches |
| Warm muted (Anthropic-style) | Thoughtfulness, safety, depth | Editorial, policy, research |

## WCAG Color Rules

- All text-on-background: ≥4.5:1 (AA) for body, ≥3:1 (AA) for large text (≥18pt/24px bold or ≥24px regular)
- Non-text elements (charts, icons): ≥3:1 against adjacent colors
- Don't rely on color alone — pair with icons, patterns, or labels
- Avoid red-green pairs for data differentiation (deuteranopia/protanopia)
- Minimum readable size: 14px body (18px recommended)

## Visual Consistency

- Use exactly **one accent color** per slide (don't mix brand colors randomly)
- All images should have the same style (same border radius, same border color)
- Table headers should be consistently styled across all tables in a deck
- Scoped styles should only override what's necessary for ONE slide, not the whole deck

## Export Considerations

- For **PPTX**: Use `--image-scale 4` to get crisp images in output
- For **PDF**: No special flags needed; check for overflow before exporting
- For **compression**: Downscale PNGs in ppt/media/ to max 2560px width
- For **HTML intermediate**: Use Marp's HTML output if you need to inspect DOM for QA
