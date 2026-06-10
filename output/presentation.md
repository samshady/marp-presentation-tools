---
marp: true
theme: cargobeamer
paginate: true
footer: "Confidential and Proprietary"
---

<!-- _class: title -->

# Research Synthesis & Upgrade Plan
## AI-Driven Marp/Markdown Presentation Workflow

<style scoped>
section {
  background-image: url("icons/material-symbols_rocket-launch.svg"), url("https://raw.githubusercontent.com/samshady/marp-presentation-tools/main/Cargobeamer_Logo.png");
  background-repeat: no-repeat, no-repeat;
  background-position: calc(100% - 60px) 75%, 30px 30px;
  background-size: 120px auto, 150px auto;
}
</style>

---

<!-- _class: agenda -->

# Agenda

<table style="font-size:18pt">
<tr><th colspan="2">Today's Topics</th></tr>
<tr><td><b>1. Design Best Practices</b><br/>Mayer's principles, typography, layout</td><td><b>4. AI Tool Landscape</b><br/>6 tools surveyed, key gap found</td></tr>
<tr><td><b>2. Color, Accessibility & Data Viz</b><br/>WCAG, palettes, chart frameworks</td><td><b>5. Open-Source Pipelines</b><br/>sunbigfly, Akxan, DeepSlide</td></tr>
<tr><td><b>3. Narrative & Anti-Patterns</b><br/>SCQA, slide count, F1-F8</td><td><b>6. Vision QA & Upgrade Roadmap</b><br/>VLM contracts, 4-phase plan</td></tr>
</table>

---

# Design Best Practices

<div class="two-col">

<div class="main">

- **Cognitive Load Theory** - Mayer's 12 principles, validated across 200+ experiments
- **Coherence** - every element must serve the message, nothing extraneous
- **Signaling** - use contrast and bold for key takeaways, never font size alone
- **Segmenting** - max 5 +/- 2 items per slide, progressive disclosure
- **Pre-training** - define key terminology upfront in title and outline

</div>

<div class="side-icon">
  <img src="icons/material-symbols_lightbulb.svg" width="140" />
</div>

</div>

<style scoped>
.two-col { display: flex; gap: 30px; margin-top: 10px; }
.main { flex: 3; }
.side-icon { flex: 1; display: flex; align-items: center; justify-content: center; }
</style>

---

# Typography & Visual Hierarchy

<div class="two-col icon-left">

<div class="side-icon">
  <img src="icons/material-symbols_layers.svg" width="120" />
</div>

<div class="main">

- **7-level scale**: 48pt > 40pt > 28pt > 22pt > 18pt > 14pt > 12pt
- **Line height**: body 1.5x, headings 1.1x (unitless CSS)
- **Hard rules**: body >= 14px and <= 24px, max 3 font families
- **7 bento templates**: full-bleed, 2-col, 3-col, 4-card, 6-card, center

</div>

</div>

<style scoped>
.two-col { display: flex; gap: 30px; margin-top: 10px; }
.main { flex: 3; }
.side-icon { flex: 1; display: flex; align-items: center; justify-content: center; }
.icon-left .side-icon { order: -1; }
</style>

---

# Color, Accessibility & Data Viz

<div class="two-col">

<div class="main">

- **Palette structure**: Base > Surface > Primary > Accent > Text (3 levels)
- **WCAG AA**: 4.5:1 body, 3:1 large text - avoid red-green pairs
- **Max 5 colors per slide**, decorative gradients excluded
- **Best charts**: bar (comparison), line (trends), scatter (correlation)
- **Avoid**: pie charts over 3 segments, 3D charts, dense tables

</div>

<div class="side-icon">
  <img src="icons/material-symbols_palette.svg" width="130" />
</div>

</div>

<style scoped>
.two-col { display: flex; gap: 30px; margin-top: 10px; }
.main { flex: 3; }
.side-icon { flex: 1; display: flex; align-items: center; justify-content: center; }
</style>

---

# Narrative Structure & Failure Modes

<div class="two-col">

<div class="main">

- **SCQA**: Situation > Complication > Question > Answer (McKinsey)
- **Pacing**: 1 slide per 2 minutes, 15 min talk = 7-8 slides
- **F2 Overfill** - content overflow, reduce count
- **F6 Contrast failure** - below WCAG threshold
- **F8 Narrative disconnect** - no story arc, restructure with SCQA

</div>

<div class="side-icon">
  <img src="icons/material-symbols_route.svg" width="130" />
</div>

</div>

<style scoped>
.two-col { display: flex; gap: 30px; margin-top: 10px; }
.main { flex: 3; }
.side-icon { flex: 1; display: flex; align-items: center; justify-content: center; }
</style>

---

# AI Presentation Tool Landscape

<table>
<tr><th>Tool</th><th>Layout Engine</th><th>Quality Mechanism</th></tr>
<tr><td><b>Gamma.app</b></td><td>Template-constrained</td><td>Human review, no visual QA</td></tr>
<tr><td><b>Beautiful.ai</b></td><td>Constraint satisfaction</td><td>Template design rules only</td></tr>
<tr><td><b>Tome</b></td><td>Narrative-first</td><td>No pixel-level QA</td></tr>
<tr><td><b>Canva Magic</b></td><td>Score heuristics</td><td>Layout balance ranking</td></tr>
<tr><td><b>MS Copilot</b></td><td>Template-constrained</td><td>Template guardrails</td></tr>
<tr><td><b>Pitch</b></td><td>Design system</td><td>Human review only</td></tr>
</table>

><span style="color:#6EC8FF; font-weight:700">Key gap:</span> No major tool uses vision feedback to refine slide appearance

---

# Open-Source Agentic Pipelines

<div class="card-row">

<div class="card">
  <img src="icons/material-symbols_layers.svg" width="40" class="card-icon" />
  <h3>sunbigfly/ppt-agent-skills</h3>
  <p>Multi-agent state machine, 4 subagents, JSON contract architecture, Pillow pixel QA, stateless resume</p>
</div>

<div class="card">
  <img src="icons/material-symbols_build.svg" width="40" class="card-icon" />
  <h3>Akxan/ppt-agent-skill</h3>
  <p>26 production styles, 14 typography rules, 18 chart types (SVG), 8 failure modes with fix protocols</p>
</div>

<div class="card">
  <img src="icons/material-symbols_bar-chart.svg" width="40" class="card-icon" />
  <h3>DeepSlide (arXiv)</h3>
  <p>Time-budgeted planner, Markov style inheritance, dual-scoreboard evaluation (artifact + delivery)</p>
</div>

</div>

<style scoped>
section { display: block; }
.card-row { display: flex; gap: 16px; width: 100%; margin-top: 24px; }
.card {
  flex: 1 1 0; min-width: 0;
  background: #FAFAFB;
  border: 0.75px solid #6EC8FF;
  border-radius: 10px;
  padding: 20px;
}
.card h3 { font-size: 18pt; font-weight: 700; color: #00132B; margin: 10px 0 8px 0; }
.card p { font-size: 14pt; line-height: 1.5; margin: 0; color: #000; }
.card-icon { display: block; }
</style>

---

# Common Gaps & Best Format

<div class="callout">

<span class="big-number">VLM Gap</span>
<span class="callout-text">No open-source tool uses vision-language models for semantic slide QA. Analysis is purely pixel-statistical.</span>

</div>

<div class="callout-row">

<div class="mini-card">
  <span class="label">Best Format</span>
  HTML/CSS as primary target, convert to Marp markdown
</div>

<div class="mini-card">
  <span class="label">DeepSlide Innovation</span>
  Logical-chain planner with time budgets, style inheritance, dual-scoreboard evaluation
</div>

</div>

<style scoped>
section { display: block; }
.callout {
  text-align: center;
  margin: 24px 0 20px 0;
  padding: 24px;
  background: #FAFAFB;
  border: 1.5px solid #6EC8FF;
  border-radius: 12px;
}
.big-number {
  display: block;
  font-size: 36pt;
  font-weight: 700;
  color: #6EC8FF;
  line-height: 1.2;
  margin-bottom: 10px;
}
.callout-text {
  display: block;
  font-size: 17pt;
  line-height: 1.5;
  color: #000;
}
.callout-row {
  display: flex;
  gap: 14px;
  width: 100%;
}
.mini-card {
  flex: 1 1 0;
  background: #FAFAFB;
  border: 0.75px solid #B6E3FF;
  border-radius: 8px;
  padding: 14px;
  font-size: 14pt;
  line-height: 1.4;
}
.label {
  display: block;
  font-size: 11pt;
  font-weight: 700;
  color: #00132B;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 6px;
}
</style>

---

# Vision QA & Style Contracts

<div class="two-col">

<div class="main">

- **Stage A**: per-slide visual audit - balance, readability, color
- **Stage B**: deck-wide narrative audit - arc, progression, pacing
- Use VLM for **semantic** checks, CSS/DOM for **quantitative**
- **theme-contract.json**: full design system encoding per deck

</div>

<div class="side-icon">
  <img src="icons/material-symbols_check-circle.svg" width="130" />
</div>

</div>

<style scoped>
.two-col { display: flex; gap: 30px; margin-top: 10px; }
.main { flex: 3; }
.side-icon { flex: 1; display: flex; align-items: center; justify-content: center; }
</style>

---

# Upgrade Roadmap

<div class="roadmap">

<div class="phase p1">
<h3>Phase 1 - Foundation</h3>
<p>Style contract system, CSS/DOM inspection QA, density contract validator</p>
<span class="tag">Week 1</span>
</div>

<div class="phase p2">
<h3>Phase 2 - Pipeline</h3>
<p>5-stage pipeline shell, per-slide JSON contracts, stateless resume support</p>
<span class="tag">Week 2</span>
</div>

<div class="phase p3">
<h3>Phase 3 - Quality</h3>
<p>VLM QA pass with structured prompts, feedback loop, chart MCP tool</p>
<span class="tag">Week 3</span>
</div>

<div class="phase p4">
<h3>Phase 4 - Polish</h3>
<p>Icon search MCP tool, narrative arc planning, integration testing</p>
<span class="tag">Week 4</span>
</div>

</div>

<style scoped>
section { display: block; }
.roadmap { display: flex; gap: 14px; width: 100%; margin-top: 24px; }
.phase {
  flex: 1 1 0;
  background: #FAFAFB;
  border-radius: 10px;
  padding: 18px;
  overflow: hidden;
}
.phase h3 { font-size: 18pt; font-weight: 700; margin: 0 0 10px 0; }
.phase p { font-size: 13pt; margin: 0 0 10px 0; line-height: 1.5; }
.tag { font-size: 11pt; font-weight: 700; color: #666; text-transform: uppercase; letter-spacing: 0.05em; }
.p1 { border-top: 5px solid #6EC8FF; } .p1 h3 { color: #6EC8FF; }
.p2 { border-top: 5px solid #00132B; } .p2 h3 { color: #00132B; }
.p3 { border-top: 5px solid #B6E3FF; } .p3 h3 { color: #00132B; }
.p4 { border-top: 5px solid #6EC8FF; } .p4 h3 { color: #6EC8FF; }
</style>
