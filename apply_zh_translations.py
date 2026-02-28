#!/usr/bin/env python3
"""
Apply all Chinese translation fixes to breed pages.
Fixes mistranslated CSS class names (bold -> 大胆的).
"""

from pathlib import Path

from zh_translations import FIXES

ZH_BREEDS_DIR = Path(__file__).parent / "zh" / "breeds"


def apply_fixes(html):
    """Apply all translation fixes to Chinese HTML."""
    updated = html
    
    for original, fixed in FIXES.items():
        updated = updated.replace(original, fixed)
    
    return updated


def main():
    breeds = sorted([f.stem for f in ZH_BREEDS_DIR.glob("*.html")])
    print(f"Total Chinese breeds: {len(breeds)}")
    
    translated = 0
    for i, breed in enumerate(breeds):
        zh_path = ZH_BREEDS_DIR / f"{breed}.html"
        zh_html = zh_path.read_text()
        
        updated_html = apply_fixes(zh_html)
        
        if updated_html != zh_html:
            zh_path.write_text(updated_html)
            translated += 1
        
        if (i + 1) % 50 == 0:
            print(f"  Progress: {i+1}/{len(breeds)}")
    
    print(f"\nDone! Updated {translated} breed files.")


if __name__ == "__main__":
    main()
