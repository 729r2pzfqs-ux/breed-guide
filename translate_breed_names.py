#!/usr/bin/env python3
"""
Translate breed names in breed pages AND front page for a specific language.
Updates: title, h1, meta descriptions, breadcrumbs, og/twitter tags, hero sections
"""

import json
import os
import re
import sys

def load_translations(lang):
    """Load breed name translations for a language."""
    path = f"data/breed_names_{lang}.json"
    if not os.path.exists(path):
        print(f"❌ Translation file not found: {path}")
        sys.exit(1)
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def translate_front_page(lang, translations, breed_names):
    """Update the front page (index.html) with localized breed names."""
    filepath = f"{lang}/index.html"
    if not os.path.exists(filepath):
        return 0
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = 0
    
    for slug, english_name in breed_names.items():
        local_name = translations.get(slug, english_name)
        if english_name == local_name:
            continue
        
        # Update alt text on breed images
        old_alt = f'alt="{english_name}"'
        new_alt = f'alt="{local_name}"'
        if old_alt in content:
            content = content.replace(old_alt, new_alt)
            changes += 1
        
        # Update breed name in card (font-semibold div after the image)
        # Pattern: after breeds/{slug}.html link, find the font-semibold div
        pattern = rf'(href="breeds/{re.escape(slug)}\.html"[^>]*>.*?<div class="font-semibold[^"]*"[^>]*>){re.escape(english_name)}(</div>)'
        replacement = rf'\g<1>{local_name}\g<2>'
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    return 0

def translate_breed_page(filepath, slug, english_name, local_name):
    """Update a breed page with the localized name."""
    if english_name == local_name:
        return False  # No change needed
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Update <title>
    content = re.sub(
        rf'<title>{re.escape(english_name)} \|',
        f'<title>{local_name} |',
        content
    )
    
    # Update <h1>
    content = re.sub(
        rf'<h1 class="[^"]*">{re.escape(english_name)}</h1>',
        lambda m: m.group(0).replace(english_name, local_name),
        content
    )
    
    # Update meta description (beginning)
    content = re.sub(
        rf'<meta name="description" content="{re.escape(english_name)}s? ',
        f'<meta name="description" content="{local_name} ',
        content
    )
    
    # Update og:title
    content = re.sub(
        rf'<meta property="og:title" content="{re.escape(english_name)} -',
        f'<meta property="og:title" content="{local_name} -',
        content
    )
    
    # Update og:description
    content = re.sub(
        rf'<meta property="og:description" content="Everything you need to know about the {re.escape(english_name)}:',
        f'<meta property="og:description" content="{local_name}:',
        content
    )
    
    # Update twitter:title
    content = re.sub(
        rf'<meta name="twitter:title" content="{re.escape(english_name)} -',
        f'<meta name="twitter:title" content="{local_name} -',
        content
    )
    
    # Update twitter:description
    content = re.sub(
        rf'<meta name="twitter:description" content="Complete guide to the {re.escape(english_name)} breed."',
        f'<meta name="twitter:description" content="{local_name}."',
        content
    )
    
    # Update schema.org headline
    content = re.sub(
        rf'"headline": "{re.escape(english_name)}: Breed Guide',
        f'"headline": "{local_name}:',
        content
    )
    
    # Update schema.org description
    content = re.sub(
        rf'"description": "Complete guide to the {re.escape(english_name)}:',
        f'"description": "{local_name}:',
        content
    )
    
    # Update schema.org name
    content = re.sub(
        rf'"name": "{re.escape(english_name)}"',
        f'"name": "{local_name}"',
        content
    )
    
    # Update breadcrumb (both variants)
    content = re.sub(
        rf'<span class="text-slate-800">{re.escape(english_name)}</span>',
        f'<span class="text-slate-800">{local_name}</span>',
        content
    )
    content = re.sub(
        rf'<span class="text-slate-700 font-medium">{re.escape(english_name)}</span>',
        f'<span class="text-slate-700 font-medium">{local_name}</span>',
        content
    )
    
    # Update image alt text
    content = re.sub(
        rf'alt="{re.escape(english_name)}"',
        f'alt="{local_name}"',
        content
    )
    
    # Update any remaining instances of "the {breed}" pattern
    content = re.sub(
        rf'\bthe {re.escape(english_name)}\b',
        f'the {local_name}',
        content,
        flags=re.IGNORECASE
    )
    
    # Update "The {breed} is" pattern
    content = re.sub(
        rf'\bThe {re.escape(english_name)} is\b',
        f'{local_name} is',
        content
    )
    
    # Update standalone breed name in text (be careful with this one)
    # Only replace in specific contexts like verdict sections
    content = re.sub(
        rf'<strong>Meidän Arvio:</strong> The {re.escape(english_name)} is',
        f'<strong>Meidän Arvio:</strong> {local_name} on',
        content
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python translate_breed_names.py <lang>")
        print("Example: python translate_breed_names.py sv")
        sys.exit(1)
    
    lang = sys.argv[1]
    
    # Load translations
    translations = load_translations(lang)
    print(f"Loaded {len(translations)} breed name translations for {lang}")
    
    # Load English breed names
    with open('data/breeds.json', 'r', encoding='utf-8') as f:
        breeds = json.load(f)
    
    breed_names = {b['id']: b['name'] for b in breeds}
    
    # Process each breed page
    breeds_dir = f"{lang}/breeds"
    if not os.path.exists(breeds_dir):
        print(f"❌ Breeds directory not found: {breeds_dir}")
        sys.exit(1)
    
    updated = 0
    skipped = 0
    
    for filename in sorted(os.listdir(breeds_dir)):
        if not filename.endswith('.html'):
            continue
        
        slug = filename[:-5]  # Remove .html
        
        if slug not in breed_names:
            print(f"  ⚠️  Unknown breed: {slug}")
            continue
        
        english_name = breed_names[slug]
        local_name = translations.get(slug, english_name)
        
        filepath = os.path.join(breeds_dir, filename)
        
        if translate_breed_page(filepath, slug, english_name, local_name):
            if english_name != local_name:
                print(f"  ✓ {english_name} → {local_name}")
            updated += 1
        else:
            skipped += 1
    
    print(f"\n✅ Breed pages - Updated: {updated} | Skipped: {skipped}")
    
    # Also update front page
    front_changes = translate_front_page(lang, translations, breed_names)
    if front_changes > 0:
        print(f"✅ Front page - Updated {front_changes} breed names")

if __name__ == "__main__":
    main()
