#!/usr/bin/env python3
"""
Generate breeds-compare.js from breeds.json for the compare tool
"""

import json
from pathlib import Path

def main():
    base_dir = Path(__file__).parent.parent
    
    # Load breeds
    with open(base_dir / 'data' / 'breeds.json', 'r', encoding='utf-8') as f:
        breeds = json.load(f)
    
    # Build JS array
    js_breeds = []
    for b in breeds:
        slug = b.get('id', b.get('slug', ''))
        size_info = b.get('size', {})
        ratings = b.get('ratings', {})
        characteristics = b.get('characteristics', {})
        
        # Map size category to display string
        size_cat = size_info.get('category', 'medium') if isinstance(size_info, dict) else 'medium'
        size_display = size_cat.capitalize() if size_cat else 'Medium'
        
        js_breed = {
            'name': b['name'],
            'slug': slug,
            'image': f"../../images/heads/{slug}.webp",
            'size': size_display,
            'height': f"{size_info.get('height_cm', 'Unknown')} cm" if isinstance(size_info, dict) else 'Unknown',
            'weight': f"{size_info.get('weight_kg', 'Unknown')} kg" if isinstance(size_info, dict) else 'Unknown',
            'lifespan': b.get('lifespan', 'Unknown'),
            'origin': b.get('origin', 'Unknown'),
            'group': b.get('group', 'Unknown').capitalize(),
            'energy': ratings.get('energy', 3),
            'grooming': ratings.get('grooming', 3),
            'trainability': ratings.get('trainability', 3),
            'shedding': characteristics.get('shedding', 'moderate').capitalize(),
            'kidFriendly': ratings.get('kid_friendly', 3),
            'apartment': ratings.get('apartment_ok', 3),
            'temperament': b.get('temperament', [])
        }
        js_breeds.append(js_breed)
    
    # Write JS file
    js_content = "const breeds = " + json.dumps(js_breeds, indent=2) + ";\n"
    
    with open(base_dir / 'data' / 'breeds-compare.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"✅ Generated breeds-compare.js with {len(breeds)} breeds")

if __name__ == '__main__':
    main()
