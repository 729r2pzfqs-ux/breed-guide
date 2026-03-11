#!/usr/bin/env python3
"""Fix FAQ pages to match breed page template"""

import os
import re
from glob import glob

# Correct header from breed pages
CORRECT_HEADER = '''    <header class="bg-white/80 backdrop-blur-md border-b border-slate-200/60 sticky top-0 z-50">
        <div class="max-w-5xl mx-auto px-4 py-4 flex items-center justify-between">
            <a href="/" class="flex items-center gap-3">
                <img src="/logo-192-green.png" alt="BreedFinder" class="h-10 w-10">
                <span class="text-xl font-bold text-slate-800">BreedFinder</span>
            </a>
            <nav class="flex items-center gap-3 sm:gap-6 text-sm font-medium">
                <a href="/breeds/" class="hidden sm:block text-slate-600 hover:text-emerald-800 transition">Breeds</a>
                <a href="/compare/" class="hidden sm:block text-slate-600 hover:text-emerald-800 transition">Compare</a>
                <a href="/quiz/" class="hidden sm:block text-slate-600 hover:text-emerald-800 transition">Quiz</a>
            </nav>
        </div>
    </header>'''

def fix_faq(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Fix body tag
    content = re.sub(
        r'<body[^>]*>',
        '<body class="bg-gradient-to-b from-slate-50 to-white min-h-screen text-[#2a2518]">',
        content
    )
    
    # Fix header
    content = re.sub(
        r'<header[^>]*>.*?</header>',
        CORRECT_HEADER,
        content,
        flags=re.DOTALL
    )
    
    # Fix main tag  
    content = re.sub(
        r'<main[^>]*>',
        '<main class="max-w-5xl mx-auto px-4 py-8">',
        content
    )
    
    with open(filepath, 'w') as f:
        f.write(content)
    return True

# Fix all FAQ pages
count = 0
for f in glob("**/faq/index.html", recursive=True):
    if fix_faq(f):
        count += 1
        print(f"Fixed {f}")

print(f"\nDone! Fixed {count} FAQ pages")
