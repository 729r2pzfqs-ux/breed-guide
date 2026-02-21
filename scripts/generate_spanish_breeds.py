#!/usr/bin/env python3
"""
Generate fully translated Spanish breed pages from English JSON data
"""

import json
import os
import re
from pathlib import Path

# Spanish breed names (native names where applicable)
BREED_NAMES_ES = {
    'Affenpinscher': 'Affenpinscher',
    'Afghan Hound': 'Lebrel Afgano',
    'Airedale Terrier': 'Airedale Terrier',
    'Akita': 'Akita',
    'Alaskan Klee Kai': 'Klee Kai de Alaska',
    'Alaskan Malamute': 'Malamute de Alaska',
    'American Bulldog': 'Bulldog Americano',
    'American English Coonhound': 'Coonhound Inglés Americano',
    'American Eskimo Dog': 'Perro Esquimal Americano',
    'American Foxhound': 'Foxhound Americano',
    'American Hairless Terrier': 'Terrier Americano Sin Pelo',
    'American Staffordshire Terrier': 'American Staffordshire Terrier',
    'American Water Spaniel': 'Spaniel de Agua Americano',
    'Anatolian Shepherd': 'Pastor de Anatolia',
    'Appenzeller Sennenhund': 'Boyero de Appenzell',
    'Australian Cattle Dog': 'Boyero Australiano',
    'Australian Shepherd': 'Pastor Australiano',
    'Australian Terrier': 'Terrier Australiano',
    'Azawakh': 'Azawakh',
    'Barbet': 'Barbet',
    'Basenji': 'Basenji',
    'Basset Hound': 'Basset Hound',
    'Beagle': 'Beagle',
    'Beauceron': 'Beauceron',
    'Bedlington Terrier': 'Bedlington Terrier',
    'Belgian Laekenois': 'Pastor Belga Laekenois',
    'Belgian Malinois': 'Pastor Belga Malinois',
    'Belgian Sheepdog': 'Pastor Belga Groenendael',
    'Belgian Tervuren': 'Pastor Belga Tervuerense',
    'Bergamasco Sheepdog': 'Pastor Bergamasco',
    'Berger Picard': 'Pastor de Picardía',
    'Bernese Mountain Dog': 'Boyero de Berna',
    'Bichon Frise': 'Bichón Frisé',
    'Biewer Terrier': 'Biewer Terrier',
    'Black and Tan Coonhound': 'Coonhound Negro y Fuego',
    'Black Russian Terrier': 'Terrier Ruso Negro',
    'Bloodhound': 'Bloodhound',
    'Bluetick Coonhound': 'Bluetick Coonhound',
    'Boerboel': 'Boerboel',
    'Bolognese': 'Bichón Boloñés',
    'Border Collie': 'Border Collie',
    'Border Terrier': 'Border Terrier',
    'Borzoi': 'Borzoi',
    'Boston Terrier': 'Boston Terrier',
    'Bouvier des Flandres': 'Boyero de Flandes',
    'Boxer': 'Bóxer',
    'Boykin Spaniel': 'Spaniel Boykin',
    'Bracco Italiano': 'Braco Italiano',
    'Briard': 'Briard',
    'Brittany': 'Bretón',
    'Brussels Griffon': 'Grifón de Bruselas',
    'Bull Terrier': 'Bull Terrier',
    'Bulldog': 'Bulldog Inglés',
    'Bullmastiff': 'Bullmastiff',
    'Cairn Terrier': 'Cairn Terrier',
    'Canaan Dog': 'Perro de Canaán',
    'Cane Corso': 'Cane Corso',
    'Cardigan Welsh Corgi': 'Welsh Corgi Cardigan',
    'Cavalier King Charles Spaniel': 'Cavalier King Charles Spaniel',
    'Cesky Terrier': 'Terrier Checo',
    'Chesapeake Bay Retriever': 'Retriever de la Bahía de Chesapeake',
    'Chihuahua': 'Chihuahua',
    'Chinese Crested': 'Crestado Chino',
    'Chinook': 'Chinook',
    'Chow Chow': 'Chow Chow',
    "Cirneco dell'Etna": 'Cirneco del Etna',
    'Clumber Spaniel': 'Clumber Spaniel',
    'Cocker Spaniel': 'Cocker Spaniel Americano',
    'Collie': 'Collie',
    'Coton de Tulear': 'Coton de Tuléar',
    'Curly-Coated Retriever': 'Retriever de Pelo Rizado',
    'Dachshund': 'Teckel',
    'Dalmatian': 'Dálmata',
    'Dandie Dinmont Terrier': 'Dandie Dinmont Terrier',
    'Deutscher Wachtelhund': 'Perro de Muestra Alemán',
    'Doberman Pinscher': 'Dóberman',
    'Dogo Argentino': 'Dogo Argentino',
    'Dogue de Bordeaux': 'Dogo de Burdeos',
    'Drentse Patrijshond': 'Perdiguero de Drente',
    'Dutch Shepherd': 'Pastor Holandés',
    'English Cocker Spaniel': 'Cocker Spaniel Inglés',
    'English Foxhound': 'Foxhound Inglés',
    'English Pointer': 'Pointer Inglés',
    'English Setter': 'Setter Inglés',
    'English Springer Spaniel': 'Springer Spaniel Inglés',
    'English Toy Spaniel': 'Spaniel Inglés Toy',
    'Entlebucher Mountain Dog': 'Boyero de Entlebuch',
    'Eurasier': 'Eurasier',
    'Field Spaniel': 'Field Spaniel',
    'Finnish Lapphund': 'Lapphund Finlandés',
    'Finnish Spitz': 'Spitz Finlandés',
    'Flat-Coated Retriever': 'Retriever de Pelo Liso',
    'French Bulldog': 'Bulldog Francés',
    'German Shepherd': 'Pastor Alemán',
    'German Shorthaired Pointer': 'Braco Alemán de Pelo Corto',
    'German Spitz': 'Spitz Alemán',
    'German Wirehaired Pointer': 'Braco Alemán de Pelo Duro',
    'Giant Schnauzer': 'Schnauzer Gigante',
    'Glen of Imaal Terrier': 'Glen of Imaal Terrier',
    'Golden Retriever': 'Golden Retriever',
    'Gordon Setter': 'Setter Gordon',
    'Grand Basset Griffon Vendéen': 'Gran Basset Grifón Vendeano',
    'Great Dane': 'Gran Danés',
    'Great Pyrenees': 'Gran Pirineo',
    'Greater Swiss Mountain Dog': 'Gran Boyero Suizo',
    'Greyhound': 'Galgo Inglés',
    'Harrier': 'Harrier',
    'Havanese': 'Bichón Habanero',
    'Hokkaido': 'Hokkaido',
    'Hovawart': 'Hovawart',
    'Ibizan Hound': 'Podenco Ibicenco',
    'Icelandic Sheepdog': 'Pastor Islandés',
    'Irish Red and White Setter': 'Setter Irlandés Rojo y Blanco',
    'Irish Setter': 'Setter Irlandés',
    'Irish Water Spaniel': 'Spaniel de Agua Irlandés',
    'Irish Wolfhound': 'Lobero Irlandés',
    'Italian Greyhound': 'Galgo Italiano',
    'Jack Russell Terrier': 'Jack Russell Terrier',
    'Japanese Chin': 'Chin Japonés',
    'Japanese Spitz': 'Spitz Japonés',
    'Kai Ken': 'Kai Ken',
    'Keeshond': 'Keeshond',
    'Kerry Blue Terrier': 'Kerry Blue Terrier',
    'Kishu Ken': 'Kishu Ken',
    'Komondor': 'Komondor',
    'Korean Jindo': 'Jindo Coreano',
    'Kuvasz': 'Kuvasz',
    'Labrador Retriever': 'Labrador Retriever',
    'Lagotto Romagnolo': 'Lagotto Romagnolo',
    'Lakeland Terrier': 'Lakeland Terrier',
    'Landseer': 'Landseer',
    'Large Münsterländer': 'Münsterländer Grande',
    'Leonberger': 'Leonberger',
    'Lhasa Apso': 'Lhasa Apso',
    'Löwchen': 'Löwchen',
    'Maltese': 'Maltés',
    'Manchester Terrier': 'Manchester Terrier',
    'Mastiff': 'Mastín Inglés',
    'Miniature American Shepherd': 'Pastor Americano Miniatura',
    'Miniature Bull Terrier': 'Bull Terrier Miniatura',
    'Miniature Pinscher': 'Pinscher Miniatura',
    'Miniature Schnauzer': 'Schnauzer Miniatura',
    'Neapolitan Mastiff': 'Mastín Napolitano',
    'Nederlandse Kooikerhondje': 'Kooikerhondje',
    'Newfoundland': 'Terranova',
    'Norfolk Terrier': 'Norfolk Terrier',
    'Norwegian Buhund': 'Buhund Noruego',
    'Norwegian Elkhound': 'Elkhound Noruego',
    'Norwegian Lundehund': 'Lundehund Noruego',
    'Norwich Terrier': 'Norwich Terrier',
    'Nova Scotia Duck Tolling Retriever': 'Retriever de Nueva Escocia',
    'Old English Sheepdog': 'Bobtail',
    'Otterhound': 'Otterhound',
    'Papillon': 'Papillón',
    'Parson Russell Terrier': 'Parson Russell Terrier',
    'Pekingese': 'Pequinés',
    'Pembroke Welsh Corgi': 'Welsh Corgi Pembroke',
    'Peruvian Inca Orchid': 'Perro sin Pelo del Perú',
    'Petit Basset Griffon Vendéen': 'Pequeño Basset Grifón Vendeano',
    'Pharaoh Hound': 'Podenco Faraónico',
    'Plott Hound': 'Plott Hound',
    'Pointer': 'Pointer',
    'Polish Lowland Sheepdog': 'Pastor Polaco de las Llanuras',
    'Pomeranian': 'Pomerania',
    'Poodle': 'Caniche',
    'Portuguese Podengo Pequeno': 'Podengo Portugués Pequeño',
    'Portuguese Water Dog': 'Perro de Agua Portugués',
    'Pug': 'Carlino',
    'Puli': 'Puli',
    'Pumi': 'Pumi',
    'Pyrenean Shepherd': 'Pastor de los Pirineos',
    'Rat Terrier': 'Rat Terrier',
    'Redbone Coonhound': 'Redbone Coonhound',
    'Rhodesian Ridgeback': 'Rhodesian Ridgeback',
    'Rottweiler': 'Rottweiler',
    'Russell Terrier': 'Russell Terrier',
    'Saint Bernard': 'San Bernardo',
    'Saluki': 'Saluki',
    'Samoyed': 'Samoyedo',
    'Schipperke': 'Schipperke',
    'Scottish Deerhound': 'Lebrel Escocés',
    'Scottish Terrier': 'Scottish Terrier',
    'Sealyham Terrier': 'Sealyham Terrier',
    'Shetland Sheepdog': 'Pastor de Shetland',
    'Shiba Inu': 'Shiba Inu',
    'Shih Tzu': 'Shih Tzu',
    'Shikoku': 'Shikoku',
    'Siberian Husky': 'Husky Siberiano',
    'Silky Terrier': 'Silky Terrier Australiano',
    'Skye Terrier': 'Skye Terrier',
    'Sloughi': 'Sloughi',
    'Smooth Fox Terrier': 'Fox Terrier de Pelo Liso',
    'Soft Coated Wheaten Terrier': 'Wheaten Terrier de Pelo Suave',
    'Spanish Water Dog': 'Perro de Agua Español',
    'Spinone Italiano': 'Spinone Italiano',
    'Staffordshire Bull Terrier': 'Staffordshire Bull Terrier',
    'Standard Poodle': 'Caniche Estándar',
    'Standard Schnauzer': 'Schnauzer Estándar',
    'Sussex Spaniel': 'Sussex Spaniel',
    'Swedish Lapphund': 'Lapphund Sueco',
    'Swedish Vallhund': 'Vallhund Sueco',
    'Thai Ridgeback': 'Thai Ridgeback',
    'Tibetan Mastiff': 'Mastín Tibetano',
    'Tibetan Spaniel': 'Spaniel Tibetano',
    'Tibetan Terrier': 'Terrier Tibetano',
    'Toy Fox Terrier': 'Toy Fox Terrier',
    'Toy Poodle': 'Caniche Toy',
    'Treeing Walker Coonhound': 'Treeing Walker Coonhound',
    'Vizsla': 'Vizsla',
    'Weimaraner': 'Weimaraner',
    'Welsh Springer Spaniel': 'Springer Spaniel Galés',
    'Welsh Terrier': 'Welsh Terrier',
    'West Highland White Terrier': 'West Highland White Terrier',
    'Whippet': 'Whippet',
    'Wire Fox Terrier': 'Fox Terrier de Pelo Duro',
    'Wirehaired Pointing Griffon': 'Grifón de Muestra de Pelo Duro',
    'Wirehaired Vizsla': 'Vizsla de Pelo Duro',
    'Xoloitzcuintli': 'Xoloitzcuintle',
    'Yorkshire Terrier': 'Yorkshire Terrier',
}

# Get Spanish name
def get_spanish_name(name):
    return BREED_NAMES_ES.get(name, name)

# Group translations
GROUPS = {
    'herding': 'Pastoreo',
    'hound': 'Sabueso',
    'working': 'Trabajo',
    'terrier': 'Terrier',
    'toy': 'Toy',
    'sporting': 'Deportivo',
    'non-sporting': 'No Deportivo',
    'miscellaneous': 'Misceláneo',
}

# Size translations
SIZES = {
    'tiny': 'Muy pequeño',
    'small': 'Pequeño',
    'medium': 'Mediano',
    'large': 'Grande',
    'giant': 'Gigante',
}

# Temperament trait translations
TRAITS = {
    'loyal': 'Leal',
    'intelligent': 'Inteligente',
    'friendly': 'Amigable',
    'playful': 'Juguetón',
    'energetic': 'Enérgico',
    'calm': 'Tranquilo',
    'alert': 'Alerta',
    'protective': 'Protector',
    'affectionate': 'Cariñoso',
    'gentle': 'Gentil',
    'independent': 'Independiente',
    'brave': 'Valiente',
    'confident': 'Seguro',
    'stubborn': 'Testarudo',
    'active': 'Activo',
    'eager to please': 'Deseoso de complacer',
    'good-natured': 'Buen carácter',
    'outgoing': 'Extrovertido',
    'curious': 'Curioso',
    'patient': 'Paciente',
    'devoted': 'Devoto',
    'dignified': 'Digno',
    'reserved': 'Reservado',
    'watchful': 'Vigilante',
    'sensitive': 'Sensible',
    'trainable': 'Entrenable',
    'sociable': 'Sociable',
    'athletic': 'Atlético',
    'courageous': 'Valiente',
    'determined': 'Determinado',
    'spirited': 'Animado',
    'lively': 'Vivaz',
    'cheerful': 'Alegre',
    'adaptable': 'Adaptable',
    'obedient': 'Obediente',
    'versatile': 'Versátil',
    'bold': 'Audaz',
    'fearless': 'Intrépido',
    'agile': 'Ágil',
    'hard-working': 'Trabajador',
    'loving': 'Amoroso',
    'sweet': 'Dulce',
    'mischievous': 'Travieso',
    'clever': 'Listo',
    'fast': 'Rápido',
    'graceful': 'Elegante',
    'noble': 'Noble',
    'proud': 'Orgulloso',
    'keen': 'Agudo',
    'even-tempered': 'Ecuánime',
    'stable': 'Estable',
    'quiet': 'Callado',
    'responsive': 'Receptivo',
    'fun-loving': 'Divertido',
    'charming': 'Encantador',
    'easygoing': 'Tranquilo',
    'docile': 'Dócil',
    'reliable': 'Confiable',
    'steady': 'Constante',
    'attentive': 'Atento',
    'self-assured': 'Seguro de sí mismo',
    'regal': 'Regio',
    'inquisitive': 'Inquisitivo',
    'quick': 'Rápido',
    'smart': 'Inteligente',
    'wilful': 'Voluntarioso',
    'aloof': 'Distante',
    'territorial': 'Territorial',
    'dominant': 'Dominante',
    'powerful': 'Poderoso',
    'muscular': 'Musculoso',
    'strong': 'Fuerte',
    'imposing': 'Imponente',
    'majestic': 'Majestuoso',
    'serene': 'Sereno',
    'trusting': 'Confiado',
    'happy': 'Feliz',
    'joyful': 'Alegre',
    'peppy': 'Animado',
    'spunky': 'Animoso',
    'perky': 'Vivaracho',
}

# Best For translations
BEST_FOR = {
    'Families with children': 'Familias con niños',
    'Homes with yards': 'Casas con jardín',
    'People who enjoy outdoor activities': 'Personas que disfrutan actividades al aire libre',
    'Apartment dwellers': 'Personas en apartamentos',
    'Seniors': 'Personas mayores',
    'Experienced owners': 'Dueños con experiencia',
    'Singles and couples': 'Solteros y parejas',
    'Working from home': 'Trabajo desde casa',
    'Allergy sufferers': 'Personas con alergias',
    'Those wanting a guard dog': 'Quienes buscan un perro guardián',
    'Runners and hikers': 'Corredores y excursionistas',
    'Active families': 'Familias activas',
    'Those who work from home': 'Quienes trabajan desde casa',
    'Adults only': 'Solo adultos',
    'Those wanting a character': 'Quienes buscan un perro con personalidad',
    'Experienced dog owners': 'Dueños de perros con experiencia',
    'Rural homes': 'Hogares rurales',
    'Hunters': 'Cazadores',
    'Those with time for grooming': 'Quienes tienen tiempo para el aseo',
    'Those with large yards': 'Quienes tienen jardín grande',
    'Those seeking a loyal companion': 'Quienes buscan un compañero leal',
    'Active outdoor enthusiasts': 'Entusiastas del aire libre activos',
    'Farms and ranches': 'Granjas y ranchos',
    'Those who want a lap dog': 'Quienes quieren un perro faldero',
    'Quiet households': 'Hogares tranquilos',
    'Multi-pet households': 'Hogares con múltiples mascotas',
    'Calm households': 'Hogares tranquilos',
    'Active households': 'Hogares activos',
    'Those wanting a therapy/service dog': 'Quienes quieren un perro de terapia',
    'Dog sport enthusiasts': 'Entusiastas de deportes caninos',
    'Families': 'Familias',
    'Active people': 'Personas activas',
}

# Not Ideal translations
NOT_IDEAL = {
    'Sedentary lifestyles': 'Estilos de vida sedentarios',
    'Those away from home often': 'Quienes están fuera de casa a menudo',
    'Allergy sufferers': 'Personas con alergias',
    'Small apartment dwellers': 'Apartamentos pequeños',
    'Small apartments': 'Apartamentos pequeños',
    'First-time owners': 'Dueños primerizos',
    'First-time dog owners': 'Dueños de perros primerizos',
    'Families with very young children': 'Familias con niños muy pequeños',
    'Families with young children': 'Familias con niños pequeños',
    'Hot climates': 'Climas cálidos',
    'Cold climates': 'Climas fríos',
    'Novice trainers': 'Entrenadores novatos',
    'Homes with small pets': 'Hogares con mascotas pequeñas',
    'Those who dislike grooming': 'Quienes no les gusta el aseo',
    'Quiet neighborhoods required': 'Se requieren vecindarios tranquilos',
    'Apartment living': 'Vida en apartamento',
    'Inactive owners': 'Dueños inactivos',
    'Busy schedules': 'Agendas ocupadas',
    'Extreme climates': 'Climas extremos',
    'Those wanting a guard dog': 'Quienes buscan un perro guardián',
    'Those who dislike dog hair': 'Quienes no les gusta el pelo de perro',
    'Very small living spaces': 'Espacios de vida muy pequeños',
    'Inexperienced owners': 'Dueños sin experiencia',
}

def translate_trait(trait):
    """Translate a temperament trait to Spanish"""
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

def generate_spanish_overview(breed):
    """Generate Spanish overview text"""
    name = get_spanish_name(breed['name'])
    group = translate_group(breed.get('group', 'miscellaneous'))
    size = translate_size(breed['size']['category'])
    
    traits = breed.get('temperament', [])[:3]
    traits_es = [translate_trait(t) for t in traits]
    traits_str = ', '.join(traits_es) if traits_es else 'versátil'
    
    origin = breed.get('origin', 'desconocido')
    
    templates = [
        f"El {name} es un perro de {group} {traits_str} originario de {origin}. Esta raza de tamaño {size.lower()} es conocida por su personalidad única y es un compañero maravilloso para la familia adecuada.",
        f"Como perro de {group} {traits_str} de {origin}, el {name} ha conquistado muchos admiradores en todo el mundo. Esta raza de tamaño {size.lower()} combina carácter y lealtad.",
        f"El {name} es un perro de {group} de tamaño {size.lower()} con temperamento {traits_str}. Originario de {origin}, esta raza es muy popular entre los amantes de los perros.",
    ]
    
    import hashlib
    idx = int(hashlib.md5(name.encode()).hexdigest(), 16) % len(templates)
    return templates[idx]

def generate_spanish_temperament(breed):
    """Generate Spanish temperament description"""
    name = get_spanish_name(breed['name'])
    traits = breed.get('temperament', [])
    traits_es = [translate_trait(t) for t in traits[:4]]
    
    if len(traits_es) >= 2:
        return f"El {name} es {traits_es[0]} y {traits_es[1]}. Esta raza es conocida por su carácter equilibrado y forma vínculos fuertes con su familia. Con una socialización y entrenamiento adecuados, se convierten en compañeros leales y cariñosos."
    return f"El {name} tiene un temperamento equilibrado y, con una buena educación, se convierte en un fiel compañero familiar."

def generate_spanish_health(breed):
    """Generate Spanish health description"""
    name = get_spanish_name(breed['name'])
    lifespan = breed.get('lifespan', '10-12 years').replace(' years', ' años').replace(' year', ' año')
    size_cat = breed['size']['category']
    
    health_issues = {
        'tiny': 'luxación de rótula, problemas dentales y enfermedades cardíacas',
        'small': 'luxación de rótula, problemas dentales y enfermedades oculares',
        'medium': 'displasia de cadera, alergias y problemas oculares',
        'large': 'displasia de cadera y codo, hinchazón y enfermedades cardíacas',
        'giant': 'displasia de cadera, torsión gástrica y problemas cardíacos',
    }
    
    issues = health_issues.get(size_cat, 'problemas de salud típicos de la raza')
    return f"El {name} tiene una esperanza de vida de {lifespan}. Como muchas razas de este tamaño, pueden ser propensos a {issues}. Las visitas veterinarias regulares y una alimentación equilibrada son importantes para una vida larga y saludable."

def generate_spanish_exercise(breed):
    """Generate Spanish exercise description"""
    name = get_spanish_name(breed['name'])
    energy = breed.get('ratings', {}).get('energy', 3)
    
    if energy >= 4:
        return f"El {name} es una raza muy enérgica que necesita al menos 60-90 minutos de ejercicio diario. Los paseos largos, correr y los juegos activos son ideales. Sin suficiente ejercicio físico y mental, pueden surgir problemas de comportamiento."
    elif energy >= 3:
        return f"El {name} necesita ejercicio moderado con paseos diarios de 30-60 minutos. El tiempo de juego en el jardín y los juegos interactivos mantienen a esta raza feliz y saludable. La actividad regular es importante para el bienestar físico y mental."
    else:
        return f"El {name} tiene necesidades de ejercicio bajas a moderadas. Paseos cortos diarios y tiempo de juego son suficientes. Esta raza es adecuada para personas con un estilo de vida más tranquilo, pero aún necesita actividad ligera regular."

def generate_spanish_verdict(breed):
    """Generate Spanish verdict summary"""
    name = get_spanish_name(breed['name'])
    traits = breed.get('temperament', [])[:2]
    traits_es = [translate_trait(t) for t in traits]
    traits_str = ' y '.join(traits_es) if traits_es else 'versátil'
    
    best = breed.get('verdict', {}).get('best_for', [])
    
    if 'Families with children' in best or 'Active families' in best:
        return f"El {name} es un excelente perro de familia. Con su temperamento {traits_str}, es perfecto para familias activas que tienen tiempo para el entrenamiento y las actividades."
    elif 'Apartment dwellers' in best:
        return f"El {name} es perfectamente adecuado para la vida en apartamento. Su temperamento {traits_str} lo convierte en un compañero ideal para los habitantes de la ciudad."
    elif 'Experienced owners' in best:
        return f"El {name} es más adecuado para dueños experimentados. Esta raza {traits_str} requiere entrenamiento consistente y dirección firme."
    else:
        return f"El {name} es un compañero {traits_str} para la familia adecuada. Con el cuidado y entrenamiento apropiados, esta raza se convierte en un amigo fiel de por vida."

def generate_breed_html(breed):
    """Generate complete Spanish HTML for a breed"""
    name_en = breed['name']
    name = get_spanish_name(name_en)
    slug = breed['id']
    group = breed.get('group', 'miscellaneous')
    origin = breed.get('origin', 'Desconocido')
    lifespan = breed.get('lifespan', '10-12 years').replace(' years', ' años').replace(' year', ' año')
    
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
    best_for = verdict.get('best_for', [])
    not_ideal = verdict.get('not_ideal', [])
    
    best_for_html = ''.join([f'<li class="flex items-start gap-2"><svg class="w-5 h-5 text-green-500 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg><span>{translate_best_for(item)}</span></li>' for item in best_for[:5]])
    not_ideal_html = ''.join([f'<li class="flex items-start gap-2"><svg class="w-5 h-5 text-red-500 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg><span>{translate_not_ideal(item)}</span></li>' for item in not_ideal[:5]])
    
    overview = generate_spanish_overview(breed)
    temperament_text = generate_spanish_temperament(breed)
    health_text = generate_spanish_health(breed)
    exercise_text = generate_spanish_exercise(breed)
    verdict_text = generate_spanish_verdict(breed)
    
    group_translated = translate_group(group)
    size_translated = translate_size(size_cat)
    
    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - Información de la Raza | BreedFinder</title>
    <meta name="description" content="Aprende todo sobre el {name}: temperamento, cuidados, salud y si es la raza adecuada para tu familia.">
    <link rel="canonical" href="https://breedfinder.org/es/breeds/{slug}/">
    <link rel="alternate" hreflang="en" href="https://breedfinder.org/breeds/{slug}/">
    <link rel="alternate" hreflang="es" href="https://breedfinder.org/es/breeds/{slug}/">
    <link rel="alternate" hreflang="de" href="https://breedfinder.org/de/breeds/{slug}/">
    <link rel="alternate" hreflang="fr" href="https://breedfinder.org/fr/breeds/{slug}/">
    <link rel="alternate" hreflang="x-default" href="https://breedfinder.org/breeds/{slug}/">
    <meta property="og:title" content="{name} - Información de la Raza">
    <meta property="og:description" content="Guía completa del {name}: temperamento, cuidados, salud y más.">
    <meta property="og:image" content="https://breedfinder.org/images/breeds/{slug}.webp">
    <meta property="og:url" content="https://breedfinder.org/es/breeds/{slug}/">
    <meta property="og:type" content="article">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
        .rating-bar {{ height: 8px; background: #e2e8f0; border-radius: 4px; overflow: hidden; }}
        .rating-bar::after {{ content: ''; display: block; height: 100%; border-radius: 4px; background: linear-gradient(90deg, #0ea5e9, #8b5cf6); }}
        .rating-1::after {{ width: 20%; }}
        .rating-2::after {{ width: 40%; }}
        .rating-3::after {{ width: 60%; }}
        .rating-4::after {{ width: 80%; }}
        .rating-5::after {{ width: 100%; }}
    </style>
</head>
<body class="bg-slate-50 text-slate-800">
    <nav class="bg-white/80 backdrop-blur-md border-b border-slate-200 sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-4">
            <div class="flex items-center justify-between">
                <a href="/es/" class="flex items-center gap-2">
                    <span class="text-2xl">🐕</span>
                    <span class="font-bold text-xl bg-gradient-to-r from-sky-600 to-violet-600 bg-clip-text text-transparent">BreedFinder</span>
                </a>
                <div class="flex items-center gap-6">
                    <a href="/es/breeds/" class="text-slate-600 hover:text-slate-900 font-medium hidden sm:block">Razas</a>
                    <a href="/es/quiz/" class="text-slate-600 hover:text-slate-900 font-medium hidden sm:block">Quiz</a>
                    <a href="/es/compare/" class="text-slate-600 hover:text-slate-900 font-medium hidden sm:block">Comparar</a>
                    <a href="/es/search/" class="text-slate-600 hover:text-slate-900 font-medium sm:hidden">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                    </a>
                    <a href="/es/search/" class="text-slate-600 hover:text-slate-900 font-medium hidden sm:block">Buscar</a>
                    <div class="relative group">
                        <button class="flex items-center gap-1 text-slate-600 hover:text-slate-900 font-medium">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"></path></svg>
                            <span class="text-sm">ES</span>
                        </button>
                        <div class="absolute right-0 mt-2 w-32 bg-white rounded-lg shadow-lg border border-slate-200 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">
                            <a href="/breeds/{slug}/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-slate-50 rounded-t-lg">English</a>
                            <a href="/es/breeds/{slug}/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-slate-50 bg-slate-100">Español</a>
                            <a href="/de/breeds/{slug}/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-slate-50">Deutsch</a>
                            <a href="/fr/breeds/{slug}/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-slate-50 rounded-b-lg">Français</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </nav>

    <main class="max-w-6xl mx-auto px-4 py-8">
        <nav class="text-sm text-slate-500 mb-6">
            <a href="/es/" class="hover:text-sky-600">Inicio</a>
            <span class="mx-2">/</span>
            <a href="/es/breeds/" class="hover:text-sky-600">Razas</a>
            <span class="mx-2">/</span>
            <span class="text-slate-700">{name}</span>
        </nav>

        <div class="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden mb-8">
            <div class="md:flex">
                <div class="md:w-2/5">
                    <img src="/images/breeds/{slug}.webp" alt="{name}" class="w-full h-72 md:h-full object-cover object-top">
                </div>
                <div class="md:w-3/5 p-6 md:p-8">
                    <div class="flex flex-wrap gap-2 mb-4">
                        <span class="bg-sky-100 text-sky-700 px-3 py-1 rounded-full text-sm font-medium">{group_translated}</span>
                        <span class="bg-violet-100 text-violet-700 px-3 py-1 rounded-full text-sm font-medium">{size_translated}</span>
                    </div>
                    <h1 class="text-3xl md:text-4xl font-bold text-slate-900 mb-4">{name}</h1>
                    <div class="grid grid-cols-2 gap-4">
                        <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-xl">
                            <svg class="w-6 h-6 text-sky-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                            <div>
                                <p class="text-xs text-slate-500">Origen</p>
                                <p class="font-semibold text-slate-700">{origin}</p>
                            </div>
                        </div>
                        <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-xl">
                            <svg class="w-6 h-6 text-sky-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                            <div>
                                <p class="text-xs text-slate-500">Esperanza de vida</p>
                                <p class="font-semibold text-slate-700">{lifespan}</p>
                            </div>
                        </div>
                        <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-xl">
                            <svg class="w-6 h-6 text-sky-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4"></path></svg>
                            <div>
                                <p class="text-xs text-slate-500">Altura</p>
                                <p class="font-semibold text-slate-700">{height_cm} cm ({height_in} in)</p>
                            </div>
                        </div>
                        <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-xl">
                            <svg class="w-6 h-6 text-sky-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"></path></svg>
                            <div>
                                <p class="text-xs text-slate-500">Peso</p>
                                <p class="font-semibold text-slate-700">{weight_kg} kg ({weight_lbs} lbs)</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <section class="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 md:p-8 mb-8">
            <h2 class="text-xl font-bold text-slate-900 mb-6">Calificaciones de la Raza</h2>
            <div class="grid md:grid-cols-2 gap-x-12 gap-y-4">
                <div>
                    <div class="flex justify-between mb-2"><span class="text-slate-600">Energía</span><span class="font-medium">{energy}/5</span></div>
                    <div class="rating-bar rating-{energy}"></div>
                </div>
                <div>
                    <div class="flex justify-between mb-2"><span class="text-slate-600">Aseo</span><span class="font-medium">{grooming}/5</span></div>
                    <div class="rating-bar rating-{grooming}"></div>
                </div>
                <div>
                    <div class="flex justify-between mb-2"><span class="text-slate-600">Entrenabilidad</span><span class="font-medium">{trainability}/5</span></div>
                    <div class="rating-bar rating-{trainability}"></div>
                </div>
                <div>
                    <div class="flex justify-between mb-2"><span class="text-slate-600">Amigable con niños</span><span class="font-medium">{kid_friendly}/5</span></div>
                    <div class="rating-bar rating-{kid_friendly}"></div>
                </div>
                <div>
                    <div class="flex justify-between mb-2"><span class="text-slate-600">Apto para apartamento</span><span class="font-medium">{apartment}/5</span></div>
                    <div class="rating-bar rating-{apartment}"></div>
                </div>
                <div>
                    <div class="flex justify-between mb-2"><span class="text-slate-600">Ladridos</span><span class="font-medium">{barking}/5</span></div>
                    <div class="rating-bar rating-{barking}"></div>
                </div>
            </div>
        </section>

        <section class="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 md:p-8 mb-8">
            <h2 class="text-xl font-bold text-slate-900 mb-4">Temperamento</h2>
            <div class="flex flex-wrap gap-2">
                {temp_html}
            </div>
        </section>

        <section class="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 md:p-8 mb-8 space-y-4">
            <details class="group" open>
                <summary class="flex items-center justify-between cursor-pointer list-none">
                    <h2 class="text-xl font-bold text-slate-900 flex items-center gap-2">
                        <span>📖</span> Descripción General
                    </h2>
                    <svg class="w-5 h-5 text-slate-400 group-open:rotate-180 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                </summary>
                <p class="mt-4 text-slate-600 leading-relaxed">{overview}</p>
            </details>
            
            <details class="group border-t border-slate-100 pt-4">
                <summary class="flex items-center justify-between cursor-pointer list-none">
                    <h2 class="text-xl font-bold text-slate-900 flex items-center gap-2">
                        <span>❤️</span> Temperamento
                    </h2>
                    <svg class="w-5 h-5 text-slate-400 group-open:rotate-180 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                </summary>
                <p class="mt-4 text-slate-600 leading-relaxed">{temperament_text}</p>
            </details>
            
            <details class="group border-t border-slate-100 pt-4">
                <summary class="flex items-center justify-between cursor-pointer list-none">
                    <h2 class="text-xl font-bold text-slate-900 flex items-center gap-2">
                        <span>💓</span> Salud
                    </h2>
                    <svg class="w-5 h-5 text-slate-400 group-open:rotate-180 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                </summary>
                <p class="mt-4 text-slate-600 leading-relaxed">{health_text}</p>
            </details>
            
            <details class="group border-t border-slate-100 pt-4">
                <summary class="flex items-center justify-between cursor-pointer list-none">
                    <h2 class="text-xl font-bold text-slate-900 flex items-center gap-2">
                        <span>🏃</span> Ejercicio
                    </h2>
                    <svg class="w-5 h-5 text-slate-400 group-open:rotate-180 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                </summary>
                <p class="mt-4 text-slate-600 leading-relaxed">{exercise_text}</p>
            </details>
        </section>

        <section class="bg-gradient-to-br from-sky-50 via-violet-50 to-rose-50 rounded-2xl p-6 md:p-8 mb-8">
            <h2 class="text-xl font-bold text-slate-900 mb-6">¿Es Esta Raza Para Ti?</h2>
            <div class="grid md:grid-cols-2 gap-6 mb-6">
                <div class="bg-white rounded-xl p-5 shadow-sm">
                    <h3 class="font-semibold text-green-700 mb-3 flex items-center gap-2">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                        Ideal Para
                    </h3>
                    <ul class="space-y-2 text-slate-600">
                        {best_for_html}
                    </ul>
                </div>
                <div class="bg-white rounded-xl p-5 shadow-sm">
                    <h3 class="font-semibold text-red-700 mb-3 flex items-center gap-2">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                        No Ideal Para
                    </h3>
                    <ul class="space-y-2 text-slate-600">
                        {not_ideal_html}
                    </ul>
                </div>
            </div>
            <div class="bg-white rounded-xl p-5 shadow-sm">
                <h3 class="font-semibold text-slate-900 mb-2">Nuestro Veredicto</h3>
                <p class="text-slate-600">{verdict_text}</p>
            </div>
        </section>
    </main>

    <footer class="bg-slate-900 text-slate-400 py-12">
        <div class="max-w-6xl mx-auto px-4">
            <div class="flex flex-col md:flex-row justify-between items-center gap-4">
                <div class="flex items-center gap-2">
                    <span class="text-2xl">🐕</span>
                    <span class="font-bold text-white">BreedFinder</span>
                </div>
                <div class="flex gap-6 text-sm">
                    <a href="/es/breeds/" class="hover:text-white">Razas</a>
                    <a href="/es/quiz/" class="hover:text-white">Quiz</a>
                    <a href="/es/compare/" class="hover:text-white">Comparar</a>
                    <a href="/about/" class="hover:text-white">Sobre</a>
                </div>
                <p class="text-sm">&copy; 2026 BreedFinder</p>
            </div>
        </div>
    </footer>
</body>
</html>'''
    
    return html

def main():
    script_dir = Path(__file__).parent
    project_dir = script_dir.parent
    data_dir = project_dir / 'data'
    es_breeds_dir = project_dir / 'es' / 'breeds'
    
    es_breeds_dir.mkdir(parents=True, exist_ok=True)
    
    with open(data_dir / 'breeds.json', 'r', encoding='utf-8') as f:
        breeds = json.load(f)
    
    print(f"Generating {len(breeds)} Spanish breed pages...")
    
    for breed in breeds:
        html = generate_breed_html(breed)
        breed_dir = es_breeds_dir / breed['id']
        breed_dir.mkdir(exist_ok=True)
        
        with open(breed_dir / 'index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"  ✓ {breed['name']} → {get_spanish_name(breed['name'])}")
    
    print(f"\n✅ Generated {len(breeds)} Spanish breed pages in /es/breeds/")

if __name__ == '__main__':
    main()
