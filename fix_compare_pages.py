#!/usr/bin/env python3
"""Fix all compare pages: nav links and language dropdown"""

import os
import re

# Language configs
LANGS = {
    'da': {'name': 'Dansk', 'browse': 'Gennemse Racer', 'quiz': 'Tag Testen'},
    'de': {'name': 'Deutsch', 'browse': 'Rassen durchsuchen', 'quiz': 'Quiz starten'},
    'es': {'name': 'Español', 'browse': 'Ver Razas', 'quiz': 'Hacer el Test'},
    'fi': {'name': 'Suomi', 'browse': 'Selaa Rotuja', 'quiz': 'Tee Testi'},
    'fr': {'name': 'Français', 'browse': 'Parcourir les Races', 'quiz': 'Faire le Quiz'},
    'it': {'name': 'Italiano', 'browse': 'Sfoglia Razze', 'quiz': 'Fai il Quiz'},
    'ja': {'name': '日本語', 'browse': '犬種一覧', 'quiz': 'クイズを受ける'},
    'nl': {'name': 'Nederlands', 'browse': 'Bekijk Rassen', 'quiz': 'Doe de Quiz'},
    'no': {'name': 'Norsk', 'browse': 'Bla gjennom Raser', 'quiz': 'Ta Quizen'},
    'pl': {'name': 'Polski', 'browse': 'Przeglądaj Rasy', 'quiz': 'Zrób Quiz'},
    'pt': {'name': 'Português', 'browse': 'Ver Raças', 'quiz': 'Fazer o Quiz'},
    'ru': {'name': 'Русский', 'browse': 'Просмотр Пород', 'quiz': 'Пройти Тест'},
    'sv': {'name': 'Svenska', 'browse': 'Bläddra Raser', 'quiz': 'Gör Testet'},
    'tr': {'name': 'Türkçe', 'browse': 'Irkları Gözat', 'quiz': 'Testi Yap'},
    'zh': {'name': '中文', 'browse': '浏览犬种', 'quiz': '做测试'},
}

# UI translations
UI = {
    'da': {
        'title': 'Sammenlign Hunderacer Side om Side',
        'meta_desc': 'Sammenlign hunderacer side om side. Se størrelse, energiniveau, plejebehov og mere.',
        'h1_compare': 'Sammenlign',
        'h1_breeds': 'Racer',
        'select_up_to': 'Vælg op til 3 racer at sammenligne side om side',
        'breed_1': 'Race 1',
        'breed_2': 'Race 2', 
        'breed_3': 'Race 3 (valgfri)',
        'select_breed': 'Vælg en race...',
        'select_breeds': 'Vælg racer at sammenligne',
        'choose_at_least': 'Vælg mindst 2 racer fra dropdowns ovenfor',
        'in_depth': 'Dybdegående Sammenligninger',
        'view_all': 'Se Alle →',
        'quick_compare': 'Hurtig Sammenligning',
        'compare_above': 'Sammenlign ovenfor',
        'footer': '© 2026 BreedFinder. Hjælper dig med at finde din perfekte følgesvend.'
    },
    'de': {
        'title': 'Hunderassen Vergleichen',
        'meta_desc': 'Vergleichen Sie Hunderassen nebeneinander. Größe, Energielevel, Pflegebedarf und mehr.',
        'h1_compare': 'Rassen',
        'h1_breeds': 'Vergleichen',
        'select_up_to': 'Wählen Sie bis zu 3 Rassen zum Vergleich',
        'breed_1': 'Rasse 1',
        'breed_2': 'Rasse 2',
        'breed_3': 'Rasse 3 (optional)',
        'select_breed': 'Rasse wählen...',
        'select_breeds': 'Rassen zum Vergleich auswählen',
        'choose_at_least': 'Wählen Sie mindestens 2 Rassen aus den Dropdowns',
        'in_depth': 'Detaillierte Vergleiche',
        'view_all': 'Alle anzeigen →',
        'quick_compare': 'Schnellvergleich',
        'compare_above': 'Oben vergleichen',
        'footer': '© 2026 BreedFinder. Wir helfen Ihnen, Ihren perfekten Begleiter zu finden.'
    },
    'es': {
        'title': 'Comparar Razas de Perros',
        'meta_desc': 'Compara razas de perros lado a lado. Ve tamaño, nivel de energía, necesidades de cuidado y más.',
        'h1_compare': 'Comparar',
        'h1_breeds': 'Razas',
        'select_up_to': 'Selecciona hasta 3 razas para comparar lado a lado',
        'breed_1': 'Raza 1',
        'breed_2': 'Raza 2',
        'breed_3': 'Raza 3 (opcional)',
        'select_breed': 'Selecciona una raza...',
        'select_breeds': 'Selecciona razas para comparar',
        'choose_at_least': 'Elige al menos 2 razas de los menús de arriba',
        'in_depth': 'Comparaciones Detalladas',
        'view_all': 'Ver Todas →',
        'quick_compare': 'Comparación Rápida',
        'compare_above': 'Comparar arriba',
        'footer': '© 2026 BreedFinder. Te ayudamos a encontrar tu compañero perfecto.'
    },
    'fi': {
        'title': 'Vertaa Koirarotuja',
        'meta_desc': 'Vertaa koirarotuja vierekkäin. Katso koko, energiataso, hoitotarpeet ja muuta.',
        'h1_compare': 'Vertaa',
        'h1_breeds': 'Rotuja',
        'select_up_to': 'Valitse enintään 3 rotua vertailtavaksi',
        'breed_1': 'Rotu 1',
        'breed_2': 'Rotu 2',
        'breed_3': 'Rotu 3 (valinnainen)',
        'select_breed': 'Valitse rotu...',
        'select_breeds': 'Valitse rotuja vertailuun',
        'choose_at_least': 'Valitse vähintään 2 rotua yllä olevista valikoista',
        'in_depth': 'Syvälliset Vertailut',
        'view_all': 'Näytä kaikki →',
        'quick_compare': 'Pikavertailu',
        'compare_above': 'Vertaa yllä',
        'footer': '© 2026 BreedFinder. Autamme sinua löytämään täydellisen kumppanin.'
    },
    'fr': {
        'title': 'Comparer les Races de Chiens',
        'meta_desc': 'Comparez les races de chiens côte à côte. Taille, niveau d\'énergie, besoins de toilettage et plus.',
        'h1_compare': 'Comparer les',
        'h1_breeds': 'Races',
        'select_up_to': 'Sélectionnez jusqu\'à 3 races à comparer',
        'breed_1': 'Race 1',
        'breed_2': 'Race 2',
        'breed_3': 'Race 3 (optionnel)',
        'select_breed': 'Sélectionnez une race...',
        'select_breeds': 'Sélectionnez des races à comparer',
        'choose_at_least': 'Choisissez au moins 2 races dans les menus ci-dessus',
        'in_depth': 'Comparaisons Détaillées',
        'view_all': 'Voir Tout →',
        'quick_compare': 'Comparaison Rapide',
        'compare_above': 'Comparer ci-dessus',
        'footer': '© 2026 BreedFinder. Nous vous aidons à trouver votre compagnon parfait.'
    },
    'it': {
        'title': 'Confronta Razze di Cani',
        'meta_desc': 'Confronta le razze di cani fianco a fianco. Vedi taglia, livello di energia, esigenze di toelettatura e altro.',
        'h1_compare': 'Confronta',
        'h1_breeds': 'Razze',
        'select_up_to': 'Seleziona fino a 3 razze da confrontare',
        'breed_1': 'Razza 1',
        'breed_2': 'Razza 2',
        'breed_3': 'Razza 3 (opzionale)',
        'select_breed': 'Seleziona una razza...',
        'select_breeds': 'Seleziona razze da confrontare',
        'choose_at_least': 'Scegli almeno 2 razze dai menu sopra',
        'in_depth': 'Confronti Dettagliati',
        'view_all': 'Vedi Tutti →',
        'quick_compare': 'Confronto Rapido',
        'compare_above': 'Confronta sopra',
        'footer': '© 2026 BreedFinder. Ti aiutiamo a trovare il tuo compagno perfetto.'
    },
    'ja': {
        'title': '犬種を比較する',
        'meta_desc': '犬種を並べて比較。サイズ、エネルギーレベル、グルーミングのニーズなどを確認。',
        'h1_compare': '犬種を',
        'h1_breeds': '比較',
        'select_up_to': '最大3つの犬種を選んで比較',
        'breed_1': '犬種 1',
        'breed_2': '犬種 2',
        'breed_3': '犬種 3（任意）',
        'select_breed': '犬種を選択...',
        'select_breeds': '比較する犬種を選択',
        'choose_at_least': '上のドロップダウンから少なくとも2つの犬種を選んでください',
        'in_depth': '詳細な比較',
        'view_all': 'すべて見る →',
        'quick_compare': 'クイック比較',
        'compare_above': '上で比較',
        'footer': '© 2026 BreedFinder. あなたの完璧なパートナーを見つけるお手伝い。'
    },
    'nl': {
        'title': 'Hondenrassen Vergelijken',
        'meta_desc': 'Vergelijk hondenrassen naast elkaar. Bekijk grootte, energieniveau, verzorgingsbehoeften en meer.',
        'h1_compare': 'Rassen',
        'h1_breeds': 'Vergelijken',
        'select_up_to': 'Selecteer tot 3 rassen om te vergelijken',
        'breed_1': 'Ras 1',
        'breed_2': 'Ras 2',
        'breed_3': 'Ras 3 (optioneel)',
        'select_breed': 'Selecteer een ras...',
        'select_breeds': 'Selecteer rassen om te vergelijken',
        'choose_at_least': 'Kies minstens 2 rassen uit de dropdowns hierboven',
        'in_depth': 'Diepgaande Vergelijkingen',
        'view_all': 'Bekijk Alle →',
        'quick_compare': 'Snelle Vergelijking',
        'compare_above': 'Vergelijk hierboven',
        'footer': '© 2026 BreedFinder. Wij helpen u uw perfecte metgezel te vinden.'
    },
    'no': {
        'title': 'Sammenlign Hunderaser',
        'meta_desc': 'Sammenlign hunderaser side om side. Se størrelse, energinivå, stellbehov og mer.',
        'h1_compare': 'Sammenlign',
        'h1_breeds': 'Raser',
        'select_up_to': 'Velg opptil 3 raser å sammenligne',
        'breed_1': 'Rase 1',
        'breed_2': 'Rase 2',
        'breed_3': 'Rase 3 (valgfritt)',
        'select_breed': 'Velg en rase...',
        'select_breeds': 'Velg raser å sammenligne',
        'choose_at_least': 'Velg minst 2 raser fra dropdown-menyene ovenfor',
        'in_depth': 'Dyptgående Sammenligninger',
        'view_all': 'Se Alle →',
        'quick_compare': 'Rask Sammenligning',
        'compare_above': 'Sammenlign ovenfor',
        'footer': '© 2026 BreedFinder. Hjelper deg å finne din perfekte følgesvenn.'
    },
    'pl': {
        'title': 'Porównaj Rasy Psów',
        'meta_desc': 'Porównaj rasy psów obok siebie. Zobacz rozmiar, poziom energii, potrzeby pielęgnacyjne i więcej.',
        'h1_compare': 'Porównaj',
        'h1_breeds': 'Rasy',
        'select_up_to': 'Wybierz do 3 ras do porównania',
        'breed_1': 'Rasa 1',
        'breed_2': 'Rasa 2',
        'breed_3': 'Rasa 3 (opcjonalnie)',
        'select_breed': 'Wybierz rasę...',
        'select_breeds': 'Wybierz rasy do porównania',
        'choose_at_least': 'Wybierz co najmniej 2 rasy z powyższych menu',
        'in_depth': 'Szczegółowe Porównania',
        'view_all': 'Zobacz Wszystkie →',
        'quick_compare': 'Szybkie Porównanie',
        'compare_above': 'Porównaj powyżej',
        'footer': '© 2026 BreedFinder. Pomagamy znaleźć idealnego towarzysza.'
    },
    'pt': {
        'title': 'Comparar Raças de Cães',
        'meta_desc': 'Compare raças de cães lado a lado. Veja tamanho, nível de energia, necessidades de cuidados e mais.',
        'h1_compare': 'Comparar',
        'h1_breeds': 'Raças',
        'select_up_to': 'Selecione até 3 raças para comparar',
        'breed_1': 'Raça 1',
        'breed_2': 'Raça 2',
        'breed_3': 'Raça 3 (opcional)',
        'select_breed': 'Selecione uma raça...',
        'select_breeds': 'Selecione raças para comparar',
        'choose_at_least': 'Escolha pelo menos 2 raças dos menus acima',
        'in_depth': 'Comparações Detalhadas',
        'view_all': 'Ver Todas →',
        'quick_compare': 'Comparação Rápida',
        'compare_above': 'Comparar acima',
        'footer': '© 2026 BreedFinder. Ajudamos você a encontrar seu companheiro perfeito.'
    },
    'ru': {
        'title': 'Сравнить Породы Собак',
        'meta_desc': 'Сравните породы собак бок о бок. Смотрите размер, уровень энергии, потребности в уходе и многое другое.',
        'h1_compare': 'Сравнить',
        'h1_breeds': 'Породы',
        'select_up_to': 'Выберите до 3 пород для сравнения',
        'breed_1': 'Порода 1',
        'breed_2': 'Порода 2',
        'breed_3': 'Порода 3 (необязательно)',
        'select_breed': 'Выберите породу...',
        'select_breeds': 'Выберите породы для сравнения',
        'choose_at_least': 'Выберите хотя бы 2 породы из меню выше',
        'in_depth': 'Подробные Сравнения',
        'view_all': 'Показать Все →',
        'quick_compare': 'Быстрое Сравнение',
        'compare_above': 'Сравнить выше',
        'footer': '© 2026 BreedFinder. Помогаем найти идеального компаньона.'
    },
    'sv': {
        'title': 'Jämför Hundraser',
        'meta_desc': 'Jämför hundraser sida vid sida. Se storlek, energinivå, skötselsbehov och mer.',
        'h1_compare': 'Jämför',
        'h1_breeds': 'Raser',
        'select_up_to': 'Välj upp till 3 raser att jämföra',
        'breed_1': 'Ras 1',
        'breed_2': 'Ras 2',
        'breed_3': 'Ras 3 (valfri)',
        'select_breed': 'Välj en ras...',
        'select_breeds': 'Välj raser att jämföra',
        'choose_at_least': 'Välj minst 2 raser från dropdown-menyerna ovan',
        'in_depth': 'Djupgående Jämförelser',
        'view_all': 'Visa Alla →',
        'quick_compare': 'Snabbjämförelse',
        'compare_above': 'Jämför ovan',
        'footer': '© 2026 BreedFinder. Vi hjälper dig att hitta din perfekta följeslagare.'
    },
    'tr': {
        'title': 'Köpek Irklarını Karşılaştır',
        'meta_desc': 'Köpek ırklarını yan yana karşılaştırın. Boyut, enerji seviyesi, bakım ihtiyaçları ve daha fazlasını görün.',
        'h1_compare': 'Irkları',
        'h1_breeds': 'Karşılaştır',
        'select_up_to': 'Karşılaştırmak için en fazla 3 ırk seçin',
        'breed_1': 'Irk 1',
        'breed_2': 'Irk 2',
        'breed_3': 'Irk 3 (isteğe bağlı)',
        'select_breed': 'Bir ırk seçin...',
        'select_breeds': 'Karşılaştırmak için ırkları seçin',
        'choose_at_least': 'Yukarıdaki menülerden en az 2 ırk seçin',
        'in_depth': 'Detaylı Karşılaştırmalar',
        'view_all': 'Tümünü Gör →',
        'quick_compare': 'Hızlı Karşılaştırma',
        'compare_above': 'Yukarıda karşılaştır',
        'footer': '© 2026 BreedFinder. Mükemmel eşinizi bulmanıza yardımcı oluyoruz.'
    },
    'zh': {
        'title': '比较犬种',
        'meta_desc': '并排比较犬种。查看大小、能量水平、美容需求等。',
        'h1_compare': '比较',
        'h1_breeds': '犬种',
        'select_up_to': '最多选择3个犬种进行比较',
        'breed_1': '犬种 1',
        'breed_2': '犬种 2',
        'breed_3': '犬种 3（可选）',
        'select_breed': '选择犬种...',
        'select_breeds': '选择要比较的犬种',
        'choose_at_least': '请从上方菜单中选择至少2个犬种',
        'in_depth': '深入比较',
        'view_all': '查看全部 →',
        'quick_compare': '快速比较',
        'compare_above': '在上方比较',
        'footer': '© 2026 BreedFinder. 帮助您找到完美的伴侣。'
    }
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def fix_compare_page(lang):
    filepath = os.path.join(BASE_DIR, lang, 'compare', 'index.html')
    if not os.path.exists(filepath):
        print(f"Skipping {lang}: no compare page")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cfg = LANGS.get(lang, {})
    ui = UI.get(lang, {})
    
    if not cfg or not ui:
        print(f"Skipping {lang}: no config")
        return
    
    # Fix nav links: ../../search/ -> ../search/
    content = re.sub(r'href="\.\.\/\.\.\/search\/"', 'href="../search/"', content)
    content = re.sub(r'href="\.\.\/\.\.\/quiz"', 'href="../quiz/"', content)
    content = re.sub(r'href="\.\.\/\.\.\/quiz/"', 'href="../quiz/"', content)
    
    # Fix homepage link
    content = re.sub(r'href="\.\.\/\.\.\/"', 'href="../"', content)
    
    # Fix language dropdown: make current language selected
    # First, remove any existing 'selected' from English option
    content = re.sub(r'(<option value="\.\.\/\.\.\/compare\/")(\s+selected)(>English<)', r'\1>\3', content)
    
    # Then add selected to the current language
    lang_pattern = r'(<option value="\.\./\.\./{}\/compare\/">)({}<)'.format(lang, re.escape(cfg["name"]))
    content = re.sub(lang_pattern, r'\1 selected>' + cfg["name"] + '<', content)
    
    # Also fix: value paths should be relative to current location
    # From /fi/compare/, ../es/compare/ is correct (not ../../es/compare/)
    content = re.sub(r'value="\.\.\/\.\.\/compare\/"', 'value="../../compare/"', content)
    for l in LANGS:
        old = f'value="../../{l}/compare/"'
        new = f'value="../{l}/compare/"' if l != lang else f'value="./"'
        content = content.replace(old, new)
    
    # Fix title
    content = re.sub(r'<title>Compare Dog Breeds.*?</title>', f'<title>{ui["title"]} | BreedFinder</title>', content)
    
    # Fix meta description
    content = re.sub(r'<meta name="description" content="Compare dog breeds.*?">', f'<meta name="description" content="{ui["meta_desc"]}">', content)
    
    # Fix H1
    content = re.sub(
        r'<h1 class="text-4xl md:text-5xl font-extrabold mb-4">\s*Compare\s*<span[^>]*>Breeds</span>',
        f'<h1 class="text-4xl md:text-5xl font-extrabold mb-4">\n                {ui["h1_compare"]}\n                <span class="bg-gradient-to-r from-sky-500 to-blue-600 bg-clip-text text-transparent">{ui["h1_breeds"]}</span>',
        content
    )
    
    # Fix subtitle
    content = re.sub(r'Valitse enintään 3 rotua to compare side by side', ui['select_up_to'], content)
    content = re.sub(r'Select up to 3 breeds to compare side by side', ui['select_up_to'], content)
    
    # Fix breed labels
    content = re.sub(r'>Rotu 1<', f'>{ui["breed_1"]}<', content)
    content = re.sub(r'>Rotu 2<', f'>{ui["breed_2"]}<', content)
    content = re.sub(r'>Rotu 3 \(optional\)<', f'>{ui["breed_3"]}<', content)
    content = re.sub(r'>Breed 1<', f'>{ui["breed_1"]}<', content)
    content = re.sub(r'>Breed 2<', f'>{ui["breed_2"]}<', content)
    content = re.sub(r'>Breed 3 \(optional\)<', f'>{ui["breed_3"]}<', content)
    
    # Fix select placeholder
    content = re.sub(r'>Valitse rotu\.\.\.<', f'>{ui["select_breed"]}<', content)
    content = re.sub(r'>Select a breed\.\.\.<', f'>{ui["select_breed"]}<', content)
    
    # Fix empty state
    content = re.sub(r'>Select breeds to compare<', f'>{ui["select_breeds"]}<', content)
    content = re.sub(r'>Choose at least 2 breeds from the dropdowns above<', f'>{ui["choose_at_least"]}<', content)
    
    # Fix In-Depth Comparisons header
    content = re.sub(r'>In-Depth Comparisons<', f'>{ui["in_depth"]}<', content)
    
    # Fix View All link
    content = re.sub(r'>View All Comparisons →<', f'>{ui["view_all"]}<', content)
    content = re.sub(r'>Näytä kaikki →<', f'>{ui["view_all"]}<', content)
    
    # Fix Quick Compare header
    content = re.sub(r'>Quick Compare<', f'>{ui["quick_compare"]}<', content)
    
    # Fix "Compare above" text
    content = re.sub(r'>Vertaa yllä<', f'>{ui["compare_above"]}<', content)
    content = re.sub(r'>Compare above<', f'>{ui["compare_above"]}<', content)
    
    # Fix footer
    content = re.sub(r'>© 2026 BreedFinder\. Helping you find your perfect companion\.<', f'>{ui["footer"]}<', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed {lang}")

# Fix all languages
for lang in LANGS:
    fix_compare_page(lang)

print("\nDone!")
