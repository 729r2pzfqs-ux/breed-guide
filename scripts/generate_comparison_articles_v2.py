#!/usr/bin/env python3
"""
Generate FULL in-depth comparison articles for 11 languages.
Includes: Temperament, Exercise, Grooming, Verdict sections.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

# Extended comparison data with all sections
COMPARISON_DATA = {
    'labrador-vs-golden': {
        'breed1_traits': ['Friendly', 'Outgoing', 'Active', 'Gentle', 'Intelligent', 'Trusting'],
        'breed2_traits': ['Intelligent', 'Friendly', 'Devoted', 'Reliable', 'Trustworthy', 'Kind'],
        'breed1_temperament_desc': 'Labs are famously friendly and bond with the whole family. They socialize well with neighbor dogs and humans alike. Don\'t mistake their easygoing personality for low energy—they need plenty of exercise!',
        'breed2_temperament_desc': 'Goldens are outgoing, trustworthy, and eager to please. They\'re wonderful with children and other pets. Their patient, gentle nature makes them excellent therapy dogs.',
        'breed1_exercise': 'High energy requiring at least 1-2 hours of vigorous daily exercise. They love swimming, fetching, and outdoor adventures.',
        'breed2_exercise': 'High energy but slightly less intense than Labs. At least 1 hour of daily exercise. They excel at fetch, swimming, and hiking.',
        'breed1_grooming': 'Weekly brushing, more during shedding season. Short, dense coat is relatively low-maintenance but sheds heavily.',
        'breed2_grooming': 'Daily brushing recommended during shedding season. Longer feathered coat needs more attention to prevent matting.',
        'breed1_reasons': ['You want the highest energy level', 'You prefer slightly less grooming', 'You want a versatile sporting dog', 'You love an outgoing, enthusiastic personality', 'Color variety matters (black, yellow, chocolate)'],
        'breed2_reasons': ['You prefer a slightly calmer demeanor', 'You love the flowing golden coat', 'You want an excellent therapy/service dog', 'You appreciate a gentle, patient disposition', 'You don\'t mind more frequent brushing'],
        'bottom_line': 'Both breeds make exceptional family dogs. Labs are slightly more energetic and lower-maintenance coat-wise, while Goldens are known for their gentle patience and flowing coats. Either choice will bring years of love and companionship to your family!',
    },
    'frenchie-vs-boston': {
        'breed1_traits': ['Playful', 'Adaptable', 'Smart', 'Affectionate', 'Patient', 'Alert'],
        'breed2_traits': ['Friendly', 'Bright', 'Amusing', 'Gentle', 'Lively', 'Intelligent'],
        'breed1_temperament_desc': 'Frenchies are easygoing and adaptable, thriving in city apartments or country homes alike. They\'re playful but not hyperactive, making them excellent companions for various lifestyles.',
        'breed2_temperament_desc': 'Boston Terriers are lively, highly intelligent, and have a gentle disposition. They\'re known for their tuxedo-like markings and friendly, amusing personality.',
        'breed1_exercise': 'Moderate exercise needs—short walks and play sessions suffice. Avoid overexertion in hot weather due to their flat faces.',
        'breed2_exercise': 'Moderate energy requiring daily walks and play. More athletic than Frenchies but still prone to overheating.',
        'breed1_grooming': 'Minimal grooming—weekly brushing. Clean facial wrinkles regularly to prevent infections.',
        'breed2_grooming': 'Low maintenance—occasional brushing. Their short coat is easy to care for.',
        'breed1_reasons': ['You want a calmer, more relaxed companion', 'You prefer a stockier build', 'You live in an apartment', 'You want minimal exercise requirements', 'You love those adorable bat ears'],
        'breed2_reasons': ['You want a slightly more active dog', 'You prefer the tuxedo look', 'You want a dog that\'s easier to train', 'You like a more athletic build', 'You want a longer-lived breed'],
        'bottom_line': 'Both are excellent apartment dogs with big personalities. Frenchies are calmer and more laid-back, while Bostons are slightly more energetic and athletic. Either will steal your heart!',
    },
    'gsd-vs-malinois': {
        'breed1_traits': ['Confident', 'Courageous', 'Smart', 'Loyal', 'Versatile', 'Protective'],
        'breed2_traits': ['Confident', 'Smart', 'Hardworking', 'Alert', 'Intense', 'Protective'],
        'breed1_temperament_desc': 'German Shepherds are confident, courageous, and incredibly versatile. They bond deeply with family and are naturally protective without being aggressive.',
        'breed2_temperament_desc': 'Malinois are intense, driven working dogs with endless energy. They need a job to do and thrive with experienced handlers who can channel their drive.',
        'breed1_exercise': 'High exercise needs—at least 2 hours daily. They excel at various dog sports, tracking, and obedience work.',
        'breed2_exercise': 'Very high exercise needs—2+ hours of intense activity daily. They need mental stimulation as much as physical exercise.',
        'breed1_grooming': 'Moderate grooming—brush 2-3 times weekly. Heavy seasonal shedding requires more attention.',
        'breed2_grooming': 'Easy grooming—weekly brushing. Shorter coat than GSD but still sheds seasonally.',
        'breed1_reasons': ['You want a versatile family protector', 'You prefer a slightly calmer working dog', 'You\'re a first-time working breed owner', 'You want a dog good with children', 'You prefer the classic look'],
        'breed2_reasons': ['You want maximum drive and intensity', 'You\'re an experienced handler', 'You want a top-tier sport/work dog', 'You can provide extensive exercise', 'You want a lighter, faster dog'],
        'bottom_line': 'Both are exceptional working dogs, but Malinois are more intense and require experienced handlers. GSDs are more versatile and better suited for families. Choose based on your experience level and lifestyle.',
    },
    'husky-vs-malamute': {
        'breed1_traits': ['Outgoing', 'Mischievous', 'Loyal', 'Friendly', 'Alert', 'Gentle'],
        'breed2_traits': ['Affectionate', 'Loyal', 'Playful', 'Dignified', 'Devoted', 'Strong'],
        'breed1_temperament_desc': 'Huskies are friendly, outgoing, and sometimes mischievous. They\'re pack dogs who love company and are known for their vocal nature and escape artist tendencies.',
        'breed2_temperament_desc': 'Malamutes are more dignified and less mischievous than Huskies. They\'re deeply loyal, affectionate with family, but can be more independent.',
        'breed1_exercise': 'Very high energy—designed to run for miles. At least 2 hours of vigorous exercise daily. They love running and pulling activities.',
        'breed2_exercise': 'High energy but with more endurance than speed. Long hikes and pulling work suit them well. They can overheat in warm climates.',
        'breed1_grooming': 'Heavy grooming—brush several times weekly. Massive seasonal shedding ("blowing coat") twice yearly.',
        'breed2_grooming': 'Heavy grooming similar to Husky. Their thicker coat requires regular brushing to prevent matting.',
        'breed1_reasons': ['You want a medium-sized arctic breed', 'You prefer a faster, more athletic dog', 'You enjoy a talkative, vocal companion', 'You want striking blue eyes', 'You like a more playful personality'],
        'breed2_reasons': ['You want a larger, more powerful dog', 'You prefer a calmer, more dignified temperament', 'You have experience with strong breeds', 'You want a quieter dog (less howling)', 'You need a dog for pulling/carting'],
        'bottom_line': 'Huskies are medium-sized athletes who love to run and talk. Malamutes are powerful giants built for strength. Both shed heavily and need lots of exercise. Choose based on size preference and desired temperament.',
    },
    'poodle-vs-labrador': {
        'breed1_traits': ['Intelligent', 'Active', 'Alert', 'Faithful', 'Trainable', 'Proud'],
        'breed2_traits': ['Friendly', 'Active', 'Outgoing', 'Gentle', 'Intelligent', 'Trusting'],
        'breed1_temperament_desc': 'Poodles are exceptionally intelligent and eager to please. Don\'t let the fancy haircuts fool you—they\'re athletic dogs bred for hunting and retrieving.',
        'breed2_temperament_desc': 'Labs are the quintessential friendly dog—outgoing with everyone, patient with children, and eager to please. They\'re the ultimate family companion.',
        'breed1_exercise': 'High energy requiring daily exercise and mental stimulation. They excel at agility, obedience, and various dog sports.',
        'breed2_exercise': 'High energy—at least 1-2 hours daily. They love swimming, fetching, and any activity involving their humans.',
        'breed1_grooming': 'High maintenance—professional grooming every 4-6 weeks. Daily brushing prevents matting. Hypoallergenic coat.',
        'breed2_grooming': 'Easy grooming but heavy shedding. Weekly brushing, more during shedding season. Not hypoallergenic.',
        'breed1_reasons': ['You have allergies (hypoallergenic)', 'You want minimal shedding', 'You enjoy grooming or don\'t mind the cost', 'You want an elegant appearance', 'You want size options (toy/mini/standard)'],
        'breed2_reasons': ['You prefer easy, low-cost grooming', 'You don\'t mind shedding', 'You want the classic family dog', 'You prefer a more casual look', 'You want a water-loving retriever'],
        'bottom_line': 'Both are highly intelligent and trainable. Poodles offer hypoallergenic coats but need more grooming. Labs are lower maintenance but shed heavily. Both make outstanding family companions!',
    },
}

# Language translations for extended content
LANG_TRANSLATIONS = {
    'no': {
        'temperament': 'Temperament',
        'exercise_needs': 'Mosjonsbehov',
        'grooming_req': 'Stellkrav',
        'which_right': 'Hvilken Passer for Deg?',
        'choose_breed': 'Velg en {breed} hvis...',
        'bottom_line': 'Konklusjon',
        # Trait translations
        'Friendly': 'Vennlig', 'Outgoing': 'Utadvendt', 'Active': 'Aktiv', 'Gentle': 'Mild',
        'Intelligent': 'Intelligent', 'Trusting': 'Tillitsfull', 'Devoted': 'Hengiven',
        'Reliable': 'Pålitelig', 'Trustworthy': 'Trofast', 'Kind': 'Snill',
        'Playful': 'Leken', 'Adaptable': 'Tilpasningsdyktig', 'Smart': 'Smart',
        'Affectionate': 'Kjærlig', 'Patient': 'Tålmodig', 'Alert': 'Årvåken',
        'Bright': 'Kvikk', 'Amusing': 'Morsom', 'Lively': 'Livlig',
        'Confident': 'Selvsikker', 'Courageous': 'Modig', 'Loyal': 'Lojal',
        'Versatile': 'Allsidig', 'Protective': 'Beskyttende', 'Hardworking': 'Arbeidsom',
        'Intense': 'Intens', 'Mischievous': 'Skøyeraktig', 'Dignified': 'Verdig',
        'Strong': 'Sterk', 'Faithful': 'Trofast', 'Trainable': 'Lærevillig', 'Proud': 'Stolt',
        # Extended content
        'breed1_temp_lab': 'Labradorer er kjent for å være vennlige og knytter sterke bånd med hele familien. De sosialiserer godt med naboer og hunder. Ikke la deres avslappede personlighet lure deg—de trenger mye mosjon!',
        'breed2_temp_golden': 'Golden Retrievere er utadvendte, troverdige og ivrige etter å behage. De er fantastiske med barn og andre kjæledyr. Deres tålmodige, milde natur gjør dem til utmerkede terapihunder.',
    },
    'da': {
        'temperament': 'Temperament',
        'exercise_needs': 'Motionsbehov',
        'grooming_req': 'Plejebehov',
        'which_right': 'Hvilken er den Rette for Dig?',
        'choose_breed': 'Vælg en {breed} hvis...',
        'bottom_line': 'Konklusion',
        'Friendly': 'Venlig', 'Outgoing': 'Udadvendt', 'Active': 'Aktiv', 'Gentle': 'Blid',
        'Intelligent': 'Intelligent', 'Trusting': 'Tillidsfuld', 'Devoted': 'Hengiven',
        'Reliable': 'Pålidelig', 'Trustworthy': 'Troværdig', 'Kind': 'Venlig',
        'Playful': 'Legesyg', 'Adaptable': 'Tilpasningsdygtig', 'Smart': 'Klog',
        'Affectionate': 'Kærlig', 'Patient': 'Tålmodig', 'Alert': 'Opmærksom',
        'Confident': 'Selvsikker', 'Courageous': 'Modig', 'Loyal': 'Loyal',
        'Versatile': 'Alsidig', 'Protective': 'Beskyttende',
    },
    'sv': {
        'temperament': 'Temperament',
        'exercise_needs': 'Motionsbehov',
        'grooming_req': 'Pälsvårdskrav',
        'which_right': 'Vilken Passar Dig?',
        'choose_breed': 'Välj en {breed} om...',
        'bottom_line': 'Sammanfattning',
        'Friendly': 'Vänlig', 'Outgoing': 'Utåtriktad', 'Active': 'Aktiv', 'Gentle': 'Mild',
        'Intelligent': 'Intelligent', 'Trusting': 'Tillitsfull', 'Devoted': 'Hängiven',
        'Reliable': 'Pålitlig', 'Trustworthy': 'Trovärdig', 'Kind': 'Snäll',
        'Playful': 'Lekfull', 'Adaptable': 'Anpassningsbar', 'Smart': 'Smart',
        'Affectionate': 'Kärleksfull', 'Patient': 'Tålmodig', 'Alert': 'Vaksam',
        'Confident': 'Självsäker', 'Courageous': 'Modig', 'Loyal': 'Lojal',
        'Versatile': 'Mångsidig', 'Protective': 'Beskyddande',
    },
    'nl': {
        'temperament': 'Temperament',
        'exercise_needs': 'Bewegingsbehoefte',
        'grooming_req': 'Verzorgingseisen',
        'which_right': 'Welke Past bij Jou?',
        'choose_breed': 'Kies een {breed} als...',
        'bottom_line': 'Conclusie',
        'Friendly': 'Vriendelijk', 'Outgoing': 'Extravert', 'Active': 'Actief', 'Gentle': 'Zacht',
        'Intelligent': 'Intelligent', 'Trusting': 'Vertrouwend', 'Devoted': 'Toegewijd',
        'Reliable': 'Betrouwbaar', 'Trustworthy': 'Trouw', 'Kind': 'Vriendelijk',
        'Playful': 'Speels', 'Adaptable': 'Aanpasbaar', 'Smart': 'Slim',
        'Affectionate': 'Aanhankelijk', 'Patient': 'Geduldig', 'Alert': 'Alert',
        'Confident': 'Zelfverzekerd', 'Courageous': 'Moedig', 'Loyal': 'Loyaal',
        'Versatile': 'Veelzijdig', 'Protective': 'Beschermend',
    },
    'it': {
        'temperament': 'Temperamento',
        'exercise_needs': 'Esigenze di Esercizio',
        'grooming_req': 'Requisiti di Toelettatura',
        'which_right': 'Qual è Quello Giusto per Te?',
        'choose_breed': 'Scegli un {breed} se...',
        'bottom_line': 'In Conclusione',
        'Friendly': 'Amichevole', 'Outgoing': 'Socievole', 'Active': 'Attivo', 'Gentle': 'Gentile',
        'Intelligent': 'Intelligente', 'Trusting': 'Fiducioso', 'Devoted': 'Devoto',
        'Reliable': 'Affidabile', 'Trustworthy': 'Fidato', 'Kind': 'Buono',
        'Playful': 'Giocoso', 'Adaptable': 'Adattabile', 'Smart': 'Sveglio',
        'Affectionate': 'Affettuoso', 'Patient': 'Paziente', 'Alert': 'Vigile',
        'Confident': 'Sicuro', 'Courageous': 'Coraggioso', 'Loyal': 'Leale',
        'Versatile': 'Versatile', 'Protective': 'Protettivo',
    },
    'pt': {
        'temperament': 'Temperamento',
        'exercise_needs': 'Necessidades de Exercício',
        'grooming_req': 'Requisitos de Tosa',
        'which_right': 'Qual é o Certo para Você?',
        'choose_breed': 'Escolha um {breed} se...',
        'bottom_line': 'Conclusão',
        'Friendly': 'Amigável', 'Outgoing': 'Extrovertido', 'Active': 'Ativo', 'Gentle': 'Gentil',
        'Intelligent': 'Inteligente', 'Trusting': 'Confiante', 'Devoted': 'Devotado',
        'Reliable': 'Confiável', 'Trustworthy': 'Leal', 'Kind': 'Bondoso',
        'Playful': 'Brincalhão', 'Adaptable': 'Adaptável', 'Smart': 'Esperto',
        'Affectionate': 'Afetuoso', 'Patient': 'Paciente', 'Alert': 'Alerta',
        'Confident': 'Confiante', 'Courageous': 'Corajoso', 'Loyal': 'Leal',
        'Versatile': 'Versátil', 'Protective': 'Protetor',
    },
    'pl': {
        'temperament': 'Temperament',
        'exercise_needs': 'Potrzeby Ruchu',
        'grooming_req': 'Wymagania Pielęgnacji',
        'which_right': 'Która Jest dla Ciebie?',
        'choose_breed': 'Wybierz {breed} jeśli...',
        'bottom_line': 'Podsumowanie',
        'Friendly': 'Przyjazny', 'Outgoing': 'Towarzyski', 'Active': 'Aktywny', 'Gentle': 'Łagodny',
        'Intelligent': 'Inteligentny', 'Trusting': 'Ufny', 'Devoted': 'Oddany',
        'Reliable': 'Niezawodny', 'Trustworthy': 'Wierny', 'Kind': 'Dobry',
        'Playful': 'Zabawny', 'Adaptable': 'Elastyczny', 'Smart': 'Bystry',
        'Affectionate': 'Czuły', 'Patient': 'Cierpliwy', 'Alert': 'Czujny',
        'Confident': 'Pewny siebie', 'Courageous': 'Odważny', 'Loyal': 'Lojalny',
        'Versatile': 'Wszechstronny', 'Protective': 'Opiekuńczy',
    },
    'ru': {
        'temperament': 'Темперамент',
        'exercise_needs': 'Потребность в Нагрузке',
        'grooming_req': 'Требования по Уходу',
        'which_right': 'Какая Подходит Вам?',
        'choose_breed': 'Выберите {breed} если...',
        'bottom_line': 'Итог',
        'Friendly': 'Дружелюбный', 'Outgoing': 'Общительный', 'Active': 'Активный', 'Gentle': 'Нежный',
        'Intelligent': 'Умный', 'Trusting': 'Доверчивый', 'Devoted': 'Преданный',
        'Reliable': 'Надёжный', 'Trustworthy': 'Верный', 'Kind': 'Добрый',
        'Playful': 'Игривый', 'Adaptable': 'Адаптивный', 'Smart': 'Сообразительный',
        'Affectionate': 'Ласковый', 'Patient': 'Терпеливый', 'Alert': 'Бдительный',
        'Confident': 'Уверенный', 'Courageous': 'Смелый', 'Loyal': 'Лояльный',
        'Versatile': 'Универсальный', 'Protective': 'Защитный',
    },
    'tr': {
        'temperament': 'Mizaç',
        'exercise_needs': 'Egzersiz İhtiyacı',
        'grooming_req': 'Bakım Gereksinimleri',
        'which_right': 'Hangisi Size Uygun?',
        'choose_breed': '{breed} seçin eğer...',
        'bottom_line': 'Sonuç',
        'Friendly': 'Dost Canlısı', 'Outgoing': 'Sosyal', 'Active': 'Aktif', 'Gentle': 'Nazik',
        'Intelligent': 'Zeki', 'Trusting': 'Güvenilir', 'Devoted': 'Sadık',
        'Reliable': 'Güvenilir', 'Trustworthy': 'Sadık', 'Kind': 'İyi Kalpli',
        'Playful': 'Oyuncu', 'Adaptable': 'Uyumlu', 'Smart': 'Akıllı',
        'Affectionate': 'Sevecen', 'Patient': 'Sabırlı', 'Alert': 'Uyanık',
        'Confident': 'Kendine Güvenen', 'Courageous': 'Cesur', 'Loyal': 'Sadık',
        'Versatile': 'Çok Yönlü', 'Protective': 'Koruyucu',
    },
    'ja': {
        'temperament': '性格',
        'exercise_needs': '運動量',
        'grooming_req': 'お手入れ',
        'which_right': 'どちらがあなたに合う？',
        'choose_breed': '{breed}を選ぶなら...',
        'bottom_line': 'まとめ',
        'Friendly': 'フレンドリー', 'Outgoing': '社交的', 'Active': '活発', 'Gentle': '穏やか',
        'Intelligent': '賢い', 'Trusting': '信頼', 'Devoted': '献身的',
        'Reliable': '頼もしい', 'Trustworthy': '誠実', 'Kind': '優しい',
        'Playful': '遊び好き', 'Adaptable': '適応力', 'Smart': '賢い',
        'Affectionate': '愛情深い', 'Patient': '忍耐強い', 'Alert': '警戒心',
        'Confident': '自信', 'Courageous': '勇敢', 'Loyal': '忠実',
        'Versatile': '多才', 'Protective': '保護的',
    },
    'zh': {
        'temperament': '性格',
        'exercise_needs': '运动需求',
        'grooming_req': '美容要求',
        'which_right': '哪种适合你？',
        'choose_breed': '如果...选择{breed}',
        'bottom_line': '总结',
        'Friendly': '友好', 'Outgoing': '外向', 'Active': '活跃', 'Gentle': '温柔',
        'Intelligent': '聪明', 'Trusting': '信任', 'Devoted': '忠诚',
        'Reliable': '可靠', 'Trustworthy': '值得信赖', 'Kind': '善良',
        'Playful': '爱玩', 'Adaptable': '适应力强', 'Smart': '机灵',
        'Affectionate': '深情', 'Patient': '耐心', 'Alert': '警觉',
        'Confident': '自信', 'Courageous': '勇敢', 'Loyal': '忠诚',
        'Versatile': '多才多艺', 'Protective': '保护性',
    },
}

def translate_trait(trait, lang):
    """Translate a single trait to target language."""
    return LANG_TRANSLATIONS.get(lang, {}).get(trait, trait)

def translate_traits(traits, lang):
    """Translate list of traits."""
    return [translate_trait(t, lang) for t in traits]

def get_ui_text(key, lang):
    """Get UI text for language."""
    return LANG_TRANSLATIONS.get(lang, {}).get(key, key)


# Import existing language configs from v1
from generate_comparison_articles import LANGUAGES

def generate_full_comparison(lang_code, lang_config, comp_key):
    """Generate a comparison article with ALL sections."""
    ui = lang_config['ui']
    comp = lang_config['comparisons'][comp_key]
    all_comps = lang_config['comparisons']
    
    # Get comparison data
    data_key = {
        'labrador-vs-golden': 'labrador-vs-golden',
        'frenchie-vs-boston': 'frenchie-vs-boston',
        'gsd-vs-malinois': 'gsd-vs-malinois',
        'husky-vs-malamute': 'husky-vs-malamute',
        'poodle-vs-labrador': 'poodle-vs-labrador',
    }.get(comp_key, comp_key)
    
    data = COMPARISON_DATA.get(data_key, COMPARISON_DATA['labrador-vs-golden'])
    
    # Translate traits
    breed1_traits = translate_traits(data['breed1_traits'], lang_code)
    breed2_traits = translate_traits(data['breed2_traits'], lang_code)
    
    # Build trait tags HTML
    def build_trait_tags(traits, color):
        return '\n                    '.join([
            f'<span class="bg-{color}-100 text-{color}-700 px-3 py-1 rounded-full text-sm font-medium">{t}</span>'
            for t in traits
        ])
    
    breed1_tags = build_trait_tags(breed1_traits, 'amber')
    breed2_tags = build_trait_tags(breed2_traits, 'yellow')
    
    # Build reasons lists
    def build_reasons(reasons):
        return '\n                        '.join([
            f'''<li class="flex items-start gap-2">
                            <span class="text-green-400">✓</span>
                            <span>{r}</span>
                        </li>'''
            for r in reasons
        ])
    
    breed1_reasons = build_reasons(data['breed1_reasons'])
    breed2_reasons = build_reasons(data['breed2_reasons'])
    
    # Get related comparisons
    related = [(k, v) for k, v in all_comps.items() if k != comp_key][:3]
    related_html = ""
    for key, rel in related:
        related_html += f'''
                <a href="{rel['slug']}.html" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md transition">
                    <span class="font-semibold">{rel['breed1']} vs {rel['breed2']}</span>
                </a>'''
    
    trans = LANG_TRANSLATIONS.get(lang_code, {})
    
    html = f'''<!DOCTYPE html>
<html lang="{lang_config['html_lang']}">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-VEERQZ53LZ"></script>
    <script>window.dataLayer = window.dataLayer || []; function gtag(){{dataLayer.push(arguments);}} gtag("js", new Date()); gtag("config", "G-VEERQZ53LZ");</script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{comp['title']} | BreedFinder</title>
    <meta name="description" content="{comp['desc']}">
    <link rel="canonical" href="https://breedfinder.org/{lang_code}/compare/comparisons/{comp['slug']}.html">
    <link rel="icon" href="../../../favicon.ico" type="image/x-icon">
    <meta property="og:title" content="{comp['title']}">
    <meta property="og:description" content="{comp['desc']}">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>* {{ font-family: 'Plus Jakarta Sans', sans-serif; }}</style>
</head>
<body class="bg-gradient-to-br from-sky-50 via-white to-blue-50 min-h-screen text-slate-800">
    <header class="bg-white/80 backdrop-blur-md border-b border-slate-100 sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
            <a href="../../" class="flex items-center gap-3">
                <img src="../../../logo-192.png" class="w-10 h-10" alt="BreedFinder">
                <span class="text-xl font-bold">BreedFinder</span>
            </a>
            <nav class="flex items-center gap-6 text-sm font-medium">
                <a href="../../breeds" class="text-slate-600 hover:text-sky-700">{ui['all_breeds']}</a>
                <a href="../" class="text-slate-600 hover:text-sky-700">{ui['compare']}</a>
                <a href="../../quiz" class="bg-sky-500 text-white px-5 py-2.5 rounded-xl font-semibold">{ui['take_quiz']}</a>
            </nav>
        </div>
    </header>

    <main class="max-w-6xl mx-auto px-4 py-12">
        <nav class="text-sm text-slate-600 mb-8">
            <a href="../">{ui['compare']}</a> › <a href="./">{ui['comparisons']}</a> › {comp['breed1']} vs {comp['breed2']}
        </nav>

        <div class="text-center mb-12">
            <h1 class="text-4xl md:text-5xl font-extrabold mb-4">
                <span class="text-amber-500">{comp['breed1']}</span>
                <span class="text-slate-600 mx-4">vs</span>
                <span class="text-yellow-500">{comp['breed2']}</span>
            </h1>
            <p class="text-lg text-slate-600 max-w-2xl mx-auto">{comp['intro']}</p>
        </div>

        <!-- Breed Cards -->
        <div class="grid md:grid-cols-2 gap-8 mb-12">
            <div class="bg-white rounded-3xl shadow-xl overflow-hidden">
                <div class="bg-gradient-to-r from-amber-500 to-amber-600 p-6 text-white text-center">
                    <img src="../../../images/heads/{comp['breed1_slug']}.webp" alt="{comp['breed1']}" class="w-32 h-32 rounded-full mx-auto mb-4 object-cover border-4 border-white/30">
                    <h2 class="text-2xl font-bold">{comp['breed1']}</h2>
                    <p class="text-amber-100">{comp['breed1_tagline']}</p>
                </div>
                <div class="p-6">
                    <p class="text-slate-600 mb-4">{comp['breed1_desc']}</p>
                    <a href="../../breeds/{comp['breed1_slug']}" class="text-sky-700 font-semibold">{ui['view_profile']}</a>
                </div>
            </div>
            <div class="bg-white rounded-3xl shadow-xl overflow-hidden">
                <div class="bg-gradient-to-r from-yellow-500 to-yellow-600 p-6 text-white text-center">
                    <img src="../../../images/heads/{comp['breed2_slug']}.webp" alt="{comp['breed2']}" class="w-32 h-32 rounded-full mx-auto mb-4 object-cover border-4 border-white/30">
                    <h2 class="text-2xl font-bold">{comp['breed2']}</h2>
                    <p class="text-yellow-100">{comp['breed2_tagline']}</p>
                </div>
                <div class="p-6">
                    <p class="text-slate-600 mb-4">{comp['breed2_desc']}</p>
                    <a href="../../breeds/{comp['breed2_slug']}" class="text-sky-700 font-semibold">{ui['view_profile']}</a>
                </div>
            </div>
        </div>

        <!-- Comparison Table -->
        <div class="bg-white rounded-3xl shadow-xl overflow-hidden mb-12">
            <div class="bg-slate-800 p-6 text-white">
                <h2 class="text-2xl font-bold text-center">{ui['side_by_side']}</h2>
            </div>
            <table class="w-full">
                <thead><tr class="bg-slate-50">
                    <th class="p-4 text-left">{ui['attribute']}</th>
                    <th class="p-4 text-center text-amber-600">{comp['breed1']}</th>
                    <th class="p-4 text-center text-yellow-600">{comp['breed2']}</th>
                </tr></thead>
                <tbody class="divide-y divide-slate-100">
                    <tr><td class="p-4">📏 {ui['size']}</td><td class="p-4 text-center font-semibold">{ui['large']}</td><td class="p-4 text-center font-semibold">{ui['large']}</td></tr>
                    <tr class="bg-slate-50/50"><td class="p-4">⏳ {ui['lifespan']}</td><td class="p-4 text-center">10-12 {ui['years']}</td><td class="p-4 text-center">10-12 {ui['years']}</td></tr>
                    <tr><td class="p-4">⚡ {ui['energy_level']}</td><td class="p-4 text-center"><span class="text-amber-500">●●●●●</span><br><span class="text-sm">{ui['very_high']}</span></td><td class="p-4 text-center"><span class="text-yellow-500">●●●●○</span><br><span class="text-sm">{ui['high']}</span></td></tr>
                    <tr class="bg-slate-50/50"><td class="p-4">✂️ {ui['grooming_needs']}</td><td class="p-4 text-center"><span class="text-amber-500">●●○○○</span><br><span class="text-sm">{ui['moderate']}</span></td><td class="p-4 text-center"><span class="text-yellow-500">●●●○○</span><br><span class="text-sm">{ui['moderate']}</span></td></tr>
                    <tr><td class="p-4">🎓 {ui['trainability']}</td><td class="p-4 text-center"><span class="text-amber-500">●●●●●</span><br><span class="text-sm">{ui['excellent']}</span></td><td class="p-4 text-center"><span class="text-yellow-500">●●●●●</span><br><span class="text-sm">{ui['excellent']}</span></td></tr>
                    <tr class="bg-slate-50/50"><td class="p-4">👶 {ui['kid_friendly']}</td><td class="p-4 text-center"><span class="text-amber-500">●●●●●</span><br><span class="text-sm">{ui['excellent']}</span></td><td class="p-4 text-center"><span class="text-yellow-500">●●●●●</span><br><span class="text-sm">{ui['excellent']}</span></td></tr>
                    <tr><td class="p-4">🏠 {ui['apartment']}</td><td class="p-4 text-center"><span class="text-amber-500">●●○○○</span><br><span class="text-sm">{ui['not_ideal']}</span></td><td class="p-4 text-center"><span class="text-yellow-500">●●○○○</span><br><span class="text-sm">{ui['not_ideal']}</span></td></tr>
                    <tr class="bg-slate-50/50"><td class="p-4">🐕 {ui['shedding']}</td><td class="p-4 text-center font-semibold text-amber-600">{ui['high']}</td><td class="p-4 text-center font-semibold text-yellow-600">{ui['heavy']}</td></tr>
                </tbody>
            </table>
        </div>

        <!-- Temperament Comparison -->
        <div class="grid md:grid-cols-2 gap-8 mb-12">
            <div class="bg-white rounded-2xl p-6 shadow-lg">
                <h3 class="text-xl font-bold text-amber-600 mb-4">🧠 {comp['breed1']} {trans.get('temperament', 'Temperament')}</h3>
                <div class="flex flex-wrap gap-2 mb-4">
                    {breed1_tags}
                </div>
                <p class="text-slate-600 text-sm">{data['breed1_temperament_desc']}</p>
            </div>
            <div class="bg-white rounded-2xl p-6 shadow-lg">
                <h3 class="text-xl font-bold text-yellow-600 mb-4">🧠 {comp['breed2']} {trans.get('temperament', 'Temperament')}</h3>
                <div class="flex flex-wrap gap-2 mb-4">
                    {breed2_tags}
                </div>
                <p class="text-slate-600 text-sm">{data['breed2_temperament_desc']}</p>
            </div>
        </div>

        <!-- Exercise & Grooming -->
        <div class="grid md:grid-cols-2 gap-8 mb-12">
            <div class="bg-gradient-to-br from-sky-50 to-sky-100 rounded-2xl p-6">
                <h3 class="text-xl font-bold text-sky-700 mb-4">🏃 {trans.get('exercise_needs', 'Exercise Needs')}</h3>
                <div class="space-y-4">
                    <div><span class="font-semibold text-amber-600">{comp['breed1']}:</span><p class="text-slate-600 text-sm">{data['breed1_exercise']}</p></div>
                    <div><span class="font-semibold text-yellow-600">{comp['breed2']}:</span><p class="text-slate-600 text-sm">{data['breed2_exercise']}</p></div>
                </div>
            </div>
            <div class="bg-gradient-to-br from-sky-50 to-sky-100 rounded-2xl p-6">
                <h3 class="text-xl font-bold text-sky-700 mb-4">✂️ {trans.get('grooming_req', 'Grooming Requirements')}</h3>
                <div class="space-y-4">
                    <div><span class="font-semibold text-amber-600">{comp['breed1']}:</span><p class="text-slate-600 text-sm">{data['breed1_grooming']}</p></div>
                    <div><span class="font-semibold text-yellow-600">{comp['breed2']}:</span><p class="text-slate-600 text-sm">{data['breed2_grooming']}</p></div>
                </div>
            </div>
        </div>

        <!-- Verdict Section -->
        <div class="bg-gradient-to-r from-slate-800 to-slate-700 rounded-3xl p-8 text-white mb-12">
            <h2 class="text-3xl font-bold text-center mb-8">🎯 {trans.get('which_right', 'Which Is Right For You?')}</h2>
            <div class="grid md:grid-cols-2 gap-8">
                <div class="bg-white/10 rounded-2xl p-6">
                    <h3 class="text-xl font-bold text-amber-400 mb-4">{trans.get('choose_breed', 'Choose {breed} If...').format(breed=comp['breed1'])}</h3>
                    <ul class="space-y-2 text-slate-200">
                        {breed1_reasons}
                    </ul>
                </div>
                <div class="bg-white/10 rounded-2xl p-6">
                    <h3 class="text-xl font-bold text-yellow-400 mb-4">{trans.get('choose_breed', 'Choose {breed} If...').format(breed=comp['breed2'])}</h3>
                    <ul class="space-y-2 text-slate-200">
                        {breed2_reasons}
                    </ul>
                </div>
            </div>
            <div class="mt-8 bg-white/5 rounded-xl p-6 text-center">
                <h4 class="text-lg font-semibold text-sky-300 mb-2">{trans.get('bottom_line', 'The Bottom Line')}</h4>
                <p class="text-slate-300">{data['bottom_line']}</p>
            </div>
        </div>

        <!-- Related Comparisons -->
        <div class="mb-12">
            <h2 class="text-2xl font-bold mb-6">{ui['more_comparisons']}</h2>
            <div class="grid md:grid-cols-3 gap-4">{related_html}</div>
        </div>

        <div class="text-center">
            <a href="../" class="text-sky-700 font-semibold">{ui['back_to_compare']}</a>
        </div>
    </main>

    <footer class="border-t border-slate-100 mt-16 py-8">
        <div class="max-w-6xl mx-auto px-4 text-center text-slate-600 text-sm">
            <p>© 2026 BreedFinder. {ui['helping_find']}</p>
        </div>
    </footer>
</body>
</html>'''
    
    return html


def main():
    """Regenerate all comparison articles with full content."""
    for lang_code, lang_config in LANGUAGES.items():
        print(f"Regenerating {lang_config['name']} ({lang_code})...")
        
        output_dir = BASE_DIR / lang_code / 'compare' / 'comparisons'
        
        # Regenerate comparison articles (not index)
        for comp_key in lang_config['comparisons']:
            comp = lang_config['comparisons'][comp_key]
            article_html = generate_full_comparison(lang_code, lang_config, comp_key)
            article_path = output_dir / f"{comp['slug']}.html"
            with open(article_path, 'w', encoding='utf-8') as f:
                f.write(article_html)
            print(f"  ✅ {article_path.name}")
    
    print(f"\n✅ Regenerated {len(LANGUAGES) * 5} comparison articles with full content")


if __name__ == '__main__':
    main()
