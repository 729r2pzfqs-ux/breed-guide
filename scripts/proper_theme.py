#!/usr/bin/env python3
"""Properly apply forest green theme to localized pages."""
import re
import sys

def apply_theme(html):
    # 1. Font import - replace Plus Jakarta Sans with Fraunces + Inter
    html = re.sub(
        r'<link href="https://fonts\.googleapis\.com/css2\?family=Plus\+Jakarta\+Sans[^"]*" rel="stylesheet">',
        '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">',
        html
    )
    
    # 2. Tailwind config - add forest/sage/warm colors
    old_config = r"tailwind\.config = \{ theme: \{ extend: \{ fontFamily: \{ sans: \['Plus Jakarta Sans', 'sans-serif'\] \} \} \} \}"
    new_config = """tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        serif: ['Fraunces', 'Georgia', 'serif']
                    },
                    colors: {
                        sage: { 50: '#f6f7f2', 100: '#eef1e8', 200: '#dde3d4' },
                        warm: { 100: '#f0ede6', 200: '#e2ddd4', 600: '#5c5647', 800: '#2a2518' },
                        forest: { DEFAULT: '#1a5632', dark: '#1a2e1a' }
                    }
                }
            }
        }"""
    html = re.sub(old_config, new_config, html)
    
    # 3. Card shadow styles
    html = re.sub(
        r'\.card-shadow \{ box-shadow: 0 1px 3px rgba\(0,0,0,0\.04\), 0 4px 12px rgba\(0,0,0,0\.03\); \}',
        '.card-shadow { box-shadow: 0 1px 3px rgba(26,86,50,0.04), 0 4px 12px rgba(26,86,50,0.03); }',
        html
    )
    html = re.sub(
        r'\.card-shadow:hover \{ box-shadow: 0 4px 12px rgba\(0,0,0,0\.06\), 0 8px 24px rgba\(0,0,0,0\.05\); \}',
        '.card-shadow:hover { box-shadow: 0 4px 12px rgba(26,86,50,0.06), 0 8px 24px rgba(26,86,50,0.05); }',
        html
    )
    
    # 4. Hero gradient
    html = re.sub(
        r'\.hero-gradient \{[^}]+\}',
        '.hero-gradient { background: linear-gradient(135deg, #f6f7f2 0%, #eef1e8 50%, #f6f7f2 100%); }',
        html
    )
    
    # 5. Body
    html = re.sub(
        r'<body class="bg-white min-h-screen text-slate-800">',
        '<body class="bg-white min-h-screen" style="color: #2a2518;">',
        html
    )
    
    # 6. Header border
    html = re.sub(
        r'<header class="bg-white/80 backdrop-blur-md border-b border-slate-100 sticky top-0 z-50">',
        '<header class="bg-white/80 backdrop-blur-md border-b sticky top-0 z-50" style="border-color: #f0ede6;">',
        html
    )
    
    # 7. Logo
    html = html.replace('logo-192.png', 'logo-192-green.png')
    
    # 8. Brand text
    html = re.sub(
        r'<span class="text-xl font-bold bg-gradient-to-r from-slate-800 to-slate-600 bg-clip-text text-transparent">BreedFinder</span>',
        '<span class="text-xl font-bold font-serif" style="color: #1a5632;">BreedFinder</span>',
        html
    )
    
    # 9. Nav links
    html = re.sub(
        r'class="text-slate-600 hover:text-sky-700 transition',
        'class="transition" style="color: #5c5647;" onmouseover="this.style.color=\'#1a5632\'" onmouseout="this.style.color=\'#5c5647\'"',
        html
    )
    
    # 10. CTA button
    html = re.sub(
        r'class="bg-gradient-to-r from-sky-500 to-blue-600 text-white px-5 py-2\.5 rounded-xl font-semibold hover:shadow-lg transition"',
        'class="text-white px-5 py-2.5 rounded-xl font-semibold transition" style="background: #1a5632;" onmouseover="this.style.boxShadow=\'0 8px 20px rgba(26,86,50,0.25)\'" onmouseout="this.style.boxShadow=\'none\'"',
        html
    )
    
    # 11. Language selector button
    html = re.sub(
        r'class="flex items-center gap-1 text-slate-600 hover:text-sky-700 py-2"',
        'class="flex items-center gap-1 py-2 transition" style="color: #5c5647;" onmouseover="this.style.color=\'#1a5632\'" onmouseout="this.style.color=\'#5c5647\'"',
        html
    )
    
    # 12. Language dropdown border
    html = re.sub(
        r'class="absolute right-0 top-full bg-white border border-slate-200 rounded-xl',
        'class="absolute right-0 top-full bg-white border rounded-xl" style="border-color: #e2ddd4;',
        html
    )
    
    # 13. Hero title gradient
    html = re.sub(
        r'<span class="bg-gradient-to-r from-sky-500 via-blue-500 to-rose-500 bg-clip-text text-transparent">',
        '<span style="color: #1a5632;">',
        html
    )
    
    # 14. Hero CTA buttons (large)
    html = re.sub(
        r'class="inline-flex items-center gap-2 bg-gradient-to-r from-sky-500 to-blue-600 text-white px-8 py-4 rounded-2xl font-semibold text-lg hover:shadow-xl hover:shadow-sky-500/25 transition transform hover:-translate-y-0\.5"',
        'class="inline-flex items-center gap-2 text-white px-8 py-4 rounded-2xl font-semibold text-lg transition transform hover:-translate-y-0.5" style="background: #1a5632;" onmouseover="this.style.boxShadow=\'0 12px 28px rgba(26,86,50,0.3)\'" onmouseout="this.style.boxShadow=\'none\'"',
        html
    )
    
    # 15. Secondary button
    html = re.sub(
        r'class="inline-flex items-center gap-2 bg-white text-slate-700 border border-slate-200 px-8 py-4 rounded-2xl font-semibold text-lg hover:border-slate-300 hover:shadow-lg transition transform hover:-translate-y-0\.5"',
        'class="inline-flex items-center gap-2 bg-white px-8 py-4 rounded-2xl font-semibold text-lg transition transform hover:-translate-y-0.5" style="color: #3d3829; border: 1px solid #e2ddd4;" onmouseover="this.style.boxShadow=\'0 8px 20px rgba(26,86,50,0.1)\'" onmouseout="this.style.boxShadow=\'none\'"',
        html
    )
    
    # 16. Footer
    html = re.sub(
        r'<footer class="bg-slate-900 text-white py-12 px-4">',
        '<footer class="py-12 px-4" style="background: #1a2e1a; color: #c8c1b5;">',
        html
    )
    
    # 17. Section headings
    html = re.sub(
        r'class="text-2xl font-bold text-slate-900 mb-2"',
        'class="text-2xl font-bold font-serif mb-2" style="color: #1a2e1a;"',
        html
    )
    
    # 18. Subheadings
    html = re.sub(
        r'class="text-slate-600 mb-8"',
        'class="mb-8" style="color: #5c5647;"',
        html
    )
    
    # 19. Size filter cards
    html = re.sub(
        r'class="bg-sky-50 hover:bg-sky-100 rounded-2xl p-6 text-center transition border border-sky-200 group"',
        'class="rounded-2xl p-6 text-center transition border group" style="background: #eef1e8; border-color: #dde3d4;" onmouseover="this.style.background=\'#e5ebe5\'" onmouseout="this.style.background=\'#eef1e8\'"',
        html
    )
    
    # 20. Lifestyle filter cards (same as size)
    
    # 21. Article cards
    html = re.sub(
        r'class="bg-white rounded-xl p-5 card-shadow hover:shadow-md transition border border-slate-100"',
        'class="bg-white rounded-xl p-5 card-shadow transition border" style="border-color: #f0ede6;"',
        html
    )
    
    # 22. FAQ items
    html = re.sub(
        r'class="bg-white rounded-xl p-6 shadow-sm"',
        'class="bg-white rounded-xl p-6 card-shadow"',
        html
    )
    
    # 23. Text colors throughout
    html = html.replace('text-slate-600', 'text-warm-600')
    html = html.replace('text-slate-700', 'text-warm-700')
    html = html.replace('text-slate-800', 'text-warm-800')
    html = html.replace('text-slate-900', 'text-forest-dark')
    
    # 24. Sky colors
    html = html.replace('text-sky-700', 'text-forest')
    html = html.replace('text-sky-600', 'text-forest')
    html = html.replace('bg-sky-50', 'bg-sage-100')
    
    # 25. Blue icons
    html = html.replace('text-blue-500', 'text-forest')
    html = html.replace('text-green-500', 'text-forest')
    html = html.replace('text-orange-500', 'text-amber-600')
    
    return html

if __name__ == '__main__':
    filepath = sys.argv[1]
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    themed = apply_theme(html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(themed)
    
    print(f"Themed: {filepath}")
