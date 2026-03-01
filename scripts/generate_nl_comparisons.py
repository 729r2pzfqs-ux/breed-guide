#!/usr/bin/env python3
"""Generate Dutch comparison articles with full translations."""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

NL_UI = {
    'all_breeds': 'Alle Rassen',
    'compare': 'Vergelijken',
    'take_quiz': 'Doe de Quiz',
    'comparisons': 'Vergelijkingen',
    'side_by_side': 'Zij aan Zij Vergelijking',
    'attribute': 'Eigenschap',
    'size': 'Grootte',
    'lifespan': 'Levensduur',
    'energy_level': 'Energieniveau',
    'grooming_needs': 'Verzorgingsbehoeften',
    'trainability': 'Trainbaarheid',
    'kid_friendly': 'Kindvriendelijk',
    'apartment': 'Appartement Geschikt',
    'shedding': 'Verharen',
    'more_comparisons': 'Meer Vergelijkingen',
    'back_to_compare': '← Terug naar Vergelijken',
    'view_profile': 'Bekijk volledig profiel →',
    'large': 'Groot',
    'years': 'jaar',
    'very_high': 'Zeer Hoog',
    'high': 'Hoog',
    'moderate': 'Gemiddeld',
    'excellent': 'Uitstekend',
    'not_ideal': 'Niet Ideaal',
    'heavy': 'Veel',
    'helping_find': 'Wij helpen je de perfecte metgezel te vinden.',
    'temperament': 'Temperament',
    'exercise_needs': 'Bewegingsbehoeften',
    'grooming_req': 'Verzorgingsvereisten',
    'which_right': 'Welke is Geschikt voor Jou?',
    'choose_if': 'Kies een {breed} als...',
    'bottom_line': 'Conclusie',
}

NL_TRAITS = {
    'Friendly': 'Vriendelijk', 'Outgoing': 'Sociaal', 'Active': 'Actief', 'Gentle': 'Zachtaardig',
    'Intelligent': 'Intelligent', 'Trusting': 'Vertrouwend', 'Devoted': 'Toegewijd',
    'Reliable': 'Betrouwbaar', 'Trustworthy': 'Betrouwbaar', 'Kind': 'Lief',
    'Playful': 'Speels', 'Adaptable': 'Aanpasbaar', 'Smart': 'Slim',
    'Affectionate': 'Aanhankelijk', 'Patient': 'Geduldig', 'Alert': 'Alert',
    'Bright': 'Slim', 'Amusing': 'Vermakelijk', 'Lively': 'Levendig',
    'Confident': 'Zelfverzekerd', 'Courageous': 'Moedig', 'Loyal': 'Trouw',
    'Versatile': 'Veelzijdig', 'Protective': 'Beschermend', 'Hardworking': 'Hardwerkend',
    'Intense': 'Intens', 'Mischievous': 'Ondeugend', 'Dignified': 'Waardig',
    'Strong': 'Sterk', 'Faithful': 'Trouw', 'Trainable': 'Trainbaar', 'Proud': 'Trots',
}

COMPARISONS = {
    'labrador-vs-golden': {
        'slug': 'labrador-vs-golden-retriever',
        'breed1': 'Labrador Retriever',
        'breed2': 'Golden Retriever',
        'breed1_slug': 'labrador-retriever',
        'breed2_slug': 'golden-retriever',
        'title': 'Labrador Retriever vs Golden Retriever: Volledige Vergelijking',
        'desc': 'Vergelijking Labrador vs Golden Retriever. Bekijk grootte, temperament, bewegingsbehoeften en gezinsgeschiktheid.',
        'intro': 'Twee van de meest geliefde gezinshonden ter wereld. Beide zijn vriendelijk, intelligent en geweldig met kinderen—maar welke past bij jou?',
        'breed1_tagline': 'Populairste Ras ter Wereld',
        'breed2_tagline': 'De Gezinsfavoriet',
        'breed1_desc': 'De Labrador Retriever is het populairste hondenras ter wereld. Ze zijn vriendelijk, sociaal en metgezellen vol energie en liefde.',
        'breed2_desc': 'De Golden Retriever is een van de populairste rassen. Hun vriendelijke en tolerante houding maakt ze fantastische gezinshuisdieren.',
        'breed1_traits': ['Friendly', 'Outgoing', 'Active', 'Gentle', 'Intelligent', 'Trusting'],
        'breed2_traits': ['Intelligent', 'Friendly', 'Devoted', 'Reliable', 'Trustworthy', 'Kind'],
        'breed1_temperament_desc': 'Labradors staan bekend om hun vriendelijkheid en vormen een band met het hele gezin. Ze socialiseren goed met buren en andere honden. Laat je niet misleiden door hun ontspannen persoonlijkheid—ze hebben veel beweging nodig!',
        'breed2_temperament_desc': 'Golden Retrievers zijn sociaal, betrouwbaar en graag bereid te behagen. Ze zijn geweldig met kinderen en andere dieren. Hun geduldige en zachtaardige aard maakt ze uitstekende therapiehonden.',
        'breed1_exercise': 'Hoge energie, heeft dagelijks minstens 1-2 uur actieve beweging nodig. Houdt van zwemmen, apporteren en buitenactiviteiten.',
        'breed2_exercise': 'Hoge energie, maar iets minder intens dan Labradors. Minstens 1 uur beweging per dag. Uitstekend in apporteren, zwemmen en wandelen.',
        'breed1_grooming': 'Wekelijks borstelen, meer tijdens de rui. Korte, dichte vacht is relatief makkelijk te onderhouden, maar verhaart veel.',
        'breed2_grooming': 'Dagelijks borstelen aanbevolen tijdens de rui. Langere vacht heeft meer aandacht nodig om klitten te voorkomen.',
        'breed1_reasons': ['Je wilt het hoogste energieniveau', 'Je geeft de voorkeur aan iets minder verzorging', 'Je wilt een veelzijdige sporthond', 'Je houdt van een sociale, enthousiaste persoonlijkheid', 'Kleurvariatie is belangrijk (zwart, geel, chocolade)'],
        'breed2_reasons': ['Je geeft de voorkeur aan een iets rustiger temperament', 'Je houdt van de vloeiende gouden vacht', 'Je wilt een uitstekende therapie-/hulphond', 'Je waardeert een zachtaardige, geduldige aard', 'Je vindt vaker borstelen niet erg'],
        'bottom_line': 'Beide rassen zijn uitzonderlijke gezinshonden. Labradors zijn iets energieker en makkelijker qua vacht, terwijl Golden Retrievers bekend staan om hun zachte geduld en vloeiende vacht. Welke je ook kiest, je krijgt jaren van liefde en gezelschap!'
    },
    'frenchie-vs-boston': {
        'slug': 'franse-bulldog-vs-boston-terrier',
        'breed1': 'Franse Bulldog',
        'breed2': 'Boston Terriër',
        'breed1_slug': 'french-bulldog',
        'breed2_slug': 'boston-terrier',
        'title': 'Franse Bulldog vs Boston Terriër: Volledige Vergelijking',
        'desc': 'Vergelijking Franse Bulldog vs Boston Terriër. Compacte metgezellen vergeleken.',
        'intro': 'Twee charmante, compacte rassen met grote persoonlijkheden. Beide geweldig voor appartementleven—maar welke past bij jouw levensstijl?',
        'breed1_tagline': 'De Charmante Fransman',
        'breed2_tagline': 'De Amerikaanse Gentleman',
        'breed1_desc': 'De Franse Bulldog is een charmant en aanpasbaar ras met een speelse persoonlijkheid, bekend om zijn vleermuisoren en aanhankelijke aard.',
        'breed2_desc': 'De Boston Terriër, bekend als "De Amerikaanse Gentleman", is een levendige kleine hond met een vriendelijk en vrolijk temperament.',
        'breed1_traits': ['Playful', 'Adaptable', 'Smart', 'Affectionate', 'Patient', 'Alert'],
        'breed2_traits': ['Friendly', 'Bright', 'Amusing', 'Gentle', 'Lively', 'Intelligent'],
        'breed1_temperament_desc': 'Franse Bulldogs zijn ontspannen en aanpasbaar, gedijen zowel in stadsappartementen als landhuizen. Ze zijn speels maar niet hyperactief, waardoor ze uitstekende metgezellen zijn voor verschillende levensstijlen.',
        'breed2_temperament_desc': 'Boston Terriërs zijn levendig, zeer intelligent en hebben een zachtaardige aard. Ze staan bekend om hun smoking-achtige aftekeningen en vriendelijke, vermakelijke persoonlijkheid.',
        'breed1_exercise': 'Matige bewegingsbehoeften—korte wandelingen en speelsessies zijn voldoende. Vermijd overmatige inspanning bij warm weer vanwege de platte snuit.',
        'breed2_exercise': 'Matige energie, heeft dagelijkse wandelingen en speeltijd nodig. Atletischer dan Frenchies, maar ook gevoelig voor oververhitting.',
        'breed1_grooming': 'Minimale verzorging—wekelijks borstelen. Reinig regelmatig de gezichtsplooien om infecties te voorkomen.',
        'breed2_grooming': 'Weinig onderhoud—af en toe borstelen. Hun korte vacht is makkelijk te verzorgen.',
        'breed1_reasons': ['Je wilt een rustigere, ontspannen metgezel', 'Je geeft de voorkeur aan een stevigere bouw', 'Je woont in een appartement', 'Je wilt minimale bewegingseisen', 'Je houdt van de schattige vleermuisoren'],
        'breed2_reasons': ['Je wilt een iets actievere hond', 'Je geeft de voorkeur aan de smokinglook', 'Je wilt een makkelijker trainbare hond', 'Je houdt van een atletischer bouw', 'Je wilt een ras met langere levensduur'],
        'bottom_line': 'Beide zijn uitstekende appartementhonden met grote persoonlijkheden. Frenchies zijn rustiger en ontspannen, terwijl Bostons iets energieker en atletischer zijn. Beide zullen je hart stelen!'
    },
    'gsd-vs-malinois': {
        'slug': 'duitse-herder-vs-mechelse-herder',
        'breed1': 'Duitse Herder',
        'breed2': 'Mechelse Herder',
        'breed1_slug': 'german-shepherd',
        'breed2_slug': 'belgian-malinois',
        'title': 'Duitse Herder vs Mechelse Herder: Volledige Vergelijking',
        'desc': 'Vergelijking Duitse Herder vs Mechelse Herder. Twee uitstekende werkhonden vergeleken.',
        'intro': 'Twee van de meest capabele werkhonden ter wereld. Beide blinken uit in politie- en militair werk—maar hebben belangrijke verschillen.',
        'breed1_tagline': 'De Veelzijdige Beschermer',
        'breed2_tagline': 'Elite Werkhond',
        'breed1_desc': 'De Duitse Herder is veelzijdig, intelligent en een van de populairste werkrassen ter wereld.',
        'breed2_desc': 'De Mechelse Herder is een intense, hoogpresterende werkhond, de voorkeur van politie en leger wereldwijd.',
        'breed1_traits': ['Confident', 'Courageous', 'Smart', 'Loyal', 'Versatile', 'Protective'],
        'breed2_traits': ['Confident', 'Smart', 'Hardworking', 'Alert', 'Intense', 'Protective'],
        'breed1_temperament_desc': 'Duitse Herders zijn zelfverzekerd, moedig en ongelooflijk veelzijdig. Ze vormen diepe banden met het gezin en zijn van nature beschermend zonder agressief te zijn.',
        'breed2_temperament_desc': 'Mechelse Herders zijn intense, gedreven werkhonden met eindeloze energie. Ze hebben een taak nodig en gedijen bij ervaren eigenaren die hun drive kunnen kanaliseren.',
        'breed1_exercise': 'Hoge bewegingsbehoeften—minstens 2 uur per dag. Uitstekend in diverse hondensporten, tracking en gehoorzaamheid.',
        'breed2_exercise': 'Zeer hoge bewegingsbehoeften—2+ uur intense activiteit per dag. Heeft evenveel mentale stimulatie nodig als fysieke beweging.',
        'breed1_grooming': 'Matige verzorging—2-3 keer per week borstelen. Seizoensgebonden zware verharing vereist meer aandacht.',
        'breed2_grooming': 'Makkelijke verzorging—wekelijks borstelen. Kortere vacht dan de Duitse Herder, maar verhaart ook seizoensgebonden.',
        'breed1_reasons': ['Je wilt een veelzijdige gezinsbeschermer', 'Je geeft de voorkeur aan een iets rustigere werkhond', 'Je bent een beginnende eigenaar van een werkras', 'Je wilt een hond die goed is met kinderen', 'Je geeft de voorkeur aan de klassieke look'],
        'breed2_reasons': ['Je wilt maximale drive en intensiteit', 'Je bent een ervaren eigenaar', 'Je wilt een elite sport-/werkhond', 'Je kunt uitgebreide beweging bieden', 'Je wilt een lichtere, snellere hond'],
        'bottom_line': 'Beide zijn uitzonderlijke werkhonden, maar Mechelse Herders zijn intenser en vereisen ervaren eigenaren. Duitse Herders zijn veelzijdiger en meer geschikt voor gezinnen. Kies op basis van je ervaringsniveau en levensstijl.'
    },
    'husky-vs-malamute': {
        'slug': 'husky-vs-malamute',
        'breed1': 'Siberische Husky',
        'breed2': 'Alaskan Malamute',
        'breed1_slug': 'siberian-husky',
        'breed2_slug': 'alaskan-malamute',
        'title': 'Siberische Husky vs Alaskan Malamute: Volledige Vergelijking',
        'desc': 'Vergelijking Husky vs Malamute. Arctische rassen zij aan zij vergeleken.',
        'intro': 'Twee majestueuze arctische rassen met wolfsachtig uiterlijk. Ze lijken op elkaar maar hebben belangrijke verschillen in grootte en temperament.',
        'breed1_tagline': 'De Snelle Sledehond',
        'breed2_tagline': 'De Krachtige Trekker',
        'breed1_desc': 'De Siberische Husky is een atletische, duurzame sledehond, bekend om zijn blauwe ogen en vriendelijke persoonlijkheid.',
        'breed2_desc': 'De Alaskan Malamute is een krachtige, stevige sledehond, gefokt voor kracht en uithoudingsvermogen.',
        'breed1_traits': ['Outgoing', 'Mischievous', 'Loyal', 'Friendly', 'Alert', 'Gentle'],
        'breed2_traits': ['Affectionate', 'Loyal', 'Playful', 'Dignified', 'Devoted', 'Strong'],
        'breed1_temperament_desc': 'Husky\'s zijn vriendelijk, sociaal en soms ondeugend. Het zijn roedelhonden die van gezelschap houden en bekend staan om hun vocale aard en ontsnappingskunsten.',
        'breed2_temperament_desc': 'Malamutes zijn waardiger en minder ondeugend dan Husky\'s. Ze zijn diep trouw, aanhankelijk met het gezin, maar kunnen onafhankelijker zijn.',
        'breed1_exercise': 'Zeer hoge energie—gebouwd om kilometers te rennen. Minstens 2 uur actieve beweging per dag. Houdt van rennen en trekactiviteiten.',
        'breed2_exercise': 'Hoge energie, maar meer uithoudingsvermogen dan snelheid. Lange wandelingen en trekwerk zijn geschikt. Kan oververhitten in warm klimaat.',
        'breed1_grooming': 'Uitgebreide verzorging—meerdere keren per week borstelen. Massieve verharing ("coat blow") tweemaal per jaar.',
        'breed2_grooming': 'Uitgebreide verzorging zoals de Husky. Hun dikkere vacht vereist regelmatig borstelen om klitten te voorkomen.',
        'breed1_reasons': ['Je wilt een middelgroot arctisch ras', 'Je geeft de voorkeur aan een snellere, atletischer hond', 'Je houdt van een praatgrage, vocale metgezel', 'Je wilt indrukwekkende blauwe ogen', 'Je houdt van een speelsere persoonlijkheid'],
        'breed2_reasons': ['Je wilt een grotere, krachtigere hond', 'Je geeft de voorkeur aan een rustiger, waardiger temperament', 'Je hebt ervaring met sterke rassen', 'Je wilt een stillere hond (minder huilen)', 'Je hebt een hond nodig voor trek-/sledewerk'],
        'bottom_line': 'Husky\'s zijn middelgrote atleten die van rennen en "praten" houden. Malamutes zijn krachtige reuzen gebouwd voor kracht. Beide verharen veel en hebben veel beweging nodig. Kies op basis van groottevoorkeuren en gewenst temperament.'
    },
    'poodle-vs-labrador': {
        'slug': 'poedel-vs-labrador',
        'breed1': 'Poedel',
        'breed2': 'Labrador Retriever',
        'breed1_slug': 'poodle',
        'breed2_slug': 'labrador-retriever',
        'title': 'Poedel vs Labrador Retriever: Volledige Vergelijking',
        'desc': 'Vergelijking Poedel vs Labrador. Twee intelligente en populaire rassen vergeleken.',
        'intro': 'Twee van de meest intelligente en populaire hondenrassen. Beide uitstekende gezinshonden met zeer verschillende vachten.',
        'breed1_tagline': 'De Elegante Atleet',
        'breed2_tagline': 'Ieders Beste Vriend',
        'breed1_desc': 'De Poedel is uitzonderlijk intelligent en actief. Achter het elegante uiterlijk schuilt een atletische en zeer slimme hond.',
        'breed2_desc': 'De Labrador Retriever is het populairste ras ter wereld, bekend om zijn vriendelijke en sociale aard.',
        'breed1_traits': ['Intelligent', 'Active', 'Alert', 'Faithful', 'Trainable', 'Proud'],
        'breed2_traits': ['Friendly', 'Active', 'Outgoing', 'Gentle', 'Intelligent', 'Trusting'],
        'breed1_temperament_desc': 'Poedels zijn uitzonderlijk intelligent en graag bereid te behagen. Laat je niet misleiden door de fancy kapsels—het zijn atletische honden gefokt voor jacht en apporteren.',
        'breed2_temperament_desc': 'Labradors zijn de ultieme vriendelijke hond—sociaal met iedereen, geduldig met kinderen en graag bereid te behagen. Ze zijn de ultieme gezinsmetgezel.',
        'breed1_exercise': 'Hoge energie, heeft dagelijkse beweging en mentale stimulatie nodig. Uitstekend in agility, gehoorzaamheid en diverse hondensporten.',
        'breed2_exercise': 'Hoge energie—minstens 1-2 uur per dag. Houdt van zwemmen, apporteren en elke activiteit met hun mensen.',
        'breed1_grooming': 'Hoog onderhoud—professionele verzorging elke 4-6 weken. Dagelijks borstelen voorkomt klitten. Hypoallergene vacht.',
        'breed2_grooming': 'Makkelijke verzorging, maar veel verharing. Wekelijks borstelen, meer tijdens de rui. Niet hypoallergeen.',
        'breed1_reasons': ['Je hebt allergieën (hypoallergeen)', 'Je wilt minimale verharing', 'Je houdt van verzorging of vindt de kosten niet erg', 'Je wilt een elegant uiterlijk', 'Je wilt grootteopties (toy/mini/standaard)'],
        'breed2_reasons': ['Je geeft de voorkeur aan makkelijke, goedkope verzorging', 'Je vindt verharing niet erg', 'Je wilt de klassieke gezinshond', 'Je geeft de voorkeur aan een meer casual uiterlijk', 'Je wilt een retriever die van water houdt'],
        'bottom_line': 'Beide zijn zeer intelligent en makkelijk trainbaar. Poedels bieden een hypoallergene vacht, maar vereisen meer verzorging. Labradors zijn makkelijker te onderhouden, maar verharen veel. Beide zijn uitstekende gezinsmetgezellen!'
    }
}


def generate_article(comp_key, comp):
    ui = NL_UI
    breed1_traits = [NL_TRAITS.get(t, t) for t in comp['breed1_traits']]
    breed2_traits = [NL_TRAITS.get(t, t) for t in comp['breed2_traits']]
    
    breed1_tags = '\n                    '.join([f'<span class="bg-amber-100 text-amber-700 px-3 py-1 rounded-full text-sm font-medium">{t}</span>' for t in breed1_traits])
    breed2_tags = '\n                    '.join([f'<span class="bg-yellow-100 text-yellow-700 px-3 py-1 rounded-full text-sm font-medium">{t}</span>' for t in breed2_traits])
    
    breed1_reasons = '\n                        '.join([f'<li class="flex items-start gap-2"><span class="text-green-400">✓</span><span>{r}</span></li>' for r in comp['breed1_reasons']])
    breed2_reasons = '\n                        '.join([f'<li class="flex items-start gap-2"><span class="text-green-400">✓</span><span>{r}</span></li>' for r in comp['breed2_reasons']])
    
    related = [(k, v) for k, v in COMPARISONS.items() if k != comp_key][:3]
    related_html = '\n'.join([f'<a href="{r[1]["slug"]}.html" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md transition"><span class="font-semibold">{r[1]["breed1"]} vs {r[1]["breed2"]}</span></a>' for r in related])
    
    return f'''<!DOCTYPE html>
<html lang="nl">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-VEERQZ53LZ"></script>
    <script>window.dataLayer = window.dataLayer || []; function gtag(){{dataLayer.push(arguments);}} gtag("js", new Date()); gtag("config", "G-VEERQZ53LZ");</script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{comp['title']} | BreedFinder</title>
    <meta name="description" content="{comp['desc']}">
    <link rel="canonical" href="https://breedfinder.org/nl/compare/comparisons/{comp['slug']}.html">
    <link rel="icon" href="../../../favicon.ico">
    <meta property="og:title" content="{comp['title']}">
    <meta property="og:description" content="{comp['desc']}">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>* {{ font-family: 'Plus Jakarta Sans', sans-serif; }}</style>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"Article","headline":"{comp['title']}","description":"{comp['desc']}","author":{{"@type":"Organization","name":"BreedFinder"}},"publisher":{{"@type":"Organization","name":"BreedFinder","logo":{{"@type":"ImageObject","url":"https://breedfinder.org/logo-192.png"}}}}}}
    </script>
</head>
<body class="bg-gradient-to-br from-sky-50 via-white to-blue-50 min-h-screen text-slate-800">
    <header class="bg-white/80 backdrop-blur-md border-b border-slate-100 sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
            <a href="../../" class="flex items-center gap-3">
                <img src="../../../logo-192.png" class="w-10 h-10" alt="BreedFinder">
                <span class="text-xl font-bold">BreedFinder</span>
            </a>
            <nav class="flex items-center gap-6 text-sm font-medium">
                <a href="/breeds/" class="text-slate-600 hover:text-sky-700">{ui['all_breeds']}</a>
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

        <div class="grid md:grid-cols-2 gap-8 mb-12">
            <div class="bg-white rounded-3xl shadow-xl overflow-hidden">
                <div class="bg-gradient-to-r from-amber-500 to-amber-600 p-6 text-white text-center">
                    <img src="../../../images/heads/{comp['breed1_slug']}.webp" alt="{comp['breed1']}" class="w-32 h-32 rounded-full mx-auto mb-4 object-cover border-4 border-white/30">
                    <h2 class="text-2xl font-bold">{comp['breed1']}</h2>
                    <p class="text-amber-100">{comp['breed1_tagline']}</p>
                </div>
                <div class="p-6">
                    <p class="text-slate-600 mb-4">{comp['breed1_desc']}</p>
                    <a href="/breeds/{comp['breed1_slug']}" class="text-sky-700 font-semibold">{ui['view_profile']}</a>
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
                    <a href="/breeds/{comp['breed2_slug']}" class="text-sky-700 font-semibold">{ui['view_profile']}</a>
                </div>
            </div>
        </div>

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

        <div class="grid md:grid-cols-2 gap-8 mb-12">
            <div class="bg-white rounded-2xl p-6 shadow-lg">
                <h3 class="text-xl font-bold text-amber-600 mb-4">🧠 {comp['breed1']} {ui['temperament']}</h3>
                <div class="flex flex-wrap gap-2 mb-4">
                    {breed1_tags}
                </div>
                <p class="text-slate-600 text-sm">{comp['breed1_temperament_desc']}</p>
            </div>
            <div class="bg-white rounded-2xl p-6 shadow-lg">
                <h3 class="text-xl font-bold text-yellow-600 mb-4">🧠 {comp['breed2']} {ui['temperament']}</h3>
                <div class="flex flex-wrap gap-2 mb-4">
                    {breed2_tags}
                </div>
                <p class="text-slate-600 text-sm">{comp['breed2_temperament_desc']}</p>
            </div>
        </div>

        <div class="grid md:grid-cols-2 gap-8 mb-12">
            <div class="bg-gradient-to-br from-sky-50 to-sky-100 rounded-2xl p-6">
                <h3 class="text-xl font-bold text-sky-700 mb-4">🏃 {ui['exercise_needs']}</h3>
                <div class="space-y-4">
                    <div><span class="font-semibold text-amber-600">{comp['breed1']}:</span><p class="text-slate-600 text-sm">{comp['breed1_exercise']}</p></div>
                    <div><span class="font-semibold text-yellow-600">{comp['breed2']}:</span><p class="text-slate-600 text-sm">{comp['breed2_exercise']}</p></div>
                </div>
            </div>
            <div class="bg-gradient-to-br from-sky-50 to-sky-100 rounded-2xl p-6">
                <h3 class="text-xl font-bold text-sky-700 mb-4">✂️ {ui['grooming_req']}</h3>
                <div class="space-y-4">
                    <div><span class="font-semibold text-amber-600">{comp['breed1']}:</span><p class="text-slate-600 text-sm">{comp['breed1_grooming']}</p></div>
                    <div><span class="font-semibold text-yellow-600">{comp['breed2']}:</span><p class="text-slate-600 text-sm">{comp['breed2_grooming']}</p></div>
                </div>
            </div>
        </div>

        <div class="bg-gradient-to-r from-slate-800 to-slate-700 rounded-3xl p-8 text-white mb-12">
            <h2 class="text-3xl font-bold text-center mb-8">🎯 {ui['which_right']}</h2>
            <div class="grid md:grid-cols-2 gap-8">
                <div class="bg-white/10 rounded-2xl p-6">
                    <h3 class="text-xl font-bold text-amber-400 mb-4">{ui['choose_if'].format(breed=comp['breed1'])}</h3>
                    <ul class="space-y-2 text-slate-200">
                        {breed1_reasons}
                    </ul>
                </div>
                <div class="bg-white/10 rounded-2xl p-6">
                    <h3 class="text-xl font-bold text-yellow-400 mb-4">{ui['choose_if'].format(breed=comp['breed2'])}</h3>
                    <ul class="space-y-2 text-slate-200">
                        {breed2_reasons}
                    </ul>
                </div>
            </div>
            <div class="mt-8 bg-white/5 rounded-xl p-6 text-center">
                <h4 class="text-lg font-semibold text-sky-300 mb-2">{ui['bottom_line']}</h4>
                <p class="text-slate-300">{comp['bottom_line']}</p>
            </div>
        </div>

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


def main():
    output_dir = BASE_DIR / 'nl' / 'compare' / 'comparisons'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for comp_key, comp in COMPARISONS.items():
        html = generate_article(comp_key, comp)
        path = output_dir / f"{comp['slug']}.html"
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ {path.name}")
    
    print(f"\n✅ Generated 5 fully translated Dutch comparison articles")


if __name__ == '__main__':
    main()
