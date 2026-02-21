#!/usr/bin/env python3
"""
Generate translated compare pages and comprehensive sitemap for BreedFinder
"""

import json
import os
from pathlib import Path
from datetime import datetime

# Languages (14 translations + English)
LANGUAGES = ['es', 'de', 'fr', 'it', 'pt', 'nl', 'pl', 'zh', 'ja', 'fi', 'sv', 'no', 'da', 'ru']

# Compare page translations
COMPARE_TRANSLATIONS = {
    'en': {
        'compare_title': 'Compare Breeds',
        'compare_subtitle': 'Select up to 3 breeds to compare side by side',
        'breed_1': 'Breed 1',
        'breed_2': 'Breed 2',
        'breed_3': 'Breed 3 (optional)',
        'select_breed': 'Select a breed...',
        'select_breeds_title': 'Select breeds to compare',
        'select_breeds_desc': 'Choose at least 2 breeds from the dropdowns above',
        'popular_comparisons': 'Popular Comparisons',
        'two_favorites': "Two of America's favorites",
        'compact_companions': 'Compact companions',
        'working_dog_showdown': 'Working dog showdown',
        'arctic_battle': 'Arctic breed battle',
        'lap_dog_legends': 'Lap dog legends',
        'hypoallergenic_picks': 'Hypoallergenic picks',
    },
    'es': {
        'compare_title': 'Comparar Razas',
        'compare_subtitle': 'Selecciona hasta 3 razas para comparar lado a lado',
        'breed_1': 'Raza 1',
        'breed_2': 'Raza 2',
        'breed_3': 'Raza 3 (opcional)',
        'select_breed': 'Selecciona una raza...',
        'select_breeds_title': 'Selecciona razas para comparar',
        'select_breeds_desc': 'Elige al menos 2 razas de los menús anteriores',
        'popular_comparisons': 'Comparaciones Populares',
        'two_favorites': 'Dos de los favoritos de América',
        'compact_companions': 'Compañeros compactos',
        'working_dog_showdown': 'Enfrentamiento de perros de trabajo',
        'arctic_battle': 'Batalla de razas árticas',
        'lap_dog_legends': 'Leyendas de perros falderos',
        'hypoallergenic_picks': 'Opciones hipoalergénicas',
    },
    'de': {
        'compare_title': 'Rassen Vergleichen',
        'compare_subtitle': 'Wähle bis zu 3 Rassen zum Vergleichen aus',
        'breed_1': 'Rasse 1',
        'breed_2': 'Rasse 2',
        'breed_3': 'Rasse 3 (optional)',
        'select_breed': 'Rasse auswählen...',
        'select_breeds_title': 'Rassen zum Vergleichen auswählen',
        'select_breeds_desc': 'Wähle mindestens 2 Rassen aus den Dropdowns oben',
        'popular_comparisons': 'Beliebte Vergleiche',
        'two_favorites': 'Zwei amerikanische Favoriten',
        'compact_companions': 'Kompakte Begleiter',
        'working_dog_showdown': 'Arbeitshund-Vergleich',
        'arctic_battle': 'Arktische Rassen im Duell',
        'lap_dog_legends': 'Schoßhund-Legenden',
        'hypoallergenic_picks': 'Hypoallergene Favoriten',
    },
    'fr': {
        'compare_title': 'Comparer les Races',
        'compare_subtitle': 'Sélectionnez jusqu\'à 3 races à comparer côte à côte',
        'breed_1': 'Race 1',
        'breed_2': 'Race 2',
        'breed_3': 'Race 3 (optionnel)',
        'select_breed': 'Sélectionner une race...',
        'select_breeds_title': 'Sélectionnez des races à comparer',
        'select_breeds_desc': 'Choisissez au moins 2 races dans les menus ci-dessus',
        'popular_comparisons': 'Comparaisons Populaires',
        'two_favorites': 'Deux favoris américains',
        'compact_companions': 'Compagnons compacts',
        'working_dog_showdown': 'Duel de chiens de travail',
        'arctic_battle': 'Combat de races arctiques',
        'lap_dog_legends': 'Légendes des chiens de salon',
        'hypoallergenic_picks': 'Choix hypoallergéniques',
    },
    'it': {
        'compare_title': 'Confronta Razze',
        'compare_subtitle': 'Seleziona fino a 3 razze da confrontare fianco a fianco',
        'breed_1': 'Razza 1',
        'breed_2': 'Razza 2',
        'breed_3': 'Razza 3 (opzionale)',
        'select_breed': 'Seleziona una razza...',
        'select_breeds_title': 'Seleziona razze da confrontare',
        'select_breeds_desc': 'Scegli almeno 2 razze dai menu sopra',
        'popular_comparisons': 'Confronti Popolari',
        'two_favorites': 'Due favoriti americani',
        'compact_companions': 'Compagni compatti',
        'working_dog_showdown': 'Sfida cani da lavoro',
        'arctic_battle': 'Battaglia razze artiche',
        'lap_dog_legends': 'Leggende dei cani da salotto',
        'hypoallergenic_picks': 'Scelte ipoallergeniche',
    },
    'pt': {
        'compare_title': 'Comparar Raças',
        'compare_subtitle': 'Selecione até 3 raças para comparar lado a lado',
        'breed_1': 'Raça 1',
        'breed_2': 'Raça 2',
        'breed_3': 'Raça 3 (opcional)',
        'select_breed': 'Selecionar uma raça...',
        'select_breeds_title': 'Selecione raças para comparar',
        'select_breeds_desc': 'Escolha pelo menos 2 raças nos menus acima',
        'popular_comparisons': 'Comparações Populares',
        'two_favorites': 'Dois favoritos americanos',
        'compact_companions': 'Companheiros compactos',
        'working_dog_showdown': 'Confronto de cães de trabalho',
        'arctic_battle': 'Batalha de raças árticas',
        'lap_dog_legends': 'Lendas dos cães de colo',
        'hypoallergenic_picks': 'Escolhas hipoalergênicas',
    },
    'nl': {
        'compare_title': 'Rassen Vergelijken',
        'compare_subtitle': 'Selecteer tot 3 rassen om naast elkaar te vergelijken',
        'breed_1': 'Ras 1',
        'breed_2': 'Ras 2',
        'breed_3': 'Ras 3 (optioneel)',
        'select_breed': 'Selecteer een ras...',
        'select_breeds_title': 'Selecteer rassen om te vergelijken',
        'select_breeds_desc': 'Kies minimaal 2 rassen uit de dropdowns hierboven',
        'popular_comparisons': 'Populaire Vergelijkingen',
        'two_favorites': 'Twee Amerikaanse favorieten',
        'compact_companions': 'Compacte metgezellen',
        'working_dog_showdown': 'Werkhonden-duel',
        'arctic_battle': 'Arctische rassenstrijd',
        'lap_dog_legends': 'Schoothodn-legendes',
        'hypoallergenic_picks': 'Hypoallergene keuzes',
    },
    'pl': {
        'compare_title': 'Porównaj Rasy',
        'compare_subtitle': 'Wybierz do 3 ras do porównania obok siebie',
        'breed_1': 'Rasa 1',
        'breed_2': 'Rasa 2',
        'breed_3': 'Rasa 3 (opcjonalnie)',
        'select_breed': 'Wybierz rasę...',
        'select_breeds_title': 'Wybierz rasy do porównania',
        'select_breeds_desc': 'Wybierz co najmniej 2 rasy z menu powyżej',
        'popular_comparisons': 'Popularne Porównania',
        'two_favorites': 'Dwaj amerykańscy faworyci',
        'compact_companions': 'Kompaktowi towarzysze',
        'working_dog_showdown': 'Starcie psów pracujących',
        'arctic_battle': 'Bitwa ras arktycznych',
        'lap_dog_legends': 'Legendy psów do towarzystwa',
        'hypoallergenic_picks': 'Hipoalergiczne wybory',
    },
    'zh': {
        'compare_title': '比较品种',
        'compare_subtitle': '选择最多3个品种进行并排比较',
        'breed_1': '品种 1',
        'breed_2': '品种 2',
        'breed_3': '品种 3 (可选)',
        'select_breed': '选择品种...',
        'select_breeds_title': '选择要比较的品种',
        'select_breeds_desc': '从上面的下拉菜单中选择至少2个品种',
        'popular_comparisons': '热门比较',
        'two_favorites': '美国两大最爱',
        'compact_companions': '紧凑型伙伴',
        'working_dog_showdown': '工作犬对决',
        'arctic_battle': '北极品种对战',
        'lap_dog_legends': '膝上犬传奇',
        'hypoallergenic_picks': '低过敏性选择',
    },
    'ja': {
        'compare_title': '犬種を比較',
        'compare_subtitle': '最大3犬種を選んで並べて比較',
        'breed_1': '犬種 1',
        'breed_2': '犬種 2',
        'breed_3': '犬種 3 (任意)',
        'select_breed': '犬種を選択...',
        'select_breeds_title': '比較する犬種を選択',
        'select_breeds_desc': '上のドロップダウンから少なくとも2犬種を選んでください',
        'popular_comparisons': '人気の比較',
        'two_favorites': 'アメリカの人気犬種2つ',
        'compact_companions': 'コンパクトな仲間',
        'working_dog_showdown': '使役犬対決',
        'arctic_battle': '北極犬種バトル',
        'lap_dog_legends': '愛玩犬の伝説',
        'hypoallergenic_picks': '低アレルゲン犬種',
    },
    'fi': {
        'compare_title': 'Vertaa Rotuja',
        'compare_subtitle': 'Valitse enintään 3 rotua vertailtavaksi vierekkäin',
        'breed_1': 'Rotu 1',
        'breed_2': 'Rotu 2',
        'breed_3': 'Rotu 3 (valinnainen)',
        'select_breed': 'Valitse rotu...',
        'select_breeds_title': 'Valitse rodut vertailtavaksi',
        'select_breeds_desc': 'Valitse vähintään 2 rotua yllä olevista valikoista',
        'popular_comparisons': 'Suositut Vertailut',
        'two_favorites': 'Kaksi amerikkalaista suosikkia',
        'compact_companions': 'Kompaktit kumppanit',
        'working_dog_showdown': 'Työkoirien ottelu',
        'arctic_battle': 'Arktisten rotujen taisto',
        'lap_dog_legends': 'Sylittävien legendat',
        'hypoallergenic_picks': 'Allergiavapaatt valinnat',
    },
    'sv': {
        'compare_title': 'Jämför Raser',
        'compare_subtitle': 'Välj upp till 3 raser att jämföra sida vid sida',
        'breed_1': 'Ras 1',
        'breed_2': 'Ras 2',
        'breed_3': 'Ras 3 (valfritt)',
        'select_breed': 'Välj en ras...',
        'select_breeds_title': 'Välj raser att jämföra',
        'select_breeds_desc': 'Välj minst 2 raser från rullgardinsmenyerna ovan',
        'popular_comparisons': 'Populära Jämförelser',
        'two_favorites': 'Två amerikanska favoriter',
        'compact_companions': 'Kompakta sällskap',
        'working_dog_showdown': 'Arbetshundarnas duell',
        'arctic_battle': 'Arktiska rasers strid',
        'lap_dog_legends': 'Knähundarnas legender',
        'hypoallergenic_picks': 'Hypoallergena val',
    },
    'no': {
        'compare_title': 'Sammenlign Raser',
        'compare_subtitle': 'Velg opptil 3 raser å sammenligne side om side',
        'breed_1': 'Rase 1',
        'breed_2': 'Rase 2',
        'breed_3': 'Rase 3 (valgfritt)',
        'select_breed': 'Velg en rase...',
        'select_breeds_title': 'Velg raser å sammenligne',
        'select_breeds_desc': 'Velg minst 2 raser fra nedtrekksmenyene over',
        'popular_comparisons': 'Populære Sammenligninger',
        'two_favorites': 'To amerikanske favoritter',
        'compact_companions': 'Kompakte følgesvenner',
        'working_dog_showdown': 'Arbeidshundenes duell',
        'arctic_battle': 'Arktiske rasers kamp',
        'lap_dog_legends': 'Fanghundenes legender',
        'hypoallergenic_picks': 'Hypoallergene valg',
    },
    'da': {
        'compare_title': 'Sammenlign Racer',
        'compare_subtitle': 'Vælg op til 3 racer at sammenligne side om side',
        'breed_1': 'Race 1',
        'breed_2': 'Race 2',
        'breed_3': 'Race 3 (valgfrit)',
        'select_breed': 'Vælg en race...',
        'select_breeds_title': 'Vælg racer at sammenligne',
        'select_breeds_desc': 'Vælg mindst 2 racer fra dropdown-menuerne ovenfor',
        'popular_comparisons': 'Populære Sammenligninger',
        'two_favorites': 'To amerikanske favoritter',
        'compact_companions': 'Kompakte ledsagere',
        'working_dog_showdown': 'Arbejdshundes duel',
        'arctic_battle': 'Arktiske racers kamp',
        'lap_dog_legends': 'Skødehundes legender',
        'hypoallergenic_picks': 'Hypoallergene valg',
    },
    'ru': {
        'compare_title': 'Сравнить Породы',
        'compare_subtitle': 'Выберите до 3 пород для сравнения бок о бок',
        'breed_1': 'Порода 1',
        'breed_2': 'Порода 2',
        'breed_3': 'Порода 3 (опционально)',
        'select_breed': 'Выберите породу...',
        'select_breeds_title': 'Выберите породы для сравнения',
        'select_breeds_desc': 'Выберите минимум 2 породы из выпадающих списков выше',
        'popular_comparisons': 'Популярные Сравнения',
        'two_favorites': 'Два американских фаворита',
        'compact_companions': 'Компактные компаньоны',
        'working_dog_showdown': 'Поединок рабочих собак',
        'arctic_battle': 'Битва арктических пород',
        'lap_dog_legends': 'Легенды декоративных собак',
        'hypoallergenic_picks': 'Гипоаллергенные варианты',
    },
}

def get_lang_name(lang):
    names = {
        'en': 'English', 'es': 'Español', 'de': 'Deutsch', 'fr': 'Français',
        'it': 'Italiano', 'pt': 'Português', 'nl': 'Nederlands', 'pl': 'Polski',
        'zh': '中文', 'ja': '日本語', 'fi': 'Suomi', 'sv': 'Svenska',
        'no': 'Norsk', 'da': 'Dansk', 'ru': 'Русский'
    }
    return names.get(lang, lang.upper())

def generate_compare_page(lang, base_dir):
    """Generate compare page for a specific language"""
    t = COMPARE_TRANSLATIONS.get(lang, COMPARE_TRANSLATIONS['en'])
    
    # Determine paths based on language
    if lang == 'en':
        return  # English page already exists
    
    output_dir = base_dir / lang / 'compare'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate hreflang tags
    hreflang_tags = ['<link rel="alternate" hreflang="en" href="https://breedfinder.org/compare/">']
    for l in LANGUAGES:
        hreflang_tags.append(f'<link rel="alternate" hreflang="{l}" href="https://breedfinder.org/{l}/compare/">')
    hreflang_tags.append(f'<link rel="alternate" hreflang="x-default" href="https://breedfinder.org/compare/">')
    hreflang_html = '\n    '.join(hreflang_tags)
    
    # Language selector options
    lang_options = [f'<option value="../../compare/">English</option>']
    for l in LANGUAGES:
        selected = 'selected' if l == lang else ''
        lang_options.append(f'<option value="../{l}/compare/" {selected}>{get_lang_name(l)}</option>')
    lang_selector_html = '\n                        '.join(lang_options)
    
    html = f'''<!DOCTYPE html>
<html lang="{lang}" class="">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{t['compare_title']} | BreedFinder</title>
    <meta name="description" content="{t['compare_subtitle']}">
    <link rel="canonical" href="https://breedfinder.org/{lang}/compare/">
    
    {hreflang_html}
    
    <link rel="icon" href="../../favicon.ico" type="image/x-icon">
    <link rel="icon" type="image/png" sizes="32x32" href="../../favicon-32.png">
    <link rel="apple-touch-icon" sizes="180x180" href="../../apple-touch-icon.png">
    
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://breedfinder.org/{lang}/compare/">
    <meta property="og:title" content="{t['compare_title']}">
    <meta property="og:description" content="{t['compare_subtitle']}">
    <meta property="og:site_name" content="BreedFinder">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    </style>

    <style>
        .dark {{ color-scheme: dark; }}
        .dark body {{ background: linear-gradient(to bottom, #0f172a, #1e293b); color: #e2e8f0; }}
        .dark header {{ background: rgba(15, 23, 42, 0.8); border-color: rgba(51, 65, 85, 0.5); }}
        .dark .bg-white {{ background: #1e293b !important; }}
        .dark .bg-white\\/80 {{ background: rgba(30, 41, 59, 0.8) !important; }}
        .dark .text-slate-800, .dark .text-slate-900 {{ color: #f1f5f9 !important; }}
        .dark .text-slate-600, .dark .text-slate-500 {{ color: #94a3b8 !important; }}
        .dark .border-slate-100, .dark .border-slate-200 {{ border-color: #334155 !important; }}
        .dark .bg-slate-50, .dark .bg-slate-100 {{ background: #334155 !important; }}
        .dark .card-shadow {{ box-shadow: 0 4px 12px rgba(0,0,0,0.3); }}
        .dark input, .dark select {{ background: #1e293b; color: #f1f5f9; border-color: #475569; }}
    </style>
</head>
<body class="bg-gradient-to-br from-sky-50 via-white to-violet-50 min-h-screen text-slate-800">
    <!-- Header -->
    <header class="bg-white/80 backdrop-blur-md border-b border-slate-100 sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
            <a href="../" class="flex items-center gap-3">
                <div class="w-10 h-10 bg-gradient-to-br from-sky-500 to-violet-500 rounded-xl flex items-center justify-center text-white shadow-lg shadow-sky-500/20">
                    <img src="../../logo-192.png" class="w-10 h-10" alt="BreedFinder">
                </div>
                <span class="text-xl font-bold bg-gradient-to-r from-slate-800 to-slate-600 bg-clip-text text-transparent">BreedFinder</span>
            </a>
            <nav class="flex items-center gap-4 text-sm font-medium">
                <a href="../search/" class="text-slate-600 hover:text-sky-600 transition hidden md:inline">All Breeds</a>
                <div class="relative">
                    <select onchange="if(this.value) window.location.href=this.value" class="appearance-none bg-transparent border border-slate-200 rounded-lg px-3 py-2 pr-8 text-sm cursor-pointer hover:border-sky-400 focus:outline-none focus:border-sky-400">
                        {lang_selector_html}
                    </select>
                    <svg class="w-4 h-4 absolute right-2 top-1/2 -translate-y-1/2 text-slate-400 pointer-events-none" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                </div>
                <button onclick="toggleDark()" class="p-2 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-700 transition" title="Toggle dark mode">
                    <svg class="w-5 h-5 text-slate-600 hidden dark:block" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                    <svg class="w-5 h-5 text-slate-600 dark:hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
                </button>
                <a href="../quiz/" class="bg-gradient-to-r from-sky-500 to-violet-500 text-white px-5 py-2.5 rounded-xl font-semibold hover:shadow-lg hover:shadow-sky-500/25 transition hidden md:inline">Take Quiz</a>
            </nav>
        </div>
    </header>

    <main class="max-w-6xl mx-auto px-4 py-12">
        <!-- Header -->
        <div class="text-center mb-10">
            <h1 class="text-4xl md:text-5xl font-extrabold mb-4">
                {t['compare_title'].split()[0]}
                <span class="bg-gradient-to-r from-sky-500 to-violet-500 bg-clip-text text-transparent">{' '.join(t['compare_title'].split()[1:]) if len(t['compare_title'].split()) > 1 else ''}</span>
            </h1>
            <p class="text-lg text-slate-600">{t['compare_subtitle']}</p>
        </div>

        <!-- Breed Selectors -->
        <div class="grid md:grid-cols-3 gap-4 mb-10">
            <div>
                <label class="block text-sm font-medium text-slate-600 mb-2">{t['breed_1']}</label>
                <select id="breed1" onchange="updateComparison()" class="w-full p-3 rounded-xl border-2 border-slate-200 focus:border-sky-400 focus:outline-none bg-white">
                    <option value="">{t['select_breed']}</option>
                </select>
            </div>
            <div>
                <label class="block text-sm font-medium text-slate-600 mb-2">{t['breed_2']}</label>
                <select id="breed2" onchange="updateComparison()" class="w-full p-3 rounded-xl border-2 border-slate-200 focus:border-sky-400 focus:outline-none bg-white">
                    <option value="">{t['select_breed']}</option>
                </select>
            </div>
            <div>
                <label class="block text-sm font-medium text-slate-600 mb-2">{t['breed_3']}</label>
                <select id="breed3" onchange="updateComparison()" class="w-full p-3 rounded-xl border-2 border-slate-200 focus:border-sky-400 focus:outline-none bg-white">
                    <option value="">{t['select_breed']}</option>
                </select>
            </div>
        </div>

        <!-- Comparison Table -->
        <div id="comparison-container" class="hidden">
            <div class="bg-white rounded-3xl shadow-xl shadow-slate-200/50 overflow-hidden">
                <table class="w-full">
                    <thead id="comparison-header">
                    </thead>
                    <tbody id="comparison-body">
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Empty State -->
        <div id="empty-state" class="text-center py-20">
            <div class="text-6xl mb-4">🐕</div>
            <h3 class="text-xl font-bold text-slate-700 mb-2">{t['select_breeds_title']}</h3>
            <p class="text-slate-500">{t['select_breeds_desc']}</p>
        </div>

        <!-- Popular Comparisons -->
        <div class="mt-16">
            <h2 class="text-2xl font-bold mb-6">{t['popular_comparisons']}</h2>
            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
                <button onclick="setBreeds('labrador-retriever', 'golden-retriever')" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md transition text-left">
                    <span class="font-semibold">Labrador vs Golden Retriever</span>
                    <p class="text-sm text-slate-500">{t['two_favorites']}</p>
                </button>
                <button onclick="setBreeds('french-bulldog', 'bulldog')" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md transition text-left">
                    <span class="font-semibold">French Bulldog vs Bulldog</span>
                    <p class="text-sm text-slate-500">{t['compact_companions']}</p>
                </button>
                <button onclick="setBreeds('german-shepherd', 'belgian-malinois')" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md transition text-left">
                    <span class="font-semibold">German Shepherd vs Malinois</span>
                    <p class="text-sm text-slate-500">{t['working_dog_showdown']}</p>
                </button>
                <button onclick="setBreeds('siberian-husky', 'alaskan-malamute')" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md transition text-left">
                    <span class="font-semibold">Husky vs Malamute</span>
                    <p class="text-sm text-slate-500">{t['arctic_battle']}</p>
                </button>
                <button onclick="setBreeds('shih-tzu', 'maltese')" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md transition text-left">
                    <span class="font-semibold">Shih Tzu vs Maltese</span>
                    <p class="text-sm text-slate-500">{t['lap_dog_legends']}</p>
                </button>
                <button onclick="setBreeds('poodle', 'bichon-frise')" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md transition text-left">
                    <span class="font-semibold">Poodle vs Bichon Frise</span>
                    <p class="text-sm text-slate-500">{t['hypoallergenic_picks']}</p>
                </button>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="border-t border-slate-100 mt-16 py-8">
        <div class="max-w-6xl mx-auto px-4 text-center text-slate-500 text-sm">
            <p>© 2026 BreedFinder. Helping you find your perfect companion.</p>
        </div>
    </footer>

    <script src="../../data/breeds-compare.js"></script>
    <script>
        // Dark mode toggle
        function toggleDark() {{
            document.documentElement.classList.toggle('dark');
            localStorage.setItem('darkMode', document.documentElement.classList.contains('dark'));
        }}
        
        if (localStorage.getItem('darkMode') === 'true') {{
            document.documentElement.classList.add('dark');
        }}
        
        // Populate breed selectors
        const selects = ['breed1', 'breed2', 'breed3'];
        selects.forEach(id => {{
            const select = document.getElementById(id);
            breeds.forEach(breed => {{
                const option = document.createElement('option');
                option.value = breed.slug;
                option.textContent = breed.name;
                select.appendChild(option);
            }});
        }});
        
        function setBreeds(slug1, slug2) {{
            document.getElementById('breed1').value = slug1;
            document.getElementById('breed2').value = slug2;
            document.getElementById('breed3').value = '';
            updateComparison();
        }}
        
        function updateComparison() {{
            const selected = selects
                .map(id => document.getElementById(id).value)
                .filter(v => v)
                .map(slug => breeds.find(b => b.slug === slug))
                .filter(b => b);
            
            if (selected.length < 2) {{
                document.getElementById('comparison-container').classList.add('hidden');
                document.getElementById('empty-state').classList.remove('hidden');
                return;
            }}
            
            document.getElementById('comparison-container').classList.remove('hidden');
            document.getElementById('empty-state').classList.add('hidden');
            
            // Build header
            const header = document.getElementById('comparison-header');
            header.innerHTML = `
                <tr class="bg-gradient-to-r from-sky-500 to-violet-500 text-white">
                    <th class="p-4 text-left font-semibold">Attribute</th>
                    ${{selected.map(b => `
                        <th class="p-4 text-center">
                            <img src="${{b.image}}" alt="${{b.name}}" class="w-16 h-16 rounded-full mx-auto mb-2 object-cover bg-white">
                            <div class="font-bold">${{b.name}}</div>
                        </th>
                    `).join('')}}
                </tr>
            `;
            
            // Build comparison rows
            const attrs = [
                ['Size', 'size'],
                ['Height', 'height'],
                ['Weight', 'weight'],
                ['Lifespan', 'lifespan'],
                ['Origin', 'origin'],
                ['Energy', 'energy', true],
                ['Grooming', 'grooming', true],
                ['Trainability', 'trainability', true],
                ['Kid Friendly', 'kidFriendly', true],
                ['Apartment', 'apartment', true],
            ];
            
            const body = document.getElementById('comparison-body');
            body.innerHTML = attrs.map(([label, key, isRating], i) => `
                <tr class="${{i % 2 === 0 ? 'bg-slate-50' : 'bg-white'}}">
                    <td class="p-4 font-medium text-slate-700">${{label}}</td>
                    ${{selected.map(b => `
                        <td class="p-4 text-center">
                            ${{isRating ? `
                                <div class="flex justify-center gap-0.5">
                                    ${{[1,2,3,4,5].map(n => `
                                        <div class="w-2 h-6 rounded-full ${{n <= b[key] ? 'bg-gradient-to-t from-sky-500 to-violet-500' : 'bg-slate-200'}}"></div>
                                    `).join('')}}
                                </div>
                            ` : b[key]}}
                        </td>
                    `).join('')}}
                </tr>
            `).join('');
        }}
    </script>
</body>
</html>'''
    
    with open(output_dir / 'index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"  Created {lang}/compare/index.html")


def generate_sitemap(base_dir):
    """Generate comprehensive sitemap with all pages"""
    
    # Load breeds
    breeds_file = base_dir / 'data' / 'breeds.json'
    with open(breeds_file, 'r', encoding='utf-8') as f:
        breeds = json.load(f)
    
    breed_slugs = [b.get('id', b.get('slug', '')) for b in breeds]
    
    urls = []
    
    # Main pages
    main_pages = [
        ('/', '1.0', 'weekly'),
        ('/breeds/', '0.9', 'weekly'),
        ('/quiz/', '0.8', 'monthly'),
        ('/compare/', '0.8', 'monthly'),
        ('/about/', '0.6', 'monthly'),
        ('/articles/', '0.8', 'weekly'),
    ]
    
    for path, priority, freq in main_pages:
        urls.append(f'  <url><loc>https://breedfinder.org{path}</loc><changefreq>{freq}</changefreq><priority>{priority}</priority></url>')
    
    # English breed pages
    for slug in breed_slugs:
        urls.append(f'  <url><loc>https://breedfinder.org/breeds/{slug}</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>')
    
    # Articles
    articles = [
        'best-dogs-for-apartments',
        'best-dogs-for-families',
        'low-shedding-dogs',
    ]
    for article in articles:
        urls.append(f'  <url><loc>https://breedfinder.org/articles/{article}/</loc><changefreq>monthly</changefreq><priority>0.8</priority></url>')
    
    # Language pages
    for lang in LANGUAGES:
        # Homepage
        urls.append(f'  <url><loc>https://breedfinder.org/{lang}/</loc><changefreq>weekly</changefreq><priority>0.9</priority></url>')
        # Search/Browse
        urls.append(f'  <url><loc>https://breedfinder.org/{lang}/search/</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>')
        # Quiz
        urls.append(f'  <url><loc>https://breedfinder.org/{lang}/quiz/</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>')
        # Compare
        urls.append(f'  <url><loc>https://breedfinder.org/{lang}/compare/</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>')
        # Breed pages
        for slug in breed_slugs:
            urls.append(f'  <url><loc>https://breedfinder.org/{lang}/breeds/{slug}</loc><changefreq>monthly</changefreq><priority>0.6</priority></url>')
    
    sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>'''
    
    with open(base_dir / 'sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
    
    print(f"\nSitemap generated with {len(urls)} URLs")
    return len(urls)


def main():
    base_dir = Path(__file__).parent.parent
    
    print("Generating translated compare pages...")
    for lang in LANGUAGES:
        generate_compare_page(lang, base_dir)
    
    print("\nGenerating comprehensive sitemap...")
    total_urls = generate_sitemap(base_dir)
    
    print(f"\n✅ Done!")
    print(f"   - {len(LANGUAGES)} compare pages created")
    print(f"   - {total_urls} URLs in sitemap")


if __name__ == '__main__':
    main()
