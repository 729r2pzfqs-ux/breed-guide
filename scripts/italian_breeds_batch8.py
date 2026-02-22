#!/usr/bin/env python3
"""Batch 8 Italian breed translations - More Working Dogs and Hounds"""

import re
from pathlib import Path

IT_BREEDS_DIR = Path(__file__).parent.parent / 'it' / 'breeds'

BREEDS = {
    'bullmastiff': {
        'overview': "Il Bullmastiff è un cane da guardia potente ma gentile. Leale e protettivo verso la famiglia.",
        'temperament': "I Bullmastiff sono calmi, leali e protettivi. Sono gentili con la famiglia ma diffidenti con gli estranei.",
        'health': "Predisposti a displasia dell'anca, torsione gastrica, cancro e problemi cardiaci.",
        'exercise': "Cani a moderata energia. Passeggiate regolari sono sufficienti. Non tollerano il caldo.",
        'verdict': "Un guardiano gentile. I Bullmastiff sono perfetti per chi cerca un protettore calmo.",
    },
    'dogue-de-bordeaux': {
        'overview': "Il Dogue de Bordeaux è un antico molosso francese. Potente ma affettuoso e leale.",
        'temperament': "I Dogue sono calmi, affettuosi e leali. Sono protettivi ma non aggressivi. Sbavano molto.",
        'health': "Predisposti a displasia dell'anca, problemi cardiaci, torsione gastrica. Vita breve (5-8 anni).",
        'exercise': "Cani a bassa energia. Passeggiate moderate. Non tollerano il caldo.",
        'verdict': "Un molosso francese devoto. I Dogue sono perfetti per chi cerca un compagno calmo e leale.",
    },
    'neapolitan-mastiff': {
        'overview': "Il Mastino Napoletano è un antico cane da guardia italiano. Imponente e protettivo.",
        'temperament': "I Mastini Napoletani sono calmi, leali e protettivi. Sono diffidenti con gli estranei.",
        'health': "Predisposti a displasia dell'anca, problemi oculari, cardiaci e cutanei. Sbavano molto.",
        'exercise': "Cani a bassa energia. Passeggiate moderate. Non tollerano il caldo.",
        'verdict': "Un guardiano italiano imponente. Perfetti per proprietari esperti.",
    },
    'tibetan-mastiff': {
        'overview': "Il Mastino Tibetano è un antico guardiano himalayano. Indipendente e protettivo.",
        'temperament': "I Mastini Tibetani sono indipendenti, protettivi e riservati. Richiedono proprietari esperti.",
        'health': "Predisposti a displasia dell'anca, ipotiroidismo e problemi oculari.",
        'exercise': "Cani moderatamente attivi. Amano il freddo e gli spazi aperti.",
        'verdict': "Un guardiano himalayano maestoso. Solo per proprietari molto esperti.",
    },
    'komondor': {
        'overview': "Il Komondor è un cane da guardia ungherese dal mantello a corde unico. Protettivo e indipendente.",
        'temperament': "I Komondor sono indipendenti, protettivi e calmi. Sono diffidenti con gli estranei.",
        'health': "Predisposti a displasia dell'anca, torsione gastrica e problemi oculari. Il mantello richiede cure.",
        'exercise': "Cani moderatamente attivi. Amano avere un territorio da guardare.",
        'verdict': "Un guardiano ungherese unico. I Komondor sono solo per proprietari esperti.",
    },
    'kuvasz': {
        'overview': "Il Kuvasz è un antico cane da guardia ungherese dal mantello bianco. Indipendente e protettivo.",
        'temperament': "I Kuvasz sono indipendenti, intelligenti e protettivi. Sono leali ma diffidenti.",
        'health': "Predisposti a displasia dell'anca, torsione gastrica e problemi oculari.",
        'exercise': "Cani moderatamente attivi che amano avere spazio e un lavoro.",
        'verdict': "Un guardiano bianco ungherese. I Kuvasz sono per proprietari esperti.",
    },
    'great-pyrenees': {
        'overview': "Il Cane da Montagna dei Pirenei è un maestoso guardiano dal mantello bianco. Gentile e protettivo.",
        'temperament': "I Pirenei sono calmi, gentili e protettivi. Sono indipendenti e possono essere testardi.",
        'health': "Predisposti a displasia dell'anca, torsione gastrica e problemi cardiaci.",
        'exercise': "Cani a moderata energia. Amano avere un territorio da pattugliare.",
        'verdict': "Un guardiano bianco maestoso. I Pirenei sono perfetti per chi ha spazio.",
    },
    'anatolian-shepherd': {
        'overview': "Il Pastore dell'Anatolia è un antico guardiano turco. Potente e indipendente.",
        'temperament': "I Pastori dell'Anatolia sono indipendenti, intelligenti e protettivi. Richiedono socializzazione.",
        'health': "Generalmente sani. Predisposti a displasia dell'anca e ipotiroidismo.",
        'exercise': "Cani moderatamente attivi che necessitano di spazio e un lavoro.",
        'verdict': "Un guardiano turco antico. Solo per proprietari esperti con spazio.",
    },
    'central-asian-shepherd': {
        'overview': "Il Pastore dell'Asia Centrale è un antico guardiano delle steppe. Potente e indipendente.",
        'temperament': "I Pastori dell'Asia Centrale sono indipendenti, calmi e protettivi. Sono diffidenti con gli estranei.",
        'health': "Generalmente sani. Predisposti a displasia dell'anca e problemi cardiaci.",
        'exercise': "Cani moderatamente attivi che necessitano di spazio.",
        'verdict': "Un guardiano delle steppe. Solo per proprietari molto esperti.",
    },
    'black-russian-terrier': {
        'overview': "Il Terrier Nero Russo è un cane da lavoro sovietico. Potente e intelligente.",
        'temperament': "I BRT sono intelligenti, coraggiosi e leali. Sono protettivi ma equilibrati.",
        'health': "Predisposti a displasia dell'anca e del gomito, problemi oculari e cardiaci.",
        'exercise': "Cani attivi che necessitano di esercizio e stimolazione mentale.",
        'verdict': "Un lavoratore russo versatile. I BRT sono perfetti per proprietari esperti attivi.",
    },
    'american-english-coonhound': {
        'overview': "L'American English Coonhound è un segugio energico. Eccelle nella caccia al procione.",
        'temperament': "Gli American English sono amichevoli, energici e vocali. Amano cacciare e la famiglia.",
        'health': "Generalmente sani. Predisposti a displasia dell'anca e problemi alle orecchie.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio e spazio.",
        'verdict': "Un segugio americano energico. Perfetti per cacciatori attivi.",
    },
    'black-and-tan-coonhound': {
        'overview': "Il Black and Tan Coonhound è un segugio americano dal mantello nero focato. Amichevole e determinato.",
        'temperament': "I Black and Tan sono amichevoli, calmi e determinati. Sono vocali e amano seguire tracce.",
        'health': "Predisposti a displasia dell'anca, problemi alle orecchie e torsione gastrica.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano e possibilità di seguire tracce.",
        'verdict': "Un segugio americano classico. Perfetti per famiglie attive con spazio.",
    },
    'bluetick-coonhound': {
        'overview': "Il Bluetick Coonhound è un segugio americano dal mantello maculato blu. Amichevole e tenace.",
        'temperament': "I Bluetick sono amichevoli, intelligenti e determinati. Sono vocali e leali.",
        'health': "Generalmente sani. Predisposti a displasia dell'anca e problemi alle orecchie.",
        'exercise': "Cani attivi che necessitano di molto esercizio e opportunità di caccia.",
        'verdict': "Un segugio blu tenace. Perfetti per cacciatori e famiglie attive.",
    },
    'redbone-coonhound': {
        'overview': "Il Redbone Coonhound è un segugio americano dal bel mantello rosso. Affettuoso e versatile.",
        'temperament': "I Redbone sono affettuosi, easygoing e determinati. Sono buoni cani da famiglia.",
        'health': "Generalmente sani. Predisposti a displasia dell'anca e problemi alle orecchie.",
        'exercise': "Cani attivi che amano l'esercizio e seguire tracce.",
        'verdict': "Un segugio rosso affettuoso. Perfetti per famiglie attive.",
    },
    'treeing-walker-coonhound': {
        'overview': "Il Treeing Walker Coonhound è un segugio veloce e intelligente. Eccelle nella caccia.",
        'temperament': "I Treeing Walker sono intelligenti, amichevoli e competitivi. Sono energici e vocali.",
        'health': "Generalmente sani. Predisposti a displasia dell'anca e problemi alle orecchie.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio.",
        'verdict': "Un segugio veloce e intelligente. Perfetti per cacciatori attivi.",
    },
    'plott-hound': {
        'overview': "Il Plott Hound è l'unico coonhound non di origine inglese. Coraggioso e determinato.",
        'temperament': "I Plott sono coraggiosi, intelligenti e leali. Sono determinati cacciatori.",
        'health': "Generalmente sani. Predisposti a displasia dell'anca e torsione gastrica.",
        'exercise': "Cani attivi che necessitano di molto esercizio e opportunità di caccia.",
        'verdict': "Un segugio coraggioso. Perfetti per cacciatori esperti.",
    },
    'american-foxhound': {
        'overview': "L'American Foxhound è un segugio americano elegante. Amichevole e indipendente.",
        'temperament': "Gli American Foxhound sono amichevoli, indipendenti e determinati. Sono vocali.",
        'health': "Generalmente sani. Predisposti a trombocitopenia e displasia dell'anca.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio.",
        'verdict': "Un segugio americano elegante. Perfetti per chi ha spazio.",
    },
    'english-foxhound': {
        'overview': "L'English Foxhound è il cugino britannico del Foxhound americano. Socievole e energico.",
        'temperament': "Gli English Foxhound sono socievoli, gentili e determinati. Amano la compagnia del branco.",
        'health': "Generalmente sani. Predisposti a displasia dell'anca e problemi renali.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio. Meglio in coppia.",
        'verdict': "Un segugio britannico socievole. Perfetti per chi ha spazio e altri cani.",
    },
    'harrier': {
        'overview': "L'Harrier è un segugio inglese di taglia media. Simile al Beagle ma più grande.",
        'temperament': "Gli Harrier sono amichevoli, allegri e determinati. Sono socievoli e energici.",
        'health': "Generalmente sani. Predisposti a displasia dell'anca e problemi alle orecchie.",
        'exercise': "Cani energici che necessitano di molto esercizio.",
        'verdict': "Un Beagle più grande. Gli Harrier sono perfetti per famiglie attive.",
    },
    'otterhound': {
        'overview': "L'Otterhound è un raro segugio britannico dal mantello ispido. Amichevole e indipendente.",
        'temperament': "Gli Otterhound sono amichevoli, allegri e indipendenti. Amano l'acqua e seguire tracce.",
        'health': "Predisposti a displasia dell'anca, torsione gastrica e trombocitopenia.",
        'exercise': "Cani attivi che amano nuotare. Necessitano di esercizio regolare.",
        'verdict': "Un segugio acquatico raro. Gli Otterhound sono per appassionati della razza.",
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
