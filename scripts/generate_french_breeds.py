#!/usr/bin/env python3
"""
Generate fully translated French breed pages from English JSON data
"""

import json
import os
import re
from pathlib import Path

# French breed names
BREED_NAMES_FR = {
    'Affenpinscher': 'Affenpinscher',
    'Afghan Hound': 'Lévrier Afghan',
    'Airedale Terrier': 'Airedale Terrier',
    'Akita': 'Akita',
    'Alaskan Klee Kai': 'Klee Kai d\'Alaska',
    'Alaskan Malamute': 'Malamute de l\'Alaska',
    'American Bulldog': 'Bouledogue Américain',
    'American English Coonhound': 'Coonhound Anglais Américain',
    'American Eskimo Dog': 'Chien Esquimau Américain',
    'American Foxhound': 'Foxhound Américain',
    'American Hairless Terrier': 'Terrier Américain Sans Poil',
    'American Staffordshire Terrier': 'American Staffordshire Terrier',
    'American Water Spaniel': 'Épagneul d\'Eau Américain',
    'Anatolian Shepherd': 'Berger d\'Anatolie',
    'Appenzeller Sennenhund': 'Bouvier de l\'Appenzell',
    'Australian Cattle Dog': 'Bouvier Australien',
    'Australian Shepherd': 'Berger Australien',
    'Australian Terrier': 'Terrier Australien',
    'Azawakh': 'Azawakh',
    'Barbet': 'Barbet',
    'Basenji': 'Basenji',
    'Basset Hound': 'Basset Hound',
    'Beagle': 'Beagle',
    'Beauceron': 'Beauceron',
    'Bedlington Terrier': 'Bedlington Terrier',
    'Belgian Laekenois': 'Berger Belge Laekenois',
    'Belgian Malinois': 'Berger Belge Malinois',
    'Belgian Sheepdog': 'Berger Belge Groenendael',
    'Belgian Tervuren': 'Berger Belge Tervueren',
    'Bergamasco Sheepdog': 'Berger de Bergame',
    'Berger Picard': 'Berger Picard',
    'Bernese Mountain Dog': 'Bouvier Bernois',
    'Bichon Frise': 'Bichon à Poil Frisé',
    'Biewer Terrier': 'Biewer Terrier',
    'Black and Tan Coonhound': 'Coonhound Noir et Feu',
    'Black Russian Terrier': 'Terrier Noir Russe',
    'Bloodhound': 'Chien de Saint-Hubert',
    'Bluetick Coonhound': 'Bluetick Coonhound',
    'Boerboel': 'Boerboel',
    'Bolognese': 'Bichon Bolonais',
    'Border Collie': 'Border Collie',
    'Border Terrier': 'Border Terrier',
    'Borzoi': 'Barzoï',
    'Boston Terrier': 'Boston Terrier',
    'Bouvier des Flandres': 'Bouvier des Flandres',
    'Boxer': 'Boxer',
    'Boykin Spaniel': 'Épagneul Boykin',
    'Bracco Italiano': 'Braque Italien',
    'Briard': 'Briard',
    'Brittany': 'Épagneul Breton',
    'Brussels Griffon': 'Griffon Bruxellois',
    'Bull Terrier': 'Bull Terrier',
    'Bulldog': 'Bouledogue Anglais',
    'Bullmastiff': 'Bullmastiff',
    'Cairn Terrier': 'Cairn Terrier',
    'Canaan Dog': 'Chien de Canaan',
    'Cane Corso': 'Cane Corso',
    'Cardigan Welsh Corgi': 'Welsh Corgi Cardigan',
    'Cavalier King Charles Spaniel': 'Cavalier King Charles',
    'Cesky Terrier': 'Terrier Tchèque',
    'Chesapeake Bay Retriever': 'Retriever de la Baie de Chesapeake',
    'Chihuahua': 'Chihuahua',
    'Chinese Crested': 'Chien Chinois à Crête',
    'Chinook': 'Chinook',
    'Chow Chow': 'Chow-Chow',
    "Cirneco dell'Etna": 'Cirneco de l\'Etna',
    'Clumber Spaniel': 'Clumber Spaniel',
    'Cocker Spaniel': 'Cocker Américain',
    'Collie': 'Colley',
    'Coton de Tulear': 'Coton de Tuléar',
    'Curly-Coated Retriever': 'Retriever à Poil Bouclé',
    'Dachshund': 'Teckel',
    'Dalmatian': 'Dalmatien',
    'Dandie Dinmont Terrier': 'Dandie Dinmont Terrier',
    'Deutscher Wachtelhund': 'Chien d\'Oysel Allemand',
    'Doberman Pinscher': 'Dobermann',
    'Dogo Argentino': 'Dogue Argentin',
    'Dogue de Bordeaux': 'Dogue de Bordeaux',
    'Drentse Patrijshond': 'Épagneul de Drente',
    'Dutch Shepherd': 'Berger Hollandais',
    'English Cocker Spaniel': 'Cocker Anglais',
    'English Foxhound': 'Foxhound Anglais',
    'English Pointer': 'Pointer Anglais',
    'English Setter': 'Setter Anglais',
    'English Springer Spaniel': 'Springer Anglais',
    'English Toy Spaniel': 'King Charles',
    'Entlebucher Mountain Dog': 'Bouvier de l\'Entlebuch',
    'Eurasier': 'Eurasier',
    'Field Spaniel': 'Field Spaniel',
    'Finnish Lapphund': 'Chien Finnois de Laponie',
    'Finnish Spitz': 'Spitz Finlandais',
    'Flat-Coated Retriever': 'Retriever à Poil Plat',
    'French Bulldog': 'Bouledogue Français',
    'German Shepherd': 'Berger Allemand',
    'German Shorthaired Pointer': 'Braque Allemand à Poil Court',
    'German Spitz': 'Spitz Allemand',
    'German Wirehaired Pointer': 'Braque Allemand à Poil Dur',
    'Giant Schnauzer': 'Schnauzer Géant',
    'Glen of Imaal Terrier': 'Glen of Imaal Terrier',
    'Golden Retriever': 'Golden Retriever',
    'Gordon Setter': 'Setter Gordon',
    'Grand Basset Griffon Vendéen': 'Grand Basset Griffon Vendéen',
    'Great Dane': 'Dogue Allemand',
    'Great Pyrenees': 'Chien de Montagne des Pyrénées',
    'Greater Swiss Mountain Dog': 'Grand Bouvier Suisse',
    'Greyhound': 'Lévrier Greyhound',
    'Harrier': 'Harrier',
    'Havanese': 'Bichon Havanais',
    'Hokkaido': 'Hokkaido',
    'Hovawart': 'Hovawart',
    'Ibizan Hound': 'Podenco d\'Ibiza',
    'Icelandic Sheepdog': 'Berger Islandais',
    'Irish Red and White Setter': 'Setter Irlandais Rouge et Blanc',
    'Irish Setter': 'Setter Irlandais',
    'Irish Water Spaniel': 'Épagneul d\'Eau Irlandais',
    'Irish Wolfhound': 'Lévrier Irlandais',
    'Italian Greyhound': 'Petit Lévrier Italien',
    'Jack Russell Terrier': 'Jack Russell Terrier',
    'Japanese Chin': 'Épagneul Japonais',
    'Japanese Spitz': 'Spitz Japonais',
    'Kai Ken': 'Kai',
    'Keeshond': 'Spitz-Loup',
    'Kerry Blue Terrier': 'Kerry Blue Terrier',
    'Kishu Ken': 'Kishu',
    'Komondor': 'Komondor',
    'Korean Jindo': 'Jindo Coréen',
    'Kuvasz': 'Kuvasz',
    'Labrador Retriever': 'Labrador Retriever',
    'Lagotto Romagnolo': 'Lagotto Romagnolo',
    'Lakeland Terrier': 'Lakeland Terrier',
    'Landseer': 'Landseer',
    'Large Münsterländer': 'Grand Münsterländer',
    'Leonberger': 'Leonberg',
    'Lhasa Apso': 'Lhassa Apso',
    'Löwchen': 'Petit Chien Lion',
    'Maltese': 'Bichon Maltais',
    'Manchester Terrier': 'Manchester Terrier',
    'Mastiff': 'Mastiff',
    'Miniature American Shepherd': 'Berger Américain Miniature',
    'Miniature Pinscher': 'Pinscher Nain',
    'Miniature Schnauzer': 'Schnauzer Nain',
    'Mudi': 'Mudi',
    'Neapolitan Mastiff': 'Mâtin Napolitain',
    'Nederlandse Kooikerhondje': 'Kooikerhondje',
    'Newfoundland': 'Terre-Neuve',
    'Norfolk Terrier': 'Norfolk Terrier',
    'Norwegian Buhund': 'Buhund Norvégien',
    'Norwegian Elkhound': 'Chien d\'Élan Norvégien',
    'Norwegian Lundehund': 'Lundehund',
    'Norwich Terrier': 'Norwich Terrier',
    'Nova Scotia Duck Tolling Retriever': 'Retriever de Nouvelle-Écosse',
    'Old English Sheepdog': 'Bobtail',
    'Otterhound': 'Otterhound',
    'Papillon': 'Épagneul Nain Continental Papillon',
    'Parson Russell Terrier': 'Parson Russell Terrier',
    'Pekingese': 'Pékinois',
    'Pembroke Welsh Corgi': 'Welsh Corgi Pembroke',
    'Peruvian Inca Orchid': 'Chien Nu du Pérou',
    'Petit Basset Griffon Vendéen': 'Petit Basset Griffon Vendéen',
    'Pharaoh Hound': 'Chien du Pharaon',
    'Plott Hound': 'Plott Hound',
    'Polish Lowland Sheepdog': 'Berger Polonais de Plaine',
    'Pomeranian': 'Spitz Nain',
    'Poodle': 'Caniche',
    'Portuguese Podengo Pequeno': 'Podengo Portugais Petit',
    'Portuguese Water Dog': 'Chien d\'Eau Portugais',
    'Pudelpointer': 'Pudelpointer',
    'Pug': 'Carlin',
    'Puli': 'Puli',
    'Pumi': 'Pumi',
    'Pyrenean Shepherd': 'Berger des Pyrénées',
    'Rat Terrier': 'Rat Terrier',
    'Redbone Coonhound': 'Redbone Coonhound',
    'Rhodesian Ridgeback': 'Rhodesian Ridgeback',
    'Rottweiler': 'Rottweiler',
    'Russell Terrier': 'Russell Terrier',
    'Russian Toy': 'Russkiy Toy',
    'Saluki': 'Saluki',
    'Samoyed': 'Samoyède',
    'Schipperke': 'Schipperke',
    'Scottish Deerhound': 'Deerhound',
    'Scottish Terrier': 'Scottish Terrier',
    'Sealyham Terrier': 'Sealyham Terrier',
    'Shar-Pei': 'Shar-Pei',
    'Shetland Sheepdog': 'Berger des Shetland',
    'Shiba Inu': 'Shiba Inu',
    'Shih Tzu': 'Shih Tzu',
    'Shikoku': 'Shikoku',
    'Siberian Husky': 'Husky Sibérien',
    'Silky Terrier': 'Silky Terrier Australien',
    'Skye Terrier': 'Skye Terrier',
    'Sloughi': 'Sloughi',
    'Small Münsterländer': 'Petit Münsterländer',
    'Smooth Fox Terrier': 'Fox Terrier à Poil Lisse',
    'Soft Coated Wheaten Terrier': 'Terrier Irlandais à Poil Doux',
    'Spanish Water Dog': 'Chien d\'Eau Espagnol',
    'Spinone Italiano': 'Spinone Italien',
    'St. Bernard': 'Saint-Bernard',
    'Staffordshire Bull Terrier': 'Staffordshire Bull Terrier',
    'Standard Schnauzer': 'Schnauzer Moyen',
    'Sussex Spaniel': 'Sussex Spaniel',
    'Swedish Vallhund': 'Vallhund Suédois',
    'Thai Ridgeback': 'Thai Ridgeback',
    'Tibetan Mastiff': 'Dogue du Tibet',
    'Tibetan Spaniel': 'Épagneul Tibétain',
    'Tibetan Terrier': 'Terrier Tibétain',
    'Toy Fox Terrier': 'Toy Fox Terrier',
    'Treeing Walker Coonhound': 'Treeing Walker Coonhound',
    'Vizsla': 'Braque Hongrois',
    'Weimaraner': 'Braque de Weimar',
    'Welsh Springer Spaniel': 'Springer Gallois',
    'Welsh Terrier': 'Welsh Terrier',
    'West Highland White Terrier': 'West Highland White Terrier',
    'Whippet': 'Whippet',
    'White Swiss Shepherd': 'Berger Blanc Suisse',
    'Wire Fox Terrier': 'Fox Terrier à Poil Dur',
    'Wirehaired Pointing Griffon': 'Griffon d\'Arrêt à Poil Dur',
    'Wirehaired Vizsla': 'Braque Hongrois à Poil Dur',
    'Xoloitzcuintli': 'Xoloitzcuintle',
    'Yorkshire Terrier': 'Yorkshire Terrier',
}

def get_french_name(english_name):
    """Get French breed name, fallback to English if not found"""
    return BREED_NAMES_FR.get(english_name, english_name)

# Group translations
GROUPS = {
    'sporting': 'Chien de Chasse',
    'hound': 'Chien Courant',
    'working': 'Chien de Travail',
    'terrier': 'Terrier',
    'toy': 'Chien de Compagnie',
    'non-sporting': 'Chien Non-Sportif',
    'herding': 'Chien de Berger',
    'miscellaneous': 'Divers',
    'foundation': 'Foundation',
}

# Size translations
SIZES = {
    'tiny': 'Très Petit',
    'small': 'Petit',
    'medium': 'Moyen',
    'large': 'Grand',
    'giant': 'Géant',
}

# Temperament trait translations
TRAITS = {
    'friendly': 'amical', 'loyal': 'loyal', 'intelligent': 'intelligent', 'active': 'actif',
    'gentle': 'doux', 'playful': 'joueur', 'protective': 'protecteur', 'calm': 'calme',
    'affectionate': 'affectueux', 'alert': 'alerte', 'energetic': 'énergique', 'independent': 'indépendant',
    'stubborn': 'têtu', 'confident': 'confiant', 'curious': 'curieux', 'outgoing': 'sociable',
    'brave': 'courageux', 'patient': 'patient', 'devoted': 'dévoué', 'eager': 'enthousiaste',
    'trainable': 'facile à dresser', 'adaptable': 'adaptable', 'reserved': 'réservé',
    'dignified': 'digne', 'sensitive': 'sensible', 'fearless': 'intrépide', 'spirited': 'vif',
    'loving': 'aimant', 'obedient': 'obéissant', 'athletic': 'athlétique', 'agile': 'agile',
    'smart': 'malin', 'charming': 'charmant', 'lively': 'vif', 'bold': 'audacieux',
    'watchful': 'vigilant', 'powerful': 'puissant', 'mischievous': 'espiègle', 'noble': 'noble',
    'steady': 'stable', 'sweet': 'doux', 'happy': 'heureux', 'cheerful': 'joyeux',
    'determined': 'déterminé', 'territorial': 'territorial', 'hardworking': 'travailleur',
    'sociable': 'sociable', 'docile': 'docile', 'easygoing': 'facile à vivre', 'versatile': 'polyvalent',
    'regal': 'royal', 'graceful': 'gracieux', 'elegant': 'élégant', 'aloof': 'distant',
    'funny': 'drôle', 'courageous': 'courageux', 'keen': 'vif', 'good-natured': 'de bonne nature',
    'even-tempered': 'équilibré', 'reliable': 'fiable', 'trusting': 'confiant',
    'self-confident': 'sûr de soi', 'proud': 'fier', 'fast': 'rapide', 'tough': 'robuste',
    'feisty': 'fougueux', 'spunky': 'courageux', 'peppy': 'pétillant', 'perky': 'alerte',
    'quiet': 'calme', 'responsive': 'réactif', 'stable': 'stable', 'eager to please': 'désireux de plaire',
    'people-oriented': 'proche des gens', 'family-oriented': 'orienté famille',
    'cat-like': 'félin', 'clownish': 'clownesque', 'comical': 'comique',
    'happy-go-lucky': 'insouciant', 'good-humored': 'de bonne humeur', 'amiable': 'aimable',
    'companionable': 'sociable', 'fun-loving': 'joueur', 'boisterous': 'turbulent',
    'assertive': 'affirmatif', 'willful': 'volontaire', 'strong-willed': 'déterminé',
    'demanding': 'exigeant', 'dominant': 'dominant', 'intense': 'intense',
    'focused': 'concentré', 'driven': 'motivé', 'tireless': 'infatigable',
    'rugged': 'robuste', 'sturdy': 'solide', 'muscular': 'musclé', 'imposing': 'imposant',
    'majestic': 'majestueux', 'serene': 'serein', 'mellow': 'doux',
    'trustworthy': 'digne de confiance', 'kind': 'gentil',
}

# Best For translations
BEST_FOR = {
    'Families with children': 'Familles avec enfants',
    'Active individuals': 'Personnes actives',
    'First-time dog owners': 'Premiers propriétaires',
    'First-time owners': 'Premiers propriétaires',
    'Homes with yards': 'Maisons avec jardin',
    'People who enjoy outdoor activities': 'Amateurs de plein air',
    'Apartment dwellers': 'Habitants d\'appartement',
    'Seniors': 'Personnes âgées',
    'Experienced owners': 'Propriétaires expérimentés',
    'Singles and couples': 'Célibataires et couples',
    'Working from home': 'Télétravail',
    'Allergy sufferers': 'Personnes allergiques',
    'Those wanting a guard dog': 'Ceux qui veulent un chien de garde',
    'Runners and hikers': 'Coureurs et randonneurs',
    'Active families': 'Familles actives',
    'Those who work from home': 'Ceux qui travaillent à domicile',
    'Adults only': 'Adultes uniquement',
    'Those wanting a character': 'Ceux qui veulent un caractère',
    'Experienced dog owners': 'Propriétaires de chiens expérimentés',
    'Rural homes': 'Maisons rurales',
    'Hunters': 'Chasseurs',
    'Those with time for grooming': 'Ceux avec du temps pour le toilettage',
    'Those with large yards': 'Ceux avec un grand jardin',
    'Those seeking a loyal companion': 'Ceux qui cherchent un compagnon fidèle',
    'Active outdoor enthusiasts': 'Passionnés de plein air actifs',
    'Farms and ranches': 'Fermes et ranchs',
    'Those who want a lap dog': 'Ceux qui veulent un chien de salon',
    'Quiet households': 'Foyers calmes',
    'Multi-pet households': 'Foyers multi-animaux',
    'Calm households': 'Foyers calmes',
    'Active households': 'Foyers actifs',
    'Those wanting a therapy/service dog': 'Ceux qui veulent un chien de thérapie',
    'Dog sport enthusiasts': 'Passionnés de sports canins',
    'Families': 'Familles',
    'Active people': 'Personnes actives',
}

# Not Ideal translations
NOT_IDEAL = {
    'Sedentary lifestyles': 'Modes de vie sédentaires',
    'Those away from home often': 'Souvent absents de la maison',
    'Allergy sufferers': 'Personnes allergiques',
    'Small apartment dwellers': 'Petits appartements',
    'Small apartments': 'Petits appartements',
    'First-time owners': 'Premiers propriétaires',
    'First-time dog owners': 'Premiers propriétaires',
    'Families with very young children': 'Familles avec très jeunes enfants',
    'Families with young children': 'Familles avec jeunes enfants',
    'Hot climates': 'Climats chauds',
    'Cold climates': 'Climats froids',
    'Novice trainers': 'Dresseurs débutants',
    'Homes with small pets': 'Foyers avec petits animaux',
    'Those who dislike grooming': 'Ceux qui n\'aiment pas le toilettage',
    'Quiet neighborhoods required': 'Quartiers calmes requis',
    'Apartment living': 'Vie en appartement',
    'Inactive owners': 'Propriétaires inactifs',
    'Busy schedules': 'Emplois du temps chargés',
    'Extreme climates': 'Climats extrêmes',
    'Those wanting a guard dog': 'Ceux qui veulent un chien de garde',
    'Those who dislike dog hair': 'Ceux qui n\'aiment pas les poils',
    'Very small living spaces': 'Très petits espaces',
    'Inexperienced owners': 'Propriétaires inexpérimentés',
}

def translate_trait(trait):
    """Translate a temperament trait to French"""
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

def generate_french_overview(breed):
    """Generate French overview text"""
    name = get_french_name(breed['name'])
    group = translate_group(breed.get('group', 'miscellaneous'))
    size = translate_size(breed['size']['category'])
    
    traits = breed.get('temperament', [])[:3]
    traits_fr = [translate_trait(t) for t in traits]
    traits_str = ', '.join(traits_fr) if traits_fr else 'polyvalent'
    
    origin = breed.get('origin', 'inconnu')
    
    templates = [
        f"Le {name} est un {group} {traits_str} originaire de {origin}. Cette race de taille {size.lower()} est connue pour sa personnalité unique et fait un merveilleux compagnon pour la bonne famille.",
        f"En tant que {group} {traits_str} de {origin}, le {name} a conquis de nombreux admirateurs dans le monde entier. Cette race de taille {size.lower()} allie caractère et loyauté.",
        f"Le {name} est un {group} de taille {size.lower()} au tempérament {traits_str}. Originaire de {origin}, cette race est très populaire auprès des amateurs de chiens.",
    ]
    
    import hashlib
    idx = int(hashlib.md5(name.encode()).hexdigest(), 16) % len(templates)
    return templates[idx]

def generate_french_temperament(breed):
    """Generate French temperament description"""
    name = get_french_name(breed['name'])
    traits = breed.get('temperament', [])
    traits_fr = [translate_trait(t) for t in traits[:4]]
    
    if len(traits_fr) >= 2:
        return f"Le {name} est {traits_fr[0]} et {traits_fr[1]}. Cette race est connue pour son caractère équilibré et forme des liens forts avec sa famille. Avec une socialisation et un dressage appropriés, ils deviennent des compagnons loyaux et affectueux."
    return f"Le {name} a un tempérament équilibré et, avec une bonne éducation, devient un fidèle compagnon familial."

def generate_french_health(breed):
    """Generate French health description"""
    name = get_french_name(breed['name'])
    lifespan = breed.get('lifespan', '10-12 years').replace(' years', ' ans').replace(' year', ' an')
    size_cat = breed['size']['category']
    
    health_issues = {
        'tiny': 'luxation de la rotule, problèmes dentaires et maladies cardiaques',
        'small': 'luxation de la rotule, problèmes dentaires et maladies oculaires',
        'medium': 'dysplasie de la hanche, allergies et problèmes oculaires',
        'large': 'dysplasie de la hanche et du coude, ballonnements et maladies cardiaques',
        'giant': 'dysplasie de la hanche, torsion d\'estomac et problèmes cardiaques',
    }
    
    issues = health_issues.get(size_cat, 'problèmes de santé typiques de la race')
    return f"Le {name} a une espérance de vie de {lifespan}. Comme beaucoup de races de cette taille, ils peuvent être sujets à {issues}. Des visites vétérinaires régulières et une alimentation équilibrée sont importantes pour une vie longue et saine."

def generate_french_exercise(breed):
    """Generate French exercise description"""
    name = get_french_name(breed['name'])
    energy = breed.get('ratings', {}).get('energy', 3)
    
    if energy >= 4:
        return f"Le {name} est une race très énergique qui nécessite au moins 60-90 minutes d'exercice quotidien. Les longues promenades, la course et les jeux actifs sont idéaux. Sans suffisamment d'exercice physique et mental, des problèmes de comportement peuvent survenir."
    elif energy >= 3:
        return f"Le {name} a besoin d'exercice modéré avec des promenades quotidiennes de 30-60 minutes. Le temps de jeu dans le jardin et les jeux interactifs gardent cette race heureuse et en bonne santé. Une activité régulière est importante pour le bien-être physique et mental."
    else:
        return f"Le {name} a des besoins d'exercice faibles à modérés. De courtes promenades quotidiennes et du temps de jeu suffisent. Cette race convient bien aux personnes ayant un mode de vie plus calme, mais nécessite tout de même une activité légère régulière."

def generate_french_verdict(breed):
    """Generate French verdict summary"""
    name = get_french_name(breed['name'])
    traits = breed.get('temperament', [])[:2]
    traits_fr = [translate_trait(t) for t in traits]
    traits_str = ' et '.join(traits_fr) if traits_fr else 'polyvalent'
    
    best = breed.get('verdict', {}).get('best_for', [])
    
    if 'Families with children' in best or 'Active families' in best:
        return f"Le {name} est un excellent chien de famille. Avec son tempérament {traits_str}, il convient parfaitement aux familles actives qui ont du temps pour le dressage et les activités."
    elif 'Apartment dwellers' in best:
        return f"Le {name} est parfaitement adapté à la vie en appartement. Son tempérament {traits_str} en fait un compagnon idéal pour les citadins."
    elif 'Experienced owners' in best:
        return f"Le {name} convient mieux aux propriétaires expérimentés. Cette race {traits_str} nécessite un dressage cohérent et une direction ferme."
    else:
        return f"Le {name} est un compagnon {traits_str} pour la bonne famille. Avec des soins et un dressage appropriés, cette race devient un ami fidèle pour la vie."

def generate_breed_html(breed):
    """Generate complete French HTML for a breed"""
    name_en = breed['name']
    name = get_french_name(name_en)
    slug = breed['id']
    group = breed.get('group', 'miscellaneous')
    origin = breed.get('origin', 'Unknown')
    lifespan = breed.get('lifespan', '10-12 years').replace(' years', ' ans').replace(' year', ' an')
    
    height_cm = breed['size'].get('height_cm', '25-30')
    weight_kg = breed['size'].get('weight_kg', '5-10')
    size_cat = breed['size']['category']
    
    def cm_to_in(cm_str):
        parts = cm_str.split('-')
        if len(parts) == 2:
            return f"{round(float(parts[0]) / 2.54)}-{round(float(parts[1]) / 2.54)}"
        return str(round(float(parts[0]) / 2.54))
    
    def kg_to_lbs(kg_str):
        parts = kg_str.split('-')
        if len(parts) == 2:
            return f"{round(float(parts[0]) * 2.205)}-{round(float(parts[1]) * 2.205)}"
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
    best_for = verdict.get('best_for', ['Familles', 'Personnes actives'])
    not_for = verdict.get('not_for', ['Très petits appartements'])
    
    best_html = '\n'.join([f'<li class="flex items-start gap-3"><span class="w-2 h-2 mt-2 bg-emerald-500 rounded-full"></span><span>{translate_best_for(b)}</span></li>' for b in best_for])
    not_html = '\n'.join([f'<li class="flex items-start gap-3"><span class="w-2 h-2 mt-2 bg-rose-500 rounded-full"></span><span>{translate_not_ideal(n)}</span></li>' for n in not_for])
    
    overview = generate_french_overview(breed)
    temperament_text = generate_french_temperament(breed)
    health_text = generate_french_health(breed)
    exercise_text = generate_french_exercise(breed)
    verdict_text = generate_french_verdict(breed)
    
    html = f'''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} | BreedFinder</title>
    <meta name="description" content="{overview[:150]}">
    <link rel="canonical" href="https://breedfinder.org/fr/breeds/{slug}.html">
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
                    <span class="hidden md:inline">Parcourir les Races</span>
                </a>
                <a href="../quiz/" class="bg-gradient-to-r from-sky-500 to-violet-500 text-white px-4 py-2 rounded-xl">Faire le Quiz</a>
            </nav>
        </div>
    </header>

    <main class="max-w-5xl mx-auto px-4 py-8">
        <nav class="text-sm text-slate-500 mb-6 flex items-center gap-2">
            <a href="../" class="hover:text-sky-600">Accueil</a>
            <i data-lucide="chevron-right" class="w-4 h-4"></i>
            <a href="../search/" class="hover:text-sky-600">Parcourir les Races</a>
            <i data-lucide="chevron-right" class="w-4 h-4"></i>
            <span class="text-slate-700 font-medium">{name}</span>
        </nav>

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
                                <i data-lucide="map-pin" class="w-3 h-3"></i> Origine
                            </div>
                            <div class="text-slate-800 font-semibold">{origin}</div>
                        </div>
                        <div class="bg-slate-50 rounded-xl p-4">
                            <div class="text-xs font-medium text-slate-500 uppercase mb-1 flex items-center gap-1">
                                <i data-lucide="heart" class="w-3 h-3"></i> Espérance de vie
                            </div>
                            <div class="text-slate-800 font-semibold">{lifespan}</div>
                        </div>
                        <div class="bg-slate-50 rounded-xl p-4">
                            <div class="text-xs font-medium text-slate-500 uppercase mb-1 flex items-center gap-1">
                                <i data-lucide="ruler" class="w-3 h-3"></i> Taille
                            </div>
                            <div class="text-slate-800 font-semibold">{height_cm} cm ({height_in} in)</div>
                        </div>
                        <div class="bg-slate-50 rounded-xl p-4">
                            <div class="text-xs font-medium text-slate-500 uppercase mb-1 flex items-center gap-1">
                                <i data-lucide="scale" class="w-3 h-3"></i> Poids
                            </div>
                            <div class="text-slate-800 font-semibold">{weight_kg} kg ({weight_lbs} lbs)</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="bg-white rounded-2xl p-6 mb-8 shadow-sm border border-slate-100">
            <h2 class="text-xl font-bold mb-4">Évaluations de la Race</h2>
            <div class="grid md:grid-cols-2 gap-4">
                <div>
                    <div class="flex justify-between text-sm mb-1"><span>Niveau d'énergie</span><span>{energy}/5</span></div>
                    <div class="rating-bar h-2 rounded-full" style="--rating: {energy * 20}%"></div>
                </div>
                <div>
                    <div class="flex justify-between text-sm mb-1"><span>Toilettage</span><span>{grooming}/5</span></div>
                    <div class="rating-bar h-2 rounded-full" style="--rating: {grooming * 20}%"></div>
                </div>
                <div>
                    <div class="flex justify-between text-sm mb-1"><span>Facilité de dressage</span><span>{trainability}/5</span></div>
                    <div class="rating-bar h-2 rounded-full" style="--rating: {trainability * 20}%"></div>
                </div>
                <div>
                    <div class="flex justify-between text-sm mb-1"><span>Adapté aux enfants</span><span>{kid_friendly}/5</span></div>
                    <div class="rating-bar h-2 rounded-full" style="--rating: {kid_friendly * 20}%"></div>
                </div>
                <div>
                    <div class="flex justify-between text-sm mb-1"><span>Adapté à l'appartement</span><span>{apartment}/5</span></div>
                    <div class="rating-bar h-2 rounded-full" style="--rating: {apartment * 20}%"></div>
                </div>
                <div>
                    <div class="flex justify-between text-sm mb-1"><span>Tendance aux aboiements</span><span>{barking}/5</span></div>
                    <div class="rating-bar h-2 rounded-full" style="--rating: {barking * 20}%"></div>
                </div>
            </div>
        </div>

        <div class="bg-white rounded-3xl p-8 mb-8 card-shadow border border-slate-100">
            <h2 class="text-2xl font-bold text-slate-900 mb-6">Tempérament</h2>
            <div class="flex flex-wrap gap-2">{temp_html}</div>
        </div>

        <div class="space-y-4 mb-8">
            <details class="bg-white rounded-2xl shadow-sm border border-slate-100 group" open>
                <summary class="p-6 cursor-pointer flex items-center justify-between">
                    <h2 class="text-xl font-bold flex items-center gap-3">
                        <i data-lucide="book-open" class="w-5 h-5 text-sky-500"></i> Aperçu
                    </h2>
                    <i data-lucide="chevron-down" class="w-5 h-5 text-slate-400 group-open:rotate-180 transition-transform"></i>
                </summary>
                <div class="px-6 pb-6"><p class="text-slate-600">{overview}</p></div>
            </details>
            <details class="bg-white rounded-2xl shadow-sm border border-slate-100 group">
                <summary class="p-6 cursor-pointer flex items-center justify-between">
                    <h2 class="text-xl font-bold flex items-center gap-3">
                        <i data-lucide="heart" class="w-5 h-5 text-sky-500"></i> Tempérament
                    </h2>
                    <i data-lucide="chevron-down" class="w-5 h-5 text-slate-400 group-open:rotate-180 transition-transform"></i>
                </summary>
                <div class="px-6 pb-6"><p class="text-slate-600">{temperament_text}</p></div>
            </details>
            <details class="bg-white rounded-2xl shadow-sm border border-slate-100 group">
                <summary class="p-6 cursor-pointer flex items-center justify-between">
                    <h2 class="text-xl font-bold flex items-center gap-3">
                        <i data-lucide="heart-pulse" class="w-5 h-5 text-sky-500"></i> Santé
                    </h2>
                    <i data-lucide="chevron-down" class="w-5 h-5 text-slate-400 group-open:rotate-180 transition-transform"></i>
                </summary>
                <div class="px-6 pb-6"><p class="text-slate-600">{health_text}</p></div>
            </details>
            <details class="bg-white rounded-2xl shadow-sm border border-slate-100 group">
                <summary class="p-6 cursor-pointer flex items-center justify-between">
                    <h2 class="text-xl font-bold flex items-center gap-3">
                        <i data-lucide="activity" class="w-5 h-5 text-sky-500"></i> Exercice
                    </h2>
                    <i data-lucide="chevron-down" class="w-5 h-5 text-slate-400 group-open:rotate-180 transition-transform"></i>
                </summary>
                <div class="px-6 pb-6"><p class="text-slate-600">{exercise_text}</p></div>
            </details>
        </div>

        <div class="bg-gradient-to-br from-sky-50 via-violet-50 to-rose-50 rounded-2xl p-6 mb-8 border border-sky-100">
            <h2 class="text-xl font-bold mb-6 flex items-center gap-3">
                <span class="w-10 h-10 bg-gradient-to-br from-sky-500 to-violet-500 rounded-xl flex items-center justify-center text-white">⦿</span>
                Cette Race Est-Elle Faite Pour Vous ?
            </h2>
            <div class="grid md:grid-cols-2 gap-6 mb-6">
                <div class="bg-white/80 rounded-xl p-5 border border-emerald-100">
                    <h3 class="font-bold text-emerald-700 mb-3 flex items-center gap-2">
                        <span class="text-emerald-500">✓</span> Idéal Pour
                    </h3>
                    <ul class="space-y-2 text-slate-700 text-sm">{best_html}</ul>
                </div>
                <div class="bg-white/80 rounded-xl p-5 border border-rose-100">
                    <h3 class="font-bold text-rose-700 mb-3 flex items-center gap-2">
                        <span class="text-rose-500">✗</span> Pas Idéal Pour
                    </h3>
                    <ul class="space-y-2 text-slate-700 text-sm">{not_html}</ul>
                </div>
            </div>
            <div class="bg-white/80 rounded-xl p-5 border border-slate-200">
                <p class="text-slate-700"><strong>Notre Verdict :</strong> {verdict_text}</p>
            </div>
        </div>

        <div class="text-center">
            <a href="../search/" class="inline-flex items-center gap-2 text-sky-600 font-semibold hover:text-sky-700">
                <i data-lucide="arrow-left" class="w-4 h-4"></i>
                Parcourir les Races
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
    output_dir = base_dir / "fr" / "breeds"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    with open(breeds_file, 'r', encoding='utf-8') as f:
        breeds = json.load(f)
    
    print(f"Generating {len(breeds)} French breed pages...")
    
    for breed in breeds:
        html = generate_breed_html(breed)
        output_file = output_dir / f"{breed['id']}.html"
        output_file.write_text(html, encoding='utf-8')
        print(f"  ✓ {breed['name']} → {get_french_name(breed['name'])}")
    
    print(f"\n✅ Done! Generated {len(breeds)} French breed pages")

if __name__ == "__main__":
    main()
