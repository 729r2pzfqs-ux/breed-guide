#!/usr/bin/env python3
"""
Translate breed page content to Italian
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
IT_BREEDS_DIR = BASE_DIR / 'it' / 'breeds'

# All Italian breed descriptions
ITALIAN_DESCRIPTIONS = {
    'labrador-retriever': {
        'overview': "Il Labrador Retriever è la razza canina più popolare d'America, e per buone ragioni. Sono compagni amichevoli, socievoli e pieni di energia che hanno abbastanza affetto per tutta la famiglia.",
        'temperament': "I Labrador sono famosi per la loro cordialità. Sono compagni di casa affabili che creano legami con tutta la famiglia e socializzano bene sia con i cani del vicinato che con le persone. Ma non confondere la loro personalità rilassata con poca energia.",
        'health': "Generalmente sani, ma predisposti a displasia dell'anca e del gomito, disturbi cardiaci, problemi oculari e collasso indotto dall'esercizio. L'obesità è comune, quindi controlla la loro dieta.",
        'exercise': "Razza ad alta energia che richiede un esercizio vigoroso quotidiano—almeno un'ora di attività. Prosperano con famiglie attive che amano le attività all'aperto. La stimolazione mentale attraverso l'addestramento e i giochi puzzle è altrettanto importante.",
        'verdict': "Il cane da famiglia per eccellenza. I Labrador Retriever sono amichevoli, pazienti e facili da addestrare—perfetti per i proprietari alle prime armi e le famiglie con bambini. Hanno bisogno di molto esercizio e perdono molto pelo, ma la loro natura amorevole li rende degni di tutto.",
    },
    'german-shepherd': {
        'overview': "Il Pastore Tedesco è una delle razze più versatili al mondo, eccellente come cane da lavoro, da servizio e da compagnia. La loro intelligenza e lealtà li rendono partner eccezionali.",
        'temperament': "I Pastori Tedeschi sono sicuri di sé, coraggiosi e intelligenti. Formano legami profondi con le loro famiglie e sono naturalmente protettivi. Richiedono socializzazione precoce e addestramento costante.",
        'health': "Predisposti a displasia dell'anca e del gomito, mielopatia degenerativa, gonfiore e problemi digestivi. Scegli un allevatore responsabile che testa per queste condizioni.",
        'exercise': "Razza ad alta energia che necessita di almeno 2 ore di esercizio al giorno. Eccellono nell'addestramento all'obbedienza, nell'agility e nel lavoro. La stimolazione mentale è importante quanto l'esercizio fisico.",
        'verdict': "Un compagno leale e versatile per proprietari esperti. I Pastori Tedeschi eccellono in quasi tutto ciò che fanno, dalla protezione della famiglia agli sport cinofili. Richiedono impegno nell'addestramento e nell'esercizio.",
    },
    'golden-retriever': {
        'overview': "Il Golden Retriever è uno dei cani più amati al mondo. Gentile, intelligente e devoto, questa razza è il compagno perfetto per famiglie, individui e come cane da terapia o servizio.",
        'temperament': "I Golden sono incredibilmente amichevoli e tolleranti. Amano tutti—bambini, estranei, altri animali. La loro natura paziente e il desiderio di compiacere li rendono eccellenti cani da famiglia.",
        'health': "Predisposti a cancro, displasia dell'anca e del gomito, problemi cardiaci e condizioni oculari. Visite veterinarie regolari e una dieta sana sono essenziali.",
        'exercise': "Cani attivi che necessitano di 1-2 ore di esercizio al giorno. Amano nuotare, fare escursioni e giocare a riporto. Senza sufficiente attività possono diventare irrequieti.",
        'verdict': "Il cane da famiglia ideale. I Golden Retriever sono pazienti, amorevoli e facili da addestrare. Richiedono molto esercizio e toelettatura, ma ripagano con infinita devozione.",
    },
    'french-bulldog': {
        'overview': "Il Bulldog Francese è diventato uno dei cani da compagnia più popolari al mondo. Piccolo, affettuoso e adattabile, è perfetto per la vita in appartamento e per i proprietari alle prime armi.",
        'temperament': "I Frenchie sono giocherelloni, vigili e adattabili. Amano stare con le persone e si adattano bene a qualsiasi situazione abitativa. Raramente abbaiano e vanno d'accordo con tutti.",
        'health': "Come razza brachicefala, possono avere difficoltà respiratorie. Predisposti a problemi alla colonna vertebrale, allergie cutanee e problemi oculari. Evita l'esercizio intenso nel caldo.",
        'exercise': "Cani a bassa energia che si accontentano di brevi passeggiate e giochi in casa. Non tollerano il caldo o l'esercizio intenso a causa della loro conformazione facciale.",
        'verdict': "Il compagno da appartamento perfetto. I Bulldog Francesi sono affettuosi, poco impegnativi e si adattano a qualsiasi stile di vita. Attenzione ai problemi di salute legati alla razza.",
    },
    'poodle': {
        'overview': "Il Barboncino è una delle razze più intelligenti e versatili. Disponibile in tre taglie (standard, miniatura e toy), eccelle in tutto, dall'obbedienza agli sport acquatici.",
        'temperament': "I Barboncini sono estremamente intelligenti, attivi e orgogliosi. Si legano strettamente alle loro famiglie e possono essere riservati con gli estranei. Hanno bisogno di stimolazione mentale.",
        'health': "Generalmente sani con una lunga aspettativa di vita. Predisposti a displasia dell'anca, problemi oculari, malattia di Addison e gonfiore (nello Standard).",
        'exercise': "Cani attivi che necessitano di esercizio regolare e stimolazione mentale. Eccellono nell'agility, nell'obbedienza e negli sport acquatici.",
        'verdict': "Intelligente, elegante e ipoallergenico. I Barboncini sono perfetti per chi cerca un cane versatile e addestrabile. Richiedono toelettatura regolare ma non perdono pelo.",
    },
    'beagle': {
        'overview': "Il Beagle è un cane da seguita amichevole e curioso, originariamente allevato per la caccia alla lepre. Oggi è un compagno familiare amato per il suo temperamento allegro.",
        'temperament': "I Beagle sono allegri, curiosi e amichevoli. Amano la compagnia e non amano stare soli. Il loro forte istinto di seguita significa che seguiranno qualsiasi odore interessante.",
        'health': "Generalmente sani ma predisposti a epilessia, ipotiroidismo, displasia dell'anca e problemi oculari. L'obesità è comune, quindi monitora la dieta.",
        'exercise': "Cani energici che necessitano di almeno un'ora di esercizio al giorno. Amano esplorare e seguire odori. Un giardino recintato è ideale.",
        'verdict': "Un compagno allegro e amichevole. I Beagle sono perfetti per famiglie attive che possono fornire compagnia e esercizio. Possono essere vocali e testardi nell'addestramento.",
    },
    'bulldog': {
        'overview': "Il Bulldog Inglese è un simbolo di tenacia e coraggio. Nonostante il suo aspetto intimidatorio, è un cane dolce e affettuoso che ama la famiglia.",
        'temperament': "I Bulldog sono docili, amichevoli e dignitosi. Formano forti legami con le loro famiglie e vanno d'accordo con bambini e altri animali. Sono coraggiosi ma non aggressivi.",
        'health': "Come razza brachicefala, hanno problemi respiratori. Predisposti a problemi cutanei, displasia dell'anca, problemi cardiaci e colpi di calore.",
        'exercise': "Cani a bassa energia che preferiscono passeggiate brevi e rilassarsi in casa. Non tollerano il caldo e non dovrebbero fare esercizio intenso.",
        'verdict': "Un compagno tranquillo e affettuoso. I Bulldog sono perfetti per chi cerca un cane calmo e poco attivo. Richiedono attenzione ai problemi di salute e non tollerano il caldo.",
    },
    'dachshund': {
        'overview': "Il Bassotto, con il suo corpo allungato e le zampe corte, è un cane coraggioso originariamente allevato per cacciare tassi. Oggi è un compagno affettuoso e vivace.",
        'temperament': "I Bassotti sono coraggiosi, curiosi e vivaci. Possono essere testardi ma sono devoti alle loro famiglie. Hanno un forte istinto di caccia e amano scavare.",
        'health': "La loro conformazione li rende predisposti a problemi alla colonna vertebrale. Evita salti e scale. Predisposti anche a obesità e problemi dentali.",
        'exercise': "Cani moderatamente attivi che necessitano di passeggiate regolari. Non dovrebbero saltare o fare attività che stressano la schiena.",
        'verdict': "Un piccolo cane con grande personalità. I Bassotti sono affettuosi e divertenti ma richiedono attenzione alla salute della schiena. Perfetti per appartamenti.",
    },
    'siberian-husky': {
        'overview': "Il Siberian Husky è un cane da lavoro atletico originario della Siberia. Allevato per trainare slitte, è un cane energico e indipendente con un magnifico mantello.",
        'temperament': "Gli Husky sono amichevoli, maliziosi e indipendenti. Amano le persone ma possono essere testardi. Hanno un forte istinto predatorio e tendenza alla fuga.",
        'health': "Generalmente sani ma predisposti a displasia dell'anca, problemi oculari e ipotiroidismo. Il loro mantello denso richiede cure durante la muta.",
        'exercise': "Cani ad altissima energia che necessitano di almeno 2 ore di esercizio intenso al giorno. Senza sufficiente attività diventano distruttivi.",
        'verdict': "Un cane bellissimo ma impegnativo. Gli Husky sono perfetti per proprietari attivi in climi freddi. Non adatti ai principianti o a chi ha poco tempo per l'esercizio.",
    },
    'rottweiler': {
        'overview': "Il Rottweiler è un cane potente e sicuro di sé, originariamente usato per condurre il bestiame e tirare carretti. È un guardiano leale e un compagno devoto.",
        'temperament': "I Rottweiler sono calmi, sicuri e coraggiosi. Sono naturalmente protettivi e riservati con gli estranei. Richiedono socializzazione precoce e addestramento costante.",
        'health': "Predisposti a displasia dell'anca e del gomito, problemi cardiaci e cancro. Scegli un allevatore che testa per queste condizioni.",
        'exercise': "Cani energici che necessitano di esercizio regolare e stimolazione mentale. Eccellono nell'obbedienza e nel lavoro.",
        'verdict': "Un guardiano leale e potente. I Rottweiler sono eccellenti per proprietari esperti che possono fornire leadership e addestramento. Non adatti ai principianti.",
    },
    'yorkshire-terrier': {
        'overview': "Lo Yorkshire Terrier è un piccolo cane con una grande personalità. Nonostante le dimensioni ridotte, ha il coraggio di un terrier e l'eleganza di un cane da compagnia.",
        'temperament': "Gli Yorkie sono vivaci, affettuosi e coraggiosi. Possono essere testardi ma sono devoti ai loro proprietari. Spesso non si rendono conto delle loro piccole dimensioni.",
        'health': "Predisposti a lussazione della rotula, problemi dentali, ipoglicemia e collasso della trachea. Richiedono cure dentali regolari.",
        'exercise': "Cani moderatamente attivi che si accontentano di brevi passeggiate e giochi in casa. Perfetti per la vita in appartamento.",
        'verdict': "Un piccolo compagno con grande carattere. Gli Yorkshire Terrier sono perfetti per chi cerca un cane portatile e affettuoso. Richiedono toelettatura regolare.",
    },
    'boxer': {
        'overview': "Il Boxer è un cane atletico e giocoso, noto per la sua energia inesauribile e il suo amore per i bambini. È un eccellente cane da famiglia e guardiano.",
        'temperament': "I Boxer sono giocosi, energici e leali. Amano i bambini e sono pazienti con loro. Sono protettivi ma non aggressivi, vigili ma amichevoli.",
        'health': "Predisposti a cardiomiopatia, cancro, displasia dell'anca e problemi intestinali. Come razza brachicefala, possono avere difficoltà respiratorie nel caldo.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio e gioco. Rimangono giocosi per tutta la vita e amano correre e saltare.",
        'verdict': "Un compagno giocoso e protettivo. I Boxer sono perfetti per famiglie attive con bambini. Richiedono molto esercizio ma ripagano con infinita gioia.",
    },
    'cavalier-king-charles-spaniel': {
        'overview': "Il Cavalier King Charles Spaniel è un cane da compagnia elegante e affettuoso. Gentile e adattabile, è perfetto sia per famiglie attive che per anziani.",
        'temperament': "I Cavalier sono dolci, affettuosi e pazienti. Amano le coccole e si adattano facilmente a qualsiasi situazione. Sono eccellenti con bambini e altri animali.",
        'health': "Predisposti a malattie cardiache, siringomielia e problemi oculari. Scegli allevatori che testano per queste condizioni.",
        'exercise': "Cani moderatamente attivi che si adattano al livello di attività del proprietario. Amano le passeggiate ma sono felici anche a rilassarsi.",
        'verdict': "Il compagno perfetto per tutti. I Cavalier sono adattabili, affettuosi e facili da gestire. Ottimi per principianti e famiglie.",
    },
    'shih-tzu': {
        'overview': "Lo Shih Tzu è un antico cane da compagnia cinese, allevato per essere un compagno affettuoso. Il suo nome significa 'cane leone'.",
        'temperament': "Gli Shih Tzu sono affettuosi, giocosi e amichevoli. Amano le persone e sono eccellenti cani da compagnia. Possono essere testardi ma sono generalmente facili da gestire.",
        'health': "Predisposti a problemi oculari, problemi respiratori e displasia dell'anca. Richiedono cure oculari e dentali regolari.",
        'exercise': "Cani a bassa energia che si accontentano di brevi passeggiate e giochi in casa. Perfetti per appartamenti.",
        'verdict': "Un compagno affettuoso e adattabile. Gli Shih Tzu sono perfetti per chi cerca un cane da coccole poco impegnativo.",
    },
    'chihuahua': {
        'overview': "Il Chihuahua è il cane più piccolo del mondo ma ha una personalità enorme. Originario del Messico, è un compagno leale e vivace.",
        'temperament': "I Chihuahua sono vivaci, coraggiosi e devoti. Si legano fortemente a una persona e possono essere protettivi. Non sempre tollerano i bambini.",
        'health': "Predisposti a lussazione della rotula, problemi cardiaci, ipoglicemia e idrocefalo. Sensibili al freddo.",
        'exercise': "Cani a bassa energia che si accontentano di brevi passeggiate. Perfetti per appartamenti e anziani.",
        'verdict': "Un grande carattere in un corpo minuscolo. I Chihuahua sono perfetti per chi cerca un compagno portatile e devoto.",
    },
    'pomeranian': {
        'overview': "Il Volpino di Pomerania è un piccolo cane vivace con un magnifico mantello. Nonostante le dimensioni, ha la personalità di un cane grande.",
        'temperament': "I Pomeranian sono vivaci, curiosi e audaci. Sono intelligenti e imparano facilmente ma possono essere testardi. Amano abbaiare.",
        'health': "Predisposti a lussazione della rotula, problemi dentali e alopecia. Richiedono cure dentali e del mantello regolari.",
        'exercise': "Cani attivi che amano giocare ma si accontentano di spazi piccoli. Perfetti per appartamenti.",
        'verdict': "Un piccolo cane con grande personalità. I Pomeranian sono perfetti per chi vuole un compagno vivace e affettuoso.",
    },
    'australian-shepherd': {
        'overview': "Il Pastore Australiano è un cane da lavoro intelligente e versatile. Nonostante il nome, è stato sviluppato negli Stati Uniti.",
        'temperament': "Gli Aussie sono intelligenti, energici e leali. Eccellono in quasi ogni attività canina. Hanno bisogno di lavoro mentale e fisico.",
        'health': "Predisposti a displasia dell'anca, epilessia e problemi oculari. Il gene merle può causare sordità e cecità se accoppiato.",
        'exercise': "Cani ad altissima energia che necessitano di almeno 2 ore di esercizio e stimolazione mentale al giorno.",
        'verdict': "Un cane versatile per proprietari attivi. Gli Aussie sono perfetti per chi pratica sport cinofili o ha bisogno di un compagno di avventure.",
    },
    'great-dane': {
        'overview': "L'Alano è uno dei cani più grandi al mondo, ma è noto come 'gigante gentile'. Nonostante le dimensioni imponenti, è un cane dolce e affettuoso.",
        'temperament': "Gli Alani sono gentili, pazienti e amichevoli. Amano stare con la famiglia e sono sorprendentemente adatti alla vita in casa.",
        'health': "Predisposti a torsione gastrica, cardiomiopatia e problemi articolari. Hanno una vita relativamente breve (7-10 anni).",
        'exercise': "Cani moderatamente attivi che necessitano di passeggiate regolari ma non di esercizio intenso.",
        'verdict': "Un gigante dal cuore tenero. Gli Alani sono perfetti per chi ha spazio e vuole un cane affettuoso e imponente.",
    },
    'maltese': {
        'overview': "Il Maltese è un antico cane da compagnia con un magnifico mantello bianco. È stato il compagno preferito dell'aristocrazia per secoli.",
        'temperament': "I Maltesi sono affettuosi, giocosi e gentili. Amano le persone e si legano fortemente ai proprietari. Possono soffrire di ansia da separazione.",
        'health': "Predisposti a lussazione della rotula, problemi dentali e lacrimazione eccessiva. Richiedono toelettatura quotidiana.",
        'exercise': "Cani a bassa energia che si accontentano di brevi passeggiate e giochi in casa.",
        'verdict': "Un elegante compagno da coccole. I Maltesi sono perfetti per chi cerca un cane affettuoso e ipoallergenico.",
    },
    'border-collie': {
        'overview': "Il Border Collie è considerato il cane più intelligente del mondo. Eccelle nella conduzione del gregge e in tutti gli sport cinofili.",
        'temperament': "I Border Collie sono estremamente intelligenti, energici e focalizzati. Hanno bisogno costante di lavoro mentale e fisico.",
        'health': "Predisposti a displasia dell'anca, epilessia, problemi oculari e anomalia dell'occhio del Collie (CEA).",
        'exercise': "Cani ad altissima energia che necessitano di almeno 2 ore di esercizio intenso e stimolazione mentale al giorno.",
        'verdict': "Il cane più intelligente per proprietari dedicati. I Border Collie sono perfetti per chi può dedicare tempo all'addestramento e agli sport cinofili.",
    },
    'doberman-pinscher': {
        'overview': "Il Dobermann è un cane atletico e intelligente, originariamente allevato come cane da guardia. È leale, protettivo e devoto alla famiglia.",
        'temperament': "I Dobermann sono intelligenti, vigili e leali. Sono naturalmente protettivi ma non aggressivi se ben socializzati. Si legano fortemente alla famiglia.",
        'health': "Predisposti a cardiomiopatia, malattia di von Willebrand, displasia dell'anca e ipotiroidismo.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio e stimolazione mentale. Eccellono nell'obbedienza e negli sport cinofili.",
        'verdict': "Un guardiano leale e atletico. I Dobermann sono perfetti per proprietari esperti che cercano un cane versatile e protettivo.",
    },
    'cocker-spaniel': {
        'overview': "Il Cocker Spaniel è un cane allegro e affettuoso, originariamente allevato per la caccia. Oggi è uno dei cani da compagnia più amati.",
        'temperament': "I Cocker Spaniel sono allegri, affettuosi e giocosi. Amano le persone e sono eccellenti con i bambini. Hanno bisogno di compagnia.",
        'health': "Predisposti a infezioni alle orecchie, problemi oculari, displasia dell'anca e epilessia. Le orecchie richiedono cure regolari.",
        'exercise': "Cani moderatamente attivi che necessitano di passeggiate quotidiane e gioco.",
        'verdict': "Un compagno allegro e affettuoso. I Cocker Spaniel sono perfetti per famiglie che cercano un cane gioioso e adattabile.",
    },
}


def update_italian_breed_file(breed_id: str, translations: dict) -> bool:
    """Update an Italian breed HTML file with translations"""
    filepath = IT_BREEDS_DIR / f'{breed_id}.html'
    if not filepath.exists():
        print(f"  File not found: {filepath}")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Update meta description
    if 'overview' in translations:
        meta_desc = translations['overview'][:150] + '...' if len(translations['overview']) > 150 else translations['overview']
        content = re.sub(
            r'<meta name="description" content="[^"]*">',
            f'<meta name="description" content="{meta_desc}">',
            content
        )
    
    # Update hero paragraph
    if 'overview' in translations:
        hero_text = translations['overview'][:200] if len(translations['overview']) > 200 else translations['overview']
        content = re.sub(
            r'(<p class="text-lg text-slate-600 mb-6">)[^<]*(</p>)',
            f'\\1{hero_text}\\2',
            content
        )
    
    # Update Panoramica section
    if 'overview' in translations:
        content = re.sub(
            r'(Panoramica\s*</h2>.*?<div class="px-6 pb-6"><p class="text-slate-600">)[^<]*(</p></div>)',
            f'\\1{translations["overview"]}\\2',
            content,
            flags=re.DOTALL
        )
    
    # Update Temperamento section content (the details section, not tags)
    if 'temperament' in translations:
        # Match the Temperamento details section specifically
        pattern = r'(<i data-lucide="heart"[^>]*></i>\s*Temperamento\s*</h2>.*?<div class="px-6 pb-6"><p class="text-slate-600">)[^<]*(</p></div>)'
        content = re.sub(pattern, f'\\1{translations["temperament"]}\\2', content, flags=re.DOTALL)
    
    # Update Salute section
    if 'health' in translations:
        content = re.sub(
            r'(Salute\s*</h2>.*?<div class="px-6 pb-6"><p class="text-slate-600">)[^<]*(</p></div>)',
            f'\\1{translations["health"]}\\2',
            content,
            flags=re.DOTALL
        )
    
    # Update Esercizio section
    if 'exercise' in translations:
        content = re.sub(
            r'(Esercizio\s*</h2>.*?<div class="px-6 pb-6"><p class="text-slate-600">)[^<]*(</p></div>)',
            f'\\1{translations["exercise"]}\\2',
            content,
            flags=re.DOTALL
        )
    
    # Update verdict
    if 'verdict' in translations:
        content = re.sub(
            r'(<strong>Il Nostro Verdetto:</strong> )[^<]*(</p>)',
            f'\\1{translations["verdict"]}\\2',
            content
        )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    print(f"Translating Italian breed pages...")
    print(f"Found {len(ITALIAN_DESCRIPTIONS)} breed translations")
    
    updated = 0
    for breed_id, translations in ITALIAN_DESCRIPTIONS.items():
        print(f"  Processing: {breed_id}")
        if update_italian_breed_file(breed_id, translations):
            updated += 1
            print(f"    ✓ Updated")
        else:
            print(f"    - No changes or not found")
    
    print(f"\nDone! Updated {updated} breed files.")


if __name__ == '__main__':
    main()
