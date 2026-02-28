#!/usr/bin/env python3
"""
Apply all Spanish translations to breed pages.
Fixes mixed English/Spanish phrases and remaining English text.
"""

import re
from pathlib import Path

from es_translations import BEST_FOR, NOT_IDEAL, TEMPERAMENT_TAGS

ES_BREEDS_DIR = Path(__file__).parent / "es" / "breeds"


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
    """Apply all translations to Spanish HTML."""
    updated = html

    # Fix "Best For" heading → "Ideal Para" (if still in English)
    updated = re.sub(
        r'(<span class="text-emerald-500">✓</span>\s*)Best For',
        r'\1Ideal Para',
        updated
    )

    # Fix "Not Ideal For" → "No Ideal Para" (if still in English)
    updated = re.sub(
        r'(<span class="text-rose-500">✗</span>\s*)Not Ideal For',
        r'\1No Ideal Para',
        updated
    )

    # Fix "Our Verdict" → "Nuestro Veredicto" (if still in English)
    updated = updated.replace("<strong>Our Verdict:</strong>", "<strong>Nuestro Veredicto:</strong>")

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
    breeds = sorted([f.stem for f in ES_BREEDS_DIR.glob("*.html")])
    print(f"Total Spanish breeds: {len(breeds)}")

    translated = 0
    for i, breed in enumerate(breeds):
        es_path = ES_BREEDS_DIR / f"{breed}.html"
        es_html = es_path.read_text()

        updated_html = apply_translations(es_html)

        if updated_html != es_html:
            es_path.write_text(updated_html)
            translated += 1

        if (i + 1) % 50 == 0:
            print(f"  Progress: {i+1}/{len(breeds)}")

    print(f"\nDone! Updated {translated} breed files.")


if __name__ == "__main__":
    main()
