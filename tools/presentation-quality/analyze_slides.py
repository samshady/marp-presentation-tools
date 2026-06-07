#!/usr/bin/env python3
"""
Marp Slide Analyzer — Render → Analyze → Report

Converts a Marp markdown file to PDF, then detects:
- Text overflow (content too close to bottom edge)
- Underuse (content too far from bottom edge)
- Content density warnings

Usage:
    python3 analyze_slides.py presentation.md
    python3 analyze_slides.py presentation.md --fix  (auto-adjust font sizes)
"""

import json
import os
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path


# ─── Constants ──────────────────────────────────────────────────────────────

# Marp default slide dimensions (960x540 pt = 16:9 at 2pt/px)
SLIDE_WIDTH_PT = 960
SLIDE_HEIGHT_PT = 540
PT_PER_PX = 2  # 1px = 2pt in Marp's default output

HEADER_HEIGHT_PT = 35  # ~70px
FOOTER_HEIGHT_PT = 20  # ~40px
PADDING_PT = 25  # 50px

CONTENT_TOP_PT = HEADER_HEIGHT_PT + PADDING_PT
CONTENT_BOTTOM_PT = FOOTER_HEIGHT_PT + PADDING_PT
CONTENT_AREA_HEIGHT_PT = SLIDE_HEIGHT_PT - CONTENT_TOP_PT - CONTENT_BOTTOM_PT

OVERFLOW_THRESHOLD_PT = 10  # less than this from bottom = overflow
UNDERUSE_THRESHOLD_PT = 60  # more than this empty at bottom = too small


# ─── Analysis ───────────────────────────────────────────────────────────────

def get_pdf_info(pdf_path: str) -> dict:
    """Get PDF metadata using pdfinfo."""
    try:
        result = subprocess.run(
            ["pdfinfo", pdf_path], capture_output=True, text=True, timeout=10
        )
        info = {}
        for line in result.stdout.strip().split("\n"):
            if ":" in line:
                key, val = line.split(":", 1)
                info[key.strip()] = val.strip()
        return info
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return {}


def get_pdf_page_count(pdf_path: str) -> int:
    """Get page count from PDF."""
    info = get_pdf_info(pdf_path)
    return int(info.get("Pages", 0))


def convert_to_images(pdf_path: str, output_dir: str, dpi: int = 72):
    """Convert PDF pages to PNG images using pdftoppm."""
    try:
        subprocess.run(
            [
                "pdftoppm",
                "-png",
                "-r", str(dpi),
                pdf_path,
                os.path.join(output_dir, "slide"),
            ],
            capture_output=True,
            timeout=30,
        )
        images = sorted(Path(output_dir).glob("slide-*.png"))
        return [str(img) for img in images]
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return []


def analyze_image(image_path: str) -> dict:
    """Analyze a single slide image for content boundaries."""
    try:
        from PIL import Image
    except ImportError:
        return {"error": "PIL not installed. Run: pip install Pillow"}

    img = Image.open(image_path)
    width, height = img.size

    # Convert to grayscale for edge detection
    gray = img.convert("L")
    pixels = gray.load()

    # Find topmost non-white pixel (content start)
    top_edge = height
    for y in range(height):
        for x in range(width):
            if pixels[x, y] < 240:  # non-white
                top_edge = y
                break
        if top_edge < height:
            break

    # Find bottommost non-white pixel (content end)
    bottom_edge = 0
    for y in range(height - 1, -1, -1):
        for x in range(width):
            if pixels[x, y] < 240:
                bottom_edge = y
                break
        if bottom_edge > 0:
            break

    # Find leftmost and rightmost for horizontal centering check
    left_edge = width
    for x in range(width):
        for y in range(top_edge, bottom_edge + 1):
            if pixels[x, y] < 240:
                left_edge = x
                break
        if left_edge < width:
            break

    right_edge = 0
    for x in range(width - 1, -1, -1):
        for y in range(top_edge, bottom_edge + 1):
            if pixels[x, y] < 240:
                right_edge = x
                break
        if right_edge > 0:
            break

    content_height = bottom_edge - top_edge
    bottom_margin = height - bottom_edge

    # Convert to points
    scale = SLIDE_HEIGHT_PT / height
    issues = []

    if bottom_margin * scale < OVERFLOW_THRESHOLD_PT:
        issues.append("overflow")
    elif bottom_margin * scale > UNDERUSE_THRESHOLD_PT and content_height > 0:
        issues.append("underused")

    return {
        "top_edge_px": top_edge,
        "bottom_edge_px": bottom_edge,
        "left_edge_px": left_edge,
        "right_edge_px": right_edge,
        "content_height_px": content_height,
        "bottom_margin_px": bottom_margin,
        "bottom_margin_pt": round(bottom_margin * scale, 1),
        "issues": issues,
    }


def estimate_content_lines(md_path: str) -> dict:
    """Estimate content density from markdown."""
    with open(md_path) as f:
        content = f.read()

    # Split slides by ---
    slides = re.split(r"\n---\n", content)
    slide_stats = []

    for i, slide in enumerate(slides):
        # Strip frontmatter
        if i == 0 and slide.startswith("---"):
            parts = slide.split("---", 2)
            if len(parts) >= 3:
                slide = parts[2]

        # Strip style blocks
        slide = re.sub(r"<style[^>]*>.*?</style>", "", slide, flags=re.DOTALL)
        slide = re.sub(r"<[^>]+>", " ", slide)

        lines = [l.strip() for l in slide.split("\n") if l.strip()]
        word_count = len(" ".join(lines).split())
        bullet_count = len([l for l in lines if l.startswith("-") or l.startswith("*")])
        header_count = len([l for l in lines if l.startswith("#")])

        # Estimate rendered lines
        rendered_lines = 0
        for line in lines:
            if line.startswith("#"):
                rendered_lines += 1
            elif line.startswith("-") or line.startswith("*"):
                rendered_lines += 1
                # Check for long bullets
                if len(line) > 80:
                    rendered_lines += 1
            else:
                text_len = len(line)
                rendered_lines += max(1, text_len // 80 + 1)

        slide_stats.append({
            "slide": i + 1,
            "words": word_count,
            "bullets": bullet_count,
            "headers": header_count,
            "estimated_lines": rendered_lines,
        })

    return {
        "total_slides": len(slide_stats),
        "slides": slide_stats,
    }


# ─── Reports ────────────────────────────────────────────────────────────────

def generate_report(md_path: str, pdf_path: str, images: list, stats: dict):
    """Generate a human-readable report."""
    lines = []
    lines.append("=" * 60)
    lines.append(f"MARPA SLIDE ANALYSIS REPORT")
    lines.append(f"File: {md_path}")
    lines.append(f"PDF:  {pdf_path}")
    lines.append(f"Pages: {len(images)}")
    lines.append("=" * 60)

    content_stats = stats.get("content_stats", {})

    for i, img_path in enumerate(images):
        slide_num = i + 1
        info = content_stats.get(i, {})
        lines.append(f"\n── Slide {slide_num} ──")

        if "error" in info:
            lines.append(f"  ⚠ {info['error']}")
            continue

        issues = info.get("issues", [])
        if issues:
            for issue in issues:
                if issue == "overflow":
                    lines.append(f"  ❌ OVERFLOW: Content too close to bottom edge!")
                    lines.append(f"     Bottom margin: {info.get('bottom_margin_pt', '?')}pt (min 10pt)")
                elif issue == "underused":
                    lines.append(f"  ⚠ UNDERUSED: Large empty space at bottom")
                    lines.append(f"     Bottom margin: {info.get('bottom_margin_pt', '?')}pt (max 60pt)")
        else:
            lines.append(f"  ✅ OK")

        lines.append(f"     Content height: {info.get('content_height_px', '?')}px")
        lines.append(f"     Bottom margin:  {info.get('bottom_margin_pt', '?')}pt")

    # Content estimation
    est = content_stats.get("estimation", {})
    slides_data = est.get("slides", [])
    if slides_data:
        lines.append(f"\n── Content Density ──")
        for s in slides_data:
            status = "❌" if s["estimated_lines"] > 18 else "⚠" if s["estimated_lines"] > 14 else "✅"
            lines.append(f"  Slide {s['slide']}: {status} {s['words']:3d} words, "
                         f"{s['bullets']} bullets, ~{s['estimated_lines']} lines")

    lines.append("\n" + "=" * 60)
    return "\n".join(lines)


# ─── Main ───────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 analyze_slides.py presentation.md [--fix]")
        sys.exit(1)

    md_path = sys.argv[1]
    fix_mode = "--fix" in sys.argv

    if not os.path.exists(md_path):
        print(f"Error: File not found: {md_path}")
        sys.exit(1)

    with tempfile.TemporaryDirectory() as tmpdir:
        pdf_path = os.path.join(tmpdir, "output.pdf")

        # Step 1: Convert markdown to PDF
        print(f"Converting {md_path} to PDF...")
        result = subprocess.run(
            ["npx", "@marp-team/marp-cli", md_path, "--pdf", "--allow-local-files",
             "-o", pdf_path],
            capture_output=True, text=True, timeout=120,
        )
        if result.returncode != 0:
            print(f"Conversion failed:\n{result.stderr}")
            sys.exit(1)

        # Step 2: Convert PDF to images
        print("Rendering slides to images...")
        images = convert_to_images(pdf_path, tmpdir)
        if not images:
            print("Warning: Could not render images (pdftoppm required)")
            images = []

        # Step 3: Analyze images
        content_stats = {}
        for i, img_path in enumerate(images):
            content_stats[i] = analyze_image(img_path)

        # Step 4: Estimate content from markdown
        estimation = estimate_content_lines(md_path)

        content_stats["estimation"] = estimation

        # Step 5: Generate report
        report = generate_report(md_path, pdf_path, images, {
            "content_stats": content_stats,
        })
        print(report)

        # Step 6: Summary
        all_issues = []
        for i in range(len(images)):
            all_issues.extend(content_stats.get(i, {}).get("issues", []))
        for s in estimation.get("slides", []):
            if s["estimated_lines"] > 18:
                all_issues.append(f"slide_{s['slide']}_dense")

        if all_issues:
            print(f"\n⚠ Found {len(all_issues)} issue(s)")
            sys.exit(1 if any("overflow" in i for i in all_issues) else 0)
        else:
            print(f"\n✅ All {len(images)} slides look good!")
            sys.exit(0)


if __name__ == "__main__":
    main()
