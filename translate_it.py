#!/usr/bin/env python3
"""
Italian translation script for breed pages.
Translates all English content to Italian.
"""

import os
import re
import sys
import json

# Translation dictionaries
TEMPERAMENT_TRANSLATIONS = {
    # Common traits
    "confident": "sicuro di sé",
    "fearless": "coraggioso",
    "funny": "divertente",
    "stubborn": "testardo",
    "curious": "curioso",
    "loyal": "leale",
    "affectionate": "affettuoso",
    "friendly": "amichevole",
    "gentle": "gentile",
    "alert": "vigile",
    "intelligent": "intelligente",
    "active": "attivo",
    "playful": "giocherellone",
    "independent": "indipendente",
    "protective": "protettivo",
    "brave": "coraggioso",
    "calm": "calmo",
    "patient": "paziente",
    "dignified": "dignitoso",
    "reserved": "riservato",
    "energetic": "energico",
    "loving": "amorevole",
    "devoted": "devoto",
    "spirited": "vivace",
    "bold": "audace",
    "athletic": "atletico",
    "agile": "agile",
    "eager": "desideroso",
    "obedient": "obbediente",
    "trainable": "addestrabile",
    "responsive": "reattivo",
    "sensitive": "sensibile",
    "sweet": "dolce",
    "sociable": "socievole",
    "outgoing": "estroverso",
    "lively": "vivace",
    "cheerful": "allegro",
    "happy": "felice",
    "merry": "gioioso",
    "clownish": "buffo",
    "mischievous": "birichino",
    "clever": "furbo",
    "keen": "acuto",
    "watchful": "attento",
    "territorial": "territoriale",
    "dominant": "dominante",
    "powerful": "potente",
    "strong": "forte",
    "muscular": "muscoloso",
    "rugged": "robusto",
    "hardy": "resistente",
    "versatile": "versatile",
    "adaptable": "adattabile",
    "graceful": "elegante",
    "noble": "nobile",
    "regal": "regale",
    "proud": "orgoglioso",
    "majestic": "maestoso",
    "elegant": "elegante",
    "refined": "raffinato",
    "charming": "affascinante",
    "amusing": "divertente",
    "entertaining": "intrattenitore",
    "comical": "comico",
    "quirky": "bizzarro",
    "spunky": "vivace",
    "feisty": "combattivo",
    "tenacious": "tenace",
    "determined": "determinato",
    "persistent": "persistente",
    "focused": "concentrato",
    "driven": "motivato",
    "hardworking": "laborioso",
    "tireless": "instancabile",
    "steady": "stabile",
    "reliable": "affidabile",
    "dependable": "fidato",
    "trustworthy": "degno di fiducia",
    "even-tempered": "equilibrato",
    "good-natured": "bonario",
    "easygoing": "accomodante",
    "relaxed": "rilassato",
    "laid-back": "tranquillo",
    "docile": "docile",
    "mild": "mite",
    "soft": "morbido",
    "submissive": "sottomesso",
    "timid": "timido",
    "shy": "timido",
    "aloof": "distaccato",
    "wary": "diffidente",
    "suspicious": "sospettoso",
    "cautious": "cauto",
    "serious": "serio",
    "thoughtful": "riflessivo",
    "composed": "composto",
    "self-assured": "sicuro di sé",
    "courageous": "coraggioso",
    "daring": "audace",
    "adventurous": "avventuroso",
    "fun-loving": "amante del divertimento",
    "joyful": "gioioso",
    "exuberant": "esuberante",
    "enthusiastic": "entusiasta",
    "eager to please": "desideroso di compiacere",
    "quick": "veloce",
    "fast": "rapido",
    "swift": "celere",
    "light-footed": "leggero",
    "nimble": "agile",
    "responsive": "reattivo",
    "attentive": "attento",
    "observant": "osservatore",
    "perceptive": "perspicace",
    "smart": "intelligente",
    "bright": "brillante",
    "sharp": "acuto",
    "clever": "intelligente",
    "cunning": "astuto",
    "sly": "furbo",
    "willful": "volitivo",
    "headstrong": "testardo",
    "obstinate": "ostinato",
    "strong-willed": "volitivo",
    "hard-headed": "testardo",
    "tough": "duro",
    "rugged": "robusto",
    "hearty": "vigoroso",
    "robust": "robusto",
    "powerful": "potente",
    "imposing": "imponente",
    "commanding": "imponente",
    "assertive": "assertivo",
    "confident": "sicuro",
    "self-confident": "sicuro di sé",
    "outgoing": "estroverso",
    "extroverted": "estroverso",
    "social": "sociale",
    "people-oriented": "orientato alle persone",
    "family-oriented": "orientato alla famiglia",
    "child-friendly": "adatto ai bambini",
    "kid-friendly": "adatto ai bambini",
    "cat-friendly": "adatto ai gatti",
    "dog-friendly": "adatto ai cani",
    "working": "lavoratore",
    "tireless": "instancabile",
    "enduring": "resistente",
    "stamina": "resistenza",
    "energy": "energia",
    "powerful": "potente",
    "strong": "forte",
    "mighty": "potente",
    "watchdog": "cane da guardia",
    "guardian": "guardiano",
    "protector": "protettore",
    "defender": "difensore",
    "keen-eyed": "dagli occhi acuti",
    "alert": "vigile",
    "vigilant": "vigilante",
    "guarding": "da guardia",
    "herding": "da pastore",
    "hunting": "da caccia",
    "tracking": "da seguita",
    "pointing": "da ferma",
    "retrieving": "da riporto",
    "swimming": "nuotatore",
    "water-loving": "amante dell'acqua",
    "catlike": "felino",
    "graceful": "aggraziato",
    "poised": "posato",
    "sleek": "snello",
    "streamlined": "aerodinamico",
    "aerodynamic": "aerodinamico",
    "swift": "veloce",
    "speedy": "veloce",
    "fleet": "veloce",
    "quick": "rapido",
    "agile": "agile",
    "nimble": "agile",
    "lithe": "flessuoso",
    "supple": "flessibile",
    "flexible": "flessibile",
    "acrobatic": "acrobatico",
    "athletic": "atletico",
    "sporty": "sportivo",
    "fit": "in forma",
    "healthy": "sano",
    "robust": "robusto",
    "vigorous": "vigoroso",
    "vital": "vitale",
    "alive": "vivace",
    "spirited": "animato",
    "animated": "animato",
    "lively": "vivace",
    "peppy": "vivace",
    "perky": "allegro",
    "bubbly": "effervescente",
    "bouncy": "vivace",
    "spring": "primaverile",
}

# Group name translations
GROUP_TRANSLATIONS = {
    "Toy": "Toy",
    "Terrier": "Terrier",
    "Hound": "Segugio",
    "Sporting": "Sportivo",
    "Non-Sporting": "Non Sportivo",
    "Working": "Lavoratore",
    "Herding": "Pastore",
    "Miscellaneous": "Varie",
    "Foundation Stock Service": "Servizio Stock Fondazione",
}

# Size translations
SIZE_TRANSLATIONS = {
    "Tiny": "Mini",
    "Small": "Piccola",
    "Medium": "Media",
    "Large": "Grande",
    "Giant": "Gigante",
}

def translate_temperament_trait(trait):
    """Translate a single temperament trait."""
    trait_lower = trait.lower().strip()
    if trait_lower in TEMPERAMENT_TRANSLATIONS:
        return TEMPERAMENT_TRANSLATIONS[trait_lower]
    return trait  # Return original if not found

def translate_group(group):
    """Translate breed group."""
    return GROUP_TRANSLATIONS.get(group, group)

def translate_size(size):
    """Translate size."""
    return SIZE_TRANSLATIONS.get(size, size)

def translate_file(filepath):
    """Translate a single breed file to Italian."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get breed name from filename
    filename = os.path.basename(filepath)
    breed_slug = filename.replace('.html', '')
    
    # 1. HTML lang attribute
    content = content.replace('<html lang="en">', '<html lang="it">')
    
    # 2. Fix canonical URL
    content = re.sub(
        r'<link rel="canonical" href="https://breedfinder\.org/breeds/([^"]+)">',
        r'<link rel="canonical" href="https://breedfinder.org/it/breeds/\1">',
        content
    )
    
    # 3. Fix OG/Twitter URLs
    content = re.sub(
        r'<meta property="og:url" content="https://breedfinder\.org/breeds/([^"]+)">',
        r'<meta property="og:url" content="https://breedfinder.org/it/breeds/\1">',
        content
    )
    
    # 4. Translate OG meta tags
    content = re.sub(
        r'<meta property="og:title" content="([^"]+) - Complete Breed Guide \| BreedFinder">',
        r'<meta property="og:title" content="\1 - Guida Completa alla Razza | BreedFinder">',
        content
    )
    content = re.sub(
        r'<meta property="og:description" content="Everything you need to know about the ([^"]+): temperament, care, exercise needs, and more\.">',
        r'<meta property="og:description" content="Tutto quello che devi sapere sul \1: temperamento, cura, esigenze di esercizio e altro.">',
        content
    )
    
    # 5. Translate Twitter meta tags
    content = re.sub(
        r'<meta name="twitter:title" content="([^"]+) - Breed Guide">',
        r'<meta name="twitter:title" content="\1 - Guida alla Razza">',
        content
    )
    content = re.sub(
        r'<meta name="twitter:description" content="Complete guide to the ([^"]+) breed\.">',
        r'<meta name="twitter:description" content="Guida completa alla razza \1.">',
        content
    )
    
    # 6. Fix Schema.org URLs
    content = re.sub(
        r'"@id": "https://breedfinder\.org/breeds/([^"]+)"',
        r'"@id": "https://breedfinder.org/it/breeds/\1"',
        content
    )
    
    # 7. Translate breadcrumb schema
    content = content.replace('"name": "Dog Breeds"', '"name": "Razze di Cani"')
    content = content.replace('"item": "https://breedfinder.org/breeds/"', '"item": "https://breedfinder.org/it/breeds/"')
    content = content.replace('"item": "https://breedfinder.org/"', '"item": "https://breedfinder.org/it/"')
    
    # 8. Translate Schema.org headline
    content = re.sub(
        r'"headline": "([^"]+): Breed Guide, Temperament & Care"',
        r'"headline": "\1: Guida alla Razza, Temperamento e Cura"',
        content
    )
    content = re.sub(
        r'"description": "Complete guide to the ([^"]+): temperament, exercise needs, grooming, and care tips\."',
        r'"description": "Guida completa al \1: temperamento, esigenze di esercizio, toelettatura e consigli per la cura."',
        content
    )
    
    # 9. Translate navigation
    content = content.replace('>Browse Breeds</a>', '>Tutte le Razze</a>')
    content = content.replace('>All Breeds</a>', '>Tutte le Razze</a>')
    content = content.replace('>Take Quiz</a>', '>Quiz</a>')
    content = content.replace('>Breed Quiz</a>', '>Quiz</a>')
    
    # 10. Translate breadcrumb text
    content = re.sub(
        r'>Home</a> → \s*<a href="\.\./breeds/" class="hover:text-sky-700">Breeds</a>',
        r'>Home</a> → <a href="../breeds/" class="hover:text-sky-700">Razze</a>',
        content
    )
    
    # 11. Translate labels
    content = content.replace('</i> Origin', '</i> Origine')
    content = content.replace('</i> Lifespan', '</i> Longevità')
    content = content.replace('</i> Height', '</i> Altezza')
    content = content.replace('</i> Weight', '</i> Peso')
    
    # 12. Translate "Breed Ratings"
    content = content.replace('>Breed Ratings</h2>', '>Valutazioni della Razza</h2>')
    
    # 13. Translate rating labels
    content = content.replace('<span>Energy Level</span>', '<span>Livello di Energia</span>')
    content = content.replace('<span>Grooming Needs</span>', '<span>Toelettatura</span>')
    content = content.replace('<span>Trainability</span>', '<span>Addestrabilità</span>')
    content = content.replace('<span>Kid Friendly</span>', '<span>Adatto ai Bambini</span>')
    content = content.replace('<span>Apartment Friendly</span>', '<span>Adatto in Appartamento</span>')
    content = content.replace('<span>Barking Level</span>', '<span>Tendenza ad Abbaiare</span>')
    content = content.replace('<span>Sociability</span>', '<span>Socialità</span>')
    
    # 14. Translate section headers
    content = re.sub(
        r'</i> Overview\s*</h2>',
        r'</i> Panoramica</h2>',
        content
    )
    content = re.sub(
        r'</i> Temperament\s*</h2>',
        r'</i> Temperamento</h2>',
        content
    )
    content = re.sub(
        r'</i> Health\s*</h2>',
        r'</i> Salute</h2>',
        content
    )
    content = re.sub(
        r'</i> Exercise\s*</h2>',
        r'</i> Esercizio</h2>',
        content
    )
    
    # 15. Translate "Temperament" standalone header
    content = re.sub(
        r'<h2 class="text-2xl font-bold text-slate-900 mb-6">Temperament</h2>',
        r'<h2 class="text-2xl font-bold text-slate-900 mb-6">Temperamento</h2>',
        content
    )
    
    # 16. Translate verdict section
    content = content.replace('Is This Breed Right for You?', 'Questa Razza Fa per Te?')
    content = content.replace('Best For', 'Ideale Per')
    content = content.replace('Not Ideal For', 'Non Ideale Per')
    content = content.replace('<strong>Our Verdict:</strong>', '<strong>Il Nostro Verdetto:</strong>')
    
    # 17. Translate footer
    content = content.replace('Find your perfect dog breed match', 'Trova la razza di cane perfetta per te')
    content = content.replace('>About</a>', '>Chi Siamo</a>')
    content = content.replace('Made with care for dog lovers everywhere.', 'Fatto con amore per gli amanti dei cani.')
    
    # 18. Translate title
    content = re.sub(
        r'<title>([^<]+) - Dog Breed Guide \| BreedFinder</title>',
        r'<title>\1 - Guida alla Razza | BreedFinder</title>',
        content
    )
    
    # Write the updated content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python translate_it.py <file.html> [file2.html ...]")
        sys.exit(1)
    
    for filepath in sys.argv[1:]:
        if os.path.exists(filepath):
            print(f"Translating: {filepath}")
            translate_file(filepath)
        else:
            print(f"File not found: {filepath}")

if __name__ == "__main__":
    main()
