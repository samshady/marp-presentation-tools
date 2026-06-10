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
  background-image: url("/home/sam/Development/marp-presentation-tools/icons/material-symbols_rocket-launch.svg"), url("https://raw.githubusercontent.com/samshady/marp-presentation-tools/main/Cargobeamer_Logo.png");
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

<div class="principle-grid">

<div class="principle-card">
  <span class="principle-icon">🧠</span>
  <h3>Cognitive Load</h3>
  <p>Mayer's 12 principles, 200+ experiments</p>
</div>

<div class="principle-card">
  <span class="principle-icon">✂️</span>
  <h3>Coherence</h3>
  <p>Omit extraneous elements</p>
</div>

<div class="principle-card">
  <span class="principle-icon">🔦</span>
  <h3>Signaling</h3>
  <p>Contrast and bold for key takeaways</p>
</div>

<div class="principle-card">
  <span class="principle-icon">🧩</span>
  <h3>Segmenting</h3>
  <p>Max 5+/-2 items per slide</p>
</div>

<div class="principle-card">
  <span class="principle-icon">📖</span>
  <h3>Pre-training</h3>
  <p>Define key terms upfront</p>
</div>

<div class="principle-card">
  <span class="principle-icon">🎯</span>
  <h3>Key Insight</h3>
  <p>Bento Grid templates produce best results</p>
</div>

</div>

<style scoped>
section { display: block; }
.principle-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 14px;
  margin-top: 16px;
}
.principle-card {
  background: #FAFAFB;
  border: 0.75px solid #6EC8FF;
  border-radius: 10px;
  padding: 16px;
  text-align: center;
}
.principle-icon {
  font-size: 32pt;
  display: block;
  margin-bottom: 6px;
}
.principle-card h3 {
  font-size: 16pt;
  font-weight: 700;
  color: #00132B;
  margin: 0 0 4px 0;
}
.principle-card p {
  font-size: 12pt;
  line-height: 1.4;
  margin: 0;
  color: #000;
}
</style>

---

# Typography & Visual Hierarchy

<div class="two-col icon-left">

<div class="side-icon">
  <img src="/home/sam/Development/marp-presentation-tools/icons/material-symbols_layers.svg" width="120" />
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

<div class="data-row">

<div class="data-card">
  <span class="stat">4.5:1</span>
  <span class="stat-label">WCAG AA body contrast</span>
</div>

<div class="data-card">
  <span class="stat">3:1</span>
  <span class="stat-label">Large text minimum</span>
</div>

<div class="data-card">
  <span class="stat">5</span>
  <span class="stat-label">Max colors per slide</span>
</div>

</div>

><span style="color:#6EC8FF; font-weight:700">Principle:</span> Pair icons, patterns, or labels with color. Never rely on color alone to convey information (WCAG 2.1 SC 1.4.1).

<div class="vis-row">

<div class="vis-card">
  <img src="/home/sam/Development/marp-presentation-tools/icons/material-symbols_palette.svg" width="40" />
  <h4>Palette</h4>
  <p>Base > Surface > Primary > Accent > Text</p>
</div>

<div class="vis-card">
  <img src="/home/sam/Development/marp-presentation-tools/icons/material-symbols_bar-chart.svg" width="40" />
  <h4>Best Charts</h4>
  <p>Bar, line, scatter, stacked bar</p>
</div>

<div class="vis-card">
  <img src="/home/sam/Development/marp-presentation-tools/icons/material-symbols_route.svg" width="40" />
  <h4>Avoid</h4>
  <p>Pie &gt;3 segments, 3D, dense tables</p>
</div>

</div>

<style scoped>
section { display: block; }
.data-row {
  display: flex;
  gap: 20px;
  width: 100%;
  margin-bottom: 20px;
}
.data-card {
  flex: 1 1 0;
  text-align: center;
  background: #FAFAFB;
  border: 0.75px solid #6EC8FF;
  border-radius: 10px;
  padding: 16px;
}
.stat {
  display: block;
  font-size: 42pt;
  font-weight: 700;
  color: #6EC8FF;
  line-height: 1;
  margin-bottom: 6px;
}
.stat-label {
  display: block;
  font-size: 13pt;
  line-height: 1.3;
  color: #00132B;
}
blockquote {
  margin: 0 0 18px 0;
}
.vis-row {
  display: flex;
  gap: 14px;
  width: 100%;
}
.vis-card {
  flex: 1 1 0;
  background: #FAFAFB;
  border: 0.75px solid #B6E3FF;
  border-radius: 8px;
  padding: 14px;
}
.vis-card h4 {
  font-size: 14pt;
  font-weight: 700;
  color: #00132B;
  margin: 6px 0 4px 0;
}
.vis-card p {
  font-size: 12pt;
  margin: 0;
  line-height: 1.4;
  color: #000;
}
</style>

---

# Narrative Structure & Failure Modes

<div class="asym-row">

<div class="asym-main">
  <span class="asym-number">SCQA</span>
  <span class="asym-desc">Situation > Complication > Question > Answer</span>
  <hr class="asym-divider" />
  <span class="asym-number">1:2</span>
  <span class="asym-desc">Pacing ratio - 1 slide per 2 minutes, 15 min = 7-8 slides</span>
</div>

<div class="asym-side">
  <div class="fail-card f2">
    <span class="fail-id">F2</span>
    <span class="fail-name">Overfill</span>
    <span class="fail-fix">Reduce font or count</span>
  </div>
  <div class="fail-card f6">
    <span class="fail-id">F6</span>
    <span class="fail-name">Contrast Failure</span>
    <span class="fail-fix">Adjust colors per WCAG</span>
  </div>
  <div class="fail-card f8">
    <span class="fail-id">F8</span>
    <span class="fail-name">Narrative Disconnect</span>
    <span class="fail-fix">Restructure with SCQA</span>
  </div>
</div>

</div>

<style scoped>
section { display: block; }
.asym-row {
  display: flex;
  gap: 24px;
  width: 100%;
  margin-top: 10px;
}
.asym-main {
  flex: 2;
  padding: 24px;
  background: #FAFAFB;
  border: 1.5px solid #6EC8FF;
  border-radius: 12px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.asym-number {
  display: block;
  font-size: 36pt;
  font-weight: 700;
  color: #6EC8FF;
  line-height: 1.1;
}
.asym-desc {
  display: block;
  font-size: 15pt;
  line-height: 1.4;
  margin-top: 6px;
  color: #000;
}
.asym-divider {
  border: none;
  border-top: 1px solid #B6E3FF;
  margin: 16px auto;
  width: 60%;
}
.asym-side {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.fail-card {
  flex: 1;
  background: #FAFAFB;
  border-radius: 8px;
  padding: 12px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  border-left: 4px solid;
}
.f2 { border-left-color: #EF4444; }
.f6 { border-left-color: #F59E0B; }
.f8 { border-left-color: #6EC8FF; }
.fail-id {
  font-size: 11pt;
  font-weight: 700;
  color: #00132B;
}
.fail-name {
  font-size: 16pt;
  font-weight: 600;
  color: #000;
}
.fail-fix {
  font-size: 12pt;
  color: #666;
}
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

# Tool Comparison: Quality Approach

<div class="image-slide">

<div class="image-container">
  <img src="/home/sam/Development/marp-presentation-tools/output/chart-visual.png" class="slide-image" />
  <span class="image-caption">AI presentation tools ranked by quality feedback mechanism</span>
</div>

<div class="image-sidebar">

<h3>Key Finding</h3>
<p>Tools rely on template constraints and human review — no automated visual QA loop exists.</p>

<h3>Our Advantage</h3>
<p>Code-first agentic workflow with pixel analysis, CSS/DOM inspection, and structured VLM evaluation closes this gap.</p>

</div>

</div>

<style scoped>
section { display: block; }
.image-slide {
  display: flex;
  gap: 24px;
  margin-top: 14px;
  align-items: flex-start;
}
.image-container {
  flex: 2;
}
.slide-image {
  width: 100%;
  border: 0.75px solid #6EC8FF;
  border-radius: 10px;
  display: block;
}
.image-caption {
  display: block;
  font-size: 11pt;
  color: #666;
  font-style: italic;
  margin-top: 6px;
  text-align: center;
}
.image-sidebar {
  flex: 1;
  background: #FAFAFB;
  border: 0.75px solid #6EC8FF;
  border-radius: 10px;
  padding: 18px;
}
.image-sidebar h3 {
  font-size: 15pt;
  font-weight: 700;
  color: #00132B;
  margin: 0 0 6px 0;
}
.image-sidebar p {
  font-size: 13pt;
  line-height: 1.5;
  margin: 0 0 16px 0;
  color: #000;
}
.image-sidebar p:last-child { margin-bottom: 0; }
</style>

---

# Open-Source Agentic Pipelines

<div class="card-row">

<div class="card">
  <img src="/home/sam/Development/marp-presentation-tools/icons/material-symbols_layers.svg" width="40" class="card-icon" />
  <h3>sunbigfly/ppt-agent-skills</h3>
  <p>Multi-agent state machine, 4 subagents, JSON contract architecture, Pillow pixel QA, stateless resume</p>
</div>

<div class="card">
  <img src="/home/sam/Development/marp-presentation-tools/icons/material-symbols_build.svg" width="40" class="card-icon" />
  <h3>Akxan/ppt-agent-skill</h3>
  <p>26 production styles, 14 typography rules, 18 chart types (SVG), 8 failure modes with fix protocols</p>
</div>

<div class="card">
  <img src="/home/sam/Development/marp-presentation-tools/icons/material-symbols_bar-chart.svg" width="40" class="card-icon" />
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

<div class="process-flow">

<div class="step">
  <div class="step-number">1</div>
  <h3>Stage A</h3>
  <p>Per-slide visual audit: balance, readability, color harmony</p>
</div>

<div class="step-arrow">→</div>

<div class="step">
  <div class="step-number">2</div>
  <h3>Stage B</h3>
  <p>Deck-wide narrative audit: arc, progression, pacing</p>
</div>

<div class="step-arrow">→</div>

<div class="step">
  <div class="step-number">3</div>
  <h3>Output</h3>
  <p>theme-contract.json + qa-report.json fed back to agent</p>
</div>

</div>

<div class="principle-callout">
  <span class="label">Key Design Decision</span>
  <span class="principle-text">VLM for <strong>semantic</strong> checks; CSS/DOM inspection for <strong>quantitative</strong> measurements. Never ask VLM to measure margins.</span>
</div>

<style scoped>
section { display: block; }
.process-flow {
  display: flex;
  align-items: center;
  gap: 10px;
  width: 100%;
  margin-top: 24px;
}
.step {
  flex: 1;
  background: #FAFAFB;
  border: 0.75px solid #6EC8FF;
  border-radius: 12px;
  padding: 18px;
  text-align: center;
}
.step-number {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  background: #6EC8FF;
  color: white;
  font-size: 18pt;
  font-weight: 700;
  border-radius: 50%;
  margin-bottom: 10px;
}
.step h3 {
  font-size: 16pt;
  font-weight: 700;
  color: #00132B;
  margin: 0 0 6px 0;
}
.step p {
  font-size: 12pt;
  line-height: 1.4;
  margin: 0;
  color: #000;
}
.step-arrow {
  font-size: 28pt;
  color: #6EC8FF;
  font-weight: 700;
  flex-shrink: 0;
}
.principle-callout {
  margin-top: 20px;
  padding: 16px;
  background: #FAFAFB;
  border-left: 4px solid #6EC8FF;
  border-radius: 6px;
}
.principle-callout .label {
  display: block;
  font-size: 10pt;
  font-weight: 700;
  color: #6EC8FF;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 4px;
}
.principle-callout .principle-text {
  display: block;
  font-size: 14pt;
  line-height: 1.5;
  color: #000;
}
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
