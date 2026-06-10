# Research Synthesis & Upgrade Plan: AI-Driven Marp/Markdown Presentation Workflow

---

## Domain 1 — Presentation Design Best Practices

### 1.1 Cognitive Load Theory (Mayer's 12 Multimedia Principles)

Mayer's principles, validated across 200+ experiments, provide the strongest evidence base for slide design decisions:

| Principle | Rule | Slide Application |
|-----------|------|-------------------|
| **Coherence** | Omit extraneous words, pictures, sounds | Remove decorative clip art, non-essential text. Every element must serve the message. |
| **Signaling** | Highlight essential material | Use color contrast, bold, or position to emphasize key takeaways; do not rely on font size alone. |
| **Redundancy** | Don't present identical info in multiple modalities simultaneously | Narration + identical on-screen text hurts learning. For slides (without narration), text + supporting image is fine. |
| **Spatial Contiguity** | Place related text and graphics near each other | Captions directly beneath diagrams, labels adjacent to chart elements. CSS `grid` or `flex` with logical source order. |
| **Temporal Contiguity** | Present narration and corresponding graphic simultaneously | In sequential reveals, animate content blocks not as a single fade-in but in logical step order. |
| **Segmenting** | Break complex content into learner-paced chunks | Max 5±2 items per slide. Use progressive disclosure across slides. |
| **Pre-training** | Introduce key concepts and vocabulary first | Title slide + outline slide with key terminology defined upfront. |
| **Modality** | Use spoken word rather than on-screen text for complex explanations | For agent-scripted decks, generate speaker notes that complement rather than duplicate on-slide text. |

**Key source**: Mayer, R. E. (2021). *Multimedia Learning* (3rd ed.). Cambridge University Press.

### 1.2 Typography Rules

**Font pairing strategy** (from industry analysis of Akxan/ppt-agent-skills + Apple HIG + Google Material):

- **Sans + Serif pair**: One display sans for headings (e.g., Inter, SF Pro, Geist), one serif for body or accent (e.g., Source Serif, NY, SangBleu). The Akxan skill uses a 3-level font stack with OpenType features enabled.
- **Hierarchy ladder**: 7 distinct levels recommended — Large Title → Title 1 → Title 2 → Headline → Body → Caption → Small. Each step ~2-4px apart, tracked to font size.
- **Line height**: Body text 1.4–1.6× font size; headings 1.1–1.3×. CSS `line-height` should be unitless.
- **Max line length**: 45–75 characters per line (the \"ideal measure\"). For slides at 16:9, this means 2–3 columns of body text max.
- **Tracking (letter-spacing)**: Dynamic — larger sizes need tighter tracking. Apple uses dynamic optical sizing. For slides: headlines 0–0.02em, body 0.01–0.03em, ALL CAPS 0.05–0.15em.
- **Minimum readable size**: 14px body text (18px recommended). WCAG AA contrast 4.5:1 for body, 3:1 for large text (≥18pt/24px bold or ≥24px regular).
- **Avoid**: Light font weights (< Regular / < 400) on slides projected in bright rooms; thin text disappears on projection.

### 1.3 Layout & Visual Hierarchy

**Grid systems**: The most successful agent-generated slide tools (Akxan, sunbigfly) use a **Bento Grid** approach — 7 distinct layout templates:

1. **Full-bleed (no grid)** — Hero/title slides, section dividers
2. **2-column symmetric** — Equal weight, compare-contrast
3. **2-column asymmetric (60:40 or 70:30)** — Content + supporting visual
4. **3-column** — Data dashboards, feature lists
5. **4-card bento (2×2)** — Quadrant layout for dense information
6. **6-card bento (3×2)** — Gallery, team, use cases
7. **Center-aligned single column** — Quotes, key numbers, CTAs

**Visual hierarchy rules**:
- **Z-pattern**: Top-left to bottom-right natural reading. Place key message in the primary optical area (top-left quadrant).
- **F-pattern**: For text-heavy slides, users scan the top line then vertical left edge. Use bolding/color on leading words.
- **Rule of thirds**: Place focal points at intersection of imaginary 3×3 grid.
- **Whitespace**: Minimum 10% of slide area should be empty. Aim for 30-40% on title slides, 15-25% on content slides.

### 1.4 Color Theory & Accessibility

**Palette structure** (from Akxan 26-style system analysis):
- Base (1 color) — slide background
- Surface (1-2 colors) — card/container backgrounds
- Primary (1-2 colors) — main brand color, used sparingly
- Accent (1-2 colors) — highlights, CTAs, data emphasis
- Text (3 colors) — high-contrast for body, medium for secondary, low-contrast for decorative

**WCAG rules to enforce**:
- All text-on-background pairs: ≥4.5:1 (AA) for body, ≥3:1 (AA) for large text
- Non-text elements (charts, icons): ≥3:1 against adjacent colors
- Don't rely on color alone to convey information — pair with icons, patterns, or labels
- Test with common CVD simulations (deuteranopia, protanopia): avoid red-green pairs for data differentiation

**Emotional impact**:
- Dark backgrounds (Linear-style): Convey technical sophistication, work well for SaaS/AI/developer audiences
- Light clean (Apple-style): Convey accessibility, clarity, corporate trust
- Vibrant saturated (Stripe-style): Convey energy, creativity, innovation
- Warm muted (Anthropic-style): Convey thoughtfulness, safety, editorial depth

### 1.5 Data Visualization on Slides

**Decision framework** (from Duarte DataStory + Tufte):

| Data Type | Best Visual | When to Avoid |
|-----------|-------------|---------------|
| Single key number | Callout stat (big number + context) | A chart would dilute the message |
| Comparison (2-5 items) | Horizontal bar chart | Pie chart (hard to compare areas) |
| Trend over time (<10 points) | Line chart | Bar chart (implies discrete categories) |
| Trend over time (>10 points) | Sparkline + callout value | Full-size area chart (too much ink) |
| Composition (parts of whole) | Waffle chart or stacked bar | Pie chart (unless 2-3 segments max) |
| Distribution | Box plot or histogram | Donut chart |
| Relationship/Correlation | Scatter plot | 3D charts (distorts perception) |
| Hierarchy/Flow | Sankey diagram or tree map | Any 3D representation |
| Geospatial | Choropleth (simple) | 3D globe (cognitive load too high) |
| Icon/data callouts | Icon + numeral (e.g., "2.3M users →") | Full table (too dense for slides) |

### 1.6 Narrative Structure

**Proven structures**:

1. **SCQA (Situation → Complication → Question → Answer)** — Barbara Minto's Pyramid Principle, formalized by McKinsey. Best for executive/strategy decks.
   - Slide 1: Situation (context we all agree on)
   - Slide 2: Complication (what changed / the problem)
   - Slides 3-5: Question and Answer (how we solve it)
   - Slides 6+: Supporting arguments in pyramidal structure

2. **Duarte's Sparkline**: What is → What could be. Create tension by contrasting the current state with the possible future.

3. **Storytelling arc** (for narrative-heavy decks): Exposition → Rising action → Climax → Falling action → Resolution. Maps to: Context → Challenge → Key insight → Implementation → Outcome.

**Slide count heuristic**: 1 slide per ~2 minutes of talk time. A 15-minute talk = 7-8 slides. A 30-minute talk = 15-18 slides. The agent should *plan to this constraint* not arbitrarily decide slide count.

### 1.7 Slide-Level Anti-Patterns (Failure Mode Catalog)

From Akxan/ppt-agent-skills `references/principles/failure-modes.md` (8 documented modes):

| ID | Failure Mode | Detection Method |
|----|-------------|-----------------|
| F1 | **Underfill** — Not enough content for the page density budget | CSS/computed: too few DOM elements, large empty areas detected by pixel analysis |
| F2 | **Overfill** — Content exceeds available space, overflow/cutoff | CSS overflow detection, pixel analysis at edges |
| F3 | **Decorative substitution** — Decorative elements replacing actual content cards | DOM audit: decoration count vs content card count |
| F4 | **Inconsistent spacing** — Different margins/padding on visually similar elements | CSS computed style comparison across cards |
| F5 | **Font size creep** — Body text too large or too small relative to hierarchy | CSS cascade audit against defined scale |
| F6 | **Contrast failure** — Text-to-background contrast below WCAG threshold | Color contrast computation from CSS variables |
| F7 | **Card misalignment** — Grid items not properly aligned to layout spec | Bounding box comparison from rendered layout |
| F8 | **Narrative disconnect** — Slides don't form a coherent story arc | Sequential content analysis via LLM |

---

## Domain 2 — AI-Powered Presentation Tools and Pipelines

### 2.1 Tool Architecture Survey

| Tool | Likely Pipeline | Layout Engine | Quality Mechanism |
|------|----------------|---------------|-------------------|
| **Gamma.app** | LLM (GPT-4/Claude) → Content chunking → Template matching → Rendering | Template-constrained, user can re-layout manually | Human-in-loop, no automated visual QA |
| **Beautiful.ai** | User input → Smart template selection → Rule-based layout engine | Constraint satisfaction solver (CSS grid-like), no visual QA feedback loop | Design rules enforced at template level; no post-hoc vision check |
| **Tome** | LLM generates narrative structure → Per-slide content blocks → Media search → Rendering | Narrative-first: each block type has preferred layouts. Multi-page sequential planning. | No pixel-level QA; relies on prompt quality. |
| **Canva Magic Design** | Input (topic/docs) → Content extraction → Template matching → Design generation | Template + brand kit constrained. Uses design score heuristic for layout ranking. | Design scoring based on layout heuristics (balance, alignment, whitespace). |
| **Microsoft Copilot in PPT** | GPT-4 → Brand template matching → Corporate asset insertion → Slide generation | Organization template constrained. Outputs to PPTX format. | No visual QA; relies on template guardrails. |
| **Pitch** | Prompt → Content → Layout matching | Design system constrained (consistent fonts, colors, spacing) | Human review only. |

**Key finding**: *No major tool uses a vision model in a feedback loop to refine slide appearance.* All rely on:
1. Prompt engineering for initial quality
2. Template/design system constraints to prevent bad output
3. Human editing for final polish

This is the **highest-leverage gap** a code-first agentic workflow can fill.

### 2.2 How These Tools Handle Core Problems

**Layout selection**:
- **Template-based** (Gamma, Canva, Pitch): Content type → template lookup → fill → render. Most reliable, least flexible.
- **Constraint-based** (Beautiful.ai): Element placement with hard constraints (non-overlap, margin minimums, aspect ratio preservation). More flexible but can produce generic results.
- **Heuristic-scored** (Canva): Generate N layouts, score by balance/alignment/whitespace, pick best.

**Content chunking**: All tools use LLM-based extraction from source documents. Key failure mode: **over-chunking** (too many slides with one sentence each) or **under-chunking** (one dense slide with 15 bullet points).

**Icon/Image selection**: Most use vector icon sets (Noun Project, Font Awesome-style) + stock photography APIs. **None do custom icon generation well.** The user's existing icon-finding skill is already competitive.

**Slide count decision**: Ad-hoc. Most tools generate as many slides as the LLM decides, with no time-budget constraint. DeepSlide (arXiv:2605.15202) is the only research system that explicitly plans to a time budget.

### 2.3 Common Limitations of Current AI Presentation Tools

1. **Visual inconsistency across slides**: Each slide generated independently; no global style memory beyond theme application.
2. **Poor handling of dense data**: Tables, complex relationships, interconnected concepts.
3. **Generic output**: Templates look recognizably templated; no tool produces truly bespoke layouts.
4. **No narrative arc awareness**: Most tools generate content per slide, not a story across slides.
5. **Zero automated QA**: No tool feeds screenshots back into a vision model for refinement.

---

## Domain 3 — Code-First Presentation Generation with AI Agents

### 3.1 Open-Source Agentic Pipelines

**Three major open-source implementations discovered:**

#### A. sunbigfly/ppt-agent-skills (781★ GitHub Stars)
- **Architecture**: Multi-agent state machine with 4 isolated subagents (Research → Outline → Style → Planning)
- **Key innovations**:
  - Subagent isolation: Each agent runs independently with `SUBAGENT_MODEL` parameter. Context never crosses agent boundaries.
  - JSON contract-driven architecture: Each page generates a validated `planning.json` before any HTML is rendered. The `planning_validator.py` ensures contracts are met.
  - Density contracts: Per-page budgets for cards, charts, decorations, and font sizes. Enforced by `contract_validator.py`.
  - Visual QA via `visual_qa.py`: Pillow-based pixel analysis checking dimensions, blank ratio, overflow, contrast zones, and planning coverage.
  - Stateless resume: No progress files. Resume by scanning disk for existing artifacts.
  - Dual PPTX export: PNG raster stream (100% visual fidelity) + SVG vector stream (editable shapes).
- **What's missing**: No VLM-based QA. The visual_qa.py is purely pixel-statistical, not semantic.

#### B. Akxan/ppt-agent-skill (77★ GitHub Stars)
- **Architecture**: Claude Code Skill with 6-step pipeline (Requirements → Research → Outline → Planning → Design → Post-processing)
- **Key innovations**:
  - 26 production-quality styles benchmarked against real brands (Linear, Anthropic, Stripe, Apple, NYT)
  - Typography rule system: 14 ironclad rules for spacing, tracking, font stack
  - Failure mode catalog: 8 failure modes with ordered fix protocol
  - Bento Grid system: 7 layout templates derived from real-world design analysis
  - 18 chart types at 3 difficulty levels, all pure HTML/CSS/SVG (no JS runtime)
  - HTML → SVG → PPTX pipeline via Puppeteer and python-pptx
- **What's missing**: No multi-agent orchestration, no visual QA feedback loop. Relies entirely on the LLM's generation quality.

#### C. DeepSlide — arXiv:2605.15202
- **Architecture**: Human-in-the-loop multi-agent system with 4 components:
  1. Controllable logical-chain planner with per-node time budgets
  2. Lightweight content-tree retriever for grounding
  3. Markov-style sequential rendering with style inheritance (each slide inherits from previous)
  4. Sandboxed execution with minimal repair for renderability
- **Key innovation**: Dual-scoreboard benchmark separating static artifact quality from dynamic delivery excellence. Narrative flow and pacing precision metrics.
- **Finding**: DeepSlide "matches strong baselines on artifact quality while consistently achieving larger gains on delivery metrics."

### 3.2 Code-Based Presentation Formats

| Format | Best For | Agent Suitability | Limitations |
|--------|----------|-------------------|-------------|
| **Marp/Markdown** | Quick slides, developer audiences, version control | ★★★★★ Simplest for LLMs to generate | Limited layout control compared to HTML |
| **HTML/CSS (reveal.js/Marp HTML slide)** | Full design control, custom layouts | ★★★★★ Agents excel at this | Longer generation time, needs browser rendering |
| **Slidev** | Developer presentations, code highlighting | ★★★★ Good but more complex syntax | Niche audience |
| **LaTeX Beamer** | Academic/research presentations | ★★★ LLMs struggle with precise LaTeX | Steep learning curve, fragile |
| **PPTX via python-pptx** | Corporate compatibility, editable output | ★★★★ Good for output, hard for design | Limited design fidelity |
| **SVG (direct)** | Vector graphics, charts, diagrams | ★★★ LLMs can generate simple SVGs | Complex layouts are hard |

**Recommendation**: Use HTML/CSS as the primary generation target (full design freedom), then convert to Marp Markdown for the deliverable. If PPTX is needed, route through the HTML→SVG→PPTX pipeline demonstrated by both open-source projects.

### 3.3 Vision Models for Quality Checking

**Current state**: Both major open-source projects use **pixel-statistical analysis** (PIL/Pillow) rather than VLM-based semantic analysis.

**How vision-capable models "see" slides**:
- **Direct image processing** (GPT-4V, Claude 3.5/4 Vision, Gemini Pro Vision): The model receives the rendered PNG as an image. It can comment on layout, spacing, color, and content — but with limitations:
  - Resolution-dependent: Models typically downsample to 512×512 or 768×768 tokens. Fine text may be illegible in the image.
  - No DOM access: The model can't inspect CSS properties or computed styles.
  - Qualitative, not quantitative: Good for "this looks cluttered" but bad for "this margin is 12px when it should be 24px."

**Practical implications**:
- Use VLM for **semantic** checks: narrative flow, content relevance, visual appeal, emotional tone
- Use CSS/DOM inspection for **quantitative** checks: margins, font sizes, contrast ratios, alignment
- The current workflow already has the right split (CSS inspection + vision screenshot check). The gap is in **how structured the feedback loop is** and **which specific rules are checked.**

### 3.4 Known Prompt Templates and Agent Skills

**Specific skills and templates discovered:**

1. **Akxan `SKILL.md`**: A complete Claude Code Skill (available on GitHub) with 6-step pipeline, 26 styles, 18 charts, 7 layouts. The `SKILL.md` file itself is the prompt template.

2. **sunbigfly `SKILL.md`**: Another complete skill with multi-agent architecture, visual_qa.py integration, planning validators, and contract enforcement.

3. **`references/prompts.md` (Akxan)**: 5 prompt templates for research, outline, planning, design, and speaker notes. Bilingual (Chinese/English).

4. **Presentation Agent skill (sacredvoid/presentation-chef)**: Generates Apple Keynote-style HTML presentations with cinematic animations, zero dependencies. Single self-contained HTML file.

5. **`nugrahalabib/AgentBuff-Presentation-Skills`**: Agent-agnostic skill usable by Claude Code, Codex, Hermes, etc. Exports to HTML, PDF, PNG, or PPTX.

### 3.5 Current Capability Ceiling

**Where quality breaks down and why:**

1. **Multi-slide visual consistency** — LLMs generate each slide independently. Despite system prompts asking for consistency, CSS variable reuse is inconsistent across slides. → *Fix: Enforce a single `style.json` contract across all slides.*

2. **Overflow and content crowding** — LLMs don't compute available space. They produce content that exceeds a 16:9 frame. → *Fix: Pre-compute and inject available height as a constraint.*

3. **Inconsistent spacing systems** — LLMs can declare a spacing system but don't consistently apply it. → *Fix: CSS custom properties with a preset scale, enforced by a linter.*

4. **Narrative coherence** — Individual slides look good, but the deck lacks a narrative arc. → *Fix: Pre-plan the entire deck structure (like DeepSlide's logical-chain planner) before generating individual slides.*

5. **Chart/data accuracy** — LLMs hallucinate numbers and data. → *Fix: Ground all data in provided source documents. The agent must cite which row/paragraph each number came from.*

---

## Synthesis — Concrete Upgrade Plan

### Improvement 1: Replace Ad-Hoc Generation with a Structured Multi-Agent Pipeline (Highest Leverage)

**What to build**: A 5-stage state-machine pipeline modeled on the best of sunbigfly and Akxan's approaches.

```
Stage 0: Interview/Requirements — Ask 5-7 structured questions (audience, context, tone, 
  duration, data sources, brand constraints, output format)
Stage 1: Planning — Generate full deck structure with time-budgeted narrative arc 
  (using DeepSlide's logical-chain planner approach)
Stage 2: Style Selection — Pick theme + bento grid layouts per slide based on content type
Stage 3: Per-Slide Generation — Generate each slide's HTML independently, grounded in 
  the planning contract from Stage 1
Stage 4: Quality Assurance — CSS/DOM inspection + pixel analysis + VLM review → 
  feedback loop back to Stage 3 for repair
```

**Key implementation details**:
- Use **JSON contract files** between stages (like sunbigfly's `planning.json`). Each stage reads the contract from the previous stage and enriches it.
- Subagent isolation: Use different Kilocode agent calls per stage, with explicit `SUBAGENT_MODEL` configuration.
- Stateless resume: Each stage writes artifacts to disk. Interruption recovers by scanning for existing files.

**Effort**: Moderate (2-3 days to implement the pipeline shell). Integrate with existing Marp output format.

### Improvement 2: Encode Design Rules into the CSS/DOM Inspection Layer (Highest ROI)

**What to build**: Extend the existing CSS/DOM inspection pipeline with specific, quantitative rules.

**Rules to add** (organized by priority):

```
// TYPOGRAPHY
- RULE-TY-01: Body text must be ≥14px and ≤24px
- RULE-TY-02: Heading-to-body contrast ratio must be ≥2:1 (size) or weight difference ≥200
- RULE-TY-03: Max 3 font families per deck (violation = WARN)
- RULE-TY-04: Line height must be 1.4–1.6× for body, 1.1–1.3× for headings
- RULE-TY-05: No text under 10px anywhere on slide (FAIL)
- RULE-TY-06: Max line length ≤75ch for multi-line body text

// LAYOUT
- RULE-LY-01: All slides must be 16:9 ratio (1280×720 minimum resolution)
- RULE-LY-02: Left/right margins ≥40px on content slides
- RULE-LY-03: Top/bottom margins ≥30px on content slides
- RULE-LY-04: Card/container border-radius must be consistent (±2px within same deck)
- RULE-LY-05: No elements overflowing slide bounds (FAIL)
- RULE-LY-06: Whitespace must occupy ≥10% of slide area
- RULE-LY-07: Max 5±2 content items per slide (FAIL if >9)

// COLOR & CONTRAST
- RULE-CO-01: All text-background pairs must pass WCAG AA (4.5:1 body, 3:1 large text)
- RULE-CO-02: No red-green pairs for data differentiation (protanopia/deuteranopia check)
- RULE-CO-03: Color palette must have ≤5 distinct colors per slide (decorative gradients excluded)

// DENSITY
- RULE-DE-01: Per-page card budget enforced (via density_contract.json)
- RULE-DE-02: Per-page chart budget enforced (max 1-2 complex charts per slide)
- RULE-DE-03: Decoration elements ≤ 20% of total DOM nodes on the page
```

**Implementation approach**: Write a Node.js script using `puppeteer` or `jsdom` that:
1. Renders each Marp slide in a headless browser
2. Queries `window.getComputedStyle()` for each relevant element
3. Checks against the rule set
4. Outputs a structured JSON report with PASS/WARN/FAIL per rule
5. Feeds failures back to the agent as specific repair instructions

**This is the single highest-leverage improvement.** It converts vague feedback ("this slide looks off") into specific, actionable commands ("RULE-LY-02 FAIL: left margin is 24px, must be ≥40px").

### Improvement 3: Build a Structured Vision-Language Model QA Pass

**What to build**: A two-stage VLM evaluation of rendered slides, structured with a specific prompt framework.

**Stage A — Per-Slide Visual Audit** (after rendering):

```
You are evaluating a presentation slide screenshot. Assess the following dimensions, 
responding ONLY with a JSON object:

{
  "visual_balance": "good|cluttered_left|cluttered_right|top_heavy|bottom_heavy",
  "text_readability": "good|too_small|too_dense|low_contrast",
  "color_harmony": "good|mismatched|too_many_colors|muddy",
  "whitespace_usage": "good|cramped|wasteful",
  "data_visualization_clarity": "good|confusing|overstyled|unnecessary",
  "content_density": "underfilled|appropriate|overfilled",
  "specific_issues": ["list of 1-3 specific, actionable issues"],
  "repair_priority": "none|low|medium|high"
}
```

**Stage B — Deck-Wide Narrative Audit** (after all slides):

```
You are evaluating a full slide deck for narrative coherence and flow. 
Review all slides in sequence and assess:

1. Does the deck have a clear narrative arc (beginning, middle, end)?
2. Is there a logical progression of ideas?
3. Are there any transition gaps (jumps between unrelated concepts)?
4. Is the pacing consistent (not 3 dense slides followed by 1 trivial slide)?
5. Does the title slide set proper expectations for the content?

Provide a JSON response with PASS/WARN/FAIL per dimension and a suggested 
slide reordering or restructuring if needed.
```

**Key design decisions**:
- Keep the VLM prompt **structured** (JSON out). This makes automated parsing and feedback loop integration trivial.
- **Never ask the VLM to measure.** VLMs are bad at "is this margin 24px?" — that's what the CSS inspector is for.
- Use VLM for **semantic** checks only: visual balance, color harmony, narrative flow.
- The VLM output feeds back into the agent's context as a `qa-report.json`, which the agent reads before deciding whether to regenerate a slide.

**Tool choice**: Claude 3.5 Sonnet/Claude 4 or GPT-4o for the VLM pass. Both handle structured output reliably. The feedback delay is ~2-5 seconds per slide — acceptable for a batch pass.

### Improvement 4: Add a Style Contract System with Brand/Theme Constraints

**What to build**: A `theme-contract.json` file that formally encodes the visual design system for each deck. The theme contract is generated once per deck and injected into every agent stage.

```json
{
  "theme_name": "corporate-dark",
  "slide_size": {"width": 1280, "height": 720, "ratio": "16:9"},
  "typography": {
    "families": ["Inter", "SF Pro Text", "system-ui"],
    "scale": [
      {"name": "display", "size": 48, "weight": 700, "line_height": 1.1},
      {"name": "heading_1", "size": 36, "weight": 600, "line_height": 1.15},
      {"name": "heading_2", "size": 28, "weight": 600, "line_height": 1.2},
      {"name": "heading_3", "size": 22, "weight": 500, "line_height": 1.3},
      {"name": "body", "size": 18, "weight": 400, "line_height": 1.5},
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
    "background": "#0D1117",
    "surface": "#161B22",
    "surface_elevated": "#21262D",
    "primary": "#58A6FF",
    "accent": "#3FB950",
    "text_primary": "#F0F6FC",
    "text_secondary": "#8B949E",
    "text_decorative": "#484F58"
  },
  "layouts": {
    "available": ["2-col", "3-col", "bento-4", "bento-6", "hero", "center-single"],
    "card_radius": 8,
    "card_shadow": "0 2px 8px rgba(0,0,0,0.3)"
  },
  "decoration_budget": "medium",
  "chart_palette": ["#58A6FF", "#3FB950", "#D29922", "#F85149", "#BC8CFF", "#FF7B72"]
}
```

**How it works**:
1. Agent generates `theme-contract.json` from user's chosen theme or from analyzing existing Marp theme CSS
2. Contract is injected into every `generate-slide` prompt and every QA pass
3. QA scripts check actual CSS properties against contract values
4. If contract values are violated, the slide is flagged for regeneration

**Fit with existing workflow**: The user already has custom Marp themes. The contract system formalizes what those themes encode, making them machine-checkable.

### Improvement 5: Build an Icon & Data Visualization MCP Tool

**What to build**: Two MCP tools that the agent can call during slide generation:

**Tool A — `search-icon`**:
- Parameters: query (string), style (outline|filled|duotone), count (1-5)
- Returns: SVG icon code + attribution
- Sources: Feather Icons, Lucide, Phosphor Icons (all MIT/open-source), plus the user's existing icon API skill
- Key: Return raw SVG, not PNG. SVGs can be styled with the deck's CSS variables.

**Tool B — `generate-chart`**:
- Parameters: chart_type (bar|line|pie|radar|heatmap|sankey|treemap), data (JSON array), dimensions (w, h), style_theme (CSS variable mapping)
- Returns: Self-contained SVG chart code rendered with the deck's color palette
- Implementation: Pure SVG generation (no JS). Use `<svg>` elements with CSS variable references like `stroke="var(--color-primary)"`.
- Libraries to study: Akxan's chart library (18 types in pure HTML/CSS/SVG), Observable Plot (if JS runtime allowed)

**Why this matters**: Current agent-generated charts are unreliable. A dedicated chart tool guarantees data accuracy, consistent styling, and accessibility compliance.

### Implementation Roadmap

**Phase 1 (Week 1) — Foundation**:
1. Implement the style contract system (generate `theme-contract.json` from existing Marp themes)
2. Build the CSS/DOM inspection QA script with the rule set from Improvement 2
3. Add the density contract validator (port from sunbigfly's `contract_validator.py`)

**Phase 2 (Week 2) — Pipeline**:
1. Build the 5-stage pipeline shell (Interview → Plan → Style → Generate → QA)
2. Implement per-slide JSON contract generation (port from sunbigfly's `planning_validator.py`)
3. Add stateless resume support

**Phase 3 (Week 3) — Quality**:
1. Implement VLM QA pass with structured JSON prompts (Improvement 3)
2. Build the feedback loop: VLM output → agent repair context → slide regeneration
3. Implement the chart generation MCP tool

**Phase 4 (Week 4) — Polish**:
1. Implement the icon search MCP tool
2. Add narrative arc planning (port DeepSlide's logical-chain planner concept)
3. Integration test with real content: article → polished deck

### Repositories and Resources to Study

| Repository | Why Study It | Key Files to Read |
|------------|-------------|-------------------|
| [sunbigfly/ppt-agent-skills](https://github.com/sunbigfly/ppt-agent-skills) | Best multi-agent architecture, visual QA pipeline, contract validation | `SKILL.md`, `scripts/visual_qa.py`, `scripts/planning_validator.py`, `scripts/contract_validator.py` |
| [Akxan/ppt-agent-skill](https://github.com/Akxan/ppt-agent-skill) | Best style system, typography rules, chart library, failure mode catalog | `SKILL.md`, `references/typography.md`, `references/principles/failure-modes.md`, `references/styles/*.md`, `references/charts/*.md` |
| [DeepSlide (arXiv:2605.15202)](https://arxiv.org/abs/2605.15202) | Narrative planning with time budgets, dual-scoreboard evaluation | Full paper (the architecture section) |
| [sacredvoid/presentation-chef](https://github.com/sacredvoid/presentation-chef) | Single-file HTML presentation generation, cinematic approaches | Main skill file |
| [nugrahalabib/AgentBuff-Presentation-Skills](https://github.com/nugrahalabib/AgentBuff-Presentation-Skills) | Agent-agnostic presentation skill framework | Skill definition files |
| [AISSA (arXiv:2605.04729)](https://arxiv.org/abs/2605.04729) | LLM-based slide analysis for rubric-based feedback | Paper methodology section |

### Reference Books and Sources

1. **Mayer, R. E.** (2021). *Multimedia Learning* (3rd ed.). Cambridge University Press.
2. **Reynolds, G.** (2011). *Presentation Zen: Simple Ideas on Presentation Design and Delivery* (2nd ed.). New Riders.
3. **Duarte, N.** (2008). *slide:ology: The Art and Science of Creating Great Presentations*. O'Reilly.
4. **Duarte, N.** (2010). *Resonate: Present Visual Stories that Transform Audiences*. Wiley.
5. **Tufte, E.** (2001). *The Visual Display of Quantitative Information* (2nd ed.). Graphics Press.
6. **Minto, B.** (2021). *The Pyramid Principle: Logic in Writing and Thinking* (3rd ed.). Pearson.
7. **WCAG 2.1**: Understanding SC 1.4.3 Contrast (Minimum). W3C.
8. **Apple Human Interface Guidelines**: Typography section.
9. **Google Material Design 3**: Type scale and color system documentation.
