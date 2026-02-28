#!/usr/bin/env python3
"""
Apply all Turkish translation fixes to breed pages.
Fixes mixed English/Turkish text in Best For, Not Ideal For sections.
"""

import re
from pathlib import Path

from tr_translations import FIXES

TR_BREEDS_DIR = Path(__file__).parent / "tr" / "breeds"


def apply_fixes(html):
    """Apply all translation fixes to Turkish HTML."""
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
    breeds = sorted([f.stem for f in TR_BREEDS_DIR.glob("*.html")])
    print(f"Total Turkish breeds: {len(breeds)}")
    
    translated = 0
    for i, breed in enumerate(breeds):
        tr_path = TR_BREEDS_DIR / f"{breed}.html"
        tr_html = tr_path.read_text()
        
        updated_html = apply_fixes(tr_html)
        
        if updated_html != tr_html:
            tr_path.write_text(updated_html)
            translated += 1
        
        if (i + 1) % 50 == 0:
            print(f"  Progress: {i+1}/{len(breeds)}")
    
    print(f"\nDone! Updated {translated} breed files.")


if __name__ == "__main__":
    main()
