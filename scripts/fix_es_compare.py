#!/usr/bin/env python3
"""Fix Spanish compare page: images, translations"""

import re

# Spanish translations
ES_TRANSLATIONS = {
    # Sizes
    "Tiny": "Diminuto",
    "Small": "Pequeño", 
    "Medium": "Mediano",
    "Large": "Grande",
    "Giant": "Gigante",
    
    # Shedding
    "Low": "Bajo",
    "Moderate": "Moderado",
    "High": "Alto",
    "Minimal": "Mínimo",
    "Seasonal": "Estacional",
    "Heavy": "Abundante",
    "None": "Ninguno",
}

# Country translations
ES_COUNTRIES = {
    "Germany": "Alemania",
    "Afghanistan": "Afganistán",
    "England": "Inglaterra",
    "Japan": "Japón",
    "United States": "Estados Unidos",
    "France": "Francia",
    "Scotland": "Escocia",
    "Ireland": "Irlanda",
    "China": "China",
    "Russia": "Rusia",
    "Belgium": "Bélgica",
    "Australia": "Australia",
    "Canada": "Canadá",
    "Wales": "Gales",
    "Switzerland": "Suiza",
    "Italy": "Italia",
    "Spain": "España",
    "Portugal": "Portugal",
    "Hungary": "Hungría",
    "Poland": "Polonia",
    "Netherlands": "Países Bajos",
    "Mexico": "México",
    "Cuba": "Cuba",
    "Malta": "Malta",
    "Croatia": "Croacia",
    "Tibet": "Tíbet",
    "Central Africa": "África Central",
    "Congo": "Congo",
    "Turkey": "Turquía",
    "Greece": "Grecia",
    "Norway": "Noruega",
    "Sweden": "Suecia",
    "Finland": "Finlandia",
    "Denmark": "Dinamarca",
    "Iceland": "Islandia",
    "Austria": "Austria",
    "Czech Republic": "República Checa",
    "Unknown": "Desconocido",
    "Ancient": "Antiguo",
}

# Spanish breed names
ES_BREED_NAMES = {
    "Affenpinscher": "Affenpinscher",
    "Afghan Hound": "Lebrel Afgano",
    "Airedale Terrier": "Airedale Terrier",
    "Akita": "Akita",
    "Alaskan Klee Kai": "Alaskan Klee Kai",
    "Alaskan Malamute": "Malamute de Alaska",
    "American Bulldog": "Bulldog Americano",
    "American Bully": "American Bully",
    "American Cocker Spaniel": "Cocker Spaniel Americano",
    "American Eskimo Dog": "Perro Esquimal Americano",
    "American Foxhound": "Foxhound Americano",
    "American Hairless Terrier": "Terrier Americano Sin Pelo",
    "American Pit Bull Terrier": "Pit Bull Terrier Americano",
    "American Staffordshire Terrier": "American Staffordshire Terrier",
    "American Water Spaniel": "Spaniel de Agua Americano",
    "Anatolian Shepherd": "Pastor de Anatolia",
    "Appenzeller Sennenhund": "Boyero de Appenzell",
    "Australian Cattle Dog": "Perro de Ganado Australiano",
    "Australian Kelpie": "Kelpie Australiano",
    "Australian Shepherd": "Pastor Australiano",
    "Australian Terrier": "Terrier Australiano",
    "Azawakh": "Azawakh",
    "Barbet": "Barbet",
    "Basenji": "Basenji",
    "Basset Hound": "Basset Hound",
    "Bavarian Mountain Hound": "Sabueso de Baviera",
    "Beagle": "Beagle",
    "Bearded Collie": "Collie Barbudo",
    "Beauceron": "Beauceron",
    "Bedlington Terrier": "Bedlington Terrier",
    "Belgian Laekenois": "Laekenois Belga",
    "Belgian Malinois": "Malinois Belga",
    "Belgian Sheepdog": "Pastor Belga Groenendael",
    "Belgian Tervuren": "Tervuren Belga",
    "Bergamasco Sheepdog": "Pastor de Bérgamo",
    "Berger Picard": "Pastor de Picardía",
    "Bernese Mountain Dog": "Boyero de Berna",
    "Bichon Frise": "Bichón Frisé",
    "Biewer Terrier": "Biewer Terrier",
    "Black and Tan Coonhound": "Coonhound Negro y Fuego",
    "Black Russian Terrier": "Terrier Ruso Negro",
    "Bloodhound": "Bloodhound",
    "Bluetick Coonhound": "Bluetick Coonhound",
    "Boerboel": "Boerboel",
    "Bolognese": "Boloñés",
    "Border Collie": "Border Collie",
    "Border Terrier": "Border Terrier",
    "Borzoi": "Borzoi",
    "Boston Terrier": "Boston Terrier",
    "Bouvier des Flandres": "Boyero de Flandes",
    "Boxer": "Bóxer",
    "Boykin Spaniel": "Boykin Spaniel",
    "Bracco Italiano": "Braco Italiano",
    "Briard": "Briard",
    "Brittany": "Bretón",
    "Brussels Griffon": "Grifón de Bruselas",
    "Bull Terrier": "Bull Terrier",
    "Bulldog": "Bulldog Inglés",
    "Bullmastiff": "Bullmastiff",
    "Cairn Terrier": "Cairn Terrier",
    "Canaan Dog": "Perro de Canaán",
    "Cane Corso": "Cane Corso",
    "Cardigan Welsh Corgi": "Welsh Corgi Cardigan",
    "Carolina Dog": "Perro de Carolina",
    "Catahoula Leopard Dog": "Perro Leopardo de Catahoula",
    "Cavalier King Charles Spaniel": "Cavalier King Charles Spaniel",
    "Central Asian Shepherd": "Pastor de Asia Central",
    "Cesky Terrier": "Terrier Checo",
    "Chesapeake Bay Retriever": "Retriever de la Bahía de Chesapeake",
    "Chihuahua": "Chihuahua",
    "Chinese Crested": "Crestado Chino",
    "Chinese Shar-Pei": "Shar Pei",
    "Chinook": "Chinook",
    "Chow Chow": "Chow Chow",
    "Cirneco dell Etna": "Cirneco del Etna",
    "Clumber Spaniel": "Clumber Spaniel",
    "Cocker Spaniel": "Cocker Spaniel Inglés",
    "Collie": "Collie",
    "Coton de Tulear": "Coton de Tulear",
    "Curly-Coated Retriever": "Retriever de Pelo Rizado",
    "Dachshund": "Teckel",
    "Dalmatian": "Dálmata",
    "Dandie Dinmont Terrier": "Dandie Dinmont Terrier",
    "Danish-Swedish Farmdog": "Perro de Granja Danés-Sueco",
    "Doberman Pinscher": "Dóberman",
    "Dogo Argentino": "Dogo Argentino",
    "Dogue de Bordeaux": "Dogo de Burdeos",
    "Dutch Shepherd": "Pastor Holandés",
    "English Foxhound": "Foxhound Inglés",
    "English Setter": "Setter Inglés",
    "English Springer Spaniel": "Springer Spaniel Inglés",
    "English Toy Spaniel": "Spaniel Toy Inglés",
    "Entlebucher Mountain Dog": "Boyero de Entlebuch",
    "Eurasier": "Eurasier",
    "Field Spaniel": "Field Spaniel",
    "Finnish Lapphund": "Lapphund Finlandés",
    "Finnish Spitz": "Spitz Finlandés",
    "Flat-Coated Retriever": "Retriever de Pelo Liso",
    "French Bulldog": "Bulldog Francés",
    "German Pinscher": "Pinscher Alemán",
    "German Shepherd": "Pastor Alemán",
    "German Shorthaired Pointer": "Braco Alemán de Pelo Corto",
    "German Spitz": "Spitz Alemán",
    "German Wirehaired Pointer": "Braco Alemán de Pelo Duro",
    "Giant Schnauzer": "Schnauzer Gigante",
    "Glen of Imaal Terrier": "Glen of Imaal Terrier",
    "Golden Retriever": "Golden Retriever",
    "Goldendoodle": "Goldendoodle",
    "Gordon Setter": "Setter Gordon",
    "Great Dane": "Gran Danés",
    "Great Pyrenees": "Gran Pirineo",
    "Greater Swiss Mountain Dog": "Gran Boyero Suizo",
    "Greyhound": "Galgo Inglés",
    "Harrier": "Harrier",
    "Havanese": "Bichón Habanero",
    "Hovawart": "Hovawart",
    "Ibizan Hound": "Podenco Ibicenco",
    "Icelandic Sheepdog": "Perro de Pastor Islandés",
    "Irish Red and White Setter": "Setter Irlandés Rojo y Blanco",
    "Irish Setter": "Setter Irlandés",
    "Irish Terrier": "Terrier Irlandés",
    "Irish Water Spaniel": "Spaniel de Agua Irlandés",
    "Irish Wolfhound": "Lobero Irlandés",
    "Italian Greyhound": "Galgo Italiano",
    "Jack Russell Terrier": "Jack Russell Terrier",
    "Japanese Chin": "Chin Japonés",
    "Japanese Spitz": "Spitz Japonés",
    "Kai Ken": "Kai Ken",
    "Kangal": "Kangal",
    "Karelian Bear Dog": "Perro de Osos de Carelia",
    "Keeshond": "Keeshond",
    "Kerry Blue Terrier": "Kerry Blue Terrier",
    "Kishu Ken": "Kishu Ken",
    "Komondor": "Komondor",
    "Korean Jindo": "Jindo Coreano",
    "Kuvasz": "Kuvasz",
    "Labradoodle": "Labradoodle",
    "Labrador Retriever": "Labrador Retriever",
    "Lagotto Romagnolo": "Lagotto Romagnolo",
    "Lakeland Terrier": "Lakeland Terrier",
    "Lancashire Heeler": "Lancashire Heeler",
    "Leonberger": "Leonberger",
    "Lhasa Apso": "Lhasa Apso",
    "Lowchen": "Löwchen",
    "Maltese": "Maltés",
    "Maltipoo": "Maltipoo",
    "Manchester Terrier": "Manchester Terrier",
    "Maremma Sheepdog": "Pastor de Maremma",
    "Mastiff": "Mastín Inglés",
    "Miniature American Shepherd": "Pastor Americano Miniatura",
    "Miniature Bull Terrier": "Bull Terrier Miniatura",
    "Miniature Pinscher": "Pinscher Miniatura",
    "Miniature Schnauzer": "Schnauzer Miniatura",
    "Mudi": "Mudi",
    "Neapolitan Mastiff": "Mastín Napolitano",
    "Nederlandse Kooikerhondje": "Kooikerhondje",
    "Newfoundland": "Terranova",
    "Norfolk Terrier": "Norfolk Terrier",
    "Norwegian Buhund": "Buhund Noruego",
    "Norwegian Elkhound": "Elkhound Noruego",
    "Norwegian Lundehund": "Lundehund Noruego",
    "Norwich Terrier": "Norwich Terrier",
    "Nova Scotia Duck Tolling Retriever": "Retriever de Nueva Escocia",
    "Old English Sheepdog": "Bobtail",
    "Otterhound": "Otterhound",
    "Papillon": "Papillón",
    "Parson Russell Terrier": "Parson Russell Terrier",
    "Patterdale Terrier": "Patterdale Terrier",
    "Pekingese": "Pequinés",
    "Pembroke Welsh Corgi": "Welsh Corgi Pembroke",
    "Petit Basset Griffon Vendeen": "Petit Basset Griffon Vendéen",
    "Pharaoh Hound": "Perro del Faraón",
    "Plott Hound": "Plott Hound",
    "Pointer": "Pointer Inglés",
    "Polish Lowland Sheepdog": "Pastor Polaco de las Llanuras",
    "Pomeranian": "Pomerania",
    "Pomsky": "Pomsky",
    "Poodle": "Caniche",
    "Portuguese Podengo": "Podengo Portugués",
    "Portuguese Water Dog": "Perro de Agua Portugués",
    "Presa Canario": "Presa Canario",
    "Pug": "Carlino",
    "Puli": "Puli",
    "Pumi": "Pumi",
    "Pyrenean Mastiff": "Mastín del Pirineo",
    "Pyrenean Shepherd": "Pastor de los Pirineos",
    "Rat Terrier": "Rat Terrier",
    "Redbone Coonhound": "Redbone Coonhound",
    "Rhodesian Ridgeback": "Rhodesian Ridgeback",
    "Rottweiler": "Rottweiler",
    "Russian Toy": "Toy Ruso",
    "Saint Bernard": "San Bernardo",
    "Saluki": "Saluki",
    "Samoyed": "Samoyedo",
    "Schipperke": "Schipperke",
    "Scottish Deerhound": "Lebrel Escocés",
    "Scottish Terrier": "Terrier Escocés",
    "Sealyham Terrier": "Sealyham Terrier",
    "Shetland Sheepdog": "Pastor de Shetland",
    "Shiba Inu": "Shiba Inu",
    "Shih Tzu": "Shih Tzu",
    "Shikoku": "Shikoku",
    "Siberian Husky": "Husky Siberiano",
    "Silky Terrier": "Silky Terrier",
    "Skye Terrier": "Skye Terrier",
    "Sloughi": "Sloughi",
    "Slovakian Wirehaired Pointer": "Braco Eslovaco de Pelo Duro",
    "Small Munsterlander": "Münsterländer Pequeño",
    "Smooth Fox Terrier": "Fox Terrier de Pelo Liso",
    "Soft Coated Wheaten Terrier": "Wheaten Terrier de Pelo Suave",
    "Spanish Mastiff": "Mastín Español",
    "Spanish Water Dog": "Perro de Agua Español",
    "Spinone Italiano": "Spinone Italiano",
    "Staffordshire Bull Terrier": "Staffordshire Bull Terrier",
    "Standard Schnauzer": "Schnauzer Estándar",
    "Sussex Spaniel": "Sussex Spaniel",
    "Swedish Lapphund": "Lapphund Sueco",
    "Swedish Vallhund": "Vallhund Sueco",
    "Thai Ridgeback": "Thai Ridgeback",
    "Tibetan Mastiff": "Mastín Tibetano",
    "Tibetan Spaniel": "Spaniel Tibetano",
    "Tibetan Terrier": "Terrier Tibetano",
    "Toy Fox Terrier": "Toy Fox Terrier",
    "Treeing Walker Coonhound": "Treeing Walker Coonhound",
    "Vizsla": "Vizsla",
    "Weimaraner": "Braco de Weimar",
    "Welsh Springer Spaniel": "Welsh Springer Spaniel",
    "Welsh Terrier": "Welsh Terrier",
    "West Highland White Terrier": "West Highland White Terrier",
    "Whippet": "Whippet",
    "Wire Fox Terrier": "Fox Terrier de Pelo Duro",
    "Wirehaired Pointing Griffon": "Grifón de Muestra de Pelo Duro",
    "Wirehaired Vizsla": "Vizsla de Pelo Duro",
    "Xoloitzcuintli": "Xoloitzcuintle",
    "Yorkshire Terrier": "Yorkshire Terrier",
}

def fix_compare_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Fix image paths: ../images/heads/ → ../../images/heads/
    content = content.replace('image: "../images/heads/', 'image: "../../images/heads/')
    
    # 2. Translate breed names
    for en_name, es_name in ES_BREED_NAMES.items():
        content = re.sub(rf'name: "{re.escape(en_name)}"', f'name: "{es_name}"', content)
    
    # 3. Translate sizes
    for en, es in ES_TRANSLATIONS.items():
        if en in ["Tiny", "Small", "Medium", "Large", "Giant"]:
            content = re.sub(rf'size: "{en}"', f'size: "{es}"', content)
        if en in ["Low", "Moderate", "High", "Minimal", "Seasonal", "Heavy", "None"]:
            content = re.sub(rf'shedding: "{en}"', f'shedding: "{es}"', content)
    
    # 4. Translate origins
    for en, es in ES_COUNTRIES.items():
        content = re.sub(rf'origin: "{re.escape(en)}"', f'origin: "{es}"', content)
    
    # 5. Translate "years"
    content = re.sub(r'(\d+-\d+) years', r'\1 años', content)
    
    # 6. Translate row labels
    content = content.replace("['Size', 'size']", "['Tamaño', 'size']")
    content = content.replace("['Height', 'height']", "['Altura', 'height']")
    content = content.replace("['Weight', 'weight']", "['Peso', 'weight']")
    content = content.replace("['Lifespan', 'lifespan']", "['Esperanza de vida', 'lifespan']")
    content = content.replace("['Origin', 'origin']", "['Origen', 'origin']")
    content = content.replace("['Energy', 'energy', true]", "['Energía', 'energy', true]")
    content = content.replace("['Grooming', 'grooming', true]", "['Aseo', 'grooming', true]")
    content = content.replace("['Trainability', 'trainability', true]", "['Adiestrabilidad', 'trainability', true]")
    content = content.replace("['Kid Friendly', 'kidFriendly', true]", "['Niños', 'kidFriendly', true]")
    content = content.replace("['Apartment', 'apartment', true]", "['Apartamento', 'apartment', true]")
    
    # 7. UI translations
    content = content.replace('>Select a breed...</option>', '>Selecciona una raza...</option>')
    content = content.replace('<option value="">Select a breed...', '<option value="">Selecciona una raza...')
    content = content.replace('class="block text-sm font-medium text-slate-600 mb-2">Breed 1</label>', 'class="block text-sm font-medium text-slate-600 mb-2">Raza 1</label>')
    content = content.replace('class="block text-sm font-medium text-slate-600 mb-2">Breed 2</label>', 'class="block text-sm font-medium text-slate-600 mb-2">Raza 2</label>')
    content = content.replace('class="block text-sm font-medium text-slate-600 mb-2">Breed 3 (optional)</label>', 'class="block text-sm font-medium text-slate-600 mb-2">Raza 3 (opcional)</label>')
    content = content.replace('>Select up to 3 breeds to compare side by side<', '>Selecciona hasta 3 razas para comparar<')
    content = content.replace('>Attribute<', '>Atributo<')
    
    # 8. Fix comparison links to English
    content = content.replace('href="comparisons/', 'href="/compare/comparisons/')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed: {filepath}")

if __name__ == "__main__":
    fix_compare_page("/Users/juhaporraskorpi/clawd/breedfinder.org/es/compare/index.html")
