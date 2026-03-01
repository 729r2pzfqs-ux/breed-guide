#!/usr/bin/env python3
"""Generate Swedish comparison articles with full translations."""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

SV_UI = {
    'all_breeds': 'Alla Raser',
    'compare': 'Jämför',
    'take_quiz': 'Gör Quizet',
    'comparisons': 'Jämförelser',
    'side_by_side': 'Jämförelse Sida vid Sida',
    'attribute': 'Egenskap',
    'size': 'Storlek',
    'lifespan': 'Livslängd',
    'energy_level': 'Energinivå',
    'grooming_needs': 'Pälsvårdsbehov',
    'trainability': 'Träningsbarhet',
    'kid_friendly': 'Barnvänlig',
    'apartment': 'Lämplig för Lägenhet',
    'shedding': 'Pälsfällning',
    'more_comparisons': 'Fler Jämförelser',
    'back_to_compare': '← Tillbaka till Jämför',
    'view_profile': 'Se fullständig profil →',
    'large': 'Stor',
    'years': 'år',
    'very_high': 'Mycket Hög',
    'high': 'Hög',
    'moderate': 'Måttlig',
    'excellent': 'Utmärkt',
    'not_ideal': 'Inte Idealt',
    'heavy': 'Mycket',
    'helping_find': 'Vi hjälper dig hitta din perfekta kompis.',
    'temperament': 'Temperament',
    'exercise_needs': 'Motionsbehov',
    'grooming_req': 'Pälsvårdskrav',
    'which_right': 'Vilken Passar Dig?',
    'choose_if': 'Välj {breed} om...',
    'bottom_line': 'Sammanfattning',
}

SV_TRAITS = {
    'Friendly': 'Vänlig', 'Outgoing': 'Utåtriktad', 'Active': 'Aktiv', 'Gentle': 'Mild',
    'Intelligent': 'Intelligent', 'Trusting': 'Tillitsfull', 'Devoted': 'Hängiven',
    'Reliable': 'Pålitlig', 'Trustworthy': 'Trovärdig', 'Kind': 'Snäll',
    'Playful': 'Lekfull', 'Adaptable': 'Anpassningsbar', 'Smart': 'Smart',
    'Affectionate': 'Tillgiven', 'Patient': 'Tålmodig', 'Alert': 'Vaksam',
    'Bright': 'Pigg', 'Amusing': 'Rolig', 'Lively': 'Livlig',
    'Confident': 'Självsäker', 'Courageous': 'Modig', 'Loyal': 'Lojal',
    'Versatile': 'Mångsidig', 'Protective': 'Beskyddande', 'Hardworking': 'Arbetsam',
    'Intense': 'Intensiv', 'Mischievous': 'Busig', 'Dignified': 'Värdig',
    'Strong': 'Stark', 'Faithful': 'Trogen', 'Trainable': 'Lättlärd', 'Proud': 'Stolt',
}

COMPARISONS = {
    'labrador-vs-golden': {
        'slug': 'labrador-vs-golden-retriever',
        'breed1': 'Labrador Retriever',
        'breed2': 'Golden Retriever',
        'breed1_slug': 'labrador-retriever',
        'breed2_slug': 'golden-retriever',
        'title': 'Labrador vs Golden Retriever: Komplett Jämförelse',
        'desc': 'Jämförelse Labrador vs Golden Retriever. Se storlek, temperament, motionsbehov och familjelämplighet.',
        'intro': 'Två av världens mest älskade familjehundar. Båda är vänliga, intelligenta och fantastiska med barn—men vilken passar dig?',
        'breed1_tagline': 'Världens Populäraste Ras',
        'breed2_tagline': 'Familjens Favorit',
        'breed1_desc': 'Labrador Retriever är världens populäraste hundras. De är vänliga, utåtriktade och fulla av energi och kärlek.',
        'breed2_desc': 'Golden Retriever är en av de populäraste raserna. Deras vänliga och toleranta attityd gör dem till fantastiska familjedjur.',
        'breed1_traits': ['Friendly', 'Outgoing', 'Active', 'Gentle', 'Intelligent', 'Trusting'],
        'breed2_traits': ['Intelligent', 'Friendly', 'Devoted', 'Reliable', 'Trustworthy', 'Kind'],
        'breed1_temperament_desc': 'Labradorer är kända för sin vänlighet och knyter an till hela familjen. De umgås bra med grannar och andra hundar. Låt dig inte luras av deras avslappnade personlighet—de behöver mycket motion!',
        'breed2_temperament_desc': 'Golden Retrievers är utåtriktade, pålitliga och ivriga att göra dig glad. De är underbara med barn och andra djur. Deras tålmodiga och milda natur gör dem till utmärkta terapihundar.',
        'breed1_exercise': 'Hög energi, behöver minst 1-2 timmar aktiv motion dagligen. Älskar att simma, apportera och utomhusäventyr.',
        'breed2_exercise': 'Hög energi, men lite mindre intensiv än Labradorer. Minst 1 timme motion dagligen. Utmärkta på apportering, simning och vandring.',
        'breed1_grooming': 'Veckoborsning, mer under pälsfällning. Kort, tät päls är relativt lättskött men fäller mycket.',
        'breed2_grooming': 'Daglig borstning rekommenderas under pälsfällning. Längre päls kräver mer uppmärksamhet för att undvika tovor.',
        'breed1_reasons': ['Du vill ha högsta energinivån', 'Du föredrar lite mindre pälsvård', 'Du vill ha en mångsidig sporthund', 'Du gillar en utåtriktad, entusiastisk personlighet', 'Färgvariation är viktigt (svart, gul, choklad)'],
        'breed2_reasons': ['Du föredrar ett lite lugnare temperament', 'Du älskar den flödande gyllene pälsen', 'Du vill ha en utmärkt terapi-/tjänstehund', 'Du uppskattar en mild, tålmodig natur', 'Du har inget emot tätare borstning'],
        'bottom_line': 'Båda raserna är exceptionella familjehundar. Labradorer är lite mer energiska och lättare att sköta pälsmässigt, medan Golden Retrievers är kända för sitt milda tålamod och flödande päls. Vilket val du än gör får du år av kärlek och sällskap!'
    },
    'frenchie-vs-boston': {
        'slug': 'fransk-bulldog-vs-boston-terrier',
        'breed1': 'Fransk Bulldog',
        'breed2': 'Boston Terrier',
        'breed1_slug': 'french-bulldog',
        'breed2_slug': 'boston-terrier',
        'title': 'Fransk Bulldog vs Boston Terrier: Komplett Jämförelse',
        'desc': 'Jämförelse Fransk Bulldog vs Boston Terrier. Kompakta kompanjoner jämförda.',
        'intro': 'Två charmiga, kompakta raser med stora personligheter. Båda utmärkta för lägenhetsliv—men vilken passar din livsstil?',
        'breed1_tagline': 'Den Charmiga Fransmannen',
        'breed2_tagline': 'Den Amerikanska Gentlemannen',
        'breed1_desc': 'Fransk Bulldog är en charmig och anpassningsbar ras med lekfull personlighet, känd för sina fladdermusöron och tillgivna natur.',
        'breed2_desc': 'Boston Terrier, känd som "Den Amerikanska Gentlemannen", är en livlig liten hund med vänligt och glatt temperament.',
        'breed1_traits': ['Playful', 'Adaptable', 'Smart', 'Affectionate', 'Patient', 'Alert'],
        'breed2_traits': ['Friendly', 'Bright', 'Amusing', 'Gentle', 'Lively', 'Intelligent'],
        'breed1_temperament_desc': 'Franska Bulldogar är avslappnade och anpassningsbara, trivs både i stadslägenheter och på landet. De är lekfulla men inte hyperaktiva, vilket gör dem till utmärkta kompanjoner för olika livsstilar.',
        'breed2_temperament_desc': 'Boston Terriers är livliga, mycket intelligenta och har en mild natur. De är kända för sina smokingliknande markeringar och vänliga, roliga personlighet.',
        'breed1_exercise': 'Måttliga motionsbehov—korta promenader och lekstunder räcker. Undvik överansträngning i varmt väder på grund av platt nos.',
        'breed2_exercise': 'Måttlig energi, behöver dagliga promenader och lek. Mer atletisk än Frenchies men också känslig för överhettning.',
        'breed1_grooming': 'Minimal pälsvård—veckoborstning. Rengör ansiktsveck regelbundet för att förhindra infektioner.',
        'breed2_grooming': 'Lågunderhåll—tillfällig borstning. Deras korta päls är lätt att sköta.',
        'breed1_reasons': ['Du vill ha en lugnare, avslappnad kompanjon', 'Du föredrar en mer robust kroppsbyggnad', 'Du bor i lägenhet', 'Du vill ha minimala motionskrav', 'Du älskar de söta fladdermusöronen'],
        'breed2_reasons': ['Du vill ha en lite mer aktiv hund', 'Du föredrar smokinglooken', 'Du vill ha en lättare tränad hund', 'Du gillar en mer atletisk kroppsbyggnad', 'Du vill ha en ras med längre livslängd'],
        'bottom_line': 'Båda är utmärkta lägenhetshundar med stora personligheter. Frenchies är lugnare och mer avslappnade, medan Bostons är lite mer energiska och atletiska. Båda kommer att stjäla ditt hjärta!'
    },
    'gsd-vs-malinois': {
        'slug': 'schaefer-vs-malinois',
        'breed1': 'Schäfer',
        'breed2': 'Belgisk Malinois',
        'breed1_slug': 'german-shepherd',
        'breed2_slug': 'belgian-malinois',
        'title': 'Schäfer vs Belgisk Malinois: Komplett Jämförelse',
        'desc': 'Jämförelse Schäfer vs Malinois. Två utmärkta arbetshundar jämförda.',
        'intro': 'Två av världens mest kapabla arbetshundar. Båda utmärker sig i polis- och militärarbete—men har viktiga skillnader.',
        'breed1_tagline': 'Den Mångsidiga Beskyddaren',
        'breed2_tagline': 'Elitarbetshund',
        'breed1_desc': 'Schäfern är mångsidig, intelligent och en av de mest populära arbetsraserna i världen.',
        'breed2_desc': 'Belgisk Malinois är en intensiv, högpresterande arbetshund, föredragen av polis och militär världen över.',
        'breed1_traits': ['Confident', 'Courageous', 'Smart', 'Loyal', 'Versatile', 'Protective'],
        'breed2_traits': ['Confident', 'Smart', 'Hardworking', 'Alert', 'Intense', 'Protective'],
        'breed1_temperament_desc': 'Schäfrar är självsäkra, modiga och otroligt mångsidiga. De bildar djupa band med familjen och är naturligt beskyddande utan att vara aggressiva.',
        'breed2_temperament_desc': 'Malinois är intensiva, drivna arbetshundar med oändlig energi. De behöver en uppgift och trivs med erfarna ägare som kan kanalisera deras drivkraft.',
        'breed1_exercise': 'Höga motionsbehov—minst 2 timmar dagligen. Utmärkta i olika hundsporter, spårning och lydnad.',
        'breed2_exercise': 'Mycket höga motionsbehov—2+ timmar intensiv aktivitet dagligen. Behöver mental stimulans lika mycket som fysisk träning.',
        'breed1_grooming': 'Måttlig pälsvård—borsta 2-3 gånger i veckan. Säsongsbunden kraftig fällning kräver mer uppmärksamhet.',
        'breed2_grooming': 'Enkel pälsvård—veckoborstning. Kortare päls än Schäfer men fäller också säsongsvis.',
        'breed1_reasons': ['Du vill ha en mångsidig familjebeskyddare', 'Du föredrar en lite lugnare arbetshund', 'Du är förstagångsägare av arbetsras', 'Du vill ha en hund som är bra med barn', 'Du föredrar den klassiska looken'],
        'breed2_reasons': ['Du vill ha maximal drivkraft och intensitet', 'Du är en erfaren ägare', 'Du vill ha en elit sport-/arbetshund', 'Du kan erbjuda omfattande motion', 'Du vill ha en lättare, snabbare hund'],
        'bottom_line': 'Båda är exceptionella arbetshundar, men Malinois är mer intensiva och kräver erfarna ägare. Schäfrar är mer mångsidiga och bättre lämpade för familjer. Välj baserat på din erfarenhetsnivå och livsstil.'
    },
    'husky-vs-malamute': {
        'slug': 'husky-vs-malamute',
        'breed1': 'Siberian Husky',
        'breed2': 'Alaskan Malamute',
        'breed1_slug': 'siberian-husky',
        'breed2_slug': 'alaskan-malamute',
        'title': 'Siberian Husky vs Alaskan Malamute: Komplett Jämförelse',
        'desc': 'Jämförelse Husky vs Malamute. Arktiska raser jämförda sida vid sida.',
        'intro': 'Två majestätiska arktiska raser med vargliknande utseende. De ser likadana ut men har viktiga skillnader i storlek och temperament.',
        'breed1_tagline': 'Den Snabba Slädhunden',
        'breed2_tagline': 'Den Kraftfulla Dragaren',
        'breed1_desc': 'Siberian Husky är en atletisk, uthållig slädhund, känd för sina blå ögon och vänliga personlighet.',
        'breed2_desc': 'Alaskan Malamute är en kraftfull, robust slädhund, avlad för styrka och uthållighet.',
        'breed1_traits': ['Outgoing', 'Mischievous', 'Loyal', 'Friendly', 'Alert', 'Gentle'],
        'breed2_traits': ['Affectionate', 'Loyal', 'Playful', 'Dignified', 'Devoted', 'Strong'],
        'breed1_temperament_desc': 'Huskies är vänliga, utåtriktade och ibland busiga. De är flockhundar som älskar sällskap och är kända för sin vokala natur och förmåga att rymma.',
        'breed2_temperament_desc': 'Malamutes är mer värdiga och mindre busiga än Huskies. De är djupt lojala, tillgivna med familjen men kan vara mer självständiga.',
        'breed1_exercise': 'Mycket hög energi—byggda för att springa mil. Minst 2 timmar aktiv motion dagligen. Älskar att springa och dragaktiviteter.',
        'breed2_exercise': 'Hög energi, men mer uthållighet än hastighet. Långa vandringar och dragarbete passar bra. Kan överhettas i varmt klimat.',
        'breed1_grooming': 'Omfattande pälsvård—borsta flera gånger i veckan. Massiv fällning ("blåsa päls") två gånger om året.',
        'breed2_grooming': 'Omfattande pälsvård som Husky. Deras tjockare päls kräver regelbunden borstning för att undvika tovor.',
        'breed1_reasons': ['Du vill ha en medelstor arktisk ras', 'Du föredrar en snabbare, mer atletisk hund', 'Du gillar en pratglad, vokal kompanjon', 'Du vill ha imponerande blå ögon', 'Du gillar en mer lekfull personlighet'],
        'breed2_reasons': ['Du vill ha en större, kraftfullare hund', 'Du föredrar ett lugnare, mer värdigt temperament', 'Du har erfarenhet av starka raser', 'Du vill ha en tystare hund (mindre ylande)', 'Du behöver en hund för drag-/slädearbete'],
        'bottom_line': 'Huskies är medelstora atleter som älskar att springa och "prata". Malamutes är kraftfulla jättar byggda för styrka. Båda fäller mycket och behöver massor av motion. Välj baserat på storlekspreferens och önskat temperament.'
    },
    'poodle-vs-labrador': {
        'slug': 'pudel-vs-labrador',
        'breed1': 'Pudel',
        'breed2': 'Labrador Retriever',
        'breed1_slug': 'poodle',
        'breed2_slug': 'labrador-retriever',
        'title': 'Pudel vs Labrador Retriever: Komplett Jämförelse',
        'desc': 'Jämförelse Pudel vs Labrador. Två intelligenta och populära raser jämförda.',
        'intro': 'Två av de mest intelligenta och populära hundraserna. Båda utmärkta familjehundar med väldigt olika pälsar.',
        'breed1_tagline': 'Den Eleganta Atleten',
        'breed2_tagline': 'Allas Bästa Vän',
        'breed1_desc': 'Pudeln är exceptionellt intelligent och aktiv. Bakom det eleganta utseendet finns en atletisk och mycket smart hund.',
        'breed2_desc': 'Labrador Retriever är världens populäraste ras, känd för sin vänliga och utåtriktade natur.',
        'breed1_traits': ['Intelligent', 'Active', 'Alert', 'Faithful', 'Trainable', 'Proud'],
        'breed2_traits': ['Friendly', 'Active', 'Outgoing', 'Gentle', 'Intelligent', 'Trusting'],
        'breed1_temperament_desc': 'Pudlar är exceptionellt intelligenta och ivriga att göra dig glad. Låt dig inte luras av de eleganta frisyrerna—det är atletiska hundar avlade för jakt och apportering.',
        'breed2_temperament_desc': 'Labradorer är den ultimata vänliga hunden—utåtriktade med alla, tålmodiga med barn och ivriga att göra dig glad. De är den ultimata familjekompanjonen.',
        'breed1_exercise': 'Hög energi, behöver daglig motion och mental stimulans. Utmärkta i agility, lydnad och olika hundsporter.',
        'breed2_exercise': 'Hög energi—minst 1-2 timmar dagligen. Älskar att simma, apportera och alla aktiviteter med sina människor.',
        'breed1_grooming': 'Högunderhåll—professionell trimning var 4-6 vecka. Daglig borstning förhindrar tovor. Hypoallergen päls.',
        'breed2_grooming': 'Enkel pälsvård, men mycket fällning. Veckoborstning, mer under fällningssäsong. Inte hypoallergen.',
        'breed1_reasons': ['Du har allergier (hypoallergen)', 'Du vill ha minimal fällning', 'Du gillar trimning eller bryr dig inte om kostnaden', 'Du vill ha ett elegant utseende', 'Du vill ha storleksalternativ (toy/mellan/standard)'],
        'breed2_reasons': ['Du föredrar enkel, billig pälsvård', 'Du bryr dig inte om fällning', 'Du vill ha den klassiska familjehunden', 'Du föredrar ett mer vardagligt utseende', 'Du vill ha en retriever som älskar vatten'],
        'bottom_line': 'Båda är mycket intelligenta och lätta att träna. Pudlar erbjuder hypoallergen päls men kräver mer pälsvård. Labradorer är lättare att underhålla men fäller mycket. Båda är utmärkta familjekompanjoner!'
    }
}


def generate_article(comp_key, comp):
    ui = SV_UI
    breed1_traits = [SV_TRAITS.get(t, t) for t in comp['breed1_traits']]
    breed2_traits = [SV_TRAITS.get(t, t) for t in comp['breed2_traits']]
    
    breed1_tags = '\n                    '.join([f'<span class="bg-amber-100 text-amber-700 px-3 py-1 rounded-full text-sm font-medium">{t}</span>' for t in breed1_traits])
    breed2_tags = '\n                    '.join([f'<span class="bg-yellow-100 text-yellow-700 px-3 py-1 rounded-full text-sm font-medium">{t}</span>' for t in breed2_traits])
    
    breed1_reasons = '\n                        '.join([f'<li class="flex items-start gap-2"><span class="text-green-400">✓</span><span>{r}</span></li>' for r in comp['breed1_reasons']])
    breed2_reasons = '\n                        '.join([f'<li class="flex items-start gap-2"><span class="text-green-400">✓</span><span>{r}</span></li>' for r in comp['breed2_reasons']])
    
    related = [(k, v) for k, v in COMPARISONS.items() if k != comp_key][:3]
    related_html = '\n'.join([f'<a href="{r[1]["slug"]}.html" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md transition"><span class="font-semibold">{r[1]["breed1"]} vs {r[1]["breed2"]}</span></a>' for r in related])
    
    return f'''<!DOCTYPE html>
<html lang="sv">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-VEERQZ53LZ"></script>
    <script>window.dataLayer = window.dataLayer || []; function gtag(){{dataLayer.push(arguments);}} gtag("js", new Date()); gtag("config", "G-VEERQZ53LZ");</script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{comp['title']} | BreedFinder</title>
    <meta name="description" content="{comp['desc']}">
    <link rel="canonical" href="https://breedfinder.org/sv/compare/comparisons/{comp['slug']}.html">
    <link rel="icon" href="../../../favicon.ico">
    <meta property="og:title" content="{comp['title']}">
    <meta property="og:description" content="{comp['desc']}">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>* {{ font-family: 'Plus Jakarta Sans', sans-serif; }}</style>
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
        <nav class="text-sm text-slate-600 mb-8"><a href="../">{ui['compare']}</a> › <a href="./">{ui['comparisons']}</a> › {comp['breed1']} vs {comp['breed2']}</nav>
        <div class="text-center mb-12">
            <h1 class="text-4xl md:text-5xl font-extrabold mb-4"><span class="text-amber-500">{comp['breed1']}</span><span class="text-slate-600 mx-4">vs</span><span class="text-yellow-500">{comp['breed2']}</span></h1>
            <p class="text-lg text-slate-600 max-w-2xl mx-auto">{comp['intro']}</p>
        </div>
        <div class="grid md:grid-cols-2 gap-8 mb-12">
            <div class="bg-white rounded-3xl shadow-xl overflow-hidden">
                <div class="bg-gradient-to-r from-amber-500 to-amber-600 p-6 text-white text-center">
                    <img src="../../../images/heads/{comp['breed1_slug']}.webp" alt="{comp['breed1']}" class="w-32 h-32 rounded-full mx-auto mb-4 object-cover border-4 border-white/30">
                    <h2 class="text-2xl font-bold">{comp['breed1']}</h2>
                    <p class="text-amber-100">{comp['breed1_tagline']}</p>
                </div>
                <div class="p-6"><p class="text-slate-600 mb-4">{comp['breed1_desc']}</p><a href="/breeds/{comp['breed1_slug']}" class="text-sky-700 font-semibold">{ui['view_profile']}</a></div>
            </div>
            <div class="bg-white rounded-3xl shadow-xl overflow-hidden">
                <div class="bg-gradient-to-r from-yellow-500 to-yellow-600 p-6 text-white text-center">
                    <img src="../../../images/heads/{comp['breed2_slug']}.webp" alt="{comp['breed2']}" class="w-32 h-32 rounded-full mx-auto mb-4 object-cover border-4 border-white/30">
                    <h2 class="text-2xl font-bold">{comp['breed2']}</h2>
                    <p class="text-yellow-100">{comp['breed2_tagline']}</p>
                </div>
                <div class="p-6"><p class="text-slate-600 mb-4">{comp['breed2_desc']}</p><a href="/breeds/{comp['breed2_slug']}" class="text-sky-700 font-semibold">{ui['view_profile']}</a></div>
            </div>
        </div>
        <div class="bg-white rounded-3xl shadow-xl overflow-hidden mb-12">
            <div class="bg-slate-800 p-6 text-white"><h2 class="text-2xl font-bold text-center">{ui['side_by_side']}</h2></div>
            <table class="w-full">
                <thead><tr class="bg-slate-50"><th class="p-4 text-left">{ui['attribute']}</th><th class="p-4 text-center text-amber-600">{comp['breed1']}</th><th class="p-4 text-center text-yellow-600">{comp['breed2']}</th></tr></thead>
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
                <div class="flex flex-wrap gap-2 mb-4">{breed1_tags}</div>
                <p class="text-slate-600 text-sm">{comp['breed1_temperament_desc']}</p>
            </div>
            <div class="bg-white rounded-2xl p-6 shadow-lg">
                <h3 class="text-xl font-bold text-yellow-600 mb-4">🧠 {comp['breed2']} {ui['temperament']}</h3>
                <div class="flex flex-wrap gap-2 mb-4">{breed2_tags}</div>
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
                    <ul class="space-y-2 text-slate-200">{breed1_reasons}</ul>
                </div>
                <div class="bg-white/10 rounded-2xl p-6">
                    <h3 class="text-xl font-bold text-yellow-400 mb-4">{ui['choose_if'].format(breed=comp['breed2'])}</h3>
                    <ul class="space-y-2 text-slate-200">{breed2_reasons}</ul>
                </div>
            </div>
            <div class="mt-8 bg-white/5 rounded-xl p-6 text-center">
                <h4 class="text-lg font-semibold text-sky-300 mb-2">{ui['bottom_line']}</h4>
                <p class="text-slate-300">{comp['bottom_line']}</p>
            </div>
        </div>
        <div class="mb-12"><h2 class="text-2xl font-bold mb-6">{ui['more_comparisons']}</h2><div class="grid md:grid-cols-3 gap-4">{related_html}</div></div>
        <div class="text-center"><a href="../" class="text-sky-700 font-semibold">{ui['back_to_compare']}</a></div>
    </main>
    <footer class="border-t border-slate-100 mt-16 py-8"><div class="max-w-6xl mx-auto px-4 text-center text-slate-600 text-sm"><p>© 2026 BreedFinder. {ui['helping_find']}</p></div></footer>
</body>
</html>'''


def main():
    output_dir = BASE_DIR / 'sv' / 'compare' / 'comparisons'
    output_dir.mkdir(parents=True, exist_ok=True)
    for comp_key, comp in COMPARISONS.items():
        html = generate_article(comp_key, comp)
        path = output_dir / f"{comp['slug']}.html"
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ {path.name}")
    print(f"\n✅ Generated 5 fully translated Swedish comparison articles")

if __name__ == '__main__':
    main()
