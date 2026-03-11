#!/usr/bin/env python3
"""Fix popular breeds for remaining languages"""

import os

BREEDS = {
    'da': {
        'Labrador Retriever': 'Labrador Retriever',
        'German Shepherd': 'Schæferhund',
        'Golden Retriever': 'Golden Retriever',
        'French Bulldog': 'Fransk Bulldog',
        'Poodle': 'Puddel',
        'Siberian Husky': 'Sibirisk Husky',
        'Beagle': 'Beagle',
        'Dachshund': 'Gravhund',
        'Friendly · Active · Loyal': 'Venlig · Aktiv · Loyal',
        'Intelligent · Protective': 'Intelligent · Beskyttende',
        'Gentle · Friendly · Smart': 'Blid · Venlig · Klog',
        'Playful · Adaptable': 'Legesyg · Tilpasningsdygtig',
        'Intelligent · Elegant': 'Intelligent · Elegant',
        'Energetic · Outgoing': 'Energisk · Udadvendt',
        'Curious · Merry': 'Nysgerrig · Munter',
        'Clever · Devoted': 'Klog · Hengiven',
    },
    'nl': {
        'Labrador Retriever': 'Labrador Retriever',
        'German Shepherd': 'Duitse Herder',
        'Golden Retriever': 'Golden Retriever',
        'French Bulldog': 'Franse Bulldog',
        'Poodle': 'Poedel',
        'Siberian Husky': 'Siberische Husky',
        'Beagle': 'Beagle',
        'Dachshund': 'Teckel',
        'Friendly · Active · Loyal': 'Vriendelijk · Actief · Trouw',
        'Intelligent · Protective': 'Intelligent · Beschermend',
        'Gentle · Friendly · Smart': 'Zacht · Vriendelijk · Slim',
        'Playful · Adaptable': 'Speels · Aanpasbaar',
        'Intelligent · Elegant': 'Intelligent · Elegant',
        'Energetic · Outgoing': 'Energiek · Uitbundig',
        'Curious · Merry': 'Nieuwsgierig · Vrolijk',
        'Clever · Devoted': 'Slim · Toegewijd',
    },
    'no': {
        'Labrador Retriever': 'Labrador Retriever',
        'German Shepherd': 'Schæferhund',
        'Golden Retriever': 'Golden Retriever',
        'French Bulldog': 'Fransk Bulldog',
        'Poodle': 'Puddel',
        'Siberian Husky': 'Sibirsk Husky',
        'Beagle': 'Beagle',
        'Dachshund': 'Dachs',
        'Friendly · Active · Loyal': 'Vennlig · Aktiv · Lojal',
        'Intelligent · Protective': 'Intelligent · Beskyttende',
        'Gentle · Friendly · Smart': 'Mild · Vennlig · Smart',
        'Playful · Adaptable': 'Leken · Tilpasningsdyktig',
        'Intelligent · Elegant': 'Intelligent · Elegant',
        'Energetic · Outgoing': 'Energisk · Utadvendt',
        'Curious · Merry': 'Nysgjerrig · Munter',
        'Clever · Devoted': 'Klok · Hengiven',
    },
    'pl': {
        'Labrador Retriever': 'Labrador Retriever',
        'German Shepherd': 'Owczarek Niemiecki',
        'Golden Retriever': 'Golden Retriever',
        'French Bulldog': 'Buldog Francuski',
        'Poodle': 'Pudel',
        'Siberian Husky': 'Siberian Husky',
        'Beagle': 'Beagle',
        'Dachshund': 'Jamnik',
        'Friendly · Active · Loyal': 'Przyjazny · Aktywny · Lojalny',
        'Intelligent · Protective': 'Inteligentny · Opiekuńczy',
        'Gentle · Friendly · Smart': 'Łagodny · Przyjazny · Mądry',
        'Playful · Adaptable': 'Zabawny · Elastyczny',
        'Intelligent · Elegant': 'Inteligentny · Elegancki',
        'Energetic · Outgoing': 'Energiczny · Towarzyski',
        'Curious · Merry': 'Ciekawy · Wesoły',
        'Clever · Devoted': 'Bystry · Oddany',
    },
    'ru': {
        'Labrador Retriever': 'Лабрадор-ретривер',
        'German Shepherd': 'Немецкая овчарка',
        'Golden Retriever': 'Золотистый ретривер',
        'French Bulldog': 'Французский бульдог',
        'Poodle': 'Пудель',
        'Siberian Husky': 'Сибирский хаски',
        'Beagle': 'Бигль',
        'Dachshund': 'Такса',
        'Friendly · Active · Loyal': 'Дружелюбный · Активный · Верный',
        'Intelligent · Protective': 'Умный · Защитник',
        'Gentle · Friendly · Smart': 'Нежный · Дружелюбный · Умный',
        'Playful · Adaptable': 'Игривый · Адаптивный',
        'Intelligent · Elegant': 'Умный · Элегантный',
        'Energetic · Outgoing': 'Энергичный · Общительный',
        'Curious · Merry': 'Любопытный · Весёлый',
        'Clever · Devoted': 'Сообразительный · Преданный',
    },
    'sv': {
        'Labrador Retriever': 'Labrador Retriever',
        'German Shepherd': 'Schäfer',
        'Golden Retriever': 'Golden Retriever',
        'French Bulldog': 'Fransk Bulldogg',
        'Poodle': 'Pudel',
        'Siberian Husky': 'Sibirisk Husky',
        'Beagle': 'Beagle',
        'Dachshund': 'Tax',
        'Friendly · Active · Loyal': 'Vänlig · Aktiv · Lojal',
        'Intelligent · Protective': 'Intelligent · Skyddande',
        'Gentle · Friendly · Smart': 'Mild · Vänlig · Smart',
        'Playful · Adaptable': 'Lekfull · Anpassningsbar',
        'Intelligent · Elegant': 'Intelligent · Elegant',
        'Energetic · Outgoing': 'Energisk · Utåtriktad',
        'Curious · Merry': 'Nyfiken · Glad',
        'Clever · Devoted': 'Klok · Hängiven',
    },
    'tr': {
        'Labrador Retriever': 'Labrador Retriever',
        'German Shepherd': 'Alman Çoban Köpeği',
        'Golden Retriever': 'Golden Retriever',
        'French Bulldog': 'Fransız Bulldog',
        'Poodle': 'Kaniş',
        'Siberian Husky': 'Sibirya Husky',
        'Beagle': 'Beagle',
        'Dachshund': 'Dachshund',
        'Friendly · Active · Loyal': 'Dost Canlısı · Aktif · Sadık',
        'Intelligent · Protective': 'Zeki · Koruyucu',
        'Gentle · Friendly · Smart': 'Nazik · Dost · Akıllı',
        'Playful · Adaptable': 'Oyuncu · Uyumlu',
        'Intelligent · Elegant': 'Zeki · Zarif',
        'Energetic · Outgoing': 'Enerjik · Girişken',
        'Curious · Merry': 'Meraklı · Neşeli',
        'Clever · Devoted': 'Zeki · Sadık',
    },
    'ja': {
        'Labrador Retriever': 'ラブラドール・レトリーバー',
        'German Shepherd': 'ジャーマン・シェパード',
        'Golden Retriever': 'ゴールデン・レトリーバー',
        'French Bulldog': 'フレンチ・ブルドッグ',
        'Poodle': 'プードル',
        'Siberian Husky': 'シベリアン・ハスキー',
        'Beagle': 'ビーグル',
        'Dachshund': 'ダックスフント',
        'Friendly · Active · Loyal': 'フレンドリー · 活発 · 忠実',
        'Intelligent · Protective': '知的 · 保護的',
        'Gentle · Friendly · Smart': '穏やか · フレンドリー · 賢い',
        'Playful · Adaptable': '遊び好き · 順応性',
        'Intelligent · Elegant': '知的 · エレガント',
        'Energetic · Outgoing': 'エネルギッシュ · 社交的',
        'Curious · Merry': '好奇心旺盛 · 陽気',
        'Clever · Devoted': '賢い · 献身的',
    },
    'zh': {
        'Labrador Retriever': '拉布拉多寻回犬',
        'German Shepherd': '德国牧羊犬',
        'Golden Retriever': '金毛寻回犬',
        'French Bulldog': '法国斗牛犬',
        'Poodle': '贵宾犬',
        'Siberian Husky': '西伯利亚雪橇犬',
        'Beagle': '比格犬',
        'Dachshund': '腊肠犬',
        'Friendly · Active · Loyal': '友好 · 活跃 · 忠诚',
        'Intelligent · Protective': '聪明 · 保护性强',
        'Gentle · Friendly · Smart': '温和 · 友好 · 聪明',
        'Playful · Adaptable': '爱玩 · 适应性强',
        'Intelligent · Elegant': '聪明 · 优雅',
        'Energetic · Outgoing': '精力充沛 · 外向',
        'Curious · Merry': '好奇 · 快乐',
        'Clever · Devoted': '聪明 · 忠诚',
    },
}

def fix_language(lang, translations):
    filepath = f"{lang}/index.html"
    if not os.path.exists(filepath):
        return False
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    for eng, trans in translations.items():
        content = content.replace(f">{eng}</div>", f">{trans}</div>")
        content = content.replace(f">{eng}<", f">{trans}<")
    
    with open(filepath, 'w') as f:
        f.write(content)
    return True

for lang, trans in BREEDS.items():
    if fix_language(lang, trans):
        print(f"Fixed {lang}")

print("Done!")
