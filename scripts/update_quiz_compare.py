#!/usr/bin/env python3
"""Update quiz and compare pages with all breeds data"""

import json
import os
import re

# Load all breeds
with open(os.path.expanduser('~/clawd/dog-breed-guide/data/breeds.json')) as f:
    all_breeds = json.load(f)

def generate_tags(breed):
    """Generate quiz tags for a breed based on its data"""
    tags = []
    r = breed.get('ratings', {})
    
    # Energy level
    energy = r.get('energy', 3)
    if energy >= 4: tags.append('high-energy')
    elif energy <= 2: tags.append('low-energy')
    else: tags.append('moderate-energy')
    
    # Size
    size_cat = breed.get('size', {}).get('category', 'medium')
    if size_cat in ['tiny', 'small']: tags.append('small')
    elif size_cat == 'medium': tags.append('medium')
    elif size_cat in ['large', 'giant']: tags.append('large')
    
    # Kid friendly
    if r.get('kid_friendly', 3) >= 4: tags.append('family-friendly')
    
    # Apartment ok
    if r.get('apartment_ok', 3) >= 4: tags.append('apartment')
    
    # Trainability
    if r.get('trainability', 3) >= 4: tags.append('trainable')
    
    # Grooming
    grooming = r.get('grooming', 3)
    if grooming >= 4: tags.append('high-grooming')
    elif grooming <= 2: tags.append('low-grooming')
    
    # Add temperament tags
    temps = breed.get('temperament', [])[:3]
    for t in temps:
        tags.append(t.lower())
    
    return tags

def generate_quiz_data(breeds):
    """Generate quiz breed entries"""
    entries = []
    for b in breeds:
        tags = generate_tags(b)
        entry = f'            {{ name: "{b["name"]}", slug: "{b["id"]}", tags: {json.dumps(tags)} }}'
        entries.append(entry)
    return ',\n'.join(entries)

def generate_compare_data(breeds):
    """Generate compare breed entries"""
    entries = []
    for b in breeds:
        r = b.get('ratings', {})
        s = b.get('size', {})
        chars = b.get('characteristics', {})
        
        entry = f'''            {{
                name: "{b["name"]}",
                slug: "{b["id"]}",
                image: "../images/heads/{b["id"]}.webp",
                size: "{s.get('category', 'medium').capitalize()}",
                height: "{s.get('height_cm', 'N/A')} cm",
                weight: "{s.get('weight_kg', 'N/A')} kg",
                lifespan: "{b.get('lifespan', 'N/A')}",
                origin: "{b.get('origin', 'Unknown')}",
                group: "{b.get('group', 'unknown').replace('_', ' ').title()}",
                energy: {r.get('energy', 3)},
                grooming: {r.get('grooming', 3)},
                trainability: {r.get('trainability', 3)},
                shedding: "{chars.get('shedding', 'moderate').capitalize()}",
                kidFriendly: {r.get('kid_friendly', 3)},
                apartment: {r.get('apartment_ok', 3)},
                temperament: {json.dumps(b.get('temperament', [])[:4])}
            }}'''
        entries.append(entry)
    return ',\n'.join(entries)

# Update quiz
quiz_path = os.path.expanduser('~/clawd/dog-breed-guide/quiz/index.html')
with open(quiz_path) as f:
    quiz_html = f.read()

# Replace breeds array in quiz
quiz_data = generate_quiz_data(all_breeds)
quiz_html = re.sub(
    r'const breeds = \[[\s\S]*?\];',
    f'const breeds = [\n{quiz_data}\n        ];',
    quiz_html
)
with open(quiz_path, 'w') as f:
    f.write(quiz_html)
print(f"Updated quiz with {len(all_breeds)} breeds")

# Update compare
compare_path = os.path.expanduser('~/clawd/dog-breed-guide/compare/index.html')
with open(compare_path) as f:
    compare_html = f.read()

# Replace breeds array in compare
compare_data = generate_compare_data(all_breeds)
compare_html = re.sub(
    r'const breeds = \[[\s\S]*?\];',
    f'const breeds = [\n{compare_data}\n        ];',
    compare_html
)
with open(compare_path, 'w') as f:
    f.write(compare_html)
print(f"Updated compare with {len(all_breeds)} breeds")
