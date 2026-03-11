#!/usr/bin/env python3
"""Update all comparison pages with the new visual template"""

import os
import re
from glob import glob

# Color pairs for breed cards
COLORS = [
    ('from-forest to-forest', 'from-amber-500 to-amber-600', 'text-white/80', 'text-amber-100'),
    ('from-emerald-600 to-emerald-700', 'from-rose-500 to-rose-600', 'text-emerald-100', 'text-rose-100'),
    ('from-sky-600 to-sky-700', 'from-purple-500 to-purple-600', 'text-sky-100', 'text-purple-100'),
    ('from-teal-600 to-teal-700', 'from-orange-500 to-orange-600', 'text-teal-100', 'text-orange-100'),
]

def slug_to_name(slug):
    """Convert slug to display name"""
    return slug.replace('-', ' ').title()

def get_breed_cards_html(breed1_slug, breed2_slug, breed1_name, breed2_name):
    """Generate breed cards HTML"""
    colors = COLORS[hash(breed1_slug) % len(COLORS)]
    
    return f'''<!-- Breed Cards -->
        <div class="grid md:grid-cols-2 gap-8 mb-12">
            <!-- {breed1_name} -->
            <div class="bg-white rounded-3xl shadow-xl shadow-slate-200/50 overflow-hidden">
                <div class="bg-gradient-to-r {colors[0]} p-6 text-white text-center">
                    <img src="/images/heads/{breed1_slug}.webp" alt="{breed1_name}" class="w-32 h-32 rounded-full mx-auto mb-4 object-cover border-4 border-white/30" onerror="this.src='/images/breeds/{breed1_slug}.webp'">
                    <h2 class="text-2xl font-bold">{breed1_name}</h2>
                </div>
                <div class="p-6">
                    <a href="/breeds/{breed1_slug}/" class="text-forest font-semibold hover:text-forest">View full profile →</a>
                </div>
            </div>

            <!-- {breed2_name} -->
            <div class="bg-white rounded-3xl shadow-xl shadow-slate-200/50 overflow-hidden">
                <div class="bg-gradient-to-r {colors[1]} p-6 text-white text-center">
                    <img src="/images/heads/{breed2_slug}.webp" alt="{breed2_name}" class="w-32 h-32 rounded-full mx-auto mb-4 object-cover border-4 border-white/30" onerror="this.src='/images/breeds/{breed2_slug}.webp'">
                    <h2 class="text-2xl font-bold">{breed2_name}</h2>
                </div>
                <div class="p-6">
                    <a href="/breeds/{breed2_slug}/" class="text-forest font-semibold hover:text-forest">View full profile →</a>
                </div>
            </div>
        </div>

        '''

def update_comparison(filepath):
    """Update a single comparison page"""
    # Extract breed names from path
    dirname = os.path.basename(os.path.dirname(filepath))
    if '-vs-' not in dirname:
        return False
    
    parts = dirname.split('-vs-')
    if len(parts) != 2:
        return False
    
    breed1_slug, breed2_slug = parts
    breed1_name = slug_to_name(breed1_slug)
    breed2_name = slug_to_name(breed2_slug)
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Check if already has breed cards
    if 'rounded-3xl shadow-xl' in content and 'w-32 h-32 rounded-full' in content:
        return False  # Already updated
    
    # Find where to insert breed cards (after the header h1 section, before comparison table)
    # Look for the main content area after the page header
    
    # Find the closing of the header/intro section and the start of comparison content
    header_pattern = r'(<p class="text-lg text-slate-600 max-w-2xl mx-auto">.*?</p>\s*</div>)'
    match = re.search(header_pattern, content, re.DOTALL)
    
    if match:
        insert_point = match.end()
        breed_cards = get_breed_cards_html(breed1_slug, breed2_slug, breed1_name, breed2_name)
        
        # Insert breed cards
        new_content = content[:insert_point] + '\n\n        ' + breed_cards + content[insert_point:]
        
        with open(filepath, 'w') as f:
            f.write(new_content)
        return True
    
    return False

# Process all comparison pages
count = 0
for f in glob("**/compare/comparisons/*/index.html", recursive=True):
    if 'labrador-vs-golden' in f:
        continue  # Skip the template source
    if update_comparison(f):
        count += 1
        print(f"Updated {os.path.dirname(f).split('/')[-1]}")

print(f"\n✅ Updated {count} comparison pages")
