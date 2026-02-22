#!/usr/bin/env python3
"""Batch 6 Italian breed translations"""

import re
from pathlib import Path

IT_BREEDS_DIR = Path(__file__).parent.parent / 'it' / 'breeds'

BREEDS = {
    'affenpinscher': {
        'overview': "L'Affenpinscher, il 'cane scimmia', è un piccolo terrier tedesco dal carattere grande. Coraggioso e divertente, è un compagno unico.",
        'temperament': "Gli Affenpinscher sono curiosi, coraggiosi e divertenti. Hanno personalità da terrier nonostante le piccole dimensioni.",
        'health': "Predisposti a lussazione della rotula, problemi cardiaci e respiratori. Generalmente sani.",
        'exercise': "Cani moderatamente attivi. Brevi passeggiate e giochi in casa sono sufficienti.",
        'verdict': "Un piccolo comico coraggioso. Gli Affenpinscher sono perfetti per chi cerca un compagno divertente.",
    },
    'brussels-griffon': {
        'overview': "Il Griffone di Bruxelles è un piccolo cane belga dall'espressione quasi umana. Affettuoso e sensibile.",
        'temperament': "I Griffoni sono affettuosi, sensibili e vigili. Si legano fortemente a una persona. Possono essere timidi.",
        'health': "Predisposti a problemi respiratori, lussazione della rotula e problemi oculari.",
        'exercise': "Cani a bassa energia. Brevi passeggiate sono sufficienti. Perfetti per appartamenti.",
        'verdict': "Un piccolo cane con espressione umana. I Griffoni sono perfetti per chi cerca un compagno devoto.",
    },
    'toy-fox-terrier': {
        'overview': "Il Toy Fox Terrier è un piccolo terrier americano vivace e intelligente. Atletico nonostante le dimensioni.",
        'temperament': "I Toy Fox Terrier sono vivaci, intelligenti e coraggiosi. Sono leali e amano la famiglia.",
        'health': "Predisposti a lussazione della rotula, malattia di Legg-Calvé-Perthes e allergie.",
        'exercise': "Cani attivi che amano giocare. Si adattano bene agli appartamenti.",
        'verdict': "Un terrier in miniatura. I Toy Fox sono perfetti per chi cerca un compagno vivace e portatile.",
    },
    'japanese-chin': {
        'overview': "Il Chin Giapponese è un elegante cane da compagnia aristocratico. Gentile e riservato, ha modi felini.",
        'temperament': "I Chin sono gentili, riservati e affettuosi. Sono indipendenti e puliti come i gatti.",
        'health': "Predisposti a problemi cardiaci, lussazione della rotula e problemi respiratori.",
        'exercise': "Cani a bassa energia. Brevi passeggiate e giochi leggeri. Perfetti per appartamenti.",
        'verdict': "Un aristocratico giapponese. I Chin sono perfetti per chi cerca un compagno elegante e tranquillo.",
    },
    'chinese-crested': {
        'overview': "Il Cane Crestato Cinese esiste in due varietà: nudo e powder puff. Affettuoso e giocoso.",
        'temperament': "I Crestati Cinesi sono affettuosi, giocosi e allegri. Amano stare con le persone.",
        'health': "La varietà nuda richiede protezione solare e cure cutanee. Predisposti a problemi dentali.",
        'exercise': "Cani moderatamente attivi. Si adattano bene agli appartamenti.",
        'verdict': "Un cane unico e affettuoso. I Crestati Cinesi sono perfetti per chi cerca un compagno distintivo.",
    },
    'silky-terrier': {
        'overview': "Il Silky Terrier australiano ha un magnifico mantello setoso. Vivace e affettuoso.",
        'temperament': "I Silky Terrier sono vivaci, curiosi e affettuosi. Hanno personalità da terrier.",
        'health': "Predisposti a lussazione della rotula, collasso della trachea e problemi oculari.",
        'exercise': "Cani attivi che amano giocare. Si adattano agli appartamenti con sufficiente esercizio.",
        'verdict': "Un terrier setoso e vivace. I Silky sono perfetti per chi cerca un compagno elegante e attivo.",
    },
    'english-toy-spaniel': {
        'overview': "L'English Toy Spaniel è un cane da compagnia aristocratico. Gentile e riservato.",
        'temperament': "Gli English Toy Spaniel sono gentili, affettuosi e tranquilli. Amano le coccole e la calma.",
        'health': "Predisposti a problemi cardiaci, lussazione della rotula e problemi respiratori.",
        'exercise': "Cani a bassa energia. Brevi passeggiate sono sufficienti. Molto adattabili.",
        'verdict': "Un compagno aristocratico e tranquillo. Perfetti per chi cerca un cane calmo e affettuoso.",
    },
    'miniature-pinscher': {
        'overview': "Il Pinscher Nano è un piccolo cane tedesco pieno di energia. Conosciuto come 'Re dei Toy'.",
        'temperament': "I Min Pin sono energici, curiosi e coraggiosi. Hanno personalità enorme. Possono essere testardi.",
        'health': "Predisposti a lussazione della rotula, malattia di Legg-Calvé-Perthes e problemi cardiaci.",
        'exercise': "Cani molto attivi che amano giocare e esplorare. Necessitano supervisione.",
        'verdict': "Il Re dei Toy. I Pinscher Nano sono perfetti per chi cerca un piccolo cane con grande personalità.",
    },
    'rat-terrier': {
        'overview': "Il Rat Terrier è un terrier americano versatile. Intelligente e affettuoso.",
        'temperament': "I Rat Terrier sono intelligenti, vivaci e affettuosi. Sono meno testardi di altri terrier.",
        'health': "Generalmente sani. Predisposti a lussazione della rotula, displasia dell'anca e allergie.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano. Versatili e adattabili.",
        'verdict': "Un terrier americano versatile. I Rat Terrier sono perfetti per famiglie attive.",
    },
    'manchester-terrier': {
        'overview': "Il Manchester Terrier è un elegante terrier inglese. Atletico e intelligente.",
        'temperament': "I Manchester sono intelligenti, vigili e leali. Sono meno aggressivi di altri terrier.",
        'health': "Predisposti a malattia di von Willebrand, lussazione della rotula e problemi oculari.",
        'exercise': "Cani attivi che necessitano di esercizio regolare. Adattabili.",
        'verdict': "Un terrier elegante. I Manchester sono perfetti per chi cerca un compagno atletico e raffinato.",
    },
    'italian-greyhound': {
        'overview': "Il Piccolo Levriero Italiano è la versione miniatura del Greyhound. Elegante e affettuoso.",
        'temperament': "I Piccoli Levrieri sono affettuosi, giocosi e sensibili. Amano le coccole e il comfort.",
        'health': "Predisposti a fratture ossee, problemi dentali, epilessia. Le ossa fragili richiedono attenzione.",
        'exercise': "Cani che amano correre ma si accontentano di giochi in casa. Sensibili al freddo.",
        'verdict': "Eleganza in miniatura. Perfetti per chi cerca un compagno affettuoso e raffinato.",
    },
    'toy-poodle': {
        'overview': "Il Barboncino Toy è la versione più piccola del Barboncino. Intelligente e affettuoso.",
        'temperament': "I Toy Poodle sono intelligenti, allegri e affettuosi. Eccellono nell'obbedienza.",
        'health': "Predisposti a lussazione della rotula, problemi oculari, epilessia e problemi dentali.",
        'exercise': "Cani moderatamente attivi che amano giocare e imparare trucchi.",
        'verdict': "Intelligenza in formato tascabile. I Toy Poodle sono perfetti per chi cerca un compagno brillante.",
    },
    'miniature-poodle': {
        'overview': "Il Barboncino Miniatura è la taglia media dei Barboncini. Versatile e intelligente.",
        'temperament': "I Miniature Poodle sono intelligenti, attivi e affettuosi. Eccellono in molte attività.",
        'health': "Predisposti a problemi oculari, epilessia, displasia dell'anca e malattia di Addison.",
        'exercise': "Cani attivi che necessitano di esercizio e stimolazione mentale regolari.",
        'verdict': "Il Barboncino versatile. I Miniature sono perfetti per famiglie attive.",
    },
    'löwchen': {
        'overview': "Il Löwchen, 'piccolo leone', è un raro cane da compagnia. Allegro e affettuoso.",
        'temperament': "I Löwchen sono allegri, affettuosi e giocosi. Amano le persone e si adattano bene.",
        'health': "Generalmente sani. Predisposti a lussazione della rotula e atrofia retinica progressiva.",
        'exercise': "Cani moderatamente attivi che amano giocare. Adattabili.",
        'verdict': "Un piccolo leone raro. I Löwchen sono perfetti per chi cerca un compagno allegro e unico.",
    },
    'coton-de-tulear': {
        'overview': "Il Coton de Tuléar è il cane nazionale del Madagascar. Dal mantello soffice come cotone.",
        'temperament': "I Coton sono allegri, affettuosi e giocosi. Amano stare con le persone. Molto adattabili.",
        'health': "Generalmente sani. Predisposti a lussazione della rotula, displasia dell'anca e problemi oculari.",
        'exercise': "Cani moderatamente attivi che amano giocare. Si adattano bene agli appartamenti.",
        'verdict': "Un batuffolo di cotone allegro. I Coton sono perfetti per famiglie che cercano un compagno gioioso.",
    },
    'bolognese': {
        'overview': "Il Bolognese è un antico cane da compagnia italiano. Affettuoso e devoto.",
        'temperament': "I Bolognese sono affettuosi, calmi e devoti. Si legano fortemente alla famiglia.",
        'health': "Generalmente sani. Predisposti a lussazione della rotula e problemi oculari.",
        'exercise': "Cani a bassa energia. Brevi passeggiate e giochi sono sufficienti.",
        'verdict': "Un tesoro italiano. I Bolognese sono perfetti per chi cerca un compagno calmo e devoto.",
    },
    'biewer-terrier': {
        'overview': "Il Biewer Terrier è una razza tedesca recente derivata dallo Yorkshire. Elegante e giocoso.",
        'temperament': "I Biewer sono giocosi, affettuosi e vivaci. Amano la famiglia e sono adattabili.",
        'health': "Predisposti a problemi gastrointestinali, lussazione della rotula e problemi dentali.",
        'exercise': "Cani moderatamente attivi che amano giocare. Perfetti per appartamenti.",
        'verdict': "Uno Yorkshire tricolore. I Biewer sono perfetti per chi cerca un piccolo compagno elegante.",
    },
    'australian-terrier': {
        'overview': "L'Australian Terrier è un robusto terrier australiano. Coraggioso e affettuoso.",
        'temperament': "Gli Australian Terrier sono coraggiosi, leali e vivaci. Sono buoni cani da guardia.",
        'health': "Generalmente sani. Predisposti a lussazione della rotula, diabete e allergie.",
        'exercise': "Cani attivi che amano esplorare. Adattabili a vari stili di vita.",
        'verdict': "Un terrier robusto dall'Australia. Perfetti per chi cerca un compagno coraggioso e leale.",
    },
    'cesky-terrier': {
        'overview': "Il Cesky Terrier è un raro terrier ceco. Calmo e affettuoso rispetto ad altri terrier.",
        'temperament': "I Cesky sono calmi, affettuosi e giocosi. Sono meno aggressivi di altri terrier.",
        'health': "Predisposti a sindrome di Scottie cramp, problemi oculari e cardiaci.",
        'exercise': "Cani moderatamente attivi. Si adattano bene a vari stili di vita.",
        'verdict': "Un terrier ceco unico. I Cesky sono perfetti per chi cerca un terrier più calmo.",
    },
    'dandie-dinmont-terrier': {
        'overview': "Il Dandie Dinmont Terrier è un terrier scozzese dall'aspetto unico. Coraggioso e indipendente.",
        'temperament': "I Dandie Dinmont sono coraggiosi, indipendenti e affettuosi. Sono calmi in casa.",
        'health': "Predisposti a problemi alla schiena, glaucoma e epilessia.",
        'exercise': "Cani moderatamente attivi. Passeggiate regolari sono sufficienti.",
        'verdict': "Un terrier unico e affascinante. I Dandie sono perfetti per chi apprezza le razze rare.",
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
