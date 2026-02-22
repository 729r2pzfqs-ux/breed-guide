#!/usr/bin/env python3
"""Batch 5 Italian breed translations - More Terriers and Working Dogs"""

import re
from pathlib import Path

IT_BREEDS_DIR = Path(__file__).parent.parent / 'it' / 'breeds'

BREEDS = {
    'norfolk-terrier': {
        'overview': "Il Norfolk Terrier è uno dei più piccoli terrier da lavoro. Vivace e coraggioso, è un compagno allegro.",
        'temperament': "I Norfolk Terrier sono coraggiosi, affettuosi e vivaci. Hanno la tipica personalità terrier. Amano la compagnia.",
        'health': "Predisposti a lussazione della rotula, displasia dell'anca e problemi cardiaci.",
        'exercise': "Cani attivi che amano giocare. Si adattano bene agli appartamenti con sufficiente esercizio.",
        'verdict': "Un piccolo terrier dal grande cuore. I Norfolk sono perfetti per chi cerca un compagno vivace.",
    },
    'norwich-terrier': {
        'overview': "Il Norwich Terrier è simile al Norfolk ma con orecchie erette. Vivace e affettuoso, è un compagno devoto.",
        'temperament': "I Norwich Terrier sono coraggiosi, affettuosi e intelligenti. Sono socievoli e amano la famiglia.",
        'health': "Predisposti a problemi respiratori, lussazione della rotula e epilessia.",
        'exercise': "Cani attivi che amano giocare. Adattabili alla vita in appartamento.",
        'verdict': "Un terrier vivace con orecchie da elfo. I Norwich sono perfetti per famiglie attive.",
    },
    'cairn-terrier': {
        'overview': "Il Cairn Terrier è un robusto terrier scozzese, famoso come Toto nel Mago di Oz. Vivace e indipendente.",
        'temperament': "I Cairn Terrier sono coraggiosi, vivaci e indipendenti. Amano esplorare e scavare. Sono leali.",
        'health': "Predisposti a lussazione della rotula, allergie cutanee e problemi oculari.",
        'exercise': "Cani attivi che amano esplorare. Si adattano bene agli appartamenti.",
        'verdict': "Un terrier avventuroso. I Cairn sono perfetti per chi cerca un compagno intraprendente.",
    },
    'border-terrier': {
        'overview': "Il Border Terrier è un terrier affettuoso e adattabile. Originariamente un cacciatore di volpi, oggi è un amato compagno.",
        'temperament': "I Border Terrier sono affettuosi, intelligenti e giocosi. Sono meno aggressivi di altri terrier.",
        'health': "Generalmente sani. Predisposti a displasia dell'anca, problemi cardiaci e epilessia.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano. Adattabili.",
        'verdict': "Un terrier equilibrato. I Border sono perfetti per famiglie che cercano un compagno adattabile.",
    },
    'fox-terrier-smooth': {
        'overview': "Il Fox Terrier a Pelo Liscio è un terrier elegante e vivace. Originariamente cacciatore di volpi, è un compagno energico.",
        'temperament': "I Fox Terrier sono vivaci, coraggiosi e intelligenti. Hanno molta energia e amano giocare.",
        'health': "Predisposti a sordità, lussazione della rotula e displasia dell'anca.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio e stimolazione.",
        'verdict': "Un terrier elegante ed energico. I Fox Terrier sono perfetti per proprietari attivi.",
    },
    'wire-fox-terrier': {
        'overview': "Il Fox Terrier a Pelo Ruvido è la versione dal mantello ispido del Fox Terrier. Elegante e vivace.",
        'temperament': "I Wire Fox Terrier sono vivaci, indipendenti e coraggiosi. Sono intelligenti e giocherelloni.",
        'health': "Predisposti a sordità, lussazione della rotula, displasia dell'anca e problemi cutanei.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio. Amano giocare.",
        'verdict': "Un terrier ispido ed elegante. I Wire Fox sono perfetti per chi ama i cani vivaci.",
    },
    'lakeland-terrier': {
        'overview': "Il Lakeland Terrier è un terrier robusto originario dell'Inghilterra. Coraggioso e amichevole.",
        'temperament': "I Lakeland sono coraggiosi, amichevoli e sicuri di sé. Sono meno aggressivi di altri terrier.",
        'health': "Generalmente sani. Predisposti a problemi oculari e allergie cutanee.",
        'exercise': "Cani attivi che amano esplorare. Adattabili a vari stili di vita.",
        'verdict': "Un terrier equilibrato. I Lakeland sono perfetti per famiglie che cercano un compagno robusto.",
    },
    'welsh-terrier': {
        'overview': "Il Welsh Terrier è un terrier vivace dal mantello nero focato. Amichevole e intelligente.",
        'temperament': "I Welsh Terrier sono vivaci, amichevoli e intelligenti. Sono meno indipendenti di altri terrier.",
        'health': "Generalmente sani. Predisposti a allergie, problemi oculari e epilessia.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano. Adattabili.",
        'verdict': "Un terrier amichevole. I Welsh sono perfetti per famiglie attive.",
    },
    'soft-coated-wheaten-terrier': {
        'overview': "Il Soft Coated Wheaten Terrier ha un magnifico mantello setoso color grano. Affettuoso e giocoso.",
        'temperament': "I Wheaten sono affettuosi, giocosi e allegri. Sono meno aggressivi di altri terrier e amano tutti.",
        'health': "Predisposti a nefropatia proteino-disperdente, enteropatia e allergie.",
        'exercise': "Cani moderatamente attivi che amano giocare. Adattabili.",
        'verdict': "Un terrier setoso e affettuoso. I Wheaten sono perfetti per famiglie.",
    },
    'kerry-blue-terrier': {
        'overview': "Il Kerry Blue Terrier è un terrier irlandese dal distintivo mantello blu-grigio. Versatile e coraggioso.",
        'temperament': "I Kerry Blue sono coraggiosi, intelligenti e leali. Possono essere aggressivi con altri cani.",
        'health': "Predisposti a problemi oculari, displasia dell'anca, ipotiroidismo e cisti.",
        'exercise': "Cani attivi che necessitano di esercizio regolare. Versatili.",
        'verdict': "Un terrier irlandese versatile. I Kerry Blue sono perfetti per proprietari esperti.",
    },
    'giant-schnauzer': {
        'overview': "Lo Schnauzer Gigante è la versione più grande della famiglia Schnauzer. Potente e intelligente, è un guardiano eccellente.",
        'temperament': "Gli Schnauzer Giganti sono intelligenti, leali e territoriali. Sono protettivi e devoti alla famiglia.",
        'health': "Predisposti a displasia dell'anca, torsione gastrica, ipotiroidismo e cancro.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio e lavoro mentale.",
        'verdict': "Un guardiano potente. Gli Schnauzer Giganti sono perfetti per proprietari esperti.",
    },
    'standard-schnauzer': {
        'overview': "Lo Schnauzer Standard è la versione originale della famiglia. Intelligente e versatile, è un compagno devoto.",
        'temperament': "Gli Schnauzer Standard sono intelligenti, vigili e giocosi. Sono versatili e adattabili.",
        'health': "Predisposti a displasia dell'anca, problemi oculari e ipotiroidismo.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano e stimolazione mentale.",
        'verdict': "Lo Schnauzer originale. Gli Standard sono perfetti per famiglie attive.",
    },
    'bouvier-des-flandres': {
        'overview': "Il Bouvier des Flandres è un cane da lavoro belga potente e versatile. Leale e coraggioso.",
        'temperament': "I Bouvier sono calmi, leali e protettivi. Sono intelligenti e facili da addestrare.",
        'health': "Predisposti a displasia dell'anca, problemi oculari, ipotiroidismo e torsione gastrica.",
        'exercise': "Cani attivi che necessitano di esercizio regolare. Amano lavorare.",
        'verdict': "Un lavoratore belga versatile. I Bouvier sono perfetti per proprietari esperti.",
    },
    'greater-swiss-mountain-dog': {
        'overview': "Il Grande Bovaro Svizzero è un cane da lavoro potente e affidabile. Affettuoso e leale.",
        'temperament': "I Grandi Bovari Svizzeri sono affettuosi, leali e vigili. Sono gentili con la famiglia.",
        'health': "Predisposti a displasia dell'anca, torsione gastrica, epilessia e problemi oculari.",
        'exercise': "Cani moderatamente attivi che amano lavorare. Non hanno bisogno di esercizio intenso.",
        'verdict': "Un lavoratore svizzero affidabile. I Grandi Bovari sono perfetti per famiglie con spazio.",
    },
    'entlebucher-mountain-dog': {
        'overview': "L'Entlebucher è il più piccolo dei bovari svizzeri. Energico e leale, è un compagno devoto.",
        'temperament': "Gli Entlebucher sono energici, intelligenti e leali. Sono buoni cani da guardia.",
        'health': "Predisposti a displasia dell'anca, atrofia retinica progressiva e problemi cardiaci.",
        'exercise': "Cani attivi che necessitano di molto esercizio. Amano lavorare.",
        'verdict': "Il piccolo bovaro energico. Gli Entlebucher sono perfetti per famiglie attive.",
    },
    'appenzeller-sennenhund': {
        'overview': "L'Appenzeller è un bovaro svizzero vivace e atletico. Versatile e leale.",
        'temperament': "Gli Appenzeller sono energici, intelligenti e leali. Sono vigili e possono essere riservati.",
        'health': "Generalmente sani. Predisposti a displasia dell'anca e problemi oculari.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio e lavoro.",
        'verdict': "Un bovaro svizzero atletico. Gli Appenzeller sono perfetti per proprietari attivi.",
    },
    'smooth-collie': {
        'overview': "Lo Smooth Collie è la versione a pelo corto del Collie. Elegante e intelligente.",
        'temperament': "Gli Smooth Collie sono gentili, intelligenti e leali. Sono eccellenti con i bambini.",
        'health': "Predisposti a anomalia dell'occhio del Collie, epilessia e sensibilità ai farmaci.",
        'exercise': "Cani moderatamente attivi che amano giocare. Adattabili.",
        'verdict': "Un Collie elegante a pelo corto. Gli Smooth sono perfetti per famiglie.",
    },
    'rough-collie': {
        'overview': "Il Rough Collie è famoso come Lassie. Elegante e intelligente, è un compagno devoto.",
        'temperament': "I Rough Collie sono gentili, intelligenti e leali. Sono eccellenti con i bambini e sensibili.",
        'health': "Predisposti a anomalia dell'occhio del Collie, epilessia e sensibilità ai farmaci.",
        'exercise': "Cani moderatamente attivi che amano giocare. Il mantello richiede cure.",
        'verdict': "Il leggendario Lassie. I Rough Collie sono perfetti per famiglie che cercano un compagno devoto.",
    },
    'old-english-sheepdog': {
        'overview': "L'Old English Sheepdog è un cane da pastore dal magnifico mantello. Giocoso e affettuoso.",
        'temperament': "Gli Old English Sheepdog sono giocosi, gentili e intelligenti. Amano la famiglia e i bambini.",
        'health': "Predisposti a displasia dell'anca, ipotiroidismo, atrofia retinica e sordità.",
        'exercise': "Cani moderatamente attivi. Il mantello richiede molta cura.",
        'verdict': "Un cane da pastore peloso e giocoso. Gli OES sono perfetti per famiglie con tempo per la toelettatura.",
    },
    'bearded-collie': {
        'overview': "Il Bearded Collie è un cane da pastore scozzese dal magnifico mantello. Allegro e vivace.",
        'temperament': "I Bearded Collie sono allegri, vivaci e affettuosi. Sono giocosi e amano la famiglia.",
        'health': "Predisposti a displasia dell'anca, ipotiroidismo, addisonian e allergie.",
        'exercise': "Cani attivi che amano giocare. Il mantello richiede cure regolari.",
        'verdict': "Un cane da pastore allegro. I Bearded Collie sono perfetti per famiglie attive.",
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
