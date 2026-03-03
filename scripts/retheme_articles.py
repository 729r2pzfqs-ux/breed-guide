#!/usr/bin/env python3
"""Retheme article pages to forest green theme."""

import os
import re
import sys

def retheme_article(html):
    """Apply forest green theme to article HTML."""
    
    # Replace font imports
    html = re.sub(
        r'<link href="https://fonts\.googleapis\.com/css2\?family=Plus\+Jakarta\+Sans[^"]*" rel="stylesheet">',
        '<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@400;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">',
        html
    )
    
    # Replace font family style
    html = re.sub(
        r"\* \{ font-family: 'Plus Jakarta Sans', sans-serif; \}",
        "body { font-family: 'Inter', sans-serif; }\n        .font-serif { font-family: 'Fraunces', serif; }",
        html
    )
    
    # Replace prose styles
    old_prose = r'\.prose h2 \{ font-size: 1\.5rem; font-weight: 700; margin-top: 2rem; margin-bottom: 1rem; color: #0f172a; \}'
    new_prose = '.prose h2 { font-size: 1.5rem; font-weight: 700; margin-top: 2rem; margin-bottom: 1rem; color: #1a2e1a; font-family: "Fraunces", serif; }'
    html = re.sub(old_prose, new_prose, html)
    
    html = re.sub(r'\.prose h3 \{[^}]+\}', '.prose h3 { font-size: 1.25rem; font-weight: 600; margin-top: 1.5rem; margin-bottom: 0.5rem; color: #2a3f2a; font-family: "Fraunces", serif; }', html)
    html = re.sub(r'\.prose p \{[^}]+\}', '.prose p { margin-bottom: 1rem; color: #5c5647; line-height: 1.8; }', html)
    html = re.sub(r'\.prose ul \{[^}]+\}', '.prose ul { margin-left: 1.5rem; margin-bottom: 1rem; list-style: disc; color: #5c5647; }', html)
    
    # Add card-shadow style if not present
    if 'card-shadow' not in html:
        html = html.replace('</style>', '        .card-shadow { box-shadow: 0 2px 12px rgba(42, 37, 24, 0.08); }\n    </style>')
    
    # Replace body class
    html = re.sub(
        r'<body class="bg-slate-50 text-slate-900">',
        '<body class="min-h-screen" style="background: linear-gradient(135deg, #f6f7f2 0%, #faf9f6 50%, #eef1e8 100%); color: #2a2518;">',
        html
    )
    
    # Replace header
    old_header = r'<header class="bg-white border-b border-slate-200 py-4 px-4">'
    new_header = '<header class="bg-white/80 backdrop-blur-md border-b sticky top-0 z-50" style="border-color: #f0ede6;">'
    html = re.sub(old_header, new_header, html)
    
    # Replace logo references
    html = re.sub(r'logo-192\.png" class="w-10 h-10 rounded-xl"', 'logo-192-green.png" class="w-10 h-10"', html)
    html = re.sub(r'logo-192\.png" class="w-8 h-8"', 'logo-192-green.png" class="w-8 h-8"', html)
    
    # Replace header brand text
    html = re.sub(
        r'<span class="text-xl font-bold">BreedFinder</span>',
        '<span class="text-xl font-bold font-serif" style="color: #1a5632;">BreedFinder</span>',
        html
    )
    
    # Replace back link
    html = re.sub(
        r'<a href="\.\./\.\./?" class="text-slate-600 hover:text-slate-900 text-sm">← Back</a>',
        '<a href="../../" class="text-sm transition" style="color: #5c5647;" onmouseover="this.style.color=\'#1a5632\'" onmouseout="this.style.color=\'#5c5647\'">← Back</a>',
        html
    )
    
    # Replace GUIDE badge colors
    html = re.sub(r'text-sky-700 font-medium', 'font-semibold" style="color: #1a5632;', html)
    html = re.sub(r'class="text-sky-700', 'style="color: #1a5632;" class="', html)
    
    # Replace title colors
    html = re.sub(
        r'<h1 class="text-3xl md:text-4xl font-bold mt-2 mb-4">',
        '<h1 class="text-3xl md:text-4xl font-bold font-serif mt-2 mb-4" style="color: #1a2e1a;">',
        html
    )
    
    # Replace subtitle colors
    html = re.sub(r'<p class="text-slate-600 text-lg">', '<p class="text-lg" style="color: #5c5647;">', html)
    
    # Replace callout boxes (sky to forest)
    html = re.sub(r'bg-sky-50 border-l-4 border-sky-500', 'border-l-4 rounded-r-xl" style="background: #eef1e8; border-color: #1a5632;', html)
    html = re.sub(r'text-sky-900', '" style="color: #1a2e1a;', html)
    
    # Replace emerald callout boxes
    html = re.sub(r'bg-emerald-50 border-l-4 border-emerald-500', 'border-l-4 rounded-r-xl" style="background: #e8f0e8; border-color: #2d6a4f;', html)
    html = re.sub(r'text-emerald-900', '" style="color: #1a3a2a;', html)
    
    # Replace rose/amber callout boxes
    html = re.sub(r'bg-rose-50 border-l-4 border-rose-400', 'border-l-4 rounded-r-xl" style="background: #f5ece8; border-color: #8b5a3c;', html)
    html = re.sub(r'text-rose-900', '" style="color: #5c3a2a;', html)
    html = re.sub(r'bg-amber-50 border-l-4 border-amber-500', 'border-l-4 rounded-r-xl" style="background: #f5f0e5; border-color: #8b6914;', html)
    html = re.sub(r'text-amber-900', '" style="color: #5c4a14;', html)
    
    # Replace breed cards
    html = re.sub(r'bg-white rounded-2xl p-5 shadow-sm hover:shadow-md', 'bg-white rounded-2xl p-5 card-shadow border" style="border-color: #f0ede6;', html)
    
    # Replace CTA buttons
    html = re.sub(
        r'bg-slate-900 hover:bg-slate-800 text-white',
        'text-white" style="background: #1a5632;" onmouseover="this.style.background=\'#143d25\'" onmouseout="this.style.background=\'#1a5632\'',
        html
    )
    
    # Replace footer
    html = re.sub(
        r'<footer class="bg-slate-900 text-white py-8 px-4[^>]*>',
        '<footer class="py-10 px-4 mt-12" style="background: #1a2e1a;">',
        html
    )
    html = re.sub(r'text-slate-600 text-sm', 'text-sm" style="color: #a8a090;', html)
    
    # Replace favicon
    html = re.sub(r'favicon\.svg" type="image/svg\+xml"', 'favicon.ico" type="image/x-icon"', html)
    
    return html


def process_directory(input_dir):
    """Process all article directories."""
    count = 0
    for item in os.listdir(input_dir):
        item_path = os.path.join(input_dir, item)
        if os.path.isdir(item_path):
            index_file = os.path.join(item_path, 'index.html')
            if os.path.exists(index_file):
                with open(index_file, 'r', encoding='utf-8') as f:
                    html = f.read()
                
                new_html = retheme_article(html)
                
                with open(index_file, 'w', encoding='utf-8') as f:
                    f.write(new_html)
                
                print(f"  [updated] {item}/index.html")
                count += 1
    
    return count


if __name__ == '__main__':
    articles_dir = sys.argv[1] if len(sys.argv) > 1 else 'articles'
    
    if not os.path.exists(articles_dir):
        print(f"Directory not found: {articles_dir}")
        sys.exit(1)
    
    print(f"Rethemimg articles in {articles_dir}...")
    count = process_directory(articles_dir)
    print(f"Done. {count} article(s) updated.")
