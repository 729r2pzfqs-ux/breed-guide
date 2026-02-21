#!/usr/bin/env python3
"""
Generate fully translated German breed pages from English JSON data
"""

import json
import os
import re
from pathlib import Path

# German translations for UI elements
UI = {
    'origin': 'Herkunft',
    'lifespan': 'Lebenserwartung',
    'height': 'Höhe',
    'weight': 'Gewicht',
    'breed_ratings': 'Rassenbewertungen',
    'energy_level': 'Energielevel',
    'grooming_needs': 'Pflegebedarf',
    'trainability': 'Trainierbarkeit',
    'kid_friendly': 'Kinderfreundlich',
    'apartment_friendly': 'Wohnungsgeeignet',
    'barking_level': 'Bellverhalten',
    'temperament': 'Temperament',
    'overview': 'Überblick',
    'health': 'Gesundheit',
    'exercise': 'Bewegung',
    'is_right_for_you': 'Ist Diese Rasse Richtig für Dich?',
    'best_for': 'Am Besten Für',
    'not_ideal': 'Nicht Ideal Für',
    'our_verdict': 'Unser Fazit',
    'browse_breeds': 'Rassen Durchsuchen',
    'home': 'Startseite',
    'take_quiz': 'Quiz Starten',
    'years': 'Jahre',
}

# Group translations
GROUPS = {
    'sporting': 'Jagdhund',
    'hound': 'Laufhund',
    'working': 'Arbeitshund',
    'terrier': 'Terrier',
    'toy': 'Gesellschaftshund',
    'non-sporting': 'Nicht-Jagdhund',
    'herding': 'Hütehund',
    'miscellaneous': 'Verschiedene',
    'foundation': 'Foundation',
}

# Size translations
SIZES = {
    'tiny': 'Winzig',
    'small': 'Klein',
    'medium': 'Mittel',
    'large': 'Groß',
    'giant': 'Riesig',
}

# Temperament trait translations
TRAITS = {
    'friendly': 'freundlich', 'loyal': 'treu', 'intelligent': 'intelligent', 'active': 'aktiv',
    'gentle': 'sanft', 'playful': 'verspielt', 'protective': 'beschützend', 'calm': 'ruhig',
    'affectionate': 'liebevoll', 'alert': 'wachsam', 'energetic': 'energisch', 'independent': 'unabhängig',
    'stubborn': 'stur', 'confident': 'selbstbewusst', 'curious': 'neugierig', 'outgoing': 'aufgeschlossen',
    'brave': 'mutig', 'patient': 'geduldig', 'devoted': 'ergeben', 'eager': 'eifrig',
    'trainable': 'trainierbar', 'adaptable': 'anpassungsfähig', 'reserved': 'zurückhaltend',
    'dignified': 'würdevoll', 'sensitive': 'sensibel', 'fearless': 'furchtlos', 'spirited': 'temperamentvoll',
    'loving': 'liebend', 'obedient': 'gehorsam', 'athletic': 'athletisch', 'agile': 'wendig',
    'smart': 'klug', 'charming': 'charmant', 'lively': 'lebhaft', 'bold': 'kühn',
    'watchful': 'wachsam', 'powerful': 'kraftvoll', 'mischievous': 'schelmisch', 'noble': 'edel',
    'steady': 'beständig', 'sweet': 'süß', 'happy': 'fröhlich', 'cheerful': 'fröhlich',
    'determined': 'entschlossen', 'territorial': 'territorial', 'hardworking': 'fleißig',
    'sociable': 'gesellig', 'docile': 'fügsam', 'easygoing': 'unkompliziert', 'versatile': 'vielseitig',
    'regal': 'königlich', 'graceful': 'anmutig', 'elegant': 'elegant', 'aloof': 'distanziert',
    'funny': 'lustig', 'courageous': 'mutig', 'keen': 'eifrig', 'good-natured': 'gutmütig',
    'even-tempered': 'ausgeglichen', 'reliable': 'zuverlässig', 'trusting': 'vertrauensvoll',
    'self-confident': 'selbstsicher', 'proud': 'stolz', 'fast': 'schnell', 'tough': 'robust',
    'feisty': 'lebhaft', 'spunky': 'mutig', 'peppy': 'lebhaft', 'perky': 'munter',
    'quiet': 'ruhig', 'responsive': 'aufmerksam', 'stable': 'stabil', 'eager to please': 'lernwillig',
    'people-oriented': 'menschenbezogen', 'family-oriented': 'familienorientiert',
    'cat-like': 'katzenartig', 'clownish': 'clownesk', 'comical': 'komisch',
    'happy-go-lucky': 'unbekümmert', 'good-humored': 'gutgelaunt', 'amiable': 'freundlich',
    'companionable': 'gesellig', 'fun-loving': 'verspielt', 'boisterous': 'übermütig',
    'assertive': 'durchsetzungsfähig', 'willful': 'eigensinnig', 'strong-willed': 'willensstark',
    'demanding': 'anspruchsvoll', 'dominant': 'dominant', 'intense': 'intensiv',
    'focused': 'fokussiert', 'driven': 'zielstrebig', 'tireless': 'unermüdlich',
    'rugged': 'robust', 'sturdy': 'kräftig', 'muscular': 'muskulös', 'imposing': 'imposant',
    'majestic': 'majestätisch', 'serene': 'gelassen', 'mellow': 'sanftmütig',
    'trustworthy': 'vertrauenswürdig', 'kind': 'gutmütig', 'gentle-mannered': 'sanftmütig',
    'well-mannered': 'wohlerzogen', 'easy-going': 'unkompliziert', 'happy-natured': 'fröhlich',
}

# Best For translations
BEST_FOR = {
    'Families with children': 'Familien mit Kindern',
    'Active individuals': 'Aktive Personen',
    'First-time dog owners': 'Erstbesitzer',
    'First-time owners': 'Erstbesitzer',
    'Homes with yards': 'Häuser mit Garten',
    'People who enjoy outdoor activities': 'Outdoor-Liebhaber',
    'Apartment dwellers': 'Wohnungsbewohner',
    'Seniors': 'Senioren',
    'Experienced owners': 'Erfahrene Besitzer',
    'Singles and couples': 'Singles und Paare',
    'Working from home': 'Heimarbeiter',
    'Allergy sufferers': 'Allergiker',
    'Those wanting a guard dog': 'Wachhundsucher',
    'Runners and hikers': 'Läufer und Wanderer',
    'Active families': 'Aktive Familien',
    'Those who work from home': 'Heimarbeiter',
    'Adults only': 'Nur Erwachsene',
    'Those wanting a character': 'Charakterhund-Liebhaber',
    'Experienced dog owners': 'Erfahrene Hundebesitzer',
    'Rural homes': 'Ländliche Häuser',
    'Hunters': 'Jäger',
    'Those with time for grooming': 'Zeit für Pflege',
    'Those with large yards': 'Großer Garten vorhanden',
    'Those seeking a loyal companion': 'Treue Begleiter gesucht',
    'Active outdoor enthusiasts': 'Aktive Outdoor-Liebhaber',
    'Farms and ranches': 'Bauernhöfe und Ranches',
    'Those who want a lap dog': 'Schoßhund-Liebhaber',
    'Quiet households': 'Ruhige Haushalte',
    'Multi-pet households': 'Mehrtierhaushalte',
    'Calm households': 'Ruhige Haushalte',
    'Moderately active people': 'Mäßig aktive Menschen',
    'Couch potatoes': 'Couchpotatoes',
    'Dog sport enthusiasts': 'Hundesport-Enthusiasten',
    'Patient trainers': 'Geduldige Trainer',
    'Cold climate residents': 'Bewohner kalter Klimazonen',
    'Warm climate residents': 'Bewohner warmer Klimazonen',
    'Active households': 'Aktive Haushalte',
    'Those wanting a therapy/service dog': 'Therapie-/Assistenzhund gesucht',
    'Those seeking a loyal companion': 'Treuer Begleiter gesucht',
    'Those with patience for training': 'Geduld für Training',
    'Those looking for a watchdog': 'Wachhund gesucht',
    'Country living': 'Landleben',
    'City dwellers': 'Stadtbewohner',
    'Those who enjoy grooming': 'Freude an Fellpflege',
    'Dog sport enthusiasts': 'Hundesport-Enthusiasten',
    'Jogging partners': 'Jogging-Partner',
    'Therapy dog candidates': 'Therapiehund-Kandidaten',
    'Service dog candidates': 'Assistenzhund-Kandidaten',
    'Search and rescue': 'Such- und Rettungsarbeit',
    'Agility enthusiasts': 'Agility-Liebhaber',
    'Hiking companions': 'Wanderbegleiter',
    'Swimming enthusiasts': 'Schwimmbegeisterte',
    'Families': 'Familien',
    'Active people': 'Aktive Menschen',
}

# Not Ideal translations
NOT_IDEAL = {
    'Sedentary lifestyles': 'Sitzender Lebensstil',
    'Those away from home often': 'Häufig abwesend',
    'Allergy sufferers': 'Allergiker',
    'Small apartment dwellers': 'Kleine Wohnungen',
    'Small apartments': 'Kleine Wohnungen',
    'First-time owners': 'Erstbesitzer',
    'First-time dog owners': 'Erstbesitzer',
    'Families with very young children': 'Familien mit Kleinkindern',
    'Families with young children': 'Familien mit kleinen Kindern',
    'Hot climates': 'Heißes Klima',
    'Cold climates': 'Kaltes Klima',
    'Novice trainers': 'Anfänger-Trainer',
    'Homes with small pets': 'Haushalte mit Kleintieren',
    'Those who dislike grooming': 'Pflegemuffel',
    'Quiet neighborhoods required': 'Ruhige Nachbarschaft nötig',
    'Apartment living': 'Wohnungsleben',
    'Inactive owners': 'Inaktive Besitzer',
    'Busy schedules': 'Volle Terminkalender',
    'Extreme climates': 'Extreme Klimazonen',
    'Those wanting an easy-to-train dog': 'Einfach zu trainieren erwünscht',
    'Cat owners': 'Katzenbesitzer',
    'Homes with cats': 'Haushalte mit Katzen',
    'Very active households': 'Sehr aktive Haushalte',
    'Noise-sensitive neighbors': 'Lärmempfindliche Nachbarn',
    'Inexperienced owners': 'Unerfahrene Besitzer',
    'Very small living spaces': 'Sehr kleine Wohnräume',
    'Those seeking a guard dog': 'Wachhund gesucht',
    'Rural areas without fencing': 'Ländliche Gebiete ohne Zaun',
    'Households with small children': 'Haushalte mit kleinen Kindern',
    'Those wanting a guard dog': 'Wachhund gesucht',
    'Those who dislike dog hair': 'Hundehaare unerwünscht',
    'Those wanting low maintenance': 'Pflegeleicht gewünscht',
    'Very active lifestyles': 'Sehr aktiver Lebensstil',
    'Those seeking independence': 'Unabhängigkeit gesucht',
    'Timid owners': 'Zurückhaltende Besitzer',
    'Those who travel often': 'Vielreisende',
    'Those with limited time': 'Wenig Zeit vorhanden',
    'Those who want a quiet dog': 'Ruhiger Hund gewünscht',
    'Homes without fenced yards': 'Häuser ohne eingezäunten Garten',
    'Small children': 'Kleine Kinder',
    'Very small spaces': 'Sehr kleine Räume',
    'Those who want an easy dog': 'Einfacher Hund gewünscht',
    'Those with no dog experience': 'Keine Hundeerfahrung',
    'Weak or frail owners': 'Körperlich eingeschränkte Besitzer',
    'Those who cannot provide leadership': 'Keine konsequente Führung möglich',
}

def translate_trait(trait):
    """Translate a temperament trait to German"""
    t = trait.lower().strip()
    return TRAITS.get(t, trait.capitalize())

def translate_best_for(item):
    """Translate a Best For item"""
    return BEST_FOR.get(item, item)

def translate_not_ideal(item):
    """Translate a Not Ideal item"""
    return NOT_IDEAL.get(item, item)

def translate_group(group):
    """Translate breed group"""
    return GROUPS.get(group.lower(), group.capitalize())

def translate_size(size):
    """Translate size category"""
    return SIZES.get(size.lower(), size.capitalize())

def generate_german_overview(breed):
    """Generate German overview text"""
    name = breed['name']
    group = translate_group(breed.get('group', 'miscellaneous'))
    size = translate_size(breed['size']['category'])
    
    traits = breed.get('temperament', [])[:3]
    traits_de = [translate_trait(t) for t in traits]
    traits_str = ', '.join(traits_de) if traits_de else 'vielseitig'
    
    origin = breed.get('origin', 'unbekannt')
    
    templates = [
        f"Der {name} ist ein {traits_str}er {group}, der ursprünglich aus {origin} stammt. Diese {size.lower()}e Rasse ist bekannt für ihre einzigartige Persönlichkeit und macht einen wunderbaren Begleiter für die richtige Familie.",
        f"Als {traits_str}er {group} aus {origin} hat der {name} viele Bewunderer weltweit gewonnen. Diese {size.lower()}e Rasse verbindet Charakter mit Loyalität.",
        f"Der {name} ist ein {size.lower()}er {group} mit {traits_str}em Wesen. Ursprünglich aus {origin}, ist diese Rasse bei Hundeliebhabern sehr beliebt.",
    ]
    
    import hashlib
    idx = int(hashlib.md5(name.encode()).hexdigest(), 16) % len(templates)
    return templates[idx]

def generate_german_temperament(breed):
    """Generate German temperament description"""
    name = breed['name']
    traits = breed.get('temperament', [])
    traits_de = [translate_trait(t) for t in traits[:4]]
    
    if len(traits_de) >= 2:
        return f"Der {name} ist {traits_de[0]} und {traits_de[1]}. Diese Rasse ist bekannt für ihre ausgeglichene Art und bildet starke Bindungen zu ihrer Familie. Mit der richtigen Sozialisierung und Training werden sie zu loyalen und liebevollen Begleitern."
    return f"Der {name} hat ein ausgeglichenes Temperament und ist bei richtiger Erziehung ein treuer Familienbegleiter."

def generate_german_health(breed):
    """Generate German health description"""
    name = breed['name']
    lifespan = breed.get('lifespan', '10-12 years').replace(' years', ' Jahre').replace(' year', ' Jahr')
    size_cat = breed['size']['category']
    
    health_issues = {
        'tiny': 'Patellaluxation, Zahnprobleme und Herzerkrankungen',
        'small': 'Patellaluxation, Zahnprobleme und Augenerkrankungen',
        'medium': 'Hüftdysplasie, Allergien und Augenprobleme',
        'large': 'Hüft- und Ellbogendysplasie, Blähungen und Herzerkrankungen',
        'giant': 'Hüftdysplasie, Blähungen (Magendrehung) und Herzprobleme',
    }
    
    issues = health_issues.get(size_cat, 'rassetypische Gesundheitsprobleme')
    return f"Der {name} hat eine Lebenserwartung von {lifespan}. Wie bei vielen Rassen dieser Größe können {issues} auftreten. Regelmäßige Tierarztbesuche und eine ausgewogene Ernährung sind wichtig für ein gesundes, langes Leben."

def generate_german_exercise(breed):
    """Generate German exercise description"""
    name = breed['name']
    energy = breed.get('ratings', {}).get('energy', 3)
    
    if energy >= 4:
        return f"Der {name} ist eine energiereiche Rasse, die mindestens 60-90 Minuten tägliche Bewegung benötigt. Lange Spaziergänge, Laufen und aktives Spielen sind ideal. Ohne ausreichende körperliche und geistige Auslastung können Verhaltensprobleme auftreten."
    elif energy >= 3:
        return f"Der {name} benötigt moderate Bewegung mit täglichen Spaziergängen von 30-60 Minuten. Spielzeit im Garten und interaktive Spiele halten diese Rasse glücklich und gesund. Regelmäßige Aktivität ist wichtig für das körperliche und geistige Wohlbefinden."
    else:
        return f"Der {name} hat einen geringen bis moderaten Bewegungsbedarf. Kurze tägliche Spaziergänge und Spielzeit reichen aus. Diese Rasse passt gut zu Menschen mit einem ruhigeren Lebensstil, braucht aber dennoch regelmäßige leichte Aktivität."

def generate_german_verdict(breed):
    """Generate German verdict summary"""
    name = breed['name']
    traits = breed.get('temperament', [])[:2]
    traits_de = [translate_trait(t) for t in traits]
    traits_str = ' und '.join(traits_de) if traits_de else 'vielseitig'
    
    best = breed.get('verdict', {}).get('best_for', [])
    
    if 'Families with children' in best or 'Active families' in best:
        return f"Der {name} ist ein ausgezeichneter Familienhund. Mit seinem {traits_str}en Wesen passt er perfekt zu aktiven Familien, die Zeit für Training und Beschäftigung haben."
    elif 'Apartment dwellers' in best:
        return f"Der {name} eignet sich hervorragend für das Wohnungsleben. Sein {traits_str}es Temperament macht ihn zu einem idealen Begleiter für Stadtbewohner."
    elif 'Experienced owners' in best:
        return f"Der {name} ist am besten für erfahrene Hundebesitzer geeignet. Diese {traits_str}e Rasse erfordert konsequentes Training und eine sichere Führung."
    else:
        return f"Der {name} ist ein {traits_str}er Begleiter für die richtige Familie. Mit angemessener Pflege und Training wird diese Rasse zu einem treuen Freund fürs Leben."

def generate_breed_html(breed):
    """Generate complete German HTML for a breed"""
    name = breed['name']
    slug = breed['id']
    group = breed.get('group', 'miscellaneous')
    origin = breed.get('origin', 'Unknown')
    lifespan = breed.get('lifespan', '10-12 years').replace(' years', ' Jahre').replace(' year', ' Jahr')
    
    height_cm = breed['size'].get('height_cm', '25-30')
    weight_kg = breed['size'].get('weight_kg', '5-10')
    size_cat = breed['size']['category']
    
    # Calculate imperial
    def cm_to_in(cm_str):
        parts = cm_str.split('-')
        if len(parts) == 2:
            low = round(float(parts[0]) / 2.54)
            high = round(float(parts[1]) / 2.54)
            return f"{low}-{high}"
        return str(round(float(parts[0]) / 2.54))
    
    def kg_to_lbs(kg_str):
        parts = kg_str.split('-')
        if len(parts) == 2:
            low = round(float(parts[0]) * 2.205)
            high = round(float(parts[1]) * 2.205)
            return f"{low}-{high}"
        return str(round(float(parts[0]) * 2.205))
    
    height_in = cm_to_in(height_cm)
    weight_lbs = kg_to_lbs(weight_kg)
    
    ratings = breed.get('ratings', {})
    energy = ratings.get('energy', 3)
    grooming = ratings.get('grooming', 3)
    trainability = ratings.get('trainability', 3)
    kid_friendly = ratings.get('kid_friendly', 3)
    apartment = ratings.get('apartment_ok', 3)
    barking = ratings.get('barking', 3)
    
    temperament = breed.get('temperament', [])
    temp_html = ''.join([f'<span class="bg-gradient-to-r from-sky-100 to-violet-100 text-slate-700 px-4 py-2 rounded-full text-sm font-medium">{translate_trait(t)}</span>' for t in temperament[:6]])
    
    verdict = breed.get('verdict', {})
    best_for = verdict.get('best_for', ['Familien', 'Aktive Menschen'])
    not_for = verdict.get('not_for', ['Sehr kleine Wohnungen'])
    
    best_html = '\n'.join([f'<li class="flex items-start gap-3"><span class="w-2 h-2 mt-2 bg-emerald-500 rounded-full"></span><span>{translate_best_for(b)}</span></li>' for b in best_for])
    not_html = '\n'.join([f'<li class="flex items-start gap-3"><span class="w-2 h-2 mt-2 bg-rose-500 rounded-full"></span><span>{translate_not_ideal(n)}</span></li>' for n in not_for])
    
    overview = generate_german_overview(breed)
    temperament_text = generate_german_temperament(breed)
    health_text = generate_german_health(breed)
    exercise_text = generate_german_exercise(breed)
    verdict_text = generate_german_verdict(breed)
    
    html = f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} | BreedFinder</title>
    <meta name="description" content="{overview[:150]}">
    <link rel="canonical" href="https://breedfinder.org/de/breeds/{slug}.html">
    <link rel="icon" href="../../favicon.ico">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
        .card-shadow {{ box-shadow: 0 4px 20px rgba(0,0,0,0.05); }}
        .rating-bar {{ background: #e2e8f0; position: relative; overflow: hidden; }}
        .rating-bar::after {{ content: ''; position: absolute; left: 0; top: 0; height: 100%; width: var(--rating); background: linear-gradient(90deg, #0ea5e9, #8b5cf6); border-radius: 9999px; }}
    </style>
</head>
<body class="bg-slate-50 min-h-screen">
    <header class="bg-white border-b border-slate-200 sticky top-0 z-50">
        <div class="max-w-5xl mx-auto px-4 py-4 flex items-center justify-between">
            <a href="../" class="flex items-center gap-2">
                <img src="../../logo-192.png" class="w-10 h-10" alt="BreedFinder">
                <span class="font-bold text-xl text-slate-800">BreedFinder</span>
            </a>
            <nav class="flex items-center gap-4 text-sm">
                <a href="../search/" class="text-slate-600 hover:text-sky-600 flex items-center">
                    <i data-lucide="search" class="w-5 h-5 md:hidden"></i>
                    <span class="hidden md:inline">Rassen Durchsuchen</span>
                </a>
                <a href="../quiz/" class="bg-gradient-to-r from-sky-500 to-violet-500 text-white px-4 py-2 rounded-xl">Quiz Starten</a>
            </nav>
        </div>
    </header>

    <main class="max-w-5xl mx-auto px-4 py-8">
        <nav class="text-sm text-slate-500 mb-6 flex items-center gap-2">
            <a href="../" class="hover:text-sky-600">Startseite</a>
            <i data-lucide="chevron-right" class="w-4 h-4"></i>
            <a href="../search/" class="hover:text-sky-600">Rassen Durchsuchen</a>
            <i data-lucide="chevron-right" class="w-4 h-4"></i>
            <span class="text-slate-700 font-medium">{name}</span>
        </nav>

        <!-- Hero Card -->
        <div class="bg-white rounded-3xl p-8 mb-8 card-shadow border border-slate-100">
            <div class="flex flex-col md:flex-row gap-8">
                <div class="md:w-2/5">
                    <img src="../../images/breeds/{slug}.webp" alt="{name}" class="rounded-2xl w-full aspect-[4/5] object-cover border border-slate-200/50" onerror="this.src='../../images/heads/{slug}.webp'">
                </div>
                <div class="md:w-3/5">
                    <div class="flex items-center gap-2 mb-3">
                        <span class="bg-sky-100 text-sky-700 text-xs font-semibold px-3 py-1 rounded-full">{translate_group(group)}</span>
                        <span class="bg-violet-100 text-violet-700 text-xs font-semibold px-3 py-1 rounded-full">{translate_size(size_cat)}</span>
                    </div>
                    <h1 class="text-4xl font-bold text-slate-900 mb-3">{name}</h1>
                    <p class="text-lg text-slate-600 mb-6">{overview[:200]}</p>
                    <div class="grid grid-cols-2 gap-4">
                        <div class="bg-slate-50 rounded-xl p-4">
                            <div class="text-xs font-medium text-slate-500 uppercase mb-1 flex items-center gap-1">
                                <i data-lucide="map-pin" class="w-3 h-3"></i> Herkunft
                            </div>
                            <div class="text-slate-800 font-semibold">{origin}</div>
                        </div>
                        <div class="bg-slate-50 rounded-xl p-4">
                            <div class="text-xs font-medium text-slate-500 uppercase mb-1 flex items-center gap-1">
                                <i data-lucide="heart" class="w-3 h-3"></i> Lebenserwartung
                            </div>
                            <div class="text-slate-800 font-semibold">{lifespan}</div>
                        </div>
                        <div class="bg-slate-50 rounded-xl p-4">
                            <div class="text-xs font-medium text-slate-500 uppercase mb-1 flex items-center gap-1">
                                <i data-lucide="ruler" class="w-3 h-3"></i> Höhe
                            </div>
                            <div class="text-slate-800 font-semibold">{height_cm} cm ({height_in} in)</div>
                        </div>
                        <div class="bg-slate-50 rounded-xl p-4">
                            <div class="text-xs font-medium text-slate-500 uppercase mb-1 flex items-center gap-1">
                                <i data-lucide="scale" class="w-3 h-3"></i> Gewicht
                            </div>
                            <div class="text-slate-800 font-semibold">{weight_kg} kg ({weight_lbs} lbs)</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Ratings -->
        <div class="bg-white rounded-2xl p-6 mb-8 shadow-sm border border-slate-100">
            <h2 class="text-xl font-bold mb-4">Rassenbewertungen</h2>
            <div class="grid md:grid-cols-2 gap-4">
                <div>
                    <div class="flex justify-between text-sm mb-1"><span>Energielevel</span><span>{energy}/5</span></div>
                    <div class="rating-bar h-2 rounded-full" style="--rating: {energy * 20}%"></div>
                </div>
                <div>
                    <div class="flex justify-between text-sm mb-1"><span>Pflegebedarf</span><span>{grooming}/5</span></div>
                    <div class="rating-bar h-2 rounded-full" style="--rating: {grooming * 20}%"></div>
                </div>
                <div>
                    <div class="flex justify-between text-sm mb-1"><span>Trainierbarkeit</span><span>{trainability}/5</span></div>
                    <div class="rating-bar h-2 rounded-full" style="--rating: {trainability * 20}%"></div>
                </div>
                <div>
                    <div class="flex justify-between text-sm mb-1"><span>Kinderfreundlich</span><span>{kid_friendly}/5</span></div>
                    <div class="rating-bar h-2 rounded-full" style="--rating: {kid_friendly * 20}%"></div>
                </div>
                <div>
                    <div class="flex justify-between text-sm mb-1"><span>Wohnungsgeeignet</span><span>{apartment}/5</span></div>
                    <div class="rating-bar h-2 rounded-full" style="--rating: {apartment * 20}%"></div>
                </div>
                <div>
                    <div class="flex justify-between text-sm mb-1"><span>Bellverhalten</span><span>{barking}/5</span></div>
                    <div class="rating-bar h-2 rounded-full" style="--rating: {barking * 20}%"></div>
                </div>
            </div>
        </div>

        <!-- Temperament -->
        <div class="bg-white rounded-3xl p-8 mb-8 card-shadow border border-slate-100">
            <h2 class="text-2xl font-bold text-slate-900 mb-6">Temperament</h2>
            <div class="flex flex-wrap gap-2">{temp_html}</div>
        </div>

        <!-- Content Sections -->
        <div class="space-y-4 mb-8">
            <details class="bg-white rounded-2xl shadow-sm border border-slate-100 group" open>
                <summary class="p-6 cursor-pointer flex items-center justify-between">
                    <h2 class="text-xl font-bold flex items-center gap-3">
                        <i data-lucide="book-open" class="w-5 h-5 text-sky-500"></i> Überblick
                    </h2>
                    <i data-lucide="chevron-down" class="w-5 h-5 text-slate-400 group-open:rotate-180 transition-transform"></i>
                </summary>
                <div class="px-6 pb-6"><p class="text-slate-600">{overview}</p></div>
            </details>
            <details class="bg-white rounded-2xl shadow-sm border border-slate-100 group">
                <summary class="p-6 cursor-pointer flex items-center justify-between">
                    <h2 class="text-xl font-bold flex items-center gap-3">
                        <i data-lucide="heart" class="w-5 h-5 text-sky-500"></i> Temperament
                    </h2>
                    <i data-lucide="chevron-down" class="w-5 h-5 text-slate-400 group-open:rotate-180 transition-transform"></i>
                </summary>
                <div class="px-6 pb-6"><p class="text-slate-600">{temperament_text}</p></div>
            </details>
            <details class="bg-white rounded-2xl shadow-sm border border-slate-100 group">
                <summary class="p-6 cursor-pointer flex items-center justify-between">
                    <h2 class="text-xl font-bold flex items-center gap-3">
                        <i data-lucide="heart-pulse" class="w-5 h-5 text-sky-500"></i> Gesundheit
                    </h2>
                    <i data-lucide="chevron-down" class="w-5 h-5 text-slate-400 group-open:rotate-180 transition-transform"></i>
                </summary>
                <div class="px-6 pb-6"><p class="text-slate-600">{health_text}</p></div>
            </details>
            <details class="bg-white rounded-2xl shadow-sm border border-slate-100 group">
                <summary class="p-6 cursor-pointer flex items-center justify-between">
                    <h2 class="text-xl font-bold flex items-center gap-3">
                        <i data-lucide="activity" class="w-5 h-5 text-sky-500"></i> Bewegung
                    </h2>
                    <i data-lucide="chevron-down" class="w-5 h-5 text-slate-400 group-open:rotate-180 transition-transform"></i>
                </summary>
                <div class="px-6 pb-6"><p class="text-slate-600">{exercise_text}</p></div>
            </details>
        </div>

        <!-- Verdict -->
        <div class="bg-gradient-to-br from-sky-50 via-violet-50 to-rose-50 rounded-2xl p-6 mb-8 border border-sky-100">
            <h2 class="text-xl font-bold mb-6 flex items-center gap-3">
                <span class="w-10 h-10 bg-gradient-to-br from-sky-500 to-violet-500 rounded-xl flex items-center justify-center text-white">⦿</span>
                Ist Diese Rasse Richtig für Dich?
            </h2>
            <div class="grid md:grid-cols-2 gap-6 mb-6">
                <div class="bg-white/80 rounded-xl p-5 border border-emerald-100">
                    <h3 class="font-bold text-emerald-700 mb-3 flex items-center gap-2">
                        <span class="text-emerald-500">✓</span> Am Besten Für
                    </h3>
                    <ul class="space-y-2 text-slate-700 text-sm">{best_html}</ul>
                </div>
                <div class="bg-white/80 rounded-xl p-5 border border-rose-100">
                    <h3 class="font-bold text-rose-700 mb-3 flex items-center gap-2">
                        <span class="text-rose-500">✗</span> Nicht Ideal Für
                    </h3>
                    <ul class="space-y-2 text-slate-700 text-sm">{not_html}</ul>
                </div>
            </div>
            <div class="bg-white/80 rounded-xl p-5 border border-slate-200">
                <p class="text-slate-700"><strong>Unser Fazit:</strong> {verdict_text}</p>
            </div>
        </div>

        <div class="text-center">
            <a href="../search/" class="inline-flex items-center gap-2 text-sky-600 font-semibold hover:text-sky-700">
                <i data-lucide="arrow-left" class="w-4 h-4"></i>
                Rassen Durchsuchen
            </a>
        </div>
    </main>

    <script>lucide.createIcons();</script>
</body>
</html>'''
    
    return html

def main():
    base_dir = Path(__file__).parent.parent
    breeds_file = base_dir / "data" / "breeds.json"
    output_dir = base_dir / "de" / "breeds"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    with open(breeds_file, 'r', encoding='utf-8') as f:
        breeds = json.load(f)
    
    print(f"Generating {len(breeds)} German breed pages...")
    
    for breed in breeds:
        html = generate_breed_html(breed)
        output_file = output_dir / f"{breed['id']}.html"
        output_file.write_text(html, encoding='utf-8')
        print(f"  ✓ {breed['name']}")
    
    print(f"\n✅ Done! Generated {len(breeds)} German breed pages")

if __name__ == "__main__":
    main()
