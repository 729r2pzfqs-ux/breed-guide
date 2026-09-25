#!/usr/bin/env python3
"""Add a visible breadcrumb (+ BreadcrumbList JSON-LD when missing) to
comparison, article, about, FAQ, quiz, search and compare pages in all
languages. Idempotent: pages already carrying aria-label="Breadcrumb" are skipped."""
import html
import json
import os
import re
import subprocess
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
os.chdir(ROOT)
sys.path.insert(0, 'scripts')
from site_footer import LABELS  # noqa: E402

HOME = {'en': 'Home', 'es': 'Inicio', 'de': 'Startseite', 'fr': 'Accueil', 'it': 'Home', 'pt': 'Início',
        'fi': 'Etusivu', 'sv': 'Hem', 'nl': 'Home', 'da': 'Forside', 'ja': 'ホーム', 'no': 'Forside',
        'pl': 'Strona główna', 'ru': 'Главная', 'tr': 'Ana Sayfa', 'zh': '首页'}
LANGS = set(HOME) - {'en'}
BASE = 'https://breedfinder.org'


def h1_text(s):
    m = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S)
    if not m:
        return None
    t = re.sub(r'<[^>]+>', ' ', m.group(1))
    return html.unescape(re.sub(r'\s+', ' ', t)).strip()


def crumbs_for(rest, lang, s):
    p = '' if lang == 'en' else '/' + lang
    b, q, c, g, faq, about, _priv, _ = LABELS[lang]
    home = (HOME[lang], p + '/')
    sec = rest[0]
    if sec == 'compare' and len(rest) > 2:
        return [home, (c, p + '/compare/'), (h1_text(s), None)]
    if sec == 'articles' and len(rest) > 2:
        return [home, (g, p + '/articles/'), (h1_text(s), None)]
    names = {'compare': c, 'articles': g, 'faq': faq, 'about': about, 'quiz': q, 'search': b}
    if sec in names and len(rest) == 2:
        return [home, (names[sec], None)]
    return None


def nav_html(items):
    parts = []
    for i, (name, href) in enumerate(items):
        if href:
            parts.append(f'<a href="{href}" class="hover:text-emerald-800 transition underline">{html.escape(name)}</a>')
        else:
            parts.append(f'<span class="text-[#3d3829] font-medium" aria-current="page">{html.escape(name)}</span>')
    sep = '\n            <span aria-hidden="true">&rsaquo;</span>\n            '
    return ('<nav aria-label="Breadcrumb" class="text-sm text-[#5c5647] mb-6 flex flex-wrap items-center gap-2">\n            '
            + sep.join(parts) + '\n        </nav>')


def ld_html(items, canonical):
    el = []
    for i, (name, href) in enumerate(items, 1):
        it = {'@type': 'ListItem', 'position': i, 'name': name}
        url = BASE + href if href else canonical
        if url:
            it['item'] = url
        el.append(it)
    return ('    <script type="application/ld+json">\n    '
            + json.dumps({'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': el}, ensure_ascii=False)
            + '\n    </script>\n')


def main():
    files = subprocess.check_output(['git', '-c', 'core.quotepath=off', 'ls-files', '-z', '*.html']).decode().split('\0')[:-1]
    stats = {'added': 0, 'replaced': 0, 'ld': 0, 'skipped': 0}
    for f in files:
        parts = f.split('/')
        lang = parts[0] if parts[0] in LANGS else 'en'
        rest = parts[1:] if lang != 'en' else parts
        if rest[0] not in ('compare', 'articles', 'faq', 'about', 'quiz', 'search'):
            continue
        s = open(f, encoding='utf-8').read()
        if 'http-equiv="refresh"' in s[:3000] or 'aria-label="Breadcrumb"' in s:
            continue
        items = crumbs_for(rest, lang, s)
        mm = re.search(r'<main[^>]*>', s)
        if not items or not mm or not items[-1][0]:
            stats['skipped'] += 1
            continue
        nav = nav_html(items)
        after = s[mm.end():]
        old = re.match(r'\s*(?:<!-- Breadcrumb -->\s*)?<nav\b[^>]*>(?:(?!</nav>).)*?(?:›|&rsaquo;|→)(?:(?!</nav>).)*</nav>', after, re.S)
        if old:
            s = s[:mm.end()] + '\n        ' + nav + after[old.end():]
            stats['replaced'] += 1
        else:
            s = s[:mm.end()] + '\n        ' + nav + '\n' + after
            stats['added'] += 1
        if 'BreadcrumbList' not in s:
            canon = re.search(r'<link rel="canonical" href="([^"]+)"', s)
            s = s.replace('</head>', ld_html(items, canon.group(1) if canon else None) + '</head>', 1)
            stats['ld'] += 1
        open(f, 'w', encoding='utf-8').write(s)
    print(stats)


if __name__ == '__main__':
    main()
