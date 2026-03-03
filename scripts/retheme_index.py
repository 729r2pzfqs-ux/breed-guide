#!/usr/bin/env python3
"""Retheme localized index.html pages to forest green theme."""

import os
import re
import sys

def retheme_index(html):
    """Apply forest green theme to index HTML."""
    
    # Replace font imports
    html = re.sub(
        r'<link href="https://fonts\.googleapis\.com/css2\?family=Plus\+Jakarta\+Sans[^"]*" rel="stylesheet">',
        '<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@400;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">',
        html
    )
    
    # Replace font-family in style blocks
    html = re.sub(
        r"\* \{ font-family: 'Plus Jakarta Sans', sans-serif; \}",
        "body { font-family: 'Inter', sans-serif; }\n        .font-serif { font-family: 'Fraunces', serif; }",
        html
    )
    
    # Add card-shadow style if not present
    if 'card-shadow {' not in html and '</style>' in html:
        html = html.replace('</style>', '''        .card-shadow { box-shadow: 0 2px 12px rgba(42, 37, 24, 0.08); }
        .card-shadow:hover { box-shadow: 0 4px 20px rgba(42, 37, 24, 0.12); }
    </style>''')
    
    # Replace body class/style
    html = re.sub(
        r'<body class="[^"]*bg-gradient-to-br from-blue-50 via-white to-sky-50[^"]*">',
        '<body class="min-h-screen" style="background: linear-gradient(135deg, #f6f7f2 0%, #faf9f6 50%, #eef1e8 100%); color: #2a2518;">',
        html
    )
    html = re.sub(
        r'<body class="bg-slate-50[^"]*">',
        '<body class="min-h-screen" style="background: linear-gradient(135deg, #f6f7f2 0%, #faf9f6 50%, #eef1e8 100%); color: #2a2518;">',
        html
    )
    
    # Replace header
    html = re.sub(
        r'<header class="bg-white/80 backdrop-blur-md border-b border-slate-200[^"]*">',
        '<header class="bg-white/80 backdrop-blur-md border-b sticky top-0 z-50" style="border-color: #f0ede6;">',
        html
    )
    html = re.sub(
        r'<header class="bg-white border-b border-slate-200[^"]*">',
        '<header class="bg-white/80 backdrop-blur-md border-b sticky top-0 z-50" style="border-color: #f0ede6;">',
        html
    )
    
    # Replace logo - various patterns
    html = re.sub(r'src="\.\./logo-192\.png"', 'src="../logo-192-green.png"', html)
    html = re.sub(r'src="logo-192\.png"', 'src="logo-192-green.png"', html)
    html = re.sub(r'class="w-10 h-10 rounded-xl"', 'class="w-10 h-10"', html)
    html = re.sub(r'class="h-8 w-8"', 'class="w-10 h-10"', html)
    
    # Replace brand text styling
    html = re.sub(
        r'<span class="text-xl font-bold">BreedFinder</span>',
        '<span class="text-xl font-bold font-serif" style="color: #1a5632;">BreedFinder</span>',
        html
    )
    html = re.sub(
        r'<span class="text-xl font-bold text-slate-900">BreedFinder</span>',
        '<span class="text-xl font-bold font-serif" style="color: #1a5632;">BreedFinder</span>',
        html
    )
    
    # Replace nav link colors
    html = re.sub(
        r'class="text-slate-600 hover:text-slate-900([^"]*)"',
        r'class="transition\1" style="color: #5c5647;" onmouseover="this.style.color=\'#1a5632\'" onmouseout="this.style.color=\'#5c5647\'"',
        html
    )
    
    # Replace blue/sky buttons with forest green
    html = re.sub(
        r'bg-blue-600 hover:bg-blue-700',
        '" style="background: #1a5632;" onmouseover="this.style.background=\'#143d25\'" onmouseout="this.style.background=\'#1a5632\'',
        html
    )
    html = re.sub(
        r'bg-sky-600 hover:bg-sky-700',
        '" style="background: #1a5632;" onmouseover="this.style.background=\'#143d25\'" onmouseout="this.style.background=\'#1a5632\'',
        html
    )
    
    # Replace text colors
    html = re.sub(r'text-blue-600', 'style="color: #1a5632;"', html)
    html = re.sub(r'text-sky-600', 'style="color: #1a5632;"', html)
    html = re.sub(r'text-slate-900', 'style="color: #1a2e1a;"', html)
    html = re.sub(r'text-slate-800', 'style="color: #2a2518;"', html)
    html = re.sub(r'text-slate-700', 'style="color: #3a3528;"', html)
    html = re.sub(r'text-slate-600', 'style="color: #5c5647;"', html)
    html = re.sub(r'text-slate-500', 'style="color: #6c6657;"', html)
    
    # Replace backgrounds
    html = re.sub(r'bg-blue-50', 'style="background: #eef1e8;"', html)
    html = re.sub(r'bg-sky-50', 'style="background: #eef1e8;"', html)
    html = re.sub(r'bg-slate-100', 'style="background: #f0ede6;"', html)
    
    # Replace border colors
    html = re.sub(r'border-slate-200', 'style="border-color: #f0ede6;"', html)
    html = re.sub(r'border-slate-100', 'style="border-color: #f0ede6;"', html)
    html = re.sub(r'hover:border-blue-200', '', html)
    html = re.sub(r'hover:border-sky-200', '', html)
    
    # Replace card shadows
    html = re.sub(r'shadow-sm hover:shadow-md', 'card-shadow', html)
    html = re.sub(r'shadow-sm hover:shadow', 'card-shadow', html)
    
    # Replace footer
    html = re.sub(
        r'<footer class="bg-slate-900[^"]*">',
        '<footer class="py-10 px-4" style="background: #1a2e1a;">',
        html
    )
    html = re.sub(
        r'<footer class="bg-slate-800[^"]*">',
        '<footer class="py-10 px-4" style="background: #1a2e1a;">',
        html
    )
    
    # Replace footer text colors
    html = re.sub(r'text-slate-400', 'style="color: #a8a090;"', html)
    html = re.sub(r'text-slate-300', 'style="color: #c8c1b5;"', html)
    
    # Replace favicon
    html = re.sub(r'favicon\.svg" type="image/svg\+xml"', 'favicon.ico" type="image/x-icon"', html)
    
    # Add font-serif to headings
    html = re.sub(
        r'class="text-4xl md:text-5xl font-bold([^"]*)"',
        r'class="text-4xl md:text-5xl font-bold font-serif\1"',
        html
    )
    html = re.sub(
        r'class="text-3xl md:text-4xl font-bold([^"]*)"',
        r'class="text-3xl md:text-4xl font-bold font-serif\1"',
        html
    )
    html = re.sub(
        r'class="text-2xl font-bold([^"]*)"',
        r'class="text-2xl font-bold font-serif\1"',
        html
    )
    
    return html


def process_lang_dirs(base_dir):
    """Process all language directories."""
    langs = ['da', 'de', 'es', 'fi', 'fr', 'it', 'ja', 'nl', 'no', 'pl', 'pt', 'ru', 'sv', 'tr', 'zh']
    count = 0
    
    for lang in langs:
        index_path = os.path.join(base_dir, lang, 'index.html')
        if os.path.exists(index_path):
            with open(index_path, 'r', encoding='utf-8') as f:
                html = f.read()
            
            new_html = retheme_index(html)
            
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(new_html)
            
            print(f"  [updated] {lang}/index.html")
            count += 1
        else:
            print(f"  [missing] {lang}/index.html")
    
    return count


if __name__ == '__main__':
    base_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    print(f"Rethemimg language index pages in {base_dir}...")
    count = process_lang_dirs(base_dir)
    print(f"Done. {count} page(s) updated.")
