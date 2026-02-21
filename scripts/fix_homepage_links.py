#!/usr/bin/env python3
"""Fix article links in homepages to use translated slugs"""

import re
from pathlib import Path

SLUGS = {
    'es': ('mejores-perros-para-apartamentos', 'mejores-perros-para-familias', 'perros-que-no-sueltan-pelo'),
    'de': ('beste-hunde-fuer-wohnungen', 'beste-hunde-fuer-familien', 'wenig-haarende-hunde'),
    'fr': ('meilleurs-chiens-pour-appartements', 'meilleurs-chiens-pour-familles', 'chiens-qui-ne-perdent-pas-leurs-poils'),
    'it': ('migliori-cani-per-appartamenti', 'migliori-cani-per-famiglie', 'cani-che-non-perdono-pelo'),
    'pt': ('melhores-caes-para-apartamentos', 'melhores-caes-para-familias', 'caes-que-nao-soltam-pelo'),
    'nl': ('beste-honden-voor-appartementen', 'beste-honden-voor-gezinnen', 'honden-die-niet-verharen'),
    'pl': ('najlepsze-psy-do-mieszkan', 'najlepsze-psy-dla-rodzin', 'psy-ktore-nie-linieja'),
    'zh': ('zui-hao-de-gongyu-quan', 'zui-hao-de-jiating-quan', 'bu-diao-mao-de-gou'),
    'ja': ('manshon-ni-tekishita-inu', 'kazoku-ni-tekishita-inu', 'ke-ga-nukenai-inu'),
    'fi': ('parhaat-kerrostalokoirat', 'parhaat-perhekoirat', 'vahan-karvaavat-koirat'),
    'sv': ('basta-hundar-for-lagenheter', 'basta-hundar-for-familjer', 'hundar-som-inte-faller'),
    'no': ('beste-hunder-for-leiligheter', 'beste-hunder-for-familier', 'hunder-som-ikke-feller'),
    'da': ('bedste-hunde-til-lejligheder', 'bedste-hunde-til-familier', 'hunde-der-ikke-falder'),
    'ru': ('luchshie-sobaki-dlya-kvartir', 'luchshie-sobaki-dlya-semey', 'sobaki-kotorye-ne-linyayut'),
}

base_dir = Path(__file__).parent.parent

for lang, (apt, fam, shed) in SLUGS.items():
    homepage = base_dir / lang / 'index.html'
    if homepage.exists():
        content = homepage.read_text()
        # Replace article links
        content = re.sub(r'articles/best-dogs-for-apartments/', f'articles/{apt}/', content)
        content = re.sub(r'articles/best-dogs-for-families/', f'articles/{fam}/', content)
        content = re.sub(r'articles/low-shedding-dogs/', f'articles/{shed}/', content)
        homepage.write_text(content)
        print(f"Fixed {lang}/index.html")

print("\n✅ Done!")
