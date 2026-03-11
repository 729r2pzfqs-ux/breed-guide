#!/usr/bin/env python3
"""Remove duplicate Breed Ratings/Temperament sections"""

import os
import re
from glob import glob

def fix_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Count Breed Ratings occurrences
    if content.count('Breed Ratings') <= 1:
        return False
    
    # Find the pattern: <!-- Verdict --><!-- Ratings --> indicates duplicate starts
    # Remove content from second <!-- Ratings --> to second <!-- Verdict -->
    
    # Split by markers
    parts = re.split(r'(<!-- Ratings -->|<!-- Temperament -->|<!-- Verdict -->)', content)
    
    # Find indices
    markers = []
    for i, part in enumerate(parts):
        if part.startswith('<!--'):
            markers.append((i, part.strip()))
    
    # Find duplicate pattern: Verdict, Ratings (duplicate), Temperament (duplicate), Verdict
    # We want to remove: second Ratings through content before second Verdict
    
    ratings_indices = [i for i, m in markers if m == '<!-- Ratings -->']
    verdict_indices = [i for i, m in markers if m == '<!-- Verdict -->']
    
    if len(ratings_indices) < 2 or len(verdict_indices) < 2:
        return False
    
    # Remove from second Ratings marker to just before second Verdict marker
    second_ratings = ratings_indices[1]
    second_verdict = verdict_indices[1]
    
    new_parts = parts[:second_ratings] + parts[second_verdict:]
    new_content = ''.join(new_parts)
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    
    return True

count = 0
for f in glob("breeds/*/index.html"):
    if fix_file(f):
        count += 1
        print(f"Fixed {os.path.basename(os.path.dirname(f))}")

print(f"\n✅ Fixed {count} pages")
