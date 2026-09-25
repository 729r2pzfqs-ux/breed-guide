#!/usr/bin/env python3
"""Regenerate sitemap.xml with real lastmod dates.

lastmod = date of the last commit that touched the page, or today when the
working copy changes the visible text of <main> (nav/breadcrumb/footer-only
edits don't count). Skips redirect stubs, noindex pages and pages whose
canonical points elsewhere."""
import datetime
import os
import re
import subprocess

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
os.chdir(ROOT)
BASE = 'https://breedfinder.org'
TODAY = datetime.date.today().isoformat()


def git(*a):
    return subprocess.check_output(['git', '-c', 'core.quotepath=off', *a]).decode('utf-8')


# newest commit date per file, in one pass over history
last = {}
date = None
for line in git('log', '--format=@%cs', '--name-only', '--', '*.html').splitlines():
    if line.startswith('@'):
        date = line[1:]
    elif line and line not in last:
        last[line] = date
dirty = set(git('diff', '--name-only', 'HEAD').splitlines()) | set(git('ls-files', '--others', '--exclude-standard').splitlines())


def text_of_main(s):
    m = re.search(r'<main.*?</main>', s, re.S)
    t = m.group(0) if m else s
    t = re.sub(r'<(script|style|nav)\b.*?</\1>', ' ', t, flags=re.S)
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', t)).strip()


def lastmod(path, html):
    if path in dirty:
        try:
            old = subprocess.check_output(['git', 'show', f'HEAD:{path}'], stderr=subprocess.DEVNULL).decode('utf-8', 'replace')
        except subprocess.CalledProcessError:
            return TODAY
        if text_of_main(old) != text_of_main(html):
            return TODAY
    return last.get(path, TODAY)


urls = []
for path in git('ls-files', '-z', '*.html').split('\0')[:-1] + git('ls-files', '-z', '--others', '--exclude-standard', '*.html').split('\0')[:-1]:
    if not path.endswith('index.html'):
        continue
    html = open(path, encoding='utf-8', errors='replace').read()
    if 'http-equiv="refresh"' in html[:3000] or re.search(r'<meta name="robots" content="[^"]*noindex', html):
        continue
    url = BASE + '/' + path[:-len('index.html')]
    canon = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    if canon and canon.group(1).rstrip('/') != url.rstrip('/'):
        continue
    urls.append((url, lastmod(path, html)))

urls.sort()
out = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for url, mod in urls:
    out += ['  <url>', f'    <loc>{url}</loc>', f'    <lastmod>{mod}</lastmod>', '  </url>']
out.append('</urlset>')
open('sitemap.xml', 'w').write('\n'.join(out) + '\n')
print(len(urls), 'urls')
