#!/usr/bin/env python3
"""Fix popular breeds section with correct translations"""

import os
import re

# Translations for popular breeds
BREEDS = {
    'de': {
        'Labrador Retriever': 'Labrador Retriever',
        'German Shepherd': 'Deutscher Schäferhund', 
        'Golden Retriever': 'Golden Retriever',
        'French Bulldog': 'Französische Bulldogge',
        'Poodle': 'Pudel',
        'Siberian Husky': 'Siberian Husky',
        'Beagle': 'Beagle',
        'Dachshund': 'Dackel',
        'Friendly · Active · Loyal': 'Freundlich · Aktiv · Treu',
        'Intelligent · Protective': 'Intelligent · Beschützend',
        'Gentle · Friendly · Smart': 'Sanft · Freundlich · Klug',
        'Playful · Adaptable': 'Verspielt · Anpassungsfähig',
        'Intelligent · Elegant': 'Intelligent · Elegant',
        'Energetic · Outgoing': 'Energisch · Aufgeschlossen',
        'Curious · Merry': 'Neugierig · Fröhlich',
        'Clever · Devoted': 'Clever · Ergeben',
    },
    'es': {
        'Labrador Retriever': 'Labrador Retriever',
        'German Shepherd': 'Pastor Alemán',
        'Golden Retriever': 'Golden Retriever', 
        'French Bulldog': 'Bulldog Francés',
        'Poodle': 'Caniche',
        'Siberian Husky': 'Husky Siberiano',
        'Beagle': 'Beagle',
        'Dachshund': 'Teckel',
        'Friendly · Active · Loyal': 'Amigable · Activo · Leal',
        'Intelligent · Protective': 'Inteligente · Protector',
        'Gentle · Friendly · Smart': 'Gentil · Amigable · Inteligente',
        'Playful · Adaptable': 'Juguetón · Adaptable',
        'Intelligent · Elegant': 'Inteligente · Elegante',
        'Energetic · Outgoing': 'Enérgico · Extrovertido',
        'Curious · Merry': 'Curioso · Alegre',
        'Clever · Devoted': 'Listo · Devoto',
    },
    'fr': {
        'Labrador Retriever': 'Labrador Retriever',
        'German Shepherd': 'Berger Allemand',
        'Golden Retriever': 'Golden Retriever',
        'French Bulldog': 'Bouledogue Français',
        'Poodle': 'Caniche',
        'Siberian Husky': 'Husky Sibérien',
        'Beagle': 'Beagle',
        'Dachshund': 'Teckel',
        'Friendly · Active · Loyal': 'Amical · Actif · Loyal',
        'Intelligent · Protective': 'Intelligent · Protecteur',
        'Gentle · Friendly · Smart': 'Doux · Amical · Intelligent',
        'Playful · Adaptable': 'Joueur · Adaptable',
        'Intelligent · Elegant': 'Intelligent · Élégant',
        'Energetic · Outgoing': 'Énergique · Extraverti',
        'Curious · Merry': 'Curieux · Joyeux',
        'Clever · Devoted': 'Malin · Dévoué',
    },
    'it': {
        'Labrador Retriever': 'Labrador Retriever',
        'German Shepherd': 'Pastore Tedesco',
        'Golden Retriever': 'Golden Retriever',
        'French Bulldog': 'Bulldog Francese',
        'Poodle': 'Barboncino',
        'Siberian Husky': 'Husky Siberiano',
        'Beagle': 'Beagle',
        'Dachshund': 'Bassotto',
        'Friendly · Active · Loyal': 'Amichevole · Attivo · Leale',
        'Intelligent · Protective': 'Intelligente · Protettivo',
        'Gentle · Friendly · Smart': 'Gentile · Amichevole · Intelligente',
        'Playful · Adaptable': 'Giocoso · Adattabile',
        'Intelligent · Elegant': 'Intelligente · Elegante',
        'Energetic · Outgoing': 'Energico · Estroverso',
        'Curious · Merry': 'Curioso · Allegro',
        'Clever · Devoted': 'Furbo · Devoto',
    },
    'pt': {
        'Labrador Retriever': 'Labrador Retriever',
        'German Shepherd': 'Pastor Alemão',
        'Golden Retriever': 'Golden Retriever',
        'French Bulldog': 'Buldogue Francês',
        'Poodle': 'Poodle',
        'Siberian Husky': 'Husky Siberiano',
        'Beagle': 'Beagle',
        'Dachshund': 'Dachshund',
        'Friendly · Active · Loyal': 'Amigável · Ativo · Leal',
        'Intelligent · Protective': 'Inteligente · Protetor',
        'Gentle · Friendly · Smart': 'Gentil · Amigável · Inteligente',
        'Playful · Adaptable': 'Brincalhão · Adaptável',
        'Intelligent · Elegant': 'Inteligente · Elegante',
        'Energetic · Outgoing': 'Energético · Extrovertido',
        'Curious · Merry': 'Curioso · Alegre',
        'Clever · Devoted': 'Esperto · Devotado',
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
