#!/usr/bin/env python3
"""Fix rating label colors in compare pages to use semantic colors"""
import os, re

count = 0
compare_dir = "compare/comparisons"

# Color mapping for rating labels
# For traits where HIGH is good (trainability, kid-friendly, sociability):
good_high = {"trainability", "kid-friendliness", "kid-friendly", "apartment", "sociability"}
# For traits where LOW is good (grooming, shedding, energy for apartment people):
good_low = {"grooming", "shedding"}

# Color classes
colors = {
    "Very Low": "text-emerald-600",
    "Low": "text-emerald-600", 
    "Minimal": "text-emerald-600",
    "Moderate": "text-amber-500",
    "Medium": "text-amber-500",
    "High": "text-rose-500",
    "Very High": "text-rose-500",
    "Heavy": "text-rose-500",
    "Extensive": "text-rose-500",
    "Excellent": "text-emerald-600",
    "Good": "text-emerald-600",
    "Fair": "text-amber-500",
    "Poor": "text-rose-500",
}

def fix_page(filepath):
    global count
    with open(filepath, 'r') as f:
        html = f.read()
    
    original = html
    
    # Replace rating labels with colored versions
    # Pattern: <span class="text-sm text-slate-600">Label</span>
    for label, color in colors.items():
        html = html.replace(
            f'<span class="text-sm text-slate-600">{label}</span>',
            f'<span class="text-sm font-medium {color}">{label}</span>'
        )
    
    # Also fix inline colored labels
    # Pattern: <td class="p-4 text-center font-semibold text-blue-600">Moderate</td>
    # These should also use semantic colors
    for label, color in colors.items():
        html = re.sub(
            rf'<td class="p-4 text-center font-semibold text-(?:blue|rose|slate)-\d+">{label}</td>',
            f'<td class="p-4 text-center font-semibold {color}">{label}</td>',
            html
        )
    
    if html != original:
        with open(filepath, 'w') as f:
            f.write(html)
        count += 1

# Process all compare pages
for d in sorted(os.listdir(compare_dir)):
    p = os.path.join(compare_dir, d, "index.html")
    if os.path.isfile(p):
        fix_page(p)

print(f"✅ Fixed rating colors on {count} compare pages")
