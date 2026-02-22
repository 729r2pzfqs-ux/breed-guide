#!/usr/bin/env python3
"""Batch 7 Italian breed translations - Spaniels and Retrievers"""

import re
from pathlib import Path

IT_BREEDS_DIR = Path(__file__).parent.parent / 'it' / 'breeds'

BREEDS = {
    'english-cocker-spaniel': {
        'overview': "Il Cocker Spaniel Inglese è un cane da caccia allegro e affettuoso. Compagno perfetto per famiglie.",
        'temperament': "I Cocker Inglesi sono allegri, affettuosi e giocosi. Amano le persone e hanno bisogno di compagnia.",
        'health': "Predisposti a problemi alle orecchie, displasia dell'anca, problemi oculari e obesità.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano. Amano nuotare e giocare a riporto.",
        'verdict': "Un compagno allegro e devoto. I Cocker Inglesi sono perfetti per famiglie attive.",
    },
    'field-spaniel': {
        'overview': "Il Field Spaniel è un raro spaniel da caccia. Docile e affettuoso, è un compagno tranquillo.",
        'temperament': "I Field Spaniel sono docili, affettuosi e sensibili. Sono tranquilli e amano la famiglia.",
        'health': "Predisposti a displasia dell'anca, problemi oculari e ipotiroidismo.",
        'exercise': "Cani moderatamente attivi che amano le passeggiate e il nuoto.",
        'verdict': "Uno spaniel raro e gentile. I Field sono perfetti per chi cerca un compagno tranquillo.",
    },
    'sussex-spaniel': {
        'overview': "Il Sussex Spaniel è uno spaniel inglese raro dal mantello dorato. Calmo e affettuoso.",
        'temperament': "I Sussex sono calmi, amichevoli e determinati. Sono più tranquilli di altri spaniel.",
        'health': "Predisposti a problemi cardiaci, displasia dell'anca e problemi alle orecchie.",
        'exercise': "Cani moderatamente attivi. Passeggiate regolari sono sufficienti.",
        'verdict': "Uno spaniel dorato e raro. I Sussex sono perfetti per chi cerca un compagno calmo.",
    },
    'clumber-spaniel': {
        'overview': "Il Clumber Spaniel è il più grande degli spaniel. Dignitoso e affettuoso.",
        'temperament': "I Clumber sono calmi, affettuosi e gentili. Sono meno energici di altri spaniel.",
        'health': "Predisposti a displasia dell'anca, problemi alle orecchie, entropion e problemi alla schiena.",
        'exercise': "Cani a bassa-media energia. Passeggiate moderate sono sufficienti.",
        'verdict': "Un gigante gentile tra gli spaniel. I Clumber sono perfetti per chi cerca un compagno calmo.",
    },
    'irish-water-spaniel': {
        'overview': "L'Irish Water Spaniel è uno spaniel dal mantello riccio unico. Atletico e intelligente.",
        'temperament': "Gli Irish Water sono intelligenti, giocosi e indipendenti. Amano l'acqua e la famiglia.",
        'health': "Predisposti a displasia dell'anca, ipotiroidismo e problemi alle orecchie.",
        'exercise': "Cani attivi che amano nuotare. Necessitano di esercizio regolare.",
        'verdict': "Uno spaniel acquatico unico. Gli Irish Water sono perfetti per chi ama l'acqua.",
    },
    'american-water-spaniel': {
        'overview': "L'American Water Spaniel è uno spaniel versatile del Wisconsin. Energico e affettuoso.",
        'temperament': "Gli American Water sono energici, intelligenti e affettuosi. Sono versatili cacciatori.",
        'health': "Predisposti a displasia dell'anca, problemi oculari e cardiaci.",
        'exercise': "Cani attivi che amano nuotare e cacciare. Necessitano di esercizio quotidiano.",
        'verdict': "Uno spaniel americano versatile. Perfetti per famiglie attive che amano l'acqua.",
    },
    'flat-coated-retriever': {
        'overview': "Il Flat-Coated Retriever è un retriever elegante e gioioso. Eternamente giovane nel cuore.",
        'temperament': "I Flat-Coated sono gioiosi, affettuosi e giocosi. Maturano lentamente e restano cuccioli a lungo.",
        'health': "Predisposti a cancro, displasia dell'anca e problemi oculari. Vita relativamente breve.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio. Amano nuotare e giocare a riporto.",
        'verdict': "Un eterno cucciolo. I Flat-Coated sono perfetti per famiglie attive che cercano gioia.",
    },
    'curly-coated-retriever': {
        'overview': "Il Curly-Coated Retriever è il più antico dei retriever. Dal mantello riccio unico.",
        'temperament': "I Curly-Coated sono intelligenti, indipendenti e affettuosi. Più riservati di altri retriever.",
        'health': "Predisposti a displasia dell'anca, problemi oculari e epilessia.",
        'exercise': "Cani attivi che amano nuotare e lavorare. Necessitano di esercizio regolare.",
        'verdict': "Un retriever riccio e unico. I Curly sono perfetti per chi cerca un retriever indipendente.",
    },
    'chesapeake-bay-retriever': {
        'overview': "Il Chesapeake Bay Retriever è un retriever americano robusto. Eccelle nel lavoro in acqua fredda.",
        'temperament': "I Chesapeake sono protettivi, intelligenti e leali. Più riservati di altri retriever.",
        'health': "Predisposti a displasia dell'anca, atrofia retinica progressiva e problemi cardiaci.",
        'exercise': "Cani ad alta energia che amano nuotare. Necessitano di molto esercizio.",
        'verdict': "Un retriever robusto e leale. I Chesapeake sono perfetti per cacciatori e famiglie attive.",
    },
    'nova-scotia-duck-tolling-retriever': {
        'overview': "Il Nova Scotia Duck Tolling Retriever è il più piccolo dei retriever. Intelligente e giocoso.",
        'temperament': "I Toller sono intelligenti, energici e affettuosi. Eccellono nello sport e nel lavoro.",
        'health': "Predisposti a displasia dell'anca, atrofia retinica progressiva e problemi cardiaci.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio e stimolazione mentale.",
        'verdict': "Un piccolo retriever versatile. I Toller sono perfetti per chi cerca un compagno atletico.",
    },
    'lagotto-romagnolo': {
        'overview': "Il Lagotto Romagnolo è un cane italiano specializzato nella ricerca del tartufo. Dal mantello riccio.",
        'temperament': "I Lagotto sono affettuosi, intelligenti e giocosi. Amano lavorare e la famiglia.",
        'health': "Predisposti a displasia dell'anca, epilessia e problemi oculari.",
        'exercise': "Cani attivi che amano cercare e lavorare. Necessitano di stimolazione mentale.",
        'verdict': "Il cane da tartufo italiano. I Lagotto sono perfetti per chi cerca un compagno attivo.",
    },
    'spanish-water-dog': {
        'overview': "Il Cane d'Acqua Spagnolo è un cane versatile dal mantello riccio. Eccelle in acqua e a terra.",
        'temperament': "Gli Spanish Water Dog sono intelligenti, leali e giocosi. Sono versatili e adattabili.",
        'health': "Predisposti a displasia dell'anca, ipotiroidismo e problemi oculari.",
        'exercise': "Cani attivi che amano nuotare e lavorare. Necessitano di esercizio regolare.",
        'verdict': "Un cane spagnolo versatile. Perfetti per famiglie attive che amano l'acqua.",
    },
    'barbet': {
        'overview': "Il Barbet è un antico cane d'acqua francese. Dal mantello lanoso e personalità allegra.",
        'temperament': "I Barbet sono allegri, affettuosi e intelligenti. Amano l'acqua e la famiglia.",
        'health': "Predisposti a displasia dell'anca, problemi oculari e alle orecchie.",
        'exercise': "Cani attivi che amano nuotare. Necessitano di esercizio quotidiano.",
        'verdict': "Un cane d'acqua francese allegro. I Barbet sono perfetti per famiglie attive.",
    },
    'labradoodle': {
        'overview': "Il Labradoodle è un incrocio tra Labrador e Barboncino. Intelligente e ipoallergenico.",
        'temperament': "I Labradoodle sono amichevoli, intelligenti e giocosi. Eccellenti cani da famiglia.",
        'health': "Predisposti a displasia dell'anca, problemi oculari e allergie. La salute varia.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano. Amano giocare e nuotare.",
        'verdict': "Un ibrido popolare e intelligente. I Labradoodle sono perfetti per famiglie allergiche.",
    },
    'goldendoodle': {
        'overview': "Il Goldendoodle è un incrocio tra Golden Retriever e Barboncino. Affettuoso e intelligente.",
        'temperament': "I Goldendoodle sono affettuosi, intelligenti e giocosi. Eccellenti cani da famiglia e terapia.",
        'health': "Predisposti a displasia dell'anca, problemi cardiaci e allergie. La salute varia.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano. Amano giocare e nuotare.",
        'verdict': "Un ibrido dorato e affettuoso. I Goldendoodle sono perfetti per famiglie.",
    },
    'cockapoo': {
        'overview': "Il Cockapoo è un incrocio tra Cocker Spaniel e Barboncino. Allegro e affettuoso.",
        'temperament': "I Cockapoo sono allegri, affettuosi e intelligenti. Amano le persone e giocano.",
        'health': "Predisposti a lussazione della rotula, problemi oculari e alle orecchie.",
        'exercise': "Cani moderatamente attivi che amano giocare. Adattabili.",
        'verdict': "Un ibrido allegro e adattabile. I Cockapoo sono perfetti per famiglie.",
    },
    'cavapoo': {
        'overview': "Il Cavapoo è un incrocio tra Cavalier e Barboncino. Dolce e affettuoso.",
        'temperament': "I Cavapoo sono dolci, affettuosi e gentili. Amano le coccole e la famiglia.",
        'health': "Predisposti a problemi cardiaci, lussazione della rotula e problemi oculari.",
        'exercise': "Cani moderatamente attivi. Adattabili a vari stili di vita.",
        'verdict': "Un ibrido dolce e adattabile. I Cavapoo sono perfetti per famiglie.",
    },
    'bernedoodle': {
        'overview': "Il Bernedoodle è un incrocio tra Bovaro del Bernese e Barboncino. Affettuoso e giocoso.",
        'temperament': "I Bernedoodle sono affettuosi, giocosi e intelligenti. Amano la famiglia.",
        'health': "Predisposti a displasia dell'anca, problemi oculari. Generalmente più sani dei Bovari puri.",
        'exercise': "Cani moderatamente attivi che amano giocare. Le esigenze variano con la taglia.",
        'verdict': "Un ibrido tricolore affettuoso. I Bernedoodle sono perfetti per famiglie.",
    },
    'aussiedoodle': {
        'overview': "L'Aussiedoodle è un incrocio tra Australian Shepherd e Barboncino. Intelligente e atletico.",
        'temperament': "Gli Aussiedoodle sono intelligenti, energici e affettuosi. Eccellono nello sport.",
        'health': "Predisposti a displasia dell'anca, problemi oculari e epilessia.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio e stimolazione mentale.",
        'verdict': "Un ibrido atletico e brillante. Gli Aussiedoodle sono perfetti per famiglie molto attive.",
    },
    'schnoodle': {
        'overview': "Lo Schnoodle è un incrocio tra Schnauzer e Barboncino. Vivace e intelligente.",
        'temperament': "Gli Schnoodle sono vivaci, intelligenti e affettuosi. Sono buoni cani da guardia.",
        'health': "Predisposti a problemi oculari, lussazione della rotula e allergie.",
        'exercise': "Cani attivi che amano giocare. Le esigenze variano con la taglia.",
        'verdict': "Un ibrido vivace e vigile. Gli Schnoodle sono perfetti per famiglie attive.",
    },
}

def update_file(breed_id, trans):
    filepath = IT_BREEDS_DIR / f'{breed_id}.html'
    if not filepath.exists():
        return False
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    if 'overview' in trans:
        meta_desc = trans['overview'][:150] + '...' if len(trans['overview']) > 150 else trans['overview']
        content = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{meta_desc}">', content)
        content = re.sub(r'(<p class="text-lg text-slate-600 mb-6">)[^<]*(</p>)', f'\\1{trans["overview"][:200]}\\2', content)
        content = re.sub(r'(Panoramica\s*</h2>.*?<div class="px-6 pb-6"><p class="text-slate-600">)[^<]*(</p></div>)', f'\\1{trans["overview"]}\\2', content, flags=re.DOTALL)
    if 'temperament' in trans:
        content = re.sub(r'(<i data-lucide="heart"[^>]*></i>\s*Temperamento\s*</h2>.*?<div class="px-6 pb-6"><p class="text-slate-600">)[^<]*(</p></div>)', f'\\1{trans["temperament"]}\\2', content, flags=re.DOTALL)
    if 'health' in trans:
        content = re.sub(r'(Salute\s*</h2>.*?<div class="px-6 pb-6"><p class="text-slate-600">)[^<]*(</p></div>)', f'\\1{trans["health"]}\\2', content, flags=re.DOTALL)
    if 'exercise' in trans:
        content = re.sub(r'(Esercizio\s*</h2>.*?<div class="px-6 pb-6"><p class="text-slate-600">)[^<]*(</p></div>)', f'\\1{trans["exercise"]}\\2', content, flags=re.DOTALL)
    if 'verdict' in trans:
        content = re.sub(r'(<strong>Il Nostro Verdetto:</strong> )[^<]*(</p>)', f'\\1{trans["verdict"]}\\2', content)
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

if __name__ == '__main__':
    print(f"Translating {len(BREEDS)} breeds...")
    count = 0
    for bid, trans in BREEDS.items():
        if update_file(bid, trans):
            print(f"  ✓ {bid}")
            count += 1
    print(f"Done! Updated {count} files.")
