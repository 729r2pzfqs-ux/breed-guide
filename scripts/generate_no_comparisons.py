#!/usr/bin/env python3
"""Generate Norwegian comparison articles with full translations."""

import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

# Norwegian UI translations
NO_UI = {
    'all_breeds': 'Alle Raser',
    'compare': 'Sammenlign',
    'take_quiz': 'Ta Quizen',
    'comparisons': 'Sammenligninger',
    'side_by_side': 'Side ved Side Sammenligning',
    'attribute': 'Egenskap',
    'size': 'Størrelse',
    'lifespan': 'Levetid',
    'energy_level': 'Energinivå',
    'grooming_needs': 'Stell',
    'trainability': 'Trenbarhet',
    'kid_friendly': 'Barnevennlig',
    'apartment': 'Egnet for Leilighet',
    'shedding': 'Hårfelling',
    'more_comparisons': 'Flere Sammenligninger',
    'back_to_compare': '← Tilbake til Sammenlign',
    'view_profile': 'Se full profil →',
    'large': 'Stor',
    'years': 'år',
    'very_high': 'Veldig Høy',
    'high': 'Høy',
    'moderate': 'Moderat',
    'excellent': 'Utmerket',
    'not_ideal': 'Ikke Ideell',
    'heavy': 'Mye',
    'helping_find': 'Vi hjelper deg finne din perfekte følgesvenn.',
    'temperament': 'Temperament',
    'exercise_needs': 'Mosjonsbehov',
    'grooming_req': 'Stellkrav',
    'which_right': 'Hvilken Passer for Deg?',
    'choose_if': 'Velg en {breed} hvis...',
    'bottom_line': 'Konklusjon',
}

# Norwegian trait translations
NO_TRAITS = {
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
}

# Comparison configurations
COMPARISONS = {
    'labrador-vs-golden': {
        'slug': 'labrador-vs-golden-retriever',
        'breed1': 'Labrador Retriever',
        'breed2': 'Golden Retriever',
        'breed1_slug': 'labrador-retriever',
        'breed2_slug': 'golden-retriever',
        'title': 'Labrador Retriever vs Golden Retriever: Komplett Sammenligning',
        'desc': 'Labrador vs Golden Retriever sammenligning. Se størrelse, temperament, mosjonsbehov og familievennlighet.',
        'intro': 'To av verdens mest elskede familiehunder. Begge er vennlige, intelligente og flotte med barn—men hvilken passer for deg?',
        'breed1_tagline': 'Verdens #1 Rase',
        'breed2_tagline': 'Familiens Favoritt',
        'breed1_desc': 'Labrador Retrieveren er verdens mest populære hunderase. De er vennlige, utadvendte og livlige følgesvenner.',
        'breed2_desc': 'Golden Retrieveren er en av de mest populære hunderasene. Deres vennlige, tolerante holdning gjør dem til fantastiske familiedyr.',
        'breed1_traits': ['Friendly', 'Outgoing', 'Active', 'Gentle', 'Intelligent', 'Trusting'],
        'breed2_traits': ['Intelligent', 'Friendly', 'Devoted', 'Reliable', 'Trustworthy', 'Kind'],
        'breed1_temperament_desc': 'Labradorer er kjent for å være vennlige og knytter sterke bånd med hele familien. De sosialiserer godt med naboer, hunder og mennesker. Ikke la deres avslappede personlighet lure deg—de trenger mye mosjon!',
        'breed2_temperament_desc': 'Golden Retrievere er utadvendte, troverdige og ivrige etter å behage. De er fantastiske med barn og andre kjæledyr. Deres tålmodige, milde natur gjør dem til utmerkede terapihunder.',
        'breed1_exercise': 'Høy energi som krever minst 1-2 timer med aktiv daglig mosjon. De elsker å svømme, hente og være med på utendørs eventyr.',
        'breed2_exercise': 'Høy energi, men litt mindre intens enn Labradorer. Minst 1 time daglig mosjon. De utmerker seg i henting, svømming og fotturer.',
        'breed1_grooming': 'Ukentlig børsting, mer under fellesesongen. Kort, tett pels er relativt lettstelt, men feller mye.',
        'breed2_grooming': 'Daglig børsting anbefales under fellesesongen. Lengre pels trenger mer oppmerksomhet for å forhindre floker.',
        'breed1_reasons': ['Du vil ha det høyeste energinivået', 'Du foretrekker litt mindre stell', 'Du vil ha en allsidig sportshund', 'Du elsker en utadvendt, entusiastisk personlighet', 'Fargevariasjon er viktig (svart, gul, sjokolade)'],
        'breed2_reasons': ['Du foretrekker et litt roligere temperament', 'Du elsker den flytende gylne pelsen', 'Du vil ha en utmerket terapi-/tjenestehund', 'Du setter pris på en mild, tålmodig holdning', 'Du har ikke noe imot hyppigere børsting'],
        'bottom_line': 'Begge rasene er eksepsjonelle familiehunder. Labradorer er litt mer energiske og lettere å stelle pelsmessig, mens Golden Retrievere er kjent for sin milde tålmodighet og flytende pels. Uansett valg vil du få år med kjærlighet og vennskap!'
    },
    'frenchie-vs-boston': {
        'slug': 'fransk-bulldog-vs-boston-terrier',
        'breed1': 'Fransk Bulldog',
        'breed2': 'Boston Terrier',
        'breed1_slug': 'french-bulldog',
        'breed2_slug': 'boston-terrier',
        'title': 'Fransk Bulldog vs Boston Terrier: Komplett Sammenligning',
        'desc': 'Fransk Bulldog vs Boston Terrier sammenligning. Kompakte følgesvenner sammenlignet.',
        'intro': 'To sjarmerende, kompakte raser med store personligheter. Begge flotte for leilighetslivet—men hvilken passer din livsstil?',
        'breed1_tagline': 'Den Sjarmerende Franskmann',
        'breed2_tagline': 'Den Amerikanske Gentleman',
        'breed1_desc': 'Fransk Bulldog er en sjarmerende, tilpasningsdyktig rase med en leken personlighet, kjent for sine flaggermusører.',
        'breed2_desc': 'Boston Terrier, kjent som "Den Amerikanske Gentleman", er en livlig liten hund med et vennlig temperament.',
        'breed1_traits': ['Playful', 'Adaptable', 'Smart', 'Affectionate', 'Patient', 'Alert'],
        'breed2_traits': ['Friendly', 'Bright', 'Amusing', 'Gentle', 'Lively', 'Intelligent'],
        'breed1_temperament_desc': 'Franske Bulldoger er avslappede og tilpasningsdyktige, trives i byleiligheter eller på landet. De er lekne, men ikke hyperaktive, noe som gjør dem til utmerkede følgesvenner for ulike livsstiler.',
        'breed2_temperament_desc': 'Boston Terriere er livlige, svært intelligente og har et mildt temperament. De er kjent for sitt smoking-lignende mønster og vennlige, morsomme personlighet.',
        'breed1_exercise': 'Moderate mosjonsbehov—korte turer og lekeøkter er nok. Unngå overanstrengelse i varmt vær på grunn av deres flate ansikt.',
        'breed2_exercise': 'Moderat energi som krever daglige turer og lek. Mer atletisk enn Frenchier, men fortsatt utsatt for overoppheting.',
        'breed1_grooming': 'Minimalt stell—ukentlig børsting. Rengjør ansiktsrynkene regelmessig for å forhindre infeksjoner.',
        'breed2_grooming': 'Lite vedlikehold—sporadisk børsting. Deres korte pels er lett å stelle.',
        'breed1_reasons': ['Du vil ha en roligere, mer avslappet følgesvenn', 'Du foretrekker en kraftigere kroppsbygning', 'Du bor i leilighet', 'Du vil ha minimale mosjonskrav', 'Du elsker de søte flaggermusørene'],
        'breed2_reasons': ['Du vil ha en litt mer aktiv hund', 'Du foretrekker smoking-looken', 'Du vil ha en hund som er lettere å trene', 'Du liker en mer atletisk kroppsbygning', 'Du vil ha en rase som lever lenger'],
        'bottom_line': 'Begge er utmerkede leilighetshunder med store personligheter. Frenchier er roligere og mer avslappede, mens Bostoner er litt mer energiske og atletiske. Begge vil stjele hjertet ditt!'
    },
    'gsd-vs-malinois': {
        'slug': 'schaefer-vs-malinois',
        'breed1': 'Schæferhund',
        'breed2': 'Belgisk Malinois',
        'breed1_slug': 'german-shepherd',
        'breed2_slug': 'belgian-malinois',
        'title': 'Schæferhund vs Belgisk Malinois: Komplett Sammenligning',
        'desc': 'Schæferhund vs Malinois sammenligning. To utmerkede brukshunder sammenlignet.',
        'intro': 'To av verdens mest kapable brukshunder. Begge utmerker seg i politi- og militærarbeid—men har viktige forskjeller.',
        'breed1_tagline': 'Den Allsidige Beskytter',
        'breed2_tagline': 'Elite Brukshund',
        'breed1_desc': 'Schæferhunden er allsidig, intelligent og en av verdens mest populære brukshunderaser.',
        'breed2_desc': 'Belgisk Malinois er en intens, høytytende brukshund foretrukket av politi og militær verden over.',
        'breed1_traits': ['Confident', 'Courageous', 'Smart', 'Loyal', 'Versatile', 'Protective'],
        'breed2_traits': ['Confident', 'Smart', 'Hardworking', 'Alert', 'Intense', 'Protective'],
        'breed1_temperament_desc': 'Schæferhunder er selvsikre, modige og utrolig allsidige. De knytter sterke bånd med familien og er naturlig beskyttende uten å være aggressive.',
        'breed2_temperament_desc': 'Malinoiser er intense, drevne arbeidshunder med endeløs energi. De trenger en oppgave og trives med erfarne eiere som kan kanalisere deres driv.',
        'breed1_exercise': 'Høye mosjonsbehov—minst 2 timer daglig. De utmerker seg i ulike hundesporter, sporing og lydighetstrening.',
        'breed2_exercise': 'Svært høye mosjonsbehov—2+ timer med intens aktivitet daglig. De trenger mental stimulering like mye som fysisk trening.',
        'breed1_grooming': 'Moderat stell—børst 2-3 ganger ukentlig. Kraftig sesongfelling krever mer oppmerksomhet.',
        'breed2_grooming': 'Enkelt stell—ukentlig børsting. Kortere pels enn Schæfer, men feller fortsatt sesongmessig.',
        'breed1_reasons': ['Du vil ha en allsidig familiebeskytter', 'Du foretrekker en litt roligere arbeidshund', 'Du er førstegangseier av arbeidsrase', 'Du vil ha en hund som er god med barn', 'Du foretrekker det klassiske utseendet'],
        'breed2_reasons': ['Du vil ha maksimal driv og intensitet', 'Du er en erfaren hundeeier', 'Du vil ha en topp sports-/arbeidshund', 'Du kan gi omfattende mosjon', 'Du vil ha en lettere, raskere hund'],
        'bottom_line': 'Begge er eksepsjonelle arbeidshunder, men Malinoiser er mer intense og krever erfarne eiere. Schæferhunder er mer allsidige og passer bedre for familier. Velg basert på erfaringsnivå og livsstil.'
    },
    'husky-vs-malamute': {
        'slug': 'husky-vs-malamute',
        'breed1': 'Siberian Husky',
        'breed2': 'Alaskan Malamute',
        'breed1_slug': 'siberian-husky',
        'breed2_slug': 'alaskan-malamute',
        'title': 'Siberian Husky vs Alaskan Malamute: Komplett Sammenligning',
        'desc': 'Husky vs Malamute sammenligning. Arktiske raser sammenlignet.',
        'intro': 'To majestetiske arktiske raser med ulvelignende utseende. De ligner hverandre men har viktige forskjeller i størrelse og temperament.',
        'breed1_tagline': 'Den Raske Sledehunden',
        'breed2_tagline': 'Den Kraftfulle Trekkeren',
        'breed1_desc': 'Siberian Husky er en atletisk, utholdende sledehund kjent for sine blå øyne og vennlige personlighet.',
        'breed2_desc': 'Alaskan Malamute er en kraftfull, tungt bygd sledehund avlet for styrke og utholdenhet.',
        'breed1_traits': ['Outgoing', 'Mischievous', 'Loyal', 'Friendly', 'Alert', 'Gentle'],
        'breed2_traits': ['Affectionate', 'Loyal', 'Playful', 'Dignified', 'Devoted', 'Strong'],
        'breed1_temperament_desc': 'Huskyer er vennlige, utadvendte og noen ganger skøyeraktige. De er flokkdyr som elsker selskap og er kjent for sin vokale natur og rømningskunster.',
        'breed2_temperament_desc': 'Malamuter er mer verdige og mindre skøyeraktige enn Huskyer. De er dypt lojale, kjærlige med familien, men kan være mer uavhengige.',
        'breed1_exercise': 'Svært høy energi—designet for å løpe milevis. Minst 2 timer med aktiv mosjon daglig. De elsker løping og trekkaktiviteter.',
        'breed2_exercise': 'Høy energi, men med mer utholdenhet enn fart. Lange fotturer og trekkarbeid passer dem godt. De kan overopphetes i varmt klima.',
        'breed1_grooming': 'Omfattende stell—børst flere ganger ukentlig. Massiv sesongfelling ("blåser pelsen") to ganger årlig.',
        'breed2_grooming': 'Omfattende stell, likt som Husky. Deres tykkere pels krever regelmessig børsting for å forhindre floker.',
        'breed1_reasons': ['Du vil ha en mellomstor arktisk rase', 'Du foretrekker en raskere, mer atletisk hund', 'Du liker en pratsom, vokal følgesvenn', 'Du vil ha slående blå øyne', 'Du liker en mer leken personlighet'],
        'breed2_reasons': ['Du vil ha en større, kraftigere hund', 'Du foretrekker et roligere, mer verdig temperament', 'Du har erfaring med sterke raser', 'Du vil ha en stillere hund (mindre hyling)', 'Du trenger en hund for trekking/kjøring'],
        'bottom_line': 'Huskyer er mellomstore atleter som elsker å løpe og prate. Malamuter er kraftige giganter bygget for styrke. Begge feller mye og trenger masse mosjon. Velg basert på størrelsespreferanse og ønsket temperament.'
    },
    'poodle-vs-labrador': {
        'slug': 'puddel-vs-labrador',
        'breed1': 'Puddel',
        'breed2': 'Labrador Retriever',
        'breed1_slug': 'poodle',
        'breed2_slug': 'labrador-retriever',
        'title': 'Puddel vs Labrador Retriever: Komplett Sammenligning',
        'desc': 'Puddel vs Labrador sammenligning. To intelligente, populære raser sammenlignet.',
        'intro': 'To av de mest intelligente og populære hunderasene. Begge utmerkede familiehunder med svært forskjellige pelser.',
        'breed1_tagline': 'Den Elegante Atleten',
        'breed2_tagline': 'Alles Beste Venn',
        'breed1_desc': 'Puddelen er eksepsjonelt intelligent og aktiv. Bak det elegante utseendet skjuler det seg en atletisk, smart hund.',
        'breed2_desc': 'Labrador Retriever er verdens mest populære hunderase, kjent for sin vennlige, utadvendte natur.',
        'breed1_traits': ['Intelligent', 'Active', 'Alert', 'Faithful', 'Trainable', 'Proud'],
        'breed2_traits': ['Friendly', 'Active', 'Outgoing', 'Gentle', 'Intelligent', 'Trusting'],
        'breed1_temperament_desc': 'Puddeler er eksepsjonelt intelligente og ivrige etter å behage. Ikke la de fancy klippene lure deg—de er atletiske hunder avlet for jakt og apportering.',
        'breed2_temperament_desc': 'Labradorer er den ultimate vennlige hunden—utadvendt med alle, tålmodig med barn og ivrig etter å behage. De er den ultimate familiefølgesvennen.',
        'breed1_exercise': 'Høy energi som krever daglig mosjon og mental stimulering. De utmerker seg i agility, lydighet og ulike hundesporter.',
        'breed2_exercise': 'Høy energi—minst 1-2 timer daglig. De elsker å svømme, hente og alle aktiviteter med menneskene sine.',
        'breed1_grooming': 'Høyt vedlikehold—profesjonelt stell hver 4-6. uke. Daglig børsting forhindrer floker. Hypoallergen pels.',
        'breed2_grooming': 'Enkelt stell, men mye felling. Ukentlig børsting, mer under fellesesongen. Ikke hypoallergen.',
        'breed1_reasons': ['Du har allergier (hypoallergen)', 'Du vil ha minimal felling', 'Du liker stell eller har ikke noe imot kostnaden', 'Du vil ha et elegant utseende', 'Du vil ha størrelsesvalg (toy/mini/standard)'],
        'breed2_reasons': ['Du foretrekker enkelt, rimelig stell', 'Du har ikke noe imot felling', 'Du vil ha den klassiske familiehunden', 'Du foretrekker et mer avslappet utseende', 'Du vil ha en vannelskende retriever'],
        'bottom_line': 'Begge er svært intelligente og lette å trene. Puddeler tilbyr hypoallergen pels, men trenger mer stell. Labradorer er lettere å vedlikeholde, men feller mye. Begge er fremragende familiefølgesvenner!'
    }
}


def generate_article(comp_key, comp):
    """Generate a single Norwegian comparison article."""
    ui = NO_UI
    
    # Translate traits
    breed1_traits = [NO_TRAITS.get(t, t) for t in comp['breed1_traits']]
    breed2_traits = [NO_TRAITS.get(t, t) for t in comp['breed2_traits']]
    
    # Build trait tags
    breed1_tags = '\n                    '.join([f'<span class="bg-amber-100 text-amber-700 px-3 py-1 rounded-full text-sm font-medium">{t}</span>' for t in breed1_traits])
    breed2_tags = '\n                    '.join([f'<span class="bg-yellow-100 text-yellow-700 px-3 py-1 rounded-full text-sm font-medium">{t}</span>' for t in breed2_traits])
    
    # Build reason lists
    breed1_reasons = '\n                        '.join([f'<li class="flex items-start gap-2"><span class="text-green-400">✓</span><span>{r}</span></li>' for r in comp['breed1_reasons']])
    breed2_reasons = '\n                        '.join([f'<li class="flex items-start gap-2"><span class="text-green-400">✓</span><span>{r}</span></li>' for r in comp['breed2_reasons']])
    
    # Get related comparisons
    related = [(k, v) for k, v in COMPARISONS.items() if k != comp_key][:3]
    related_html = '\n'.join([f'<a href="{r[1]["slug"]}.html" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md transition"><span class="font-semibold">{r[1]["breed1"]} vs {r[1]["breed2"]}</span></a>' for r in related])
    
    return f'''<!DOCTYPE html>
<html lang="no">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-VEERQZ53LZ"></script>
    <script>window.dataLayer = window.dataLayer || []; function gtag(){{dataLayer.push(arguments);}} gtag("js", new Date()); gtag("config", "G-VEERQZ53LZ");</script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{comp['title']} | BreedFinder</title>
    <meta name="description" content="{comp['desc']}">
    <link rel="canonical" href="https://breedfinder.org/no/compare/comparisons/{comp['slug']}.html">
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

        <!-- Exercise & Grooming -->
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

        <!-- Verdict Section -->
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


def main():
    output_dir = BASE_DIR / 'no' / 'compare' / 'comparisons'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for comp_key, comp in COMPARISONS.items():
        html = generate_article(comp_key, comp)
        path = output_dir / f"{comp['slug']}.html"
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ {path.name}")
    
    print(f"\n✅ Generated 5 fully translated Norwegian comparison articles")


if __name__ == '__main__':
    main()
