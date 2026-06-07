# Marp Presentation Tools

Themes, skills, and tools for Marp markdown presentations.

## Themes

Two themes in `themes/`:

### `cargobeamer` — CargoBeamer brand

- Logo: CSS `background-image` on `section` (top-left `30px 30px`, 150px wide)
- Font: Axiforma 20pt
- h1: `#6EC8FF` 40pt, h2: `#00132B` 28pt
- Table header: `#B6E3FF` bg, black text
- Blockquote: `#FAFAFB` bg, `#6EC8FF` left border

### `unihalle` — MLU Halle-Wittenberg brand

- Logo: CSS `background-image` on `section` (right `40px`, top `15px`, 100px wide)
- Logo hidden on `section.title` slides via `background-image: none`
- Font: Helvetica 24pt
- h1: `#9FBF47` (MLU green) 1.4em, h2: `#295A97` (MLU blue) 1.1em
- Header/footer: `#928781` (18px, inherited from default theme)
- Blockquote: `#F5F5F2` bg, `#9FBF47` left border 6px
- Table header: `#295A97` bg, white text
- `.focus-text` for agenda descriptions (italic, `#928781`)

## How themes work

Both themes use `background-image` on the `section` element to embed logos. This works reliably inside Marp's SVG `<foreignObject>` rendering. The images are hosted as PNGs on GitHub raw. VS Code loads the theme CSS from remote URLs specified in `markdown.marp.themes` in settings.json.

## VS Code Setup

In `~/.config/Code/User/settings.json`:

```json
"markdown.marp.themes": [
    "https://raw.githubusercontent.com/samshady/marp-presentation-tools/refs/heads/main/themes/cargobeamer.css",
    "https://raw.githubusercontent.com/samshady/marp-presentation-tools/refs/heads/main/themes/unihalle.css",
],
```

Add `?v=N` to force cache refresh after theme changes.

## CLI Setup

Two `.marprc` files configure theme paths:

- **Global** (`~/.marprc`): absolute paths — works from any directory
- **Per-project** (repo root): relative paths — works inside the repo

Both enable `html: true` for raw HTML in slides.

## VS Code Snippets

Four markdown snippets in `~/.config/Code/User/snippets/markdown.json`:

| Prefix | Action |
|---|---|
| `marp-cb` | cargobeamer frontmatter + title slide |
| `marp-uni` | unihalle frontmatter with MLU header + title slide |
| `marp-cb-slide` | cargobeamer content slide (h2 + bullets) |
| `marp-uni-slide` | unihalle content slide (h2 + bullets) |

## Skills (Kilo/Claude)

Two skills for AI-assisted presentation creation:

- **marp-presentation-creator**: Generates new presentations with correct frontmatter, layout, and theme
- **marp-presentation-quality**: Analyzes slides for overflow, underuse, and styling issues

Both are at `skills/` in this repo and synced to `~/.kilo/skills/`.

## Known issues & history

- Remote CSS URLs in `markdown.marp.themes` are cached by VS Code — use `?v=N` to bust cache after edits
- `background-image` on `section` is the only reliable way to show logos inside Marp's SVG foreignObject rendering
- JPG format doesn't render as `background-image` inside SVG foreignObject (Chromium quirk) — always use PNG
- The `::before` pseudo-element approach doesn't render `background-image` inside SVG foreignObject
- Base64 data URIs >~10KB may be truncated by VS Code's Marp extension when used via remote CSS URLs — use external URLs instead

## File reference

| File | Purpose |
|---|---|
| `themes/cargobeamer.css` | CargoBeamer brand theme |
| `themes/unihalle.css` | MLU brand theme |
| `skills/marp-presentation-creator/` | Kilo skill for creating presentations |
| `skills/marp-presentation-quality/` | Kilo skill for analyzing presentation quality |
| `tools/bib-format/` | APA bibliography formatting |
| `tools/presentation-quality/` | Slide quality analysis scripts |
| `tools/slide-fixes/` | Automated slide fix scripts |
| `docs/slide-rules.md` | Slide dimension and constraint reference |
| `Cargobeamer_Logo.png` | Embedded in cargobeamer theme CSS |
| `uni_halle_logo.png` | Embedded in unihalle theme CSS |
