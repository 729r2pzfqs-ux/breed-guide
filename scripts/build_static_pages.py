#!/usr/bin/env python3
"""Build /privacy/index.html and /404.html in the site's green theme.

Header markup is copied from an English breed page (without the language
switcher) and the footer comes from scripts/site_footer.py, so both pages stay
in step with the rest of the site. Re-run after changing either.
"""
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
os.chdir(ROOT)
sys.path.insert(0, 'scripts')
from site_footer import footer  # noqa: E402

GA = ("<script>(function(){try{if(Intl.DateTimeFormat().resolvedOptions().timeZone==='Asia/Singapore')return}catch(e){}"
      "var s=document.createElement('script');s.async=true;s.src='https://www.googletagmanager.com/gtag/js?id=G-VEERQZ53LZ';"
      "document.head.appendChild(s);window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}"
      "gtag('js',new Date());gtag('config','G-VEERQZ53LZ');})();</script>")

src = open('breeds/labrador-retriever/index.html', encoding='utf-8').read()
HEADER = re.search(r'<header.*?</header>', src, re.S).group(0)
HEADER = re.sub(r'\s*<div class="relative group">.*?</div>\s*</div>\s*(?=</nav>)', '\n            ', HEADER, flags=re.S)

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
{extra}
    <link rel="icon" href="/favicon.ico" type="image/x-icon">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="stylesheet" href="/css/tailwind.css">
    <script src="/js/icons.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Inter', sans-serif; }}
        h1, h2, h3, .font-serif {{ font-family: 'Fraunces', Georgia, serif; }}
        .card-shadow {{ box-shadow: 0 1px 3px rgba(26,86,50,0.05), 0 4px 12px rgba(26,86,50,0.04); }}
    </style>
{jsonld}</head>
<body class="bg-gradient-to-b from-slate-50 to-white min-h-screen text-[#2a2518]">
    {header}
'''

TAIL = '''
    {footer}

    <script>lucide.createIcons();</script>
{scripts}{ga}
</body>
</html>
'''


def section(title, body):
    return f'''        <section class="bg-white rounded-2xl p-6 md:p-8 mb-4 card-shadow border border-[#f0ede6]">
            <h2 class="text-xl font-bold text-[#1a2e1a] mb-3">{title}</h2>
            {body}
        </section>
'''


def p(text):
    return f'<p class="text-[#5c5647] leading-relaxed mb-3">{text}</p>'


LINK = 'class="text-emerald-800 underline hover:text-emerald-900" rel="noopener" target="_blank"'


def privacy():
    desc = ('BreedFinder collects no names or accounts; it uses Google Analytics 4 to count visits and page views. '
            'Learn what GA4 records, which cookies it sets and how to opt out.')
    jsonld = '''    <script type="application/ld+json">
    {"@context": "https://schema.org", "@type": "WebPage", "name": "Privacy Policy", "url": "https://breedfinder.org/privacy/",
     "inLanguage": "en", "dateModified": "2026-09-25",
     "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://breedfinder.org/"},
        {"@type": "ListItem", "position": 2, "name": "Privacy Policy", "item": "https://breedfinder.org/privacy/"}]}}
    </script>
'''
    extra = '''    <link rel="canonical" href="https://breedfinder.org/privacy/">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://breedfinder.org/privacy/">
    <meta property="og:title" content="Privacy Policy | BreedFinder">
    <meta property="og:description" content="What BreedFinder collects (only anonymous GA4 usage statistics), the cookies involved and how to opt out.">
    <meta property="og:site_name" content="BreedFinder">
    <meta property="og:image" content="https://breedfinder.org/images/og-card.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:image" content="https://breedfinder.org/images/og-card.png">'''
    out = HEAD.format(title='Privacy Policy | BreedFinder', desc=desc, extra=extra, jsonld=jsonld, header=HEADER)
    mail = '<a href="mailto:info@breedfinder.org" class="text-emerald-800 underline hover:text-emerald-900">info@breedfinder.org</a>'
    out += '''
    <main class="max-w-3xl mx-auto px-4 py-8">
        <nav aria-label="Breadcrumb" class="text-sm text-[#5c5647] mb-6 flex items-center gap-2">
            <a href="/" class="hover:text-emerald-800 transition underline">Home</a>
            <i data-lucide="chevron-right" class="w-4 h-4 text-[#5c5647]"></i>
            <span class="text-[#3d3829] font-medium">Privacy Policy</span>
        </nav>
        <div class="mb-8">
            <h1 class="text-4xl md:text-5xl font-bold text-[#1a2e1a] mb-3">Privacy Policy</h1>
            <p class="text-[#5c5647]">Last updated: September 25, 2026</p>
        </div>
'''
    out += section('Summary', p(
        'BreedFinder (breedfinder.org) is a free dog breed guide. You do not need an account, and we never ask for your name, '
        'email address or other personal details. The only data collected automatically is anonymous usage statistics from '
        'Google Analytics 4, described below.'))
    out += section('Analytics (Google Analytics 4)', p(
        'We use Google Analytics 4 (GA4), a service provided by Google, to understand how the site is used: which pages are '
        'visited, how visitors arrive (for example from a search engine), and general device, browser and approximate '
        'location information (country or city level). GA4 does not log or store IP addresses. We use these statistics only '
        'to improve the site; we do not use them to identify individual visitors, and we do not sell or share them.') + p(
        f'Google processes this data under its own terms; see the <a href="https://policies.google.com/privacy" {LINK}>Google '
        f'Privacy Policy</a> and <a href="https://policies.google.com/technologies/partner-sites" {LINK}>how Google uses data '
        f'from sites that use its services</a>. You can opt out of Google Analytics on all websites with the '
        f'<a href="https://tools.google.com/dlpage/gaoptout" {LINK}>Google Analytics opt-out browser add-on</a>.'))
    out += section('Cookies', p(
        'Google Analytics sets first-party cookies (named <code>_ga</code> and <code>_ga_&lt;ID&gt;</code>) to tell visits and '
        'sessions apart. They contain a random identifier, not your name or contact details. BreedFinder does not set any '
        'other cookies. You can block or delete cookies at any time in your browser settings; every part of the site works '
        'without them.'))
    out += section('Other third-party services', p(
        'Pages load fonts from Google Fonts, and the breed search page loads a search library from the jsDelivr CDN. When your '
        'browser requests these files, the provider receives your IP address as part of the normal web request. The site is '
        f'hosted on GitHub Pages and delivered through Cloudflare, both of which may keep standard server logs for security and '
        f'performance. See the <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" {LINK}>'
        f'GitHub Privacy Statement</a> and <a href="https://www.cloudflare.com/privacypolicy/" {LINK}>Cloudflare Privacy Policy</a>.'))
    out += section('Your rights', p(
        'Depending on where you live (for example under the GDPR in the EU/EEA and UK, or the CCPA in California) you may have '
        'the right to access, correct, delete or object to the processing of your personal data. Because BreedFinder does not '
        f'hold personal data itself, most requests relate to Google Analytics: use the opt-out above, or email us at {mail} '
        'and we will help.'))
    out += section('Children', p(
        'BreedFinder is a general-audience site and does not knowingly collect personal information from children under 13 '
        '(or the equivalent minimum age in your country).'))
    out += section('Changes and contact', p(
        'If this policy changes, we will update this page and the date at the top. Questions about privacy? Contact us at '
        f'{mail}.'))
    out += '    </main>\n'
    out += TAIL.format(footer=footer('en'), scripts='', ga=GA)
    os.makedirs('privacy', exist_ok=True)
    open('privacy/index.html', 'w', encoding='utf-8').write(out)


# Client-side redirects for mistyped/localized breed URLs (kept from the original 404)
REDIRECT_JS = open('scripts/404_redirect.js', encoding='utf-8').read()

POPULAR = [('labrador-retriever', 'Labrador Retriever'), ('golden-retriever', 'Golden Retriever'),
           ('german-shepherd', 'German Shepherd'), ('french-bulldog', 'French Bulldog'), ('beagle', 'Beagle'),
           ('poodle', 'Poodle'), ('dachshund', 'Dachshund'), ('siberian-husky', 'Siberian Husky')]


def not_found():
    desc = 'This page could not be found. Browse all 220 dog breeds, take the breed quiz or compare two breeds side by side on BreedFinder.'
    out = HEAD.format(title='Page Not Found | BreedFinder', desc=desc,
                      extra='    <meta name="robots" content="noindex">\n    <script>\n' + REDIRECT_JS + '    </script>',
                      jsonld='', header=HEADER)
    cards = '\n'.join(f'''                <a href="/breeds/{s}/" class="group bg-white rounded-2xl card-shadow border border-[#f0ede6] p-3 flex items-center gap-3 hover:border-emerald-300 transition">
                    <img src="/images/heads/{s}.webp" alt="{n}" width="48" height="48" loading="lazy" class="w-12 h-12 rounded-xl object-cover">
                    <span class="font-medium text-[#2a2518] group-hover:text-emerald-800 text-left text-sm">{n}</span>
                </a>''' for s, n in POPULAR)
    btn = 'inline-flex items-center gap-2 px-6 py-3 rounded-xl font-semibold transition'
    alt = f'{btn} bg-white border border-[#e2ddd4] text-[#3d3829] hover:border-emerald-300'
    out += f'''
    <main class="max-w-4xl mx-auto px-4 py-16 text-center">
        <div class="w-16 h-16 mx-auto mb-6 bg-emerald-50 border border-emerald-100 rounded-2xl flex items-center justify-center text-emerald-800">
            <i data-lucide="search-x" class="w-8 h-8"></i>
        </div>
        <p class="text-sm font-semibold text-emerald-700 mb-2">404</p>
        <h1 class="text-4xl md:text-5xl font-bold text-[#1a2e1a] mb-4">We couldn&rsquo;t find that page</h1>
        <p class="text-[#5c5647] max-w-xl mx-auto mb-6">The page may have moved, or the link may be mistyped. Try one of these instead.</p>
        <div class="flex flex-wrap justify-center gap-3 mb-12">
            <a href="/search/" class="{btn} bg-emerald-800 text-white hover:bg-emerald-900"><i data-lucide="search" class="w-4 h-4"></i>Browse all breeds</a>
            <a href="/quiz/" class="{alt}"><i data-lucide="target" class="w-4 h-4"></i>Breed quiz</a>
            <a href="/compare/" class="{alt}"><i data-lucide="scale" class="w-4 h-4"></i>Compare breeds</a>
            <a href="/" class="{alt}"><i data-lucide="home" class="w-4 h-4"></i>Home</a>
        </div>
        <h2 class="text-2xl font-bold text-[#1a2e1a] mb-4">Popular breeds</h2>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-10">
{cards}
        </div>
        <p class="text-sm text-[#5c5647]">Need advice? Read our <a href="/articles/" class="text-emerald-800 underline">dog breed guides</a> or the <a href="/faq/" class="text-emerald-800 underline">FAQ</a>.</p>
    </main>
'''
    out += TAIL.format(footer=footer('en'), scripts='', ga=GA)
    open('404.html', 'w', encoding='utf-8').write(out)


if __name__ == '__main__':
    privacy()
    not_found()
    print('built privacy/index.html and 404.html')
