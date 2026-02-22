#!/usr/bin/env python3
"""Batch 4 Italian breed translations"""

import re
from pathlib import Path

IT_BREEDS_DIR = Path(__file__).parent.parent / 'it' / 'breeds'

BREEDS_BATCH4 = {
    'chinese-shar-pei': {
        'overview': "Lo Shar Pei è un cane antico cinese dalle caratteristiche rughe. Dignitoso e indipendente, è un guardiano leale.",
        'temperament': "Gli Shar Pei sono calmi, indipendenti e leali. Possono essere diffidenti con gli estranei. Richiedono socializzazione precoce.",
        'health': "Predisposti a problemi cutanei, febbre dello Shar Pei, problemi oculari e amiloidosi. Le rughe richiedono cure.",
        'exercise': "Cani moderatamente attivi. Non tollerano il caldo e hanno bisogno di passeggiate regolari.",
        'verdict': "Un guardiano rugoso e dignitoso. Gli Shar Pei sono perfetti per proprietari esperti che cercano un cane unico.",
    },
    'chow-chow': {
        'overview': "Il Chow Chow è un cane antico dalla lingua blu e l'aspetto leonino. Dignitoso e indipendente, è devoto alla famiglia.",
        'temperament': "I Chow Chow sono dignitosi, indipendenti e leali. Possono essere distaccati con gli estranei. Sono protettivi.",
        'health': "Predisposti a displasia dell'anca, problemi oculari, ipotiroidismo e problemi cutanei. Non tollerano il caldo.",
        'exercise': "Cani a bassa energia. Passeggiate moderate sono sufficienti. Soffrono nel caldo.",
        'verdict': "Un leone dignitoso. I Chow Chow sono perfetti per proprietari esperti che apprezzano l'indipendenza.",
    },
    'lhasa-apso': {
        'overview': "Il Lhasa Apso è un antico cane tibetano da guardia. Piccolo ma coraggioso, è un compagno leale con personalità forte.",
        'temperament': "I Lhasa Apso sono indipendenti, vigili e leali. Sono buoni cani da guardia nonostante le dimensioni. Possono essere testardi.",
        'health': "Predisposti a problemi renali, problemi oculari, displasia dell'anca e allergie cutanee.",
        'exercise': "Cani a bassa energia che si accontentano di brevi passeggiate. Adatti agli appartamenti.",
        'verdict': "Un piccolo guardiano tibetano. I Lhasa Apso sono perfetti per chi cerca un compagno indipendente.",
    },
    'tibetan-terrier': {
        'overview': "Il Tibetan Terrier non è un vero terrier ma un antico cane da compagnia tibetano. Affettuoso e adattabile.",
        'temperament': "I Tibetan Terrier sono affettuosi, sensibili e adattabili. Sono devoti alla famiglia e possono essere riservati con gli estranei.",
        'health': "Predisposti a problemi oculari, displasia dell'anca, lussazione della rotula e problemi alla tiroide.",
        'exercise': "Cani moderatamente attivi che amano giocare. Adattabili a vari stili di vita.",
        'verdict': "Un compagno tibetano versatile. I Tibetan Terrier sono perfetti per famiglie che cercano un cane adattabile.",
    },
    'afghan-hound': {
        'overview': "Il Levriero Afgano è un cane elegante e aristocratico dal magnifico mantello. Dignitoso e indipendente.",
        'temperament': "I Levrieri Afgani sono dignitosi, indipendenti e affettuosi. Possono essere distaccati ma leali alla famiglia.",
        'health': "Predisposti a displasia dell'anca, cataratta, ipotiroidismo e sensibilità agli anestetici.",
        'exercise': "Cani che amano correre. Hanno bisogno di spazio per sprint ma sono calmi in casa.",
        'verdict': "Un'aristocrazia canina. I Levrieri Afgani sono perfetti per chi apprezza l'eleganza e l'indipendenza.",
    },
    'saluki': {
        'overview': "Il Saluki è uno dei cani più antichi del mondo, un levriero elegante del Medio Oriente. Nobile e riservato.",
        'temperament': "I Saluki sono gentili, dignitosi e riservati. Sono affettuosi con la famiglia ma indipendenti. Hanno forte istinto di caccia.",
        'health': "Generalmente sani ma predisposti a problemi cardiaci e sensibilità agli anestetici. Sensibili al freddo.",
        'exercise': "Cani che amano correre. Hanno bisogno di sprint regolari ma sono calmi in casa.",
        'verdict': "Un aristocratico del deserto. I Saluki sono perfetti per chi cerca un compagno elegante e riservato.",
    },
    'greyhound': {
        'overview': "Il Greyhound è il cane più veloce del mondo. Nonostante la fama di corridore, è un pantofolaio che ama rilassarsi.",
        'temperament': "I Greyhound sono gentili, tranquilli e affettuosi. Sono calmi in casa e amano le comodità. Sono sensibili.",
        'health': "Generalmente sani ma sensibili agli anestetici. Predisposti a torsione gastrica e problemi dentali.",
        'exercise': "Hanno bisogno di sprint brevi ma sono pantofolai. Perfetti per appartamenti con accesso a spazi per correre.",
        'verdict': "Un velocista pantofolaio. I Greyhound sono perfetti per chi cerca un cane tranquillo con occasionale bisogno di correre.",
    },
    'borzoi': {
        'overview': "Il Borzoi è un elegante levriero russo dall'aspetto aristocratico. Gentile e riservato, è un compagno raffinato.",
        'temperament': "I Borzoi sono gentili, dignitosi e indipendenti. Sono affettuosi con la famiglia ma riservati. Hanno forte istinto di caccia.",
        'health': "Predisposti a torsione gastrica, problemi cardiaci e sensibilità agli anestetici.",
        'exercise': "Cani che amano correre. Hanno bisogno di sprint ma sono calmi in casa.",
        'verdict': "Un aristocratico russo. I Borzoi sono perfetti per chi cerca un compagno elegante e tranquillo.",
    },
    'dalmatian': {
        'overview': "Il Dalmata è famoso per le sue macchie uniche. Atletico ed energico, è un compagno perfetto per famiglie attive.",
        'temperament': "I Dalmata sono energici, giocosi e affettuosi. Amano correre e stare con la famiglia. Possono essere testardi.",
        'health': "Predisposti a sordità, calcoli urinari, allergie cutanee e displasia dell'anca.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio. Amano correre e giocare.",
        'verdict': "Un compagno macchiato ed energico. I Dalmata sono perfetti per famiglie molto attive.",
    },
    'keeshond': {
        'overview': "Il Keeshond è un cane olandese allegro e affettuoso. Con il suo magnifico mantello grigio, è un compagno ideale.",
        'temperament': "I Keeshond sono allegri, amichevoli e intelligenti. Amano le persone e sono eccellenti cani da famiglia. Possono abbaiare.",
        'health': "Predisposti a displasia dell'anca, problemi cardiaci, ipotiroidismo e epilessia.",
        'exercise': "Cani moderatamente attivi che amano giocare. Si adattano bene a vari stili di vita.",
        'verdict': "Un sorriso olandese. I Keeshond sono perfetti per famiglie che cercano un compagno allegro e adattabile.",
    },
    'american-eskimo-dog': {
        'overview': "L'American Eskimo Dog è un bellissimo cane bianco dal mantello soffice. Intelligente e giocoso, è un compagno devoto.",
        'temperament': "Gli American Eskimo sono intelligenti, vigili e giocosi. Sono buoni cani da guardia e amano imparare trucchi.",
        'health': "Predisposti a displasia dell'anca, problemi oculari, lussazione della rotula e diabete.",
        'exercise': "Cani attivi che amano giocare. Eccellono nell'obbedienza e nell'agility.",
        'verdict': "Un bianco fiocco di neve. Gli American Eskimo sono perfetti per chi cerca un compagno intelligente e allegro.",
    },
    'finnish-spitz': {
        'overview': "Il Finnish Spitz è il cane nazionale della Finlandia. Con il suo mantello rosso e la personalità vivace, è un compagno unico.",
        'temperament': "I Finnish Spitz sono vivaci, indipendenti e vocali. Sono buoni cani da guardia e abbaiano molto. Sono leali.",
        'health': "Generalmente sani. Predisposti a displasia dell'anca, epilessia e problemi oculari.",
        'exercise': "Cani attivi che amano l'esercizio. Amano abbaiare e hanno bisogno di stimolazione.",
        'verdict': "Un cantore finlandese. I Finnish Spitz sono perfetti per chi apprezza un cane vocale e vivace.",
    },
    'norwegian-elkhound': {
        'overview': "Il Norwegian Elkhound è un antico cane nordico usato per la caccia all'alce. Robusto e leale, è un compagno devoto.",
        'temperament': "I Norwegian Elkhound sono coraggiosi, leali e indipendenti. Sono buoni cani da guardia e amano la famiglia.",
        'health': "Predisposti a displasia dell'anca, problemi oculari, ipotiroidismo e obesità.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano. Amano il freddo.",
        'verdict': "Un cacciatore nordico. I Norwegian Elkhound sono perfetti per chi cerca un compagno robusto e leale.",
    },
    'basenji': {
        'overview': "Il Basenji è il 'cane che non abbaia' dall'Africa. Invece di abbaiare, emette un suono unico chiamato yodel.",
        'temperament': "I Basenji sono indipendenti, curiosi e affettuosi. Sono puliti come i gatti e possono essere testardi.",
        'health': "Predisposti a sindrome di Fanconi, atrofia retinica progressiva, ipotiroidismo e displasia dell'anca.",
        'exercise': "Cani attivi che amano correre. Hanno forte istinto di caccia e devono essere tenuti al guinzaglio.",
        'verdict': "Un cane silenzioso e unico. I Basenji sono perfetti per chi cerca un compagno indipendente e pulito.",
    },
    'pharaoh-hound': {
        'overview': "Il Pharaoh Hound è un elegante levriero maltese che arrossisce quando è felice. Atletico e affettuoso.",
        'temperament': "I Pharaoh Hound sono affettuosi, giocosi e intelligenti. Sono gentili e amano la famiglia. Hanno forte istinto di caccia.",
        'health': "Generalmente sani. Sensibili al freddo e agli anestetici. Predisposti ad allergie.",
        'exercise': "Cani attivi che amano correre. Hanno bisogno di esercizio ma sono calmi in casa.",
        'verdict': "Un levriero che arrossisce. I Pharaoh Hound sono perfetti per chi cerca un compagno elegante e affettuoso.",
    },
    'ibizan-hound': {
        'overview': "L'Ibizan Hound è un elegante levriero spagnolo dalle grandi orecchie. Atletico e indipendente.",
        'temperament': "Gli Ibizan Hound sono eleganti, indipendenti e affettuosi. Sono giocosi e amano correre. Possono essere timidi.",
        'health': "Generalmente sani. Sensibili al freddo e agli anestetici. Predisposti a sordità e allergie.",
        'exercise': "Cani attivi che amano correre e saltare. Hanno bisogno di esercizio ma sono calmi in casa.",
        'verdict': "Un saltatore elegante. Gli Ibizan Hound sono perfetti per chi cerca un compagno atletico e affettuoso.",
    },
    'cirneco-delletna': {
        'overview': "Il Cirneco dell'Etna è un antico levriero siciliano. Elegante e affettuoso, è un compagno devoto.",
        'temperament': "I Cirneco sono affettuosi, intelligenti e indipendenti. Sono gentili e amano la famiglia. Hanno forte istinto di caccia.",
        'health': "Generalmente sani con pochi problemi genetici. Sensibili al freddo.",
        'exercise': "Cani attivi che amano correre. Hanno bisogno di esercizio ma sono calmi in casa.",
        'verdict': "Un tesoro siciliano. I Cirneco dell'Etna sono perfetti per chi cerca un compagno elegante italiano.",
    },
    'irish-wolfhound': {
        'overview': "L'Irish Wolfhound è uno dei cani più alti del mondo. Nonostante le dimensioni imponenti, è un gigante gentile.",
        'temperament': "Gli Irish Wolfhound sono gentili, pazienti e dignitosi. Amano le persone e sono eccellenti con i bambini.",
        'health': "Predisposti a cardiomiopatia, cancro osseo, torsione gastrica e displasia dell'anca. Vita breve (6-8 anni).",
        'exercise': "Cani moderatamente attivi. Hanno bisogno di spazio ma non di esercizio intenso.",
        'verdict': "Un gigante gentile. Gli Irish Wolfhound sono perfetti per chi ha spazio e vuole un compagno maestoso.",
    },
    'scottish-deerhound': {
        'overview': "Lo Scottish Deerhound è un elegante levriero scozzese. Gentile e dignitoso, è un compagno tranquillo.",
        'temperament': "Gli Scottish Deerhound sono gentili, amichevoli e dignitosi. Amano la famiglia e sono calmi in casa.",
        'health': "Predisposti a cardiomiopatia, cancro osseo, torsione gastrica e ipotiroidismo. Vita breve (8-11 anni).",
        'exercise': "Cani che amano correre ma sono calmi in casa. Hanno bisogno di sprint occasionali.",
        'verdict': "Un nobile scozzese. Gli Scottish Deerhound sono perfetti per chi cerca un compagno elegante e tranquillo.",
    },
    'english-mastiff': {
        'overview': "L'English Mastiff è uno dei cani più grandi e pesanti del mondo. Nonostante le dimensioni imponenti, è un gigante gentile.",
        'temperament': "I Mastiff sono gentili, dignitosi e protettivi. Amano la famiglia e sono pazienti con i bambini. Sbavano molto.",
        'health': "Predisposti a displasia dell'anca, torsione gastrica, problemi cardiaci e obesità. Vita breve (6-10 anni).",
        'exercise': "Cani a bassa energia. Passeggiate moderate sono sufficienti. Non tollerano il caldo.",
        'verdict': "Un colosso gentile. I Mastiff sono perfetti per chi ha spazio e vuole un guardiano paziente.",
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
    print(f"Translating {len(BREEDS_BATCH4)} breeds...")
    count = 0
    for bid, trans in BREEDS_BATCH4.items():
        if update_file(bid, trans):
            print(f"  ✓ {bid}")
            count += 1
    print(f"Done! Updated {count} files.")
