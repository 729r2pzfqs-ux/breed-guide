#!/usr/bin/env python3
"""
Apply all German translations to breed pages.
Translates headings, Best For, Not Ideal For, and temperament tags.
"""

import re
from pathlib import Path

from de_translations import BEST_FOR, NOT_IDEAL, TEMPERAMENT_TAGS

DE_BREEDS_DIR = Path(__file__).parent / "de" / "breeds"


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
    """Apply all translations to German HTML."""
    updated = html

    # Fix "Best For" heading → "Am Besten Für" (if not already)
    updated = re.sub(
        r'(<span class="text-emerald-500">✓</span>\s*)Best For',
        r'\1Am Besten Für',
        updated
    )

    # Fix "Not Ideal For" heading → "Nicht Ideal Für" (if not already)
    updated = re.sub(
        r'(<span class="text-rose-500">✗</span>\s*)Not Ideal For',
        r'\1Nicht Ideal Für',
        updated
    )
    
    # Fix "Our Verdict" → "Unser Fazit" (if not already)
    updated = updated.replace(">Our Verdict:", ">Unser Fazit:")

    # Replace Best For items
    def replace_best_for(match):
        original = match.group(1).strip()
        translated = translate_text(original, BEST_FOR)
        return f'<span class="w-2 h-2 mt-2 bg-emerald-500 rounded-full"></span><span>{translated}</span>'

    pattern = r'<span class="w-2 h-2 mt-2 bg-emerald-500 rounded-full[^"]*"></span>\s*<span>([^<]+)</span>'
    updated = re.sub(pattern, replace_best_for, updated)

    # Replace Not Ideal items
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
    breeds = sorted([f.stem for f in DE_BREEDS_DIR.glob("*.html")])
    print(f"Total German breeds: {len(breeds)}")

    translated = 0
    for i, breed in enumerate(breeds):
        de_path = DE_BREEDS_DIR / f"{breed}.html"
        de_html = de_path.read_text()

        updated_html = apply_translations(de_html)

        if updated_html != de_html:
            de_path.write_text(updated_html)
            translated += 1

        if (i + 1) % 50 == 0:
            print(f"  Progress: {i+1}/{len(breeds)}")

    print(f"\nDone! Updated {translated} breed files.")


if __name__ == "__main__":
    main()
