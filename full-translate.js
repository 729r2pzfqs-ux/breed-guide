#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const breedsDir = path.join(__dirname, 'it/breeds');

// Breed-specific translations
const breedTranslations = {
  'airedale-terrier.html': {
    meta: "L'Airedale Terrier, conosciuto come il 'Re dei Terrier', è la razza di terrier più grande. Intelligente, versatile e coraggioso.",
    hero: "L'Airedale Terrier, conosciuto come il 'Re dei Terrier', è la razza di terrier più grande. Intelligente, versatile e coraggioso, eccelle in molti ruoli.",
    panoramica: "L'Airedale Terrier è la razza di terrier più grande, soprannominato il 'Re dei Terrier'. Originario dello Yorkshire, in Inghilterra, questa razza versatile è stata sviluppata per la caccia a lontre e tassi. Oggi eccellono come cani da famiglia, da lavoro e da esposizione.",
    temperamento: "Gli Airedale sono sicuri di sé, coraggiosi e intelligenti con una vena testarda. Sono giocherelloni e affettuosi con la famiglia ma possono essere riservati con gli estranei. Il loro forte istinto predatorio richiede una socializzazione precoce con animali più piccoli.",
    salute: "Generalmente sani ma predisposti a displasia dell'anca, problemi cardiaci e allergie cutanee. La torsione gastrica è un rischio per la loro taglia. Controlli regolari dal veterinario e una dieta appropriata sono essenziali.",
    esercizio: "Elevate esigenze di esercizio che richiedono almeno un'ora di attività vigorosa al giorno. Eccellono negli sport cinofili come agility e obedience. La stimolazione mentale è importante quanto l'esercizio fisico.",
    verdetto: "L'Airedale è un terrier versatile e intelligente, perfetto per proprietari attivi che desiderano un compagno leale e coraggioso. Richiede addestramento costante e molto esercizio."
  },
  'akita.html': {
    meta: "L'Akita è un cane potente e dignitoso originario del Giappone, noto per la sua lealtà incrollabile e il suo portamento maestoso.",
    hero: "L'Akita è un cane potente e dignitoso originario del Giappone, noto per la sua lealtà incrollabile e il carattere protettivo.",
    panoramica: "L'Akita è una razza giapponese antica, sviluppata nella regione montuosa di Akita per la caccia a orsi e cinghiali. Simbolo di lealtà in Giappone, la storia di Hachiko ha reso famosa questa razza nel mondo.",
    temperamento: "Gli Akita sono dignitosi, coraggiosi e profondamente leali alla famiglia. Possono essere riservati o diffidenti con gli estranei e altri cani. Richiedono un proprietario esperto che stabilisca una leadership chiara.",
    salute: "Predisposti a displasia dell'anca e del gomito, problemi alla tiroide e malattie autoimmuni. La torsione gastrica è un rischio. L'aspettativa di vita è di 10-13 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono sufficienti. Non amano il caldo eccessivo. La stimolazione mentale attraverso l'addestramento è importante.",
    verdetto: "L'Akita è un compagno maestoso e devoto, ideale per proprietari esperti che possono offrire leadership ferma e socializzazione precoce. Non adatto a proprietari alle prime armi o famiglie con altri animali."
  },
  'alaskan-malamute.html': {
    meta: "L'Alaskan Malamute è un cane da slitta potente e maestoso, costruito per resistenza e forza. Affettuoso e giocherellone con la famiglia.",
    hero: "L'Alaskan Malamute è un cane da slitta potente e maestoso, costruito per resistenza e forza nel rigido clima artico.",
    panoramica: "L'Alaskan Malamute è una delle razze da slitta più antiche, sviluppata dal popolo Mahlemut dell'Alaska. Costruiti per trainare carichi pesanti su lunghe distanze, questi cani sono incredibilmente forti e resistenti.",
    temperamento: "I Malamute sono affettuosi, giocherelloni e leali con la famiglia. Hanno una forte natura da branco e possono essere dominanti con altri cani. Il loro istinto predatorio è forte. Sono socievoli con le persone.",
    salute: "Predisposti a displasia dell'anca, cataratta, ipotiroidismo e polineuropatia. Sensibili al caldo. L'aspettativa di vita è di 10-14 anni con cure adeguate.",
    esercizio: "Elevate esigenze di esercizio. Necessitano di attività vigorose quotidiane come corsa, escursionismo o traino. Senza sfogo adeguato possono diventare distruttivi.",
    verdetto: "Il Malamute è un compagno maestoso per proprietari attivi in climi freschi. Richiede molto esercizio, spazio e un proprietario esperto che comprenda la sua natura indipendente."
  },
  'beagle.html': {
    meta: "Il Beagle è un segugio allegro e curioso, amato per il suo carattere amichevole e il naso eccezionale. Perfetto cane da famiglia.",
    hero: "Il Beagle è un segugio allegro e curioso, amato per il suo carattere amichevole, il naso eccezionale e la taglia compatta.",
    panoramica: "Il Beagle è una delle razze di segugi più popolari, sviluppata in Inghilterra per la caccia alla lepre. Il loro naso eccezionale li rende ancora oggi ottimi cani da fiuto per la ricerca di contrabbando.",
    temperamento: "I Beagle sono allegri, curiosi e amichevoli. Adorano la compagnia e possono soffrire di ansia da separazione. Il loro istinto di seguire le tracce può portarli a fuggire. Sono vocali e amano abbaiare e ululare.",
    salute: "Generalmente sani ma predisposti a displasia dell'anca, epilessia e ipotiroidismo. Tendono all'obesità se non controllati. L'aspettativa di vita è di 10-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono essenziali. Amano seguire le tracce e sniffare. Un giardino recintato è importante poiché tendono a seguire gli odori.",
    verdetto: "Il Beagle è un eccellente cane da famiglia, allegro e affettuoso. Adatto a famiglie con bambini e proprietari alle prime armi. Attenzione alla tendenza a fuggire seguendo gli odori e alla vocalizzazione."
  },
  'border-collie.html': {
    meta: "Il Border Collie è considerato il cane più intelligente del mondo. Energico, atletico e devoto al lavoro.",
    hero: "Il Border Collie è considerato il cane più intelligente del mondo. Energico, atletico e incredibilmente devoto al lavoro e alla famiglia.",
    panoramica: "Il Border Collie è originario della regione di confine tra Scozia e Inghilterra, sviluppato per la conduzione del gregge. La loro intelligenza e istinto al lavoro li rendono eccellenti in agility, obedience e flyball.",
    temperamento: "I Border Collie sono estremamente intelligenti, energici e desiderosi di lavorare. Hanno bisogno di stimolazione mentale costante. Possono essere riservati con gli estranei ma sono devoti alla famiglia.",
    salute: "Predisposti a displasia dell'anca, anomalia dell'occhio del Collie (CEA) e epilessia. Alcuni portano il gene MDR1 che causa sensibilità a certi farmaci. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio molto elevate. Richiedono almeno 2 ore di attività intensa al giorno. Eccellono negli sport cinofili. Senza sfogo adeguato sviluppano comportamenti problematici.",
    verdetto: "Il Border Collie è ideale per proprietari molto attivi che possono offrire stimolazione mentale e fisica costante. Non adatto a proprietari sedentari o alla vita in appartamento."
  },
  'boxer.html': {
    meta: "Il Boxer è un cane atletico e giocherellone, noto per il suo carattere allegro e l'amore per le famiglie. Eccellente guardiano.",
    hero: "Il Boxer è un cane atletico e giocherellone, noto per il suo carattere allegro, l'energia inesauribile e l'amore incondizionato per la famiglia.",
    panoramica: "Il Boxer è una razza tedesca sviluppata nel XIX secolo incrociando il Bullenbeisser con il Bulldog. Originariamente usati per la caccia e la guardia, oggi sono amati cani da famiglia.",
    temperamento: "I Boxer sono giocherelloni, energici e affettuosi. Rimangono cuccioli nel cuore fino a tarda età. Sono protettivi con la famiglia e diffidenti con gli estranei. Ottimi con i bambini.",
    salute: "Predisposti a cardiomiopatia, displasia dell'anca, ipotiroidismo e alcuni tumori. Il muso corto può causare problemi respiratori. Aspettativa di vita 10-12 anni.",
    esercizio: "Elevate esigenze di esercizio. Necessitano di attività vigorose quotidiane. Sensibili al caldo a causa del muso corto. Adorano giocare e correre.",
    verdetto: "Il Boxer è un eccellente cane da famiglia, giocherellone e protettivo. Adatto a famiglie attive con bambini. Richiede esercizio regolare e attenzione alla salute."
  },
  'bulldog.html': {
    meta: "Il Bulldog Inglese è un cane dal carattere dolce e dignitoso, noto per il suo aspetto distintivo e la personalità affettuosa.",
    hero: "Il Bulldog Inglese è un cane dal carattere dolce e dignitoso, amato per il suo aspetto unico e la personalità calma e affettuosa.",
    panoramica: "Il Bulldog Inglese, un tempo feroce combattente di tori, oggi è un compagno dolce e amabile. La razza è stata trasformata attraverso l'allevamento selettivo in un cane da famiglia affettuoso.",
    temperamento: "I Bulldog sono calmi, coraggiosi e affettuosi. Hanno una natura dignitosa ma anche un lato giocherellone. Sono ottimi con i bambini e si adattano bene alla vita in appartamento.",
    salute: "Predisposti a molti problemi di salute: difficoltà respiratorie, displasia dell'anca, problemi cutanei e cardiaci. Sensibili al caldo. Aspettativa di vita 8-10 anni.",
    esercizio: "Esigenze di esercizio basse. Passeggiate brevi sono sufficienti. Evitare l'esercizio in climi caldi. Preferiscono il divano alle lunghe camminate.",
    verdetto: "Il Bulldog è un compagno affettuoso e rilassato, perfetto per la vita in appartamento. Attenzione ai costi veterinari elevati e ai problemi di salute tipici della razza."
  },
  'cavalier-king-charles-spaniel.html': {
    meta: "Il Cavalier King Charles Spaniel è un elegante cane da compagnia, noto per la sua dolcezza e l'amore per le coccole.",
    hero: "Il Cavalier King Charles Spaniel è un elegante cane da compagnia, adorato per la sua natura affettuosa, dolce e il suo aspetto regale.",
    panoramica: "Il Cavalier King Charles Spaniel prende il nome dal Re Carlo II d'Inghilterra, che amava profondamente questi cani. Sviluppati come cani da compagnia, eccellono nel ruolo di coccoloni di casa.",
    temperamento: "I Cavalier sono dolci, affettuosi e adattabili. Adorano stare con le persone e soffrono se lasciati soli. Sono amichevoli con tutti, inclusi estranei e altri animali.",
    salute: "Purtroppo predisposti a gravi problemi cardiaci (MVD) e siringomielia. Controlli cardiaci regolari sono essenziali. Aspettativa di vita 9-14 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono sufficienti. Si adattano allo stile di vita del proprietario, che sia attivo o tranquillo.",
    verdetto: "Il Cavalier è un compagno ideale per chi cerca un cane affettuoso e adattabile. Perfetto per anziani, famiglie e vita in appartamento. Attenzione ai problemi di salute della razza."
  },
  'chihuahua.html': {
    meta: "Il Chihuahua è il cane più piccolo del mondo, con una personalità grande quanto il suo coraggio. Leale e vivace.",
    hero: "Il Chihuahua è il cane più piccolo del mondo, ma possiede una personalità enorme, piena di coraggio, lealtà e vivacità.",
    panoramica: "Il Chihuahua prende il nome dallo stato messicano di Chihuahua. È la razza canina più piccola del mondo ma non manca di personalità. Erano considerati sacri dagli Aztechi e dai Toltechi.",
    temperamento: "I Chihuahua sono coraggiosi, vivaci e profondamente legati al loro proprietario. Possono essere diffidenti con gli estranei e altri cani. Spesso non si rendono conto delle loro piccole dimensioni.",
    salute: "Predisposti a lussazione della rotula, problemi cardiaci, ipoglicemia e problemi dentali. La fontanella può rimanere aperta. Aspettativa di vita 12-20 anni.",
    esercizio: "Esigenze di esercizio basse. Brevi passeggiate e gioco in casa sono sufficienti. Sensibili al freddo e necessitano di protezione.",
    verdetto: "Il Chihuahua è un compagno devoto perfetto per la vita in appartamento. Adatto a single e anziani. Non ideale per famiglie con bambini piccoli per le sue dimensioni delicate."
  },
  'cocker-spaniel.html': {
    meta: "Il Cocker Spaniel Americano è un cane allegro e affettuoso, con un mantello lussuoso e una natura giocherellona.",
    hero: "Il Cocker Spaniel Americano è un cane allegro e affettuoso, amato per il suo mantello setoso e la personalità gioiosa.",
    panoramica: "Il Cocker Spaniel Americano deriva dal Cocker Spaniel Inglese, sviluppato come cane da caccia per le beccacce (woodcock). Oggi è principalmente un amato cane da compagnia.",
    temperamento: "I Cocker sono allegri, affettuosi e desiderosi di piacere. Sono ottimi con i bambini e altri animali. Possono essere sensibili e rispondono meglio all'addestramento positivo.",
    salute: "Predisposti a problemi oculari (cataratta, glaucoma), otiti croniche, displasia dell'anca e problemi cardiaci. Aspettativa di vita 10-14 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono essenziali. Amano nuotare e riportare oggetti.",
    verdetto: "Il Cocker Spaniel è un eccellente cane da famiglia, allegro e adattabile. Richiede toelettatura regolare e attenzione alle orecchie. Perfetto per proprietari alle prime armi."
  },
  'dachshund.html': {
    meta: "Il Bassotto è un cane coraggioso e vivace con un corpo allungato distintivo. Intelligente, curioso e pieno di personalità.",
    hero: "Il Bassotto è un cane coraggioso e vivace con un corpo allungato distintivo, noto per la sua intelligenza e personalità audace.",
    panoramica: "Il Bassotto, letteralmente 'cane tasso' in tedesco, è stato sviluppato per cacciare tassi nelle loro tane. Il suo corpo allungato e le zampe corte erano perfetti per seguire la preda sottoterra.",
    temperamento: "I Bassotti sono coraggiosi, vivaci e testardi. Hanno una personalità forte nonostante le piccole dimensioni. Possono essere vocali e territoriali. Sono leali e affettuosi con la famiglia.",
    salute: "Molto predisposti a problemi alla schiena (IVDD) a causa della loro conformazione. Anche obesità, diabete e problemi dentali. Aspettativa di vita 12-16 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane ma evitare salti e scale che stressano la schiena. Mantenere il peso forma è cruciale.",
    verdetto: "Il Bassotto è un compagno vivace e coraggioso, adatto alla vita in appartamento. Richiede attenzione alla salute della schiena e controllo del peso. Può essere testardo nell'addestramento."
  },
  'dalmatian.html': {
    meta: "Il Dalmata è un cane elegante e atletico, famoso per il suo mantello a macchie unico. Energico, intelligente e devoto.",
    hero: "Il Dalmata è un cane elegante e atletico, immediatamente riconoscibile per il suo splendido mantello bianco a macchie nere.",
    panoramica: "Il Dalmata ha una storia misteriosa, ma è associato alla Dalmazia (Croazia). Erano cani da carrozza, correndo accanto ai cavalli. La loro associazione con i pompieri deriva da questo ruolo.",
    temperamento: "I Dalmata sono energici, intelligenti e sensibili. Possono essere riservati con gli estranei ma sono devoti alla famiglia. Necessitano di molta stimolazione mentale e fisica.",
    salute: "Predisposti a sordità (8-12% sono sordi), calcoli urinari e allergie. Richiedono una dieta specifica a basso contenuto di purine. Aspettativa di vita 11-13 anni.",
    esercizio: "Esigenze di esercizio molto elevate. Necessitano di almeno 2 ore di attività al giorno. Eccellenti compagni per la corsa e le attività all'aperto.",
    verdetto: "Il Dalmata è ideale per proprietari molto attivi che possono offrire esercizio intenso. Non adatto a proprietari sedentari o vita in appartamento senza adeguato sfogo."
  },
  'doberman-pinscher.html': {
    meta: "Il Dobermann è un cane atletico, intelligente e leale, noto per le sue capacità di guardia e la devozione alla famiglia.",
    hero: "Il Dobermann è un cane atletico, intelligente e leale, combinando eleganza, potenza e una profonda devozione alla famiglia.",
    panoramica: "Il Dobermann è stato sviluppato in Germania da Karl Friedrich Louis Dobermann alla fine del 1800. Voleva un cane da protezione intelligente e leale. Il risultato è una delle razze più versatili.",
    temperamento: "I Dobermann sono intelligenti, leali e vigili. Sono protettivi con la famiglia ma possono essere amichevoli quando ben socializzati. Sensibili e rispondono meglio all'addestramento positivo.",
    salute: "Predisposti a cardiomiopatia dilatativa, displasia dell'anca, sindrome di von Willebrand e ipotiroidismo. Controlli cardiaci regolari sono essenziali. Aspettativa di vita 10-12 anni.",
    esercizio: "Elevate esigenze di esercizio. Necessitano di attività fisica e mentale quotidiana. Eccellono in obedience, agility e protezione sportiva.",
    verdetto: "Il Dobermann è un compagno leale e protettivo per proprietari esperti. Richiede addestramento costante, socializzazione e molto esercizio. Non adatto a proprietari alle prime armi."
  },
  'french-bulldog.html': {
    meta: "Il Bulldog Francese è un compagno affettuoso e giocherellone, noto per le sue orecchie a pipistrello e la personalità allegra.",
    hero: "Il Bulldog Francese è un compagno affettuoso e giocherellone, amato per le sue caratteristiche orecchie a pipistrello e la natura allegra.",
    panoramica: "Il Bulldog Francese discende dai Bulldog Inglesi portati in Francia dai merlettai di Nottingham. In Francia, furono incrociati con razze locali creando il 'Bouledogue Français'.",
    temperamento: "I Frenchie sono affettuosi, giocherelloni e adattabili. Adorano stare con le persone e sono ottimi cani da appartamento. Sono divertenti e amano essere al centro dell'attenzione.",
    salute: "Predisposti a problemi respiratori (BOAS), problemi alla colonna vertebrale, allergie e colpo di calore. I costi veterinari possono essere elevati. Aspettativa di vita 10-12 anni.",
    esercizio: "Esigenze di esercizio basse. Brevi passeggiate e gioco sono sufficienti. Evitare esercizio in climi caldi. Sensibili al caldo e al freddo.",
    verdetto: "Il Bulldog Francese è perfetto per la vita in appartamento e proprietari meno attivi. Affettuoso e divertente, ma richiede attenzione ai costi veterinari e ai problemi respiratori."
  },
  'german-shepherd.html': {
    meta: "Il Pastore Tedesco è un cane da lavoro intelligente e versatile, noto per il suo coraggio, lealtà e capacità di addestramento.",
    hero: "Il Pastore Tedesco è un cane da lavoro intelligente e versatile, apprezzato per il suo coraggio, lealtà e versatilità in ogni campo.",
    panoramica: "Il Pastore Tedesco è stato sviluppato in Germania alla fine del 1800 per la conduzione del gregge. La loro forza, intelligenza e addestrabilità li hanno resi ideali per polizia, militari e soccorso.",
    temperamento: "I Pastori Tedeschi sono sicuri, coraggiosi e intelligenti. Sono disposti a rischiare la vita per i loro cari. Possono essere riservati con gli estranei ma sono leali e amorevoli con la famiglia.",
    salute: "Predisposti a displasia dell'anca e del gomito, mielopatia degenerativa e torsione gastrica. Controlli veterinari regolari sono importanti. Acquistare da allevatori che testano per le condizioni genetiche.",
    esercizio: "Elevate esigenze di esercizio che richiedono almeno un'ora di attività vigorosa al giorno. Eccellono in agility, obedience e lavoro. La stimolazione mentale è altrettanto importante.",
    verdetto: "Il Pastore Tedesco è un cane leale, intelligente e versatile. Ideale per proprietari esperti che possono offrire leadership, addestramento costante e molto esercizio. Non adatto a proprietari alle prime armi o vita in appartamento."
  },
  'golden-retriever.html': {
    meta: "Il Golden Retriever è il cane da famiglia per eccellenza, noto per la sua natura amichevole, intelligenza e bellezza dorata.",
    hero: "Il Golden Retriever è il cane da famiglia per eccellenza, amato per la sua natura amichevole, gentile e la sua intelligenza.",
    panoramica: "Il Golden Retriever è stato sviluppato in Scozia nel XIX secolo come cane da riporto per la caccia. Oggi è una delle razze più popolari al mondo, eccellendo come cane da famiglia, da terapia e da assistenza.",
    temperamento: "I Golden sono amichevoli, affidabili e desiderosi di piacere. Sono ottimi con bambini, altri animali e tutti quelli che incontrano. Sono intelligenti e facili da addestrare.",
    salute: "Predisposti a displasia dell'anca e del gomito, problemi cardiaci, cataratta e alcuni tumori. Controlli regolari sono importanti. Aspettativa di vita 10-12 anni.",
    esercizio: "Elevate esigenze di esercizio. Necessitano di almeno un'ora di attività al giorno. Adorano nuotare, riportare oggetti e le attività all'aperto.",
    verdetto: "Il Golden Retriever è un eccellente cane da famiglia, affettuoso, paziente e facile da addestrare. Perfetto per famiglie con bambini e proprietari alle prime armi. Richiede molto esercizio e perdono molto pelo."
  },
  'labrador-retriever.html': {
    meta: "Il Labrador Retriever è la razza canina più popolare d'America per ottime ragioni. Amichevoli, estroversi e pieni di energia.",
    hero: "Il Labrador Retriever è la razza canina più popolare d'America per ottime ragioni. Sono compagni amichevoli, estroversi e pieni di energia.",
    panoramica: "Il Labrador Retriever è la razza canina più popolare d'America per ottime ragioni. Sono compagni amichevoli, estroversi e pieni di affetto per chiunque cerchi un cane di taglia medio-grande.",
    temperamento: "I Labrador sono famosi per la loro cordialità. Sono compagni di casa affettuosi che legano con tutta la famiglia, e socializzano bene con i cani e le persone del vicinato. Ma non confondete la loro personalità rilassata con poca energia.",
    salute: "Generalmente sani, ma predisposti a displasia dell'anca e del gomito, disturbi cardiaci, problemi oculari e collasso indotto dall'esercizio. L'obesità è comune, quindi controllate la loro dieta.",
    esercizio: "Razza ad alta energia che richiede esercizio quotidiano vigoroso—almeno un'ora di attività. Prosperano con famiglie attive che amano le attività all'aperto. La stimolazione mentale attraverso l'addestramento e i giochi puzzle è altrettanto importante. Senza esercizio adeguato, possono sviluppare problemi comportamentali.",
    verdetto: "Il cane da famiglia definitivo. I Labrador Retriever sono amichevoli, pazienti e facili da addestrare—perfetti per proprietari alle prime armi e famiglie con bambini. Hanno bisogno di molto esercizio e perdono molto pelo, ma la loro natura amorevole ne vale la pena."
  },
  'poodle.html': {
    meta: "Il Barboncino è un cane elegante e altamente intelligente, disponibile in tre taglie. Eccelle in addestramento e non perde pelo.",
    hero: "Il Barboncino è un cane elegante e altamente intelligente, noto per il suo mantello ipoallergenico e la versatilità eccezionale.",
    panoramica: "Il Barboncino, nonostante l'associazione con la Francia, ha origini tedesche come cane da riporto in acqua. Il nome deriva dal tedesco 'Pudel' (sguazzare). Disponibile in tre taglie: Standard, Miniatura e Toy.",
    temperamento: "I Barboncini sono estremamente intelligenti, attivi e orgogliosi. Sono eccellenti cani da famiglia, affettuosi e giocherelloni. Imparano rapidamente e adorano compiacere i loro proprietari.",
    salute: "Predisposti a displasia dell'anca, epilessia, problemi oculari e malattia di Addison. La taglia Toy può avere problemi alle rotule. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate-alte a seconda della taglia. I Barboncini Standard necessitano di più attività. Eccellono negli sport cinofili e nella stimolazione mentale.",
    verdetto: "Il Barboncino è un compagno versatile e intelligente, perfetto per chi cerca un cane che non perde pelo. Richiede toelettatura regolare e stimolazione mentale. Adatto a diverse situazioni abitative."
  },
  'pug.html': {
    meta: "Il Carlino è un piccolo cane affettuoso con una grande personalità, famoso per il suo muso rugoso e la natura allegra.",
    hero: "Il Carlino è un piccolo cane affettuoso con una grande personalità, amato per il suo aspetto espressivo e la natura socievole.",
    panoramica: "Il Carlino è una razza antica originaria della Cina, dove era il compagno preferito degli imperatori. Arrivato in Europa nel XVI secolo, divenne popolare tra la nobiltà olandese e britannica.",
    temperamento: "I Carlini sono affettuosi, allegri e birichini. Adorano stare con le persone e odiano essere lasciati soli. Sono ottimi con bambini e altri animali. Amano il cibo e le coccole.",
    salute: "Predisposti a molti problemi: difficoltà respiratorie (BOAS), problemi oculari, obesità, problemi cutanei e displasia dell'anca. Sensibili al caldo. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio basse. Brevi passeggiate e gioco sono sufficienti. Evitare sforzi in climi caldi. Tendenza all'obesità richiede controllo della dieta.",
    verdetto: "Il Carlino è un compagno affettuoso perfetto per la vita in appartamento. Adatto a famiglie e anziani. Attenzione ai problemi respiratori e al controllo del peso."
  },
  'rottweiler.html': {
    meta: "Il Rottweiler è un cane potente e leale, noto per la sua natura protettiva e l'intelligenza. Eccellente guardiano della famiglia.",
    hero: "Il Rottweiler è un cane potente e leale, combinando forza, intelligenza e una profonda devozione verso la famiglia.",
    panoramica: "Il Rottweiler discende dai cani molossi romani, utilizzati per condurre il bestiame. La razza prende il nome dalla città tedesca di Rottweil. Erano usati come cani da macelleria e da traino.",
    temperamento: "I Rottweiler sono calmi, sicuri e coraggiosi. Sono protettivi con la famiglia ma possono essere amichevoli quando ben socializzati. Necessitano di una leadership chiara e costante.",
    salute: "Predisposti a displasia dell'anca e del gomito, problemi cardiaci, cancro e torsione gastrica. Controlli regolari sono importanti. Aspettativa di vita 8-10 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Necessitano di passeggiate quotidiane e attività mentali. Eccellono in obedience e protezione sportiva.",
    verdetto: "Il Rottweiler è un guardiano devoto e affettuoso per proprietari esperti. Richiede socializzazione precoce, addestramento costante e leadership ferma. Non adatto a proprietari alle prime armi."
  },
  'shiba-inu.html': {
    meta: "Lo Shiba Inu è un cane giapponese antico, noto per la sua personalità indipendente, l'aspetto da volpe e la lealtà.",
    hero: "Lo Shiba Inu è un cane giapponese antico, amato per il suo aspetto da volpe, la personalità audace e lo spirito indipendente.",
    panoramica: "Lo Shiba Inu è la più piccola e antica delle razze giapponesi originarie. Sviluppato per la caccia in montagna, il nome 'Shiba' può significare 'piccolo' o riferirsi al sottobosco in cui cacciavano.",
    temperamento: "Gli Shiba sono indipendenti, vigili e audaci. Possono essere riservati con gli estranei ma sono leali alla famiglia. Hanno una personalità forte e possono essere testardi.",
    salute: "Generalmente sani ma predisposti ad allergie, displasia dell'anca, lussazione della rotula e problemi oculari. Aspettativa di vita 13-16 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Hanno un forte istinto predatorio quindi necessitano di un'area recintata.",
    verdetto: "Lo Shiba Inu è un compagno indipendente e leale per proprietari che rispettano la sua natura autonoma. Richiede pazienza nell'addestramento. Non adatto a chi cerca un cane molto affettuoso."
  },
  'siberian-husky.html': {
    meta: "Il Siberian Husky è un cane da slitta atletico e amichevole, noto per i suoi occhi sorprendenti e la natura giocherellona.",
    hero: "Il Siberian Husky è un cane da slitta atletico e amichevole, famoso per i suoi occhi sorprendenti e l'energia inesauribile.",
    panoramica: "Il Siberian Husky è stato sviluppato dal popolo Ciukci della Siberia come cane da slitta resistente. Capaci di correre lunghe distanze in condizioni estreme, sono arrivati in Alaska durante la corsa all'oro.",
    temperamento: "Gli Husky sono amichevoli, giocherelloni e un po' birichini. Sono socievoli con tutti, rendendoli pessimi cani da guardia. Hanno una forte natura di branco e possono essere vocali.",
    salute: "Predisposti a problemi oculari (cataratta, glaucoma), displasia dell'anca e ipotiroidismo. Relativamente sani per la loro taglia. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio molto elevate. Costruiti per correre, necessitano di attività intensa quotidiana. Eccellono nel canicross, bikejoring e sleddog. Senza sfogo tendono a fuggire e distruggere.",
    verdetto: "Il Siberian Husky è ideale per proprietari molto attivi in climi freschi. Richiede enormi quantità di esercizio e attenzione alla sicurezza (tendenza alla fuga). Non adatto a climi caldi o proprietari sedentari."
  },
  'yorkshire-terrier.html': {
    meta: "Lo Yorkshire Terrier è un piccolo cane elegante con una grande personalità. Coraggioso, affettuoso e pieno di energia.",
    hero: "Lo Yorkshire Terrier è un piccolo cane elegante con una grande personalità, noto per il suo splendido mantello setoso e il carattere vivace.",
    panoramica: "Lo Yorkshire Terrier è stato sviluppato nel XIX secolo nello Yorkshire, in Inghilterra, dai lavoratori tessili per cacciare i topi nelle fabbriche. Oggi è uno dei cani toy più popolari al mondo.",
    temperamento: "Gli Yorkie sono coraggiosi, vivaci e affettuosi. Non si rendono conto delle loro piccole dimensioni e possono essere territoriali. Sono leali ai loro proprietari e possono essere vocali.",
    salute: "Predisposti a lussazione della rotula, ipoglicemia, collasso tracheale e problemi dentali. La fontanella può rimanere aperta. Aspettativa di vita 11-15 anni.",
    esercizio: "Esigenze di esercizio basse-moderate. Passeggiate brevi e gioco in casa sono sufficienti. Nonostante la taglia, hanno energia da terrier.",
    verdetto: "Lo Yorkshire Terrier è un compagno vivace e affettuoso, perfetto per la vita in appartamento. Richiede toelettatura regolare del mantello. Adatto a single e anziani, meno a famiglie con bambini piccoli."
  }
};

function translateFile(filename) {
  const filepath = path.join(breedsDir, filename);
  let content = fs.readFileSync(filepath, 'utf-8');
  
  const translations = breedTranslations[filename];
  if (!translations) return false;
  
  // Update meta description
  if (translations.meta) {
    content = content.replace(
      /<meta name="description" content="[^"]*">/,
      `<meta name="description" content="${translations.meta}">`
    );
  }
  
  // Update hero description
  if (translations.hero) {
    content = content.replace(
      /<p class="text-lg text-slate-600 mb-6">[^<]*<\/p>/,
      `<p class="text-lg text-slate-600 mb-6">${translations.hero}</p>`
    );
  }
  
  // Update Panoramica section
  if (translations.panoramica) {
    content = content.replace(
      /(<i data-lucide="book-open"[^>]*><\/i> Panoramica[\s\S]*?<div class="px-6 pb-6"><p class="text-slate-600">)[^<]*(<\/p><\/div>)/,
      `$1${translations.panoramica}$2`
    );
  }
  
  // Update Temperamento section
  if (translations.temperamento) {
    content = content.replace(
      /(<i data-lucide="heart" class="w-5 h-5 text-sky-500"><\/i> Temperamento[\s\S]*?<div class="px-6 pb-6"><p class="text-slate-600">)[^<]*(<\/p><\/div>)/,
      `$1${translations.temperamento}$2`
    );
  }
  
  // Update Salute section
  if (translations.salute) {
    content = content.replace(
      /(<i data-lucide="heart-pulse"[^>]*><\/i> Salute[\s\S]*?<div class="px-6 pb-6"><p class="text-slate-600">)[^<]*(<\/p><\/div>)/,
      `$1${translations.salute}$2`
    );
  }
  
  // Update Esercizio section
  if (translations.esercizio) {
    content = content.replace(
      /(<i data-lucide="activity"[^>]*><\/i> Esercizio[\s\S]*?<div class="px-6 pb-6"><p class="text-slate-600">)[^<]*(<\/p><\/div>)/,
      `$1${translations.esercizio}$2`
    );
  }
  
  // Update verdict
  if (translations.verdetto) {
    content = content.replace(
      /(<strong>Il Nostro Verdetto:<\/strong> )[^<]*(<\/p>)/,
      `$1${translations.verdetto}$2`
    );
  }
  
  fs.writeFileSync(filepath, content);
  console.log(`Translated: ${filename}`);
  return true;
}

const files = fs.readdirSync(breedsDir).filter(f => f.endsWith('.html'));
let translated = 0;
files.forEach(f => {
  if (translateFile(f)) translated++;
});
console.log(`\nTranslated ${translated} files with custom content`);
