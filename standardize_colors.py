#!/usr/bin/env python3
"""Standardize comparison page cards to green/yellow"""

import os
import re
from glob import glob

def fix_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    original = content
    
    # Find breed card sections and standardize colors
    # First card (breed 1) should be forest green
    # Second card (breed 2) should be yellow/amber
    
    # Pattern for first breed card gradient
    first_card_patterns = [
        r'from-rose-500 to-rose-600',
        r'from-sky-600 to-sky-700',
        r'from-emerald-600 to-emerald-700',
        r'from-teal-600 to-teal-700',
        r'from-blue-600 to-blue-700',
        r'from-purple-500 to-purple-600',
    ]
    
    second_card_patterns = [
        r'from-slate-700 to-slate-800',
        r'from-slate-600 to-slate-700',
        r'from-amber-500 to-amber-600',
        r'from-orange-500 to-orange-600',
        r'from-rose-500 to-rose-600',  # When used as second
    ]
    
    # Find the two breed card divs
    card_pattern = r'(<div class="bg-gradient-to-r )(from-[a-z]+-\d+ to-[a-z]+-\d+)( p-6 text-white text-center">)'
    
    matches = list(re.finditer(card_pattern, content))
    
    if len(matches) >= 2:
        # Replace first card color with forest
        first_match = matches[0]
        content = content[:first_match.start(2)] + 'from-forest to-forest' + content[first_match.end(2):]
        
        # Recalculate second match position after first replacement
        offset = len('from-forest to-forest') - len(first_match.group(2))
        
        # Find second match again
        matches = list(re.finditer(card_pattern, content))
        if len(matches) >= 2:
            second_match = matches[1]
            content = content[:second_match.start(2)] + 'from-yellow-500 to-yellow-600' + content[second_match.end(2):]
    
    # Also fix the subtitle text colors
    content = re.sub(r'<p class="text-rose-100">', '<p class="text-white/80">', content)
    content = re.sub(r'<p class="text-slate-600">([^<]+)</p>\s*</div>\s*<div class="p-6">', '<p class="text-yellow-100">\\1</p>\n                </div>\n                <div class="p-6">', content)
    content = re.sub(r'<p class="text-[a-z]+-100">', '<p class="text-white/80">', content)
    
    # Fix h1 span colors for consistency
    content = re.sub(r'<span class="bg-gradient-to-r from-rose-500 to-rose-600 bg-clip-text text-transparent">', '<span class="text-forest">', content)
    content = re.sub(r'<span class="bg-gradient-to-r from-[a-z]+-\d+ to-[a-z]+-\d+ bg-clip-text text-transparent">([^<]+)</span>\s*<span class="text-slate-600 mx-4">vs</span>', '<span class="text-forest">\\1</span>\n                <span class="text-slate-600 mx-4">vs</span>', content)
    
    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    return False

count = 0
for f in glob("**/compare/comparisons/*/index.html", recursive=True):
    if fix_file(f):
        count += 1
        print(f"Fixed {os.path.dirname(f).split('comparisons/')[-1]}")

print(f"\n✅ Updated {count} comparison pages")
