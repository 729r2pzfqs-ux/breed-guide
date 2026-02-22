#!/usr/bin/env python3
"""Batch 9 - Remaining breeds"""

import re
from pathlib import Path

IT_BREEDS_DIR = Path(__file__).parent.parent / 'it' / 'breeds'

BREEDS = {
    'petit-basset-griffon-vendeen': {
        'overview': "Il Petit Basset Griffon Vendéen è un segugio francese allegro. Vivace e affettuoso.",
        'temperament': "I PBGV sono allegri, vivaci e indipendenti. Sono socievoli e amano la famiglia.",
        'health': "Predisposti a problemi oculari, epilessia e displasia dell'anca.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano. Amano esplorare.",
        'verdict': "Un segugio francese allegro. I PBGV sono perfetti per famiglie attive.",
    },
    'grand-basset-griffon-vendeen': {
        'overview': "Il Grand Basset Griffon Vendéen è la versione più grande del PBGV. Coraggioso e allegro.",
        'temperament': "I GBGV sono coraggiosi, allegri e indipendenti. Amano cacciare e la famiglia.",
        'health': "Predisposti a displasia dell'anca, problemi oculari e cardiaci.",
        'exercise': "Cani attivi che necessitano di molto esercizio.",
        'verdict': "Un segugio francese coraggioso. I GBGV sono perfetti per cacciatori.",
    },
    'polish-lowland-sheepdog': {
        'overview': "Il Polish Lowland Sheepdog è un cane da pastore polacco. Intelligente e adattabile.",
        'temperament': "I PON sono intelligenti, vivaci e adattabili. Possono essere indipendenti.",
        'health': "Predisposti a displasia dell'anca, atrofia retinica progressiva e ipotiroidismo.",
        'exercise': "Cani attivi che necessitano di esercizio e stimolazione mentale.",
        'verdict': "Un pastore polacco versatile. I PON sono perfetti per famiglie attive.",
    },
    'bergamasco-sheepdog': {
        'overview': "Il Pastore Bergamasco ha un mantello a corde unico. Intelligente e paziente.",
        'temperament': "I Bergamaschi sono intelligenti, pazienti e protettivi. Amano i bambini.",
        'health': "Generalmente sani. Predisposti a displasia dell'anca e problemi oculari.",
        'exercise': "Cani moderatamente attivi. Il mantello non richiede spazzolatura.",
        'verdict': "Un pastore italiano unico. I Bergamaschi sono perfetti per famiglie.",
    },
    'puli': {
        'overview': "Il Puli è un cane da pastore ungherese dal mantello a corde. Energico e intelligente.",
        'temperament': "I Puli sono energici, intelligenti e leali. Sono vigili e giocosi.",
        'health': "Predisposti a displasia dell'anca, atrofia retinica progressiva e problemi oculari.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano e stimolazione.",
        'verdict': "Un pastore ungherese unico. I Puli sono perfetti per proprietari attivi.",
    },
    'pumi': {
        'overview': "Il Pumi è un terrier ungherese dal mantello riccio. Vivace e intelligente.",
        'temperament': "I Pumi sono vivaci, intelligenti e coraggiosi. Sono vocali e vigili.",
        'health': "Generalmente sani. Predisposti a lussazione della rotula e displasia dell'anca.",
        'exercise': "Cani molto attivi che necessitano di esercizio e lavoro mentale.",
        'verdict': "Un terrier ungherese energico. I Pumi sono perfetti per proprietari attivi.",
    },
    'mudi': {
        'overview': "Il Mudi è un cane da pastore ungherese versatile. Intelligente e coraggioso.",
        'temperament': "I Mudi sono intelligenti, coraggiosi e versatili. Eccellono in molte attività.",
        'health': "Generalmente sani. Predisposti a displasia dell'anca e epilessia.",
        'exercise': "Cani molto attivi che necessitano di lavoro e stimolazione.",
        'verdict': "Un pastore ungherese versatile. I Mudi sono perfetti per sport cinofili.",
    },
    'briard': {
        'overview': "Il Briard è un cane da pastore francese dal magnifico mantello. Leale e protettivo.",
        'temperament': "I Briard sono leali, coraggiosi e affettuosi. Sono protettivi con la famiglia.",
        'health': "Predisposti a displasia dell'anca, torsione gastrica e problemi oculari.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano. Il mantello richiede cure.",
        'verdict': "Un pastore francese maestoso. I Briard sono perfetti per famiglie attive.",
    },
    'beauceron': {
        'overview': "Il Beauceron è un cane da pastore francese potente. Intelligente e versatile.",
        'temperament': "I Beauceron sono intelligenti, leali e protettivi. Richiedono un proprietario esperto.",
        'health': "Predisposti a displasia dell'anca, torsione gastrica e cardiomiopatia.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio e lavoro.",
        'verdict': "Un pastore francese potente. I Beauceron sono per proprietari esperti.",
    },
    'berger-picard': {
        'overview': "Il Berger Picard è un antico cane da pastore francese. Rustico e affettuoso.",
        'temperament': "I Picard sono allegri, intelligenti e leali. Sono adattabili e affettuosi.",
        'health': "Generalmente sani. Predisposti a displasia dell'anca e atrofia retinica.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano.",
        'verdict': "Un pastore francese rustico. I Picard sono perfetti per famiglie attive.",
    },
    'canaan-dog': {
        'overview': "Il Canaan Dog è l'antico cane di Israele. Vigile e indipendente.",
        'temperament': "I Canaan sono vigili, intelligenti e indipendenti. Sono leali ma riservati.",
        'health': "Generalmente sani. Predisposti a displasia dell'anca, ipotiroidismo e epilessia.",
        'exercise': "Cani moderatamente attivi. Adattabili a vari stili di vita.",
        'verdict': "Un cane antico e versatile. I Canaan sono perfetti per proprietari esperti.",
    },
    'thai-ridgeback': {
        'overview': "Il Thai Ridgeback è un antico cane thailandese. Indipendente e atletico.",
        'temperament': "I Thai Ridgeback sono indipendenti, intelligenti e protettivi. Richiedono socializzazione.",
        'health': "Generalmente sani. Predisposti a seno dermoide e displasia dell'anca.",
        'exercise': "Cani atletici che necessitano di esercizio regolare.",
        'verdict': "Un cane thailandese unico. Solo per proprietari esperti.",
    },
    'xoloitzcuintli': {
        'overview': "Lo Xoloitzcuintli è un antico cane messicano, spesso senza pelo. Calmo e affettuoso.",
        'temperament': "Gli Xolo sono calmi, intelligenti e affettuosi. Sono leali e riservati.",
        'health': "Generalmente sani. La varietà senza pelo richiede protezione solare e cure cutanee.",
        'exercise': "Cani moderatamente attivi. Adattabili a vari stili di vita.",
        'verdict': "Un tesoro messicano antico. Gli Xolo sono perfetti per chi cerca un cane unico.",
    },
    'peruvian-inca-orchid': {
        'overview': "Il Peruvian Inca Orchid è un antico cane peruviano, spesso senza pelo. Affettuoso e vigile.",
        'temperament': "I PIO sono affettuosi, vigili e intelligenti. Sono leali alla famiglia.",
        'health': "Generalmente sani. La varietà senza pelo richiede protezione solare.",
        'exercise': "Cani moderatamente attivi. Sensibili al freddo e al sole.",
        'verdict': "Un cane peruviano elegante. Perfetti per chi cerca un compagno unico.",
    },
    'sloughi': {
        'overview': "Lo Sloughi è un antico levriero nordafricano. Elegante e riservato.",
        'temperament': "Gli Sloughi sono riservati, dignitosi e leali. Sono affettuosi con la famiglia.",
        'health': "Generalmente sani. Sensibili agli anestetici come tutti i levrieri.",
        'exercise': "Cani che amano correre. Hanno bisogno di sprint ma sono calmi in casa.",
        'verdict': "Un levriero del deserto. Gli Sloughi sono perfetti per chi apprezza l'eleganza.",
    },
    'azawakh': {
        'overview': "L'Azawakh è un elegante levriero africano. Snello e veloce.",
        'temperament': "Gli Azawakh sono riservati, leali e indipendenti. Si legano fortemente alla famiglia.",
        'health': "Generalmente sani. Predisposti a epilessia e problemi cardiaci. Sensibili al freddo.",
        'exercise': "Cani che amano correre. Hanno bisogno di sprint regolari.",
        'verdict': "Un levriero africano elegante. Gli Azawakh sono per appassionati della razza.",
    },
    'chinook': {
        'overview': "Il Chinook è un raro cane da slitta americano. Versatile e affettuoso.",
        'temperament': "I Chinook sono affettuosi, calmi e intelligenti. Sono eccellenti cani da famiglia.",
        'health': "Predisposti a displasia dell'anca, epilessia e problemi oculari.",
        'exercise': "Cani attivi che amano lavorare e trainare.",
        'verdict': "Un cane da slitta americano raro. I Chinook sono perfetti per famiglie attive.",
    },
    'alaskan-klee-kai': {
        'overview': "L'Alaskan Klee Kai è un Husky in miniatura. Intelligente e riservato.",
        'temperament': "Gli Alaskan Klee Kai sono intelligenti, vigili e riservati. Possono essere timidi.",
        'health': "Predisposti a lussazione della rotula, problemi cardiaci e malattia della tiroide.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano.",
        'verdict': "Un piccolo Husky. Gli Alaskan Klee Kai sono perfetti per chi ama gli Husky in piccolo.",
    },
    'norwegian-lundehund': {
        'overview': "Il Norwegian Lundehund è un cane unico con sei dita per zampa. Originariamente cacciatore di pulcinelle.",
        'temperament': "I Lundehund sono allegri, curiosi e indipendenti. Sono affettuosi ma riservati.",
        'health': "Predisposti a sindrome di Lundehund (problemi gastrointestinali).",
        'exercise': "Cani attivi che amano esplorare e arrampicarsi.",
        'verdict': "Un cane unico nel suo genere. I Lundehund sono per appassionati di razze rare.",
    },
    'finnish-lapphund': {
        'overview': "Il Finnish Lapphund è un cane da pastore finlandese delle renne. Affettuoso e versatile.",
        'temperament': "I Lapphund sono affettuosi, calmi e intelligenti. Sono ottimi cani da famiglia.",
        'health': "Predisposti a atrofia retinica progressiva, cataratta e displasia dell'anca.",
        'exercise': "Cani moderatamente attivi che amano l'aria aperta.",
        'verdict': "Un pastore finlandese affettuoso. I Lapphund sono perfetti per famiglie.",
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
