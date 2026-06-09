#!/usr/bin/env python3
"""Regenerate sitemap.xml to include all content pages."""
import os
import re
from datetime import date

REPO = os.path.dirname(os.path.abspath(__file__))
BASE = 'https://breedfinder.org'
TODAY = date.today().isoformat()

def get_priority(path):
    """Assign priority based on page type and depth."""
    if path == '/' or path == '': return '1.0'
    depth = path.strip('/').count('/')
    if '/quiz/' in path or '/compare/' in path and depth <= 2: return '0.8'
    if '/about/' in path or '/faq/' in path or '/articles/' in path: return '0.8'
    if '/search/' in path: return '0.7'
    if '/breeds/' in path: return '0.7'
    if '/compare/comparisons/' in path: return '0.6'
    # Language index pages
    parts = path.strip('/').split('/')
    if len(parts) == 1: return '0.9'
    if len(parts) == 2: return '0.7'
    return '0.6'

content_pages = []
for root, dirs, files in os.walk(REPO):
    if '.git' in root or '__pycache__' in root:
        continue
    for f in files:
        if not f.endswith('.html'):
            continue
        fullpath = os.path.join(root, f)
        # Read first 500 bytes to check for redirects
        with open(fullpath, 'r', errors='ignore') as fh:
            head = fh.read(500)
        if 'http-equiv="refresh"' in head:
            continue
        
        rel = os.path.relpath(fullpath, REPO)
        # Convert to URL path
        if rel == 'index.html':
            url_path = '/'
        elif rel.endswith('/index.html'):
            url_path = '/' + rel[:-10]  # strip index.html, keep trailing /
        else:
            url_path = '/' + rel
        
        # Skip 404
        if '404' in url_path:
            continue
        
        content_pages.append(url_path)

content_pages.sort()

# Build sitemap XML
lines = ['<?xml version="1.0" encoding="UTF-8"?>']
lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

for path in content_pages:
    url = BASE + path
    priority = get_priority(path)
    lines.append(f'  <url>')
    lines.append(f'    <loc>{url}</loc>')
    lines.append(f'    <lastmod>{TODAY}</lastmod>')
    lines.append(f'    <priority>{priority}</priority>')
    lines.append(f'  </url>')

lines.append('</urlset>')

sitemap_path = os.path.join(REPO, 'sitemap.xml')
with open(sitemap_path, 'w') as f:
    f.write('\n'.join(lines) + '\n')

print(f'Sitemap generated with {len(content_pages)} URLs')
print(f'Written to: {sitemap_path}')

# Show breakdown
from collections import Counter
types = Counter()
for p in content_pages:
    if '/breeds/' in p: types['breeds'] += 1
    elif '/compare/comparisons/' in p: types['comparisons'] += 1
    elif '/compare/' in p: types['compare_index'] += 1
    elif '/faq/' in p: types['faq'] += 1
    elif '/articles/' in p: types['articles'] += 1
    elif '/about/' in p: types['about'] += 1
    elif '/quiz/' in p: types['quiz'] += 1
    elif '/search/' in p: types['search'] += 1
    else: types['other'] += 1

print('\nBreakdown:')
for k, v in sorted(types.items()):
    print(f'  {k}: {v}')
