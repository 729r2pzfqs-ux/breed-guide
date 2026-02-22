#!/usr/bin/env python3
"""Batch 10 - Final breeds"""

import re
from pathlib import Path

IT_BREEDS_DIR = Path(__file__).parent.parent / 'it' / 'breeds'

BREEDS = {
    'swedish-vallhund': {
        'overview': "Il Swedish Vallhund è un antico cane da pastore vichingo. Energico e versatile.",
        'temperament': "I Vallhund sono energici, intelligenti e allegri. Sono eccellenti cani da famiglia.",
        'health': "Predisposti a retinopatia, displasia dell'anca e problemi alla schiena.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano e stimolazione.",
        'verdict': "Un vichingo in miniatura. I Vallhund sono perfetti per famiglie attive.",
    },
    'icelandic-sheepdog': {
        'overview': "L'Icelandic Sheepdog è l'unica razza nativa dell'Islanda. Allegro e affettuoso.",
        'temperament': "Gli Icelandic sono allegri, amichevoli e attivi. Sono vocali e amano la famiglia.",
        'health': "Predisposti a displasia dell'anca e problemi oculari.",
        'exercise': "Cani attivi che amano giocare e lavorare.",
        'verdict': "Un tesoro islandese. Gli Icelandic sono perfetti per famiglie.",
    },
    'norwegian-buhund': {
        'overview': "Il Norwegian Buhund è un versatile cane da fattoria norvegese. Energico e affettuoso.",
        'temperament': "I Buhund sono energici, affettuosi e intelligenti. Sono vocali e giocosi.",
        'health': "Predisposti a displasia dell'anca, cataratta e problemi oculari.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano.",
        'verdict': "Un cane norvegese versatile. I Buhund sono perfetti per famiglie attive.",
    },
    'cardigan-welsh-corgi': {
        'overview': "Il Cardigan Welsh Corgi è il cugino con la coda del Pembroke. Versatile e affettuoso.",
        'temperament': "I Cardigan sono intelligenti, affettuosi e adattabili. Sono meno energici dei Pembroke.",
        'health': "Predisposti a problemi alla schiena, displasia dell'anca e atrofia retinica.",
        'exercise': "Cani attivi che necessitano di esercizio moderato.",
        'verdict': "Il Corgi con la coda. I Cardigan sono perfetti per famiglie.",
    },
    'belgian-tervuren': {
        'overview': "Il Tervuren Belga è un elegante cane da pastore. Intelligente e atletico.",
        'temperament': "I Tervuren sono intelligenti, vigili e protettivi. Eccellono nello sport.",
        'health': "Predisposti a displasia dell'anca, epilessia e problemi oculari.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio e lavoro.",
        'verdict': "Un pastore belga elegante. I Tervuren sono per proprietari esperti attivi.",
    },
    'belgian-laekenois': {
        'overview': "Il Laekenois Belga è il più raro dei pastori belgi. Robusto e protettivo.",
        'temperament': "I Laekenois sono intelligenti, vigili e protettivi. Sono riservati ma leali.",
        'health': "Predisposti a displasia dell'anca, epilessia e problemi oculari.",
        'exercise': "Cani attivi che necessitano di esercizio e lavoro.",
        'verdict': "Il più raro pastore belga. I Laekenois sono per appassionati della razza.",
    },
    'belgian-sheepdog': {
        'overview': "Il Groenendael (Belgian Sheepdog) è un elegante pastore nero. Intelligente e versatile.",
        'temperament': "I Groenendael sono intelligenti, leali e protettivi. Eccellono nel lavoro.",
        'health': "Predisposti a displasia dell'anca, epilessia e problemi oculari.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio.",
        'verdict': "Un pastore belga nero elegante. Per proprietari esperti.",
    },
    'german-spitz': {
        'overview': "Il German Spitz è un allegro cane tedesco. Vivace e affettuoso.",
        'temperament': "I German Spitz sono vivaci, vigili e affettuosi. Sono buoni cani da guardia.",
        'health': "Predisposti a lussazione della rotula, problemi oculari e epilessia.",
        'exercise': "Cani moderatamente attivi che amano giocare.",
        'verdict': "Un piccolo tedesco allegro. I German Spitz sono perfetti per famiglie.",
    },
    'japanese-spitz': {
        'overview': "Il Japanese Spitz è un elegante cane bianco. Allegro e affettuoso.",
        'temperament': "I Japanese Spitz sono allegri, intelligenti e affettuosi. Amano la famiglia.",
        'health': "Generalmente sani. Predisposti a lussazione della rotula e lacrimazione.",
        'exercise': "Cani moderatamente attivi che amano giocare.",
        'verdict': "Un elegante Spitz bianco. Perfetti per famiglie che cercano bellezza e allegria.",
    },
    'schipperke': {
        'overview': "Lo Schipperke è un piccolo cane belga nero. Curioso e coraggioso.",
        'temperament': "Gli Schipperke sono curiosi, vivaci e coraggiosi. Sono buoni cani da guardia.",
        'health': "Predisposti a MPS IIIB, lussazione della rotula e problemi oculari.",
        'exercise': "Cani attivi che amano esplorare. Adattabili.",
        'verdict': "Un piccolo capitano belga. Gli Schipperke sono perfetti per chi cerca carattere.",
    },
    'english-setter': {
        'overview': "L'English Setter è un elegante cane da caccia. Gentile e affettuoso.",
        'temperament': "Gli English Setter sono gentili, amichevoli e calmi. Sono eccellenti con i bambini.",
        'health': "Predisposti a displasia dell'anca, sordità, ipotiroidismo e allergie.",
        'exercise': "Cani attivi che amano correre. Necessitano di esercizio quotidiano.",
        'verdict': "Un gentiluomo elegante. Gli English Setter sono perfetti per famiglie.",
    },
    'gordon-setter': {
        'overview': "Il Gordon Setter è un elegante setter scozzese. Leale e atletico.",
        'temperament': "I Gordon sono leali, intelligenti e affettuosi. Sono più riservati degli altri setter.",
        'health': "Predisposti a displasia dell'anca, torsione gastrica e ipotiroidismo.",
        'exercise': "Cani attivi che necessitano di molto esercizio.",
        'verdict': "Un setter scozzese leale. I Gordon sono perfetti per famiglie attive.",
    },
    'irish-red-and-white-setter': {
        'overview': "L'Irish Red and White Setter è l'antenato del Setter Irlandese. Atletico e affettuoso.",
        'temperament': "Sono energici, amichevoli e affettuosi. Sono eccellenti cani da caccia e da famiglia.",
        'health': "Predisposti a displasia dell'anca, atrofia retinica e problemi oculari.",
        'exercise': "Cani attivi che necessitano di molto esercizio.",
        'verdict': "Un setter elegante e atletico. Perfetti per famiglie attive.",
    },
    'spinone-italiano': {
        'overview': "Lo Spinone Italiano è un antico cane da caccia italiano. Gentile e versatile.",
        'temperament': "Gli Spinoni sono gentili, pazienti e affettuosi. Sono eccellenti con i bambini.",
        'health': "Predisposti a displasia dell'anca, atassia cerebellare e ipotiroidismo.",
        'exercise': "Cani moderatamente attivi che amano cacciare e nuotare.",
        'verdict': "Un cacciatore italiano gentile. Gli Spinoni sono perfetti per famiglie.",
    },
    'bracco-italiano': {
        'overview': "Il Bracco Italiano è uno dei più antichi cani da ferma. Elegante e affettuoso.",
        'temperament': "I Bracchi sono gentili, intelligenti e affettuosi. Sono eccellenti con la famiglia.",
        'health': "Predisposti a displasia dell'anca, entropion e problemi alle orecchie.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano.",
        'verdict': "Un classico italiano elegante. I Bracchi sono perfetti per famiglie attive.",
    },
    'wirehaired-pointing-griffon': {
        'overview': "Il Wirehaired Pointing Griffon è un versatile cane da caccia. Affettuoso e adattabile.",
        'temperament': "I Griffon sono affettuosi, intelligenti e versatili. Sono eccellenti con la famiglia.",
        'health': "Predisposti a displasia dell'anca, problemi oculari e ipotiroidismo.",
        'exercise': "Cani attivi che amano cacciare e nuotare.",
        'verdict': "Un cacciatore versatile. I Griffon sono perfetti per famiglie attive.",
    },
    'wirehaired-vizsla': {
        'overview': "Il Wirehaired Vizsla è la versione a pelo ruvido del Vizsla. Versatile e affettuoso.",
        'temperament': "I Wirehaired Vizsla sono affettuosi, energici e leali. Sono eccellenti compagni.",
        'health': "Predisposti a displasia dell'anca, epilessia e allergie.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio.",
        'verdict': "Un Vizsla robusto. I Wirehaired Vizsla sono perfetti per cacciatori e atleti.",
    },
    'german-wirehaired-pointer': {
        'overview': "Il German Wirehaired Pointer è un cacciatore tedesco versatile. Determinato e affettuoso.",
        'temperament': "I GWP sono determinati, intelligenti e affettuosi. Sono versatili cacciatori.",
        'health': "Predisposti a displasia dell'anca, cancro e ipotiroidismo.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio e lavoro.",
        'verdict': "Un cacciatore tedesco versatile. I GWP sono per cacciatori attivi.",
    },
    'german-longhaired-pointer': {
        'overview': "Il German Longhaired Pointer è un elegante cacciatore tedesco. Versatile e gentile.",
        'temperament': "I GLP sono gentili, intelligenti e versatili. Sono affettuosi e calmi.",
        'health': "Predisposti a displasia dell'anca, problemi oculari e alle orecchie.",
        'exercise': "Cani attivi che amano cacciare e nuotare.",
        'verdict': "Un elegante cacciatore tedesco. I GLP sono perfetti per famiglie attive.",
    },
    'large-munsterlander': {
        'overview': "Il Large Munsterlander è un versatile cane da caccia tedesco. Elegante e affettuoso.",
        'temperament': "I Large Munsterlander sono intelligenti, affettuosi e versatili. Sono ottimi cani da famiglia.",
        'health': "Predisposti a displasia dell'anca, problemi oculari e ipotiroidismo.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano.",
        'verdict': "Un cacciatore elegante. I Large Munsterlander sono perfetti per famiglie attive.",
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
