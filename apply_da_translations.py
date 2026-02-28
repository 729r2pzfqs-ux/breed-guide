#!/usr/bin/env python3
"""
Apply all Danish translations to breed pages.
"""

import re
from pathlib import Path
from da_translations import BEST_FOR, NOT_IDEAL, TEMPERAMENT_TAGS

DA_BREEDS_DIR = Path(__file__).parent / "da" / "breeds"

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

def apply_translation(html_content):
    """Apply translations to Danish HTML."""
    updated = html_content
    
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
    breeds = sorted([f for f in DA_BREEDS_DIR.glob("*.html")])
    print(f"Total breeds: {len(breeds)}")
    
    translated = 0
    changes = []
    
    for i, breed_path in enumerate(breeds):
        html = breed_path.read_text()
        updated_html = apply_translation(html)
        
        if updated_html != html:
            breed_path.write_text(updated_html)
            translated += 1
            changes.append(breed_path.stem)
            
        if (i + 1) % 50 == 0:
            print(f"  Progress: {i+1}/{len(breeds)}")
    
    print(f"\nDone! Updated {translated} breeds.")
    if changes:
        print(f"Changed files: {', '.join(changes[:20])}" + ("..." if len(changes) > 20 else ""))

if __name__ == "__main__":
    main()
