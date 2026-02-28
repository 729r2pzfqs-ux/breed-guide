#!/usr/bin/env python3
"""
Clean up truncated English text in Russian breed pages.
"""

import re
from pathlib import Path

RU_BREEDS_DIR = Path(__file__).parent / "ru" / "breeds"

# Pattern to match truncated English at end of Russian sentences
# Matches: .xx xxx xxx. or .xx xxx. (English fragments after Russian period)
TRUNCATION_PATTERN = re.compile(r'\.([a-z][a-z\s\-]+\.)', re.IGNORECASE)

# Also match mixed Russian ending with English
MIXED_PATTERN = re.compile(r'([а-яА-ЯёЁ]+)\.[a-z][a-z\s\-\']+\.')

def clean_truncations(text):
    """Remove truncated English fragments from Russian text."""
    # Remove patterns like "компаньоны.ly компаньонs."
    text = re.sub(r'([а-яА-ЯёЁ])\.ly [a-zA-Zа-яА-Я]+\.', r'\1.', text)
    text = re.sub(r'([а-яА-ЯёЁ])\.ng [a-zA-Zа-яА-Я ]+\.', r'\1.', text)
    text = re.sub(r'([а-яА-ЯёЁ])\.ke [a-zA-Zа-яА-Я ]+\.', r'\1.', text)
    text = re.sub(r'([а-яА-ЯёЁ])\.ed [a-zA-Zа-яА-Я ]+\.', r'\1.', text)
    text = re.sub(r'([а-яА-ЯёЁ])\.er [a-zA-Zа-яА-Я ]+\.', r'\1.', text)
    text = re.sub(r'([а-яА-ЯёЁ])\.ve [a-zA-Zа-яА-Я ]+\.', r'\1.', text)
    text = re.sub(r'([а-яА-ЯёЁ])\.th [a-zA-Zа-яА-Я ]+\.', r'\1.', text)
    text = re.sub(r'([а-яА-ЯёЁ])\.rs\.?', r'\1.', text)
    text = re.sub(r'([а-яА-ЯёЁ])\.ns\.?', r'\1.', text)
    text = re.sub(r'([а-яА-ЯёЁ])\.ty\.?', r'\1.', text)
    text = re.sub(r'([а-яА-ЯёЁ])\.ce\.?', r'\1.', text)
    text = re.sub(r'([а-яА-ЯёЁ])\.es\.?', r'\1.', text)
    text = re.sub(r'([а-яА-ЯёЁ])\.on\.?', r'\1.', text)
    
    # General pattern for any .xx xxx. at end of Russian text
    text = re.sub(r'([а-яА-ЯёЁ])\.[a-z][a-z\s\-\']{2,30}\.', r'\1.', text)
    
    return text

def main():
    breeds = sorted([f for f in RU_BREEDS_DIR.glob("*.html")])
    print(f"Processing {len(breeds)} Russian breed pages...")
    
    fixed = 0
    changes = []
    
    for breed_path in breeds:
        html = breed_path.read_text()
        cleaned = clean_truncations(html)
        
        if cleaned != html:
            breed_path.write_text(cleaned)
            fixed += 1
            changes.append(breed_path.stem)
    
    print(f"\nFixed {fixed} files with truncation issues.")
    if changes:
        print(f"Changed: {', '.join(changes[:30])}" + ("..." if len(changes) > 30 else ""))

if __name__ == "__main__":
    main()
