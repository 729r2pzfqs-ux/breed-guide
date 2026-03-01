#!/usr/bin/env python3
"""
Generate in-depth comparison articles for 11 missing languages.
Languages: DA, IT, JA, NL, NO, PL, PT, RU, SV, TR, ZH
"""

import os
from pathlib import Path

# Base path
BASE_DIR = Path(__file__).parent.parent

# Language configurations
LANGUAGES = {
    'da': {
        'name': 'Danish',
        'html_lang': 'da',
        'ui': {
            'all_breeds': 'Alle Racer',
            'compare': 'Sammenlign',
            'take_quiz': 'Tag Quiz',
            'comparisons': 'Sammenligninger',
            'complete_comparison': 'Komplet Sammenligning',
            'side_by_side': 'Side om Side Sammenligning',
            'attribute': 'Egenskab',
            'size': 'Størrelse',
            'lifespan': 'Levetid',
            'energy_level': 'Energiniveau',
            'grooming_needs': 'Plejebehov',
            'trainability': 'Trænbarhed',
            'kid_friendly': 'Børnevenlig',
            'apartment': 'Egnet til lejlighed',
            'shedding': 'Fældning',
            'origin': 'Oprindelse',
            'temperament': 'Temperament',
            'exercise_needs': 'Motionsbehov',
            'grooming_req': 'Plejekrav',
            'which_right': 'Hvilken er den rette for dig?',
            'choose_if': 'Vælg en {breed} hvis...',
            'bottom_line': 'Konklusion',
            'more_comparisons': 'Flere Sammenligninger',
            'back_to_compare': '← Tilbage til Sammenlign',
            'view_profile': 'Se fuld profil →',
            'large': 'Stor',
            'medium': 'Mellem',
            'small': 'Lille',
            'years': 'år',
            'very_high': 'Meget Høj',
            'high': 'Høj',
            'moderate': 'Moderat',
            'low': 'Lav',
            'excellent': 'Fremragende',
            'good': 'God',
            'not_ideal': 'Ikke Ideel',
            'heavy': 'Kraftig',
            'dog_breed_comparisons': 'Hunderace Sammenligninger',
            'popular_comparisons_desc': 'Populære hunderace sammenligninger. Find den perfekte race til dig.',
            'helping_find': 'Hjælper dig med at finde din perfekte følgesvend.',
        },
        'comparisons': {
            'labrador-vs-golden': {
                'slug': 'labrador-vs-golden-retriever',
                'breed1': 'Labrador Retriever',
                'breed2': 'Golden Retriever',
                'breed1_slug': 'labrador-retriever',
                'breed2_slug': 'golden-retriever',
                'title': 'Labrador Retriever vs Golden Retriever: Komplet Sammenligning',
                'desc': 'Labrador vs Golden Retriever sammenligning. Se størrelse, temperament, motionsbehov og familievenlighed side om side.',
                'intro': 'To af verdens mest elskede familiehunde. Begge er venlige, intelligente og fantastiske med børn—men hvilken er den rette for dig?',
                'breed1_tagline': 'Verdens #1 Race',
                'breed2_tagline': 'Familiens Favorit',
                'breed1_desc': 'Labrador Retrieveren er verdens mest populære hunderace af gode grunde. De er venlige, udadvendte og livlige følgesvende med masser af kærlighed at give.',
                'breed2_desc': 'Golden Retrieveren er en af de mest populære hunderacer. Deres venlige, tolerante attitude gør dem til fantastiske familiehunde, og deres intelligens gør dem til dygtige arbejdshunde.',
            },
            'frenchie-vs-boston': {
                'slug': 'fransk-bulldog-vs-boston-terrier',
                'breed1': 'Fransk Bulldog',
                'breed2': 'Boston Terrier',
                'breed1_slug': 'french-bulldog',
                'breed2_slug': 'boston-terrier',
                'title': 'Fransk Bulldog vs Boston Terrier: Komplet Sammenligning',
                'desc': 'Fransk Bulldog vs Boston Terrier sammenligning. Kompakte følgesvende sammenlignet side om side.',
                'intro': 'To charmerende, kompakte racer med store personligheder. Begge er fantastiske til lejlighedsliv—men hvilken passer bedst til din livsstil?',
                'breed1_tagline': 'Den Charmerende Franskman',
                'breed2_tagline': 'Den Amerikanske Gentleman',
                'breed1_desc': 'Fransk Bulldog er en charmerende, tilpasningsdygtig race med en legesyg personlighed. De er kendt for deres flagermusører og hengivne natur.',
                'breed2_desc': 'Boston Terrieren, kendt som "Den Amerikanske Gentleman", er en livlig lille hund med et venligt, muntert temperament.',
            },
            'gsd-vs-malinois': {
                'slug': 'schaefer-vs-malinois',
                'breed1': 'Tysk Schæferhund',
                'breed2': 'Belgisk Malinois',
                'breed1_slug': 'german-shepherd',
                'breed2_slug': 'belgian-malinois',
                'title': 'Tysk Schæferhund vs Belgisk Malinois: Komplet Sammenligning',
                'desc': 'Tysk Schæferhund vs Belgisk Malinois sammenligning. To fremragende arbejdshunde sammenlignet.',
                'intro': 'To af verdens mest kapable arbejdshunde. Begge excellerer i politi- og militærarbejde—men de har vigtige forskelle.',
                'breed1_tagline': 'Den Alsidige Beskytter',
                'breed2_tagline': 'Elite Arbejdshund',
                'breed1_desc': 'Den Tyske Schæferhund er alsidig, intelligent og en af de mest populære arbejdshunderacer i verden.',
                'breed2_desc': 'Den Belgiske Malinois er en intens, højtydende arbejdshund foretrukket af politi og militær verden over.',
            },
            'husky-vs-malamute': {
                'slug': 'husky-vs-malamute',
                'breed1': 'Sibirisk Husky',
                'breed2': 'Alaskan Malamute',
                'breed1_slug': 'siberian-husky',
                'breed2_slug': 'alaskan-malamute',
                'title': 'Sibirisk Husky vs Alaskan Malamute: Komplet Sammenligning',
                'desc': 'Husky vs Malamute sammenligning. Arktiske racer sammenlignet side om side.',
                'intro': 'To majestætiske arktiske racer med ulvelignende udseende. De ligner hinanden, men har vigtige forskelle i størrelse og temperament.',
                'breed1_tagline': 'Den Hurtige Slædehund',
                'breed2_tagline': 'Den Kraftfulde Lastdyrs',
                'breed1_desc': 'Sibirisk Husky er en atletisk, udholdende slædehund kendt for sine slående blå øjne og venlige personlighed.',
                'breed2_desc': 'Alaskan Malamute er en kraftfuld, tungtbygget slædehund avlet til styrke og udholdenhed.',
            },
            'poodle-vs-labrador': {
                'slug': 'puddel-vs-labrador',
                'breed1': 'Puddel',
                'breed2': 'Labrador Retriever',
                'breed1_slug': 'poodle',
                'breed2_slug': 'labrador-retriever',
                'title': 'Puddel vs Labrador Retriever: Komplet Sammenligning',
                'desc': 'Puddel vs Labrador Retriever sammenligning. To intelligente, populære racer sammenlignet.',
                'intro': 'To af de mest intelligente og populære hunderacer. Begge er fremragende familiehunde med meget forskellige pelse.',
                'breed1_tagline': 'Den Elegante Atlet',
                'breed2_tagline': 'Alles Bedste Ven',
                'breed1_desc': 'Pudlen er exceptionelt intelligent og aktiv. Bag det elegante ydre gemmer sig en atletisk, ivrig og meget klog hund.',
                'breed2_desc': 'Labrador Retrieveren er verdens mest populære hunderace, kendt for sin venlige, udadvendte natur.',
            },
        },
    },
    'it': {
        'name': 'Italian',
        'html_lang': 'it',
        'ui': {
            'all_breeds': 'Tutte le Razze',
            'compare': 'Confronta',
            'take_quiz': 'Fai il Quiz',
            'comparisons': 'Confronti',
            'complete_comparison': 'Confronto Completo',
            'side_by_side': 'Confronto Fianco a Fianco',
            'attribute': 'Attributo',
            'size': 'Taglia',
            'lifespan': 'Durata della Vita',
            'energy_level': 'Livello di Energia',
            'grooming_needs': 'Esigenze di Toelettatura',
            'trainability': 'Addestrabilità',
            'kid_friendly': 'Adatto ai Bambini',
            'apartment': 'Adatto ad Appartamento',
            'shedding': 'Perdita di Pelo',
            'origin': 'Origine',
            'temperament': 'Temperamento',
            'exercise_needs': 'Esigenze di Esercizio',
            'grooming_req': 'Requisiti di Toelettatura',
            'which_right': 'Qual è Quello Giusto per Te?',
            'choose_if': 'Scegli un {breed} se...',
            'bottom_line': 'In Conclusione',
            'more_comparisons': 'Altri Confronti',
            'back_to_compare': '← Torna a Confronta',
            'view_profile': 'Vedi profilo completo →',
            'large': 'Grande',
            'medium': 'Medio',
            'small': 'Piccolo',
            'years': 'anni',
            'very_high': 'Molto Alto',
            'high': 'Alto',
            'moderate': 'Moderato',
            'low': 'Basso',
            'excellent': 'Eccellente',
            'good': 'Buono',
            'not_ideal': 'Non Ideale',
            'heavy': 'Abbondante',
            'dog_breed_comparisons': 'Confronti tra Razze Canine',
            'popular_comparisons_desc': 'Confronti popolari tra razze canine. Trova la razza perfetta per te.',
            'helping_find': 'Ti aiutiamo a trovare il tuo compagno perfetto.',
        },
        'comparisons': {
            'labrador-vs-golden': {
                'slug': 'labrador-vs-golden-retriever',
                'breed1': 'Labrador Retriever',
                'breed2': 'Golden Retriever',
                'breed1_slug': 'labrador-retriever',
                'breed2_slug': 'golden-retriever',
                'title': 'Labrador Retriever vs Golden Retriever: Confronto Completo',
                'desc': 'Confronto Labrador vs Golden Retriever. Scopri taglia, temperamento, esigenze di esercizio e adattabilità familiare.',
                'intro': 'Due delle razze familiari più amate al mondo. Entrambi sono amichevoli, intelligenti e ottimi con i bambini—ma quale è giusto per te?',
                'breed1_tagline': 'Razza #1 al Mondo',
                'breed2_tagline': 'Il Preferito delle Famiglie',
                'breed1_desc': 'Il Labrador Retriever è la razza canina più popolare al mondo per ottime ragioni. Sono amichevoli, socievoli e compagni vivaci.',
                'breed2_desc': 'Il Golden Retriever è una delle razze più popolari. Il loro atteggiamento amichevole e tollerante li rende fantastici animali domestici.',
            },
            'frenchie-vs-boston': {
                'slug': 'bulldog-francese-vs-boston-terrier',
                'breed1': 'Bulldog Francese',
                'breed2': 'Boston Terrier',
                'breed1_slug': 'french-bulldog',
                'breed2_slug': 'boston-terrier',
                'title': 'Bulldog Francese vs Boston Terrier: Confronto Completo',
                'desc': 'Confronto Bulldog Francese vs Boston Terrier. Due compagni compatti a confronto.',
                'intro': 'Due razze affascinanti e compatte con grandi personalità. Entrambe ottime per la vita in appartamento—ma quale si adatta meglio al tuo stile di vita?',
                'breed1_tagline': 'Il Francese Affascinante',
                'breed2_tagline': 'Il Gentiluomo Americano',
                'breed1_desc': 'Il Bulldog Francese è una razza affascinante e adattabile con una personalità giocosa, noto per le sue orecchie da pipistrello.',
                'breed2_desc': 'Il Boston Terrier, noto come "Il Gentiluomo Americano", è un cane vivace con un temperamento amichevole e allegro.',
            },
            'gsd-vs-malinois': {
                'slug': 'pastore-tedesco-vs-malinois',
                'breed1': 'Pastore Tedesco',
                'breed2': 'Malinois Belga',
                'breed1_slug': 'german-shepherd',
                'breed2_slug': 'belgian-malinois',
                'title': 'Pastore Tedesco vs Malinois Belga: Confronto Completo',
                'desc': 'Confronto Pastore Tedesco vs Malinois Belga. Due eccellenti cani da lavoro a confronto.',
                'intro': 'Due dei cani da lavoro più capaci al mondo. Entrambi eccellono nel lavoro di polizia e militare—ma hanno differenze importanti.',
                'breed1_tagline': 'Il Protettore Versatile',
                'breed2_tagline': 'Cane da Lavoro d\'Elite',
                'breed1_desc': 'Il Pastore Tedesco è versatile, intelligente e una delle razze da lavoro più popolari al mondo.',
                'breed2_desc': 'Il Malinois Belga è un cane da lavoro intenso e ad alte prestazioni, preferito da polizia e militari.',
            },
            'husky-vs-malamute': {
                'slug': 'husky-vs-malamute',
                'breed1': 'Siberian Husky',
                'breed2': 'Alaskan Malamute',
                'breed1_slug': 'siberian-husky',
                'breed2_slug': 'alaskan-malamute',
                'title': 'Siberian Husky vs Alaskan Malamute: Confronto Completo',
                'desc': 'Confronto Husky vs Malamute. Razze artiche a confronto.',
                'intro': 'Due razze artiche maestose dall\'aspetto simile al lupo. Sembrano simili ma hanno differenze importanti in dimensioni e temperamento.',
                'breed1_tagline': 'Il Cane da Slitta Veloce',
                'breed2_tagline': 'Il Potente Trasportatore',
                'breed1_desc': 'Il Siberian Husky è un cane da slitta atletico e resistente, noto per i suoi occhi blu e la personalità amichevole.',
                'breed2_desc': 'L\'Alaskan Malamute è un cane da slitta potente e robusto, allevato per forza e resistenza.',
            },
            'poodle-vs-labrador': {
                'slug': 'barboncino-vs-labrador',
                'breed1': 'Barboncino',
                'breed2': 'Labrador Retriever',
                'breed1_slug': 'poodle',
                'breed2_slug': 'labrador-retriever',
                'title': 'Barboncino vs Labrador Retriever: Confronto Completo',
                'desc': 'Confronto Barboncino vs Labrador. Due razze intelligenti e popolari a confronto.',
                'intro': 'Due delle razze canine più intelligenti e popolari. Entrambi eccellenti cani da famiglia con mantelli molto diversi.',
                'breed1_tagline': 'L\'Atleta Elegante',
                'breed2_tagline': 'Il Migliore Amico di Tutti',
                'breed1_desc': 'Il Barboncino è eccezionalmente intelligente e attivo. Dietro l\'aspetto elegante c\'è un cane atletico e molto intelligente.',
                'breed2_desc': 'Il Labrador Retriever è la razza più popolare al mondo, nota per la sua natura amichevole e socievole.',
            },
        },
    },
    'ja': {
        'name': 'Japanese',
        'html_lang': 'ja',
        'ui': {
            'all_breeds': 'すべての犬種',
            'compare': '比較',
            'take_quiz': 'クイズに挑戦',
            'comparisons': '比較記事',
            'complete_comparison': '完全比較',
            'side_by_side': '並べて比較',
            'attribute': '属性',
            'size': 'サイズ',
            'lifespan': '寿命',
            'energy_level': 'エネルギーレベル',
            'grooming_needs': 'グルーミング',
            'trainability': 'しつけやすさ',
            'kid_friendly': '子供との相性',
            'apartment': 'マンション適性',
            'shedding': '抜け毛',
            'origin': '原産国',
            'temperament': '性格',
            'exercise_needs': '運動量',
            'grooming_req': 'お手入れ',
            'which_right': 'あなたに合うのはどっち？',
            'choose_if': '{breed}を選ぶなら...',
            'bottom_line': 'まとめ',
            'more_comparisons': 'その他の比較',
            'back_to_compare': '← 比較ツールに戻る',
            'view_profile': '詳細を見る →',
            'large': '大型',
            'medium': '中型',
            'small': '小型',
            'years': '年',
            'very_high': '非常に高い',
            'high': '高い',
            'moderate': '普通',
            'low': '低い',
            'excellent': '優秀',
            'good': '良い',
            'not_ideal': '不向き',
            'heavy': '多い',
            'dog_breed_comparisons': '犬種比較',
            'popular_comparisons_desc': '人気の犬種比較。あなたにぴったりの犬種を見つけましょう。',
            'helping_find': '最高のパートナー探しをお手伝い。',
        },
        'comparisons': {
            'labrador-vs-golden': {
                'slug': 'labrador-vs-golden-retriever',
                'breed1': 'ラブラドール・レトリバー',
                'breed2': 'ゴールデン・レトリバー',
                'breed1_slug': 'labrador-retriever',
                'breed2_slug': 'golden-retriever',
                'title': 'ラブラドール vs ゴールデン・レトリバー：完全比較',
                'desc': 'ラブラドールとゴールデン・レトリバーを比較。サイズ、性格、運動量、家族との相性を並べて解説。',
                'intro': '世界で最も愛されている家庭犬の2大巨頭。どちらもフレンドリーで賢く、子供との相性も抜群—でも、あなたに合うのはどっち？',
                'breed1_tagline': '世界No.1の人気犬種',
                'breed2_tagline': '家族のアイドル',
                'breed1_desc': 'ラブラドール・レトリバーは世界で最も人気のある犬種。フレンドリーで社交的、愛情いっぱいの最高の相棒です。',
                'breed2_desc': 'ゴールデン・レトリバーは最も人気のある犬種の一つ。優しく寛容な性格で素晴らしい家庭犬になります。',
            },
            'frenchie-vs-boston': {
                'slug': 'french-bulldog-vs-boston-terrier',
                'breed1': 'フレンチ・ブルドッグ',
                'breed2': 'ボストン・テリア',
                'breed1_slug': 'french-bulldog',
                'breed2_slug': 'boston-terrier',
                'title': 'フレンチ・ブルドッグ vs ボストン・テリア：完全比較',
                'desc': 'フレブルとボストン・テリアを比較。コンパクトな人気犬種を徹底解説。',
                'intro': '魅力的でコンパクトな2つの犬種。どちらもマンション暮らしに最適—でも、あなたのライフスタイルに合うのは？',
                'breed1_tagline': '魅惑のフレンチ',
                'breed2_tagline': 'アメリカの紳士',
                'breed1_desc': 'フレンチ・ブルドッグは愛らしく適応力の高い犬種。コウモリ耳と献身的な性格が魅力です。',
                'breed2_desc': 'ボストン・テリアは「アメリカの紳士」として知られ、フレンドリーで陽気な性格の活発な小型犬です。',
            },
            'gsd-vs-malinois': {
                'slug': 'german-shepherd-vs-malinois',
                'breed1': 'ジャーマン・シェパード',
                'breed2': 'ベルジアン・マリノア',
                'breed1_slug': 'german-shepherd',
                'breed2_slug': 'belgian-malinois',
                'title': 'ジャーマン・シェパード vs マリノア：完全比較',
                'desc': 'シェパードとマリノアを比較。2大ワーキングドッグを徹底解説。',
                'intro': '世界最高峰のワーキングドッグ対決。警察犬・軍用犬として活躍する両者の重要な違いとは。',
                'breed1_tagline': '万能の守護者',
                'breed2_tagline': 'エリート作業犬',
                'breed1_desc': 'ジャーマン・シェパードは万能で賢く、世界で最も人気のあるワーキングドッグの一つです。',
                'breed2_desc': 'ベルジアン・マリノアは集中力と能力が高く、世界中の警察・軍で採用されています。',
            },
            'husky-vs-malamute': {
                'slug': 'husky-vs-malamute',
                'breed1': 'シベリアン・ハスキー',
                'breed2': 'アラスカン・マラミュート',
                'breed1_slug': 'siberian-husky',
                'breed2_slug': 'alaskan-malamute',
                'title': 'ハスキー vs マラミュート：完全比較',
                'desc': 'ハスキーとマラミュートを比較。北極犬種を並べて解説。',
                'intro': 'オオカミのような外見を持つ2つの北極犬種。似ているようで、サイズと性格に重要な違いがあります。',
                'breed1_tagline': '俊足のそり犬',
                'breed2_tagline': 'パワフルな重量犬',
                'breed1_desc': 'シベリアン・ハスキーは運動能力が高く持久力のあるそり犬。青い瞳とフレンドリーな性格が魅力。',
                'breed2_desc': 'アラスカン・マラミュートはパワフルで頑丈なそり犬。力強さと持久力のために改良されました。',
            },
            'poodle-vs-labrador': {
                'slug': 'poodle-vs-labrador',
                'breed1': 'プードル',
                'breed2': 'ラブラドール・レトリバー',
                'breed1_slug': 'poodle',
                'breed2_slug': 'labrador-retriever',
                'title': 'プードル vs ラブラドール：完全比較',
                'desc': 'プードルとラブラドールを比較。賢くて人気の2犬種を解説。',
                'intro': '最も賢くて人気のある2つの犬種。どちらも素晴らしい家庭犬ですが、被毛は大きく異なります。',
                'breed1_tagline': 'エレガントなアスリート',
                'breed2_tagline': 'みんなの親友',
                'breed1_desc': 'プードルは非常に賢く活発。エレガントな外見の下には、運動神経抜群で賢い犬が隠れています。',
                'breed2_desc': 'ラブラドール・レトリバーは世界で最も人気のある犬種。フレンドリーで社交的な性格が魅力です。',
            },
        },
    },
    'nl': {
        'name': 'Dutch',
        'html_lang': 'nl',
        'ui': {
            'all_breeds': 'Alle Rassen',
            'compare': 'Vergelijk',
            'take_quiz': 'Doe de Quiz',
            'comparisons': 'Vergelijkingen',
            'complete_comparison': 'Complete Vergelijking',
            'side_by_side': 'Zij aan Zij Vergelijking',
            'attribute': 'Eigenschap',
            'size': 'Grootte',
            'lifespan': 'Levensduur',
            'energy_level': 'Energieniveau',
            'grooming_needs': 'Verzorgingsbehoefte',
            'trainability': 'Trainbaarheid',
            'kid_friendly': 'Kindvriendelijk',
            'apartment': 'Geschikt voor Appartement',
            'shedding': 'Verharing',
            'origin': 'Herkomst',
            'temperament': 'Temperament',
            'exercise_needs': 'Bewegingsbehoefte',
            'grooming_req': 'Verzorgingseisen',
            'which_right': 'Welke is Geschikt voor Jou?',
            'choose_if': 'Kies een {breed} als...',
            'bottom_line': 'Conclusie',
            'more_comparisons': 'Meer Vergelijkingen',
            'back_to_compare': '← Terug naar Vergelijk',
            'view_profile': 'Bekijk volledig profiel →',
            'large': 'Groot',
            'medium': 'Middelgroot',
            'small': 'Klein',
            'years': 'jaar',
            'very_high': 'Zeer Hoog',
            'high': 'Hoog',
            'moderate': 'Gemiddeld',
            'low': 'Laag',
            'excellent': 'Uitstekend',
            'good': 'Goed',
            'not_ideal': 'Niet Ideaal',
            'heavy': 'Veel',
            'dog_breed_comparisons': 'Hondenras Vergelijkingen',
            'popular_comparisons_desc': 'Populaire hondenras vergelijkingen. Vind het perfecte ras voor jou.',
            'helping_find': 'We helpen je je perfecte metgezel te vinden.',
        },
        'comparisons': {
            'labrador-vs-golden': {
                'slug': 'labrador-vs-golden-retriever',
                'breed1': 'Labrador Retriever',
                'breed2': 'Golden Retriever',
                'breed1_slug': 'labrador-retriever',
                'breed2_slug': 'golden-retriever',
                'title': 'Labrador Retriever vs Golden Retriever: Complete Vergelijking',
                'desc': 'Labrador vs Golden Retriever vergelijking. Bekijk grootte, temperament, bewegingsbehoefte en gezinsvriendelijkheid.',
                'intro': 'Twee van de meest geliefde familiehonden ter wereld. Beide zijn vriendelijk, intelligent en geweldig met kinderen—maar welke past bij jou?',
                'breed1_tagline': '\'s Werelds #1 Ras',
                'breed2_tagline': 'De Familie Favoriet',
                'breed1_desc': 'De Labrador Retriever is het populairste hondenras ter wereld. Ze zijn vriendelijk, extravert en liefdevolle metgezellen.',
                'breed2_desc': 'De Golden Retriever is een van de populairste hondenrassen. Hun vriendelijke, tolerante houding maakt hen fantastische huisdieren.',
            },
            'frenchie-vs-boston': {
                'slug': 'franse-bulldog-vs-boston-terrier',
                'breed1': 'Franse Bulldog',
                'breed2': 'Boston Terriër',
                'breed1_slug': 'french-bulldog',
                'breed2_slug': 'boston-terrier',
                'title': 'Franse Bulldog vs Boston Terriër: Complete Vergelijking',
                'desc': 'Franse Bulldog vs Boston Terriër vergelijking. Compacte metgezellen vergeleken.',
                'intro': 'Twee charmante, compacte rassen met grote persoonlijkheden. Beide geweldig voor appartementleven—maar welke past bij jouw levensstijl?',
                'breed1_tagline': 'De Charmante Fransman',
                'breed2_tagline': 'De Amerikaanse Gentleman',
                'breed1_desc': 'De Franse Bulldog is een charmant, aanpasbaar ras met een speelse persoonlijkheid, bekend om zijn vleermuisoren.',
                'breed2_desc': 'De Boston Terriër, bekend als "De Amerikaanse Gentleman", is een levendige kleine hond met een vriendelijk temperament.',
            },
            'gsd-vs-malinois': {
                'slug': 'duitse-herder-vs-mechelse-herder',
                'breed1': 'Duitse Herder',
                'breed2': 'Mechelse Herder',
                'breed1_slug': 'german-shepherd',
                'breed2_slug': 'belgian-malinois',
                'title': 'Duitse Herder vs Mechelse Herder: Complete Vergelijking',
                'desc': 'Duitse Herder vs Mechelse Herder vergelijking. Twee uitstekende werkhonden vergeleken.',
                'intro': 'Twee van de meest capabele werkhonden ter wereld. Beide excelleren in politie- en militair werk—maar hebben belangrijke verschillen.',
                'breed1_tagline': 'De Veelzijdige Beschermer',
                'breed2_tagline': 'Elite Werkhond',
                'breed1_desc': 'De Duitse Herder is veelzijdig, intelligent en een van de populairste werkhondenrassen ter wereld.',
                'breed2_desc': 'De Mechelse Herder is een intense, hoogpresterende werkhond, favoriet bij politie en militairen wereldwijd.',
            },
            'husky-vs-malamute': {
                'slug': 'husky-vs-malamute',
                'breed1': 'Siberische Husky',
                'breed2': 'Alaskan Malamute',
                'breed1_slug': 'siberian-husky',
                'breed2_slug': 'alaskan-malamute',
                'title': 'Siberische Husky vs Alaskan Malamute: Complete Vergelijking',
                'desc': 'Husky vs Malamute vergelijking. Arctische rassen vergeleken.',
                'intro': 'Twee majestueuze arctische rassen met een wolfsachtig uiterlijk. Ze lijken op elkaar maar hebben belangrijke verschillen.',
                'breed1_tagline': 'De Snelle Sledehond',
                'breed2_tagline': 'De Krachtige Trekker',
                'breed1_desc': 'De Siberische Husky is een atletische, uithoudenide sledehond bekend om zijn blauwe ogen en vriendelijke persoonlijkheid.',
                'breed2_desc': 'De Alaskan Malamute is een krachtige, zwaargebouwde sledehond gefokt voor kracht en uithoudingsvermogen.',
            },
            'poodle-vs-labrador': {
                'slug': 'poedel-vs-labrador',
                'breed1': 'Poedel',
                'breed2': 'Labrador Retriever',
                'breed1_slug': 'poodle',
                'breed2_slug': 'labrador-retriever',
                'title': 'Poedel vs Labrador Retriever: Complete Vergelijking',
                'desc': 'Poedel vs Labrador vergelijking. Twee intelligente, populaire rassen vergeleken.',
                'intro': 'Twee van de intelligentste en populairste hondenrassen. Beide uitstekende familiehonden met zeer verschillende vachten.',
                'breed1_tagline': 'De Elegante Atleet',
                'breed2_tagline': 'Ieders Beste Vriend',
                'breed1_desc': 'De Poedel is uitzonderlijk intelligent en actief. Achter het elegante uiterlijk schuilt een atletische, slimme hond.',
                'breed2_desc': 'De Labrador Retriever is het populairste hondenras ter wereld, bekend om zijn vriendelijke, extraverte aard.',
            },
        },
    },
    'no': {
        'name': 'Norwegian',
        'html_lang': 'no',
        'ui': {
            'all_breeds': 'Alle Raser',
            'compare': 'Sammenlign',
            'take_quiz': 'Ta Quizen',
            'comparisons': 'Sammenligninger',
            'complete_comparison': 'Komplett Sammenligning',
            'side_by_side': 'Side ved Side Sammenligning',
            'attribute': 'Egenskap',
            'size': 'Størrelse',
            'lifespan': 'Levetid',
            'energy_level': 'Energinivå',
            'grooming_needs': 'Stell',
            'trainability': 'Trenbarhet',
            'kid_friendly': 'Barnevennlig',
            'apartment': 'Egnet for Leilighet',
            'shedding': 'Hårfelling',
            'origin': 'Opprinnelse',
            'temperament': 'Temperament',
            'exercise_needs': 'Mosjonsbehov',
            'grooming_req': 'Stellkrav',
            'which_right': 'Hvilken Passer for Deg?',
            'choose_if': 'Velg en {breed} hvis...',
            'bottom_line': 'Konklusjon',
            'more_comparisons': 'Flere Sammenligninger',
            'back_to_compare': '← Tilbake til Sammenlign',
            'view_profile': 'Se full profil →',
            'large': 'Stor',
            'medium': 'Mellomstor',
            'small': 'Liten',
            'years': 'år',
            'very_high': 'Veldig Høy',
            'high': 'Høy',
            'moderate': 'Moderat',
            'low': 'Lav',
            'excellent': 'Utmerket',
            'good': 'God',
            'not_ideal': 'Ikke Ideell',
            'heavy': 'Mye',
            'dog_breed_comparisons': 'Hunderase Sammenligninger',
            'popular_comparisons_desc': 'Populære hunderase sammenligninger. Finn den perfekte rasen for deg.',
            'helping_find': 'Vi hjelper deg finne din perfekte følgesvenn.',
        },
        'comparisons': {
            'labrador-vs-golden': {
                'slug': 'labrador-vs-golden-retriever',
                'breed1': 'Labrador Retriever',
                'breed2': 'Golden Retriever',
                'breed1_slug': 'labrador-retriever',
                'breed2_slug': 'golden-retriever',
                'title': 'Labrador Retriever vs Golden Retriever: Komplett Sammenligning',
                'desc': 'Labrador vs Golden Retriever sammenligning. Se størrelse, temperament, mosjonsbehov og familievennlighet.',
                'intro': 'To av verdens mest elskede familiehunder. Begge er vennlige, intelligente og flotte med barn—men hvilken passer for deg?',
                'breed1_tagline': 'Verdens #1 Rase',
                'breed2_tagline': 'Familiens Favoritt',
                'breed1_desc': 'Labrador Retrieveren er verdens mest populære hunderase. De er vennlige, utadvendte og livlige følgesvenner.',
                'breed2_desc': 'Golden Retrieveren er en av de mest populære hunderasene. Deres vennlige, tolerante holdning gjør dem til fantastiske familiedyr.',
            },
            'frenchie-vs-boston': {
                'slug': 'fransk-bulldog-vs-boston-terrier',
                'breed1': 'Fransk Bulldog',
                'breed2': 'Boston Terrier',
                'breed1_slug': 'french-bulldog',
                'breed2_slug': 'boston-terrier',
                'title': 'Fransk Bulldog vs Boston Terrier: Komplett Sammenligning',
                'desc': 'Fransk Bulldog vs Boston Terrier sammenligning. Kompakte følgesvenner sammenlignet.',
                'intro': 'To sjarmerende, kompakte raser med store personligheter. Begge flotte for leilighetslivet—men hvilken passer din livsstil?',
                'breed1_tagline': 'Den Sjarmerende Franskmann',
                'breed2_tagline': 'Den Amerikanske Gentleman',
                'breed1_desc': 'Fransk Bulldog er en sjarmerende, tilpasningsdyktig rase med en leken personlighet, kjent for sine flaggermusører.',
                'breed2_desc': 'Boston Terrier, kjent som "Den Amerikanske Gentleman", er en livlig liten hund med et vennlig temperament.',
            },
            'gsd-vs-malinois': {
                'slug': 'schaefer-vs-malinois',
                'breed1': 'Schæferhund',
                'breed2': 'Belgisk Malinois',
                'breed1_slug': 'german-shepherd',
                'breed2_slug': 'belgian-malinois',
                'title': 'Schæferhund vs Belgisk Malinois: Komplett Sammenligning',
                'desc': 'Schæferhund vs Malinois sammenligning. To utmerkede brukshunder sammenlignet.',
                'intro': 'To av verdens mest kapable brukshunder. Begge utmerker seg i politi- og militærarbeid—men har viktige forskjeller.',
                'breed1_tagline': 'Den Allsidige Beskytter',
                'breed2_tagline': 'Elite Brukshund',
                'breed1_desc': 'Schæferhunden er allsidig, intelligent og en av verdens mest populære brukshunderaser.',
                'breed2_desc': 'Belgisk Malinois er en intens, høytytende brukshund foretrukket av politi og militær verden over.',
            },
            'husky-vs-malamute': {
                'slug': 'husky-vs-malamute',
                'breed1': 'Siberian Husky',
                'breed2': 'Alaskan Malamute',
                'breed1_slug': 'siberian-husky',
                'breed2_slug': 'alaskan-malamute',
                'title': 'Siberian Husky vs Alaskan Malamute: Komplett Sammenligning',
                'desc': 'Husky vs Malamute sammenligning. Arktiske raser sammenlignet.',
                'intro': 'To majestetiske arktiske raser med ulvelignende utseende. De ligner hverandre men har viktige forskjeller.',
                'breed1_tagline': 'Den Raske Sledehunden',
                'breed2_tagline': 'Den Kraftfulle Trekkeren',
                'breed1_desc': 'Siberian Husky er en atletisk, utholdende sledehund kjent for sine blå øyne og vennlige personlighet.',
                'breed2_desc': 'Alaskan Malamute er en kraftfull, tungt bygd sledehund avlet for styrke og utholdenhet.',
            },
            'poodle-vs-labrador': {
                'slug': 'puddel-vs-labrador',
                'breed1': 'Puddel',
                'breed2': 'Labrador Retriever',
                'breed1_slug': 'poodle',
                'breed2_slug': 'labrador-retriever',
                'title': 'Puddel vs Labrador Retriever: Komplett Sammenligning',
                'desc': 'Puddel vs Labrador sammenligning. To intelligente, populære raser sammenlignet.',
                'intro': 'To av de mest intelligente og populære hunderasene. Begge utmerkede familiehunder med svært forskjellige pelser.',
                'breed1_tagline': 'Den Elegante Atleten',
                'breed2_tagline': 'Alles Beste Venn',
                'breed1_desc': 'Puddelen er eksepsjonelt intelligent og aktiv. Bak det elegante utseendet skjuler det seg en atletisk, smart hund.',
                'breed2_desc': 'Labrador Retriever er verdens mest populære hunderase, kjent for sin vennlige, utadvendte natur.',
            },
        },
    },
    'pl': {
        'name': 'Polish',
        'html_lang': 'pl',
        'ui': {
            'all_breeds': 'Wszystkie Rasy',
            'compare': 'Porównaj',
            'take_quiz': 'Zrób Quiz',
            'comparisons': 'Porównania',
            'complete_comparison': 'Pełne Porównanie',
            'side_by_side': 'Porównanie Obok Siebie',
            'attribute': 'Cecha',
            'size': 'Rozmiar',
            'lifespan': 'Długość Życia',
            'energy_level': 'Poziom Energii',
            'grooming_needs': 'Pielęgnacja',
            'trainability': 'Łatwość Szkolenia',
            'kid_friendly': 'Przyjazny Dzieciom',
            'apartment': 'Do Mieszkania',
            'shedding': 'Linienie',
            'origin': 'Pochodzenie',
            'temperament': 'Temperament',
            'exercise_needs': 'Potrzeby Ruchu',
            'grooming_req': 'Wymagania Pielęgnacji',
            'which_right': 'Która Jest Dla Ciebie?',
            'choose_if': 'Wybierz {breed} jeśli...',
            'bottom_line': 'Podsumowanie',
            'more_comparisons': 'Więcej Porównań',
            'back_to_compare': '← Powrót do Porównaj',
            'view_profile': 'Zobacz pełny profil →',
            'large': 'Duży',
            'medium': 'Średni',
            'small': 'Mały',
            'years': 'lat',
            'very_high': 'Bardzo Wysoki',
            'high': 'Wysoki',
            'moderate': 'Umiarkowany',
            'low': 'Niski',
            'excellent': 'Doskonały',
            'good': 'Dobry',
            'not_ideal': 'Nieodpowiedni',
            'heavy': 'Intensywne',
            'dog_breed_comparisons': 'Porównania Ras Psów',
            'popular_comparisons_desc': 'Popularne porównania ras psów. Znajdź idealną rasę dla siebie.',
            'helping_find': 'Pomagamy znaleźć idealnego towarzysza.',
        },
        'comparisons': {
            'labrador-vs-golden': {
                'slug': 'labrador-vs-golden-retriever',
                'breed1': 'Labrador Retriever',
                'breed2': 'Golden Retriever',
                'breed1_slug': 'labrador-retriever',
                'breed2_slug': 'golden-retriever',
                'title': 'Labrador Retriever vs Golden Retriever: Pełne Porównanie',
                'desc': 'Porównanie Labrador vs Golden Retriever. Zobacz rozmiar, temperament, potrzeby ruchu i przyjazność rodzinną.',
                'intro': 'Dwie z najbardziej kochanych ras rodzinnych na świecie. Obie są przyjazne, inteligentne i świetne z dziećmi—ale która jest dla ciebie?',
                'breed1_tagline': 'Rasa #1 na Świecie',
                'breed2_tagline': 'Ulubieniec Rodzin',
                'breed1_desc': 'Labrador Retriever to najpopularniejsza rasa psa na świecie. Są przyjazne, towarzyskie i pełne energii.',
                'breed2_desc': 'Golden Retriever to jedna z najpopularniejszych ras. Ich przyjazny, tolerancyjny charakter czyni je wspaniałymi zwierzętami domowymi.',
            },
            'frenchie-vs-boston': {
                'slug': 'buldog-francuski-vs-boston-terrier',
                'breed1': 'Buldog Francuski',
                'breed2': 'Boston Terrier',
                'breed1_slug': 'french-bulldog',
                'breed2_slug': 'boston-terrier',
                'title': 'Buldog Francuski vs Boston Terrier: Pełne Porównanie',
                'desc': 'Porównanie Buldog Francuski vs Boston Terrier. Kompaktowi towarzysze porównani.',
                'intro': 'Dwie urocze, kompaktowe rasy z wielkimi osobowościami. Obie świetne do mieszkania—ale która pasuje do twojego stylu życia?',
                'breed1_tagline': 'Uroczy Francuz',
                'breed2_tagline': 'Amerykański Dżentelmen',
                'breed1_desc': 'Buldog Francuski to urocza, łatwo adaptująca się rasa z zabawną osobowością, znana z uszu nietoperza.',
                'breed2_desc': 'Boston Terrier, znany jako "Amerykański Dżentelmen", to żywy mały pies o przyjaznym temperamencie.',
            },
            'gsd-vs-malinois': {
                'slug': 'owczarek-niemiecki-vs-malinois',
                'breed1': 'Owczarek Niemiecki',
                'breed2': 'Owczarek Belgijski Malinois',
                'breed1_slug': 'german-shepherd',
                'breed2_slug': 'belgian-malinois',
                'title': 'Owczarek Niemiecki vs Malinois: Pełne Porównanie',
                'desc': 'Porównanie Owczarek Niemiecki vs Malinois. Dwa doskonałe psy robocze porównane.',
                'intro': 'Dwa z najbardziej zdolnych psów roboczych na świecie. Oba doskonale sprawdzają się w pracy policyjnej i wojskowej.',
                'breed1_tagline': 'Wszechstronny Obrońca',
                'breed2_tagline': 'Elitarny Pies Roboczy',
                'breed1_desc': 'Owczarek Niemiecki jest wszechstronny, inteligentny i jedną z najpopularniejszych ras roboczych na świecie.',
                'breed2_desc': 'Owczarek Belgijski Malinois to intensywny, wysoko wydajny pies roboczy, preferowany przez policję i wojsko.',
            },
            'husky-vs-malamute': {
                'slug': 'husky-vs-malamute',
                'breed1': 'Siberian Husky',
                'breed2': 'Alaskan Malamute',
                'breed1_slug': 'siberian-husky',
                'breed2_slug': 'alaskan-malamute',
                'title': 'Siberian Husky vs Alaskan Malamute: Pełne Porównanie',
                'desc': 'Porównanie Husky vs Malamute. Rasy arktyczne porównane.',
                'intro': 'Dwie majestatyczne rasy arktyczne o wyglądzie podobnym do wilka. Wyglądają podobnie, ale mają ważne różnice.',
                'breed1_tagline': 'Szybki Pies Zaprzęgowy',
                'breed2_tagline': 'Potężny Ciągnik',
                'breed1_desc': 'Siberian Husky to atletyczny, wytrzymały pies zaprzęgowy znany z niebieskich oczu i przyjaznej osobowości.',
                'breed2_desc': 'Alaskan Malamute to potężny, masywny pies zaprzęgowy hodowany dla siły i wytrzymałości.',
            },
            'poodle-vs-labrador': {
                'slug': 'pudel-vs-labrador',
                'breed1': 'Pudel',
                'breed2': 'Labrador Retriever',
                'breed1_slug': 'poodle',
                'breed2_slug': 'labrador-retriever',
                'title': 'Pudel vs Labrador Retriever: Pełne Porównanie',
                'desc': 'Porównanie Pudel vs Labrador. Dwie inteligentne, popularne rasy porównane.',
                'intro': 'Dwie z najbardziej inteligentnych i popularnych ras psów. Obie są doskonałymi psami rodzinnymi z bardzo różnymi sierściami.',
                'breed1_tagline': 'Elegancki Atleta',
                'breed2_tagline': 'Najlepszy Przyjaciel Wszystkich',
                'breed1_desc': 'Pudel jest wyjątkowo inteligentny i aktywny. Za eleganckim wyglądem kryje się atletyczny, bystry pies.',
                'breed2_desc': 'Labrador Retriever to najpopularniejsza rasa psa na świecie, znana z przyjaznej, towarzyskiej natury.',
            },
        },
    },
    'pt': {
        'name': 'Portuguese',
        'html_lang': 'pt',
        'ui': {
            'all_breeds': 'Todas as Raças',
            'compare': 'Comparar',
            'take_quiz': 'Fazer Quiz',
            'comparisons': 'Comparações',
            'complete_comparison': 'Comparação Completa',
            'side_by_side': 'Comparação Lado a Lado',
            'attribute': 'Atributo',
            'size': 'Tamanho',
            'lifespan': 'Expectativa de Vida',
            'energy_level': 'Nível de Energia',
            'grooming_needs': 'Necessidades de Tosa',
            'trainability': 'Treinabilidade',
            'kid_friendly': 'Bom com Crianças',
            'apartment': 'Apto para Apartamento',
            'shedding': 'Queda de Pelo',
            'origin': 'Origem',
            'temperament': 'Temperamento',
            'exercise_needs': 'Necessidades de Exercício',
            'grooming_req': 'Requisitos de Tosa',
            'which_right': 'Qual é o Certo para Você?',
            'choose_if': 'Escolha um {breed} se...',
            'bottom_line': 'Conclusão',
            'more_comparisons': 'Mais Comparações',
            'back_to_compare': '← Voltar para Comparar',
            'view_profile': 'Ver perfil completo →',
            'large': 'Grande',
            'medium': 'Médio',
            'small': 'Pequeno',
            'years': 'anos',
            'very_high': 'Muito Alto',
            'high': 'Alto',
            'moderate': 'Moderado',
            'low': 'Baixo',
            'excellent': 'Excelente',
            'good': 'Bom',
            'not_ideal': 'Não Ideal',
            'heavy': 'Intensa',
            'dog_breed_comparisons': 'Comparações de Raças de Cães',
            'popular_comparisons_desc': 'Comparações populares de raças de cães. Encontre a raça perfeita para você.',
            'helping_find': 'Ajudando você a encontrar seu companheiro perfeito.',
        },
        'comparisons': {
            'labrador-vs-golden': {
                'slug': 'labrador-vs-golden-retriever',
                'breed1': 'Labrador Retriever',
                'breed2': 'Golden Retriever',
                'breed1_slug': 'labrador-retriever',
                'breed2_slug': 'golden-retriever',
                'title': 'Labrador Retriever vs Golden Retriever: Comparação Completa',
                'desc': 'Comparação Labrador vs Golden Retriever. Veja tamanho, temperamento, necessidades de exercício e adequação familiar.',
                'intro': 'Duas das raças familiares mais amadas do mundo. Ambas são amigáveis, inteligentes e ótimas com crianças—mas qual é a certa para você?',
                'breed1_tagline': 'Raça #1 do Mundo',
                'breed2_tagline': 'O Favorito das Famílias',
                'breed1_desc': 'O Labrador Retriever é a raça de cão mais popular do mundo. São amigáveis, extrovertidos e companheiros cheios de energia.',
                'breed2_desc': 'O Golden Retriever é uma das raças mais populares. Sua atitude amigável e tolerante os torna ótimos animais de estimação.',
            },
            'frenchie-vs-boston': {
                'slug': 'buldogue-frances-vs-boston-terrier',
                'breed1': 'Buldogue Francês',
                'breed2': 'Boston Terrier',
                'breed1_slug': 'french-bulldog',
                'breed2_slug': 'boston-terrier',
                'title': 'Buldogue Francês vs Boston Terrier: Comparação Completa',
                'desc': 'Comparação Buldogue Francês vs Boston Terrier. Companheiros compactos comparados.',
                'intro': 'Duas raças charmosas e compactas com grandes personalidades. Ambas ótimas para vida em apartamento—mas qual se adapta ao seu estilo de vida?',
                'breed1_tagline': 'O Francês Charmoso',
                'breed2_tagline': 'O Cavalheiro Americano',
                'breed1_desc': 'O Buldogue Francês é uma raça charmosa e adaptável com personalidade brincalhona, conhecido por suas orelhas de morcego.',
                'breed2_desc': 'O Boston Terrier, conhecido como "O Cavalheiro Americano", é um cão pequeno e animado com temperamento amigável.',
            },
            'gsd-vs-malinois': {
                'slug': 'pastor-alemao-vs-malinois',
                'breed1': 'Pastor Alemão',
                'breed2': 'Malinois Belga',
                'breed1_slug': 'german-shepherd',
                'breed2_slug': 'belgian-malinois',
                'title': 'Pastor Alemão vs Malinois Belga: Comparação Completa',
                'desc': 'Comparação Pastor Alemão vs Malinois. Dois excelentes cães de trabalho comparados.',
                'intro': 'Dois dos cães de trabalho mais capazes do mundo. Ambos se destacam em trabalho policial e militar—mas têm diferenças importantes.',
                'breed1_tagline': 'O Protetor Versátil',
                'breed2_tagline': 'Cão de Trabalho de Elite',
                'breed1_desc': 'O Pastor Alemão é versátil, inteligente e uma das raças de trabalho mais populares do mundo.',
                'breed2_desc': 'O Malinois Belga é um cão de trabalho intenso e de alto desempenho, preferido por polícias e militares.',
            },
            'husky-vs-malamute': {
                'slug': 'husky-vs-malamute',
                'breed1': 'Husky Siberiano',
                'breed2': 'Malamute do Alasca',
                'breed1_slug': 'siberian-husky',
                'breed2_slug': 'alaskan-malamute',
                'title': 'Husky Siberiano vs Malamute do Alasca: Comparação Completa',
                'desc': 'Comparação Husky vs Malamute. Raças árticas comparadas.',
                'intro': 'Duas raças árticas majestosas com aparência de lobo. Parecem semelhantes mas têm diferenças importantes em tamanho e temperamento.',
                'breed1_tagline': 'O Cão de Trenó Veloz',
                'breed2_tagline': 'O Poderoso Puxador',
                'breed1_desc': 'O Husky Siberiano é um cão de trenó atlético e resistente, conhecido por seus olhos azuis e personalidade amigável.',
                'breed2_desc': 'O Malamute do Alasca é um cão de trenó poderoso e robusto, criado para força e resistência.',
            },
            'poodle-vs-labrador': {
                'slug': 'poodle-vs-labrador',
                'breed1': 'Poodle',
                'breed2': 'Labrador Retriever',
                'breed1_slug': 'poodle',
                'breed2_slug': 'labrador-retriever',
                'title': 'Poodle vs Labrador Retriever: Comparação Completa',
                'desc': 'Comparação Poodle vs Labrador. Duas raças inteligentes e populares comparadas.',
                'intro': 'Duas das raças de cães mais inteligentes e populares. Ambas excelentes cães de família com pelagens muito diferentes.',
                'breed1_tagline': 'O Atleta Elegante',
                'breed2_tagline': 'O Melhor Amigo de Todos',
                'breed1_desc': 'O Poodle é excepcionalmente inteligente e ativo. Por trás da aparência elegante há um cão atlético e muito esperto.',
                'breed2_desc': 'O Labrador Retriever é a raça mais popular do mundo, conhecida por sua natureza amigável e extrovertida.',
            },
        },
    },
    'ru': {
        'name': 'Russian',
        'html_lang': 'ru',
        'ui': {
            'all_breeds': 'Все Породы',
            'compare': 'Сравнить',
            'take_quiz': 'Пройти Тест',
            'comparisons': 'Сравнения',
            'complete_comparison': 'Полное Сравнение',
            'side_by_side': 'Сравнение Бок о Бок',
            'attribute': 'Характеристика',
            'size': 'Размер',
            'lifespan': 'Продолжительность Жизни',
            'energy_level': 'Уровень Энергии',
            'grooming_needs': 'Уход',
            'trainability': 'Обучаемость',
            'kid_friendly': 'Дружелюбие к Детям',
            'apartment': 'Для Квартиры',
            'shedding': 'Линька',
            'origin': 'Происхождение',
            'temperament': 'Темперамент',
            'exercise_needs': 'Потребность в Нагрузке',
            'grooming_req': 'Требования по Уходу',
            'which_right': 'Какая Подходит Вам?',
            'choose_if': 'Выберите {breed} если...',
            'bottom_line': 'Итог',
            'more_comparisons': 'Больше Сравнений',
            'back_to_compare': '← Назад к Сравнению',
            'view_profile': 'Смотреть полный профиль →',
            'large': 'Крупная',
            'medium': 'Средняя',
            'small': 'Маленькая',
            'years': 'лет',
            'very_high': 'Очень Высокий',
            'high': 'Высокий',
            'moderate': 'Умеренный',
            'low': 'Низкий',
            'excellent': 'Отлично',
            'good': 'Хорошо',
            'not_ideal': 'Не Подходит',
            'heavy': 'Сильная',
            'dog_breed_comparisons': 'Сравнения Пород Собак',
            'popular_comparisons_desc': 'Популярные сравнения пород собак. Найдите идеальную породу для вас.',
            'helping_find': 'Помогаем найти идеального компаньона.',
        },
        'comparisons': {
            'labrador-vs-golden': {
                'slug': 'labrador-vs-golden-retriever',
                'breed1': 'Лабрадор Ретривер',
                'breed2': 'Золотистый Ретривер',
                'breed1_slug': 'labrador-retriever',
                'breed2_slug': 'golden-retriever',
                'title': 'Лабрадор vs Золотистый Ретривер: Полное Сравнение',
                'desc': 'Сравнение Лабрадора и Золотистого Ретривера. Размер, темперамент, потребности в нагрузке и семейная совместимость.',
                'intro': 'Две из самых любимых семейных пород в мире. Обе дружелюбные, умные и отличные с детьми—но какая подходит вам?',
                'breed1_tagline': 'Порода #1 в Мире',
                'breed2_tagline': 'Любимец Семей',
                'breed1_desc': 'Лабрадор Ретривер — самая популярная порода собак в мире. Они дружелюбные, общительные и энергичные компаньоны.',
                'breed2_desc': 'Золотистый Ретривер — одна из самых популярных пород. Их дружелюбный, терпеливый характер делает их отличными домашними питомцами.',
            },
            'frenchie-vs-boston': {
                'slug': 'francuzskij-buldog-vs-boston-terer',
                'breed1': 'Французский Бульдог',
                'breed2': 'Бостон Терьер',
                'breed1_slug': 'french-bulldog',
                'breed2_slug': 'boston-terrier',
                'title': 'Французский Бульдог vs Бостон Терьер: Полное Сравнение',
                'desc': 'Сравнение Французского Бульдога и Бостон Терьера. Компактные компаньоны в сравнении.',
                'intro': 'Две очаровательные, компактные породы с большими личностями. Обе отлично подходят для квартиры—но какая соответствует вашему образу жизни?',
                'breed1_tagline': 'Очаровательный Француз',
                'breed2_tagline': 'Американский Джентльмен',
                'breed1_desc': 'Французский Бульдог — очаровательная, адаптивная порода с игривым характером, известная своими ушами летучей мыши.',
                'breed2_desc': 'Бостон Терьер, известный как "Американский Джентльмен" — живая маленькая собака с дружелюбным темпераментом.',
            },
            'gsd-vs-malinois': {
                'slug': 'nemeckaja-ovcharka-vs-malinua',
                'breed1': 'Немецкая Овчарка',
                'breed2': 'Бельгийская Малинуа',
                'breed1_slug': 'german-shepherd',
                'breed2_slug': 'belgian-malinois',
                'title': 'Немецкая Овчарка vs Малинуа: Полное Сравнение',
                'desc': 'Сравнение Немецкой Овчарки и Малинуа. Две превосходные рабочие породы.',
                'intro': 'Две из самых способных рабочих пород в мире. Обе превосходны в полицейской и военной службе—но имеют важные различия.',
                'breed1_tagline': 'Универсальный Защитник',
                'breed2_tagline': 'Элитная Рабочая Собака',
                'breed1_desc': 'Немецкая Овчарка универсальна, умна и является одной из самых популярных рабочих пород в мире.',
                'breed2_desc': 'Бельгийская Малинуа — интенсивная, высокоэффективная рабочая собака, предпочитаемая полицией и военными.',
            },
            'husky-vs-malamute': {
                'slug': 'haski-vs-malamut',
                'breed1': 'Сибирский Хаски',
                'breed2': 'Аляскинский Маламут',
                'breed1_slug': 'siberian-husky',
                'breed2_slug': 'alaskan-malamute',
                'title': 'Хаски vs Маламут: Полное Сравнение',
                'desc': 'Сравнение Хаски и Маламута. Арктические породы в сравнении.',
                'intro': 'Две величественные арктические породы с волчьей внешностью. Похожи, но имеют важные различия в размере и темпераменте.',
                'breed1_tagline': 'Быстрая Ездовая Собака',
                'breed2_tagline': 'Мощный Тягач',
                'breed1_desc': 'Сибирский Хаски — атлетичная, выносливая ездовая собака, известная голубыми глазами и дружелюбным характером.',
                'breed2_desc': 'Аляскинский Маламут — мощная, крепко сложенная ездовая собака, выведенная для силы и выносливости.',
            },
            'poodle-vs-labrador': {
                'slug': 'pudel-vs-labrador',
                'breed1': 'Пудель',
                'breed2': 'Лабрадор Ретривер',
                'breed1_slug': 'poodle',
                'breed2_slug': 'labrador-retriever',
                'title': 'Пудель vs Лабрадор: Полное Сравнение',
                'desc': 'Сравнение Пуделя и Лабрадора. Две умные, популярные породы.',
                'intro': 'Две из самых умных и популярных пород собак. Обе отличные семейные собаки с очень разной шерстью.',
                'breed1_tagline': 'Элегантный Атлет',
                'breed2_tagline': 'Лучший Друг Всех',
                'breed1_desc': 'Пудель исключительно умён и активен. За элегантной внешностью скрывается атлетичная, сообразительная собака.',
                'breed2_desc': 'Лабрадор Ретривер — самая популярная порода в мире, известная дружелюбным, общительным характером.',
            },
        },
    },
    'sv': {
        'name': 'Swedish',
        'html_lang': 'sv',
        'ui': {
            'all_breeds': 'Alla Raser',
            'compare': 'Jämför',
            'take_quiz': 'Gör Quizet',
            'comparisons': 'Jämförelser',
            'complete_comparison': 'Komplett Jämförelse',
            'side_by_side': 'Jämförelse Sida vid Sida',
            'attribute': 'Egenskap',
            'size': 'Storlek',
            'lifespan': 'Livslängd',
            'energy_level': 'Energinivå',
            'grooming_needs': 'Pälsvård',
            'trainability': 'Träningsbarhet',
            'kid_friendly': 'Barnvänlig',
            'apartment': 'Passar Lägenhet',
            'shedding': 'Fällning',
            'origin': 'Ursprung',
            'temperament': 'Temperament',
            'exercise_needs': 'Motionsbehov',
            'grooming_req': 'Pälsvårdskrav',
            'which_right': 'Vilken Passar Dig?',
            'choose_if': 'Välj en {breed} om...',
            'bottom_line': 'Sammanfattning',
            'more_comparisons': 'Fler Jämförelser',
            'back_to_compare': '← Tillbaka till Jämför',
            'view_profile': 'Se fullständig profil →',
            'large': 'Stor',
            'medium': 'Medelstor',
            'small': 'Liten',
            'years': 'år',
            'very_high': 'Mycket Hög',
            'high': 'Hög',
            'moderate': 'Måttlig',
            'low': 'Låg',
            'excellent': 'Utmärkt',
            'good': 'Bra',
            'not_ideal': 'Ej Ideal',
            'heavy': 'Kraftig',
            'dog_breed_comparisons': 'Hundras Jämförelser',
            'popular_comparisons_desc': 'Populära hundras jämförelser. Hitta den perfekta rasen för dig.',
            'helping_find': 'Vi hjälper dig hitta din perfekta följeslagare.',
        },
        'comparisons': {
            'labrador-vs-golden': {
                'slug': 'labrador-vs-golden-retriever',
                'breed1': 'Labrador Retriever',
                'breed2': 'Golden Retriever',
                'breed1_slug': 'labrador-retriever',
                'breed2_slug': 'golden-retriever',
                'title': 'Labrador Retriever vs Golden Retriever: Komplett Jämförelse',
                'desc': 'Labrador vs Golden Retriever jämförelse. Se storlek, temperament, motionsbehov och familjevänlighet.',
                'intro': 'Två av världens mest älskade familjehundar. Båda är vänliga, intelligenta och fantastiska med barn—men vilken passar dig?',
                'breed1_tagline': 'Världens #1 Ras',
                'breed2_tagline': 'Familjens Favorit',
                'breed1_desc': 'Labrador Retrievern är världens populäraste hundras. De är vänliga, utåtriktade och livfulla följeslagare.',
                'breed2_desc': 'Golden Retrievern är en av de populäraste hundraserna. Deras vänliga, toleranta attityd gör dem till fantastiska familjedjur.',
            },
            'frenchie-vs-boston': {
                'slug': 'fransk-bulldog-vs-boston-terrier',
                'breed1': 'Fransk Bulldog',
                'breed2': 'Boston Terrier',
                'breed1_slug': 'french-bulldog',
                'breed2_slug': 'boston-terrier',
                'title': 'Fransk Bulldog vs Boston Terrier: Komplett Jämförelse',
                'desc': 'Fransk Bulldog vs Boston Terrier jämförelse. Kompakta följeslagare jämförda.',
                'intro': 'Två charmiga, kompakta raser med stora personligheter. Båda utmärkta för lägenhetsliv—men vilken passar din livsstil?',
                'breed1_tagline': 'Den Charmiga Fransmannen',
                'breed2_tagline': 'Den Amerikanske Gentlemannen',
                'breed1_desc': 'Fransk Bulldog är en charmig, anpassningsbar ras med en lekfull personlighet, känd för sina fladdermusöron.',
                'breed2_desc': 'Boston Terrier, känd som "Den Amerikanske Gentlemannen", är en livlig liten hund med ett vänligt temperament.',
            },
            'gsd-vs-malinois': {
                'slug': 'schaefer-vs-malinois',
                'breed1': 'Schäfer',
                'breed2': 'Belgisk Malinois',
                'breed1_slug': 'german-shepherd',
                'breed2_slug': 'belgian-malinois',
                'title': 'Schäfer vs Belgisk Malinois: Komplett Jämförelse',
                'desc': 'Schäfer vs Malinois jämförelse. Två utmärkta brukshundar jämförda.',
                'intro': 'Två av världens mest kapabla brukshundar. Båda utmärker sig i polis- och militärarbete—men har viktiga skillnader.',
                'breed1_tagline': 'Den Mångsidiga Beskyddaren',
                'breed2_tagline': 'Elit Brukshund',
                'breed1_desc': 'Schäfern är mångsidig, intelligent och en av världens populäraste brukshundraser.',
                'breed2_desc': 'Belgisk Malinois är en intensiv, högpresterande brukshund som föredras av polis och militär världen över.',
            },
            'husky-vs-malamute': {
                'slug': 'husky-vs-malamute',
                'breed1': 'Siberian Husky',
                'breed2': 'Alaskan Malamute',
                'breed1_slug': 'siberian-husky',
                'breed2_slug': 'alaskan-malamute',
                'title': 'Siberian Husky vs Alaskan Malamute: Komplett Jämförelse',
                'desc': 'Husky vs Malamute jämförelse. Arktiska raser jämförda.',
                'intro': 'Två majestätiska arktiska raser med varglikt utseende. De liknar varandra men har viktiga skillnader i storlek och temperament.',
                'breed1_tagline': 'Den Snabba Slädhunden',
                'breed2_tagline': 'Den Kraftfulla Dragaren',
                'breed1_desc': 'Siberian Husky är en atletisk, uthållig slädhund känd för sina blå ögon och vänliga personlighet.',
                'breed2_desc': 'Alaskan Malamute är en kraftfull, tungt byggd slädhund avlad för styrka och uthållighet.',
            },
            'poodle-vs-labrador': {
                'slug': 'pudel-vs-labrador',
                'breed1': 'Pudel',
                'breed2': 'Labrador Retriever',
                'breed1_slug': 'poodle',
                'breed2_slug': 'labrador-retriever',
                'title': 'Pudel vs Labrador Retriever: Komplett Jämförelse',
                'desc': 'Pudel vs Labrador jämförelse. Två intelligenta, populära raser jämförda.',
                'intro': 'Två av de intelligentaste och populäraste hundraserna. Båda utmärkta familjehundar med mycket olika pälsar.',
                'breed1_tagline': 'Den Eleganta Atleten',
                'breed2_tagline': 'Allas Bästa Vän',
                'breed1_desc': 'Pudeln är exceptionellt intelligent och aktiv. Bakom det eleganta utseendet döljer sig en atletisk, smart hund.',
                'breed2_desc': 'Labrador Retriever är världens populäraste hundras, känd för sin vänliga, utåtriktade natur.',
            },
        },
    },
    'tr': {
        'name': 'Turkish',
        'html_lang': 'tr',
        'ui': {
            'all_breeds': 'Tüm Irklar',
            'compare': 'Karşılaştır',
            'take_quiz': 'Teste Başla',
            'comparisons': 'Karşılaştırmalar',
            'complete_comparison': 'Tam Karşılaştırma',
            'side_by_side': 'Yan Yana Karşılaştırma',
            'attribute': 'Özellik',
            'size': 'Boyut',
            'lifespan': 'Ömür',
            'energy_level': 'Enerji Seviyesi',
            'grooming_needs': 'Bakım İhtiyacı',
            'trainability': 'Eğitilebilirlik',
            'kid_friendly': 'Çocuk Dostu',
            'apartment': 'Daireye Uygun',
            'shedding': 'Tüy Dökümü',
            'origin': 'Köken',
            'temperament': 'Mizaç',
            'exercise_needs': 'Egzersiz İhtiyacı',
            'grooming_req': 'Bakım Gereksinimleri',
            'which_right': 'Hangisi Size Uygun?',
            'choose_if': 'Eğer {breed} seçin...',
            'bottom_line': 'Sonuç',
            'more_comparisons': 'Daha Fazla Karşılaştırma',
            'back_to_compare': '← Karşılaştırmaya Dön',
            'view_profile': 'Tam profili gör →',
            'large': 'Büyük',
            'medium': 'Orta',
            'small': 'Küçük',
            'years': 'yıl',
            'very_high': 'Çok Yüksek',
            'high': 'Yüksek',
            'moderate': 'Orta',
            'low': 'Düşük',
            'excellent': 'Mükemmel',
            'good': 'İyi',
            'not_ideal': 'Uygun Değil',
            'heavy': 'Yoğun',
            'dog_breed_comparisons': 'Köpek Irkı Karşılaştırmaları',
            'popular_comparisons_desc': 'Popüler köpek ırkı karşılaştırmaları. Sizin için mükemmel ırkı bulun.',
            'helping_find': 'Mükemmel arkadaşınızı bulmanıza yardımcı oluyoruz.',
        },
        'comparisons': {
            'labrador-vs-golden': {
                'slug': 'labrador-vs-golden-retriever',
                'breed1': 'Labrador Retriever',
                'breed2': 'Golden Retriever',
                'breed1_slug': 'labrador-retriever',
                'breed2_slug': 'golden-retriever',
                'title': 'Labrador Retriever vs Golden Retriever: Tam Karşılaştırma',
                'desc': 'Labrador vs Golden Retriever karşılaştırması. Boyut, mizaç, egzersiz ihtiyaçları ve aile uyumluluğunu görün.',
                'intro': 'Dünyanın en sevilen iki aile köpeği. Her ikisi de dost canlısı, zeki ve çocuklarla harika—ama hangisi size uygun?',
                'breed1_tagline': 'Dünyanın #1 Irkı',
                'breed2_tagline': 'Ailenin Favorisi',
                'breed1_desc': 'Labrador Retriever dünyanın en popüler köpek ırkıdır. Dost canlısı, sosyal ve enerjik dostlardır.',
                'breed2_desc': 'Golden Retriever en popüler ırklardan biridir. Dost canlısı, hoşgörülü tavırları onları harika evcil hayvanlar yapar.',
            },
            'frenchie-vs-boston': {
                'slug': 'fransiz-bulldog-vs-boston-terrier',
                'breed1': 'Fransız Bulldog',
                'breed2': 'Boston Terrier',
                'breed1_slug': 'french-bulldog',
                'breed2_slug': 'boston-terrier',
                'title': 'Fransız Bulldog vs Boston Terrier: Tam Karşılaştırma',
                'desc': 'Fransız Bulldog vs Boston Terrier karşılaştırması. Kompakt dostlar karşılaştırıldı.',
                'intro': 'Büyük kişiliklere sahip iki çekici, kompakt ırk. Her ikisi de daire yaşamı için harika—ama hangisi yaşam tarzınıza uygun?',
                'breed1_tagline': 'Çekici Fransız',
                'breed2_tagline': 'Amerikan Beyefendisi',
                'breed1_desc': 'Fransız Bulldog, yarasa kulakları ile tanınan, oyuncu kişiliğe sahip çekici, uyumlu bir ırktır.',
                'breed2_desc': 'Boston Terrier, "Amerikan Beyefendisi" olarak bilinir, dost canlısı mizacıyla canlı küçük bir köpektir.',
            },
            'gsd-vs-malinois': {
                'slug': 'alman-coban-vs-malinois',
                'breed1': 'Alman Çoban Köpeği',
                'breed2': 'Belçika Malinois',
                'breed1_slug': 'german-shepherd',
                'breed2_slug': 'belgian-malinois',
                'title': 'Alman Çoban vs Malinois: Tam Karşılaştırma',
                'desc': 'Alman Çoban vs Malinois karşılaştırması. İki mükemmel çalışma köpeği karşılaştırıldı.',
                'intro': 'Dünyanın en yetenekli iki çalışma köpeği. Her ikisi de polis ve askeri işlerde mükemmel—ama önemli farklılıkları var.',
                'breed1_tagline': 'Çok Yönlü Koruyucu',
                'breed2_tagline': 'Elit Çalışma Köpeği',
                'breed1_desc': 'Alman Çoban Köpeği çok yönlü, zeki ve dünyanın en popüler çalışma köpeği ırklarından biridir.',
                'breed2_desc': 'Belçika Malinois, dünya genelinde polis ve askerler tarafından tercih edilen yoğun, yüksek performanslı bir çalışma köpeğidir.',
            },
            'husky-vs-malamute': {
                'slug': 'husky-vs-malamute',
                'breed1': 'Sibirya Husky',
                'breed2': 'Alaska Malamute',
                'breed1_slug': 'siberian-husky',
                'breed2_slug': 'alaskan-malamute',
                'title': 'Sibirya Husky vs Alaska Malamute: Tam Karşılaştırma',
                'desc': 'Husky vs Malamute karşılaştırması. Arktik ırklar karşılaştırıldı.',
                'intro': 'Kurt görünümlü iki görkemli arktik ırk. Benzer görünseler de boyut ve mizaçta önemli farklılıkları var.',
                'breed1_tagline': 'Hızlı Kızak Köpeği',
                'breed2_tagline': 'Güçlü Çekici',
                'breed1_desc': 'Sibirya Husky, mavi gözleri ve dost canlısı kişiliği ile tanınan atletik, dayanıklı bir kızak köpeğidir.',
                'breed2_desc': 'Alaska Malamute, güç ve dayanıklılık için yetiştirilmiş güçlü, iri yapılı bir kızak köpeğidir.',
            },
            'poodle-vs-labrador': {
                'slug': 'kaniş-vs-labrador',
                'breed1': 'Kaniş',
                'breed2': 'Labrador Retriever',
                'breed1_slug': 'poodle',
                'breed2_slug': 'labrador-retriever',
                'title': 'Kaniş vs Labrador Retriever: Tam Karşılaştırma',
                'desc': 'Kaniş vs Labrador karşılaştırması. İki zeki, popüler ırk karşılaştırıldı.',
                'intro': 'En zeki ve popüler iki köpek ırkı. Her ikisi de mükemmel aile köpekleri ama çok farklı tüylere sahipler.',
                'breed1_tagline': 'Zarif Atlet',
                'breed2_tagline': 'Herkesin En İyi Arkadaşı',
                'breed1_desc': 'Kaniş son derece zeki ve aktiftir. Zarif görünümün arkasında atletik, zeki bir köpek gizlidir.',
                'breed2_desc': 'Labrador Retriever dünyanın en popüler köpek ırkıdır, dost canlısı, sosyal doğasıyla tanınır.',
            },
        },
    },
    'zh': {
        'name': 'Chinese',
        'html_lang': 'zh',
        'ui': {
            'all_breeds': '所有品种',
            'compare': '比较',
            'take_quiz': '参加测验',
            'comparisons': '对比文章',
            'complete_comparison': '完整对比',
            'side_by_side': '并排对比',
            'attribute': '属性',
            'size': '体型',
            'lifespan': '寿命',
            'energy_level': '精力水平',
            'grooming_needs': '美容需求',
            'trainability': '可训练性',
            'kid_friendly': '儿童友好',
            'apartment': '适合公寓',
            'shedding': '掉毛',
            'origin': '原产地',
            'temperament': '性格',
            'exercise_needs': '运动需求',
            'grooming_req': '美容要求',
            'which_right': '哪种适合你？',
            'choose_if': '如果你...选择{breed}',
            'bottom_line': '总结',
            'more_comparisons': '更多对比',
            'back_to_compare': '← 返回比较',
            'view_profile': '查看完整资料 →',
            'large': '大型',
            'medium': '中型',
            'small': '小型',
            'years': '年',
            'very_high': '非常高',
            'high': '高',
            'moderate': '中等',
            'low': '低',
            'excellent': '优秀',
            'good': '良好',
            'not_ideal': '不理想',
            'heavy': '严重',
            'dog_breed_comparisons': '犬种对比',
            'popular_comparisons_desc': '热门犬种对比。找到最适合你的品种。',
            'helping_find': '帮助您找到完美的伴侣。',
        },
        'comparisons': {
            'labrador-vs-golden': {
                'slug': 'labrador-vs-golden-retriever',
                'breed1': '拉布拉多犬',
                'breed2': '金毛寻回犬',
                'breed1_slug': 'labrador-retriever',
                'breed2_slug': 'golden-retriever',
                'title': '拉布拉多 vs 金毛寻回犬：完整对比',
                'desc': '拉布拉多与金毛寻回犬对比。了解体型、性格、运动需求和家庭适应性。',
                'intro': '世界上最受欢迎的两种家庭犬。都友好、聪明、对孩子很好——但哪种更适合你？',
                'breed1_tagline': '世界第一犬种',
                'breed2_tagline': '家庭最爱',
                'breed1_desc': '拉布拉多犬是世界上最受欢迎的犬种。它们友好、外向、充满活力。',
                'breed2_desc': '金毛寻回犬是最受欢迎的犬种之一。它们友好、宽容的性格使它们成为出色的家庭宠物。',
            },
            'frenchie-vs-boston': {
                'slug': 'faguo-dougou-vs-boston-geng',
                'breed1': '法国斗牛犬',
                'breed2': '波士顿梗',
                'breed1_slug': 'french-bulldog',
                'breed2_slug': 'boston-terrier',
                'title': '法国斗牛犬 vs 波士顿梗：完整对比',
                'desc': '法国斗牛犬与波士顿梗对比。紧凑型伴侣犬对比。',
                'intro': '两种迷人的紧凑型犬种，都有大大的个性。都适合公寓生活——但哪种更适合你的生活方式？',
                'breed1_tagline': '迷人的法国犬',
                'breed2_tagline': '美国绅士',
                'breed1_desc': '法国斗牛犬是迷人、适应性强的犬种，以蝙蝠耳和活泼个性著称。',
                'breed2_desc': '波士顿梗被称为"美国绅士"，是一种活泼的小型犬，性格友好。',
            },
            'gsd-vs-malinois': {
                'slug': 'demumuyangquan-vs-malinuoa',
                'breed1': '德国牧羊犬',
                'breed2': '比利时马林诺斯',
                'breed1_slug': 'german-shepherd',
                'breed2_slug': 'belgian-malinois',
                'title': '德国牧羊犬 vs 马林诺斯：完整对比',
                'desc': '德国牧羊犬与马林诺斯对比。两种优秀的工作犬对比。',
                'intro': '世界上最优秀的两种工作犬。都在警察和军事工作中表现出色——但有重要区别。',
                'breed1_tagline': '全能保护者',
                'breed2_tagline': '精英工作犬',
                'breed1_desc': '德国牧羊犬多才多艺、聪明，是世界上最受欢迎的工作犬种之一。',
                'breed2_desc': '比利时马林诺斯是一种高强度、高性能的工作犬，受到世界各地警察和军队的青睐。',
            },
            'husky-vs-malamute': {
                'slug': 'hashiqi-vs-alasijia-xuedequan',
                'breed1': '西伯利亚哈士奇',
                'breed2': '阿拉斯加雪橇犬',
                'breed1_slug': 'siberian-husky',
                'breed2_slug': 'alaskan-malamute',
                'title': '哈士奇 vs 阿拉斯加雪橇犬：完整对比',
                'desc': '哈士奇与阿拉斯加雪橇犬对比。北极犬种对比。',
                'intro': '两种外表像狼的壮丽北极犬种。看起来相似，但在体型和性格上有重要区别。',
                'breed1_tagline': '快速雪橇犬',
                'breed2_tagline': '强壮的拖拉犬',
                'breed1_desc': '西伯利亚哈士奇是一种运动型、耐力强的雪橇犬，以蓝眼睛和友好性格著称。',
                'breed2_desc': '阿拉斯加雪橇犬是一种强壮、体格健壮的雪橇犬，为力量和耐力而培育。',
            },
            'poodle-vs-labrador': {
                'slug': 'guibinquan-vs-labrador',
                'breed1': '贵宾犬',
                'breed2': '拉布拉多犬',
                'breed1_slug': 'poodle',
                'breed2_slug': 'labrador-retriever',
                'title': '贵宾犬 vs 拉布拉多：完整对比',
                'desc': '贵宾犬与拉布拉多对比。两种聪明、受欢迎的犬种对比。',
                'intro': '两种最聪明、最受欢迎的犬种。都是出色的家庭犬，但毛发非常不同。',
                'breed1_tagline': '优雅的运动员',
                'breed2_tagline': '所有人的好朋友',
                'breed1_desc': '贵宾犬非常聪明且活跃。优雅的外表下是一只运动型、聪明的狗。',
                'breed2_desc': '拉布拉多犬是世界上最受欢迎的犬种，以友好、外向的性格著称。',
            },
        },
    },
}


def generate_index_page(lang_code, lang_config):
    """Generate the index page for comparison articles."""
    ui = lang_config['ui']
    comparisons = lang_config['comparisons']
    
    # Build comparison cards
    cards_html = ""
    for key, comp in comparisons.items():
        cards_html += f'''
                <a href="{comp['slug']}.html" class="bg-white p-6 rounded-xl shadow-sm hover:shadow-lg transition group">
                    <div class="flex items-center gap-4 mb-3">
                        <img src="../../../images/heads/{comp['breed1_slug']}.webp" alt="{comp['breed1']}" class="w-12 h-12 rounded-full object-cover">
                        <span class="text-slate-400 font-bold">vs</span>
                        <img src="../../../images/heads/{comp['breed2_slug']}.webp" alt="{comp['breed2']}" class="w-12 h-12 rounded-full object-cover">
                    </div>
                    <h2 class="text-lg font-bold text-slate-800 group-hover:text-sky-700 transition">{comp['breed1']} vs {comp['breed2']}</h2>
                </a>'''
    
    html = f'''<!DOCTYPE html>
<html lang="{lang_config['html_lang']}">
<head>
    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-VEERQZ53LZ"></script>
    <script>window.dataLayer = window.dataLayer || []; function gtag(){{dataLayer.push(arguments);}} gtag("js", new Date()); gtag("config", "G-VEERQZ53LZ");</script>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{ui['dog_breed_comparisons']} | BreedFinder</title>
    <meta name="description" content="{ui['popular_comparisons_desc']}">
    <link rel="canonical" href="https://breedfinder.org/{lang_code}/compare/comparisons/">
    
    <link rel="icon" href="../../../favicon.ico" type="image/x-icon">
    <link rel="icon" type="image/png" sizes="32x32" href="../../../favicon-32.png">
    <link rel="apple-touch-icon" sizes="180x180" href="../../../apple-touch-icon.png">
    
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://breedfinder.org/{lang_code}/compare/comparisons/">
    <meta property="og:title" content="{ui['dog_breed_comparisons']}">
    <meta property="og:description" content="{ui['popular_comparisons_desc']}">
    <meta property="og:site_name" content="BreedFinder">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    </style>

    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": "{ui['dog_breed_comparisons']}",
        "description": "{ui['popular_comparisons_desc']}",
        "publisher": {{
            "@type": "Organization",
            "name": "BreedFinder"
        }}
    }}
    </script>
</head>
<body class="bg-gradient-to-br from-sky-50 via-white to-blue-50 min-h-screen text-slate-800">
    <!-- Header -->
    <header class="bg-white/80 backdrop-blur-md border-b border-slate-100 sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
            <a href="../../" class="flex items-center gap-3">
                <div class="w-10 h-10 bg-gradient-to-br from-sky-500 to-blue-600 rounded-xl flex items-center justify-center text-white shadow-lg shadow-sky-500/20">
                    <img src="../../../logo-192.png" class="w-10 h-10" alt="BreedFinder">
                </div>
                <span class="text-xl font-bold bg-gradient-to-r from-slate-800 to-slate-600 bg-clip-text text-transparent">BreedFinder</span>
            </a>
            <nav class="flex items-center gap-6 text-sm font-medium">
                <a href="../../breeds" class="text-slate-600 hover:text-sky-700 transition">{ui['all_breeds']}</a>
                <a href="../" class="text-slate-600 hover:text-sky-700 transition">{ui['compare']}</a>
                <a href="../../quiz" class="bg-gradient-to-r from-sky-500 to-blue-600 text-white px-5 py-2.5 rounded-xl font-semibold hover:shadow-lg hover:shadow-sky-500/25 transition">{ui['take_quiz']}</a>
            </nav>
        </div>
    </header>

    <main class="max-w-6xl mx-auto px-4 py-12">
        <div class="text-center mb-12">
            <h1 class="text-4xl md:text-5xl font-extrabold mb-4 bg-gradient-to-r from-slate-800 to-slate-600 bg-clip-text text-transparent">
                {ui['dog_breed_comparisons']}
            </h1>
            <p class="text-lg text-slate-600 max-w-2xl mx-auto">{ui['popular_comparisons_desc']}</p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {cards_html}
        </div>

        <div class="text-center mt-12">
            <a href="../" class="inline-flex items-center gap-2 text-sky-700 font-semibold hover:text-sky-700">
                {ui['back_to_compare']}
            </a>
        </div>
    </main>

    <!-- Footer -->
    <footer class="border-t border-slate-100 mt-16 py-8">
        <div class="max-w-6xl mx-auto px-4 text-center text-slate-600 text-sm">
            <p>© 2026 BreedFinder. {ui['helping_find']}</p>
        </div>
    </footer>
</body>
</html>'''
    
    return html


def generate_comparison_article(lang_code, lang_config, comp_key):
    """Generate a single comparison article."""
    ui = lang_config['ui']
    comp = lang_config['comparisons'][comp_key]
    all_comps = lang_config['comparisons']
    
    # Get related comparisons (exclude current)
    related = [(k, v) for k, v in all_comps.items() if k != comp_key][:3]
    
    related_html = ""
    for key, rel in related:
        related_html += f'''
                <a href="{rel['slug']}.html" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md transition">
                    <span class="font-semibold">{rel['breed1']} vs {rel['breed2']}</span>
                </a>'''
    
    html = f'''<!DOCTYPE html>
<html lang="{lang_config['html_lang']}">
<head>
    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-VEERQZ53LZ"></script>
    <script>window.dataLayer = window.dataLayer || []; function gtag(){{dataLayer.push(arguments);}} gtag("js", new Date()); gtag("config", "G-VEERQZ53LZ");</script>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{comp['title']} | BreedFinder</title>
    <meta name="description" content="{comp['desc']}">
    <link rel="canonical" href="https://breedfinder.org/{lang_code}/compare/comparisons/{comp['slug']}.html">
    
    <link rel="icon" href="../../../favicon.ico" type="image/x-icon">
    <link rel="icon" type="image/png" sizes="32x32" href="../../../favicon-32.png">
    <link rel="apple-touch-icon" sizes="180x180" href="../../../apple-touch-icon.png">
    
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://breedfinder.org/{lang_code}/compare/comparisons/{comp['slug']}.html">
    <meta property="og:title" content="{comp['title']}">
    <meta property="og:description" content="{comp['desc']}">
    <meta property="og:site_name" content="BreedFinder">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    </style>

    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "{comp['title']}",
        "description": "{comp['desc']}",
        "author": {{
            "@type": "Organization",
            "name": "BreedFinder"
        }},
        "publisher": {{
            "@type": "Organization",
            "name": "BreedFinder",
            "logo": {{
                "@type": "ImageObject",
                "url": "https://breedfinder.org/logo-192.png"
            }}
        }},
        "mainEntityOfPage": {{
            "@type": "WebPage",
            "@id": "https://breedfinder.org/{lang_code}/compare/comparisons/{comp['slug']}.html"
        }}
    }}
    </script>
</head>
<body class="bg-gradient-to-br from-sky-50 via-white to-blue-50 min-h-screen text-slate-800">
    <!-- Header -->
    <header class="bg-white/80 backdrop-blur-md border-b border-slate-100 sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
            <a href="../../" class="flex items-center gap-3">
                <div class="w-10 h-10 bg-gradient-to-br from-sky-500 to-blue-600 rounded-xl flex items-center justify-center text-white shadow-lg shadow-sky-500/20">
                    <img src="../../../logo-192.png" class="w-10 h-10" alt="BreedFinder">
                </div>
                <span class="text-xl font-bold bg-gradient-to-r from-slate-800 to-slate-600 bg-clip-text text-transparent">BreedFinder</span>
            </a>
            <nav class="flex items-center gap-6 text-sm font-medium">
                <a href="../../breeds" class="text-slate-600 hover:text-sky-700 transition">{ui['all_breeds']}</a>
                <a href="../" class="text-slate-600 hover:text-sky-700 transition">{ui['compare']}</a>
                <a href="../../quiz" class="bg-gradient-to-r from-sky-500 to-blue-600 text-white px-5 py-2.5 rounded-xl font-semibold hover:shadow-lg hover:shadow-sky-500/25 transition">{ui['take_quiz']}</a>
            </nav>
        </div>
    </header>

    <main class="max-w-6xl mx-auto px-4 py-12">
        <!-- Breadcrumb -->
        <nav class="text-sm text-slate-600 mb-8">
            <a href="../" class="hover:text-sky-700">{ui['compare']}</a>
            <span class="mx-2">›</span>
            <a href="./" class="hover:text-sky-700">{ui['comparisons']}</a>
            <span class="mx-2">›</span>
            <span class="text-slate-700">{comp['breed1']} vs {comp['breed2']}</span>
        </nav>

        <!-- Header -->
        <div class="text-center mb-12">
            <h1 class="text-4xl md:text-5xl font-extrabold mb-4">
                <span class="bg-gradient-to-r from-amber-500 to-amber-600 bg-clip-text text-transparent">{comp['breed1']}</span>
                <span class="text-slate-600 mx-4">vs</span>
                <span class="bg-gradient-to-r from-yellow-500 to-yellow-600 bg-clip-text text-transparent">{comp['breed2']}</span>
            </h1>
            <p class="text-lg text-slate-600 max-w-2xl mx-auto">{comp['intro']}</p>
        </div>

        <!-- Breed Cards -->
        <div class="grid md:grid-cols-2 gap-8 mb-12">
            <!-- Breed 1 -->
            <div class="bg-white rounded-3xl shadow-xl shadow-slate-200/50 overflow-hidden">
                <div class="bg-gradient-to-r from-amber-500 to-amber-600 p-6 text-white text-center">
                    <img src="../../../images/heads/{comp['breed1_slug']}.webp" alt="{comp['breed1']}" class="w-32 h-32 rounded-full mx-auto mb-4 object-cover border-4 border-white/30">
                    <h2 class="text-2xl font-bold">{comp['breed1']}</h2>
                    <p class="text-amber-100">{comp['breed1_tagline']}</p>
                </div>
                <div class="p-6">
                    <p class="text-slate-600 mb-4">{comp['breed1_desc']}</p>
                    <a href="../../breeds/{comp['breed1_slug']}" class="text-sky-700 font-semibold hover:text-sky-700">{ui['view_profile']}</a>
                </div>
            </div>

            <!-- Breed 2 -->
            <div class="bg-white rounded-3xl shadow-xl shadow-slate-200/50 overflow-hidden">
                <div class="bg-gradient-to-r from-yellow-500 to-yellow-600 p-6 text-white text-center">
                    <img src="../../../images/heads/{comp['breed2_slug']}.webp" alt="{comp['breed2']}" class="w-32 h-32 rounded-full mx-auto mb-4 object-cover border-4 border-white/30">
                    <h2 class="text-2xl font-bold">{comp['breed2']}</h2>
                    <p class="text-yellow-100">{comp['breed2_tagline']}</p>
                </div>
                <div class="p-6">
                    <p class="text-slate-600 mb-4">{comp['breed2_desc']}</p>
                    <a href="../../breeds/{comp['breed2_slug']}" class="text-sky-700 font-semibold hover:text-sky-700">{ui['view_profile']}</a>
                </div>
            </div>
        </div>

        <!-- Comparison Table -->
        <div class="bg-white rounded-3xl shadow-xl shadow-slate-200/50 overflow-hidden mb-12">
            <div class="bg-gradient-to-r from-slate-800 to-slate-700 p-6 text-white">
                <h2 class="text-2xl font-bold text-center">{ui['side_by_side']}</h2>
            </div>
            <table class="w-full">
                <thead>
                    <tr class="bg-slate-50">
                        <th class="p-4 text-left text-slate-600 font-semibold">{ui['attribute']}</th>
                        <th class="p-4 text-center text-amber-600 font-semibold">{comp['breed1']}</th>
                        <th class="p-4 text-center text-yellow-600 font-semibold">{comp['breed2']}</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-slate-100">
                    <tr>
                        <td class="p-4 font-medium text-slate-700">📏 {ui['size']}</td>
                        <td class="p-4 text-center font-semibold">{ui['large']}</td>
                        <td class="p-4 text-center font-semibold">{ui['large']}</td>
                    </tr>
                    <tr class="bg-slate-50/50">
                        <td class="p-4 font-medium text-slate-700">⏳ {ui['lifespan']}</td>
                        <td class="p-4 text-center font-semibold">10-12 {ui['years']}</td>
                        <td class="p-4 text-center font-semibold">10-12 {ui['years']}</td>
                    </tr>
                    <tr>
                        <td class="p-4 font-medium text-slate-700">⚡ {ui['energy_level']}</td>
                        <td class="p-4 text-center">
                            <div class="flex justify-center gap-1"><span class="text-amber-500">●●●●●</span></div>
                            <span class="text-sm text-slate-600">{ui['very_high']}</span>
                        </td>
                        <td class="p-4 text-center">
                            <div class="flex justify-center gap-1"><span class="text-yellow-500">●●●●○</span></div>
                            <span class="text-sm text-slate-600">{ui['high']}</span>
                        </td>
                    </tr>
                    <tr class="bg-slate-50/50">
                        <td class="p-4 font-medium text-slate-700">✂️ {ui['grooming_needs']}</td>
                        <td class="p-4 text-center">
                            <div class="flex justify-center gap-1"><span class="text-amber-500">●●○○○</span></div>
                            <span class="text-sm text-slate-600">{ui['moderate']}</span>
                        </td>
                        <td class="p-4 text-center">
                            <div class="flex justify-center gap-1"><span class="text-yellow-500">●●●○○</span></div>
                            <span class="text-sm text-slate-600">{ui['moderate']}</span>
                        </td>
                    </tr>
                    <tr>
                        <td class="p-4 font-medium text-slate-700">🎓 {ui['trainability']}</td>
                        <td class="p-4 text-center">
                            <div class="flex justify-center gap-1"><span class="text-amber-500">●●●●●</span></div>
                            <span class="text-sm text-slate-600">{ui['excellent']}</span>
                        </td>
                        <td class="p-4 text-center">
                            <div class="flex justify-center gap-1"><span class="text-yellow-500">●●●●●</span></div>
                            <span class="text-sm text-slate-600">{ui['excellent']}</span>
                        </td>
                    </tr>
                    <tr class="bg-slate-50/50">
                        <td class="p-4 font-medium text-slate-700">👶 {ui['kid_friendly']}</td>
                        <td class="p-4 text-center">
                            <div class="flex justify-center gap-1"><span class="text-amber-500">●●●●●</span></div>
                            <span class="text-sm text-slate-600">{ui['excellent']}</span>
                        </td>
                        <td class="p-4 text-center">
                            <div class="flex justify-center gap-1"><span class="text-yellow-500">●●●●●</span></div>
                            <span class="text-sm text-slate-600">{ui['excellent']}</span>
                        </td>
                    </tr>
                    <tr>
                        <td class="p-4 font-medium text-slate-700">🏠 {ui['apartment']}</td>
                        <td class="p-4 text-center">
                            <div class="flex justify-center gap-1"><span class="text-amber-500">●●○○○</span></div>
                            <span class="text-sm text-slate-600">{ui['not_ideal']}</span>
                        </td>
                        <td class="p-4 text-center">
                            <div class="flex justify-center gap-1"><span class="text-yellow-500">●●○○○</span></div>
                            <span class="text-sm text-slate-600">{ui['not_ideal']}</span>
                        </td>
                    </tr>
                    <tr class="bg-slate-50/50">
                        <td class="p-4 font-medium text-slate-700">🐕 {ui['shedding']}</td>
                        <td class="p-4 text-center font-semibold text-amber-600">{ui['high']}</td>
                        <td class="p-4 text-center font-semibold text-yellow-600">{ui['heavy']}</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Related Comparisons -->
        <div class="mb-12">
            <h2 class="text-2xl font-bold mb-6">{ui['more_comparisons']}</h2>
            <div class="grid md:grid-cols-3 gap-4">
                {related_html}
            </div>
        </div>

        <!-- Back Link -->
        <div class="text-center">
            <a href="../" class="inline-flex items-center gap-2 text-sky-700 font-semibold hover:text-sky-700">
                {ui['back_to_compare']}
            </a>
        </div>
    </main>

    <!-- Footer -->
    <footer class="border-t border-slate-100 mt-16 py-8">
        <div class="max-w-6xl mx-auto px-4 text-center text-slate-600 text-sm">
            <p>© 2026 BreedFinder. {ui['helping_find']}</p>
        </div>
    </footer>
</body>
</html>'''
    
    return html


def main():
    """Generate all comparison articles for all languages."""
    for lang_code, lang_config in LANGUAGES.items():
        print(f"\n{'='*50}")
        print(f"Generating {lang_config['name']} ({lang_code})...")
        print(f"{'='*50}")
        
        # Create directory
        output_dir = BASE_DIR / lang_code / 'compare' / 'comparisons'
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate index page
        index_html = generate_index_page(lang_code, lang_config)
        index_path = output_dir / 'index.html'
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_html)
        print(f"  ✅ {index_path.relative_to(BASE_DIR)}")
        
        # Generate comparison articles
        for comp_key in lang_config['comparisons']:
            comp = lang_config['comparisons'][comp_key]
            article_html = generate_comparison_article(lang_code, lang_config, comp_key)
            article_path = output_dir / f"{comp['slug']}.html"
            with open(article_path, 'w', encoding='utf-8') as f:
                f.write(article_html)
            print(f"  ✅ {article_path.relative_to(BASE_DIR)}")
    
    print(f"\n{'='*50}")
    print(f"✅ Generated {len(LANGUAGES)} languages × 6 files = {len(LANGUAGES) * 6} files")
    print(f"{'='*50}")


if __name__ == '__main__':
    main()
