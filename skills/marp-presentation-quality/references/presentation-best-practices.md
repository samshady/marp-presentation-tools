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

## Slide Types

| Type | When to use | Key constraints |
|---|---|---|
| Title slide | First slide only | Centered content, minimal text |
| Section/chapter | Transitions between major sections | Full-width headline, optionally with image |
| Content slide | Main body | 200-250 words max |
| Table slide | Comparing data | 4 columns max, 6-8 rows max |
| Cards slide | Grouping related items | 3-5 cards, 3-5 points each |
| Quote/blockquote | Emphasizing a statement | Short, impactful |
| Agenda | Overview/table of contents | 5-7 items + optional descriptions |

## Visual Consistency

- Use exactly **one accent color** per slide (don't mix brand colors randomly)
- All images should have the same style (same border radius, same border color)
- Table headers should be consistently styled across all tables in a deck
- Scoped styles should only override what's necessary for ONE slide, not the whole deck

## Export Considerations

- For **PPTX**: Use `--image-scale 4` to get crisp images in the output
- For **PDF**: No special flags needed; check for overflow before exporting
- For **compression**: Downscale PNGs in ppt/media/ to max 2560px width
