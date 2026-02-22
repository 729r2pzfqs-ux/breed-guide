#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const breedsDir = path.join(__dirname, 'it/breeds');

const breedTranslations = {
  'american-english-coonhound.html': {
    meta: "L'American English Coonhound è un segugio atletico e resistente, noto per la sua velocità e l'eccezionale olfatto.",
    hero: "L'American English Coonhound è un segugio atletico e resistente, sviluppato per la caccia al procione nelle foreste americane.",
    panoramica: "L'American English Coonhound discende dai Foxhound inglesi portati in America. Furono sviluppati per la caccia al procione e alla volpe, con una resistenza e velocità eccezionali.",
    temperamento: "Gli American English Coonhound sono amichevoli, socievoli e pieni di energia. Sono ottimi con bambini e altri cani. Hanno un forte istinto da segugio e possono essere vocali.",
    salute: "Generalmente sani ma predisposti a displasia dell'anca, infezioni alle orecchie e problemi oculari. Aspettativa di vita 11-12 anni.",
    esercizio: "Esigenze di esercizio molto elevate. Necessitano di attività intensa quotidiana. Ideali per proprietari attivi e cacciatori.",
    verdetto: "L'American English Coonhound è ideale per proprietari attivi che amano le attività all'aperto. Richiede molto esercizio e socializzazione."
  },
  'american-foxhound.html': {
    meta: "L'American Foxhound è un segugio elegante e atletico, uno dei più antichi cani da caccia americani.",
    hero: "L'American Foxhound è un segugio elegante e atletico, noto per la sua resistenza e il temperamento dolce.",
    panoramica: "L'American Foxhound è una delle razze americane più antiche, sviluppata dai Foxhound inglesi portati dai coloni. George Washington contribuì allo sviluppo della razza.",
    temperamento: "Gli American Foxhound sono dolci, leali e indipendenti. Sono ottimi con bambini e altri cani. Hanno un forte istinto da branco e possono essere vocali.",
    salute: "Generalmente sani ma predisposti a displasia dell'anca, trombocitopatia e infezioni alle orecchie. Aspettativa di vita 11-13 anni.",
    esercizio: "Esigenze di esercizio molto elevate. Necessitano di molto spazio e attività quotidiana. Non adatti alla vita in appartamento.",
    verdetto: "L'American Foxhound è ideale per case rurali con molto spazio. Richiede esercizio intenso e compagnia, preferibilmente altri cani."
  },
  'american-hairless-terrier.html': {
    meta: "L'American Hairless Terrier è un terrier vivace e senza pelo, perfetto per chi soffre di allergie. Intelligente e affettuoso.",
    hero: "L'American Hairless Terrier è un terrier vivace e senza pelo, noto per la sua intelligenza e la natura affettuosa.",
    panoramica: "L'American Hairless Terrier è l'unica razza senza pelo originaria degli Stati Uniti. Nato da una mutazione nel Rat Terrier, è ideale per chi soffre di allergie.",
    temperamento: "Gli AHT sono intelligenti, curiosi e giocherelloni. Hanno la tipica energia terrier ma sono anche affettuosi e coccoloni. Ottimi cani da famiglia.",
    salute: "Predisposti a problemi cutanei (necessitano protezione solare), lussazione della rotula e problemi dentali. Aspettativa di vita 14-16 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono sufficienti. Proteggere dal sole e dal freddo.",
    verdetto: "L'American Hairless Terrier è perfetto per chi soffre di allergie. Richiede protezione dalla pelle esposta e cure regolari."
  },
  'american-water-spaniel.html': {
    meta: "L'American Water Spaniel è un cane da caccia versatile, eccellente in acqua. Energico, intelligente e affettuoso.",
    hero: "L'American Water Spaniel è un cane da caccia versatile, eccellente sia in acqua che sulla terraferma.",
    panoramica: "L'American Water Spaniel è stato sviluppato nel Wisconsin come cane da caccia versatile per le zone umide. È il cane di stato del Wisconsin.",
    temperamento: "Gli AWS sono energici, intelligenti e desiderosi di piacere. Sono affettuosi con la famiglia e possono essere riservati con gli estranei.",
    salute: "Predisposti a displasia dell'anca, problemi cardiaci, epilessia e alopecia. Aspettativa di vita 10-14 anni.",
    esercizio: "Esigenze di esercizio elevate. Amano nuotare e cacciare. Necessitano di attività fisica e mentale quotidiana.",
    verdetto: "L'American Water Spaniel è ideale per cacciatori e famiglie attive che amano l'acqua. Richiede esercizio e stimolazione mentale."
  },
  'anatolian-shepherd.html': {
    meta: "Il Pastore dell'Anatolia è un guardiano potente e indipendente, sviluppato per proteggere il bestiame dai predatori.",
    hero: "Il Pastore dell'Anatolia è un guardiano potente e indipendente, noto per la sua protezione instancabile del bestiame.",
    panoramica: "Il Pastore dell'Anatolia è originario della Turchia, dove protegge le greggi dai lupi e altri predatori da migliaia di anni. È uno dei cani da guardia più antichi.",
    temperamento: "I Pastori dell'Anatolia sono indipendenti, protettivi e territoriali. Sono devoti alla famiglia ma diffidenti con gli estranei. Richiedono un proprietario esperto.",
    salute: "Generalmente sani ma predisposti a displasia dell'anca, entropion e ipotiroidismo. Aspettativa di vita 11-13 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane sono importanti. Necessitano di molto spazio e un lavoro da fare.",
    verdetto: "Il Pastore dell'Anatolia è ideale per proprietari esperti con proprietà da proteggere. Non adatto alla vita in città o a proprietari inesperti."
  },
  'appenzeller-sennenhund.html': {
    meta: "L'Appenzeller Sennenhund è un bovaro svizzero agile e versatile. Energico, intelligente e ottimo guardiano.",
    hero: "L'Appenzeller Sennenhund è un bovaro svizzero agile e versatile, noto per la sua energia e versatilità.",
    panoramica: "L'Appenzeller Sennenhund è uno dei quattro Bovari Svizzeri, originario della regione di Appenzell. Era usato come cane da fattoria per la conduzione del bestiame e la guardia.",
    temperamento: "Gli Appenzeller sono energici, intelligenti e leali. Sono eccellenti cani da guardia e da lavoro. Possono essere riservati con gli estranei.",
    salute: "Generalmente sani ma predisposti a displasia dell'anca, problemi oculari ed entropion. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica e mentale quotidiana. Eccellono negli sport cinofili.",
    verdetto: "L'Appenzeller è ideale per proprietari attivi che possono offrire lavoro e stimolazione. Richiede socializzazione precoce."
  },
  'australian-terrier.html': {
    meta: "L'Australian Terrier è un piccolo terrier coraggioso e vivace. Intelligente, leale e pieno di personalità.",
    hero: "L'Australian Terrier è un piccolo terrier coraggioso e vivace, il primo terrier sviluppato in Australia.",
    panoramica: "L'Australian Terrier è stato sviluppato in Australia nel XIX secolo da vari terrier britannici. Era usato per cacciare serpenti e roditori nelle fattorie australiane.",
    temperamento: "Gli Australian Terrier sono coraggiosi, spiritosi e affettuosi. Hanno la tipica personalità terrier: audaci e un po' testardi. Sono leali alla famiglia.",
    salute: "Predisposti a diabete, lussazione della rotula e allergie cutanee. Aspettativa di vita 11-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Hanno più energia della loro taglia.",
    verdetto: "L'Australian Terrier è un compagno vivace e affettuoso, adatto a diverse situazioni abitative. Richiede socializzazione con altri animali."
  },
  'azawakh.html': {
    meta: "L'Azawakh è un levriero africano elegante e veloce. Riservato, leale e atleticamente magnifico.",
    hero: "L'Azawakh è un levriero africano elegante e veloce, originario del deserto del Sahel.",
    panoramica: "L'Azawakh è originario della regione del Sahel in Africa occidentale, dove i nomadi Tuareg lo usavano per la caccia e la guardia. È uno dei levrieri più rari.",
    temperamento: "Gli Azawakh sono riservati, indipendenti e leali. Sono affettuosi con la famiglia ma diffidenti con gli estranei. Formano legami molto forti.",
    salute: "Generalmente sani ma predisposti a epilessia, problemi cardiaci e sensibilità all'anestesia. Aspettativa di vita 10-12 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di spazio per correre. Non tollerano bene il freddo.",
    verdetto: "L'Azawakh è ideale per proprietari esperti che apprezzano la sua natura indipendente. Richiede socializzazione e spazio per correre."
  },
  'barbet.html': {
    meta: "Il Barbet è un cane d'acqua francese con un mantello riccio. Allegro, intelligente e amante dell'acqua.",
    hero: "Il Barbet è un cane d'acqua francese con un caratteristico mantello riccio, noto per la sua natura allegra.",
    panoramica: "Il Barbet è un'antica razza francese di cani d'acqua, antenato di molte razze moderne incluso il Barboncino. Il nome deriva da 'barbe' (barba) per il pelo sul muso.",
    temperamento: "I Barbet sono allegri, socievoli e intelligenti. Amano l'acqua e sono ottimi cani da famiglia. Sono facili da addestrare e desiderosi di piacere.",
    salute: "Predisposti a displasia dell'anca, problemi oculari ed epilessia. Il mantello richiede cure regolari. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Amano nuotare e le attività all'aperto. Necessitano di stimolazione fisica e mentale.",
    verdetto: "Il Barbet è un compagno allegro e versatile, ideale per famiglie attive. Il mantello richiede toelettatura regolare."
  },
  'basenji.html': {
    meta: "Il Basenji è il cane che non abbaia, con origini africane antiche. Indipendente, curioso e elegante.",
    hero: "Il Basenji è un cane elegante e antico, famoso per non abbaiare e per la sua natura indipendente.",
    panoramica: "Il Basenji è una delle razze più antiche, originaria del Congo. Conosciuto come il 'cane che non abbaia', emette invece un caratteristico yodel. Era usato per la caccia.",
    temperamento: "I Basenji sono indipendenti, curiosi e intelligenti. Sono affettuosi ma non eccessivamente dimostrativi. Hanno un forte istinto predatorio.",
    salute: "Predisposti a sindrome di Fanconi, atrofia retinica progressiva, ipotiroidismo e displasia dell'anca. Aspettativa di vita 13-14 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Necessitano di attività quotidiana e stimolazione mentale. Tendono a fuggire se non recintati.",
    verdetto: "Il Basenji è ideale per proprietari esperti che apprezzano un cane indipendente. Richiede pazienza nell'addestramento e un ambiente sicuro."
  },
  'beauceron.html': {
    meta: "Il Beauceron è un cane da pastore francese potente e versatile. Intelligente, coraggioso e devoto.",
    hero: "Il Beauceron è un cane da pastore francese potente e versatile, noto per la sua intelligenza e lealtà.",
    panoramica: "Il Beauceron è un'antica razza francese da pastore, usata per la conduzione del bestiame e la guardia. È conosciuto anche come Berger de Beauce o Bas Rouge per le sue marcature rosso fuoco.",
    temperamento: "I Beauceron sono intelligenti, coraggiosi e leali. Sono protettivi con la famiglia e possono essere riservati con gli estranei. Richiedono un proprietario esperto.",
    salute: "Predisposti a displasia dell'anca, dilatazione gastrica e problemi cardiaci. Aspettativa di vita 10-12 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di lavoro fisico e mentale quotidiano. Eccellono in molti sport cinofili.",
    verdetto: "Il Beauceron è ideale per proprietari esperti che possono offrire leadership e lavoro. Non adatto a proprietari inesperti."
  },
  'bedlington-terrier.html': {
    meta: "Il Bedlington Terrier ha l'aspetto di un agnello ma il cuore di un leone. Dolce, coraggioso e atletico.",
    hero: "Il Bedlington Terrier ha un aspetto unico simile a un agnello, ma nasconde un cuore coraggioso da terrier.",
    panoramica: "Il Bedlington Terrier è originario della città mineraria di Bedlington in Inghilterra. Era usato per la caccia a conigli e tassi, e anche per le corse.",
    temperamento: "I Bedlington sono dolci, vivaci e coraggiosi. Sono affettuosi con la famiglia ma possono essere combattivi con altri cani. Hanno un lato giocherellone.",
    salute: "Predisposti a tossicosi da rame (malattia ereditaria), displasia della retina e lussazione della rotula. Aspettativa di vita 11-16 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Sorprendentemente atletici.",
    verdetto: "Il Bedlington è un compagno affettuoso e unico, adatto a diverse situazioni. Richiede toelettatura professionale regolare."
  },
  'belgian-laekenois.html': {
    meta: "Il Laekenois Belga è il più raro dei pastori belgi. Intelligente, protettivo e versatile.",
    hero: "Il Laekenois Belga è il più raro dei quattro pastori belgi, con un caratteristico mantello ruvido.",
    panoramica: "Il Laekenois Belga è la varietà più rara dei pastori belgi, originaria della regione di Laeken. Era usato per la guardia e la custodia della biancheria nei prati.",
    temperamento: "I Laekenois sono intelligenti, vigili e protettivi. Sono devoti alla famiglia e possono essere riservati con gli estranei. Hanno bisogno di socializzazione.",
    salute: "Predisposti a displasia dell'anca e del gomito, problemi oculari ed epilessia. Aspettativa di vita 10-12 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica e mentale quotidiana. Eccellono negli sport cinofili.",
    verdetto: "Il Laekenois è ideale per proprietari esperti che possono offrire lavoro e stimolazione. Richiede socializzazione precoce."
  },
  'belgian-malinois.html': {
    meta: "Il Malinois Belga è un cane da lavoro eccezionale, usato da polizia e militari. Intelligente, energico e devoto.",
    hero: "Il Malinois Belga è un cane da lavoro eccezionale, noto per la sua intelligenza, energia e versatilità.",
    panoramica: "Il Malinois Belga è una delle quattro varietà di pastori belgi, originaria della città di Malines. Oggi è la scelta preferita di polizia e forze speciali in tutto il mondo.",
    temperamento: "I Malinois sono estremamente intelligenti, energici e devoti. Hanno un forte istinto al lavoro e necessitano di stimolazione costante. Sono protettivi con la famiglia.",
    salute: "Predisposti a displasia dell'anca e del gomito, problemi oculari ed epilessia. Aspettativa di vita 14-16 anni.",
    esercizio: "Esigenze di esercizio molto elevate. Necessitano di ore di attività fisica e mentale. Non adatti a proprietari sedentari.",
    verdetto: "Il Malinois è ideale per proprietari molto esperti che possono offrire lavoro intenso. Non adatto come semplice cane da compagnia."
  },
  'belgian-sheepdog.html': {
    meta: "Il Pastore Belga Groenendael è elegante e intelligente con un magnifico mantello nero. Devoto e versatile.",
    hero: "Il Pastore Belga Groenendael è elegante e intelligente, con un magnifico mantello nero fluente.",
    panoramica: "Il Groenendael è la varietà a pelo lungo nero del pastore belga, prende il nome dal villaggio del suo primo allevatore. È versatile nel lavoro e come compagno.",
    temperamento: "I Groenendael sono intelligenti, sensibili e devoti. Sono protettivi con la famiglia e possono essere riservati con gli estranei. Richiedono socializzazione.",
    salute: "Predisposti a displasia dell'anca e del gomito, problemi oculari ed epilessia. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica e mentale quotidiana. Eccellono in obedience e agility.",
    verdetto: "Il Groenendael è ideale per proprietari attivi che possono offrire lavoro e compagnia. Richiede toelettatura regolare."
  },
  'belgian-tervuren.html': {
    meta: "Il Tervuren Belga è elegante e intelligente con un ricco mantello fulvo. Energico, devoto e versatile.",
    hero: "Il Tervuren Belga è elegante e intelligente, con un ricco mantello fulvo a punte nere.",
    panoramica: "Il Tervuren è la varietà a pelo lungo fulvo del pastore belga, originaria del villaggio di Tervuren. È conosciuto per la sua bellezza e versatilità nel lavoro.",
    temperamento: "I Tervuren sono intelligenti, energici e devoti. Sono protettivi e sensibili. Formano legami molto forti con il proprietario.",
    salute: "Predisposti a displasia dell'anca e del gomito, problemi oculari ed epilessia. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica e mentale quotidiana. Eccellono negli sport cinofili.",
    verdetto: "Il Tervuren è ideale per proprietari esperti che possono offrire lavoro e compagnia costante. Bellissimo ma impegnativo."
  },
  'bergamasco-sheepdog.html': {
    meta: "Il Pastore Bergamasco è un cane unico con il caratteristico mantello a 'feltro'. Intelligente, paziente e devoto.",
    hero: "Il Pastore Bergamasco è unico nel suo genere, con il caratteristico mantello che forma naturalmente 'cordoni' di pelo.",
    panoramica: "Il Pastore Bergamasco è originario delle Alpi bergamasche in Italia. Il suo mantello unico a 'feltro' lo proteggeva dal freddo e dai predatori durante la guardia del gregge.",
    temperamento: "I Bergamaschi sono intelligenti, pazienti e protettivi. Sono indipendenti ma devoti alla famiglia. Sono ottimi con i bambini.",
    salute: "Generalmente sani ma predisposti a displasia dell'anca e problemi oculari. Il mantello richiede cure specifiche. Aspettativa di vita 13-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Preferiscono avere un lavoro da fare.",
    verdetto: "Il Pastore Bergamasco è un compagno unico e affettuoso per chi apprezza il suo aspetto distintivo. Il mantello richiede cura specifica."
  },
  'berger-picard.html': {
    meta: "Il Berger Picard è un antico cane da pastore francese con un aspetto rustico. Leale, intelligente e pieno di carattere.",
    hero: "Il Berger Picard è un antico cane da pastore francese, noto per il suo aspetto rustico e la personalità vivace.",
    panoramica: "Il Berger Picard è una delle più antiche razze da pastore francesi, originaria della Piccardia. Quasi estinto dopo le guerre mondiali, sta lentamente recuperando.",
    temperamento: "I Picard sono leali, energici e un po' testardi. Hanno un grande senso dell'umorismo e sono ottimi cani da famiglia. Possono essere riservati con gli estranei.",
    salute: "Generalmente sani ma predisposti a displasia dell'anca e atrofia retinica progressiva. Aspettativa di vita 12-13 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e attività mentale sono importanti. Amano avere un lavoro.",
    verdetto: "Il Berger Picard è un compagno rustico e affettuoso per famiglie attive. Richiede pazienza nell'addestramento."
  },
  'biewer-terrier.html': {
    meta: "Il Biewer Terrier è un piccolo cane elegante derivato dallo Yorkshire. Giocherellone, affettuoso e vivace.",
    hero: "Il Biewer Terrier è un piccolo cane elegante, noto per il suo splendido mantello tricolore e la personalità vivace.",
    panoramica: "Il Biewer Terrier è nato in Germania negli anni '80 da Yorkshire Terrier con una rara colorazione pezzata. È riconosciuto come razza separata dal 2021.",
    temperamento: "I Biewer sono giocherelloni, affettuosi e vivaci. Adorano la compagnia e sono ottimi cani da appartamento. Hanno la tipica personalità terrier.",
    salute: "Predisposti a lussazione della rotula, ipoglicemia, problemi dentali e shunt portosistemico. Aspettativa di vita 16 anni.",
    esercizio: "Esigenze di esercizio basse-moderate. Brevi passeggiate e gioco sono sufficienti. Si adattano bene alla vita in appartamento.",
    verdetto: "Il Biewer Terrier è un compagno elegante e affettuoso per chi cerca un cane toy vivace. Richiede toelettatura regolare."
  },
  'black-and-tan-coonhound.html': {
    meta: "Il Black and Tan Coonhound è un segugio americano con un olfatto eccezionale. Amichevole, rilassato e vocale.",
    hero: "Il Black and Tan Coonhound è un segugio americano elegante, famoso per il suo olfatto eccezionale e la voce melodiosa.",
    panoramica: "Il Black and Tan Coonhound è uno dei sei coonhound americani, discendente dai Foxhound e Bloodhound. È stato sviluppato per seguire il procione di notte.",
    temperamento: "I Black and Tan sono amichevoli, rilassati e socievoli. Sono ottimi con bambini e altri cani. Sono vocali e amano seguire le tracce.",
    salute: "Predisposti a displasia dell'anca, infezioni alle orecchie ed ectropion. Aspettativa di vita 10-12 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di molto spazio e attività quotidiana. Amano seguire le tracce.",
    verdetto: "Il Black and Tan Coonhound è ideale per case rurali e famiglie attive. Richiede spazio e tolleranza per la vocalizzazione."
  },
  'black-russian-terrier.html': {
    meta: "Il Terrier Nero Russo è un cane potente e protettivo, sviluppato in Unione Sovietica. Coraggioso, intelligente e leale.",
    hero: "Il Terrier Nero Russo è un cane potente e maestoso, sviluppato come guardiano per le forze armate sovietiche.",
    panoramica: "Il Terrier Nero Russo è stato creato in URSS negli anni '40 incrociando varie razze tra cui Giant Schnauzer, Airedale e Rottweiler. Era il 'cane da guardia' dell'Armata Rossa.",
    temperamento: "I BRT sono coraggiosi, intelligenti e protettivi. Sono devoti alla famiglia e riservati con gli estranei. Richiedono un proprietario esperto.",
    salute: "Predisposti a displasia dell'anca e del gomito, problemi cardiaci e allergie. Aspettativa di vita 10-12 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e attività mentale sono importanti. Necessitano di socializzazione.",
    verdetto: "Il Terrier Nero Russo è un guardiano formidabile per proprietari esperti. Richiede addestramento, socializzazione e spazio."
  },
  'bloodhound.html': {
    meta: "Il Bloodhound ha l'olfatto più potente del mondo canino. Dolce, paziente e instancabile nelle ricerche.",
    hero: "Il Bloodhound ha l'olfatto più potente del mondo canino, capace di seguire tracce vecchie di giorni.",
    panoramica: "Il Bloodhound è una razza antichissima, probabilmente sviluppata dai monaci belgi. Il suo olfatto è così accurato che le sue tracce sono ammesse come prove in tribunale.",
    temperamento: "I Bloodhound sono dolci, pazienti e determinati. Sono affettuosi con tutti ma possono essere testardi. Una volta su una traccia, nulla li ferma.",
    salute: "Predisposti a torsione gastrica, displasia dell'anca, entropion e infezioni cutanee e alle orecchie. Aspettativa di vita 10-12 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Amano seguire le tracce. Necessitano di un'area sicura perché seguono l'olfatto.",
    verdetto: "Il Bloodhound è ideale per chi apprezza un cane dolce ma indipendente. Richiede pazienza, spazio e tolleranza per la bava."
  },
  'bluetick-coonhound.html': {
    meta: "Il Bluetick Coonhound è un segugio americano con un mantello maculato distintivo. Amichevole, leale e vocale.",
    hero: "Il Bluetick Coonhound è un segugio americano con un bellissimo mantello maculato blu, noto per la sua voce melodiosa.",
    panoramica: "Il Bluetick Coonhound discende dai Bleu de Gascogne francesi e dai Foxhound inglesi. È stato sviluppato negli Stati Uniti per la caccia al procione.",
    temperamento: "I Bluetick sono amichevoli, leali e intelligenti. Sono ottimi cani da famiglia ma hanno un forte istinto da segugio. Sono vocali.",
    salute: "Predisposti a displasia dell'anca, torsione gastrica e malattia di Krabbe. Aspettativa di vita 11-12 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di molto spazio e attività quotidiana. Amano seguire le tracce.",
    verdetto: "Il Bluetick Coonhound è ideale per case rurali e cacciatori. Richiede spazio, esercizio e tolleranza per l'abbaio."
  },
  'boerboel.html': {
    meta: "Il Boerboel è un mastino sudafricano potente e protettivo. Calmo, sicuro e devoto alla famiglia.",
    hero: "Il Boerboel è un mastino sudafricano potente e maestoso, noto per la sua natura protettiva e la devozione alla famiglia.",
    panoramica: "Il Boerboel è stato sviluppato in Sudafrica dai coloni olandesi per proteggere le fattorie dai predatori. Il nome significa 'cane da fattoria' in afrikaans.",
    temperamento: "I Boerboel sono calmi, sicuri e protettivi. Sono devoti alla famiglia e ottimi con i bambini. Richiedono un proprietario esperto e dominante.",
    salute: "Predisposti a displasia dell'anca e del gomito, problemi cardiaci ed entropion. Aspettativa di vita 9-11 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Necessitano di spazio.",
    verdetto: "Il Boerboel è un guardiano formidabile per proprietari esperti. Richiede socializzazione precoce, addestramento e molto spazio."
  },
  'bolognese.html': {
    meta: "Il Bolognese è un piccolo cane italiano con un soffice mantello bianco. Dolce, devoto e compagno ideale.",
    hero: "Il Bolognese è un piccolo cane italiano elegante, noto per il suo soffice mantello bianco e la natura affettuosa.",
    panoramica: "Il Bolognese è un'antica razza italiana, parte della famiglia Bichon. Era il preferito della nobiltà rinascimentale, inclusi i Medici e i Gonzaga.",
    temperamento: "I Bolognese sono dolci, devoti e calmi. Sono meno attivi di altri Bichon e preferiscono stare vicino al proprietario. Possono soffrire d'ansia da separazione.",
    salute: "Predisposti a lussazione della rotula, problemi oculari e allergie. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio basse. Brevi passeggiate e gioco in casa sono sufficienti. Si adattano perfettamente alla vita in appartamento.",
    verdetto: "Il Bolognese è un compagno devoto e tranquillo, perfetto per chi cerca un cane da compagnia affettuoso. Richiede toelettatura regolare."
  },
  'border-terrier.html': {
    meta: "Il Border Terrier è un piccolo terrier robusto con una grande personalità. Affettuoso, energico e adattabile.",
    hero: "Il Border Terrier è un piccolo terrier robusto, noto per la sua personalità allegra e il carattere affettuoso.",
    panoramica: "Il Border Terrier è originario del confine tra Scozia e Inghilterra (le 'Borders'). Era usato per la caccia alla volpe, abbastanza piccolo da entrare nelle tane.",
    temperamento: "I Border Terrier sono affettuosi, energici e adattabili. Sono meno testardi di altri terrier. Sono ottimi cani da famiglia.",
    salute: "Predisposti a displasia dell'anca, lussazione della rotula, problemi cardiaci e CECS (sindrome dell'epilessia). Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Hanno più resistenza della loro taglia.",
    verdetto: "Il Border Terrier è un compagno versatile e affettuoso, adatto a famiglie e diversi stili di vita. Richiede stripping del mantello."
  },
  'borzoi.html': {
    meta: "Il Borzoi è un levriero russo elegante e aristocratico. Calmo, indipendente e magnificamente aggraziato.",
    hero: "Il Borzoi è un levriero russo elegante e aristocratico, noto per la sua grazia e il portamento regale.",
    panoramica: "Il Borzoi, conosciuto anche come Levriero Russo, era usato dall'aristocrazia russa per la caccia ai lupi. La razza quasi scomparve con la Rivoluzione Russa.",
    temperamento: "I Borzoi sono calmi, indipendenti e affettuosi. Sono riservati con gli estranei ma dolci con la famiglia. Hanno un forte istinto predatorio.",
    salute: "Predisposti a torsione gastrica, problemi cardiaci e osteosarcoma. Sensibili all'anestesia. Aspettativa di vita 9-14 anni.",
    esercizio: "Esigenze di esercizio moderate. Amano correre ma sono anche felici di rilassarsi. Necessitano di un'area recintata sicura.",
    verdetto: "Il Borzoi è un compagno elegante e tranquillo per chi apprezza la sua natura indipendente. Non adatto a case con piccoli animali."
  },
  'bouvier-des-flandres.html': {
    meta: "Il Bouvier des Flandres è un cane da lavoro potente e versatile. Calmo, coraggioso e protettivo.",
    hero: "Il Bouvier des Flandres è un cane da lavoro potente e versatile, originario del Belgio e della Francia.",
    panoramica: "Il Bouvier des Flandres era il cane da fattoria multiuso delle Fiandre, usato per la conduzione del bestiame, il traino e la guardia. Il nome significa 'bovaro delle Fiandre'.",
    temperamento: "I Bouvier sono calmi, coraggiosi e leali. Sono protettivi con la famiglia e riservati con gli estranei. Sono versatili e intelligenti.",
    salute: "Predisposti a displasia dell'anca, torsione gastrica, ipotiroidismo e cancro. Aspettativa di vita 10-12 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e attività mentale sono importanti. Amano avere un lavoro.",
    verdetto: "Il Bouvier des Flandres è un compagno leale e protettivo per proprietari esperti. Richiede toelettatura regolare e socializzazione."
  },
  'boykin-spaniel.html': {
    meta: "Il Boykin Spaniel è un cane da caccia americano versatile e amichevole. Energico, intelligente e amante dell'acqua.",
    hero: "Il Boykin Spaniel è un cane da caccia americano versatile, noto per la sua abilità in acqua e la natura allegra.",
    panoramica: "Il Boykin Spaniel è stato sviluppato in South Carolina per la caccia nelle paludi. È il cane di stato della South Carolina, amato per la sua versatilità.",
    temperamento: "I Boykin sono energici, amichevoli e desiderosi di piacere. Sono eccellenti cani da famiglia e compagni di caccia. Amano l'acqua.",
    salute: "Predisposti a displasia dell'anca, problemi cardiaci, cataratta e miopatia indotta dall'esercizio. Aspettativa di vita 10-15 anni.",
    esercizio: "Esigenze di esercizio elevate. Amano nuotare e cacciare. Necessitano di attività fisica quotidiana.",
    verdetto: "Il Boykin Spaniel è ideale per famiglie attive e cacciatori. Richiede esercizio regolare e stimolazione mentale."
  },
  'bracco-italiano.html': {
    meta: "Il Bracco Italiano è un antico cane da caccia italiano, elegante e versatile. Docile, intelligente e affettuoso.",
    hero: "Il Bracco Italiano è un antico cane da caccia italiano, noto per la sua eleganza e versatilità sul campo.",
    panoramica: "Il Bracco Italiano è una delle razze da caccia più antiche, con origini che risalgono al IV-V secolo. Era il preferito della nobiltà italiana per la caccia agli uccelli.",
    temperamento: "I Bracco sono docili, intelligenti e affettuosi. Sono ottimi cani da famiglia e compagni di caccia. Sono sensibili e rispondono bene all'addestramento positivo.",
    salute: "Predisposti a displasia dell'anca e del gomito, entropion, problemi alle orecchie e torsione gastrica. Aspettativa di vita 10-14 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica quotidiana e stimolazione mentale. Eccellono nella caccia.",
    verdetto: "Il Bracco Italiano è un compagno elegante e affettuoso per famiglie attive. Richiede esercizio regolare e attenzione alle orecchie."
  },
  'briard.html': {
    meta: "Il Briard è un antico cane da pastore francese con un mantello lussuoso. Leale, protettivo e affettuoso.",
    hero: "Il Briard è un antico cane da pastore francese, noto per il suo magnifico mantello lungo e la devozione alla famiglia.",
    panoramica: "Il Briard è una delle razze da pastore francesi più antiche, usata da secoli per la conduzione e la protezione del gregge. Napoleone e Lafayette possedevano Briard.",
    temperamento: "I Briard sono leali, protettivi e affettuosi. Sono ottimi con i bambini e protettivi con la famiglia. Possono essere riservati con gli estranei.",
    salute: "Predisposti a displasia dell'anca, torsione gastrica, atrofia retinica progressiva e ipotiroidismo. Aspettativa di vita 10-12 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e attività mentale sono importanti. Amano avere un lavoro.",
    verdetto: "Il Briard è un compagno leale e protettivo per famiglie attive. Richiede toelettatura intensiva e socializzazione."
  },
  'brussels-griffon.html': {
    meta: "Il Griffone di Bruxelles è un piccolo cane con una grande personalità. Vivace, affettuoso e pieno di carattere.",
    hero: "Il Griffone di Bruxelles è un piccolo cane con un'espressione unica e una grande personalità.",
    panoramica: "Il Griffone di Bruxelles era originariamente un cacciatore di topi nelle stalle di Bruxelles. È diventato popolare tra la nobiltà belga per la sua personalità affascinante.",
    temperamento: "I Griffon sono vivaci, intelligenti e affettuosi. Hanno una grande personalità in un corpo piccolo. Possono essere testardi ma adorano la compagnia.",
    salute: "Predisposti a problemi respiratori (BOAS), lussazione della rotula, problemi oculari e distocia. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio basse-moderate. Brevi passeggiate e gioco sono sufficienti. Sensibili al caldo.",
    verdetto: "Il Griffone di Bruxelles è un compagno vivace e affettuoso per chi cerca un cane toy con personalità. Non adatto a famiglie con bambini piccoli."
  }
};

function translateFile(filename) {
  const filepath = path.join(breedsDir, filename);
  let content = fs.readFileSync(filepath, 'utf-8');
  
  const translations = breedTranslations[filename];
  if (!translations) return false;
  
  if (translations.meta) {
    content = content.replace(
      /<meta name="description" content="[^"]*">/,
      `<meta name="description" content="${translations.meta}">`
    );
  }
  
  if (translations.hero) {
    content = content.replace(
      /<p class="text-lg text-slate-600 mb-6">[^<]*<\/p>/,
      `<p class="text-lg text-slate-600 mb-6">${translations.hero}</p>`
    );
  }
  
  if (translations.panoramica) {
    content = content.replace(
      /(<i data-lucide="book-open"[^>]*><\/i> Panoramica[\s\S]*?<div class="px-6 pb-6"><p class="text-slate-600">)[^<]*(<\/p><\/div>)/,
      `$1${translations.panoramica}$2`
    );
  }
  
  if (translations.temperamento) {
    content = content.replace(
      /(<i data-lucide="heart" class="w-5 h-5 text-sky-500"><\/i> Temperamento[\s\S]*?<div class="px-6 pb-6"><p class="text-slate-600">)[^<]*(<\/p><\/div>)/,
      `$1${translations.temperamento}$2`
    );
  }
  
  if (translations.salute) {
    content = content.replace(
      /(<i data-lucide="heart-pulse"[^>]*><\/i> Salute[\s\S]*?<div class="px-6 pb-6"><p class="text-slate-600">)[^<]*(<\/p><\/div>)/,
      `$1${translations.salute}$2`
    );
  }
  
  if (translations.esercizio) {
    content = content.replace(
      /(<i data-lucide="activity"[^>]*><\/i> Esercizio[\s\S]*?<div class="px-6 pb-6"><p class="text-slate-600">)[^<]*(<\/p><\/div>)/,
      `$1${translations.esercizio}$2`
    );
  }
  
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
console.log(`\nTranslated ${translated} more files`);
