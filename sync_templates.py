#!/usr/bin/env python3
"""Sync header/styling across all pages to match breed page template"""

import os
import re
from glob import glob

# The correct header from breed pages
CORRECT_HEADER = '''        <header class="bg-white/80 backdrop-blur-md border-b border-slate-200/60 sticky top-0 z-50">
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

CORRECT_FONTS = '''    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,400;1,9..144,600&family=Inter:wght@400;500;600;700" rel="stylesheet">'''

def update_header(content):
    """Replace header section with correct template"""
    # Match header tag including all content until closing tag
    header_pattern = r'<header[^>]*>.*?</header>'
    return re.sub(header_pattern, CORRECT_HEADER.strip(), content, flags=re.DOTALL)

def update_fonts(content):
    """Ensure correct Google Fonts are used"""
    # Remove any Plus Jakarta Sans references
    content = re.sub(r"<link[^>]*Plus\+Jakarta[^>]*>", "", content)
    
    # Check if correct fonts exist
    if "Fraunces" not in content:
        # Add fonts before </head>
        content = content.replace("</head>", CORRECT_FONTS + "\n</head>")
    
    return content

def update_body_font(content):
    """Update body font to Inter"""
    # Replace Plus Jakarta Sans with Inter
    content = re.sub(r"font-family:\s*'Plus Jakarta Sans'", "font-family: 'Inter'", content)
    return content

def process_file(filepath):
    """Process a single file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    content = update_header(content)
    content = update_fonts(content)
    content = update_body_font(content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Process comparison pages
print("Updating comparison pages...")
count = 0
for f in glob("**/compare/comparisons/*/index.html", recursive=True):
    if process_file(f):
        count += 1
print(f"  Updated {count} comparison pages")

# Process article pages
print("Updating article pages...")
count = 0
for f in glob("**/articles/*/index.html", recursive=True):
    if "comparisons" not in f:
        if process_file(f):
            count += 1
print(f"  Updated {count} article pages")

print("Done!")
