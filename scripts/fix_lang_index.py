#!/usr/bin/env python3
"""Properly retheme a language index page."""
import sys
import re

def fix_page(html):
    # 1. Fix font import
    html = re.sub(
        r"<link href=\"https://fonts\.googleapis\.com/css2\?family=Plus\+Jakarta\+Sans[^\"]*\"",
        '<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@400;600;700&family=Inter:wght@400;500;600"',
        html
    )
    
    # 2. Fix tailwind config
    html = re.sub(
        r"tailwind\.config = \{ theme: \{ extend: \{ fontFamily: \{ sans: \['Plus Jakarta Sans', 'sans-serif'\] \} \} \} \}",
        "tailwind.config = { theme: { extend: { fontFamily: { sans: ['Inter', 'sans-serif'], serif: ['Fraunces', 'serif'] } } } }",
        html
    )
    
    # 3. Fix body
    html = re.sub(
        r'<body class="[^"]*">',
        '<body class="min-h-screen" style="background: linear-gradient(135deg, #f6f7f2 0%, #faf9f6 50%, #eef1e8 100%); color: #2a2518;">',
        html
    )
    
    # 4. Fix header
    html = re.sub(
        r'<header class="bg-white/80 backdrop-blur-md border-b border-slate-200 sticky top-0 z-50">',
        '<header class="bg-white/80 backdrop-blur-md border-b sticky top-0 z-50" style="border-color: #f0ede6;">',
        html
    )
    
    # 5. Fix logo
    html = html.replace('logo-192.png', 'logo-192-green.png')
    html = re.sub(
        r'<span class="text-xl font-bold bg-gradient-to-r from-slate-800 to-slate-600 bg-clip-text text-transparent">BreedFinder</span>',
        '<span class="text-xl font-bold font-serif" style="color: #1a5632;">BreedFinder</span>',
        html
    )
    
    # 6. Fix hero section
    html = re.sub(
        r'<section class="hero-gradient py-20 px-4">',
        '<section class="py-20 px-4" style="background: linear-gradient(135deg, #f6f7f2 0%, #eef1e8 50%, #f6f7f2 100%);">',
        html
    )
    
    # 7. Fix hero title
    html = re.sub(
        r'<span class="bg-gradient-to-r from-sky-500 via-blue-500 to-rose-500 bg-clip-text text-transparent">',
        '<span style="color: #1a5632;">',
        html
    )
    
    # 8. Fix main CTA buttons
    html = re.sub(
        r'bg-gradient-to-r from-sky-500 to-blue-600 text-white',
        'text-white" style="background: #1a5632;',
        html
    )
    
    # 9. Fix footer
    html = re.sub(
        r'<footer class="bg-slate-900 text-white py-12 px-4">',
        '<footer class="py-10 px-4" style="background: #1a2e1a;">',
        html
    )
    
    # 10. Fix footer brand
    html = re.sub(
        r'<span class="text-xl font-bold text-white">BreedFinder</span>',
        '<span class="text-xl font-bold font-serif text-white">BreedFinder</span>',
        html
    )
    
    # 11. Fix hero-gradient style
    html = re.sub(
        r'\.hero-gradient \{[^}]+\}',
        '.hero-gradient { background: linear-gradient(135deg, #f6f7f2 0%, #eef1e8 50%, #f6f7f2 100%); }',
        html
    )
    
    # 12. Fix section headings to use font-serif (just once)
    html = re.sub(
        r'class="text-2xl font-bold text-slate-900',
        'class="text-2xl font-bold font-serif" style="color: #1a2e1a;',
        html
    )
    
    # 13. Fix card borders
    html = re.sub(r'border-slate-100/50', 'border" style="border-color: #f0ede6;', html)
    html = re.sub(r'border border-slate-200', 'border" style="border-color: #f0ede6;', html)
    
    # 14. Fix bg-slate-50 sections
    html = re.sub(r'bg-slate-50', '" style="background: #f6f7f2;', html)
    
    # 15. Fix sky/blue links
    html = re.sub(r'text-sky-600', '" style="color: #1a5632;', html)
    html = re.sub(r'hover:text-sky-700', 'hover:opacity-80', html)
    
    return html

if __name__ == '__main__':
    filepath = sys.argv[1]
    with open(filepath, 'r') as f:
        html = f.read()
    fixed = fix_page(html)
    with open(filepath, 'w') as f:
        f.write(fixed)
    print(f"Fixed: {filepath}")
