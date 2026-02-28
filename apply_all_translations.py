#!/usr/bin/env python3
"""
Apply all Swedish translations to breed pages.
Merges all batches and applies to HTML files.
"""

import re
from pathlib import Path

# Import all translation batches
from translate_all_breeds import TRANSLATIONS
from sv_breeds_batch2 import TRANSLATIONS_BATCH2
from sv_breeds_batch3 import TRANSLATIONS_BATCH3
from sv_breeds_batch4 import TRANSLATIONS_BATCH4
from sv_breeds_batch5 import TRANSLATIONS_BATCH5
from sv_breeds_batch6 import TRANSLATIONS_BATCH6
from sv_breeds_batch7 import TRANSLATIONS_BATCH7
from sv_translations import BEST_FOR, NOT_IDEAL, TEMPERAMENT_TAGS

# Merge all translations
ALL_TRANSLATIONS = {}
ALL_TRANSLATIONS.update(TRANSLATIONS)
ALL_TRANSLATIONS.update(TRANSLATIONS_BATCH2)
ALL_TRANSLATIONS.update(TRANSLATIONS_BATCH3)
ALL_TRANSLATIONS.update(TRANSLATIONS_BATCH4)
ALL_TRANSLATIONS.update(TRANSLATIONS_BATCH5)
ALL_TRANSLATIONS.update(TRANSLATIONS_BATCH6)
ALL_TRANSLATIONS.update(TRANSLATIONS_BATCH7)

SV_BREEDS_DIR = Path(__file__).parent / "sv" / "breeds"

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

def apply_translation(sv_html, breed, translation):
    """Apply translation to Swedish HTML."""
    if not translation:
        return sv_html
    
    updated = sv_html
    
    # Replace meta description
    if 'meta_description' in translation:
        old_pattern = r'<meta name="description" content="[^"]*">'
        new_meta = f'<meta name="description" content="{translation["meta_description"]}">'
        updated = re.sub(old_pattern, new_meta, updated)
    
    # Replace hero description
    if 'hero_desc' in translation:
        pattern = r'(<p class="text-lg text-slate-600 mb-6 leading-relaxed">)[^<]*(</p>)'
        updated = re.sub(pattern, rf'\g<1>{translation["hero_desc"]}\2', updated)
    
    # Replace overview - target the specific section
    if 'overview' in translation:
        pattern = r'(<i data-lucide="book-open"[^>]*></i>\s*Översikt.*?<p class="text-slate-600[^"]*">)[^<]*(</p>)'
        updated = re.sub(pattern, rf'\g<1>{translation["overview"]}\2', updated, flags=re.DOTALL)
    
    # Replace temperament section
    if 'temperament' in translation:
        pattern = r'(<i data-lucide="heart"[^>]*></i>\s*Temperament.*?<p class="text-slate-600[^"]*">)[^<]*(</p>)'
        updated = re.sub(pattern, rf'\g<1>{translation["temperament"]}\2', updated, flags=re.DOTALL)
    
    # Replace health section
    if 'health' in translation:
        pattern = r'(<i data-lucide="heart-pulse"[^>]*></i>\s*Hälsa.*?<p class="text-slate-600[^"]*">)[^<]*(</p>)'
        updated = re.sub(pattern, rf'\g<1>{translation["health"]}\2', updated, flags=re.DOTALL)
    
    # Replace exercise section
    if 'exercise' in translation:
        pattern = r'(<i data-lucide="activity"[^>]*></i>\s*Motion.*?<p class="text-slate-600[^"]*">)[^<]*(</p>)'
        updated = re.sub(pattern, rf'\g<1>{translation["exercise"]}\2', updated, flags=re.DOTALL)
    
    # Replace verdict
    if 'verdict' in translation:
        pattern = r'(<strong>Vårt Omdöme:</strong>\s*)[^<]*(</p>)'
        updated = re.sub(pattern, rf'\g<1>{translation["verdict"]}\2', updated)
    
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
    breeds = sorted([f.stem for f in SV_BREEDS_DIR.glob("*.html")])
    print(f"Total breeds: {len(breeds)}")
    print(f"Total translations available: {len(ALL_TRANSLATIONS)}")
    
    translated = 0
    for i, breed in enumerate(breeds):
        sv_path = SV_BREEDS_DIR / f"{breed}.html"
        sv_html = sv_path.read_text()
        
        translation = ALL_TRANSLATIONS.get(breed, {})
        updated_html = apply_translation(sv_html, breed, translation)
        
        if updated_html != sv_html:
            sv_path.write_text(updated_html)
            translated += 1
            if (i + 1) % 20 == 0:
                print(f"  Progress: {i+1}/{len(breeds)}")
    
    print(f"\nDone! Translated {translated} breeds.")

if __name__ == "__main__":
    main()
