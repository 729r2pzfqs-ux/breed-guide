#!/usr/bin/env python3
"""Replace emojis with Lucide icons in comparison pages"""

import os
from glob import glob

# Emoji to Lucide icon mapping
REPLACEMENTS = {
    '📏 Size': '<i data-lucide="ruler" class="w-4 h-4 inline mr-1"></i> Size',
    '⏳ Lifespan': '<i data-lucide="clock" class="w-4 h-4 inline mr-1"></i> Lifespan',
    '⚡ Energy Level': '<i data-lucide="zap" class="w-4 h-4 inline mr-1"></i> Energy Level',
    '✂️ Grooming Needs': '<i data-lucide="scissors" class="w-4 h-4 inline mr-1"></i> Grooming Needs',
    '✂️ Grooming Requirements': '<i data-lucide="scissors" class="w-4 h-4 inline mr-1"></i> Grooming Requirements',
    '👶 Kid Friendly': '<i data-lucide="baby" class="w-4 h-4 inline mr-1"></i> Kid Friendly',
    '🏠 Apartment Suitable': '<i data-lucide="home" class="w-4 h-4 inline mr-1"></i> Apartment Suitable',
    '🐕 Shedding': '<i data-lucide="wind" class="w-4 h-4 inline mr-1"></i> Shedding',
    '🧠 ': '<i data-lucide="brain" class="w-5 h-5 inline mr-2"></i> ',
    '🏃 Exercise': '<i data-lucide="activity" class="w-5 h-5 inline mr-2"></i> Exercise',
    '🎯 ': '<i data-lucide="target" class="w-6 h-6 inline mr-2"></i> ',
}

def fix_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    original = content
    for emoji, icon in REPLACEMENTS.items():
        content = content.replace(emoji, icon)
    
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
