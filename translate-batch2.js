#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const breedsDir = path.join(__dirname, 'it/breeds');

const breedTranslations = {
  'alaskan-klee-kai.html': {
    meta: "L'Alaskan Klee Kai è un piccolo cane simile all'Husky, energico e intelligente. Perfetto per chi ama gli Husky ma preferisce una taglia piccola.",
    hero: "L'Alaskan Klee Kai è un piccolo cane simile all'Husky, energico, intelligente e affettuoso con la famiglia.",
    panoramica: "L'Alaskan Klee Kai è una razza relativamente nuova, sviluppata negli anni '70 in Alaska per creare una versione in miniatura dell'Husky. Disponibile in tre taglie: Toy, Miniatura e Standard.",
    temperamento: "Gli Alaskan Klee Kai sono intelligenti, curiosi e riservati con gli estranei. Sono leali alla famiglia ma possono essere diffidenti. Richiedono socializzazione precoce.",
    salute: "Generalmente sani ma predisposti a lussazione della rotula, problemi cardiaci e malattie della tiroide. Aspettativa di vita 12-16 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e gioco attivo sono essenziali. Hanno molta energia nonostante la taglia.",
    verdetto: "L'Alaskan Klee Kai è perfetto per chi ama l'aspetto dell'Husky ma preferisce un cane più piccolo. Richiede socializzazione e esercizio regolare."
  },
  'american-bulldog.html': {
    meta: "L'American Bulldog è un cane atletico e protettivo, noto per la sua forza, lealtà e natura affettuosa con la famiglia.",
    hero: "L'American Bulldog è un cane atletico e protettivo, combinando forza, agilità e una profonda devozione verso la famiglia.",
    panoramica: "L'American Bulldog discende dai Bulldog Inglesi portati in America dai coloni. Usati originariamente nelle fattorie per il bestiame e la guardia, sono cani da lavoro versatili.",
    temperamento: "Gli American Bulldog sono sicuri, leali e protettivi. Sono affettuosi con la famiglia e ottimi con i bambini. Possono essere diffidenti con gli estranei.",
    salute: "Predisposti a displasia dell'anca e del gomito, problemi della pelle e allergie. Alcuni hanno problemi respiratori. Aspettativa di vita 10-12 anni.",
    esercizio: "Elevate esigenze di esercizio. Necessitano di attività fisica quotidiana e stimolazione mentale. Amano il gioco attivo e le sfide.",
    verdetto: "L'American Bulldog è un compagno leale e protettivo per famiglie attive. Richiede socializzazione precoce e proprietario esperto."
  },
  'american-eskimo-dog.html': {
    meta: "L'American Eskimo Dog è un cane brillante e vivace con un bellissimo mantello bianco. Intelligente, giocherellone e affettuoso.",
    hero: "L'American Eskimo Dog è un cane brillante e vivace, noto per il suo splendido mantello bianco e la personalità allegra.",
    panoramica: "Nonostante il nome, l'American Eskimo Dog discende dallo Spitz tedesco. Diventò popolare nei circhi americani per la sua intelligenza e capacità di apprendimento.",
    temperamento: "Gli Eskie sono intelligenti, giocherelloni e affettuosi. Sono ottimi cani da famiglia ma possono essere diffidenti con gli estranei. Amano imparare trucchi.",
    salute: "Predisposti a displasia dell'anca, malattia di Legg-Calvé-Perthes e problemi oculari. Aspettativa di vita 13-15 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane, gioco e stimolazione mentale sono importanti. Eccellono nell'agility.",
    verdetto: "L'American Eskimo Dog è un compagno brillante e giocherellone, ideale per famiglie attive. Richiede toelettatura regolare e stimolazione mentale."
  },
  'american-staffordshire-terrier.html': {
    meta: "L'American Staffordshire Terrier è un cane forte e leale, noto per il suo coraggio e l'amore incondizionato per la famiglia.",
    hero: "L'American Staffordshire Terrier è un cane forte e leale, combinando potenza atletica con una natura affettuosa verso la famiglia.",
    panoramica: "L'American Staffordshire Terrier, o AmStaff, discende dai cani da combattimento inglesi. Oggi sono amati cani da famiglia noti per la loro lealtà e affetto.",
    temperamento: "Gli AmStaff sono sicuri, leali e affettuosi. Adorano le persone e sono ottimi con i bambini. Possono essere riservati con altri cani.",
    salute: "Predisposti a displasia dell'anca, cardiopatia, allergie e atassia cerebellare. Aspettativa di vita 12-16 anni.",
    esercizio: "Elevate esigenze di esercizio. Necessitano di attività fisica quotidiana e gioco interattivo. Eccellono negli sport cinofili.",
    verdetto: "L'AmStaff è un compagno leale e affettuoso per proprietari responsabili. Richiede socializzazione, addestramento e un proprietario esperto."
  },
  'australian-cattle-dog.html': {
    meta: "L'Australian Cattle Dog è un cane da lavoro intelligente e resistente, sviluppato per la conduzione del bestiame in Australia.",
    hero: "L'Australian Cattle Dog è un cane da lavoro intelligente e resistente, noto per la sua energia inesauribile e lealtà.",
    panoramica: "L'Australian Cattle Dog, o Blue Heeler/Red Heeler, è stato sviluppato in Australia nel XIX secolo per la conduzione del bestiame. Discende da incroci con Dingo, Collie e Dalmata.",
    temperamento: "Gli ACD sono intelligenti, energici e leali. Sono protettivi con la famiglia e possono essere diffidenti con gli estranei. Hanno un forte istinto al lavoro.",
    salute: "Predisposti a sordità, atrofia retinica progressiva, displasia dell'anca e osteocondrite. Aspettativa di vita 12-16 anni.",
    esercizio: "Esigenze di esercizio molto elevate. Necessitano di lavoro fisico e mentale quotidiano. Eccellono nell'agility e negli sport cinofili.",
    verdetto: "L'Australian Cattle Dog è ideale per proprietari molto attivi che possono offrire lavoro e stimolazione costante. Non adatto alla vita sedentaria."
  },
  'australian-shepherd.html': {
    meta: "L'Australian Shepherd è un cane da pastore versatile e intelligente, noto per la sua energia, bellezza e versatilità.",
    hero: "L'Australian Shepherd è un cane da pastore versatile e intelligente, amato per la sua energia instancabile e la bellezza del mantello.",
    panoramica: "Nonostante il nome, l'Australian Shepherd è stato sviluppato negli Stati Uniti per la conduzione del bestiame. Il nome deriva dai pastori baschi che li portarono dall'Australia.",
    temperamento: "Gli Aussie sono intelligenti, energici e versatili. Sono devoti alla famiglia e amano lavorare. Possono essere riservati con gli estranei.",
    salute: "Predisposti a displasia dell'anca, problemi oculari (cataratta, coloboma) e epilessia. Alcuni portano il gene MDR1. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio molto elevate. Necessitano di almeno 2 ore di attività al giorno. Eccellono in agility, frisbee e pastorizia.",
    verdetto: "L'Australian Shepherd è ideale per proprietari molto attivi. Richiede stimolazione fisica e mentale costante. Non adatto a proprietari sedentari."
  },
  'basset-hound.html': {
    meta: "Il Basset Hound è un segugio dal carattere dolce con orecchie lunghissime. Calmo, affettuoso e con un naso eccezionale.",
    hero: "Il Basset Hound è un segugio dal carattere dolce e rilassato, famoso per le sue lunghe orecchie e l'olfatto straordinario.",
    panoramica: "Il Basset Hound è stato sviluppato in Francia per la caccia a piedi. Le sue zampe corte permettevano ai cacciatori di seguirlo senza cavalli. 'Basset' deriva dal francese 'bas', che significa basso.",
    temperamento: "I Basset sono calmi, affettuosi e un po' testardi. Sono ottimi con bambini e altri animali. Il loro istinto da segugio li porta a seguire le tracce.",
    salute: "Predisposti a problemi alla schiena, obesità, infezioni alle orecchie, problemi oculari e torsione gastrica. Aspettativa di vita 12-13 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane sono importanti ma evitare sforzi eccessivi. Tendenza all'obesità.",
    verdetto: "Il Basset Hound è un compagno rilassato e affettuoso, perfetto per famiglie tranquille. Attenzione al peso e alle orecchie che richiedono pulizia regolare."
  },
  'bernese-mountain-dog.html': {
    meta: "Il Bovaro del Bernese è un cane dolce e maestoso, originario delle Alpi Svizzere. Gentile, leale e ottimo con le famiglie.",
    hero: "Il Bovaro del Bernese è un cane dolce e maestoso, noto per il suo carattere gentile, la bellezza del mantello tricolore e la devozione alla famiglia.",
    panoramica: "Il Bovaro del Bernese è originario della regione di Berna in Svizzera, dove era usato come cane da fattoria per trainare carri e custodire il bestiame. È uno dei quattro Bovari Svizzeri.",
    temperamento: "I Bernesi sono dolci, calmi e affettuosi. Sono ottimi con i bambini e altri animali. Possono essere riservati con gli estranei ma non aggressivi.",
    salute: "Purtroppo predisposti a molti problemi: cancro (istiocitosi), displasia dell'anca e del gomito, problemi cardiaci. Aspettativa di vita breve: 6-8 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono sufficienti. Non tollerano bene il caldo.",
    verdetto: "Il Bovaro del Bernese è un compagno gentile e affettuoso, perfetto per famiglie. La breve aspettativa di vita e i problemi di salute richiedono considerazione."
  },
  'bichon-frise.html': {
    meta: "Il Bichon Frisé è un piccolo cane allegro e affettuoso con un morbido mantello bianco. Giocherellone e adatto a chi soffre di allergie.",
    hero: "Il Bichon Frisé è un piccolo cane allegro e affettuoso, noto per il suo soffice mantello bianco e la personalità gioiosa.",
    panoramica: "Il Bichon Frisé discende dai Water Spaniel del Mediterraneo. Era il preferito della nobiltà europea nel XVI secolo. Il nome significa 'cane riccio' in francese.",
    temperamento: "I Bichon sono allegri, giocherelloni e affettuosi. Adorano le persone e non amano essere lasciati soli. Sono ottimi cani da terapia.",
    salute: "Predisposti ad allergie, lussazione della rotula, cataratta e malattie del fegato. Il mantello richiede cure regolari. Aspettativa di vita 14-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Brevi passeggiate e gioco quotidiano sono sufficienti. Adorano i giochi interattivi.",
    verdetto: "Il Bichon Frisé è un compagno allegro perfetto per appartamenti e famiglie. Il mantello ipoallergenico richiede toelettatura regolare."
  },
  'boston-terrier.html': {
    meta: "Il Boston Terrier è il 'gentiluomo americano', un cane affettuoso e vivace con un distintivo mantello 'tuxedo'.",
    hero: "Il Boston Terrier è il 'gentiluomo americano', un cane affettuoso e vivace noto per il suo elegante mantello bianco e nero.",
    panoramica: "Il Boston Terrier è una delle poche razze americane, sviluppata a Boston nel XIX secolo. È un incrocio tra Bulldog Inglese e il White English Terrier, ormai estinto.",
    temperamento: "I Boston sono allegri, intelligenti e affettuosi. Adorano le persone e sono ottimi con i bambini. Possono essere un po' testardi ma desiderano piacere.",
    salute: "Predisposti a problemi respiratori (BOAS), problemi oculari, lussazione della rotula e sordità. Sensibili al caldo e al freddo. Aspettativa di vita 11-13 anni.",
    esercizio: "Esigenze di esercizio moderate. Brevi passeggiate e gioco sono sufficienti. Evitare sforzi in climi estremi.",
    verdetto: "Il Boston Terrier è un compagno affettuoso e adattabile, perfetto per appartamenti. Attenzione ai problemi respiratori e alla sensibilità al clima."
  },
  'brittany.html': {
    meta: "Il Brittany è un cane da caccia versatile e atletico, noto per la sua energia, intelligenza e natura affettuosa.",
    hero: "Il Brittany è un cane da caccia versatile e atletico, amato per la sua energia inesauribile e il carattere allegro.",
    panoramica: "Il Brittany, originario della Bretagna francese, è un cane da ferma versatile. Eccellente per la caccia a fagiani e pernici, è anche un meraviglioso compagno di famiglia.",
    temperamento: "I Brittany sono energici, intelligenti e desiderosi di piacere. Sono affettuosi con la famiglia e vanno d'accordo con bambini e altri animali.",
    salute: "Generalmente sani ma predisposti a displasia dell'anca, epilessia e ipotiroidismo. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio molto elevate. Necessitano di almeno 1-2 ore di attività intensa al giorno. Eccellono nella caccia e nell'agility.",
    verdetto: "Il Brittany è ideale per famiglie attive e cacciatori. Richiede molto esercizio e stimolazione. Non adatto a proprietari sedentari."
  },
  'bullmastiff.html': {
    meta: "Il Bullmastiff è un guardiano potente e silenzioso, noto per la sua natura protettiva e il temperamento calmo.",
    hero: "Il Bullmastiff è un guardiano potente e silenzioso, combinando la forza del Mastiff con l'agilità del Bulldog.",
    panoramica: "Il Bullmastiff è stato sviluppato in Inghilterra nel XIX secolo incrociando Mastiff e Bulldog per creare il guardiano perfetto per le tenute e contro i bracconieri.",
    temperamento: "I Bullmastiff sono calmi, sicuri e leali. Sono protettivi con la famiglia ma non aggressivi senza motivo. Sono affettuosi nonostante l'aspetto imponente.",
    salute: "Predisposti a displasia dell'anca e del gomito, problemi cardiaci, cancro e torsione gastrica. Aspettativa di vita 7-9 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane sono sufficienti. Non tollerano bene il caldo.",
    verdetto: "Il Bullmastiff è un guardiano leale e affettuoso per proprietari esperti. Richiede socializzazione precoce e spazio adeguato."
  },
  'cane-corso.html': {
    meta: "Il Cane Corso è un antico mastino italiano, potente e maestoso. Guardiano leale con una natura affettuosa verso la famiglia.",
    hero: "Il Cane Corso è un antico mastino italiano, potente e maestoso, noto per la sua intelligenza e natura protettiva.",
    panoramica: "Il Cane Corso discende dal Canis Pugnax romano, usato in guerra e per la caccia grossa. In Italia era il guardiano delle fattorie e del bestiame.",
    temperamento: "I Cane Corso sono intelligenti, leali e protettivi. Sono affettuosi con la famiglia ma riservati con gli estranei. Richiedono una leadership chiara.",
    salute: "Predisposti a displasia dell'anca, problemi cardiaci, entropion e torsione gastrica. Aspettativa di vita 9-12 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e gioco sono importanti. Necessitano di stimolazione mentale.",
    verdetto: "Il Cane Corso è un guardiano maestoso per proprietari esperti. Richiede socializzazione precoce, addestramento costante e spazio."
  },
  'chow-chow.html': {
    meta: "Il Chow Chow è un cane antico e dignitoso con la caratteristica lingua blu. Indipendente, leale e protettivo.",
    hero: "Il Chow Chow è un cane antico e dignitoso, immediatamente riconoscibile per la sua criniera leonina e la lingua blu-nera.",
    panoramica: "Il Chow Chow è una delle razze più antiche, originaria della Cina settentrionale. Erano usati come cani da guardia, da caccia e da traino. La lingua blu è unica di questa razza.",
    temperamento: "I Chow sono dignitosi, indipendenti e leali. Sono riservati con gli estranei e possono essere diffidenti. Sono devoti a un solo proprietario.",
    salute: "Predisposti a displasia dell'anca e del gomito, entropion, ipotiroidismo e problemi cutanei. Aspettativa di vita 8-12 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane sono sufficienti. Non tollerano bene il caldo.",
    verdetto: "Il Chow Chow è un compagno dignitoso e leale per proprietari esperti che rispettano la sua indipendenza. Richiede socializzazione precoce."
  },
  'collie.html': {
    meta: "Il Collie è un cane elegante e intelligente, reso famoso da Lassie. Dolce, leale e devoto alla famiglia.",
    hero: "Il Collie è un cane elegante e intelligente, amato per la sua bellezza, dolcezza e l'incredibile devozione alla famiglia.",
    panoramica: "Il Collie è originario della Scozia dove era usato per la conduzione del gregge. La razza divenne famosa grazie alla Regina Vittoria e successivamente alla serie TV Lassie.",
    temperamento: "I Collie sono dolci, intelligenti e devoti. Sono ottimi con i bambini e altri animali. Sono sensibili e rispondono meglio all'addestramento positivo.",
    salute: "Predisposti all'anomalia dell'occhio del Collie (CEA), displasia dell'anca, dermatomiosite. Molti portano il gene MDR1. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Amano le attività con la famiglia.",
    verdetto: "Il Collie è un eccellente cane da famiglia, dolce e adattabile. Perfetto per famiglie con bambini. Richiede toelettatura regolare del lungo mantello."
  },
  'corgi-pembroke.html': {
    meta: "Il Pembroke Welsh Corgi è un piccolo cane da pastore energico, famoso per essere il preferito della Regina Elisabetta II.",
    hero: "Il Pembroke Welsh Corgi è un piccolo cane da pastore energico e affettuoso, noto per la sua vivacità e il carattere allegro.",
    panoramica: "Il Pembroke Welsh Corgi è originario del Galles, dove era usato per la conduzione del bestiame. Le zampe corte gli permettevano di evitare i calci. È famoso per essere il cane preferito della Regina Elisabetta II.",
    temperamento: "I Corgi sono intelligenti, vivaci e affettuosi. Sono ottimi cani da famiglia ma possono essere vocali. Hanno una personalità grande nonostante la taglia.",
    salute: "Predisposti a problemi alla schiena (IVDD), displasia dell'anca, problemi oculari e obesità. Aspettativa di vita 12-13 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e gioco attivo sono essenziali. Mantenere il peso forma è importante.",
    verdetto: "Il Pembroke Welsh Corgi è un compagno vivace e affettuoso per famiglie attive. Richiede esercizio regolare e attenzione al peso."
  },
  'great-dane.html': {
    meta: "L'Alano è il 'gigante gentile' del mondo canino. Nonostante la taglia imponente, è affettuoso, paziente e amichevole.",
    hero: "L'Alano è il 'gigante gentile' del mondo canino, combinando una taglia imponente con un carattere dolce e affettuoso.",
    panoramica: "L'Alano, nonostante il nome, è di origine tedesca dove era usato per la caccia al cinghiale. È una delle razze più alte del mondo, con alcuni esemplari che superano il metro al garrese.",
    temperamento: "Gli Alani sono gentili, affettuosi e pazienti. Sono ottimi con i bambini nonostante la taglia. Sono amichevoli ma possono essere protettivi.",
    salute: "Purtroppo predisposti a molti problemi: cardiomiopatia dilatativa, torsione gastrica, displasia dell'anca e osteosarcoma. Aspettativa di vita breve: 7-10 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane sono importanti ma evitare sforzi eccessivi da cuccioli per proteggere le articolazioni.",
    verdetto: "L'Alano è un compagno gentile e affettuoso per chi ha spazio. La breve aspettativa di vita e i problemi di salute richiedono considerazione."
  },
  'havanese.html': {
    meta: "L'Havanese è il cane nazionale di Cuba, un piccolo compagno allegro e affettuoso con un mantello setoso.",
    hero: "L'Havanese è il cane nazionale di Cuba, un piccolo compagno allegro e affettuoso noto per la sua personalità vivace.",
    panoramica: "L'Havanese discende dai cani Bichon portati a Cuba dai coloni spagnoli. Divenne il cane preferito dell'aristocrazia cubana. È l'unica razza originaria di Cuba.",
    temperamento: "Gli Havanese sono allegri, affettuosi e socievoli. Adorano le persone e sono ottimi con bambini e altri animali. Possono soffrire di ansia da separazione.",
    salute: "Predisposti a lussazione della rotula, displasia dell'anca, cataratta e sordità. Aspettativa di vita 14-16 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono sufficienti. Si adattano bene alla vita in appartamento.",
    verdetto: "L'Havanese è un compagno allegro e adattabile, perfetto per famiglie e vita in appartamento. Richiede compagnia costante e toelettatura regolare."
  },
  'irish-setter.html': {
    meta: "Il Setter Irlandese è un cane elegante e atletico con un magnifico mantello rosso mogano. Energico, amichevole e giocherellone.",
    hero: "Il Setter Irlandese è un cane elegante e atletico, noto per il suo splendido mantello rosso mogano e la personalità esuberante.",
    panoramica: "Il Setter Irlandese è stato sviluppato in Irlanda nel XVIII secolo per la caccia agli uccelli. Il suo magnifico mantello rosso è diventato il marchio distintivo della razza.",
    temperamento: "I Setter Irlandesi sono energici, amichevoli e giocherelloni. Rimangono cuccioli nel cuore per molti anni. Sono affettuosi con tutti.",
    salute: "Predisposti a displasia dell'anca, torsione gastrica, epilessia e atrofia retinica progressiva. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio molto elevate. Necessitano di almeno 2 ore di attività al giorno. Ideali per famiglie attive e runner.",
    verdetto: "Il Setter Irlandese è un compagno energico e affettuoso per proprietari molto attivi. Richiede molto esercizio e socializzazione."
  },
  'jack-russell-terrier.html': {
    meta: "Il Jack Russell Terrier è un piccolo cane energico e coraggioso, noto per la sua intelligenza e personalità vivace.",
    hero: "Il Jack Russell Terrier è un piccolo cane energico e coraggioso, pieno di personalità e sempre pronto all'avventura.",
    panoramica: "Il Jack Russell Terrier è stato sviluppato in Inghilterra nel XIX secolo dal reverendo John Russell per la caccia alla volpe. Sono cani da lavoro instancabili.",
    temperamento: "I Jack Russell sono energici, intelligenti e coraggiosi. Hanno una personalità enorme nonostante la taglia. Possono essere testardi e hanno un forte istinto predatorio.",
    salute: "Predisposti a lussazione della rotula, sordità, problemi oculari e malattia di Legg-Calvé-Perthes. Aspettativa di vita 13-16 anni.",
    esercizio: "Esigenze di esercizio molto elevate. Necessitano di attività intensa quotidiana. Eccellono nell'agility e nel flyball.",
    verdetto: "Il Jack Russell è ideale per proprietari attivi che possono gestire la sua energia. Non adatto a proprietari alle prime armi o vita sedentaria."
  },
  'maltese.html': {
    meta: "Il Maltese è un elegante cane da compagnia con un lussuoso mantello bianco. Dolce, giocherellone e affettuoso.",
    hero: "Il Maltese è un elegante cane da compagnia, noto per il suo splendido mantello bianco e la personalità dolce e vivace.",
    panoramica: "Il Maltese è una delle razze più antiche, conosciuta da oltre 2000 anni. Era il compagno preferito della nobiltà greca e romana. Il nome deriva dall'isola di Malta.",
    temperamento: "I Maltesi sono dolci, giocherelloni e affettuosi. Amano le coccole e la compagnia. Possono essere vocali e soffrire se lasciati soli.",
    salute: "Predisposti a lussazione della rotula, shunt portosistemico, ipoglicemia e problemi dentali. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio basse. Brevi passeggiate e gioco in casa sono sufficienti. Si adattano perfettamente alla vita in appartamento.",
    verdetto: "Il Maltese è un compagno elegante e affettuoso, perfetto per appartamenti. Richiede toelettatura frequente e compagnia costante."
  },
  'miniature-schnauzer.html': {
    meta: "Lo Schnauzer Nano è un piccolo cane vivace e vigile, noto per la sua barba distintiva e la personalità allegra.",
    hero: "Lo Schnauzer Nano è un piccolo cane vivace e vigile, amato per la sua espressione caratteristica e il temperamento allegro.",
    panoramica: "Lo Schnauzer Nano è stato sviluppato in Germania nel XIX secolo incrociando lo Schnauzer Standard con razze più piccole come l'Affenpinscher. Era usato come cane da fattoria e cacciatore di topi.",
    temperamento: "Gli Schnauzer Nani sono vigili, spiritosi e amichevoli. Sono ottimi cani da guardia e compagni di famiglia. Possono essere vocali.",
    salute: "Predisposti a pancreatite, diabete, calcoli urinari e problemi oculari. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Si adattano bene a diversi stili di vita.",
    verdetto: "Lo Schnauzer Nano è un compagno versatile e vivace, adatto a famiglie e vita in appartamento. Richiede toelettatura regolare."
  },
  'newfoundland.html': {
    meta: "Il Terranova è un gigante gentile con un cuore enorme. Noto per le sue capacità di salvataggio in acqua e la dolcezza.",
    hero: "Il Terranova è un gigante gentile, famoso per la sua dolcezza, le capacità di salvataggio in acqua e l'amore per i bambini.",
    panoramica: "Il Terranova è originario dell'isola di Terranova in Canada. Era usato dai pescatori per trainare reti e salvare persone in mare. Sono nuotatori eccezionali.",
    temperamento: "I Terranova sono dolci, pazienti e protettivi. Sono eccellenti con i bambini e sono chiamati 'cani tata'. Sono calmi ma pronti ad agire in caso di emergenza.",
    salute: "Predisposti a displasia dell'anca e del gomito, problemi cardiaci, cistinuria e torsione gastrica. Aspettativa di vita 8-10 anni.",
    esercizio: "Esigenze di esercizio moderate. Amano nuotare. Passeggiate quotidiane sono importanti ma evitare il caldo eccessivo.",
    verdetto: "Il Terranova è un compagno dolce e protettivo, ideale per famiglie con bambini. Richiede spazio, tolleranza per la bava e toelettatura."
  },
  'papillon.html': {
    meta: "Il Papillon è un elegante cane toy con le caratteristiche orecchie a farfalla. Intelligente, vivace e affettuoso.",
    hero: "Il Papillon è un elegante cane toy, noto per le sue splendide orecchie a farfalla e l'intelligenza eccezionale.",
    panoramica: "Il Papillon, il cui nome significa 'farfalla' in francese, era il preferito della nobiltà europea. Maria Antonietta possedeva un Papillon. Le orecchie possono essere erette (Papillon) o pendenti (Phalène).",
    temperamento: "I Papillon sono intelligenti, vivaci e affettuosi. Sono tra le razze toy più intelligenti. Sono coraggiosi nonostante la taglia piccola.",
    salute: "Predisposti a lussazione della rotula, fontanella aperta, collasso tracheale e problemi dentali. Aspettativa di vita 14-16 anni.",
    esercizio: "Esigenze di esercizio moderate. Nonostante la taglia, sono attivi e amano il gioco. Si adattano bene all'agility.",
    verdetto: "Il Papillon è un compagno elegante e intelligente, perfetto per chi cerca un cane toy attivo. Richiede stimolazione mentale."
  },
  'pomeranian.html': {
    meta: "Il Volpino di Pomerania è un piccolo cane vivace con un soffice mantello. Coraggioso, curioso e pieno di personalità.",
    hero: "Il Volpino di Pomerania è un piccolo cane vivace, noto per il suo soffice mantello e la personalità esuberante.",
    panoramica: "Il Volpino di Pomerania discende dai cani da slitta artici ma è stato allevato in piccola taglia in Pomerania. La Regina Vittoria contribuì a rendere popolare la taglia più piccola.",
    temperamento: "I Pom sono vivaci, curiosi e coraggiosi. Non si rendono conto delle loro piccole dimensioni. Possono essere vocali e territoriali.",
    salute: "Predisposti a lussazione della rotula, collasso tracheale, ipoglicemia e problemi dentali. Aspettativa di vita 12-16 anni.",
    esercizio: "Esigenze di esercizio basse-moderate. Brevi passeggiate e gioco sono sufficienti. Sensibili al caldo.",
    verdetto: "Il Volpino di Pomerania è un compagno vivace e affettuoso, perfetto per appartamenti. Richiede toelettatura regolare e socializzazione."
  },
  'portuguese-water-dog.html': {
    meta: "Il Cane d'Acqua Portoghese è un cane atletico e intelligente, noto per il suo mantello ipoallergenico e l'amore per l'acqua.",
    hero: "Il Cane d'Acqua Portoghese è un cane atletico e intelligente, famoso per il suo amore per l'acqua e il mantello riccio.",
    panoramica: "Il Cane d'Acqua Portoghese era usato dai pescatori portoghesi per guidare i pesci nelle reti e recuperare attrezzi. Barack Obama ha reso famosa la razza con i suoi cani Bo e Sunny.",
    temperamento: "I PWD sono intelligenti, vivaci e affettuosi. Sono eccellenti nuotatori e amano lavorare. Sono leali alla famiglia e vanno d'accordo con i bambini.",
    salute: "Predisposti a displasia dell'anca, atrofia retinica progressiva, cardiomiopatia e malattia da accumulo GM1. Aspettativa di vita 11-13 anni.",
    esercizio: "Esigenze di esercizio elevate. Amano nuotare e necessitano di attività quotidiana. Eccellono negli sport acquatici.",
    verdetto: "Il Cane d'Acqua Portoghese è ideale per famiglie attive che amano l'acqua. Il mantello ipoallergenico richiede toelettatura regolare."
  },
  'samoyed.html': {
    meta: "Il Samoiedo è un cane bianco soffice con il caratteristico 'sorriso'. Amichevole, gentile e pieno di energia.",
    hero: "Il Samoiedo è un cane bianco soffice, noto per il suo caratteristico 'sorriso Sammy' e la natura amichevole.",
    panoramica: "Il Samoiedo prende il nome dal popolo Samoiedo della Siberia, che lo usava per la conduzione delle renne e il traino delle slitte. Il loro mantello bianco li proteggeva dal freddo estremo.",
    temperamento: "I Samoiedi sono amichevoli, gentili e giocherelloni. Adorano le persone e sono ottimi con i bambini. Possono essere vocali e amano 'parlare'.",
    salute: "Predisposti a displasia dell'anca, diabete, ipotiroidismo e glomerulopatia. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e gioco sono importanti. Non tollerano bene il caldo.",
    verdetto: "Il Samoiedo è un compagno affettuoso e allegro per famiglie in climi freschi. Richiede toelettatura frequente e attenzione alla perdita di pelo."
  },
  'shar-pei.html': {
    meta: "Lo Shar-Pei è un cane distintivo con pelle rugosa e lingua blu. Indipendente, leale e protettivo.",
    hero: "Lo Shar-Pei è un cane distintivo, immediatamente riconoscibile per la sua pelle rugosa e l'aspetto unico.",
    panoramica: "Lo Shar-Pei è una razza antica cinese, usata per la guardia, la caccia e purtroppo i combattimenti. Il nome significa 'pelle di sabbia' in cinese, riferendosi alla texture del mantello.",
    temperamento: "Gli Shar-Pei sono calmi, indipendenti e leali. Sono riservati con gli estranei ma devoti alla famiglia. Richiedono socializzazione precoce.",
    salute: "Predisposti a molti problemi: febbre dello Shar-Pei, problemi cutanei, entropion, displasia dell'anca e amiloidosi. Aspettativa di vita 8-12 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane sono sufficienti. Non tollerano bene il caldo.",
    verdetto: "Lo Shar-Pei è un compagno leale e protettivo per proprietari esperti. Richiede attenzione alla salute e socializzazione precoce."
  },
  'shetland-sheepdog.html': {
    meta: "Il Pastore delle Shetland è un cane elegante e intelligente, simile a un Collie in miniatura. Devoto, dolce e addestrabile.",
    hero: "Il Pastore delle Shetland è un cane elegante e intelligente, amato per la sua bellezza, dolcezza e incredibile addestrabilità.",
    panoramica: "Il Pastore delle Shetland, o Sheltie, è originario delle Isole Shetland in Scozia. Era usato per la conduzione del gregge in terreni difficili. Non è un Collie in miniatura, ma una razza distinta.",
    temperamento: "Gli Sheltie sono intelligenti, sensibili e devoti. Sono ottimi cani da famiglia ma possono essere riservati con gli estranei. Amano imparare e piacere.",
    salute: "Predisposti all'anomalia dell'occhio del Collie, displasia dell'anca, ipotiroidismo e dermatomiosite. Portano spesso il gene MDR1. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Eccellono nell'agility e nell'obedience.",
    verdetto: "Lo Sheltie è un compagno intelligente e devoto, perfetto per famiglie. Richiede toelettatura regolare e stimolazione mentale."
  },
  'shih-tzu.html': {
    meta: "Lo Shih Tzu è un elegante cane da compagnia con un lussuoso mantello. Affettuoso, vivace e perfetto per la vita in appartamento.",
    hero: "Lo Shih Tzu è un elegante cane da compagnia, noto per il suo magnifico mantello fluente e la personalità affettuosa.",
    panoramica: "Lo Shih Tzu è una razza antica cinese, il cui nome significa 'cane leone'. Era il compagno preferito degli imperatori cinesi e veniva tenuto nei palazzi reali.",
    temperamento: "Gli Shih Tzu sono affettuosi, vivaci e amichevoli. Adorano stare con le persone e sono ottimi cani da appartamento. Possono essere un po' testardi.",
    salute: "Predisposti a problemi respiratori, problemi oculari, lussazione della rotula e malattie del disco intervertebrale. Aspettativa di vita 10-18 anni.",
    esercizio: "Esigenze di esercizio basse. Brevi passeggiate e gioco in casa sono sufficienti. Sensibili al caldo.",
    verdetto: "Lo Shih Tzu è un compagno affettuoso perfetto per appartamenti e famiglie. Richiede toelettatura quotidiana e attenzione al clima."
  },
  'st-bernard.html': {
    meta: "Il San Bernardo è un gigante gentile, famoso per il salvataggio alpino. Dolce, paziente e devoto alla famiglia.",
    hero: "Il San Bernardo è un gigante gentile, famoso per le sue eroiche imprese di salvataggio nelle Alpi e la natura affettuosa.",
    panoramica: "Il San Bernardo prende il nome dall'ospizio del Gran San Bernardo nelle Alpi svizzere, dove i monaci li usavano per il salvataggio dei viaggiatori. Barry, il più famoso, salvò oltre 40 persone.",
    temperamento: "I San Bernardo sono dolci, pazienti e gentili. Sono eccellenti con i bambini e sono chiamati 'giganti buoni'. Sono protettivi ma non aggressivi.",
    salute: "Predisposti a displasia dell'anca e del gomito, torsione gastrica, problemi cardiaci e osteosarcoma. Aspettativa di vita 8-10 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane sono importanti ma evitare sforzi eccessivi da cuccioli. Non tollerano il caldo.",
    verdetto: "Il San Bernardo è un compagno dolce e paziente per famiglie con spazio. Richiede tolleranza per la bava e attenzione alla salute."
  },
  'vizsla.html': {
    meta: "Il Vizsla è un cane da caccia ungherese elegante e atletico. Affettuoso, energico e profondamente legato al proprietario.",
    hero: "Il Vizsla è un cane da caccia ungherese elegante e atletico, noto per la sua affettuosità e il mantello dorato ruggine.",
    panoramica: "Il Vizsla è una razza ungherese antica, sviluppata come cane da caccia versatile per la nobiltà magiara. Il nome significa 'cercatore' in ungherese.",
    temperamento: "I Vizsla sono affettuosi, energici e sensibili. Sono chiamati 'cani velcro' per il loro attaccamento al proprietario. Soffrono se lasciati soli.",
    salute: "Predisposti a displasia dell'anca, epilessia, ipotiroidismo e allergie. Relativamente sani. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio molto elevate. Necessitano di almeno 2 ore di attività al giorno. Ideali per runner e famiglie attive.",
    verdetto: "Il Vizsla è ideale per famiglie molto attive che desiderano un compagno affettuoso. Richiede molto esercizio e compagnia costante."
  },
  'weimaraner.html': {
    meta: "Il Weimaraner è un cane da caccia elegante con il distintivo mantello grigio. Atletico, intelligente e profondamente leale.",
    hero: "Il Weimaraner è un cane da caccia elegante, noto per il suo splendido mantello grigio-argento e gli occhi ambra.",
    panoramica: "Il Weimaraner è stato sviluppato a Weimar, in Germania, come cane da caccia per la nobiltà. Era chiamato il 'fantasma grigio' per il suo mantello distintivo e la sua agilità nella caccia.",
    temperamento: "I Weimaraner sono energici, intelligenti e affettuosi. Sono molto legati alla famiglia e soffrono l'ansia da separazione. Necessitano di stimolazione costante.",
    salute: "Predisposti a torsione gastrica, displasia dell'anca, problemi oculari e malattia di von Willebrand. Aspettativa di vita 10-13 anni.",
    esercizio: "Esigenze di esercizio molto elevate. Necessitano di almeno 2 ore di attività intensa al giorno. Ideali per proprietari atletici.",
    verdetto: "Il Weimaraner è ideale per proprietari molto attivi che possono offrire esercizio intenso e compagnia. Non adatto a proprietari sedentari."
  },
  'west-highland-white-terrier.html': {
    meta: "Il West Highland White Terrier è un piccolo cane bianco vivace e coraggioso. Allegro, indipendente e pieno di personalità.",
    hero: "Il West Highland White Terrier è un piccolo cane bianco vivace, noto per la sua personalità allegra e il carattere coraggioso.",
    panoramica: "Il Westie è originario della Scozia, sviluppato per la caccia a volpi, tassi e roditori. Il mantello bianco fu selezionato per distinguerli dalla preda durante la caccia.",
    temperamento: "I Westie sono allegri, sicuri e indipendenti. Hanno la tipica personalità terrier: coraggiosi e un po' testardi. Sono affettuosi con la famiglia.",
    salute: "Predisposti a dermatite atopica, lussazione della rotula, malattia di Legg-Calvé-Perthes e problemi epatici. Aspettativa di vita 13-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Hanno più energia di quanto suggerisca la taglia.",
    verdetto: "Il Westie è un compagno allegro e adattabile, adatto a diversi stili di vita. Richiede toelettatura regolare e gestione delle allergie cutanee."
  },
  'whippet.html': {
    meta: "Il Whippet è un levriero elegante e veloce, perfetto per la vita in appartamento. Dolce, calmo in casa e velocissimo all'aperto.",
    hero: "Il Whippet è un levriero elegante e veloce, combinando grazia atletica con una natura dolce e affettuosa.",
    panoramica: "Il Whippet è stato sviluppato in Inghilterra come 'levriero dei poveri' per le corse e la caccia alla lepre. Può raggiungere i 56 km/h, rendendolo uno dei cani più veloci.",
    temperamento: "I Whippet sono dolci, calmi e affettuosi in casa. Sono veloci e atletici all'aperto. Sono sensibili e amano il comfort.",
    salute: "Generalmente sani ma predisposti a problemi cardiaci, problemi oculari e sensibilità all'anestesia. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Amano correre ma sono anche felici di rilassarsi sul divano. Necessitano di un'area recintata per correre.",
    verdetto: "Il Whippet è un compagno elegante e adattabile, perfetto per appartamenti. Ideale per chi cerca un cane atletico ma tranquillo in casa."
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
