#!/usr/bin/env python3
"""Generate Italian comparison articles with full translations."""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

IT_UI = {
    'all_breeds': 'Tutte le Razze',
    'compare': 'Confronta',
    'take_quiz': 'Fai il Quiz',
    'comparisons': 'Confronti',
    'side_by_side': 'Confronto Fianco a Fianco',
    'attribute': 'Attributo',
    'size': 'Taglia',
    'lifespan': 'Durata della Vita',
    'energy_level': 'Livello di Energia',
    'grooming_needs': 'Esigenze di Toelettatura',
    'trainability': 'Addestrabilità',
    'kid_friendly': 'Adatto ai Bambini',
    'apartment': 'Adatto ad Appartamento',
    'shedding': 'Perdita di Pelo',
    'more_comparisons': 'Altri Confronti',
    'back_to_compare': '← Torna a Confronta',
    'view_profile': 'Vedi profilo completo →',
    'large': 'Grande',
    'years': 'anni',
    'very_high': 'Molto Alto',
    'high': 'Alto',
    'moderate': 'Moderato',
    'excellent': 'Eccellente',
    'not_ideal': 'Non Ideale',
    'heavy': 'Abbondante',
    'helping_find': 'Ti aiutiamo a trovare il tuo compagno perfetto.',
    'temperament': 'Temperamento',
    'exercise_needs': 'Esigenze di Esercizio',
    'grooming_req': 'Requisiti di Toelettatura',
    'which_right': 'Qual è Quello Giusto per Te?',
    'choose_if': 'Scegli un {breed} se...',
    'bottom_line': 'In Conclusione',
}

IT_TRAITS = {
    'Friendly': 'Amichevole', 'Outgoing': 'Socievole', 'Active': 'Attivo', 'Gentle': 'Gentile',
    'Intelligent': 'Intelligente', 'Trusting': 'Fiducioso', 'Devoted': 'Devoto',
    'Reliable': 'Affidabile', 'Trustworthy': 'Fidato', 'Kind': 'Buono',
    'Playful': 'Giocoso', 'Adaptable': 'Adattabile', 'Smart': 'Sveglio',
    'Affectionate': 'Affettuoso', 'Patient': 'Paziente', 'Alert': 'Vigile',
    'Bright': 'Brillante', 'Amusing': 'Divertente', 'Lively': 'Vivace',
    'Confident': 'Sicuro', 'Courageous': 'Coraggioso', 'Loyal': 'Leale',
    'Versatile': 'Versatile', 'Protective': 'Protettivo', 'Hardworking': 'Lavoratore',
    'Intense': 'Intenso', 'Mischievous': 'Birichino', 'Dignified': 'Dignitoso',
    'Strong': 'Forte', 'Faithful': 'Fedele', 'Trainable': 'Addestrabile', 'Proud': 'Fiero',
}

COMPARISONS = {
    'labrador-vs-golden': {
        'slug': 'labrador-vs-golden-retriever',
        'breed1': 'Labrador Retriever',
        'breed2': 'Golden Retriever',
        'breed1_slug': 'labrador-retriever',
        'breed2_slug': 'golden-retriever',
        'title': 'Labrador Retriever vs Golden Retriever: Confronto Completo',
        'desc': 'Confronto Labrador vs Golden Retriever. Scopri taglia, temperamento, esigenze di esercizio e adattabilità familiare.',
        'intro': 'Due delle razze familiari più amate al mondo. Entrambi sono amichevoli, intelligenti e ottimi con i bambini—ma quale è giusto per te?',
        'breed1_tagline': 'Razza #1 al Mondo',
        'breed2_tagline': 'Il Preferito delle Famiglie',
        'breed1_desc': 'Il Labrador Retriever è la razza canina più popolare al mondo. Sono amichevoli, socievoli e compagni pieni di energia e amore.',
        'breed2_desc': 'Il Golden Retriever è una delle razze più popolari. Il loro atteggiamento amichevole e tollerante li rende fantastici animali domestici.',
        'breed1_traits': ['Friendly', 'Outgoing', 'Active', 'Gentle', 'Intelligent', 'Trusting'],
        'breed2_traits': ['Intelligent', 'Friendly', 'Devoted', 'Reliable', 'Trustworthy', 'Kind'],
        'breed1_temperament_desc': 'I Labrador sono famosi per la loro cordialità e creano legami con tutta la famiglia. Socializzano bene con vicini e altri cani. Non lasciarti ingannare dalla loro personalità rilassata—hanno bisogno di molto esercizio!',
        'breed2_temperament_desc': 'I Golden Retriever sono socievoli, affidabili e desiderosi di compiacere. Sono meravigliosi con i bambini e altri animali. La loro natura paziente e gentile li rende eccellenti cani da terapia.',
        'breed1_exercise': 'Alta energia, necessita di almeno 1-2 ore di esercizio attivo giornaliero. Adorano nuotare, riportare oggetti e avventure all\'aperto.',
        'breed2_exercise': 'Alta energia, ma leggermente meno intenso dei Labrador. Almeno 1 ora di esercizio giornaliero. Eccellenti nel riporto, nuoto e escursioni.',
        'breed1_grooming': 'Spazzolatura settimanale, più frequente durante la muta. Il pelo corto e denso è relativamente facile da mantenere, ma perde molto pelo.',
        'breed2_grooming': 'Spazzolatura quotidiana consigliata durante la muta. Il pelo più lungo richiede più attenzione per evitare nodi.',
        'breed1_reasons': ['Vuoi il massimo livello di energia', 'Preferisci un po\' meno toelettatura', 'Vuoi un cane sportivo versatile', 'Ami una personalità socievole ed entusiasta', 'La varietà di colori è importante (nero, giallo, cioccolato)'],
        'breed2_reasons': ['Preferisci un temperamento leggermente più calmo', 'Ami il pelo dorato fluente', 'Vuoi un eccellente cane da terapia/servizio', 'Apprezzi un\'indole gentile e paziente', 'Non ti dispiace spazzolare più frequentemente'],
        'bottom_line': 'Entrambe le razze sono eccezionali cani da famiglia. I Labrador sono leggermente più energici e più facili da mantenere per il pelo, mentre i Golden Retriever sono noti per la loro pazienza gentile e il pelo fluente. Qualsiasi scelta porterà anni di amore e compagnia!'
    },
    'frenchie-vs-boston': {
        'slug': 'bulldog-francese-vs-boston-terrier',
        'breed1': 'Bulldog Francese',
        'breed2': 'Boston Terrier',
        'breed1_slug': 'french-bulldog',
        'breed2_slug': 'boston-terrier',
        'title': 'Bulldog Francese vs Boston Terrier: Confronto Completo',
        'desc': 'Confronto Bulldog Francese vs Boston Terrier. Due compagni compatti a confronto.',
        'intro': 'Due razze affascinanti e compatte con grandi personalità. Entrambe ottime per la vita in appartamento—ma quale si adatta meglio al tuo stile di vita?',
        'breed1_tagline': 'Il Francese Affascinante',
        'breed2_tagline': 'Il Gentiluomo Americano',
        'breed1_desc': 'Il Bulldog Francese è una razza affascinante e adattabile con una personalità giocosa, noto per le sue orecchie da pipistrello e natura affettuosa.',
        'breed2_desc': 'Il Boston Terrier, noto come "Il Gentiluomo Americano", è un cane vivace con un temperamento amichevole e allegro.',
        'breed1_traits': ['Playful', 'Adaptable', 'Smart', 'Affectionate', 'Patient', 'Alert'],
        'breed2_traits': ['Friendly', 'Bright', 'Amusing', 'Gentle', 'Lively', 'Intelligent'],
        'breed1_temperament_desc': 'I Bulldog Francesi sono rilassati e adattabili, prosperano sia in appartamenti urbani che in case di campagna. Sono giocosi ma non iperattivi, rendendoli eccellenti compagni per vari stili di vita.',
        'breed2_temperament_desc': 'I Boston Terrier sono vivaci, molto intelligenti e hanno un\'indole gentile. Sono noti per le loro marcature simili a uno smoking e la personalità amichevole e divertente.',
        'breed1_exercise': 'Esigenze di esercizio moderate—brevi passeggiate e sessioni di gioco sono sufficienti. Evita sforzi eccessivi con il caldo a causa del muso schiacciato.',
        'breed2_exercise': 'Energia moderata, necessita di passeggiate quotidiane e gioco. Più atletico dei Frenchie, ma comunque soggetto al surriscaldamento.',
        'breed1_grooming': 'Toelettatura minima—spazzolatura settimanale. Pulisci regolarmente le pieghe facciali per prevenire infezioni.',
        'breed2_grooming': 'Bassa manutenzione—spazzolatura occasionale. Il loro pelo corto è facile da curare.',
        'breed1_reasons': ['Vuoi un compagno più calmo e rilassato', 'Preferisci una corporatura più robusta', 'Vivi in appartamento', 'Vuoi requisiti minimi di esercizio', 'Ami le adorabili orecchie da pipistrello'],
        'breed2_reasons': ['Vuoi un cane leggermente più attivo', 'Preferisci il look da smoking', 'Vuoi un cane più facile da addestrare', 'Ti piace una corporatura più atletica', 'Vuoi una razza più longeva'],
        'bottom_line': 'Entrambi sono eccellenti cani da appartamento con grandi personalità. I Frenchie sono più calmi e rilassati, mentre i Boston sono leggermente più energici e atletici. Entrambi ruberanno il tuo cuore!'
    },
    'gsd-vs-malinois': {
        'slug': 'pastore-tedesco-vs-malinois',
        'breed1': 'Pastore Tedesco',
        'breed2': 'Malinois Belga',
        'breed1_slug': 'german-shepherd',
        'breed2_slug': 'belgian-malinois',
        'title': 'Pastore Tedesco vs Malinois Belga: Confronto Completo',
        'desc': 'Confronto Pastore Tedesco vs Malinois Belga. Due eccellenti cani da lavoro a confronto.',
        'intro': 'Due dei cani da lavoro più capaci al mondo. Entrambi eccellono nel lavoro di polizia e militare—ma hanno differenze importanti.',
        'breed1_tagline': 'Il Protettore Versatile',
        'breed2_tagline': 'Cane da Lavoro d\'Elite',
        'breed1_desc': 'Il Pastore Tedesco è versatile, intelligente e una delle razze da lavoro più popolari al mondo.',
        'breed2_desc': 'Il Malinois Belga è un cane da lavoro intenso e ad alte prestazioni, preferito da polizia e militari in tutto il mondo.',
        'breed1_traits': ['Confident', 'Courageous', 'Smart', 'Loyal', 'Versatile', 'Protective'],
        'breed2_traits': ['Confident', 'Smart', 'Hardworking', 'Alert', 'Intense', 'Protective'],
        'breed1_temperament_desc': 'I Pastori Tedeschi sono sicuri, coraggiosi e incredibilmente versatili. Creano legami profondi con la famiglia e sono naturalmente protettivi senza essere aggressivi.',
        'breed2_temperament_desc': 'I Malinois sono cani da lavoro intensi e motivati con energia infinita. Hanno bisogno di un compito e prosperano con proprietari esperti che possono canalizzare la loro motivazione.',
        'breed1_exercise': 'Elevate esigenze di esercizio—almeno 2 ore al giorno. Eccellono in vari sport cinofili, tracking e obbedienza.',
        'breed2_exercise': 'Esigenze di esercizio molto elevate—2+ ore di attività intensa al giorno. Hanno bisogno di stimolazione mentale quanto di esercizio fisico.',
        'breed1_grooming': 'Toelettatura moderata—spazzola 2-3 volte a settimana. La muta stagionale intensa richiede più attenzione.',
        'breed2_grooming': 'Toelettatura facile—spazzolatura settimanale. Pelo più corto del Pastore Tedesco, ma perde comunque pelo stagionalmente.',
        'breed1_reasons': ['Vuoi un protettore familiare versatile', 'Preferisci un cane da lavoro leggermente più calmo', 'Sei un proprietario alle prime armi con razze da lavoro', 'Vuoi un cane bravo con i bambini', 'Preferisci il look classico'],
        'breed2_reasons': ['Vuoi massima motivazione e intensità', 'Sei un proprietario esperto', 'Vuoi un cane da sport/lavoro d\'elite', 'Puoi fornire esercizio estensivo', 'Vuoi un cane più leggero e veloce'],
        'bottom_line': 'Entrambi sono eccezionali cani da lavoro, ma i Malinois sono più intensi e richiedono proprietari esperti. I Pastori Tedeschi sono più versatili e più adatti alle famiglie. Scegli in base al tuo livello di esperienza e stile di vita.'
    },
    'husky-vs-malamute': {
        'slug': 'husky-vs-malamute',
        'breed1': 'Siberian Husky',
        'breed2': 'Alaskan Malamute',
        'breed1_slug': 'siberian-husky',
        'breed2_slug': 'alaskan-malamute',
        'title': 'Siberian Husky vs Alaskan Malamute: Confronto Completo',
        'desc': 'Confronto Husky vs Malamute. Razze artiche a confronto fianco a fianco.',
        'intro': 'Due razze artiche maestose dall\'aspetto simile al lupo. Sembrano simili ma hanno differenze importanti in dimensioni e temperamento.',
        'breed1_tagline': 'Il Cane da Slitta Veloce',
        'breed2_tagline': 'Il Potente Trasportatore',
        'breed1_desc': 'Il Siberian Husky è un cane da slitta atletico e resistente, noto per i suoi occhi blu e la personalità amichevole.',
        'breed2_desc': 'L\'Alaskan Malamute è un cane da slitta potente e robusto, allevato per forza e resistenza.',
        'breed1_traits': ['Outgoing', 'Mischievous', 'Loyal', 'Friendly', 'Alert', 'Gentle'],
        'breed2_traits': ['Affectionate', 'Loyal', 'Playful', 'Dignified', 'Devoted', 'Strong'],
        'breed1_temperament_desc': 'Gli Husky sono amichevoli, socievoli e a volte birichini. Sono cani da branco che amano la compagnia e sono noti per la loro natura vocale e le abilità di fuga.',
        'breed2_temperament_desc': 'I Malamute sono più dignitosi e meno birichini degli Husky. Sono profondamente leali, affettuosi con la famiglia, ma possono essere più indipendenti.',
        'breed1_exercise': 'Energia molto alta—progettati per correre chilometri. Almeno 2 ore di esercizio attivo al giorno. Adorano correre e attività di traino.',
        'breed2_exercise': 'Alta energia, ma con più resistenza che velocità. Lunghe escursioni e lavoro di traino sono adatti. Possono surriscaldarsi nei climi caldi.',
        'breed1_grooming': 'Toelettatura estensiva—spazzola più volte a settimana. Muta massiccia ("soffiare il pelo") due volte l\'anno.',
        'breed2_grooming': 'Toelettatura estensiva come l\'Husky. Il loro pelo più spesso richiede spazzolatura regolare per evitare nodi.',
        'breed1_reasons': ['Vuoi una razza artica di media taglia', 'Preferisci un cane più veloce e atletico', 'Ti piace un compagno chiacchierone e vocale', 'Vuoi occhi blu sorprendenti', 'Ti piace una personalità più giocosa'],
        'breed2_reasons': ['Vuoi un cane più grande e potente', 'Preferisci un temperamento più calmo e dignitoso', 'Hai esperienza con razze forti', 'Vuoi un cane più silenzioso (meno ululati)', 'Hai bisogno di un cane per traino/trasporto'],
        'bottom_line': 'Gli Husky sono atleti di media taglia che adorano correre e "parlare". I Malamute sono giganti potenti costruiti per la forza. Entrambi perdono molto pelo e hanno bisogno di molto esercizio. Scegli in base alla preferenza di taglia e temperamento desiderato.'
    },
    'poodle-vs-labrador': {
        'slug': 'barboncino-vs-labrador',
        'breed1': 'Barboncino',
        'breed2': 'Labrador Retriever',
        'breed1_slug': 'poodle',
        'breed2_slug': 'labrador-retriever',
        'title': 'Barboncino vs Labrador Retriever: Confronto Completo',
        'desc': 'Confronto Barboncino vs Labrador. Due razze intelligenti e popolari a confronto.',
        'intro': 'Due delle razze canine più intelligenti e popolari. Entrambi eccellenti cani da famiglia con mantelli molto diversi.',
        'breed1_tagline': 'L\'Atleta Elegante',
        'breed2_tagline': 'Il Migliore Amico di Tutti',
        'breed1_desc': 'Il Barboncino è eccezionalmente intelligente e attivo. Dietro l\'aspetto elegante c\'è un cane atletico e molto intelligente.',
        'breed2_desc': 'Il Labrador Retriever è la razza più popolare al mondo, nota per la sua natura amichevole e socievole.',
        'breed1_traits': ['Intelligent', 'Active', 'Alert', 'Faithful', 'Trainable', 'Proud'],
        'breed2_traits': ['Friendly', 'Active', 'Outgoing', 'Gentle', 'Intelligent', 'Trusting'],
        'breed1_temperament_desc': 'I Barboncini sono eccezionalmente intelligenti e desiderosi di compiacere. Non lasciarti ingannare dalle toelettature eleganti—sono cani atletici allevati per la caccia e il riporto.',
        'breed2_temperament_desc': 'I Labrador sono il cane amichevole per eccellenza—socievoli con tutti, pazienti con i bambini e desiderosi di compiacere. Sono il compagno familiare definitivo.',
        'breed1_exercise': 'Alta energia, necessita di esercizio quotidiano e stimolazione mentale. Eccellono in agility, obbedienza e vari sport cinofili.',
        'breed2_exercise': 'Alta energia—almeno 1-2 ore al giorno. Adorano nuotare, riportare oggetti e qualsiasi attività con i loro umani.',
        'breed1_grooming': 'Alta manutenzione—toelettatura professionale ogni 4-6 settimane. La spazzolatura quotidiana previene i nodi. Pelo ipoallergenico.',
        'breed2_grooming': 'Toelettatura facile, ma molta perdita di pelo. Spazzolatura settimanale, più frequente durante la muta. Non ipoallergenico.',
        'breed1_reasons': ['Hai allergie (ipoallergenico)', 'Vuoi minima perdita di pelo', 'Ti piace la toelettatura o non ti dispiace il costo', 'Vuoi un aspetto elegante', 'Vuoi opzioni di taglia (toy/mini/standard)'],
        'breed2_reasons': ['Preferisci toelettatura facile e economica', 'Non ti dispiace la perdita di pelo', 'Vuoi il classico cane da famiglia', 'Preferisci un look più casual', 'Vuoi un retriever che ama l\'acqua'],
        'bottom_line': 'Entrambi sono altamente intelligenti e facili da addestrare. I Barboncini offrono pelo ipoallergenico, ma richiedono più toelettatura. I Labrador sono più facili da mantenere, ma perdono molto pelo. Entrambi sono eccellenti compagni familiari!'
    }
}


def generate_article(comp_key, comp):
    ui = IT_UI
    breed1_traits = [IT_TRAITS.get(t, t) for t in comp['breed1_traits']]
    breed2_traits = [IT_TRAITS.get(t, t) for t in comp['breed2_traits']]
    
    breed1_tags = '\n                    '.join([f'<span class="bg-amber-100 text-amber-700 px-3 py-1 rounded-full text-sm font-medium">{t}</span>' for t in breed1_traits])
    breed2_tags = '\n                    '.join([f'<span class="bg-yellow-100 text-yellow-700 px-3 py-1 rounded-full text-sm font-medium">{t}</span>' for t in breed2_traits])
    
    breed1_reasons = '\n                        '.join([f'<li class="flex items-start gap-2"><span class="text-green-400">✓</span><span>{r}</span></li>' for r in comp['breed1_reasons']])
    breed2_reasons = '\n                        '.join([f'<li class="flex items-start gap-2"><span class="text-green-400">✓</span><span>{r}</span></li>' for r in comp['breed2_reasons']])
    
    related = [(k, v) for k, v in COMPARISONS.items() if k != comp_key][:3]
    related_html = '\n'.join([f'<a href="{r[1]["slug"]}.html" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md transition"><span class="font-semibold">{r[1]["breed1"]} vs {r[1]["breed2"]}</span></a>' for r in related])
    
    return f'''<!DOCTYPE html>
<html lang="it">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-VEERQZ53LZ"></script>
    <script>window.dataLayer = window.dataLayer || []; function gtag(){{dataLayer.push(arguments);}} gtag("js", new Date()); gtag("config", "G-VEERQZ53LZ");</script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{comp['title']} | BreedFinder</title>
    <meta name="description" content="{comp['desc']}">
    <link rel="canonical" href="https://breedfinder.org/it/compare/comparisons/{comp['slug']}.html">
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
                <a href="../../breeds/" class="text-slate-600 hover:text-sky-700">{ui['all_breeds']}</a>
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
                    <a href="../../breeds/{comp['breed1_slug']}" class="text-sky-700 font-semibold">{ui['view_profile']}</a>
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
                    <a href="../../breeds/{comp['breed2_slug']}" class="text-sky-700 font-semibold">{ui['view_profile']}</a>
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
    output_dir = BASE_DIR / 'it' / 'compare' / 'comparisons'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for comp_key, comp in COMPARISONS.items():
        html = generate_article(comp_key, comp)
        path = output_dir / f"{comp['slug']}.html"
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ {path.name}")
    
    print(f"\n✅ Generated 5 fully translated Italian comparison articles")


if __name__ == '__main__':
    main()
