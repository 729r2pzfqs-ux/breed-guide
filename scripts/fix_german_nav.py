#!/usr/bin/env python3
"""Fix German breed pages - hide Browse Breeds on mobile"""

import os
import re
from pathlib import Path

breeds_dir = Path(__file__).parent.parent / "de" / "breeds"

# Patterns to fix
fixes = [
    # Fix the nav Browse link - hide on mobile
    (
        r'<a href="\.\./search/" class="text-slate-600 hover:text-sky-600">Rassen Durchsuchen</a>',
        '<a href="../search/" class="hidden md:block text-slate-600 hover:text-sky-600">Rassen Durchsuchen</a>'
    ),
]

count = 0
for html_file in breeds_dir.glob("*.html"):
    content = html_file.read_text(encoding='utf-8')
    original = content
    
    for pattern, replacement in fixes:
        content = re.sub(pattern, replacement, content)
    
    if content != original:
        html_file.write_text(content, encoding='utf-8')
        count += 1
        print(f"  Fixed {html_file.name}")

print(f"\n✅ Fixed {count} German breed pages")
