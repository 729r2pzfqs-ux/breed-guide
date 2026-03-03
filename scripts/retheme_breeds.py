#!/usr/bin/env python3
"""
retheme_breeds.py
-----------------
Retheme BreedFinder breed HTML pages from the blue/sky palette to Forest Green.

Usage:
    python retheme_breeds.py <input_dir> <output_dir> [--dry-run]

Arguments:
    input_dir   Directory containing source .html breed files
    output_dir  Directory where rethemed files will be written
    --dry-run   Report changes without writing any files
"""

import argparse
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# 1. Font loading replacement
# ---------------------------------------------------------------------------
# Matches the Google Fonts URL portion for Plus Jakarta Sans and replaces it
# with Fraunces + Inter.
FONT_LINK_RE = re.compile(
    r'(https://fonts\.googleapis\.com/css2\?family=)Plus\+Jakarta\+Sans:[^"\']+'  ,
    re.IGNORECASE,
)
FONT_NEW = (
    "Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,600;"
    "0,9..144,700;1,9..144,400;1,9..144,600&family=Inter:wght@400;500;600;700"
)

# ---------------------------------------------------------------------------
# 2. Tailwind config fontFamily replacement
# ---------------------------------------------------------------------------
TW_FONT_OLD = "fontFamily: { sans: ['Plus Jakarta Sans', 'sans-serif'] }"
TW_FONT_NEW = (
    "fontFamily: { sans: ['Inter', 'sans-serif'], serif: ['Fraunces', 'Georgia', 'serif'] }"
)

# ---------------------------------------------------------------------------
# 3. Tailwind class replacements
#
#    CRITICAL ORDERING RULE: when one token is a prefix of another
#    (e.g. "from-sky-50" is a prefix of "from-sky-500"), the LONGER token
#    must appear first so str.replace does not corrupt it.
# ---------------------------------------------------------------------------
CLASS_REPLACEMENTS = [
    # --- gradient from ---
    ("from-sky-500",         "from-emerald-700"),   # before from-sky-50
    ("from-sky-50",          "from-[#f6f7f2]"),

    # --- gradient to ---
    ("to-blue-600",          "to-emerald-800"),
    ("to-blue-50",           "to-[#eef1e8]"),
    ("to-sky-50",            "to-[#eef1e8]"),

    # --- gradient via ---
    ("via-blue-50",          "via-[#eef1e8]"),
    ("via-sky-50",           "via-[#eef1e8]"),

    # --- background (longer suffix first within each colour family) ---
    ("bg-sky-100",           "bg-[#eef1e8]"),       # before bg-sky-50
    ("bg-sky-50",            "bg-[#f6f7f2]"),
    ("bg-slate-900",         "bg-[#1a2e1a]"),
    ("bg-slate-800",         "bg-[#2a2518]"),
    ("bg-slate-100",         "bg-[#f0ede6]"),
    ("bg-slate-50",          "bg-[#faf9f6]"),

    # --- borders (longer numeric suffixes first) ---
    ("border-sky-500",       "border-emerald-700"),
    ("border-sky-400",       "border-emerald-600"),
    ("border-sky-200",       "border-[#dde3d4]"),
    ("border-sky-100",       "border-[#dde3d4]"),
    ("border-slate-800",     "border-[#2a2518]"),
    ("border-slate-200",     "border-[#e2ddd4]"),
    ("border-slate-100",     "border-[#f0ede6]"),

    # --- text colours (longer numeric suffixes first) ---
    ("text-sky-800",         "text-emerald-900"),
    ("text-sky-700",         "text-emerald-800"),
    ("text-sky-500",         "text-emerald-700"),
    ("text-slate-900",       "text-[#1a2e1a]"),
    ("text-slate-800",       "text-[#2a2518]"),
    ("text-slate-700",       "text-[#3d3829]"),
    ("text-slate-600",       "text-[#5c5647]"),
    ("text-slate-500",       "text-[#7a7265]"),
    ("text-slate-400",       "text-[#9a9285]"),
    ("text-slate-300",       "text-[#c8c1b5]"),

    # --- hover variants ---
    ("hover:text-sky-700",   "hover:text-emerald-800"),
    ("hover:border-sky-400", "hover:border-emerald-600"),

    # --- ring ---
    ("ring-sky-500",         "ring-emerald-700"),

    # --- shadow colour helpers ---
    ("shadow-sky-500/20",    "shadow-emerald-700/20"),
]

# ---------------------------------------------------------------------------
# 4. Hex colour replacements (inline styles / CSS colour values)
# ---------------------------------------------------------------------------
HEX_REPLACEMENTS = [
    ("#0ea5e9", "#1a5632"),   # sky-500
    ("#2563eb", "#1a5632"),   # blue-600
    ("#3b82f6", "#1a5632"),   # blue-500
    ("#e2e8f0", "#e2ddd4"),   # slate-200
]

# ---------------------------------------------------------------------------
# 5. Logo replacement
# ---------------------------------------------------------------------------
LOGO_OLD = "logo-192.png"
LOGO_NEW = "logo-192-green.png"

# ---------------------------------------------------------------------------
# 6. rgba shadow colour replacements (in <style> blocks)
# ---------------------------------------------------------------------------
RGBA_REPLACEMENTS = [
    # Versions without spaces
    ("rgba(0,0,0,0.06)", "rgba(26,86,50,0.06)"),
    ("rgba(0,0,0,0.05)", "rgba(26,86,50,0.05)"),
    ("rgba(0,0,0,0.04)", "rgba(26,86,50,0.04)"),
    ("rgba(0,0,0,0.03)", "rgba(26,86,50,0.03)"),
    # Versions with spaces
    ("rgba(0, 0, 0, 0.06)", "rgba(26,86,50,0.06)"),
    ("rgba(0, 0, 0, 0.05)", "rgba(26,86,50,0.05)"),
    ("rgba(0, 0, 0, 0.04)", "rgba(26,86,50,0.04)"),
    ("rgba(0, 0, 0, 0.03)", "rgba(26,86,50,0.03)"),
]

# ---------------------------------------------------------------------------
# 7. Heading font-serif injection
#    Add "font-serif" to class attribute of <h1>, <h2>, <h3> if not present.
# ---------------------------------------------------------------------------
HEADING_WITH_CLASS_RE = re.compile(
    r'(<h[123]\b[^>]*\bclass\s*=\s*")([^"]*)"',
    re.IGNORECASE,
)

HEADING_NO_CLASS_RE = re.compile(
    r'(<h[123]\b)(?![^>]*\bclass\s*=)([^>]*>)',
    re.IGNORECASE,
)


def _inject_font_serif_with_class(match: re.Match) -> str:
    """Add font-serif to a heading that already has a class attribute."""
    prefix = match.group(1)   # e.g.  <h2 class="
    classes = match.group(2)  # existing class string
    if "font-serif" in classes.split():
        return match.group(0)  # already present, leave untouched
    new_classes = (classes.rstrip() + " font-serif")
    return f'{prefix}{new_classes}"'


def _inject_font_serif_no_class(match: re.Match) -> str:
    """Add class=\"font-serif\" to a heading that has no class attribute."""
    return f'{match.group(1)} class="font-serif"{match.group(2)}'


# ---------------------------------------------------------------------------
# Core transformation
# ---------------------------------------------------------------------------

def transform(html: str) -> str:
    """Apply all retheme transformations to an HTML string and return result."""

    # 1. Google Fonts URL
    html = FONT_LINK_RE.sub(lambda m: m.group(1) + FONT_NEW, html)

    # 2. Tailwind config fontFamily
    html = html.replace(TW_FONT_OLD, TW_FONT_NEW)

    # 3. Tailwind class substitutions (plain string, in ordered list)
    for old, new in CLASS_REPLACEMENTS:
        html = html.replace(old, new)

    # 4. Hex colour values (case-insensitive)
    for old, new in HEX_REPLACEMENTS:
        html = re.sub(re.escape(old), new, html, flags=re.IGNORECASE)

    # 5. Logo filename
    html = html.replace(LOGO_OLD, LOGO_NEW)

    # 6. rgba shadow colours
    for old, new in RGBA_REPLACEMENTS:
        html = html.replace(old, new)

    # 7. Inject font-serif into headings
    html = HEADING_WITH_CLASS_RE.sub(_inject_font_serif_with_class, html)
    html = HEADING_NO_CLASS_RE.sub(_inject_font_serif_no_class, html)

    return html


# ---------------------------------------------------------------------------
# File processing
# ---------------------------------------------------------------------------

def process_file(src: Path, dst: Path, dry_run: bool) -> bool:
    """
    Read src, transform, optionally write to dst.
    Returns True if the file was / would be changed.
    """
    original = src.read_text(encoding="utf-8")
    transformed = transform(original)
    changed = original != transformed

    if dry_run:
        status = "CHANGED  " if changed else "unchanged"
        print(f"  [{status}] {src.name}")
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(transformed, encoding="utf-8")
        status = "written  " if changed else "copied (no changes)"
        print(f"  [{status}] {src.name}  →  {dst}")

    return changed


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Retheme BreedFinder breed HTML pages to Forest Green theme."
    )
    parser.add_argument("input_dir",  help="Directory containing source .html files")
    parser.add_argument("output_dir", help="Directory to write rethemed .html files")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report what would change without writing any files",
    )
    args = parser.parse_args()

    input_dir  = Path(args.input_dir)
    output_dir = Path(args.output_dir)

    if not input_dir.is_dir():
        print(f"ERROR: input_dir is not a directory: {input_dir}", file=sys.stderr)
        sys.exit(1)

    html_files = sorted(input_dir.glob("*.html"))
    if not html_files:
        print(f"No .html files found in {input_dir}")
        sys.exit(0)

    mode = "DRY RUN" if args.dry_run else "Processing"
    print(f"\n{mode}: {len(html_files)} file(s)")
    print(f"  from  {input_dir}")
    if not args.dry_run:
        print(f"  to    {output_dir}")
    print()

    changed_count = 0
    for src in html_files:
        dst = output_dir / src.name
        if process_file(src, dst, args.dry_run):
            changed_count += 1

    total     = len(html_files)
    unchanged = total - changed_count
    print(f"\nDone. {total} file(s) processed — {changed_count} changed, {unchanged} unchanged.")


if __name__ == "__main__":
    main()
