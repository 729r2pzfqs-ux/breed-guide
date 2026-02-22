#!/usr/bin/env python3
"""Final batch - remaining breeds"""

import re
from pathlib import Path

IT_BREEDS_DIR = Path(__file__).parent.parent / 'it' / 'breeds'

BREEDS = {
    'small-munsterlander': {
        'overview': "Il Small Munsterlander è un versatile cane da caccia tedesco. Intelligente e adattabile.",
        'temperament': "I Small Munsterlander sono intelligenti, versatili e affettuosi. Ottimi cani da famiglia.",
        'health': "Generalmente sani. Predisposti a displasia dell'anca e problemi oculari.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano.",
        'verdict': "Un cacciatore tedesco compatto. Perfetti per famiglie attive.",
    },
    'pudelpointer': {
        'overview': "Il Pudelpointer è un versatile cane da caccia tedesco. Intelligente e resistente.",
        'temperament': "I Pudelpointer sono intelligenti, calmi e versatili. Sono eccellenti cacciatori.",
        'health': "Generalmente sani. Predisposti a displasia dell'anca.",
        'exercise': "Cani attivi che necessitano di molto esercizio e lavoro.",
        'verdict': "Un cacciatore tedesco versatile. Per cacciatori attivi.",
    },
    'irish-terrier': {
        'overview': "L'Irish Terrier è un coraggioso terrier irlandese. Leale e protettivo.",
        'temperament': "Gli Irish Terrier sono coraggiosi, leali e giocosi. Sono buoni cani da guardia.",
        'health': "Generalmente sani. Predisposti a cistinuria e problemi cutanei.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano.",
        'verdict': "Un terrier irlandese coraggioso. Perfetti per famiglie attive.",
    },
    'glen-of-imaal-terrier': {
        'overview': "Il Glen of Imaal Terrier è un robusto terrier irlandese. Coraggioso e tranquillo.",
        'temperament': "I Glen sono coraggiosi, gentili e tranquilli. Meno energici di altri terrier.",
        'health': "Predisposti a atrofia retinica progressiva e displasia dell'anca.",
        'exercise': "Cani moderatamente attivi. Più tranquilli di altri terrier.",
        'verdict': "Un terrier irlandese calmo. Perfetti per chi cerca un terrier più tranquillo.",
    },
    'sealyham-terrier': {
        'overview': "Il Sealyham Terrier è un raro terrier gallese. Coraggioso e affettuoso.",
        'temperament': "I Sealyham sono coraggiosi, affettuosi e indipendenti. Sono calmi per essere terrier.",
        'health': "Predisposti a sordità, atrofia retinica progressiva e problemi oculari.",
        'exercise': "Cani moderatamente attivi. Adattabili.",
        'verdict': "Un raro terrier gallese. I Sealyham sono per appassionati della razza.",
    },
    'skye-terrier': {
        'overview': "Lo Skye Terrier è un elegante terrier scozzese. Leale e dignitoso.",
        'temperament': "Gli Skye sono leali, dignitosi e riservati. Sono devoti alla famiglia.",
        'health': "Predisposti a problemi alla schiena, ipotiroidismo e cancro.",
        'exercise': "Cani moderatamente attivi. Le passeggiate sono sufficienti.",
        'verdict': "Un terrier elegante e raro. Gli Skye sono per appassionati della razza.",
    },
    'bedlington-terrier': {
        'overview': "Il Bedlington Terrier ha l'aspetto di un agnellino. Gentile ma coraggioso.",
        'temperament': "I Bedlington sono gentili, giocosi e coraggiosi. Sono meno aggressivi di altri terrier.",
        'health': "Predisposti a tossicosi da rame, problemi oculari e renali.",
        'exercise': "Cani moderatamente attivi che amano giocare.",
        'verdict': "Un agnellino con cuore di leone. I Bedlington sono perfetti per famiglie.",
    },
    'parson-russell-terrier': {
        'overview': "Il Parson Russell Terrier è la versione più alta del Jack Russell. Energico e coraggioso.",
        'temperament': "I Parson sono energici, intelligenti e coraggiosi. Hanno molta energia.",
        'health': "Generalmente sani. Predisposti a lussazione della rotula e problemi oculari.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio.",
        'verdict': "Un Jack Russell più alto. Per proprietari molto attivi.",
    },
    'american-pit-bull-terrier': {
        'overview': "L'American Pit Bull Terrier è un cane atletico e leale. Spesso frainteso.",
        'temperament': "I Pit Bull sono affettuosi, leali e giocosi. Amano le persone e i bambini.",
        'health': "Predisposti a displasia dell'anca, allergie e problemi cardiaci.",
        'exercise': "Cani atletici che necessitano di molto esercizio.",
        'verdict': "Un atleta amorevole. I Pit Bull sono perfetti per proprietari esperti e responsabili.",
    },
    'american-bully': {
        'overview': "L'American Bully è una razza recente. Muscoloso ma affettuoso.",
        'temperament': "Gli American Bully sono affettuosi, leali e gentili. Amano la famiglia.",
        'health': "Predisposti a displasia dell'anca, problemi cutanei e cardiaci.",
        'exercise': "Cani moderatamente attivi. Non hanno bisogno di esercizio intenso.",
        'verdict': "Un muscoloso cucciolone. Gli American Bully sono perfetti per famiglie.",
    },
    'white-swiss-shepherd': {
        'overview': "Il Pastore Svizzero Bianco è un elegante cane da pastore. Gentile e versatile.",
        'temperament': "I Pastori Svizzeri Bianchi sono gentili, intelligenti e leali. Sono meno intensi dei Pastori Tedeschi.",
        'health': "Predisposti a displasia dell'anca, problemi gastrointestinali e allergie.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano.",
        'verdict': "Un pastore bianco elegante. Perfetti per famiglie attive.",
    },
    'dutch-shepherd': {
        'overview': "Il Dutch Shepherd è un versatile cane da pastore olandese. Atletico e intelligente.",
        'temperament': "I Dutch Shepherd sono intelligenti, leali e versatili. Eccellono nel lavoro.",
        'health': "Generalmente sani. Predisposti a displasia dell'anca e problemi oculari.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio e lavoro.",
        'verdict': "Un pastore olandese versatile. Per proprietari esperti attivi.",
    },
    'croatian-sheepdog': {
        'overview': "Il Croatian Sheepdog è un agile cane da pastore. Intelligente e devoto.",
        'temperament': "I Croatian Sheepdog sono intelligenti, attenti e devoti. Sono eccellenti lavoratori.",
        'health': "Generalmente sani. Razza robusta.",
        'exercise': "Cani attivi che necessitano di esercizio e lavoro.",
        'verdict': "Un pastore croato agile. Per famiglie attive.",
    },
    'kooikerhondje': {
        'overview': "Il Kooikerhondje è un allegro cane olandese. Originariamente usato per attirare anatre.",
        'temperament': "I Kooikerhondje sono allegri, intelligenti e adattabili. Sono riservati con gli estranei.",
        'health': "Predisposti a malattia di von Willebrand, cataratta e problemi renali.",
        'exercise': "Cani attivi che amano giocare e lavorare.",
        'verdict': "Un allegro olandese. I Kooikerhondje sono perfetti per famiglie attive.",
    },
    'stabyhoun': {
        'overview': "Lo Stabyhoun è un raro cane olandese versatile. Gentile e affidabile.",
        'temperament': "Gli Stabyhoun sono gentili, pazienti e versatili. Sono eccellenti cani da famiglia.",
        'health': "Predisposti a displasia dell'anca, epilessia e stenosi aortica.",
        'exercise': "Cani moderatamente attivi che amano nuotare e cacciare.",
        'verdict': "Un tesoro olandese raro. Gli Stabyhoun sono perfetti per famiglie.",
    },
    'german-pinscher': {
        'overview': "Il German Pinscher è un elegante cane tedesco. Energico e vigile.",
        'temperament': "I German Pinscher sono energici, intelligenti e vigili. Sono buoni cani da guardia.",
        'health': "Predisposti a displasia dell'anca, cataratta e malattia di von Willebrand.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano.",
        'verdict': "Un elegante tedesco. I German Pinscher sono perfetti per proprietari attivi.",
    },
    'austrian-pinscher': {
        'overview': "L'Austrian Pinscher è un robusto cane da fattoria austriaco. Vigile e affettuoso.",
        'temperament': "Gli Austrian Pinscher sono vigili, giocosi e affettuosi. Sono buoni cani da guardia.",
        'health': "Generalmente sani. Predisposti a problemi cardiaci.",
        'exercise': "Cani attivi che necessitano di esercizio e lavoro.",
        'verdict': "Un robusto cane austriaco. Per famiglie attive.",
    },
    'hovawart': {
        'overview': "L'Hovawart è un antico cane da guardia tedesco. Versatile e devoto.",
        'temperament': "Gli Hovawart sono intelligenti, leali e protettivi. Sono eccellenti cani da famiglia.",
        'health': "Predisposti a displasia dell'anca e ipotiroidismo.",
        'exercise': "Cani attivi che necessitano di esercizio e stimolazione mentale.",
        'verdict': "Un guardiano tedesco versatile. Gli Hovawart sono perfetti per famiglie.",
    },
    'eurasier': {
        'overview': "L'Eurasier è un cane tedesco recente. Calmo e affettuoso.",
        'temperament': "Gli Eurasier sono calmi, riservati e affettuosi. Sono devoti alla famiglia.",
        'health': "Predisposti a displasia dell'anca, lussazione della rotula e problemi oculari.",
        'exercise': "Cani moderatamente attivi. Adattabili.",
        'verdict': "Un cane tedesco equilibrato. Gli Eurasier sono perfetti per famiglie.",
    },
    'tornjak': {
        'overview': "Il Tornjak è un antico cane da guardia bosniaco-croato. Potente e calmo.",
        'temperament': "I Tornjak sono calmi, protettivi e leali. Sono guardiani naturali.",
        'health': "Generalmente sani. Predisposti a displasia dell'anca.",
        'exercise': "Cani moderatamente attivi che amano avere un territorio.",
        'verdict': "Un guardiano balcanico. I Tornjak sono per chi ha spazio.",
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
