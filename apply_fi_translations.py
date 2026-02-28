#!/usr/bin/env python3
"""
Apply all Finnish translation fixes to breed pages.
Fixes mixed English/Finnish text in Best For, Not Ideal For sections.
"""

import re
from pathlib import Path

from fi_translations import FIXES

FI_BREEDS_DIR = Path(__file__).parent / "fi" / "breeds"


def apply_fixes(html):
    """Apply all translation fixes to Finnish HTML."""
    updated = html
    
    # Sort fixes by length (longest first) to avoid partial replacements
    sorted_fixes = sorted(FIXES.items(), key=lambda x: len(x[0]), reverse=True)
    
    for original, fixed in sorted_fixes:
        # Replace in span tags for Best For / Not Ideal items
        pattern_span = f'<span>{re.escape(original)}</span>'
        replacement_span = f'<span>{fixed}</span>'
        updated = re.sub(pattern_span, replacement_span, updated)
    
    return updated


def main():
    breeds = sorted([f.stem for f in FI_BREEDS_DIR.glob("*.html")])
    print(f"Total Finnish breeds: {len(breeds)}")
    
    translated = 0
    for i, breed in enumerate(breeds):
        fi_path = FI_BREEDS_DIR / f"{breed}.html"
        fi_html = fi_path.read_text()
        
        updated_html = apply_fixes(fi_html)
        
        if updated_html != fi_html:
            fi_path.write_text(updated_html)
            translated += 1
        
        if (i + 1) % 50 == 0:
            print(f"  Progress: {i+1}/{len(breeds)}")
    
    print(f"\nDone! Updated {translated} breed files.")


if __name__ == "__main__":
    main()
