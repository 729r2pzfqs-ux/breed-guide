#!/usr/bin/env python3
"""Batch 2 Italian breed translations"""

import re
from pathlib import Path

IT_BREEDS_DIR = Path(__file__).parent.parent / 'it' / 'breeds'

BREEDS_BATCH2 = {
    'akita': {
        'overview': "L'Akita è un cane grande e potente originario del Giappone. Leale e dignitoso, è un eccellente guardiano e compagno devoto per proprietari esperti.",
        'temperament': "Gli Akita sono coraggiosi, dignitosi e profondamente leali. Possono essere riservati con gli estranei e dominanti con altri cani. Richiedono un proprietario esperto.",
        'health': "Predisposti a displasia dell'anca, problemi oculari, ipotiroidismo e torsione gastrica. Scegli allevatori che testano per queste condizioni.",
        'exercise': "Cani moderatamente attivi che necessitano di passeggiate quotidiane. Non amano il caldo e preferiscono climi freschi.",
        'verdict': "Un guardiano leale e imponente. Gli Akita sono perfetti per proprietari esperti che cercano un compagno devoto e protettivo.",
    },
    'shiba-inu': {
        'overview': "Lo Shiba Inu è il cane più popolare del Giappone. Piccolo, agile e indipendente, ha conquistato il mondo con la sua personalità unica.",
        'temperament': "Gli Shiba sono indipendenti, vigili e coraggiosi. Sono puliti come i gatti e possono essere testardi. Non sempre vanno d'accordo con altri cani.",
        'health': "Generalmente sani ma predisposti a allergie, lussazione della rotula e displasia dell'anca. Hanno una lunga aspettativa di vita.",
        'exercise': "Cani moderatamente attivi che necessitano di passeggiate quotidiane. Hanno un forte istinto di caccia e dovrebbero essere tenuti al guinzaglio.",
        'verdict': "Un cane indipendente con grande personalità. Gli Shiba sono perfetti per chi apprezza un compagno felino in forma canina.",
    },
    'bernese-mountain-dog': {
        'overview': "Il Bovaro del Bernese è un cane da lavoro svizzero dal magnifico mantello tricolore. Gentile e affettuoso, è un eccellente cane da famiglia.",
        'temperament': "I Bovari del Bernese sono gentili, calmi e affettuosi. Amano i bambini e sono pazienti con tutti. Sono leali e devoti alla famiglia.",
        'health': "Purtroppo hanno una vita breve (7-10 anni). Predisposti a cancro, displasia dell'anca e del gomito, e problemi cardiaci.",
        'exercise': "Cani moderatamente attivi che amano le attività all'aperto. Non tollerano il caldo a causa del loro mantello pesante.",
        'verdict': "Un gigante gentile con il cuore d'oro. I Bovari del Bernese sono perfetti per famiglie che cercano un compagno affettuoso e paziente.",
    },
    'bichon-frise': {
        'overview': "Il Bichon Frise è un piccolo cane bianco allegro e giocoso. Con il suo mantello ipoallergenico e la personalità solare, è perfetto per molte famiglie.",
        'temperament': "I Bichon sono allegri, giocosi e affettuosi. Amano le persone e vanno d'accordo con tutti. Possono soffrire di ansia da separazione.",
        'health': "Predisposti a allergie cutanee, lussazione della rotula e problemi oculari. Il mantello richiede toelettatura professionale regolare.",
        'exercise': "Cani moderatamente attivi che amano giocare. Si adattano bene alla vita in appartamento.",
        'verdict': "Un piccolo raggio di sole. I Bichon Frise sono perfetti per chi cerca un compagno allegro e ipoallergenico.",
    },
    'boston-terrier': {
        'overview': "Il Boston Terrier, soprannominato 'il gentiluomo americano', è un cane elegante e amichevole. Il suo aspetto distintivo e la personalità affabile lo rendono molto amato.",
        'temperament': "I Boston Terrier sono amichevoli, intelligenti e vivaci. Amano le persone e sono eccellenti compagni. Si adattano bene a qualsiasi situazione.",
        'health': "Come razza brachicefala, possono avere problemi respiratori. Predisposti anche a problemi oculari, lussazione della rotula e sordità.",
        'exercise': "Cani moderatamente attivi che si accontentano di passeggiate brevi e giochi in casa. Non tollerano il caldo.",
        'verdict': "Un compagno elegante e amichevole. I Boston Terrier sono perfetti per appartamenti e famiglie che cercano un cane adattabile.",
    },
    'pug': {
        'overview': "Il Carlino è un cane antico con una personalità enorme. Con il suo muso schiacciato e gli occhi espressivi, conquista tutti con il suo fascino comico.",
        'temperament': "I Carlini sono affettuosi, giocosi e un po' monelli. Amano stare con le persone e soffrono se lasciati soli. Sono eccellenti cani da compagnia.",
        'health': "Come razza brachicefala, hanno problemi respiratori. Predisposti a problemi oculari, obesità e problemi cutanei. Non tollerano il caldo.",
        'exercise': "Cani a bassa energia che si accontentano di brevi passeggiate. Amano giocare ma si stancano facilmente.",
        'verdict': "Un comico in formato cane. I Carlini sono perfetti per chi cerca un compagno affettuoso e divertente per la vita in appartamento.",
    },
    'miniature-schnauzer': {
        'overview': "Lo Schnauzer Nano è un piccolo cane robusto con una personalità vivace. Originariamente allevato come cane da fattoria, oggi è un popolare compagno di famiglia.",
        'temperament': "Gli Schnauzer Nani sono vigili, intelligenti e giocosi. Sono buoni cani da guardia e abbaiano per avvisare. Leali e affettuosi con la famiglia.",
        'health': "Predisposti a pancreatite, diabete, calcoli urinari e problemi oculari. Richiedono una dieta attenta.",
        'exercise': "Cani attivi che necessitano di esercizio regolare e stimolazione mentale. Amano giocare e imparare trucchi.",
        'verdict': "Un piccolo cane con grande personalità. Gli Schnauzer Nani sono perfetti per famiglie attive che cercano un compagno vigile e affettuoso.",
    },
    'weimaraner': {
        'overview': "Il Weimaraner è un elegante cane da caccia tedesco dal distintivo mantello grigio. Atletico e intelligente, è un compagno perfetto per proprietari attivi.",
        'temperament': "I Weimaraner sono energici, intelligenti e affettuosi. Si legano fortemente ai proprietari e possono soffrire di ansia da separazione. Hanno bisogno di molto esercizio.",
        'health': "Predisposti a torsione gastrica, displasia dell'anca e problemi cardiaci. Generalmente sani con buona cura.",
        'exercise': "Cani ad altissima energia che necessitano di almeno 2 ore di esercizio intenso al giorno. Non adatti a proprietari sedentari.",
        'verdict': "Un atleta elegante. I Weimaraner sono perfetti per proprietari molto attivi che possono fornire esercizio intenso e compagnia costante.",
    },
    'vizsla': {
        'overview': "Il Vizsla è un elegante cane da caccia ungherese dal mantello dorato. Affettuoso e atletico, è conosciuto come il 'cane velcro' per il suo attaccamento ai proprietari.",
        'temperament': "I Vizsla sono affettuosi, energici e sensibili. Si legano fortemente alla famiglia e non amano stare soli. Sono gentili e amano le coccole.",
        'health': "Generalmente sani ma predisposti a displasia dell'anca, epilessia e allergie. Hanno una buona aspettativa di vita.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio quotidiano. Amano correre, nuotare e cacciare.",
        'verdict': "Il compagno perfetto per atleti. I Vizsla sono affettuosi e atletici, ideali per famiglie attive che vogliono un cane sempre presente.",
    },
    'whippet': {
        'overview': "Il Whippet è un levriero di taglia media, elegante e veloce. Nonostante la sua velocità, è un cane calmo e affettuoso in casa.",
        'temperament': "I Whippet sono gentili, affettuosi e calmi. Amano correre ma sono pantofolai in casa. Sono sensibili e non tollerano trattamenti duri.",
        'health': "Generalmente sani con pochi problemi ereditari. Sensibili al freddo e agli anestetici. Possono avere problemi cardiaci.",
        'exercise': "Hanno bisogno di sprint quotidiani ma sono calmi in casa. Un giardino recintato è ideale per farli correre.",
        'verdict': "Un velocista elegante e affettuoso. I Whippet sono perfetti per chi cerca un cane atletico ma tranquillo in casa.",
    },
    'italian-greyhound': {
        'overview': "Il Piccolo Levriero Italiano è la versione miniatura del Greyhound. Elegante e affettuoso, è un compagno perfetto per la vita in appartamento.",
        'temperament': "I Piccoli Levrieri Italiani sono affettuosi, giocosi e un po' timidi. Amano le coccole e stare vicino ai proprietari. Possono essere riservati con gli estranei.",
        'health': "Predisposti a fratture ossee, problemi dentali, epilessia e ipotiroidismo. Le loro ossa sottili richiedono attenzione.",
        'exercise': "Cani moderatamente attivi che amano correre ma si accontentano di giochi in casa. Sensibili al freddo.",
        'verdict': "Eleganza in miniatura. I Piccoli Levrieri Italiani sono perfetti per chi cerca un compagno affettuoso e raffinato.",
    },
    'basset-hound': {
        'overview': "Il Basset Hound è un cane da seguita con orecchie lunghe e espressione malinconica. Nonostante l'aspetto triste, è un cane allegro e affettuoso.",
        'temperament': "I Basset Hound sono calmi, affettuosi e testardi. Seguono il naso ovunque e possono essere difficili da richiamare. Amano la compagnia.",
        'health': "Predisposti a problemi alla schiena, infezioni alle orecchie, obesità e problemi oculari. Le orecchie richiedono pulizia regolare.",
        'exercise': "Cani a bassa-media energia che necessitano di passeggiate moderate. Tendono all'obesità se non esercitati.",
        'verdict': "Un segugio dal cuore tenero. I Basset Hound sono perfetti per famiglie che cercano un compagno calmo e affettuoso.",
    },
    'bloodhound': {
        'overview': "Il Bloodhound è il re dei cani da seguita, famoso per il suo olfatto eccezionale. Gentile e paziente, è un compagno dolce nonostante le grandi dimensioni.",
        'temperament': "I Bloodhound sono gentili, pazienti e determinati. Seguono le tracce con ossessione. Sono affettuosi ma possono essere testardi.",
        'health': "Predisposti a torsione gastrica, displasia dell'anca, problemi oculari e infezioni alle orecchie. Le pieghe cutanee richiedono pulizia.",
        'exercise': "Cani moderatamente attivi che amano seguire tracce. Devono essere tenuti al guinzaglio o in aree recintate.",
        'verdict': "Il naso più famoso del mondo canino. I Bloodhound sono perfetti per chi apprezza un cane unico e affettuoso.",
    },
    'english-springer-spaniel': {
        'overview': "L'English Springer Spaniel è un cane da caccia versatile ed entusiasta. Allegro e affettuoso, è un eccellente compagno per famiglie attive.",
        'temperament': "Gli Springer sono allegri, affettuosi e desiderosi di compiacere. Amano lavorare e giocare. Hanno bisogno di compagnia e attività.",
        'health': "Predisposti a displasia dell'anca, problemi oculari, infezioni alle orecchie e epilessia. Generalmente sani.",
        'exercise': "Cani ad alta energia che necessitano di molto esercizio. Amano nuotare, cacciare e giocare a riporto.",
        'verdict': "Un compagno entusiasta per famiglie attive. Gli Springer sono perfetti per chi ama le attività all'aperto.",
    },
    'shetland-sheepdog': {
        'overview': "Lo Shetland Sheepdog, o Sheltie, è un cane da pastore intelligente e affettuoso. Simile a un Collie in miniatura, è un compagno devoto.",
        'temperament': "Gli Sheltie sono intelligenti, leali e sensibili. Possono essere riservati con gli estranei. Eccellono nell'obbedienza e nell'agility.",
        'health': "Predisposti a problemi oculari, displasia dell'anca, epilessia e problemi alla tiroide. Il gene merle richiede attenzione negli accoppiamenti.",
        'exercise': "Cani attivi che amano lavorare. Eccellono negli sport cinofili e hanno bisogno di stimolazione mentale.",
        'verdict': "Un piccolo genio devoto. Gli Sheltie sono perfetti per chi cerca un cane intelligente e addestrabile.",
    },
    'cane-corso': {
        'overview': "Il Cane Corso è un antico molosso italiano, potente e atletico. Guardiano nato, è devoto alla famiglia e diffidente con gli estranei.",
        'temperament': "I Cane Corso sono intelligenti, leali e protettivi. Sono calmi ma vigili. Richiedono un proprietario esperto e socializzazione precoce.",
        'health': "Predisposti a displasia dell'anca, problemi cardiaci, torsione gastrica ed entropion. Scegli allevatori responsabili.",
        'exercise': "Cani moderatamente attivi che necessitano di esercizio regolare. Non sono iperattivi ma hanno bisogno di spazio.",
        'verdict': "Un guardiano italiano imponente. I Cane Corso sono perfetti per proprietari esperti che cercano un protettore leale.",
    },
    'bull-terrier': {
        'overview': "Il Bull Terrier è un cane unico con la sua testa a forma di uovo. Giocherellone e affettuoso, è un compagno divertente e leale.",
        'temperament': "I Bull Terrier sono giocosi, coraggiosi e affettuosi. Possono essere testardi ma sono devoti alla famiglia. Amano giocare.",
        'health': "Predisposti a sordità, problemi cardiaci, lussazione della rotula e allergie cutanee. Richiedono protezione solare.",
        'exercise': "Cani energici che necessitano di esercizio quotidiano e gioco. Si annoiano facilmente senza stimolazione.",
        'verdict': "Un clown coraggioso. I Bull Terrier sono perfetti per famiglie attive che cercano un compagno divertente e unico.",
    },
    'staffordshire-bull-terrier': {
        'overview': "Lo Staffordshire Bull Terrier è un cane muscoloso ma affettuoso. Conosciuto come 'nanny dog', è eccellente con i bambini.",
        'temperament': "Gli Staffie sono coraggiosi, affettuosi e leali. Amano le persone, specialmente i bambini. Possono essere testardi ma sono desiderosi di compiacere.",
        'health': "Predisposti a displasia dell'anca, cataratta, problemi cutanei e L-2 HGA. Generalmente robusti.",
        'exercise': "Cani energici che necessitano di esercizio quotidiano. Amano giocare e sono atletici.",
        'verdict': "Un cuore tenero in un corpo muscoloso. Gli Staffie sono perfetti per famiglie che cercano un compagno leale e affettuoso.",
    },
    'west-highland-white-terrier': {
        'overview': "Il West Highland White Terrier, o Westie, è un piccolo terrier bianco pieno di personalità. Vivace e sicuro di sé, è un compagno allegro.",
        'temperament': "I Westie sono vivaci, coraggiosi e indipendenti. Hanno la tipica personalità terrier. Possono essere testardi ma sono affettuosi.",
        'health': "Predisposti a problemi cutanei, allergie, lussazione della rotula e malattia di Legg-Calvé-Perthes.",
        'exercise': "Cani attivi che amano giocare ed esplorare. Si adattano bene agli appartamenti con sufficiente esercizio.",
        'verdict': "Un piccolo terrier con grande cuore. I Westie sono perfetti per chi cerca un compagno vivace e allegro.",
    },
    'scottish-terrier': {
        'overview': "Lo Scottish Terrier, o Scottie, è un terrier dignitoso e indipendente. Con il suo aspetto distintivo e la personalità forte, è un cane unico.",
        'temperament': "Gli Scottie sono indipendenti, determinati e leali. Possono essere riservati con gli estranei. Hanno una personalità forte.",
        'health': "Predisposti a cancro della vescica, crampi di Scottie, malattia di von Willebrand e problemi cutanei.",
        'exercise': "Cani moderatamente attivi che amano le passeggiate. Hanno istinto di caccia e amano scavare.",
        'verdict': "Un terrier con dignità scozzese. Gli Scottie sono perfetti per chi apprezza un cane indipendente e caratteristico.",
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
    print(f"Translating {len(BREEDS_BATCH2)} breeds...")
    count = 0
    for bid, trans in BREEDS_BATCH2.items():
        if update_file(bid, trans):
            print(f"  ✓ {bid}")
            count += 1
    print(f"Done! Updated {count} files.")
