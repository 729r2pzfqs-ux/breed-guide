#!/usr/bin/env python3
"""Batch 3 Italian breed translations"""

import re
from pathlib import Path

IT_BREEDS_DIR = Path(__file__).parent.parent / 'it' / 'breeds'

BREEDS_BATCH3 = {
    'jack-russell-terrier': {
        'overview': "Il Jack Russell Terrier è un piccolo terrier energico originariamente allevato per la caccia alla volpe. Intelligente e atletico, è un cane con energia inesauribile.",
        'temperament': "I Jack Russell sono energici, intelligenti e coraggiosi. Hanno personalità enorme in un corpo piccolo. Possono essere testardi e hanno bisogno di stimolazione costante.",
        'health': "Generalmente sani ma predisposti a lussazione della rotula, sordità e problemi oculari. Hanno una lunga aspettativa di vita.",
        'exercise': "Cani ad altissima energia che necessitano di molto esercizio. Amano scavare, correre e giocare. Non adatti a proprietari sedentari.",
        'verdict': "Un piccolo vulcano di energia. I Jack Russell sono perfetti per proprietari attivi che possono fornire molto esercizio e stimolazione mentale.",
    },
    'pembroke-welsh-corgi': {
        'overview': "Il Pembroke Welsh Corgi è un cane da pastore basso e robusto, famoso come il cane preferito della Regina Elisabetta II. Intelligente e affettuoso.",
        'temperament': "I Corgi sono intelligenti, vigili e affettuosi. Sono buoni cani da guardia e abbaiano per avvisare. Possono cercare di condurre la famiglia.",
        'health': "Predisposti a problemi alla schiena, displasia dell'anca, problemi oculari e obesità. La loro struttura richiede attenzione.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano. Sono atletici nonostante le zampe corte.",
        'verdict': "Un cane da pastore in formato compatto. I Corgi sono perfetti per famiglie che cercano un compagno intelligente e affettuoso.",
    },
    'havanese': {
        'overview': "L'Havanese è il cane nazionale di Cuba, un piccolo compagno allegro e affettuoso. Con il suo mantello setoso e la personalità solare, conquista tutti.",
        'temperament': "Gli Havanese sono allegri, affettuosi e socievoli. Amano stare con le persone e si adattano bene a qualsiasi situazione. Sono ottimi cani da terapia.",
        'health': "Predisposti a lussazione della rotula, problemi oculari, sordità e displasia dell'anca. Generalmente sani.",
        'exercise': "Cani moderatamente attivi che amano giocare. Si adattano bene agli appartamenti.",
        'verdict': "Un raggio di sole cubano. Gli Havanese sono perfetti per famiglie che cercano un compagno allegro e adattabile.",
    },
    'papillon': {
        'overview': "Il Papillon prende il nome dalle sue orecchie a farfalla. Piccolo ma atletico, è uno dei cani toy più intelligenti e addestrabili.",
        'temperament': "I Papillon sono vivaci, amichevoli e intelligenti. Eccellono nell'obbedienza e nell'agility. Sono avventurosi nonostante le piccole dimensioni.",
        'health': "Predisposti a lussazione della rotula, problemi dentali e fontanella aperta. Generalmente sani con buona cura.",
        'exercise': "Cani attivi che amano giocare e imparare. Eccellono negli sport cinofili.",
        'verdict': "Una farfalla atletica. I Papillon sono perfetti per chi cerca un cane toy intelligente e addestrabile.",
    },
    'samoyed': {
        'overview': "Il Samoiedo è un cane nordico dal magnifico mantello bianco e il sorriso caratteristico. Originariamente allevato per trainare slitte e tenere calde le persone.",
        'temperament': "I Samoiedi sono amichevoli, gentili e giocosi. Amano le persone e non sono buoni cani da guardia. Possono essere vocali e testardi.",
        'health': "Predisposti a displasia dell'anca, problemi oculari, diabete e ipotiroidismo. Il mantello richiede molta cura.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano. Amano il freddo e soffrono nel caldo.",
        'verdict': "Un sorriso bianco e soffice. I Samoiedi sono perfetti per famiglie in climi freddi che cercano un compagno affettuoso.",
    },
    'alaskan-malamute': {
        'overview': "L'Alaskan Malamute è un cane da slitta potente e resistente. Più grande del Husky, è un lavoratore instancabile e un compagno leale.",
        'temperament': "I Malamute sono affettuosi, leali e giocosi. Amano le persone ma possono essere dominanti con altri cani. Hanno un forte istinto predatorio.",
        'health': "Predisposti a displasia dell'anca, problemi oculari, ipotiroidismo e polineuropatia. Richiedono cure del mantello.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio. Amano il freddo e trainare pesi.",
        'verdict': "Un atleta artico potente. I Malamute sono perfetti per proprietari esperti in climi freddi.",
    },
    'newfoundland': {
        'overview': "Il Terranova è un gigante gentile famoso per le sue capacità di salvataggio in acqua. Dolce e paziente, è un eccellente cane da famiglia.",
        'temperament': "I Terranova sono gentili, pazienti e protettivi. Amano l'acqua e i bambini. Sono naturalmente portati al salvataggio.",
        'health': "Predisposti a displasia dell'anca e del gomito, problemi cardiaci e torsione gastrica. Hanno una vita relativamente breve.",
        'exercise': "Cani moderatamente attivi che amano nuotare. Non hanno bisogno di esercizio intenso ma adorano l'acqua.",
        'verdict': "Un salvatore gentile. I Terranova sono perfetti per famiglie con spazio che cercano un compagno dolce e protettivo.",
    },
    'saint-bernard': {
        'overview': "Il San Bernardo è famoso per il salvataggio alpino. Questo gigante gentile è un compagno paziente e affettuoso, perfetto per famiglie.",
        'temperament': "I San Bernardo sono gentili, pazienti e amichevoli. Amano i bambini e sono protettivi senza essere aggressivi. Sbavano molto.",
        'health': "Predisposti a displasia dell'anca, problemi cardiaci, torsione gastrica e problemi oculari. Vita breve (8-10 anni).",
        'exercise': "Cani a bassa-media energia. Non tollerano il caldo e preferiscono climi freschi.",
        'verdict': "Un gigante dal cuore d'oro. I San Bernardo sono perfetti per famiglie con spazio che cercano un compagno paziente.",
    },
    'leonberger': {
        'overview': "Il Leonberger è un cane gigante dal magnifico mantello leonino. Gentile e giocoso, è un compagno devoto per famiglie con esperienza.",
        'temperament': "I Leonberger sono gentili, leali e giocosi. Amano l'acqua e i bambini. Sono adattabili e facili da addestrare.",
        'health': "Predisposti a displasia dell'anca, cancro osseo e problemi cardiaci. Hanno una vita breve (7-9 anni).",
        'exercise': "Cani moderatamente attivi che amano nuotare e giocare. Hanno bisogno di spazio.",
        'verdict': "Un leone gentile. I Leonberger sono perfetti per famiglie esperte con spazio che cercano un compagno maestoso.",
    },
    'irish-setter': {
        'overview': "Il Setter Irlandese è un elegante cane da caccia dal magnifico mantello rosso. Energico e affettuoso, è un compagno gioioso.",
        'temperament': "I Setter Irlandesi sono amichevoli, energici e giocosi. Maturano lentamente e rimangono cuccioli a lungo. Amano tutti.",
        'health': "Predisposti a displasia dell'anca, torsione gastrica, epilessia e problemi oculari. Generalmente sani.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio. Amano correre e giocare.",
        'verdict': "Una bellezza rossa piena di gioia. I Setter Irlandesi sono perfetti per famiglie attive che cercano un compagno entusiasta.",
    },
    'english-setter': {
        'overview': "L'English Setter è un elegante cane da caccia noto per il suo mantello maculato e la personalità gentile. Un vero gentiluomo.",
        'temperament': "Gli English Setter sono gentili, amichevoli e calmi. Amano le persone e sono eccellenti con i bambini. Sono sensibili.",
        'health': "Predisposti a displasia dell'anca, sordità, ipotiroidismo e allergie. Generalmente sani.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano. Amano correre in spazi aperti.",
        'verdict': "Un gentiluomo elegante. Gli English Setter sono perfetti per famiglie che cercano un compagno gentile e affettuoso.",
    },
    'pointer': {
        'overview': "Il Pointer è un cane da caccia atletico e elegante. Energico e devoto, è un compagno perfetto per proprietari sportivi.",
        'temperament': "I Pointer sono energici, leali e amichevoli. Amano lavorare e stare con la famiglia. Sono eccellenti atleti.",
        'health': "Predisposti a displasia dell'anca, problemi oculari, epilessia e allergie. Generalmente sani.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio. Eccellono nella caccia e negli sport.",
        'verdict': "Un atleta elegante. I Pointer sono perfetti per proprietari attivi che cercano un compagno sportivo.",
    },
    'brittany': {
        'overview': "Il Brittany è un cane da caccia versatile di taglia media. Energico e affettuoso, è un compagno eccellente per famiglie attive.",
        'temperament': "I Brittany sono energici, intelligenti e affettuosi. Amano lavorare e compiacere. Sono sensibili e rispondono bene all'addestramento positivo.",
        'health': "Predisposti a displasia dell'anca, epilessia e problemi oculari. Generalmente sani.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio. Eccellono nella caccia e nell'agility.",
        'verdict': "Un cacciatore entusiasta. I Brittany sono perfetti per famiglie attive che cercano un compagno versatile.",
    },
    'german-shorthaired-pointer': {
        'overview': "Il Bracco Tedesco a Pelo Corto è un cane da caccia versatile e atletico. Eccelle in terra e in acqua.",
        'temperament': "I Bracchi Tedeschi sono energici, intelligenti e affettuosi. Amano lavorare e stare con la famiglia. Sono eccellenti atleti.",
        'health': "Predisposti a displasia dell'anca, torsione gastrica, problemi oculari e cancro. Generalmente sani.",
        'exercise': "Cani ad altissima energia che necessitano di almeno 2 ore di esercizio al giorno.",
        'verdict': "Un atleta versatile. I Bracchi Tedeschi sono perfetti per proprietari molto attivi che cercano un compagno sportivo.",
    },
    'rhodesian-ridgeback': {
        'overview': "Il Rhodesian Ridgeback è un cane atletico originario dell'Africa, noto per la cresta di pelo sulla schiena. È un guardiano leale e un compagno devoto.",
        'temperament': "I Ridgeback sono leali, dignitosi e indipendenti. Sono protettivi ma non aggressivi. Possono essere riservati con gli estranei.",
        'health': "Predisposti a displasia dell'anca, ipotiroidismo, seno dermoide e torsione gastrica.",
        'exercise': "Cani atletici che necessitano di esercizio regolare. Sono resistenti e amano correre.",
        'verdict': "Un guardiano africano dignitoso. I Ridgeback sono perfetti per proprietari esperti che cercano un compagno leale.",
    },
    'australian-cattle-dog': {
        'overview': "Il Bovaro Australiano è un cane da lavoro intelligente e resistente. Allevato per condurre il bestiame, è energico e devoto.",
        'temperament': "I Bovari Australiani sono intelligenti, energici e leali. Possono essere riservati con gli estranei. Hanno bisogno di lavoro.",
        'health': "Predisposti a displasia dell'anca, sordità e atrofia retinica progressiva. Generalmente robusti.",
        'exercise': "Cani ad altissima energia che necessitano di molto esercizio e stimolazione mentale.",
        'verdict': "Un lavoratore instancabile. I Bovari Australiani sono perfetti per proprietari attivi che possono fornire lavoro e stimolazione.",
    },
    'belgian-malinois': {
        'overview': "Il Malinois Belga è un cane da lavoro atletico e intelligente, molto usato nelle forze dell'ordine. È un compagno devoto per proprietari esperti.",
        'temperament': "I Malinois sono intelligenti, energici e protettivi. Sono estremamente addestrabili ma hanno bisogno di lavoro costante.",
        'health': "Predisposti a displasia dell'anca e del gomito, problemi oculari e epilessia. Generalmente sani.",
        'exercise': "Cani ad altissima energia che necessitano di ore di esercizio e lavoro mentale al giorno.",
        'verdict': "Un atleta d'élite. I Malinois sono perfetti solo per proprietari molto esperti che possono fornire lavoro intenso.",
    },
    'portuguese-water-dog': {
        'overview': "Il Cane d'Acqua Portoghese è un cane atletico dal mantello riccio. Famoso per essere il cane della famiglia Obama, è un compagno allegro.",
        'temperament': "I Cani d'Acqua Portoghesi sono intelligenti, energici e affettuosi. Amano nuotare e stare con la famiglia. Sono facilmente addestrabili.",
        'health': "Predisposti a displasia dell'anca, atrofia retinica progressiva e malattia da accumulo di GM1. Generalmente sani.",
        'exercise': "Cani attivi che amano nuotare. Hanno bisogno di esercizio quotidiano e stimolazione mentale.",
        'verdict': "Un nuotatore entusiasta. I Cani d'Acqua Portoghesi sono perfetti per famiglie attive, specialmente quelle che amano l'acqua.",
    },
    'standard-poodle': {
        'overview': "Il Barbone Standard è la versione originale e più grande del Barboncino. Elegante e atletico, è uno dei cani più intelligenti al mondo.",
        'temperament': "I Barbone Standard sono intelligenti, dignitosi e giocosi. Eccellono in quasi ogni attività. Sono sensibili e si legano fortemente alla famiglia.",
        'health': "Predisposti a displasia dell'anca, torsione gastrica, epilessia e malattia di Addison. Generalmente sani.",
        'exercise': "Cani attivi che necessitano di esercizio quotidiano e stimolazione mentale. Amano nuotare.",
        'verdict': "Intelligenza e eleganza combinate. I Barbone Standard sono perfetti per chi cerca un cane versatile e ipoallergenico.",
    },
    'airedale-terrier': {
        'overview': "L'Airedale Terrier è il 'Re dei Terrier', il più grande della famiglia. Versatile e coraggioso, è un compagno leale e protettivo.",
        'temperament': "Gli Airedale sono coraggiosi, intelligenti e leali. Hanno la tipica personalità terrier ma sono più calmi dei cugini più piccoli.",
        'health': "Predisposti a displasia dell'anca, ipotiroidismo, problemi cutanei e torsione gastrica. Generalmente robusti.",
        'exercise': "Cani attivi che necessitano di esercizio regolare. Amano giocare e lavorare.",
        'verdict': "Il Re dei Terrier. Gli Airedale sono perfetti per famiglie attive che cercano un compagno versatile e coraggioso.",
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
    print(f"Translating {len(BREEDS_BATCH3)} breeds...")
    count = 0
    for bid, trans in BREEDS_BATCH3.items():
        if update_file(bid, trans):
            print(f"  ✓ {bid}")
            count += 1
    print(f"Done! Updated {count} files.")
