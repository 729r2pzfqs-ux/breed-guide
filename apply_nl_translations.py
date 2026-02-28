#!/usr/bin/env python3
"""
Apply all Dutch translations to breed pages.
Translates Best For, Not Ideal For, and temperament tags.
"""

import re
from pathlib import Path

from nl_translations import BEST_FOR, NOT_IDEAL, TEMPERAMENT_TAGS

NL_BREEDS_DIR = Path(__file__).parent / "nl" / "breeds"


def translate_text(text, translations_dict):
    """Translate text using dictionary."""
    text = text.strip()
    if text in translations_dict:
        return translations_dict[text]
    if text.title() in translations_dict:
        return translations_dict[text.title()]
    if text.lower() in translations_dict:
        return translations_dict[text.lower()]
    return text


def apply_translations(html):
    """Apply all translations to Dutch HTML."""
    updated = html

    # Replace Best For items (green dots)
    def replace_best_for(match):
        original = match.group(1).strip()
        translated = translate_text(original, BEST_FOR)
        return f'<span class="w-2 h-2 mt-2 bg-emerald-500 rounded-full"></span><span>{translated}</span>'

    pattern = r'<span class="w-2 h-2 mt-2 bg-emerald-500 rounded-full[^"]*"></span>\s*<span>([^<]+)</span>'
    updated = re.sub(pattern, replace_best_for, updated)

    # Replace Not Ideal items (red dots)
    def replace_not_ideal(match):
        original = match.group(1).strip()
        translated = translate_text(original, NOT_IDEAL)
        return f'<span class="w-2 h-2 mt-2 bg-rose-500 rounded-full"></span><span>{translated}</span>'

    pattern = r'<span class="w-2 h-2 mt-2 bg-rose-500 rounded-full[^"]*"></span>\s*<span>([^<]+)</span>'
    updated = re.sub(pattern, replace_not_ideal, updated)

    # Replace temperament tags
    def replace_tags(match):
        original = match.group(1).strip()
        translated = translate_text(original, TEMPERAMENT_TAGS)
        return f'from-sky-100 to-blue-100 text-slate-700 px-4 py-2 rounded-full text-sm font-medium">{translated}</span>'

    pattern = r'from-sky-100 to-blue-100 text-slate-700 px-4 py-2 rounded-full text-sm font-medium">([^<]+)</span>'
    updated = re.sub(pattern, replace_tags, updated)

    return updated


def main():
    breeds = sorted([f.stem for f in NL_BREEDS_DIR.glob("*.html")])
    print(f"Total Dutch breeds: {len(breeds)}")

    translated = 0
    for i, breed in enumerate(breeds):
        nl_path = NL_BREEDS_DIR / f"{breed}.html"
        nl_html = nl_path.read_text()

        updated_html = apply_translations(nl_html)

        if updated_html != nl_html:
            nl_path.write_text(updated_html)
            translated += 1

        if (i + 1) % 50 == 0:
            print(f"  Progress: {i+1}/{len(breeds)}")

    print(f"\nDone! Updated {translated} breed files.")


if __name__ == "__main__":
    main()
