#!/usr/bin/env python3
"""
Generate translated article pages for all 14 languages
"""

import json
from pathlib import Path

LANGUAGES = ['es', 'de', 'fr', 'it', 'pt', 'nl', 'pl', 'zh', 'ja', 'fi', 'sv', 'no', 'da', 'ru']

# Article translations
ARTICLES = {
    'apartments': {
        'en': {
            'slug': 'best-dogs-for-apartments',
            'badge': 'GUIDE',
            'badge_color': 'sky',
            'title': '15 Best Dog Breeds for Apartments',
            'meta_title': '15 Best Dog Breeds for Apartments (2026)',
            'meta_desc': 'Looking for apartment-friendly dogs? These 15 breeds thrive in small spaces.',
            'subtitle': "Think you need a house with a yard to own a dog? Think again. These breeds thrive in cozy spaces.",
            'intro': "Living in an apartment doesn't mean you can't have a dog. In fact, some breeds are <em>better</em> suited to apartment life than suburban homes. The key factors aren't just size—they're <strong>energy level, barking tendency, and adaptability</strong>.",
            'tip_box': '<strong>Surprising fact:</strong> Some large breeds like Greyhounds make excellent apartment dogs, while some small breeds like Jack Russell Terriers need tons of space to burn energy.',
            'sections': [
                {'emoji': '🏆', 'title': 'Top 5 Apartment Dogs', 'breeds': [
                    ('French Bulldog', 'french-bulldog', 'The ultimate apartment companion. Frenchies are quiet, don\'t need much exercise, and love lounging on the couch.'),
                    ('Cavalier King Charles Spaniel', 'cavalier-king-charles-spaniel', 'Gentle, quiet, and happy to curl up in your lap. Cavaliers are adaptable and naturally quiet dogs.'),
                    ('Bichon Frise', 'bichon-frise', 'Small, cheerful, and hypoallergenic. Bichons don\'t shed much and are known for being quiet.'),
                    ('Pug', 'pug', 'Pugs were literally bred to be lap dogs. They\'re low-energy, love being close to their owners.'),
                    ('Boston Terrier', 'boston-terrier', 'The "American Gentleman" is compact, quiet, and adaptable with moderate energy levels.'),
                ]},
                {'emoji': '🐕', 'title': 'Medium-Sized Apartment Dogs', 'breeds': [
                    ('Basset Hound', 'basset-hound', 'Don\'t let their size fool you—Basset Hounds are couch potatoes. Calm, low-energy, and happy with a daily walk.'),
                    ('English Bulldog', 'bulldog', 'Bulldogs are calm, dignified, and require minimal exercise. They prefer air-conditioned apartments.'),
                    ('Shiba Inu', 'shiba-inu', 'Clean, quiet, and cat-like in their independence. Shibas groom themselves and rarely bark.'),
                ]},
                {'emoji': '🦴', 'title': 'Surprisingly Good: Large Apartment Dogs', 'breeds': [
                    ('Greyhound', 'greyhound', 'Yes, really! Retired racing Greyhounds are calm, quiet, and sleep up to 18 hours a day.'),
                    ('Great Dane', 'great-dane', 'Known as "gentle giants," Great Danes are surprisingly low-energy and calm indoors.'),
                ]},
            ],
            'quiet_title': '🔇 Quietest Breeds for Apartments',
            'quiet_intro': 'Noise complaints are a real concern for apartment dwellers. These breeds rarely bark:',
            'quiet_breeds': ['Basenji – The "barkless dog"', 'Whippet – Quiet and low-maintenance', 'Italian Greyhound – Gentle and silent', 'Cavalier King Charles Spaniel – Naturally quiet', 'Bulldog – More snores than barks'],
            'avoid_title': '⚠️ Breeds to Avoid in Apartments',
            'avoid_intro': 'Some breeds struggle in apartments due to high energy, barking, or space needs:',
            'avoid_breeds': ['Border Collie – Needs constant mental stimulation', 'Husky – High energy, loves to howl', 'Beagle – Notorious barkers and howlers', 'Jack Russell Terrier – Endless energy', 'Australian Shepherd – Needs a job to do'],
            'tips_title': 'Tips for Apartment Dog Owners',
            'tips': ['Exercise matters more than space – A tired dog is a happy apartment dog', 'Mental stimulation – Puzzle toys prevent boredom', 'Potty training – Consider pee pads or a balcony grass patch', 'Noise training – Teach "quiet" commands early', 'Check building rules – Some have breed or size restrictions'],
            'cta_title': 'Find Your Match',
            'cta_text': 'Not sure which apartment breed is right for you? Take our quiz to find breeds that match your lifestyle.',
            'back': '← Back',
            'quiz_btn': 'Take the Breed Quiz →',
            'compare_btn': 'Compare Breeds',
            'footer': '© 2026 BreedFinder. Made with care for dog lovers everywhere.',
        },
        'fi': {
            'slug': 'parhaat-kerrostalokoirat',
            'badge': 'OPAS',
            'badge_color': 'sky',
            'title': '15 Parasta Koirarotua Kerrostaloon',
            'meta_title': '15 Parasta Koirarotua Kerrostaloon (2026)',
            'meta_desc': 'Etsitkö kerrostaloon sopivaa koiraa? Nämä 15 rotua viihtyvät pienissä tiloissa.',
            'subtitle': 'Luuletko, että tarvitset talon ja pihan koiran omistamiseen? Mieti uudelleen. Nämä rodut viihtyvät kodikkaissa tiloissa.',
            'intro': 'Kerrostalossa asuminen ei tarkoita, ettet voisi omistaa koiraa. Itse asiassa jotkut rodut sopivat <em>paremmin</em> kerrostaloelämään kuin omakotitaloihin. Tärkeimmät tekijät eivät ole vain koko—vaan <strong>energiataso, haukkumisalttius ja sopeutuvuus</strong>.',
            'tip_box': '<strong>Yllättävä fakta:</strong> Jotkut suuret rodut kuten Vinttikoirat ovat erinomaisia kerrostalokoiria, kun taas pienet rodut kuten Jack Russell Terrierit tarvitsevat paljon tilaa energian purkamiseen.',
            'sections': [
                {'emoji': '🏆', 'title': 'Top 5 Kerrostalokoiraa', 'breeds': [
                    ('Ranskanbulldoggi', 'french-bulldog', 'Täydellinen kerrostalokumppani. Frenchiet ovat hiljaisia, eivät tarvitse paljon liikuntaa ja rakastavat sohvalla löhöilyä.'),
                    ('Cavalier King Charles Spanieli', 'cavalier-king-charles-spaniel', 'Lempeä, hiljainen ja onnellinen sylissäsi. Cavalierit ovat sopeutuvia ja luonnostaan hiljaisia.'),
                    ('Bichon Frise', 'bichon-frise', 'Pieni, iloinen ja allergikoille sopiva. Bichonit eivät karista paljon ja ovat tunnettuja hiljaisuudestaan.'),
                    ('Mopsi', 'pug', 'Mopsit on kirjaimellisesti jalostettu sylikoiriksi. Ne ovat vähäenergisiä ja rakastavat olla lähellä omistajaansa.'),
                    ('Bostoninterrieri', 'boston-terrier', '"Amerikkalainen herrasmies" on kompakti, hiljainen ja sopeutuva kohtuullisella energiatasolla.'),
                ]},
                {'emoji': '🐕', 'title': 'Keskikokoiset Kerrostalokoirat', 'breeds': [
                    ('Basset Hound', 'basset-hound', 'Älä anna koon hämätä—Basset Houndit ovat sohvaperunoita. Rauhallisia, vähäenergisiä ja tyytyväisiä päivittäiseen lenkkiin.'),
                    ('Englanninbulldoggi', 'bulldog', 'Bulldogit ovat rauhallisia, arvokkaita ja vaativat minimaalista liikuntaa. Ne suosivat ilmastoituja asuntoja.'),
                    ('Shiba Inu', 'shiba-inu', 'Siistejä, hiljaisia ja kissanomaisesti itsenäisiä. Shibat hoitavat itsensä ja haukkuvat harvoin.'),
                ]},
                {'emoji': '🦴', 'title': 'Yllättävästi Hyviä: Suuret Kerrostalokoirat', 'breeds': [
                    ('Vinttikoira', 'greyhound', 'Kyllä, todella! Eläkkeellä olevat kilpavinttikoirat ovat rauhallisia, hiljaisia ja nukkuvat jopa 18 tuntia päivässä.'),
                    ('Tanskandoggi', 'great-dane', 'Tunnetaan "lempeinä jättiläisinä", Tanskandogit ovat yllättävän vähäenergisiä ja rauhallisia sisällä.'),
                ]},
            ],
            'quiet_title': '🔇 Hiljaisimmat Rodut Kerrostaloihin',
            'quiet_intro': 'Meluvalitukset ovat todellinen huoli kerrostaloasukkaille. Nämä rodut haukkuvat harvoin:',
            'quiet_breeds': ['Basenji – "Haukuton koira"', 'Whippet – Hiljainen ja helppohoitoinen', 'Italianvinttikoira – Lempeä ja äänetön', 'Cavalier King Charles Spanieli – Luonnostaan hiljainen', 'Bulldoggi – Enemmän kuorsausta kuin haukuntaa'],
            'avoid_title': '⚠️ Kerrostaloihin Sopimattomia Rotuja',
            'avoid_intro': 'Jotkut rodut kärsivät kerrostaloissa korkean energian, haukunnan tai tilatarpeiden vuoksi:',
            'avoid_breeds': ['Bordercollie – Tarvitsee jatkuvaa henkistä stimulaatiota', 'Siperianhusky – Korkea energia, rakastaa ulvontaa', 'Beagle – Tunnettu haukkuja', 'Jack Russell Terrieri – Loputon energia', 'Australianpaimenkoira – Tarvitsee työtä tehtäväksi'],
            'tips_title': 'Vinkkejä Kerrostalokoiran Omistajille',
            'tips': ['Liikunta on tärkeämpää kuin tila – Väsynyt koira on onnellinen kerrostalokoira', 'Henkinen stimulaatio – Aktivointilelut ehkäisevät tylsistymistä', 'Siisteyskoulutus – Harkitse sisävessoja tai parvekeruohoa', 'Äänenkoulutus – Opeta "hiljaa"-komento aikaisin', 'Tarkista taloyhtiön säännöt – Joissain on rotu- tai kokorajoituksia'],
            'cta_title': 'Löydä Sopivasi',
            'cta_text': 'Et ole varma, mikä kerrostaloon sopiva rotu on sinulle oikea? Tee testimme löytääksesi elämäntyyliisi sopivat rodut.',
            'back': '← Takaisin',
            'quiz_btn': 'Tee Rotutesti →',
            'compare_btn': 'Vertaile Rotuja',
            'footer': '© 2026 BreedFinder. Tehty rakkaudella koiraystäville.',
        },
        'de': {
            'slug': 'beste-hunde-fuer-wohnungen',
            'badge': 'RATGEBER',
            'badge_color': 'sky',
            'title': '15 Beste Hunderassen für Wohnungen',
            'meta_title': '15 Beste Hunderassen für Wohnungen (2026)',
            'meta_desc': 'Suchst du einen wohnungsfreundlichen Hund? Diese 15 Rassen gedeihen in kleinen Räumen.',
            'subtitle': 'Denkst du, du brauchst ein Haus mit Garten für einen Hund? Denk nochmal. Diese Rassen fühlen sich in gemütlichen Räumen wohl.',
            'intro': 'In einer Wohnung zu leben bedeutet nicht, dass du keinen Hund haben kannst. Tatsächlich sind einige Rassen <em>besser</em> für das Wohnungsleben geeignet. Die wichtigsten Faktoren sind nicht nur die Größe—sondern <strong>Energielevel, Bellneigung und Anpassungsfähigkeit</strong>.',
            'tip_box': '<strong>Überraschende Tatsache:</strong> Einige große Rassen wie Windhunde sind ausgezeichnete Wohnungshunde, während kleine Rassen wie Jack Russell Terrier viel Platz brauchen.',
            'sections': [
                {'emoji': '🏆', 'title': 'Top 5 Wohnungshunde', 'breeds': [
                    ('Französische Bulldogge', 'french-bulldog', 'Der ultimative Wohnungsbegleiter. Frenchies sind ruhig, brauchen wenig Bewegung und lieben es, auf der Couch zu faulenzen.'),
                    ('Cavalier King Charles Spaniel', 'cavalier-king-charles-spaniel', 'Sanft, ruhig und glücklich auf deinem Schoß. Cavaliers sind anpassungsfähig und von Natur aus ruhig.'),
                    ('Bichon Frisé', 'bichon-frise', 'Klein, fröhlich und hypoallergen. Bichons haaren kaum und sind für ihre Ruhe bekannt.'),
                    ('Mops', 'pug', 'Möpse wurden buchstäblich als Schoßhunde gezüchtet. Sie sind energiearm und lieben die Nähe zu ihren Besitzern.'),
                    ('Boston Terrier', 'boston-terrier', 'Der "Amerikanische Gentleman" ist kompakt, ruhig und anpassungsfähig mit moderatem Energieniveau.'),
                ]},
                {'emoji': '🐕', 'title': 'Mittelgroße Wohnungshunde', 'breeds': [
                    ('Basset Hound', 'basset-hound', 'Lass dich nicht von der Größe täuschen—Basset Hounds sind Couchpotatoes. Ruhig, energiearm und zufrieden mit einem täglichen Spaziergang.'),
                    ('Englische Bulldogge', 'bulldog', 'Bulldoggen sind ruhig, würdevoll und brauchen minimale Bewegung. Sie bevorzugen klimatisierte Wohnungen.'),
                    ('Shiba Inu', 'shiba-inu', 'Sauber, ruhig und katzenartig unabhängig. Shibas pflegen sich selbst und bellen selten.'),
                ]},
                {'emoji': '🦴', 'title': 'Überraschend Gut: Große Wohnungshunde', 'breeds': [
                    ('Windhund', 'greyhound', 'Ja, wirklich! Pensionierte Rennwindhunde sind ruhig, leise und schlafen bis zu 18 Stunden am Tag.'),
                    ('Deutsche Dogge', 'great-dane', 'Als "sanfte Riesen" bekannt, sind Deutsche Doggen überraschend energiearm und ruhig drinnen.'),
                ]},
            ],
            'quiet_title': '🔇 Leiseste Rassen für Wohnungen',
            'quiet_intro': 'Lärmbeschwerden sind ein echtes Problem für Wohnungsbewohner. Diese Rassen bellen selten:',
            'quiet_breeds': ['Basenji – Der "belllose Hund"', 'Whippet – Ruhig und pflegeleicht', 'Italienisches Windspiel – Sanft und still', 'Cavalier King Charles Spaniel – Von Natur aus ruhig', 'Bulldogge – Mehr Schnarchen als Bellen'],
            'avoid_title': '⚠️ Zu Vermeidende Rassen in Wohnungen',
            'avoid_intro': 'Einige Rassen haben Schwierigkeiten in Wohnungen wegen hoher Energie, Bellen oder Platzbedarf:',
            'avoid_breeds': ['Border Collie – Braucht ständige geistige Stimulation', 'Husky – Hohe Energie, liebt zu heulen', 'Beagle – Notorische Beller', 'Jack Russell Terrier – Endlose Energie', 'Australian Shepherd – Braucht eine Aufgabe'],
            'tips_title': 'Tipps für Wohnungshundebesitzer',
            'tips': ['Bewegung ist wichtiger als Platz – Ein müder Hund ist ein glücklicher Wohnungshund', 'Geistige Stimulation – Puzzlespielzeug verhindert Langeweile', 'Sauberkeitstraining – Erwäge Hundetoiletten oder Balkonrasen', 'Lärmtraining – Lehre früh "leise" Kommandos', 'Prüfe Hausregeln – Manche haben Rassen- oder Größenbeschränkungen'],
            'cta_title': 'Finde Deinen Match',
            'cta_text': 'Nicht sicher, welche Wohnungsrasse die richtige für dich ist? Mach unser Quiz.',
            'back': '← Zurück',
            'quiz_btn': 'Mach das Rassen-Quiz →',
            'compare_btn': 'Rassen Vergleichen',
            'footer': '© 2026 BreedFinder. Mit Liebe für Hundefreunde gemacht.',
        },
    },
    'families': {
        'en': {
            'slug': 'best-dogs-for-families',
            'badge': 'FAMILY GUIDE',
            'badge_color': 'rose',
            'title': '12 Best Dog Breeds for Families with Kids',
            'meta_title': '12 Best Dog Breeds for Families with Kids (2026)',
            'meta_desc': 'Finding a family dog? These 12 breeds are patient, gentle, and great with children.',
            'subtitle': 'Looking for a four-legged family member? These breeds are known for patience, gentleness, and love for children.',
            'intro': 'The right family dog becomes a best friend, protector, and teacher of responsibility for your children. The best family dogs are <strong>patient, tolerant of noise and handling, and gentle by nature</strong>.',
            'tip_box': '<strong>Important:</strong> No matter the breed, always supervise interactions between dogs and young children. Teach kids how to approach and handle dogs respectfully.',
        },
        'fi': {
            'slug': 'parhaat-perhekoirat',
            'badge': 'PERHEOPAS',
            'badge_color': 'rose',
            'title': '12 Parasta Koirarotua Lapsiperheille',
            'meta_title': '12 Parasta Koirarotua Lapsiperheille (2026)',
            'meta_desc': 'Etsitkö perhekoiraa? Nämä 12 rotua ovat kärsivällisiä, lempeitä ja loistavia lasten kanssa.',
            'subtitle': 'Etsitkö nelijalkaista perheenjäsentä? Nämä rodut tunnetaan kärsivällisyydestään, lempeydestään ja rakkaudestaan lapsia kohtaan.',
            'intro': 'Oikea perhekoira tulee lasten parhaaksi ystäväksi, suojelijaksi ja vastuullisuuden opettajaksi. Parhaat perhekoirat ovat <strong>kärsivällisiä, sietävät melua ja käsittelyä, ja ovat luonnostaan lempeitä</strong>.',
            'tip_box': '<strong>Tärkeää:</strong> Rodusta riippumatta, valvo aina koiran ja pienten lasten kohtaamisia. Opeta lapsille, miten koiraa lähestytään ja käsitellään kunnioittavasti.',
        },
        'de': {
            'slug': 'beste-hunde-fuer-familien',
            'badge': 'FAMILIENRATGEBER',
            'badge_color': 'rose',
            'title': '12 Beste Hunderassen für Familien mit Kindern',
            'meta_title': '12 Beste Hunderassen für Familien mit Kindern (2026)',
            'meta_desc': 'Suchst du einen Familienhund? Diese 12 Rassen sind geduldig, sanft und großartig mit Kindern.',
            'subtitle': 'Suchst du ein vierbeiniges Familienmitglied? Diese Rassen sind bekannt für Geduld, Sanftheit und Liebe zu Kindern.',
            'intro': 'Der richtige Familienhund wird zum besten Freund, Beschützer und Lehrer für Verantwortung. Die besten Familienhunde sind <strong>geduldig, tolerant gegenüber Lärm und Anfassen, und von Natur aus sanft</strong>.',
            'tip_box': '<strong>Wichtig:</strong> Unabhängig von der Rasse, beaufsichtige immer Interaktionen zwischen Hunden und kleinen Kindern.',
        },
    },
    'shedding': {
        'en': {
            'slug': 'low-shedding-dogs',
            'badge': 'GROOMING GUIDE',
            'badge_color': 'emerald',
            'title': '20 Best Low-Shedding Dog Breeds',
            'meta_title': '20 Best Low-Shedding Dog Breeds (2026)',
            'meta_desc': 'Hate vacuuming dog hair? These 20 low-shedding breeds keep your home cleaner.',
            'subtitle': "Love dogs but hate fur on your couch? These breeds keep shedding to a minimum—but there's a trade-off.",
            'intro': "All dogs shed at least a little—it's how they regulate temperature. But some breeds shed so minimally you'll barely notice. The secret? Many low-shedding dogs have <strong>hair that grows continuously</strong> rather than fur that cycles.",
            'tip_box': '<strong>The trade-off:</strong> Most low-shedding breeds require regular professional grooming (every 4-8 weeks). Less vacuuming, more grooming appointments!',
        },
        'fi': {
            'slug': 'vahan-karvaavat-koirat',
            'badge': 'HOITO-OPAS',
            'badge_color': 'emerald',
            'title': '20 Parasta Vähän Karvaavaa Koirarotua',
            'meta_title': '20 Parasta Vähän Karvaavaa Koirarotua (2026)',
            'meta_desc': 'Vihaatko koirankarvojen imurointia? Nämä 20 rotua pitävät kotisi siistimpänä.',
            'subtitle': 'Rakastatko koiria mutta vihaat karvoja sohvalla? Nämä rodut karvaavat minimaalisesti—mutta vaihtokauppa on olemassa.',
            'intro': 'Kaikki koirat karvaavat ainakin vähän—se on tapa säädellä lämpötilaa. Mutta jotkut rodut karvaavat niin vähän, ettet juuri huomaa. Salaisuus? Monilla vähän karvaavilla koirilla on <strong>jatkuvasti kasvavat karvat</strong> turkin sijaan.',
            'tip_box': '<strong>Vaihtokauppa:</strong> Useimmat vähän karvaavat rodut vaativat säännöllistä ammattitrimmaus (4-8 viikon välein). Vähemmän imurointia, enemmän trimmausaikoja!',
        },
        'de': {
            'slug': 'wenig-haarende-hunde',
            'badge': 'PFLEGERAT',
            'badge_color': 'emerald',
            'title': '20 Beste Wenig Haarende Hunderassen',
            'meta_title': '20 Beste Wenig Haarende Hunderassen (2026)',
            'meta_desc': 'Hasst du das Staubsaugen von Hundehaaren? Diese 20 Rassen halten dein Zuhause sauberer.',
            'subtitle': 'Liebst du Hunde aber hasst Fell auf deiner Couch? Diese Rassen haaren minimal—aber es gibt einen Kompromiss.',
            'intro': 'Alle Hunde haaren zumindest ein wenig—so regulieren sie ihre Temperatur. Aber einige Rassen haaren so minimal, dass du es kaum bemerkst. Das Geheimnis? Viele wenig haarende Hunde haben <strong>kontinuierlich wachsendes Haar</strong> statt Fell.',
            'tip_box': '<strong>Der Kompromiss:</strong> Die meisten wenig haarenden Rassen brauchen regelmäßige professionelle Pflege (alle 4-8 Wochen). Weniger Staubsaugen, mehr Pflege!',
        },
    },
}

# Add fallback for missing translations
for article_key in ARTICLES:
    for lang in LANGUAGES:
        if lang not in ARTICLES[article_key]:
            ARTICLES[article_key][lang] = ARTICLES[article_key]['en'].copy()


def generate_article_html(article_key, lang, t):
    """Generate article HTML for a specific language"""
    
    # Use different depth based on language
    depth = '../../' if lang == 'en' else '../../../'
    lang_path = '' if lang == 'en' else f'{lang}/'
    
    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{t['meta_title']} | BreedFinder</title>
    <meta name="description" content="{t['meta_desc']}">
    <link rel="canonical" href="https://breedfinder.org/{lang_path}articles/{t['slug']}/">
    <link rel="icon" href="{depth}favicon.ico" type="image/x-icon">
    
    <meta property="og:title" content="{t['title']}">
    <meta property="og:description" content="{t['meta_desc']}">
    <meta property="og:url" content="https://breedfinder.org/{lang_path}articles/{t['slug']}/">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
        .prose h2 {{ font-size: 1.5rem; font-weight: 700; margin-top: 2rem; margin-bottom: 1rem; color: #0f172a; }}
        .prose h3 {{ font-size: 1.25rem; font-weight: 600; margin-top: 1.5rem; margin-bottom: 0.5rem; color: #334155; }}
        .prose p {{ margin-bottom: 1rem; color: #475569; line-height: 1.8; }}
        .prose ul {{ margin-left: 1.5rem; margin-bottom: 1rem; list-style: disc; color: #475569; }}
        .prose li {{ margin-bottom: 0.5rem; }}
    </style>
</head>
<body class="bg-slate-50 text-slate-900">
    <header class="bg-white border-b border-slate-200 py-4 px-4">
        <div class="max-w-4xl mx-auto flex items-center justify-between">
            <a href="{depth}{lang_path}" class="flex items-center gap-2">
                <img src="{depth}logo-192.png" class="w-10 h-10 rounded-xl" alt="BreedFinder">
                <span class="text-xl font-bold">BreedFinder</span>
            </a>
            <a href="{depth}{lang_path}" class="text-slate-600 hover:text-slate-900 text-sm">{t.get('back', '← Back')}</a>
        </div>
    </header>

    <main class="px-4 py-12">
        <article class="max-w-3xl mx-auto">
            <div class="mb-8">
                <span class="text-{t['badge_color']}-600 font-medium text-sm">{t['badge']}</span>
                <h1 class="text-3xl md:text-4xl font-bold mt-2 mb-4">{t['title']}</h1>
                <p class="text-slate-600 text-lg">{t['subtitle']}</p>
            </div>

            <div class="prose max-w-none">
                <p class="text-lg">{t['intro']}</p>

                <div class="bg-{t['badge_color']}-50 border-l-4 border-{t['badge_color']}-500 p-4 rounded-r-xl my-6">
                    <p class="text-{t['badge_color']}-900 mb-0">{t['tip_box']}</p>
                </div>
'''
    
    # Add sections if present (for apartments article)
    if 'sections' in t:
        for section in t['sections']:
            html += f'''
                <h2>{section['emoji']} {section['title']}</h2>
'''
            for breed_name, breed_slug, breed_desc in section['breeds']:
                html += f'''
                <h3>{breed_name}</h3>
                <p>{breed_desc} <a href="{depth}{lang_path}breeds/{breed_slug}.html" class="text-sky-600 hover:underline">→</a></p>
'''
    
    # Add quiet breeds section if present
    if 'quiet_title' in t:
        html += f'''
                <h2>{t['quiet_title']}</h2>
                <p>{t['quiet_intro']}</p>
                <ul>
'''
        for breed in t['quiet_breeds']:
            html += f'                    <li><strong>{breed.split(" – ")[0]}</strong> – {breed.split(" – ")[1] if " – " in breed else ""}</li>\n'
        html += '                </ul>\n'
    
    # Add avoid breeds section if present
    if 'avoid_title' in t:
        html += f'''
                <h2>{t['avoid_title']}</h2>
                <p>{t['avoid_intro']}</p>
                <ul>
'''
        for breed in t['avoid_breeds']:
            html += f'                    <li><strong>{breed.split(" – ")[0]}</strong> – {breed.split(" – ")[1] if " – " in breed else ""}</li>\n'
        html += '                </ul>\n'
    
    # Add tips section if present
    if 'tips_title' in t:
        html += f'''
                <h2>{t['tips_title']}</h2>
                <div class="bg-slate-100 rounded-xl p-6 my-6">
                    <ul class="mb-0">
'''
        for tip in t['tips']:
            parts = tip.split(' – ')
            if len(parts) == 2:
                html += f'                        <li><strong>{parts[0]}</strong> – {parts[1]}</li>\n'
            else:
                html += f'                        <li>{tip}</li>\n'
        html += '''                    </ul>
                </div>
'''
    
    # Add CTA section
    cta_title = t.get('cta_title', 'Find Your Match')
    cta_text = t.get('cta_text', 'Take our quiz to find breeds that match your lifestyle.')
    quiz_btn = t.get('quiz_btn', 'Take the Breed Quiz →')
    compare_btn = t.get('compare_btn', 'Compare Breeds')
    
    html += f'''
                <h2>{cta_title}</h2>
                <p>{cta_text}</p>

                <div class="flex gap-4 mt-6">
                    <a href="{depth}{lang_path}quiz/" class="inline-block bg-{t['badge_color']}-600 hover:bg-{t['badge_color']}-700 text-white font-semibold px-6 py-3 rounded-xl">{quiz_btn}</a>
                    <a href="{depth}{lang_path}compare/" class="inline-block bg-slate-200 hover:bg-slate-300 text-slate-800 font-semibold px-6 py-3 rounded-xl">{compare_btn}</a>
                </div>
            </div>
        </article>
    </main>

    <footer class="bg-slate-900 text-white py-8 px-4 mt-12">
        <div class="max-w-4xl mx-auto text-center text-slate-400 text-sm">
            <p>{t.get('footer', '© 2026 BreedFinder. Made with care for dog lovers everywhere.')}</p>
        </div>
    </footer>
</body>
</html>'''
    
    return html


def main():
    base_dir = Path(__file__).parent.parent
    
    print("Generating translated articles...")
    count = 0
    
    for lang in LANGUAGES:
        lang_dir = base_dir / lang / 'articles'
        lang_dir.mkdir(parents=True, exist_ok=True)
        
        # Create articles index for this language
        # ... (simplified for now)
        
        for article_key, translations in ARTICLES.items():
            t = translations.get(lang, translations['en'])
            slug = t['slug']
            
            article_dir = lang_dir / slug
            article_dir.mkdir(parents=True, exist_ok=True)
            
            html = generate_article_html(article_key, lang, t)
            
            with open(article_dir / 'index.html', 'w', encoding='utf-8') as f:
                f.write(html)
            
            count += 1
            print(f"  Created {lang}/articles/{slug}/index.html")
    
    print(f"\n✅ Done! Created {count} article pages")


if __name__ == '__main__':
    main()
