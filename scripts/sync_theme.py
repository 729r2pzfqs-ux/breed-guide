#!/usr/bin/env python3
"""Sync theme from English index.html to localized pages."""
import sys
import re

# Read English index.html to extract head content
with open('index.html', 'r', encoding='utf-8') as f:
    en_html = f.read()

# Extract the tailwind config + styles section from English
tailwind_config = re.search(r'(<script>\s*tailwind\.config = \{.*?\}\s*</script>)', en_html, re.DOTALL)
styles = re.search(r'(<style>\s*\.card-shadow \{.*?</style>)', en_html, re.DOTALL)
font_link = '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,400;1,9..144,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'

if not tailwind_config or not styles:
    print("Could not extract config from English index.html")
    sys.exit(1)

tailwind_config_str = tailwind_config.group(1)
styles_str = styles.group(1)

def fix_page(filepath, lang_code, lang_name):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 1. Replace old tailwind config
    html = re.sub(
        r'<script>\s*tailwind\.config = \{[^}]+\}\s*</script>',
        tailwind_config_str,
        html
    )
    
    # 2. Replace font link
    html = re.sub(
        r'<link href="https://fonts\.googleapis\.com/css2\?family=[^"]*" rel="stylesheet">',
        font_link,
        html
    )
    
    # 3. Replace styles
    html = re.sub(
        r'<style>\s*\.card-shadow \{[^}]+\}[^<]*\.card-shadow:hover \{[^}]+\}[^<]*\.hero-gradient \{[^}]+\}[^<]*</style>',
        styles_str,
        html,
        flags=re.DOTALL
    )
    
    # 4. Fix body
    html = re.sub(
        r'<body[^>]*>',
        '<body class="bg-white min-h-screen text-warm-800" style="color: #2a2518;">',
        html
    )
    
    # 5. Fix header
    html = re.sub(
        r'<header[^>]*>',
        '<header class="bg-white/80 backdrop-blur-md border-b sticky top-0 z-50" style="border-color: #f0ede6;">',
        html
    )
    
    # 6. Fix brand
    html = re.sub(
        r'<span class="[^"]*font-bold[^"]*">BreedFinder</span>',
        '<span class="text-xl font-bold font-serif" style="color: #1a5632;">BreedFinder</span>',
        html
    )
    
    # 7. Fix footer
    html = re.sub(
        r'<footer[^>]*>',
        '<footer class="py-12 px-4" style="background: #1a2e1a; color: #c8c1b5;">',
        html
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Synced: {filepath}")

if __name__ == '__main__':
    langs = {
        'da': 'Dansk', 'de': 'Deutsch', 'es': 'Español', 'fi': 'Suomi',
        'fr': 'Français', 'it': 'Italiano', 'ja': '日本語', 'nl': 'Nederlands',
        'no': 'Norsk', 'pl': 'Polski', 'pt': 'Português', 'ru': 'Русский',
        'sv': 'Svenska', 'tr': 'Türkçe', 'zh': '中文'
    }
    
    for lang_code, lang_name in langs.items():
        filepath = f'{lang_code}/index.html'
        try:
            fix_page(filepath, lang_code, lang_name)
        except Exception as e:
            print(f"Error with {filepath}: {e}")
