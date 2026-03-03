#!/usr/bin/env python3
"""Properly retheme tool pages (search/quiz/compare/about/faq)."""
import sys
import re

def fix_page(html):
    # 1. Fix font import - replace Plus Jakarta Sans with Fraunces + Inter
    html = re.sub(
        r"family=Plus\+Jakarta\+Sans[^'\"&]*",
        'family=Fraunces:wght@400;600;700&family=Inter:wght@400;500;600',
        html
    )
    
    # 2. Add font-family CSS if not present
    if "font-family: 'Inter'" not in html and '</style>' in html:
        html = html.replace(
            '</style>',
            "        body { font-family: 'Inter', sans-serif; }\n        .font-serif { font-family: 'Fraunces', serif; }\n    </style>"
        )
    
    # 3. Fix logo reference
    html = html.replace('logo-192.png', 'logo-192-green.png')
    
    # 4. Fix favicon
    html = html.replace('favicon.svg" type="image/svg+xml"', 'favicon.ico" type="image/x-icon"')
    
    # 5. Fix body - be careful with class attribute
    html = re.sub(
        r'<body class="bg-slate-50 min-h-screen">',
        '<body class="min-h-screen" style="background: linear-gradient(135deg, #f6f7f2 0%, #faf9f6 50%, #eef1e8 100%); color: #2a2518;">',
        html
    )
    html = re.sub(
        r'<body class="min-h-screen bg-slate-50">',
        '<body class="min-h-screen" style="background: linear-gradient(135deg, #f6f7f2 0%, #faf9f6 50%, #eef1e8 100%); color: #2a2518;">',
        html
    )
    
    # 6. Fix footer background
    html = re.sub(
        r'<footer class="bg-slate-900([^"]*)"',
        r'<footer class="py-10 px-4\1" style="background: #1a2e1a;"',
        html
    )
    html = re.sub(
        r'<footer class="([^"]*?)bg-slate-900([^"]*)"',
        r'<footer class="\1\2" style="background: #1a2e1a;"',
        html
    )
    
    return html

if __name__ == '__main__':
    filepath = sys.argv[1]
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    fixed = fix_page(html)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed)
    print(f"Fixed: {filepath}")
