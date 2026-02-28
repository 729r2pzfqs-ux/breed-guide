#!/usr/bin/env python3
"""Chinese translations for breed pages - fixing mistranslated CSS classes."""

# Fix CSS class mistranslations - "bold" was incorrectly translated to Chinese
FIXES = {
    # CSS class names that were mistranslated
    "font-大胆的": "font-bold",
    "font-semi大胆的": "font-semibold",
}

if __name__ == "__main__":
    print(f"Total Chinese fixes: {len(FIXES)}")
