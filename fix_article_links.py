#!/usr/bin/env python3
"""Fix article links on homepages - change search filters to actual articles"""

import os
import re

# Article folder names per language
ARTICLES = {
    'da': {'apartment': 'bedste-hunde-til-lejligheder', 'family': 'bedste-hunde-til-familier', 'shedding': 'hunde-der-ikke-falder'},
    'de': {'apartment': 'beste-hunde-fur-wohnungen', 'family': 'beste-hunde-fur-familien', 'shedding': 'hunde-die-nicht-haaren'},
    'es': {'apartment': 'mejores-perros-para-apartamentos', 'family': 'mejores-perros-para-familias', 'shedding': 'perros-que-no-sueltan-pelo'},
    'fi': {'apartment': 'parhaat-koirat-kerrostaloihin', 'family': 'parhaat-koirat-perheille', 'shedding': 'koirat-jotka-eivat-karvaa'},
    'fr': {'apartment': 'meilleurs-chiens-pour-appartements', 'family': 'meilleurs-chiens-pour-familles', 'shedding': 'chiens-qui-ne-perdent-pas-leurs-poils'},
    'it': {'apartment': 'migliori-cani-per-appartamenti', 'family': 'migliori-cani-per-famiglie', 'shedding': 'cani-che-non-perdono-pelo'},
    'ja': {'apartment': 'apartment-dogs', 'family': 'family-dogs', 'shedding': 'low-shedding-dogs'},
    'nl': {'apartment': 'beste-honden-voor-appartementen', 'family': 'beste-honden-voor-gezinnen', 'shedding': 'honden-die-niet-verharen'},
    'no': {'apartment': 'beste-hunder-for-leiligheter', 'family': 'beste-hunder-for-familier', 'shedding': 'hunder-som-ikke-roper'},
    'pl': {'apartment': 'najlepsze-psy-do-mieszkan', 'family': 'najlepsze-psy-dla-rodzin', 'shedding': 'psy-ktore-nie-linieja'},
    'pt': {'apartment': 'melhores-caes-para-apartamentos', 'family': 'melhores-caes-para-familias', 'shedding': 'caes-que-nao-soltam-pelo'},
    'ru': {'apartment': 'luchshie-sobaki-dlja-kvartir', 'family': 'luchshie-sobaki-dlja-semej', 'shedding': 'sobaki-kotorye-ne-linjajut'},
    'sv': {'apartment': 'basta-hundar-for-lagenheter', 'family': 'basta-hundar-for-familjer', 'shedding': 'hundar-som-inte-faller'},
    'tr': {'apartment': 'en-iyi-daire-kopekleri', 'family': 'en-iyi-aile-kopekleri', 'shedding': 'tuy-dokmeyen-kopekler'},
    'zh': {'apartment': 'gongyu-shiyong-quan', 'family': 'jiating-shiyong-quan', 'shedding': 'bu-diao-mao-quan'},
}

def fix_homepage(lang, articles):
    filepath = f"{lang}/index.html"
    if not os.path.exists(filepath):
        return False
    
    # First check if article folders exist
    for key, folder in articles.items():
        if os.path.exists(f"{lang}/articles/{folder}/index.html"):
            pass  # Folder exists
        else:
            # Try to find the actual folder
            if os.path.exists(f"{lang}/articles"):
                folders = os.listdir(f"{lang}/articles")
                # Just use the first article for now
                if folders:
                    articles[key] = folders[0] if folders[0] != 'index.html' else (folders[1] if len(folders) > 1 else folder)
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    original = content
    
    # Replace search filters with article links
    content = content.replace('href="search/?apartment=1"', f'href="articles/{articles["apartment"]}/"')
    content = content.replace('href="search/?kids=1"', f'href="articles/{articles["family"]}/"')
    content = content.replace('href="search/?shedding=minimal"', f'href="articles/{articles["shedding"]}/"')
    
    # Also fix "View all guides" link
    content = content.replace('href="search/"', 'href="articles/"')
    
    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    return False

# Get actual article folders
for lang in ARTICLES:
    if os.path.exists(f"{lang}/articles"):
        folders = [f for f in os.listdir(f"{lang}/articles") if f != 'index.html' and os.path.isdir(f"{lang}/articles/{f}")]
        if len(folders) >= 3:
            # Find apartment, family, shedding articles by keyword
            for folder in folders:
                if 'apartment' in folder or 'lejlighed' in folder or 'wohnung' in folder or 'apartament' in folder or 'appartement' in folder or 'leilighet' in folder or 'daire' in folder or 'mieszkan' in folder or 'gongyu' in folder or 'kvartir' in folder or 'lägenhet' in folder or 'kerros' in folder:
                    ARTICLES[lang]['apartment'] = folder
                elif 'famil' in folder or 'rodzin' in folder or 'gezin' in folder or 'semej' in folder or 'jiating' in folder or 'perhei' in folder or 'aile' in folder:
                    ARTICLES[lang]['family'] = folder
                elif 'shed' in folder or 'haar' in folder or 'pelo' in folder or 'poil' in folder or 'karv' in folder or 'lin' in folder or 'fall' in folder or 'tuy' in folder or 'mao' in folder or 'roper' in folder:
                    ARTICLES[lang]['shedding'] = folder

count = 0
for lang in ARTICLES:
    if fix_homepage(lang, ARTICLES[lang]):
        count += 1
        print(f"Fixed {lang}")

print(f"\nDone! Fixed {count} homepages")
