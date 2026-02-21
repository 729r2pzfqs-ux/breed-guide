#!/usr/bin/env python3
"""
Translate all breed page content for all 14 languages
"""

import re
from pathlib import Path
from breed_translations import TRAITS, BEST_FOR, NOT_IDEAL, YEARS, translate_trait

LANGUAGES = ['es', 'de', 'fr', 'it', 'pt', 'nl', 'pl', 'zh', 'ja', 'fi', 'sv', 'no', 'da', 'ru']

def translate_breed_page(content, lang):
    """Translate content in a breed page"""
    
    # Translate temperament traits in pills
    def translate_trait_match(match):
        trait = match.group(1)
        translated = translate_trait(trait, lang)
        return f'rounded-full text-sm font-medium">{translated}</span>'
    
    content = re.sub(
        r'rounded-full text-sm font-medium">([^<]+)</span>',
        translate_trait_match,
        content
    )
    
    # Translate "years" in lifespan
    if lang in YEARS:
        content = re.sub(r'(\d+-\d+)\s*years', rf'\1 {YEARS[lang]}', content)
        content = re.sub(r'(\d+)\s*years', rf'\1 {YEARS[lang]}', content)
    
    # Translate Best For items
    for eng, translations in BEST_FOR.items():
        if lang in translations:
            content = content.replace(f'<span>{eng}</span>', f'<span>{translations[lang]}</span>')
    
    # Translate Not Ideal items
    for eng, translations in NOT_IDEAL.items():
        if lang in translations:
            content = content.replace(f'<span>{eng}</span>', f'<span>{translations[lang]}</span>')
    
    return content


def main():
    base_dir = Path(__file__).parent.parent
    
    print("Translating breed pages...")
    count = 0
    
    for lang in LANGUAGES:
        breeds_dir = base_dir / lang / 'breeds'
        if not breeds_dir.exists():
            print(f"  Skipping {lang} - no breeds directory")
            continue
        
        for breed_file in breeds_dir.glob('*.html'):
            content = breed_file.read_text(encoding='utf-8')
            translated = translate_breed_page(content, lang)
            breed_file.write_text(translated, encoding='utf-8')
            count += 1
        
        print(f"  Translated {lang}/breeds/ ({len(list(breeds_dir.glob('*.html')))} files)")
    
    print(f"\n✅ Done! Translated {count} breed pages")


if __name__ == '__main__':
    main()
