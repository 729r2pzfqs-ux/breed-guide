#!/usr/bin/env python3
"""Fix Finnish compare page: images, translations"""

import re

# Finnish translations
FI_TRANSLATIONS = {
    # Sizes
    "Tiny": "Pikkuruinen",
    "Small": "Pieni", 
    "Medium": "Keskikokoinen",
    "Large": "Suuri",
    "Giant": "Jättiläinen",
    
    # Shedding
    "Low": "Vähäinen",
    "Moderate": "Kohtalainen",
    "High": "Runsas",
    "Minimal": "Minimaalinen",
    "Seasonal": "Kausittainen",
    "Heavy": "Runsas",
    "None": "Ei lainkaan",
    
    # Countries/Origins
    "Germany": "Saksa",
    "Afghanistan": "Afganistan",
    "England": "Englanti",
    "Japan": "Japani",
    "United States": "Yhdysvallat",
    "France": "Ranska",
    "Scotland": "Skotlanti",
    "Ireland": "Irlanti",
    "China": "Kiina",
    "Russia": "Venäjä",
    "Belgium": "Belgia",
    "Australia": "Australia",
    "Canada": "Kanada",
    "Wales": "Wales",
    "Switzerland": "Sveitsi",
    "Italy": "Italia",
    "Spain": "Espanja",
    "Portugal": "Portugali",
    "Hungary": "Unkari",
    "Poland": "Puola",
    "Netherlands": "Alankomaat",
    "Mexico": "Meksiko",
    "Cuba": "Kuuba",
    "Malta": "Malta",
    "Croatia": "Kroatia",
    "Tibet": "Tiibet",
    "Central Africa": "Keski-Afrikka",
    "Congo": "Kongo",
    "Turkey": "Turkki",
    "Greece": "Kreikka",
    "Norway": "Norja",
    "Sweden": "Ruotsi",
    "Finland": "Suomi",
    "Denmark": "Tanska",
    "Iceland": "Islanti",
    "Austria": "Itävalta",
    "Czech Republic": "Tšekki",
    "Slovakia": "Slovakia",
    "Romania": "Romania",
    "Bulgaria": "Bulgaria",
    "Serbia": "Serbia",
    "Slovenia": "Slovenia",
    "Ukraine": "Ukraina",
    "Israel": "Israel",
    "South Africa": "Etelä-Afrikka",
    "Egypt": "Egypti",
    "Morocco": "Marokko",
    "Mali": "Mali",
    "Madagascar": "Madagaskar",
    "Korea": "Korea",
    "Thailand": "Thaimaa",
    "Vietnam": "Vietnam",
    "Philippines": "Filippiinit",
    "Indonesia": "Indonesia",
    "India": "Intia",
    "Pakistan": "Pakistan",
    "Iran": "Iran",
    "Iraq": "Irak",
    "Saudi Arabia": "Saudi-Arabia",
    "Argentina": "Argentiina",
    "Brazil": "Brasilia",
    "Chile": "Chile",
    "Colombia": "Kolumbia",
    "Peru": "Peru",
    "Venezuela": "Venezuela",
    "New Zealand": "Uusi-Seelanti",
    "Unknown": "Tuntematon",
    "Ancient": "Muinainen",
    
    # Row labels
    "Size": "Koko",
    "Height": "Korkeus",
    "Weight": "Paino",
    "Lifespan": "Elinikä",
    "Origin": "Alkuperä",
    "Energy": "Energiataso",
    "Grooming": "Turkinhoito",
    "Trainability": "Koulutettavuus",
    "Kid Friendly": "Lapsiystävällisyys",
    "Apartment": "Asuntosopivuus",
    
    # Years
    "years": "vuotta",
    
    # UI
    "Select a breed...": "Valitse rotu...",
    "Breed 1": "Rotu 1",
    "Breed 2": "Rotu 2",
    "Breed 3 (optional)": "Rotu 3 (valinnainen)",
    "Select up to 3 breeds to compare side by side": "Valitse enintään 3 rotua vertailtavaksi",
    "Attribute": "Ominaisuus",
}

# Finnish breed names
FI_BREED_NAMES = {
    "Affenpinscher": "Affenpinseri",
    "Afghan Hound": "Afgaaninvinttikoira",
    "Airedale Terrier": "Airedalenterrieri",
    "Akita": "Akita",
    "Alaskan Klee Kai": "Alaskan Klee Kai",
    "Alaskan Malamute": "Alaskanmalamuutti",
    "American Bulldog": "Amerikanenbulldoggi",
    "American Bully": "American Bully",
    "American Cocker Spaniel": "Amerikancockerinspanieli",
    "American Eskimo Dog": "Amerikaneskimokoira",
    "American Foxhound": "Amerikanenajokoira",
    "American Hairless Terrier": "Amerikankarvaton terrieri",
    "American Pit Bull Terrier": "Amerikan pitbull terrieri",
    "American Staffordshire Terrier": "Amerikanstaffordshirenterrieri",
    "American Water Spaniel": "Amerikanvesispanieli",
    "Anatolian Shepherd": "Anatolianpaimenkoira",
    "Appenzeller Sennenhund": "Appenzellinsennenhund",
    "Australian Cattle Dog": "Australiankarjakoira",
    "Australian Kelpie": "Australiankelpie",
    "Australian Shepherd": "Australianpaimenkoira",
    "Australian Terrier": "Australianterrieri",
    "Azawakh": "Azawakh",
    "Barbet": "Barbet",
    "Basenji": "Basenji",
    "Basset Hound": "Basset hound",
    "Bavarian Mountain Hound": "Baijerinvuoristovihikoira",
    "Beagle": "Beagle",
    "Bearded Collie": "Partacollie",
    "Beauceron": "Beauceron",
    "Bedlington Terrier": "Bedlingtoninterrieri",
    "Belgian Laekenois": "Belgianpaimenkoira laekenois",
    "Belgian Malinois": "Belgianpaimenkoira malinois",
    "Belgian Sheepdog": "Belgianpaimenkoira groenendael",
    "Belgian Tervuren": "Belgianpaimenkoira tervueren",
    "Bergamasco Sheepdog": "Bergamasconpaimenkoira",
    "Berger Picard": "Picardinpaimenkoira",
    "Bernese Mountain Dog": "Berninpaimenkoira",
    "Bichon Frise": "Bichon frisé",
    "Biewer Terrier": "Biewerinterrieri",
    "Black and Tan Coonhound": "Mustapalokki",
    "Black Russian Terrier": "Mustaterriéri",
    "Bloodhound": "Verijälkikoira",
    "Bluetick Coonhound": "Bluetick coonhound",
    "Boerboel": "Boerboel",
    "Bolognese": "Bolognese",
    "Border Collie": "Bordercollie",
    "Border Terrier": "Borderterrieri",
    "Borzoi": "Borzoi",
    "Boston Terrier": "Bostoninterrieri",
    "Bouvier des Flandres": "Flanderinpaimenkoira",
    "Boxer": "Bokseri",
    "Boykin Spaniel": "Boykinspanieli",
    "Bracco Italiano": "Italianseisoja",
    "Briard": "Briard",
    "Brittany": "Bretoninspanieli",
    "Brussels Griffon": "Brysselingriffoni",
    "Bull Terrier": "Bullterrieri",
    "Bulldog": "Englanninbulldoggi",
    "Bullmastiff": "Bullmastiffi",
    "Cairn Terrier": "Cairnterrieri",
    "Canaan Dog": "Kaanaankoira",
    "Cane Corso": "Cane corso",
    "Cardigan Welsh Corgi": "Cardiganinwelshcorgi",
    "Carolina Dog": "Carolinankoira",
    "Catahoula Leopard Dog": "Catahoulanleopardi",
    "Cavalier King Charles Spaniel": "Cavalier kingcharlesinspanieli",
    "Central Asian Shepherd": "Keskiaasianpaimenkoira",
    "Cesky Terrier": "Tšekinterrieri",
    "Chesapeake Bay Retriever": "Chesapeakenlahden noutaja",
    "Chihuahua": "Chihuahua",
    "Chinese Crested": "Kiinanharjakoira",
    "Chinese Shar-Pei": "Shar pei",
    "Chinook": "Chinook",
    "Chow Chow": "Chow chow",
    "Cirneco dell Etna": "Cirneco dell'Etna",
    "Clumber Spaniel": "Clumberinspanieli",
    "Cocker Spaniel": "Englannincockerinspanieli",
    "Collie": "Collie",
    "Coton de Tulear": "Coton de tuléar",
    "Curly-Coated Retriever": "Kihara noutaja",
    "Dachshund": "Mäyräkoira",
    "Dalmatian": "Dalmatiankoira",
    "Dandie Dinmont Terrier": "Dandie dinmont terrieri",
    "Danish-Swedish Farmdog": "Tanskalais-ruotsalainen pihakoira",
    "Doberman Pinscher": "Dobermanni",
    "Dogo Argentino": "Dogo argentino",
    "Dogue de Bordeaux": "Bordeauxindoggi",
    "Dutch Shepherd": "Hollanninpaimenkoira",
    "English Foxhound": "Englanninajokoira",
    "English Setter": "Englanninsetteri",
    "English Springer Spaniel": "Englannin springerspanieli",
    "English Toy Spaniel": "Englanninleiijispanieli",
    "Entlebucher Mountain Dog": "Entlebuchinsennenhund",
    "Eurasier": "Eurasier",
    "Field Spaniel": "Kenttäspanieli",
    "Finnish Lapphund": "Suomenlapinkoira",
    "Finnish Spitz": "Suomenpystykorva",
    "Flat-Coated Retriever": "Sileäkarvainen noutaja",
    "French Bulldog": "Ranskanbulldoggi",
    "German Pinscher": "Saksanpinseri",
    "German Shepherd": "Saksanpaimenkoira",
    "German Shorthaired Pointer": "Saksanseisoja",
    "German Spitz": "Saksanpystykorva",
    "German Wirehaired Pointer": "Karkeakarvainen saksanseisoja",
    "Giant Schnauzer": "Jättisnautseri",
    "Glen of Imaal Terrier": "Imaalinrotkonterrieri",
    "Golden Retriever": "Kultainennoutaja",
    "Goldendoodle": "Goldendoodle",
    "Gordon Setter": "Gordoninsetteri",
    "Great Dane": "Tanskandoggi",
    "Great Pyrenees": "Pyreneittenkoira",
    "Greater Swiss Mountain Dog": "Suurisveitsinpaimenkoira",
    "Greyhound": "Greyhound",
    "Harrier": "Harrier",
    "Havanese": "Havannankoira",
    "Hovawart": "Hovawart",
    "Ibizan Hound": "Podenco ibicenco",
    "Icelandic Sheepdog": "Islanninlammaskoira",
    "Irish Red and White Setter": "Irlannin puna-valkosetteri",
    "Irish Setter": "Irlanninsetteri",
    "Irish Terrier": "Irlanninterrieri",
    "Irish Water Spaniel": "Irlannin vesispanieli",
    "Irish Wolfhound": "Irlanninsusikoira",
    "Italian Greyhound": "Italianvinttikoira",
    "Jack Russell Terrier": "Jackrussellinterrieri",
    "Japanese Chin": "Japaninhin",
    "Japanese Spitz": "Japaninpystykorva",
    "Kai Ken": "Kai",
    "Kangal": "Kangal",
    "Karelian Bear Dog": "Karjalankarhukoira",
    "Keeshond": "Keeshond",
    "Kerry Blue Terrier": "Kerrynsinterrieri",
    "Kishu Ken": "Kishu",
    "Komondor": "Komondor",
    "Korean Jindo": "Jindokoira",
    "Kuvasz": "Kuvasz",
    "Labradoodle": "Labradoodle",
    "Labrador Retriever": "Labradorinnoutaja",
    "Lagotto Romagnolo": "Lagotto romagnolo",
    "Lakeland Terrier": "Lakelandinterrieri",
    "Lancashire Heeler": "Lancastheeler",
    "Leonberger": "Leonberginkoira",
    "Lhasa Apso": "Lhasa apso",
    "Lowchen": "Löwchen",
    "Maltese": "Maltankoira",
    "Maltipoo": "Maltipoo",
    "Manchester Terrier": "Manchesterinterrieri",
    "Maremma Sheepdog": "Maremmano-abruzzese",
    "Mastiff": "Englanninmastiffi",
    "Miniature American Shepherd": "Amerikanpaimenten miniatyyri",
    "Miniature Bull Terrier": "Miniatyyrenbullterrieri",
    "Miniature Pinscher": "Kääpiöpinseri",
    "Miniature Schnauzer": "Kääpiösnautseri",
    "Mudi": "Mudi",
    "Neapolitan Mastiff": "Napolinmastiffi",
    "Nederlandse Kooikerhondje": "Hollanninankkakoira",
    "Newfoundland": "Newfoundlandinkoira",
    "Norfolk Terrier": "Norfolkinterrieri",
    "Norwegian Buhund": "Norjanbuhund",
    "Norwegian Elkhound": "Norjanharmaaelkhound",
    "Norwegian Lundehund": "Lunni",
    "Norwich Terrier": "Norwichinterrieri",
    "Nova Scotia Duck Tolling Retriever": "Novascotiannoutaja",
    "Old English Sheepdog": "Vanhaenglanninlammaskoira",
    "Otterhound": "Saukkokoira",
    "Papillon": "Papillon",
    "Parson Russell Terrier": "Parsonrussellinterrieri",
    "Patterdale Terrier": "Patterdalenterrieri",
    "Pekingese": "Pekingesinkoira",
    "Pembroke Welsh Corgi": "Pembrokenwelshcorgi",
    "Petit Basset Griffon Vendeen": "Petit basset griffon vendéen",
    "Pharaoh Hound": "Faaraonkoira",
    "Plott Hound": "Plott hound",
    "Pointer": "Englanninseisoja",
    "Polish Lowland Sheepdog": "Puolanponi",
    "Pomeranian": "Pomeranian",
    "Pomsky": "Pomsky",
    "Poodle": "Villakoira",
    "Portuguese Podengo": "Portugalinpodengo",
    "Portuguese Water Dog": "Portugalin vesikoira",
    "Presa Canario": "Presa canario",
    "Pug": "Mopsi",
    "Puli": "Puli",
    "Pumi": "Pumi",
    "Pyrenean Mastiff": "Pyreneittenmastiffi",
    "Pyrenean Shepherd": "Pyreneittenlammaskoira",
    "Rat Terrier": "Rotterrieri",
    "Redbone Coonhound": "Redbone coonhound",
    "Rhodesian Ridgeback": "Rhodesiankoira",
    "Rottweiler": "Rottweiler",
    "Russian Toy": "Venäjäntoy",
    "Saint Bernard": "Bernhardinkoira",
    "Saluki": "Saluki",
    "Samoyed": "Samojedinkoira",
    "Schipperke": "Schipperke",
    "Scottish Deerhound": "Skotlanninpeurankoira",
    "Scottish Terrier": "Skotlanninterrieri",
    "Sealyham Terrier": "Sealyhaminterrieri",
    "Shetland Sheepdog": "Shetlanninlammaskoira",
    "Shiba Inu": "Shiba",
    "Shih Tzu": "Shih tzu",
    "Shikoku": "Shikoku",
    "Siberian Husky": "Siperianhusky",
    "Silky Terrier": "Silkkiterrieri",
    "Skye Terrier": "Skyenterrieri",
    "Sloughi": "Sloughi",
    "Slovakian Wirehaired Pointer": "Slovakiankarkeakarvainen seisoja",
    "Small Munsterlander": "Pikku münsterilänneräre",
    "Smooth Fox Terrier": "Sileäkarvainen kettuterrieri",
    "Soft Coated Wheaten Terrier": "Irlanninterrieri",
    "Spanish Mastiff": "Espanjanmastiffi",
    "Spanish Water Dog": "Espanjanvesikoira",
    "Spinone Italiano": "Spinone italiano",
    "Staffordshire Bull Terrier": "Staffordshirenbullterrieri",
    "Standard Schnauzer": "Keskisnautseri",
    "Sussex Spaniel": "Sussexinspanieli",
    "Swedish Lapphund": "Ruotsinlapinkoira",
    "Swedish Vallhund": "Ruotsinvallhund",
    "Thai Ridgeback": "Thainridgeback",
    "Tibetan Mastiff": "Tiibetinmastiffi",
    "Tibetan Spaniel": "Tiibetinspanieli",
    "Tibetan Terrier": "Tiibetinterrieri",
    "Toy Fox Terrier": "Lelukettuterrieri",
    "Treeing Walker Coonhound": "Treeing walker coonhound",
    "Vizsla": "Unkarin vizsla",
    "Weimaraner": "Weimarinseisoja",
    "Welsh Springer Spaniel": "Welshspringerspanieli",
    "Welsh Terrier": "Welshinterrieri",
    "West Highland White Terrier": "Länsiylämaanterrieri",
    "Whippet": "Whippet",
    "Wire Fox Terrier": "Karkeakarvainen kettuterrieri",
    "Wirehaired Pointing Griffon": "Karkeakarvainen griffon",
    "Wirehaired Vizsla": "Karkeakarvainen unkarin vizsla",
    "Xoloitzcuintli": "Meksikonkarvatonkoira",
    "Yorkshire Terrier": "Yorkshirenterrieri",
}

def fix_compare_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Fix image paths: ../images/heads/ → ../../images/heads/
    content = content.replace('image: "../images/heads/', 'image: "../../images/heads/')
    
    # 2. Translate breed names in the breeds array
    for en_name, fi_name in FI_BREED_NAMES.items():
        # Match: name: "English Name"
        content = re.sub(
            rf'name: "{re.escape(en_name)}"',
            f'name: "{fi_name}"',
            content
        )
    
    # 3. Translate size values
    for en, fi in [("Tiny", "Pikkuruinen"), ("Small", "Pieni"), ("Medium", "Keskikokoinen"), ("Large", "Suuri"), ("Giant", "Jättiläinen")]:
        content = re.sub(rf'size: "{en}"', f'size: "{fi}"', content)
    
    # 4. Translate shedding
    for en, fi in [("Low", "Vähäinen"), ("Moderate", "Kohtalainen"), ("High", "Runsas"), ("Minimal", "Minimaalinen"), ("Seasonal", "Kausittainen"), ("Heavy", "Runsas"), ("None", "Ei lainkaan")]:
        content = re.sub(rf'shedding: "{en}"', f'shedding: "{fi}"', content)
    
    # 5. Translate origins
    for en, fi in FI_TRANSLATIONS.items():
        if en in ["Germany", "Afghanistan", "England", "Japan", "United States", "France", "Scotland", "Ireland", "China", "Russia", "Belgium", "Australia", "Canada", "Wales", "Switzerland", "Italy", "Spain", "Portugal", "Hungary", "Poland", "Netherlands", "Mexico", "Cuba", "Malta", "Croatia", "Tibet", "Central Africa", "Congo", "Turkey", "Greece", "Norway", "Sweden", "Finland", "Denmark", "Iceland", "Austria", "Czech Republic", "Slovakia", "Romania", "Bulgaria", "Serbia", "Slovenia", "Ukraine", "Israel", "South Africa", "Egypt", "Morocco", "Mali", "Madagascar", "Korea", "Thailand", "Vietnam", "Philippines", "Indonesia", "India", "Pakistan", "Iran", "Iraq", "Saudi Arabia", "Argentina", "Brazil", "Chile", "Colombia", "Peru", "Venezuela", "New Zealand", "Unknown", "Ancient"]:
            content = re.sub(rf'origin: "{re.escape(en)}"', f'origin: "{fi}"', content)
    
    # 6. Translate "years" in lifespan
    content = re.sub(r'(\d+-\d+) years', r'\1 vuotta', content)
    
    # 7. Translate row labels in attrs array
    content = content.replace("['Size', 'size']", "['Koko', 'size']")
    content = content.replace("['Height', 'height']", "['Korkeus', 'height']")
    content = content.replace("['Weight', 'weight']", "['Paino', 'weight']")
    content = content.replace("['Lifespan', 'lifespan']", "['Elinikä', 'lifespan']")
    content = content.replace("['Origin', 'origin']", "['Alkuperä', 'origin']")
    content = content.replace("['Energy', 'energy', true]", "['Energiataso', 'energy', true]")
    content = content.replace("['Grooming', 'grooming', true]", "['Turkinhoito', 'grooming', true]")
    content = content.replace("['Trainability', 'trainability', true]", "['Koulutettavuus', 'trainability', true]")
    content = content.replace("['Kid Friendly', 'kidFriendly', true]", "['Lapsiystävällisyys', 'kidFriendly', true]")
    content = content.replace("['Apartment', 'apartment', true]", "['Asuntosopivuus', 'apartment', true]")
    
    # 8. Translate UI labels
    content = content.replace('>Select a breed...</option>', '>Valitse rotu...</option>')
    content = content.replace('<option value="">Select a breed...', '<option value="">Valitse rotu...')
    content = content.replace('class="block text-sm font-medium text-slate-600 mb-2">Breed 1</label>', 'class="block text-sm font-medium text-slate-600 mb-2">Rotu 1</label>')
    content = content.replace('class="block text-sm font-medium text-slate-600 mb-2">Breed 2</label>', 'class="block text-sm font-medium text-slate-600 mb-2">Rotu 2</label>')
    content = content.replace('class="block text-sm font-medium text-slate-600 mb-2">Breed 3 (optional)</label>', 'class="block text-sm font-medium text-slate-600 mb-2">Rotu 3 (valinnainen)</label>')
    content = content.replace('>Select up to 3 breeds to compare side by side<', '>Valitse enintään 3 rotua vertailtavaksi<')
    content = content.replace('>Attribute<', '>Ominaisuus<')
    
    # 9. Fix comparison links to point to English (no Finnish translations yet)
    content = content.replace('href="comparisons/', 'href="/compare/comparisons/')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed: {filepath}")

if __name__ == "__main__":
    fix_compare_page("/Users/juhaporraskorpi/clawd/breedfinder.org/fi/compare/index.html")
