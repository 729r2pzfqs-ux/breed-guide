#!/usr/bin/env python3
"""Generate Danish comparison articles with full translations."""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

DA_UI = {
    'all_breeds': 'Alle Racer',
    'compare': 'Sammenlign',
    'take_quiz': 'Tag Quiz',
    'comparisons': 'Sammenligninger',
    'side_by_side': 'Side om Side Sammenligning',
    'attribute': 'Egenskab',
    'size': 'Størrelse',
    'lifespan': 'Levetid',
    'energy_level': 'Energiniveau',
    'grooming_needs': 'Plejebehov',
    'trainability': 'Trænbarhed',
    'kid_friendly': 'Børnevenlig',
    'apartment': 'Egnet til Lejlighed',
    'shedding': 'Fældning',
    'more_comparisons': 'Flere Sammenligninger',
    'back_to_compare': '← Tilbage til Sammenlign',
    'view_profile': 'Se fuld profil →',
    'large': 'Stor',
    'years': 'år',
    'very_high': 'Meget Høj',
    'high': 'Høj',
    'moderate': 'Moderat',
    'excellent': 'Fremragende',
    'not_ideal': 'Ikke Ideel',
    'heavy': 'Kraftig',
    'helping_find': 'Vi hjælper dig med at finde din perfekte følgesvend.',
    'temperament': 'Temperament',
    'exercise_needs': 'Motionsbehov',
    'grooming_req': 'Plejekrav',
    'which_right': 'Hvilken er den Rette for Dig?',
    'choose_if': 'Vælg en {breed} hvis...',
    'bottom_line': 'Konklusion',
}

DA_TRAITS = {
    'Friendly': 'Venlig', 'Outgoing': 'Udadvendt', 'Active': 'Aktiv', 'Gentle': 'Blid',
    'Intelligent': 'Intelligent', 'Trusting': 'Tillidsfuld', 'Devoted': 'Hengiven',
    'Reliable': 'Pålidelig', 'Trustworthy': 'Troværdig', 'Kind': 'Venlig',
    'Playful': 'Legesyg', 'Adaptable': 'Tilpasningsdygtig', 'Smart': 'Klog',
    'Affectionate': 'Kærlig', 'Patient': 'Tålmodig', 'Alert': 'Opmærksom',
    'Bright': 'Kvik', 'Amusing': 'Underholdende', 'Lively': 'Livlig',
    'Confident': 'Selvsikker', 'Courageous': 'Modig', 'Loyal': 'Loyal',
    'Versatile': 'Alsidig', 'Protective': 'Beskyttende', 'Hardworking': 'Hårdtarbejdende',
    'Intense': 'Intens', 'Mischievous': 'Drillesyg', 'Dignified': 'Værdig',
    'Strong': 'Stærk', 'Faithful': 'Trofast', 'Trainable': 'Lærenem', 'Proud': 'Stolt',
}

COMPARISONS = {
    'labrador-vs-golden': {
        'slug': 'labrador-vs-golden-retriever',
        'breed1': 'Labrador Retriever',
        'breed2': 'Golden Retriever',
        'breed1_slug': 'labrador-retriever',
        'breed2_slug': 'golden-retriever',
        'title': 'Labrador Retriever vs Golden Retriever: Komplet Sammenligning',
        'desc': 'Labrador vs Golden Retriever sammenligning. Se størrelse, temperament, motionsbehov og familievenlighed side om side.',
        'intro': 'To af verdens mest elskede familiehunde. Begge er venlige, intelligente og fantastiske med børn—men hvilken er den rette for dig?',
        'breed1_tagline': 'Verdens #1 Race',
        'breed2_tagline': 'Familiens Favorit',
        'breed1_desc': 'Labrador Retrieveren er verdens mest populære hunderace. De er venlige, udadvendte og livlige følgesvende med masser af kærlighed.',
        'breed2_desc': 'Golden Retrieveren er en af de mest populære hunderacer. Deres venlige, tolerante attitude gør dem til fantastiske familiekæledyr.',
        'breed1_traits': ['Friendly', 'Outgoing', 'Active', 'Gentle', 'Intelligent', 'Trusting'],
        'breed2_traits': ['Intelligent', 'Friendly', 'Devoted', 'Reliable', 'Trustworthy', 'Kind'],
        'breed1_temperament_desc': 'Labradorer er berømte for deres venlighed og knytter bånd med hele familien. De socialiserer godt med naboer og andre hunde. Lad dig ikke narre af deres afslappede personlighed—de har brug for masser af motion!',
        'breed2_temperament_desc': 'Golden Retrievere er udadvendte, troværdige og ivrige efter at behage. De er vidunderlige med børn og andre kæledyr. Deres tålmodige, blide natur gør dem til fremragende terapihunde.',
        'breed1_exercise': 'Høj energi, der kræver mindst 1-2 timers aktiv daglig motion. De elsker at svømme, apportere og udendørs eventyr.',
        'breed2_exercise': 'Høj energi, men lidt mindre intens end Labradorer. Mindst 1 times daglig motion. De udmærker sig i apportering, svømning og vandreture.',
        'breed1_grooming': 'Ugentlig børstning, mere i fældningssæsonen. Kort, tæt pels er relativt let at pleje, men fælder meget.',
        'breed2_grooming': 'Daglig børstning anbefales i fældningssæsonen. Længere pels kræver mere opmærksomhed for at forhindre filtring.',
        'breed1_reasons': ['Du vil have det højeste energiniveau', 'Du foretrækker lidt mindre pleje', 'Du vil have en alsidig sportshund', 'Du elsker en udadvendt, entusiastisk personlighed', 'Farvevariation er vigtig (sort, gul, chokolade)'],
        'breed2_reasons': ['Du foretrækker et lidt roligere temperament', 'Du elsker den flydende gyldne pels', 'Du vil have en fremragende terapi-/servicehund', 'Du sætter pris på en blid, tålmodig holdning', 'Du har ikke noget imod hyppigere børstning'],
        'bottom_line': 'Begge racer er enestående familiehunde. Labradorer er lidt mere energiske og nemmere at pleje pelsmæssigt, mens Golden Retrievere er kendt for deres blide tålmodighed og flydende pels. Uanset valget får du år med kærlighed og venskab!'
    },
    'frenchie-vs-boston': {
        'slug': 'fransk-bulldog-vs-boston-terrier',
        'breed1': 'Fransk Bulldog',
        'breed2': 'Boston Terrier',
        'breed1_slug': 'french-bulldog',
        'breed2_slug': 'boston-terrier',
        'title': 'Fransk Bulldog vs Boston Terrier: Komplet Sammenligning',
        'desc': 'Fransk Bulldog vs Boston Terrier sammenligning. Kompakte følgesvende sammenlignet.',
        'intro': 'To charmerende, kompakte racer med store personligheder. Begge er fantastiske til lejlighedsliv—men hvilken passer til din livsstil?',
        'breed1_tagline': 'Den Charmerende Franskmand',
        'breed2_tagline': 'Den Amerikanske Gentleman',
        'breed1_desc': 'Fransk Bulldog er en charmerende, tilpasningsdygtig race med en legesyg personlighed, kendt for sine flagermusører.',
        'breed2_desc': 'Boston Terrieren, kendt som "Den Amerikanske Gentleman", er en livlig lille hund med et venligt temperament.',
        'breed1_traits': ['Playful', 'Adaptable', 'Smart', 'Affectionate', 'Patient', 'Alert'],
        'breed2_traits': ['Friendly', 'Bright', 'Amusing', 'Gentle', 'Lively', 'Intelligent'],
        'breed1_temperament_desc': 'Franske Bulldogs er afslappede og tilpasningsdygtige, trives i bylejligheder eller på landet. De er legesyge, men ikke hyperaktive, hvilket gør dem til fremragende følgesvende for forskellige livsstile.',
        'breed2_temperament_desc': 'Boston Terriere er livlige, meget intelligente og har et mildt temperament. De er kendt for deres smoking-lignende aftegninger og venlige, underholdende personlighed.',
        'breed1_exercise': 'Moderate motionsbehov—korte gåture og legesessioner er nok. Undgå overanstrengelse i varmt vejr på grund af deres flade ansigt.',
        'breed2_exercise': 'Moderat energi, der kræver daglige gåture og leg. Mere atletisk end Frenchies, men stadig tilbøjelig til overophedning.',
        'breed1_grooming': 'Minimal pleje—ugentlig børstning. Rengør ansigtsrynkerne regelmæssigt for at forhindre infektioner.',
        'breed2_grooming': 'Lav vedligeholdelse—lejlighedsvis børstning. Deres korte pels er let at pleje.',
        'breed1_reasons': ['Du vil have en roligere, mere afslappet følgesvend', 'Du foretrækker en kraftigere kropsbygning', 'Du bor i lejlighed', 'Du vil have minimale motionskrav', 'Du elsker de søde flagermusører'],
        'breed2_reasons': ['Du vil have en lidt mere aktiv hund', 'Du foretrækker smoking-looket', 'Du vil have en hund, der er nemmere at træne', 'Du kan lide en mere atletisk kropsbygning', 'Du vil have en race, der lever længere'],
        'bottom_line': 'Begge er fremragende lejlighedshunde med store personligheder. Frenchies er roligere og mere afslappede, mens Bostons er lidt mere energiske og atletiske. Begge vil stjæle dit hjerte!'
    },
    'gsd-vs-malinois': {
        'slug': 'schaefer-vs-malinois',
        'breed1': 'Schæferhund',
        'breed2': 'Belgisk Malinois',
        'breed1_slug': 'german-shepherd',
        'breed2_slug': 'belgian-malinois',
        'title': 'Schæferhund vs Belgisk Malinois: Komplet Sammenligning',
        'desc': 'Schæferhund vs Malinois sammenligning. To fremragende arbejdshunde sammenlignet.',
        'intro': 'To af verdens mest kapable arbejdshunde. Begge udmærker sig i politi- og militærarbejde—men har vigtige forskelle.',
        'breed1_tagline': 'Den Alsidige Beskytter',
        'breed2_tagline': 'Elite Arbejdshund',
        'breed1_desc': 'Schæferhunden er alsidig, intelligent og en af de mest populære arbejdshunderacer i verden.',
        'breed2_desc': 'Belgisk Malinois er en intens, højtydende arbejdshund foretrukket af politi og militær verden over.',
        'breed1_traits': ['Confident', 'Courageous', 'Smart', 'Loyal', 'Versatile', 'Protective'],
        'breed2_traits': ['Confident', 'Smart', 'Hardworking', 'Alert', 'Intense', 'Protective'],
        'breed1_temperament_desc': 'Schæferhunde er selvsikre, modige og utroligt alsidige. De knytter dybe bånd med familien og er naturligt beskyttende uden at være aggressive.',
        'breed2_temperament_desc': 'Malinois er intense, drevne arbejdshunde med uendelig energi. De har brug for en opgave og trives med erfarne ejere, der kan kanalisere deres drivkraft.',
        'breed1_exercise': 'Høje motionsbehov—mindst 2 timer dagligt. De udmærker sig i forskellige hundesportsgrene, sporing og lydighedstræning.',
        'breed2_exercise': 'Meget høje motionsbehov—2+ timer med intens aktivitet dagligt. De har brug for mental stimulation lige så meget som fysisk træning.',
        'breed1_grooming': 'Moderat pleje—børst 2-3 gange ugentligt. Kraftig sæsonfældning kræver mere opmærksomhed.',
        'breed2_grooming': 'Let pleje—ugentlig børstning. Kortere pels end Schæfer, men fælder stadig sæsonmæssigt.',
        'breed1_reasons': ['Du vil have en alsidig familiebeskytter', 'Du foretrækker en lidt roligere arbejdshund', 'Du er førstegangsejer af arbejdsrace', 'Du vil have en hund, der er god med børn', 'Du foretrækker det klassiske look'],
        'breed2_reasons': ['Du vil have maksimal drivkraft og intensitet', 'Du er en erfaren hundeejer', 'Du vil have en top sports-/arbejdshund', 'Du kan give omfattende motion', 'Du vil have en lettere, hurtigere hund'],
        'bottom_line': 'Begge er enestående arbejdshunde, men Malinois er mere intense og kræver erfarne ejere. Schæferhunde er mere alsidige og passer bedre til familier. Vælg baseret på erfaringsniveau og livsstil.'
    },
    'husky-vs-malamute': {
        'slug': 'husky-vs-malamute',
        'breed1': 'Siberian Husky',
        'breed2': 'Alaskan Malamute',
        'breed1_slug': 'siberian-husky',
        'breed2_slug': 'alaskan-malamute',
        'title': 'Siberian Husky vs Alaskan Malamute: Komplet Sammenligning',
        'desc': 'Husky vs Malamute sammenligning. Arktiske racer sammenlignet side om side.',
        'intro': 'To majestætiske arktiske racer med ulvelignende udseende. De ligner hinanden, men har vigtige forskelle i størrelse og temperament.',
        'breed1_tagline': 'Den Hurtige Slædehund',
        'breed2_tagline': 'Den Kraftfulde Trækker',
        'breed1_desc': 'Siberian Husky er en atletisk, udholdende slædehund kendt for sine blå øjne og venlige personlighed.',
        'breed2_desc': 'Alaskan Malamute er en kraftfuld, tungtbygget slædehund avlet til styrke og udholdenhed.',
        'breed1_traits': ['Outgoing', 'Mischievous', 'Loyal', 'Friendly', 'Alert', 'Gentle'],
        'breed2_traits': ['Affectionate', 'Loyal', 'Playful', 'Dignified', 'Devoted', 'Strong'],
        'breed1_temperament_desc': 'Huskyer er venlige, udadvendte og til tider drillesyge. De er flokdyr, der elsker selskab og er kendt for deres vokale natur og flugtkunster.',
        'breed2_temperament_desc': 'Malamuter er mere værdige og mindre drillesyge end Huskyer. De er dybt loyale, kærlige med familien, men kan være mere uafhængige.',
        'breed1_exercise': 'Meget høj energi—designet til at løbe kilometervis. Mindst 2 timer med aktiv motion dagligt. De elsker at løbe og trækaktiviteter.',
        'breed2_exercise': 'Høj energi, men med mere udholdenhed end fart. Lange vandreture og trækarbejde passer dem godt. De kan blive overophedede i varmt klima.',
        'breed1_grooming': 'Omfattende pleje—børst flere gange ugentligt. Massiv sæsonfældning ("blæser pelsen") to gange årligt.',
        'breed2_grooming': 'Omfattende pleje ligesom Husky. Deres tykkere pels kræver regelmæssig børstning for at forhindre filtring.',
        'breed1_reasons': ['Du vil have en mellemstor arktisk race', 'Du foretrækker en hurtigere, mere atletisk hund', 'Du kan lide en snakkesalig, vokal følgesvend', 'Du vil have slående blå øjne', 'Du kan lide en mere legesyg personlighed'],
        'breed2_reasons': ['Du vil have en større, kraftigere hund', 'Du foretrækker et roligere, mere værdigt temperament', 'Du har erfaring med stærke racer', 'Du vil have en mere stille hund (mindre hylen)', 'Du har brug for en hund til trækning/kørsel'],
        'bottom_line': 'Huskyer er mellemstore atleter, der elsker at løbe og snakke. Malamuter er kraftfulde giganter bygget til styrke. Begge fælder meget og har brug for masser af motion. Vælg baseret på størrelsesprference og ønsket temperament.'
    },
    'poodle-vs-labrador': {
        'slug': 'puddel-vs-labrador',
        'breed1': 'Puddel',
        'breed2': 'Labrador Retriever',
        'breed1_slug': 'poodle',
        'breed2_slug': 'labrador-retriever',
        'title': 'Puddel vs Labrador Retriever: Komplet Sammenligning',
        'desc': 'Puddel vs Labrador sammenligning. To intelligente, populære racer sammenlignet.',
        'intro': 'To af de mest intelligente og populære hunderacer. Begge er fremragende familiehunde med meget forskellige pelse.',
        'breed1_tagline': 'Den Elegante Atlet',
        'breed2_tagline': 'Alles Bedste Ven',
        'breed1_desc': 'Puddelen er exceptionelt intelligent og aktiv. Bag det elegante ydre gemmer sig en atletisk, ivrig og klog hund.',
        'breed2_desc': 'Labrador Retrieveren er verdens mest populære hunderace, kendt for sin venlige, udadvendte natur.',
        'breed1_traits': ['Intelligent', 'Active', 'Alert', 'Faithful', 'Trainable', 'Proud'],
        'breed2_traits': ['Friendly', 'Active', 'Outgoing', 'Gentle', 'Intelligent', 'Trusting'],
        'breed1_temperament_desc': 'Puddeler er exceptionelt intelligente og ivrige efter at behage. Lad dig ikke narre af de fancy klipninger—de er atletiske hunde avlet til jagt og apportering.',
        'breed2_temperament_desc': 'Labradorer er den ultimative venlige hund—udadvendte med alle, tålmodige med børn og ivrige efter at behage. De er den ultimative familiefølgesvend.',
        'breed1_exercise': 'Høj energi, der kræver daglig motion og mental stimulation. De udmærker sig i agility, lydighed og forskellige hundesportsgrene.',
        'breed2_exercise': 'Høj energi—mindst 1-2 timer dagligt. De elsker at svømme, apportere og alle aktiviteter med deres mennesker.',
        'breed1_grooming': 'Høj vedligeholdelse—professionel pleje hver 4-6. uge. Daglig børstning forhindrer filtring. Hypoallergen pels.',
        'breed2_grooming': 'Let pleje, men megen fældning. Ugentlig børstning, mere i fældningssæsonen. Ikke hypoallergen.',
        'breed1_reasons': ['Du har allergier (hypoallergen)', 'Du vil have minimal fældning', 'Du kan lide pleje eller har ikke noget imod omkostningen', 'Du vil have et elegant udseende', 'Du vil have størrelsesmuligheder (toy/mini/standard)'],
        'breed2_reasons': ['Du foretrækker let, billig pleje', 'Du har ikke noget imod fældning', 'Du vil have den klassiske familiehund', 'Du foretrækker et mere afslappet look', 'Du vil have en vandelskende retriever'],
        'bottom_line': 'Begge er meget intelligente og nemme at træne. Puddeler tilbyder hypoallergen pels, men kræver mere pleje. Labradorer er nemmere at vedligeholde, men fælder meget. Begge er fremragende familiefølgesvende!'
    }
}


def generate_article(comp_key, comp):
    ui = DA_UI
    breed1_traits = [DA_TRAITS.get(t, t) for t in comp['breed1_traits']]
    breed2_traits = [DA_TRAITS.get(t, t) for t in comp['breed2_traits']]
    
    breed1_tags = '\n                    '.join([f'<span class="bg-amber-100 text-amber-700 px-3 py-1 rounded-full text-sm font-medium">{t}</span>' for t in breed1_traits])
    breed2_tags = '\n                    '.join([f'<span class="bg-yellow-100 text-yellow-700 px-3 py-1 rounded-full text-sm font-medium">{t}</span>' for t in breed2_traits])
    
    breed1_reasons = '\n                        '.join([f'<li class="flex items-start gap-2"><span class="text-green-400">✓</span><span>{r}</span></li>' for r in comp['breed1_reasons']])
    breed2_reasons = '\n                        '.join([f'<li class="flex items-start gap-2"><span class="text-green-400">✓</span><span>{r}</span></li>' for r in comp['breed2_reasons']])
    
    related = [(k, v) for k, v in COMPARISONS.items() if k != comp_key][:3]
    related_html = '\n'.join([f'<a href="{r[1]["slug"]}.html" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md transition"><span class="font-semibold">{r[1]["breed1"]} vs {r[1]["breed2"]}</span></a>' for r in related])
    
    return f'''<!DOCTYPE html>
<html lang="da">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-VEERQZ53LZ"></script>
    <script>window.dataLayer = window.dataLayer || []; function gtag(){{dataLayer.push(arguments);}} gtag("js", new Date()); gtag("config", "G-VEERQZ53LZ");</script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{comp['title']} | BreedFinder</title>
    <meta name="description" content="{comp['desc']}">
    <link rel="canonical" href="https://breedfinder.org/da/compare/comparisons/{comp['slug']}.html">
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
    output_dir = BASE_DIR / 'da' / 'compare' / 'comparisons'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for comp_key, comp in COMPARISONS.items():
        html = generate_article(comp_key, comp)
        path = output_dir / f"{comp['slug']}.html"
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ {path.name}")
    
    print(f"\n✅ Generated 5 fully translated Danish comparison articles")


if __name__ == '__main__':
    main()
