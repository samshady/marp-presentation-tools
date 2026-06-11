#!/usr/bin/env python3
"""
Spell-check Marp presentation slides using hunspell.

Detects the language from the markdown frontmatter's `lang:` field
(defaults to en_US). Reports per-slide misspellings with line numbers.

Usage:
    python3 check-spelling.py presentation.md
    python3 check-spelling.py presentation.md --lang en_GB
    python3 check-spelling.py presentation.md --json   (machine-readable)
"""

import argparse
import json
import os
import re
import subprocess
import sys


SKIP_PATTERNS = [
    r"^---$",                    # YAML frontmatter delimiter
    r"^<style",                  # Style blocks
    r"^</style>",
    r"^<!--",                    # HTML comments
    r"^-->",
    r"^```",                     # Code blocks
    r"^#",                       # Headers (often contain proper nouns)
    r"^\s*$",                    # Empty lines
    r"^>",                       # Blockquotes
    r"class=\"",                 # CSS class names
    r"url\(|src=",               # URLs and paths
    r"http[s]?://",              # URLs
    r"git@",                     # Git URLs
    r"[./]svg|\.png|\.jpg",      # File extensions
    r"arXiv|WCAG|VLM|CSS|DOM|MCP|QA|PPTX|PDF|Markdown|Marp|SVG|HTML",  # Acronyms
    r"sunbigfly|Akxan|DeepSlide",  # Proper project names
    r"theme-contract|qa-report|planning\.json",  # Pipeline artifacts
]

# Technical terms specific to these presentations that hunspell may not know
CUSTOM_WORDS = {
    "cargobeamer", "unihalle", "marp", "bento", "SCQA", "Axiforma",
    "Iconify", "WCAG", "VLM", "MCP", "CVD", "deuteranopia", "protanopia",
    "Sankey", "Choropleth", "sparkline", "wireframe", "mockup",
    "repo", "config", "frontmatter", "scoped", "paginate",
    "GitHub", "CLI", "API", "JSON", "YAML", "SVG", "PNG", "PPTX", "PDF",
    "Tome", "Canva", "Beautiful", "Mayer", "Tufte", "Duarte",
    "McKinsey", "Minto", "Mayer's", "AI", "MS", "px", "Markov",
    "pre-training", "coherence", "signaling", "segmenting",
    "pre-training", "contiguity", "modality", "overfill", "underfill",
    "underused", "bento", "github", "http", "pre", "multi", "auto",
}

# Words likely to be actual typos (never in dictionary)
COMMON_TYPOS = {
    "teh": "the", "recieve": "receive", "acheive": "achieve",
    "occured": "occurred", "ocurred": "occurred", "seperate": "separate",
    "definately": "definitely", "definately": "definitely",
    "goverment": "government", "alot": "a lot",
}


def get_language(md_path: str) -> str:
    """Detect language from frontmatter, default en_US."""
    try:
        with open(md_path) as f:
            content = f.read()
        m = re.search(r"^lang:\s*[\"']?([\w_-]+)", content, re.MULTILINE)
        return m.group(1) if m else "en_US"
    except FileNotFoundError:
        return "en_US"


def get_all_text_blocks(md_path: str) -> list:
    """Split markdown into slides, returning per-slide text blocks with line numbers."""
    with open(md_path) as f:
        lines = f.readlines()

    slides = []
    current_slide = []
    in_code_block = False
    in_style_block = False

    for line_num, line in enumerate(lines, 1):
        stripped = line.rstrip()

        # Track code blocks
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue

        # Track style blocks
        if stripped.startswith("<style"):
            in_style_block = True
            continue
        if in_style_block and stripped == "</style>":
            in_style_block = False
            continue
        if in_style_block or in_code_block:
            continue

        # Slide separator
        if stripped == "---" and line_num > 1:
            if current_slide:
                slides.append(current_slide)
                current_slide = []
            continue

        # Skip frontmatter (first --- block before slide 1)
        if stripped == "---" and not slides and not current_slide:
            continue

        current_slide.append((line_num, stripped))

    if current_slide:
        slides.append(current_slide)

    return slides


def should_skip_line(text: str) -> bool:
    """Check if a line should be skipped (code, markup, acronyms)."""
    for pattern in SKIP_PATTERNS:
        if re.search(pattern, text.strip()):
            return True
    return False


def extract_words(text: str) -> list:
    """Extract individual words from a line, handling inline HTML."""
    # Remove HTML tags
    text = re.sub(r"<[^>]+>", " ", text)
    # Remove markdown links
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # Split on non-alphabetic characters (keep apostrophes for contractions)
    words = re.findall(r"[A-Za-z][A-Za-z']+(?:'[A-Za-z]+)?", text)
    return words


def check_line_spelling(line_num: int, text: str, lang: str) -> list:
    """Check a single line for spelling errors using hunspell."""
    if should_skip_line(text):
        return []

    words = extract_words(text)
    if not words:
        return []

    errors = []
    for word in words:
        word_lower = word.lower().strip("'")
        if not word_lower:
            continue
        if word_lower in CUSTOM_WORDS or word_lower in {w.lower() for w in CUSTOM_WORDS}:
            continue
        if len(word_lower) <= 1:
            continue
        # Check if it looks like code (camelCase, snake_case, etc.)
        if re.search(r'[a-z][A-Z]', word):
            continue
        if '_' in word:
            continue

        result = subprocess.run(
            ["hunspell", "-d", lang, "-l"],
            input=word_lower + "\n",
            capture_output=True, text=True, timeout=5
        )
        misspelled = result.stdout.strip()
        if misspelled:
            suggestion = COMMON_TYPOS.get(word_lower, "")
            errors.append({
                "line": line_num,
                "word": word,
                "suggestion": suggestion,
            })

    return errors


def check_spelling(md_path: str, lang: str = "en_US") -> dict:
    """Spell-check the entire presentation."""
    slides = get_all_text_blocks(md_path)
    all_errors = []

    for slide_idx, slide_lines in enumerate(slides):
        slide_errors = []
        for line_num, text in slide_lines:
            errors = check_line_spelling(line_num, text, lang)
            slide_errors.extend(errors)

        all_errors.append({
            "slide": slide_idx + 1,
            "errors": slide_errors,
        })

    return {
        "file": os.path.basename(md_path),
        "language": lang,
        "total_slides": len(slides),
        "total_errors": sum(len(s["errors"]) for s in all_errors),
        "slides": all_errors,
    }


def print_report(results: dict):
    """Print a human-readable spelling report."""
    total = results["total_errors"]
    print(f"\n{'='*60}")
    print(f"SPELLING CHECK REPORT")
    print(f"File: {results['file']}")
    print(f"Lang: {results['language']}")
    print(f"{'='*60}")

    if total == 0:
        print(f"\n{'  '*5} All good!")
        return

    has_typos = False
    for slide in results["slides"]:
        if not slide["errors"]:
            continue
        print(f"\n-- Slide {slide['slide']} --")
        for err in slide["errors"]:
            ctx = f"  -> suggestion: {err['suggestion']}" if err["suggestion"] else ""
            print(f"  L{err['line']:>4}: {err['word']}{ctx}")
            has_typos = True

    if has_typos:
        common = {}
        for slide in results["slides"]:
            for err in slide["errors"]:
                if err["suggestion"]:
                    common[err["word"]] = err["suggestion"]
        if common:
            print(f"\n-- Known typos (auto-fix available) --")
            for word, fix in common.items():
                print(f"  {word} -> {fix}")

    print(f"\nTotal: {total} issue(s)")


def fix_typos(md_path: str, results: dict) -> tuple:
    """Apply auto-fixes for known typos."""
    with open(md_path) as f:
        content = f.read()

    fixes = []
    for slide in results["slides"]:
        for err in slide["errors"]:
            if err["suggestion"]:
                old = err["word"]
                new = err["suggestion"]
                # Only replace full word (not substring)
                content = re.sub(r'\b' + re.escape(old) + r'\b', new, content)
                fixes.append(f"  {old} -> {new}")

    if fixes:
        with open(md_path, "w") as f:
            f.write(content)

    return fixes


def main():
    p = argparse.ArgumentParser(description="Spell-check Marp presentations")
    p.add_argument("md_path", help="Path to the markdown file")
    p.add_argument("--lang", help="Language code (e.g. en_US, en_GB)", default=None)
    p.add_argument("--json", action="store_true", help="Machine-readable output")
    p.add_argument("--fix", action="store_true", help="Auto-fix known typos")
    args = p.parse_args()

    if not os.path.exists(args.md_path):
        print(f"Error: file not found: {args.md_path}")
        sys.exit(1)

    lang = args.lang or get_language(args.md_path)
    results = check_spelling(args.md_path, lang)

    if args.fix:
        fixes = fix_typos(args.md_path, results)
        if fixes:
            print("Applied fixes:")
            for f in fixes:
                print(f)
        else:
            print("No auto-fixable typos found.")
        # Re-check after fixes
        results = check_spelling(args.md_path, lang)

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print_report(results)

    sys.exit(1 if results["total_errors"] > 0 else 0)


if __name__ == "__main__":
    main()
