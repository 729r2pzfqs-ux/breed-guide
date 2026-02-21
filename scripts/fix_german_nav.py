#!/usr/bin/env python3
"""Fix German breed pages - search icon on mobile, text on desktop"""

import os
import re
from pathlib import Path

breeds_dir = Path(__file__).parent.parent / "de" / "breeds"

# Old pattern (from previous fix)
old_pattern = r'<a href="\.\./search/" class="hidden md:block text-slate-600 hover:text-sky-600">Rassen Durchsuchen</a>'

# New replacement with icon on mobile, text on desktop
new_html = '''<a href="../search/" class="text-slate-600 hover:text-sky-600 flex items-center">
                    <i data-lucide="search" class="w-5 h-5 md:hidden"></i>
                    <span class="hidden md:inline">Rassen Durchsuchen</span>
                </a>'''

count = 0
for html_file in breeds_dir.glob("*.html"):
    content = html_file.read_text(encoding='utf-8')
    original = content
    
    content = re.sub(old_pattern, new_html, content)
    
    if content != original:
        html_file.write_text(content, encoding='utf-8')
        count += 1
        print(f"  Fixed {html_file.name}")

print(f"\n✅ Fixed {count} German breed pages")
