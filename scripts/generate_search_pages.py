#!/usr/bin/env python3
"""
Generate translated search pages with full filters for BreedFinder
"""

import json
from pathlib import Path

LANGUAGES = {
    'es': {'name': 'Español', 'code': 'ES'},
    'de': {'name': 'Deutsch', 'code': 'DE'},
    'fr': {'name': 'Français', 'code': 'FR'},
    'it': {'name': 'Italiano', 'code': 'IT'},
    'pt': {'name': 'Português', 'code': 'PT'},
    'nl': {'name': 'Nederlands', 'code': 'NL'},
    'pl': {'name': 'Polski', 'code': 'PL'},
    'zh': {'name': '中文', 'code': 'ZH'},
    'ja': {'name': '日本語', 'code': 'JA'},
    'fi': {'name': 'Suomi', 'code': 'FI'},
    'sv': {'name': 'Svenska', 'code': 'SV'},
    'no': {'name': 'Norsk', 'code': 'NO'},
    'da': {'name': 'Dansk', 'code': 'DA'},
    'ru': {'name': 'Русский', 'code': 'RU'},
}

TRANSLATIONS = {
    'en': {
        'title': 'Browse Breeds',
        'page_title': 'Find Your Perfect Dog Breed',
        'page_subtitle': 'Filter by size, energy level, grooming needs & more',
        'search_placeholder': 'Search breeds... (e.g. Golden Retriever, small, friendly)',
        'filters': 'Filters',
        'reset': 'Reset',
        'size': 'Size',
        'tiny': 'Tiny',
        'small': 'Small',
        'medium': 'Medium',
        'large': 'Large',
        'giant': 'Giant',
        'energy_level': 'Energy Level',
        'low': 'Low',
        'high': 'High',
        'grooming_needs': 'Grooming Needs',
        'trainability': 'Trainability',
        'barking_level': 'Barking Level',
        'quiet': 'Quiet',
        'vocal': 'Vocal',
        'good_for': 'Good For',
        'kids': 'Kids',
        'apartments': 'Apartments',
        'shedding': 'Shedding',
        'minimal': 'Minimal',
        'moderate': 'Moderate',
        'heavy': 'Heavy',
        'breeds_found': 'breeds found',
        'sort_by_name': 'Sort by Name',
        'sort_by_size': 'Sort by Size',
        'sort_by_energy': 'Sort by Energy',
        'sort_by_trainability': 'Sort by Trainability',
        'no_breeds_found': 'No breeds found',
        'try_adjusting': 'Try adjusting your filters or search terms',
        'home': 'Home',
        'browse_breeds': 'Browse Breeds',
        'quiz': 'Quiz',
        'compare': 'Compare',
        'or_less': 'or less',
    },
    'fi': {
        'title': 'Selaa Rotuja',
        'page_title': 'Löydä Täydellinen Koirarotusi',
        'page_subtitle': 'Suodata koon, energiatason, turkinhoitotarpeen ja muiden mukaan',
        'search_placeholder': 'Etsi rotuja... (esim. kultainennoutaja, pieni, ystävällinen)',
        'filters': 'Suodattimet',
        'reset': 'Nollaa',
        'size': 'Koko',
        'tiny': 'Pienoinen',
        'small': 'Pieni',
        'medium': 'Keskikokoinen',
        'large': 'Suuri',
        'giant': 'Jättiläinen',
        'energy_level': 'Energiataso',
        'low': 'Matala',
        'high': 'Korkea',
        'grooming_needs': 'Turkinhoitotarve',
        'trainability': 'Koulutettavuus',
        'barking_level': 'Haukkumistaso',
        'quiet': 'Hiljainen',
        'vocal': 'Äänekäs',
        'good_for': 'Sopii',
        'kids': 'Lapset',
        'apartments': 'Kerrostalot',
        'shedding': 'Karvanlähtö',
        'minimal': 'Vähäinen',
        'moderate': 'Kohtalainen',
        'heavy': 'Runsas',
        'breeds_found': 'rotua löydetty',
        'sort_by_name': 'Järjestä nimen mukaan',
        'sort_by_size': 'Järjestä koon mukaan',
        'sort_by_energy': 'Järjestä energian mukaan',
        'sort_by_trainability': 'Järjestä koulutettavuuden mukaan',
        'no_breeds_found': 'Rotuja ei löytynyt',
        'try_adjusting': 'Kokeile muuttaa suodattimia tai hakusanoja',
        'home': 'Etusivu',
        'browse_breeds': 'Selaa Rotuja',
        'quiz': 'Testi',
        'compare': 'Vertaile',
        'or_less': 'tai vähemmän',
    },
    'de': {
        'title': 'Rassen Durchsuchen',
        'page_title': 'Finde Deine Perfekte Hunderasse',
        'page_subtitle': 'Filtern nach Größe, Energielevel, Pflegebedarf & mehr',
        'search_placeholder': 'Rassen suchen... (z.B. Golden Retriever, klein, freundlich)',
        'filters': 'Filter',
        'reset': 'Zurücksetzen',
        'size': 'Größe',
        'tiny': 'Winzig',
        'small': 'Klein',
        'medium': 'Mittel',
        'large': 'Groß',
        'giant': 'Riesig',
        'energy_level': 'Energielevel',
        'low': 'Niedrig',
        'high': 'Hoch',
        'grooming_needs': 'Pflegebedarf',
        'trainability': 'Trainierbarkeit',
        'barking_level': 'Bellverhalten',
        'quiet': 'Ruhig',
        'vocal': 'Laut',
        'good_for': 'Geeignet für',
        'kids': 'Kinder',
        'apartments': 'Wohnungen',
        'shedding': 'Haarausfall',
        'minimal': 'Minimal',
        'moderate': 'Mäßig',
        'heavy': 'Stark',
        'breeds_found': 'Rassen gefunden',
        'sort_by_name': 'Nach Name',
        'sort_by_size': 'Nach Größe',
        'sort_by_energy': 'Nach Energie',
        'sort_by_trainability': 'Nach Trainierbarkeit',
        'no_breeds_found': 'Keine Rassen gefunden',
        'try_adjusting': 'Versuche die Filter oder Suchbegriffe anzupassen',
        'home': 'Startseite',
        'browse_breeds': 'Rassen Durchsuchen',
        'quiz': 'Quiz',
        'compare': 'Vergleichen',
        'or_less': 'oder weniger',
    },
    'es': {
        'title': 'Ver Razas',
        'page_title': 'Encuentra Tu Raza de Perro Perfecta',
        'page_subtitle': 'Filtra por tamaño, nivel de energía, necesidades de aseo y más',
        'search_placeholder': 'Buscar razas... (ej. Golden Retriever, pequeño, amigable)',
        'filters': 'Filtros',
        'reset': 'Reiniciar',
        'size': 'Tamaño',
        'tiny': 'Miniatura',
        'small': 'Pequeño',
        'medium': 'Mediano',
        'large': 'Grande',
        'giant': 'Gigante',
        'energy_level': 'Nivel de Energía',
        'low': 'Bajo',
        'high': 'Alto',
        'grooming_needs': 'Necesidades de Aseo',
        'trainability': 'Entrenabilidad',
        'barking_level': 'Nivel de Ladrido',
        'quiet': 'Silencioso',
        'vocal': 'Ruidoso',
        'good_for': 'Bueno Para',
        'kids': 'Niños',
        'apartments': 'Apartamentos',
        'shedding': 'Caída de Pelo',
        'minimal': 'Mínima',
        'moderate': 'Moderada',
        'heavy': 'Abundante',
        'breeds_found': 'razas encontradas',
        'sort_by_name': 'Por Nombre',
        'sort_by_size': 'Por Tamaño',
        'sort_by_energy': 'Por Energía',
        'sort_by_trainability': 'Por Entrenabilidad',
        'no_breeds_found': 'No se encontraron razas',
        'try_adjusting': 'Intenta ajustar los filtros o términos de búsqueda',
        'home': 'Inicio',
        'browse_breeds': 'Ver Razas',
        'quiz': 'Quiz',
        'compare': 'Comparar',
        'or_less': 'o menos',
    },
    'fr': {
        'title': 'Parcourir les Races',
        'page_title': 'Trouvez Votre Race de Chien Parfaite',
        'page_subtitle': 'Filtrer par taille, niveau d\'énergie, besoins de toilettage et plus',
        'search_placeholder': 'Rechercher des races... (ex. Golden Retriever, petit, amical)',
        'filters': 'Filtres',
        'reset': 'Réinitialiser',
        'size': 'Taille',
        'tiny': 'Minuscule',
        'small': 'Petit',
        'medium': 'Moyen',
        'large': 'Grand',
        'giant': 'Géant',
        'energy_level': 'Niveau d\'Énergie',
        'low': 'Faible',
        'high': 'Élevé',
        'grooming_needs': 'Besoins de Toilettage',
        'trainability': 'Capacité d\'Entraînement',
        'barking_level': 'Niveau d\'Aboiement',
        'quiet': 'Calme',
        'vocal': 'Bruyant',
        'good_for': 'Bon Pour',
        'kids': 'Enfants',
        'apartments': 'Appartements',
        'shedding': 'Perte de Poils',
        'minimal': 'Minimale',
        'moderate': 'Modérée',
        'heavy': 'Importante',
        'breeds_found': 'races trouvées',
        'sort_by_name': 'Par Nom',
        'sort_by_size': 'Par Taille',
        'sort_by_energy': 'Par Énergie',
        'sort_by_trainability': 'Par Entraînabilité',
        'no_breeds_found': 'Aucune race trouvée',
        'try_adjusting': 'Essayez d\'ajuster les filtres ou les termes de recherche',
        'home': 'Accueil',
        'browse_breeds': 'Parcourir les Races',
        'quiz': 'Quiz',
        'compare': 'Comparer',
        'or_less': 'ou moins',
    },
    'it': {
        'title': 'Esplora le Razze',
        'page_title': 'Trova la Tua Razza di Cane Perfetta',
        'page_subtitle': 'Filtra per taglia, livello di energia, esigenze di toelettatura e altro',
        'search_placeholder': 'Cerca razze... (es. Golden Retriever, piccolo, amichevole)',
        'filters': 'Filtri',
        'reset': 'Reimposta',
        'size': 'Taglia',
        'tiny': 'Minuscolo',
        'small': 'Piccolo',
        'medium': 'Medio',
        'large': 'Grande',
        'giant': 'Gigante',
        'energy_level': 'Livello di Energia',
        'low': 'Basso',
        'high': 'Alto',
        'grooming_needs': 'Esigenze di Toelettatura',
        'trainability': 'Addestrabilità',
        'barking_level': 'Livello di Abbaiamento',
        'quiet': 'Silenzioso',
        'vocal': 'Rumoroso',
        'good_for': 'Adatto a',
        'kids': 'Bambini',
        'apartments': 'Appartamenti',
        'shedding': 'Perdita di Pelo',
        'minimal': 'Minima',
        'moderate': 'Moderata',
        'heavy': 'Abbondante',
        'breeds_found': 'razze trovate',
        'sort_by_name': 'Per Nome',
        'sort_by_size': 'Per Taglia',
        'sort_by_energy': 'Per Energia',
        'sort_by_trainability': 'Per Addestrabilità',
        'no_breeds_found': 'Nessuna razza trovata',
        'try_adjusting': 'Prova a modificare i filtri o i termini di ricerca',
        'home': 'Home',
        'browse_breeds': 'Esplora le Razze',
        'quiz': 'Quiz',
        'compare': 'Confronta',
        'or_less': 'o meno',
    },
    'pt': {
        'title': 'Ver Raças',
        'page_title': 'Encontre Sua Raça de Cachorro Perfeita',
        'page_subtitle': 'Filtre por tamanho, nível de energia, necessidades de higiene e mais',
        'search_placeholder': 'Buscar raças... (ex. Golden Retriever, pequeno, amigável)',
        'filters': 'Filtros',
        'reset': 'Resetar',
        'size': 'Tamanho',
        'tiny': 'Minúsculo',
        'small': 'Pequeno',
        'medium': 'Médio',
        'large': 'Grande',
        'giant': 'Gigante',
        'energy_level': 'Nível de Energia',
        'low': 'Baixo',
        'high': 'Alto',
        'grooming_needs': 'Necessidades de Higiene',
        'trainability': 'Treinabilidade',
        'barking_level': 'Nível de Latido',
        'quiet': 'Silencioso',
        'vocal': 'Barulhento',
        'good_for': 'Bom Para',
        'kids': 'Crianças',
        'apartments': 'Apartamentos',
        'shedding': 'Queda de Pelo',
        'minimal': 'Mínima',
        'moderate': 'Moderada',
        'heavy': 'Intensa',
        'breeds_found': 'raças encontradas',
        'sort_by_name': 'Por Nome',
        'sort_by_size': 'Por Tamanho',
        'sort_by_energy': 'Por Energia',
        'sort_by_trainability': 'Por Treinabilidade',
        'no_breeds_found': 'Nenhuma raça encontrada',
        'try_adjusting': 'Tente ajustar os filtros ou termos de busca',
        'home': 'Início',
        'browse_breeds': 'Ver Raças',
        'quiz': 'Quiz',
        'compare': 'Comparar',
        'or_less': 'ou menos',
    },
    'nl': {
        'title': 'Bekijk Rassen',
        'page_title': 'Vind Jouw Perfecte Hondenras',
        'page_subtitle': 'Filter op grootte, energieniveau, verzorgingsbehoeften en meer',
        'search_placeholder': 'Zoek rassen... (bijv. Golden Retriever, klein, vriendelijk)',
        'filters': 'Filters',
        'reset': 'Reset',
        'size': 'Grootte',
        'tiny': 'Mini',
        'small': 'Klein',
        'medium': 'Middelgroot',
        'large': 'Groot',
        'giant': 'Reus',
        'energy_level': 'Energieniveau',
        'low': 'Laag',
        'high': 'Hoog',
        'grooming_needs': 'Verzorgingsbehoeften',
        'trainability': 'Trainbaarheid',
        'barking_level': 'Blaffen',
        'quiet': 'Stil',
        'vocal': 'Luid',
        'good_for': 'Geschikt voor',
        'kids': 'Kinderen',
        'apartments': 'Appartementen',
        'shedding': 'Haaruitval',
        'minimal': 'Minimaal',
        'moderate': 'Matig',
        'heavy': 'Veel',
        'breeds_found': 'rassen gevonden',
        'sort_by_name': 'Op Naam',
        'sort_by_size': 'Op Grootte',
        'sort_by_energy': 'Op Energie',
        'sort_by_trainability': 'Op Trainbaarheid',
        'no_breeds_found': 'Geen rassen gevonden',
        'try_adjusting': 'Probeer de filters of zoektermen aan te passen',
        'home': 'Home',
        'browse_breeds': 'Bekijk Rassen',
        'quiz': 'Quiz',
        'compare': 'Vergelijken',
        'or_less': 'of minder',
    },
    'pl': {
        'title': 'Przeglądaj Rasy',
        'page_title': 'Znajdź Swoją Idealną Rasę Psa',
        'page_subtitle': 'Filtruj według rozmiaru, poziomu energii, potrzeb pielęgnacyjnych i więcej',
        'search_placeholder': 'Szukaj ras... (np. Golden Retriever, mały, przyjazny)',
        'filters': 'Filtry',
        'reset': 'Resetuj',
        'size': 'Rozmiar',
        'tiny': 'Miniaturowy',
        'small': 'Mały',
        'medium': 'Średni',
        'large': 'Duży',
        'giant': 'Olbrzymi',
        'energy_level': 'Poziom Energii',
        'low': 'Niski',
        'high': 'Wysoki',
        'grooming_needs': 'Potrzeby Pielęgnacyjne',
        'trainability': 'Łatwość Szkolenia',
        'barking_level': 'Poziom Szczekania',
        'quiet': 'Cichy',
        'vocal': 'Głośny',
        'good_for': 'Dobry dla',
        'kids': 'Dzieci',
        'apartments': 'Mieszkania',
        'shedding': 'Linienie',
        'minimal': 'Minimalne',
        'moderate': 'Umiarkowane',
        'heavy': 'Intensywne',
        'breeds_found': 'ras znaleziono',
        'sort_by_name': 'Wg Nazwy',
        'sort_by_size': 'Wg Rozmiaru',
        'sort_by_energy': 'Wg Energii',
        'sort_by_trainability': 'Wg Szkolenia',
        'no_breeds_found': 'Nie znaleziono ras',
        'try_adjusting': 'Spróbuj dostosować filtry lub hasła wyszukiwania',
        'home': 'Strona główna',
        'browse_breeds': 'Przeglądaj Rasy',
        'quiz': 'Quiz',
        'compare': 'Porównaj',
        'or_less': 'lub mniej',
    },
    'zh': {
        'title': '浏览品种',
        'page_title': '找到您完美的狗品种',
        'page_subtitle': '按体型、活力水平、美容需求等筛选',
        'search_placeholder': '搜索品种... (如 金毛, 小型, 友好)',
        'filters': '筛选',
        'reset': '重置',
        'size': '体型',
        'tiny': '迷你',
        'small': '小型',
        'medium': '中型',
        'large': '大型',
        'giant': '巨型',
        'energy_level': '活力水平',
        'low': '低',
        'high': '高',
        'grooming_needs': '美容需求',
        'trainability': '可训练性',
        'barking_level': '吠叫程度',
        'quiet': '安静',
        'vocal': '爱叫',
        'good_for': '适合',
        'kids': '儿童',
        'apartments': '公寓',
        'shedding': '掉毛程度',
        'minimal': '极少',
        'moderate': '中等',
        'heavy': '大量',
        'breeds_found': '个品种',
        'sort_by_name': '按名称',
        'sort_by_size': '按体型',
        'sort_by_energy': '按活力',
        'sort_by_trainability': '按可训练性',
        'no_breeds_found': '未找到品种',
        'try_adjusting': '请尝试调整筛选条件或搜索词',
        'home': '首页',
        'browse_breeds': '浏览品种',
        'quiz': '测验',
        'compare': '比较',
        'or_less': '或更少',
    },
    'ja': {
        'title': '犬種を見る',
        'page_title': 'あなたにぴったりの犬種を見つけよう',
        'page_subtitle': 'サイズ、活動レベル、お手入れなどで絞り込み',
        'search_placeholder': '犬種を検索... (例: ゴールデンレトリバー, 小型, フレンドリー)',
        'filters': 'フィルター',
        'reset': 'リセット',
        'size': 'サイズ',
        'tiny': '極小',
        'small': '小型',
        'medium': '中型',
        'large': '大型',
        'giant': '超大型',
        'energy_level': '活動レベル',
        'low': '低い',
        'high': '高い',
        'grooming_needs': 'お手入れ',
        'trainability': 'しつけやすさ',
        'barking_level': '吠え声',
        'quiet': '静か',
        'vocal': 'よく吠える',
        'good_for': '向いている',
        'kids': '子供',
        'apartments': 'マンション',
        'shedding': '抜け毛',
        'minimal': '少ない',
        'moderate': '普通',
        'heavy': '多い',
        'breeds_found': '犬種',
        'sort_by_name': '名前順',
        'sort_by_size': 'サイズ順',
        'sort_by_energy': '活動量順',
        'sort_by_trainability': 'しつけやすさ順',
        'no_breeds_found': '犬種が見つかりません',
        'try_adjusting': 'フィルターや検索条件を変更してみてください',
        'home': 'ホーム',
        'browse_breeds': '犬種を見る',
        'quiz': 'クイズ',
        'compare': '比較',
        'or_less': '以下',
    },
    'sv': {
        'title': 'Bläddra Raser',
        'page_title': 'Hitta Din Perfekta Hundras',
        'page_subtitle': 'Filtrera efter storlek, energinivå, pälsvård och mer',
        'search_placeholder': 'Sök raser... (t.ex. Golden Retriever, liten, vänlig)',
        'filters': 'Filter',
        'reset': 'Återställ',
        'size': 'Storlek',
        'tiny': 'Mini',
        'small': 'Liten',
        'medium': 'Medel',
        'large': 'Stor',
        'giant': 'Jätte',
        'energy_level': 'Energinivå',
        'low': 'Låg',
        'high': 'Hög',
        'grooming_needs': 'Pälsvård',
        'trainability': 'Träningsbarhet',
        'barking_level': 'Skällnivå',
        'quiet': 'Tyst',
        'vocal': 'Högljudd',
        'good_for': 'Bra för',
        'kids': 'Barn',
        'apartments': 'Lägenheter',
        'shedding': 'Fällning',
        'minimal': 'Minimal',
        'moderate': 'Måttlig',
        'heavy': 'Mycket',
        'breeds_found': 'raser hittade',
        'sort_by_name': 'Efter Namn',
        'sort_by_size': 'Efter Storlek',
        'sort_by_energy': 'Efter Energi',
        'sort_by_trainability': 'Efter Träningsbarhet',
        'no_breeds_found': 'Inga raser hittades',
        'try_adjusting': 'Försök justera filter eller sökord',
        'home': 'Hem',
        'browse_breeds': 'Bläddra Raser',
        'quiz': 'Quiz',
        'compare': 'Jämför',
        'or_less': 'eller mindre',
    },
    'no': {
        'title': 'Bla Gjennom Raser',
        'page_title': 'Finn Din Perfekte Hunderase',
        'page_subtitle': 'Filtrer etter størrelse, energinivå, pelspleie og mer',
        'search_placeholder': 'Søk etter raser... (f.eks. Golden Retriever, liten, vennlig)',
        'filters': 'Filter',
        'reset': 'Tilbakestill',
        'size': 'Størrelse',
        'tiny': 'Mini',
        'small': 'Liten',
        'medium': 'Middels',
        'large': 'Stor',
        'giant': 'Kjempe',
        'energy_level': 'Energinivå',
        'low': 'Lav',
        'high': 'Høy',
        'grooming_needs': 'Pelspleie',
        'trainability': 'Trenbarhet',
        'barking_level': 'Bjeffenivå',
        'quiet': 'Stille',
        'vocal': 'Høylytt',
        'good_for': 'Bra for',
        'kids': 'Barn',
        'apartments': 'Leiligheter',
        'shedding': 'Hårfelling',
        'minimal': 'Minimal',
        'moderate': 'Moderat',
        'heavy': 'Mye',
        'breeds_found': 'raser funnet',
        'sort_by_name': 'Etter Navn',
        'sort_by_size': 'Etter Størrelse',
        'sort_by_energy': 'Etter Energi',
        'sort_by_trainability': 'Etter Trenbarhet',
        'no_breeds_found': 'Ingen raser funnet',
        'try_adjusting': 'Prøv å justere filter eller søkeord',
        'home': 'Hjem',
        'browse_breeds': 'Bla Gjennom Raser',
        'quiz': 'Quiz',
        'compare': 'Sammenlign',
        'or_less': 'eller mindre',
    },
    'da': {
        'title': 'Gennemse Racer',
        'page_title': 'Find Din Perfekte Hunderace',
        'page_subtitle': 'Filtrer efter størrelse, energiniveau, pelspleje og mere',
        'search_placeholder': 'Søg efter racer... (f.eks. Golden Retriever, lille, venlig)',
        'filters': 'Filtre',
        'reset': 'Nulstil',
        'size': 'Størrelse',
        'tiny': 'Mini',
        'small': 'Lille',
        'medium': 'Mellem',
        'large': 'Stor',
        'giant': 'Kæmpe',
        'energy_level': 'Energiniveau',
        'low': 'Lav',
        'high': 'Høj',
        'grooming_needs': 'Pelspleje',
        'trainability': 'Trænbarhed',
        'barking_level': 'Gøniveau',
        'quiet': 'Stille',
        'vocal': 'Højlydt',
        'good_for': 'God til',
        'kids': 'Børn',
        'apartments': 'Lejligheder',
        'shedding': 'Fældning',
        'minimal': 'Minimal',
        'moderate': 'Moderat',
        'heavy': 'Meget',
        'breeds_found': 'racer fundet',
        'sort_by_name': 'Efter Navn',
        'sort_by_size': 'Efter Størrelse',
        'sort_by_energy': 'Efter Energi',
        'sort_by_trainability': 'Efter Trænbarhed',
        'no_breeds_found': 'Ingen racer fundet',
        'try_adjusting': 'Prøv at justere filtre eller søgeord',
        'home': 'Hjem',
        'browse_breeds': 'Gennemse Racer',
        'quiz': 'Quiz',
        'compare': 'Sammenlign',
        'or_less': 'eller mindre',
    },
    'ru': {
        'title': 'Обзор Пород',
        'page_title': 'Найдите Свою Идеальную Породу Собаки',
        'page_subtitle': 'Фильтруйте по размеру, уровню энергии, уходу и другим параметрам',
        'search_placeholder': 'Поиск пород... (напр. Золотистый ретривер, маленькая, дружелюбная)',
        'filters': 'Фильтры',
        'reset': 'Сбросить',
        'size': 'Размер',
        'tiny': 'Миниатюрный',
        'small': 'Маленький',
        'medium': 'Средний',
        'large': 'Большой',
        'giant': 'Гигантский',
        'energy_level': 'Уровень Энергии',
        'low': 'Низкий',
        'high': 'Высокий',
        'grooming_needs': 'Потребность в Уходе',
        'trainability': 'Обучаемость',
        'barking_level': 'Уровень Лая',
        'quiet': 'Тихий',
        'vocal': 'Громкий',
        'good_for': 'Подходит для',
        'kids': 'Дети',
        'apartments': 'Квартиры',
        'shedding': 'Линька',
        'minimal': 'Минимальная',
        'moderate': 'Умеренная',
        'heavy': 'Сильная',
        'breeds_found': 'пород найдено',
        'sort_by_name': 'По Названию',
        'sort_by_size': 'По Размеру',
        'sort_by_energy': 'По Энергии',
        'sort_by_trainability': 'По Обучаемости',
        'no_breeds_found': 'Породы не найдены',
        'try_adjusting': 'Попробуйте изменить фильтры или поисковые запросы',
        'home': 'Главная',
        'browse_breeds': 'Обзор Пород',
        'quiz': 'Тест',
        'compare': 'Сравнить',
        'or_less': 'или меньше',
    },
}

def generate_lang_dropdown(current_lang):
    """Generate language dropdown HTML"""
    items = ['<a href="../../search/" class="block px-4 py-2 hover:bg-slate-100 text-slate-600">English</a>']
    for code, info in LANGUAGES.items():
        selected = 'font-semibold text-sky-600' if code == current_lang else 'text-slate-600'
        items.append(f'<a href="../../{code}/search/" class="block px-4 py-2 hover:bg-slate-100 {selected}">{info["name"]}</a>')
    return ''.join(items)

def generate_search_page(lang, base_dir):
    """Generate search page for a specific language"""
    t = TRANSLATIONS.get(lang, TRANSLATIONS['en'])
    lang_info = LANGUAGES.get(lang, {'name': 'English', 'code': 'EN'})
    
    output_dir = base_dir / lang / 'search'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    lang_dropdown = generate_lang_dropdown(lang)
    
    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{t['title']} | BreedFinder</title>
    <meta name="description" content="{t['page_subtitle']}">
    <link rel="canonical" href="https://breedfinder.org/{lang}/search/">
    <link rel="icon" href="../../favicon.ico" type="image/x-icon">
    <link rel="icon" type="image/png" sizes="32x32" href="../../favicon-32.png">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <script src="https://cdn.jsdelivr.net/npm/fuse.js@7.0.0"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
        .breed-card {{ transition: transform 0.2s, box-shadow 0.2s; }}
        .breed-card:hover {{ transform: translateY(-4px); box-shadow: 0 12px 24px rgba(0,0,0,0.1); }}
        .filter-section {{ border-bottom: 1px solid #e2e8f0; }}
        .filter-section:last-child {{ border-bottom: none; }}
        input[type="range"] {{ -webkit-appearance: none; height: 6px; border-radius: 3px; background: #e2e8f0; }}
        input[type="range"]::-webkit-slider-thumb {{ -webkit-appearance: none; width: 18px; height: 18px; border-radius: 50%; background: #0ea5e9; cursor: pointer; }}
        .tag {{ display: inline-block; padding: 2px 8px; border-radius: 9999px; font-size: 12px; font-weight: 500; }}
    </style>
</head>
<body class="bg-slate-50 min-h-screen">
    <header class="bg-white border-b border-slate-200 sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 py-4">
            <div class="flex items-center justify-between">
                <a href="../" class="flex items-center gap-2">
                    <img src="../../logo-192.png" class="w-10 h-10" alt="BreedFinder">
                    <span class="font-bold text-xl text-slate-800">BreedFinder</span>
                </a>
                <nav class="hidden md:flex items-center gap-6">
                    <a href="../" class="text-slate-600 hover:text-slate-900">{t['home']}</a>
                    <a href="./" class="text-sky-600 font-medium">{t['browse_breeds']}</a>
                    <a href="../quiz/" class="text-slate-600 hover:text-slate-900">{t['quiz']}</a>
                    <a href="../compare/" class="text-slate-600 hover:text-slate-900">{t['compare']}</a>
                    <div class="relative group">
                        <button class="flex items-center gap-1 text-slate-600 hover:text-sky-600 py-2">
                            <i data-lucide="globe" class="w-4 h-4"></i>
                            <span>{lang_info['code']}</span>
                        </button>
                        <div class="absolute right-0 top-full bg-white border border-slate-200 rounded-xl shadow-xl hidden group-hover:block min-w-[140px] py-2 z-50 before:absolute before:h-2 before:-top-2 before:left-0 before:right-0 before:bg-transparent">
                            {lang_dropdown}
                        </div>
                    </div>
                </nav>
            </div>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 py-8">
        <div class="text-center mb-8">
            <h1 class="text-3xl md:text-4xl font-bold text-slate-800 mb-3">{t['page_title']}</h1>
            <p class="text-slate-600 text-lg">{t['page_subtitle']}</p>
        </div>

        <div class="max-w-2xl mx-auto mb-8">
            <div class="relative">
                <i data-lucide="search" class="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-400"></i>
                <input type="text" id="searchInput" placeholder="{t['search_placeholder']}" 
                    class="w-full pl-12 pr-4 py-4 rounded-xl border border-slate-200 bg-white shadow-sm focus:ring-2 focus:ring-sky-500 focus:border-sky-500 text-lg" autocomplete="off">
                <button id="clearSearch" class="absolute right-4 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 hidden">
                    <i data-lucide="x" class="w-5 h-5"></i>
                </button>
                <div id="search-dropdown" class="absolute top-full left-0 right-0 mt-2 bg-white border border-slate-200 rounded-2xl shadow-xl z-50 hidden max-h-80 overflow-y-auto"></div>
            </div>
        </div>

        <div class="flex flex-col lg:flex-row gap-8">
            <aside class="lg:w-72 flex-shrink-0">
                <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-5">
                    <div class="flex items-center justify-between mb-4">
                        <h2 class="font-semibold text-slate-800 flex items-center gap-2">
                            <i data-lucide="sliders-horizontal" class="w-5 h-5"></i>
                            {t['filters']}
                        </h2>
                        <button id="resetFilters" class="text-sm text-sky-600 hover:text-sky-700">{t['reset']}</button>
                    </div>

                    <div class="filter-section py-4">
                        <h3 class="font-medium text-slate-700 mb-3">{t['size']}</h3>
                        <div class="space-y-2">
                            <label class="flex items-center gap-2 cursor-pointer">
                                <input type="checkbox" value="tiny" class="size-filter rounded text-sky-600">
                                <span class="text-slate-600">{t['tiny']}</span>
                            </label>
                            <label class="flex items-center gap-2 cursor-pointer">
                                <input type="checkbox" value="small" class="size-filter rounded text-sky-600">
                                <span class="text-slate-600">{t['small']}</span>
                            </label>
                            <label class="flex items-center gap-2 cursor-pointer">
                                <input type="checkbox" value="medium" class="size-filter rounded text-sky-600">
                                <span class="text-slate-600">{t['medium']}</span>
                            </label>
                            <label class="flex items-center gap-2 cursor-pointer">
                                <input type="checkbox" value="large" class="size-filter rounded text-sky-600">
                                <span class="text-slate-600">{t['large']}</span>
                            </label>
                            <label class="flex items-center gap-2 cursor-pointer">
                                <input type="checkbox" value="giant" class="size-filter rounded text-sky-600">
                                <span class="text-slate-600">{t['giant']}</span>
                            </label>
                        </div>
                    </div>

                    <div class="filter-section py-4">
                        <label class="flex items-center justify-between mb-3 cursor-pointer">
                            <h3 class="font-medium text-slate-700">{t['energy_level']}</h3>
                            <input type="checkbox" id="energyEnabled" class="rounded text-sky-600">
                        </label>
                        <div id="energyControls" class="hidden">
                            <div class="flex items-center gap-3">
                                <span class="text-xs text-slate-500">{t['low']}</span>
                                <input type="range" id="energyFilter" min="1" max="5" value="3" class="flex-1">
                                <span class="text-xs text-slate-500">{t['high']}</span>
                            </div>
                            <div class="text-center text-sm text-slate-600 mt-1"><span id="energyValue">3</span>+</div>
                        </div>
                    </div>

                    <div class="filter-section py-4">
                        <label class="flex items-center justify-between mb-3 cursor-pointer">
                            <h3 class="font-medium text-slate-700">{t['grooming_needs']}</h3>
                            <input type="checkbox" id="groomingEnabled" class="rounded text-sky-600">
                        </label>
                        <div id="groomingControls" class="hidden">
                            <div class="flex items-center gap-3">
                                <span class="text-xs text-slate-500">{t['low']}</span>
                                <input type="range" id="groomingFilter" min="1" max="5" value="3" class="flex-1">
                                <span class="text-xs text-slate-500">{t['high']}</span>
                            </div>
                            <div class="text-center text-sm text-slate-600 mt-1"><span id="groomingValue">3</span> {t['or_less']}</div>
                        </div>
                    </div>

                    <div class="filter-section py-4">
                        <label class="flex items-center justify-between mb-3 cursor-pointer">
                            <h3 class="font-medium text-slate-700">{t['trainability']}</h3>
                            <input type="checkbox" id="trainabilityEnabled" class="rounded text-sky-600">
                        </label>
                        <div id="trainabilityControls" class="hidden">
                            <div class="flex items-center gap-3">
                                <span class="text-xs text-slate-500">{t['low']}</span>
                                <input type="range" id="trainabilityFilter" min="1" max="5" value="3" class="flex-1">
                                <span class="text-xs text-slate-500">{t['high']}</span>
                            </div>
                            <div class="text-center text-sm text-slate-600 mt-1"><span id="trainabilityValue">3</span>+</div>
                        </div>
                    </div>

                    <div class="filter-section py-4">
                        <label class="flex items-center justify-between mb-3 cursor-pointer">
                            <h3 class="font-medium text-slate-700">{t['barking_level']}</h3>
                            <input type="checkbox" id="barkingEnabled" class="rounded text-sky-600">
                        </label>
                        <div id="barkingControls" class="hidden">
                            <div class="flex items-center gap-3">
                                <span class="text-xs text-slate-500">{t['quiet']}</span>
                                <input type="range" id="barkingFilter" min="1" max="5" value="3" class="flex-1">
                                <span class="text-xs text-slate-500">{t['vocal']}</span>
                            </div>
                            <div class="text-center text-sm text-slate-600 mt-1"><span id="barkingValue">3</span> {t['or_less']}</div>
                        </div>
                    </div>

                    <div class="filter-section py-4">
                        <h3 class="font-medium text-slate-700 mb-3">{t['good_for']}</h3>
                        <div class="space-y-3">
                            <label class="flex items-center justify-between cursor-pointer">
                                <span class="text-slate-600">{t['kids']}</span>
                                <input type="checkbox" id="kidFriendly" class="toggle-filter rounded text-sky-600">
                            </label>
                            <label class="flex items-center justify-between cursor-pointer">
                                <span class="text-slate-600">{t['apartments']}</span>
                                <input type="checkbox" id="apartmentOk" class="toggle-filter rounded text-sky-600">
                            </label>
                        </div>
                    </div>

                    <div class="py-4">
                        <h3 class="font-medium text-slate-700 mb-3">{t['shedding']}</h3>
                        <div class="space-y-2">
                            <label class="flex items-center gap-2 cursor-pointer">
                                <input type="checkbox" value="minimal" class="shed-filter rounded text-sky-600">
                                <span class="text-slate-600">{t['minimal']}</span>
                            </label>
                            <label class="flex items-center gap-2 cursor-pointer">
                                <input type="checkbox" value="moderate" class="shed-filter rounded text-sky-600">
                                <span class="text-slate-600">{t['moderate']}</span>
                            </label>
                            <label class="flex items-center gap-2 cursor-pointer">
                                <input type="checkbox" value="heavy" class="shed-filter rounded text-sky-600">
                                <span class="text-slate-600">{t['heavy']}</span>
                            </label>
                        </div>
                    </div>
                </div>
            </aside>

            <div class="flex-1">
                <div class="flex items-center justify-between mb-4">
                    <p class="text-slate-600"><span id="resultCount">0</span> {t['breeds_found']}</p>
                    <select id="sortBy" class="px-3 py-2 rounded-lg border border-slate-200 bg-white text-sm">
                        <option value="name">{t['sort_by_name']}</option>
                        <option value="size">{t['sort_by_size']}</option>
                        <option value="energy">{t['sort_by_energy']}</option>
                        <option value="trainability">{t['sort_by_trainability']}</option>
                    </select>
                </div>

                <div id="resultsGrid" class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-5"></div>

                <div id="noResults" class="hidden text-center py-16">
                    <i data-lucide="search-x" class="w-16 h-16 text-slate-300 mx-auto mb-4"></i>
                    <h3 class="text-xl font-semibold text-slate-700 mb-2">{t['no_breeds_found']}</h3>
                    <p class="text-slate-500">{t['try_adjusting']}</p>
                </div>
            </div>
        </div>
    </main>

    <footer class="bg-slate-800 text-white py-8 mt-16">
        <div class="max-w-7xl mx-auto px-4 text-center">
            <div class="flex items-center justify-center gap-2 mb-4">
                <img src="../../logo-192.png" class="w-8 h-8 rounded-lg" alt="BreedFinder">
                <span class="font-semibold">BreedFinder</span>
            </div>
            <p class="text-slate-400 text-sm">Find your perfect dog breed match</p>
            <p class="text-slate-500 text-xs mt-6">© 2026 BreedFinder</p>
        </div>
    </footer>

    <script>
        lucide.createIcons();
        let allBreeds = [];
        let fuse = null;

        async function loadBreeds() {{
            const response = await fetch('../../data/breeds.json');
            allBreeds = await response.json();
            fuse = new Fuse(allBreeds, {{
                keys: ['name', 'aliases', 'temperament', 'group', 'description.overview'],
                threshold: 0.4,
                includeScore: true
            }});
            applyFilters();
        }}

        function renderBreedCard(breed) {{
            const imageUrl = `../../images/breeds/${{breed.id}}.webp`;
            const fallbackUrl = `../../images/heads/${{breed.id}}.webp`;
            const sizeColors = {{
                tiny: 'bg-purple-100 text-purple-700',
                small: 'bg-blue-100 text-blue-700',
                medium: 'bg-green-100 text-green-700',
                large: 'bg-orange-100 text-orange-700',
                giant: 'bg-red-100 text-red-700'
            }};
            const temperamentTags = breed.temperament.slice(0, 3).map(t => 
                `<span class="tag bg-slate-100 text-slate-600">${{t}}</span>`
            ).join('');

            return `
                <a href="../breeds/${{breed.id}}.html" class="breed-card bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden block">
                    <div class="aspect-[4/5] bg-slate-100 relative overflow-hidden">
                        <img src="${{imageUrl}}" alt="${{breed.name}}" 
                            class="w-full h-full object-cover object-top"
                            onerror="this.onerror=null; this.src='${{fallbackUrl}}';">
                        <span class="absolute top-2 right-2 tag ${{sizeColors[breed.size.category] || 'bg-slate-100 text-slate-600'}}">
                            ${{breed.size.category}}
                        </span>
                    </div>
                    <div class="p-4">
                        <h3 class="font-semibold text-slate-800 text-lg mb-1">${{breed.name}}</h3>
                        <p class="text-slate-500 text-sm mb-3">${{breed.origin}} · ${{breed.lifespan}}</p>
                        <div class="flex flex-wrap gap-1 mb-3">${{temperamentTags}}</div>
                        <div class="grid grid-cols-3 gap-2 text-center text-xs">
                            <div class="bg-slate-50 rounded-lg py-2">
                                <div class="text-slate-500">Energy</div>
                                <div class="font-semibold text-slate-700">${{'●'.repeat(breed.ratings.energy)}}${{'○'.repeat(5-breed.ratings.energy)}}</div>
                            </div>
                            <div class="bg-slate-50 rounded-lg py-2">
                                <div class="text-slate-500">Groom</div>
                                <div class="font-semibold text-slate-700">${{'●'.repeat(breed.ratings.grooming)}}${{'○'.repeat(5-breed.ratings.grooming)}}</div>
                            </div>
                            <div class="bg-slate-50 rounded-lg py-2">
                                <div class="text-slate-500">Train</div>
                                <div class="font-semibold text-slate-700">${{'●'.repeat(breed.ratings.trainability)}}${{'○'.repeat(5-breed.ratings.trainability)}}</div>
                            </div>
                        </div>
                    </div>
                </a>
            `;
        }}

        function applyFilters() {{
            const searchQuery = document.getElementById('searchInput').value.trim();
            const energyEnabled = document.getElementById('energyEnabled').checked;
            const groomingEnabled = document.getElementById('groomingEnabled').checked;
            const trainabilityEnabled = document.getElementById('trainabilityEnabled').checked;
            const barkingEnabled = document.getElementById('barkingEnabled').checked;
            const energyMin = parseInt(document.getElementById('energyFilter').value);
            const groomingMax = parseInt(document.getElementById('groomingFilter').value);
            const trainabilityMin = parseInt(document.getElementById('trainabilityFilter').value);
            const barkingMax = parseInt(document.getElementById('barkingFilter').value);
            const kidFriendly = document.getElementById('kidFriendly').checked;
            const apartmentOk = document.getElementById('apartmentOk').checked;
            const sortBy = document.getElementById('sortBy').value;
            const selectedSizes = Array.from(document.querySelectorAll('.size-filter:checked')).map(cb => cb.value);
            const selectedShedding = Array.from(document.querySelectorAll('.shed-filter:checked')).map(cb => cb.value);

            let results = searchQuery && fuse 
                ? fuse.search(searchQuery).map(r => r.item)
                : [...allBreeds];

            results = results.filter(breed => {{
                if (selectedSizes.length > 0 && !selectedSizes.includes(breed.size.category)) return false;
                if (energyEnabled && breed.ratings.energy < energyMin) return false;
                if (groomingEnabled && breed.ratings.grooming > groomingMax) return false;
                if (trainabilityEnabled && breed.ratings.trainability < trainabilityMin) return false;
                if (barkingEnabled && breed.ratings.barking > barkingMax) return false;
                if (kidFriendly && breed.ratings.kid_friendly < 4) return false;
                if (apartmentOk && breed.ratings.apartment_ok < 3) return false;
                if (selectedShedding.length > 0 && !selectedShedding.includes(breed.characteristics.shedding)) return false;
                return true;
            }});

            results.sort((a, b) => {{
                switch (sortBy) {{
                    case 'size': return (a.ratings.size || 3) - (b.ratings.size || 3);
                    case 'energy': return b.ratings.energy - a.ratings.energy;
                    case 'trainability': return b.ratings.trainability - a.ratings.trainability;
                    default: return a.name.localeCompare(b.name);
                }}
            }});

            const grid = document.getElementById('resultsGrid');
            const noResults = document.getElementById('noResults');
            document.getElementById('resultCount').textContent = results.length;

            if (results.length === 0) {{
                grid.innerHTML = '';
                noResults.classList.remove('hidden');
            }} else {{
                noResults.classList.add('hidden');
                grid.innerHTML = results.map(renderBreedCard).join('');
                lucide.createIcons();
            }}
            document.getElementById('clearSearch').classList.toggle('hidden', !searchQuery);
        }}

        function toggleFilterControls() {{
            document.getElementById('energyControls').classList.toggle('hidden', !document.getElementById('energyEnabled').checked);
            document.getElementById('groomingControls').classList.toggle('hidden', !document.getElementById('groomingEnabled').checked);
            document.getElementById('trainabilityControls').classList.toggle('hidden', !document.getElementById('trainabilityEnabled').checked);
            document.getElementById('barkingControls').classList.toggle('hidden', !document.getElementById('barkingEnabled').checked);
        }}

        function updateSliderLabels() {{
            document.getElementById('energyValue').textContent = document.getElementById('energyFilter').value;
            document.getElementById('groomingValue').textContent = document.getElementById('groomingFilter').value;
            document.getElementById('trainabilityValue').textContent = document.getElementById('trainabilityFilter').value;
            document.getElementById('barkingValue').textContent = document.getElementById('barkingFilter').value;
        }}

        function resetFilters() {{
            document.getElementById('searchInput').value = '';
            document.getElementById('energyEnabled').checked = false;
            document.getElementById('groomingEnabled').checked = false;
            document.getElementById('trainabilityEnabled').checked = false;
            document.getElementById('barkingEnabled').checked = false;
            document.getElementById('energyFilter').value = 3;
            document.getElementById('groomingFilter').value = 3;
            document.getElementById('trainabilityFilter').value = 3;
            document.getElementById('barkingFilter').value = 3;
            document.getElementById('kidFriendly').checked = false;
            document.getElementById('apartmentOk').checked = false;
            document.querySelectorAll('.size-filter, .shed-filter').forEach(cb => cb.checked = false);
            document.getElementById('sortBy').value = 'name';
            toggleFilterControls();
            updateSliderLabels();
            applyFilters();
        }}

        // Autocomplete
        const searchInput = document.getElementById('searchInput');
        const searchDropdown = document.getElementById('search-dropdown');
        
        function showAutocomplete(query) {{
            if (!query || allBreeds.length === 0) {{
                searchDropdown.classList.add('hidden');
                return;
            }}
            const matches = allBreeds.filter(b => b.name.toLowerCase().includes(query.toLowerCase())).slice(0, 8);
            if (matches.length === 0) {{
                searchDropdown.classList.add('hidden');
                return;
            }}
            searchDropdown.innerHTML = matches.map(b => `
                <a href="../breeds/${{b.id}}.html" class="flex items-center gap-3 px-4 py-3 hover:bg-slate-50 transition border-b border-slate-100 last:border-0">
                    <img src="../../images/heads/${{b.id}}.webp" alt="${{b.name}}" class="w-10 h-10 rounded-xl object-cover">
                    <div><div class="font-medium text-slate-800">${{b.name}}</div><div class="text-sm text-slate-500">${{b.group}} · ${{b.size.category}}</div></div>
                </a>
            `).join('');
            searchDropdown.classList.remove('hidden');
        }}

        document.addEventListener('click', (e) => {{
            if (!searchInput.contains(e.target) && !searchDropdown.contains(e.target)) searchDropdown.classList.add('hidden');
        }});

        searchInput.addEventListener('input', function() {{ showAutocomplete(this.value.trim()); applyFilters(); }});
        searchInput.addEventListener('focus', function() {{ if (this.value.trim()) showAutocomplete(this.value.trim()); }});
        document.getElementById('clearSearch').addEventListener('click', () => {{ searchInput.value = ''; searchDropdown.classList.add('hidden'); applyFilters(); }});
        document.getElementById('energyEnabled').addEventListener('change', () => {{ toggleFilterControls(); applyFilters(); }});
        document.getElementById('groomingEnabled').addEventListener('change', () => {{ toggleFilterControls(); applyFilters(); }});
        document.getElementById('trainabilityEnabled').addEventListener('change', () => {{ toggleFilterControls(); applyFilters(); }});
        document.getElementById('barkingEnabled').addEventListener('change', () => {{ toggleFilterControls(); applyFilters(); }});
        document.getElementById('energyFilter').addEventListener('input', () => {{ updateSliderLabels(); applyFilters(); }});
        document.getElementById('groomingFilter').addEventListener('input', () => {{ updateSliderLabels(); applyFilters(); }});
        document.getElementById('trainabilityFilter').addEventListener('input', () => {{ updateSliderLabels(); applyFilters(); }});
        document.getElementById('barkingFilter').addEventListener('input', () => {{ updateSliderLabels(); applyFilters(); }});
        document.getElementById('kidFriendly').addEventListener('change', applyFilters);
        document.getElementById('apartmentOk').addEventListener('change', applyFilters);
        document.getElementById('sortBy').addEventListener('change', applyFilters);
        document.getElementById('resetFilters').addEventListener('click', resetFilters);
        document.querySelectorAll('.size-filter, .shed-filter').forEach(cb => cb.addEventListener('change', applyFilters));

        loadBreeds();
    </script>
</body>
</html>'''
    
    with open(output_dir / 'index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  Created {lang}/search/index.html")


def main():
    base_dir = Path(__file__).parent.parent
    
    print("Generating translated search pages with full filters...")
    for lang in LANGUAGES.keys():
        generate_search_page(lang, base_dir)
    
    print(f"\n✅ Done! Created {len(LANGUAGES)} search pages with full filters")


if __name__ == '__main__':
    main()
