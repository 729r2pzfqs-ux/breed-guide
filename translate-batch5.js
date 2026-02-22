#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const breedsDir = path.join(__dirname, 'it/breeds');

const breedTranslations = {
  'german-shorthaired-pointer.html': {
    meta: "Il Bracco Tedesco a Pelo Corto è un cane da caccia versatile e atletico. Energico, intelligente e affettuoso.",
    hero: "Il Bracco Tedesco a Pelo Corto è un cane da caccia versatile, eccellente sia sul campo che in famiglia.",
    panoramica: "Il Bracco Tedesco a Pelo Corto è stato sviluppato in Germania nel XIX secolo come cane da caccia versatile. Eccelle nella caccia, nel nuoto e negli sport cinofili.",
    temperamento: "I GSP sono energici, intelligenti e affettuosi. Sono ottimi cani da famiglia se adeguatamente esercitati. Sono versatili e desiderosi di piacere.",
    salute: "Predisposti a displasia dell'anca, torsione gastrica, problemi cardiaci e malattia di von Willebrand. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio molto elevate. Necessitano di almeno 2 ore di attività intensa al giorno. Non adatti a proprietari sedentari.",
    verdetto: "Il Bracco Tedesco è ideale per famiglie molto attive e cacciatori. Richiede enorme quantità di esercizio."
  },
  'german-spitz.html': {
    meta: "Lo Spitz Tedesco è un cane vivace e allegro con un soffice mantello. Vigile, intelligente e affettuoso.",
    hero: "Lo Spitz Tedesco è un cane vivace e allegro, disponibile in diverse taglie e colori.",
    panoramica: "Lo Spitz Tedesco è una delle razze europee più antiche. È disponibile in cinque varietà di taglia: Wolfspitz, Grande, Medio, Piccolo e Nano (Pomerania).",
    temperamento: "Gli Spitz Tedeschi sono vivaci, vigili e intelligenti. Sono buoni cani da guardia e affettuosi con la famiglia. Possono essere vocali.",
    salute: "Predisposti a lussazione della rotula, collasso tracheale, problemi dentali e cataratta. Aspettativa di vita 13-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Si adattano bene a diversi stili di vita.",
    verdetto: "Lo Spitz Tedesco è un compagno allegro e vigile, adatto a diverse situazioni. Richiede toelettatura regolare."
  },
  'german-wirehaired-pointer.html': {
    meta: "Il Bracco Tedesco a Pelo Duro è un cane da caccia resistente e versatile. Energico, leale e determinato.",
    hero: "Il Bracco Tedesco a Pelo Duro è un cane da caccia resistente, il più popolare in Germania.",
    panoramica: "Il Bracco Tedesco a Pelo Duro è stato sviluppato in Germania per essere un cane da caccia versatile in ogni terreno e clima. Il pelo duro lo protegge da acqua e rovi.",
    temperamento: "I GWP sono energici, leali e determinati. Sono ottimi cani da caccia e compagni per proprietari attivi. Possono essere riservati con gli estranei.",
    salute: "Predisposti a displasia dell'anca, problemi oculari, malattia di von Willebrand e torsione gastrica. Aspettativa di vita 14-16 anni.",
    esercizio: "Esigenze di esercizio molto elevate. Necessitano di attività fisica intensa quotidiana. Eccellono nella caccia.",
    verdetto: "Il Bracco Tedesco a Pelo Duro è ideale per cacciatori e famiglie molto attive. Richiede esercizio intenso."
  },
  'giant-schnauzer.html': {
    meta: "Lo Schnauzer Gigante è un cane potente e versatile. Intelligente, leale e sempre vigile.",
    hero: "Lo Schnauzer Gigante è la versione più grande dello Schnauzer, un guardiano potente e intelligente.",
    panoramica: "Lo Schnauzer Gigante è stato sviluppato in Germania come cane da lavoro per la conduzione del bestiame e la guardia. È usato anche come cane poliziotto.",
    temperamento: "Gli Schnauzer Giganti sono intelligenti, leali e protettivi. Sono versatili nel lavoro e devoti alla famiglia. Richiedono un proprietario esperto.",
    salute: "Predisposti a displasia dell'anca, torsione gastrica, problemi oculari e ipotiroidismo. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica e mentale quotidiana. Eccellono negli sport cinofili.",
    verdetto: "Lo Schnauzer Gigante è un guardiano versatile per proprietari esperti. Richiede addestramento, socializzazione e toelettatura."
  },
  'glen-of-imaal-terrier.html': {
    meta: "Il Glen of Imaal Terrier è un terrier irlandese robusto e coraggioso. Spiritoso, gentile e meno vocale di altri terrier.",
    hero: "Il Glen of Imaal Terrier è un terrier irlandese robusto, uno dei terrier più rari al mondo.",
    panoramica: "Il Glen of Imaal Terrier prende il nome dalla valle di Glen of Imaal in Irlanda. Era usato per cacciare tassi e volpi, e come cane da cucina per girare lo spiedo.",
    temperamento: "I Glen sono spiritosi, gentili e coraggiosi. Sono meno eccitabili di altri terrier. Sono affettuosi con la famiglia.",
    salute: "Predisposti a atrofia retinica progressiva, displasia dell'anca e problemi alla schiena. Aspettativa di vita 10-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono sufficienti. Hanno meno energia di altri terrier.",
    verdetto: "Il Glen of Imaal Terrier è un terrier più calmo per chi cerca la personalità terrier senza l'eccesso di energia."
  },
  'gordon-setter.html': {
    meta: "Il Gordon Setter è un elegante cane da caccia scozzese. Leale, intelligente e con un magnifico mantello nero focato.",
    hero: "Il Gordon Setter è un elegante cane da caccia scozzese, il più grande e robusto dei setter.",
    panoramica: "Il Gordon Setter prende il nome dal Duca di Gordon che sviluppò la razza nel castello di Gordon in Scozia. È il più grande e robusto dei setter.",
    temperamento: "I Gordon sono leali, intelligenti e affettuosi. Sono più riservati degli altri setter. Formano legami molto forti con il proprietario.",
    salute: "Predisposti a displasia dell'anca e del gomito, torsione gastrica, atrofia retinica progressiva e ipotiroidismo. Aspettativa di vita 12-13 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica quotidiana. Amano correre e cacciare.",
    verdetto: "Il Gordon Setter è un compagno leale ed elegante per famiglie attive. Richiede esercizio e toelettatura regolare."
  },
  'grand-basset-griffon-vendeen.html': {
    meta: "Il Grand Basset Griffon Vendéen è un segugio francese allegro con un mantello ruvido. Vivace, socievole e instancabile.",
    hero: "Il Grand Basset Griffon Vendéen è un segugio francese allegro, più grande del cugino Petit.",
    panoramica: "Il GBGV è originario della regione della Vandea in Francia, sviluppato per la caccia alla lepre. È la versione più grande del Petit Basset Griffon Vendéen.",
    temperamento: "I GBGV sono allegri, vivaci e socievoli. Sono ottimi con bambini e altri cani. Hanno un forte istinto da segugio.",
    salute: "Predisposti a problemi alla schiena, epilessia, problemi oculari e allergie. Aspettativa di vita 13-15 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e opportunità di seguire tracce sono importanti.",
    verdetto: "Il GBGV è un compagno allegro e socievole per famiglie. Richiede un giardino recintato e toelettatura."
  },
  'great-pyrenees.html': {
    meta: "Il Grande Pirenei è un maestoso guardiano del bestiame. Calmo, protettivo e affettuoso con la famiglia.",
    hero: "Il Grande Pirenei è un maestoso guardiano del bestiame, noto per il suo magnifico mantello bianco.",
    panoramica: "Il Grande Pirenei ha custodito le greggi sui Pirenei per secoli. Era anche usato dalla nobiltà francese come guardiano dei castelli.",
    temperamento: "I Pirenei sono calmi, pazienti e protettivi. Sono affettuosi con la famiglia ma possono essere indipendenti. Sono naturalmente guardiani.",
    salute: "Predisposti a displasia dell'anca, torsione gastrica, lussazione della rotula e problemi cardiaci. Aspettativa di vita 10-12 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane sono importanti. Amano pattugliare il loro territorio.",
    verdetto: "Il Grande Pirenei è un guardiano maestoso per proprietari con spazio. Richiede tolleranza per l'abbaio notturno e lo spargimento di pelo."
  },
  'greater-swiss-mountain-dog.html': {
    meta: "Il Grande Bovaro Svizzero è il più grande dei bovari svizzeri. Forte, leale e affettuoso.",
    hero: "Il Grande Bovaro Svizzero è il più grande dei bovari svizzeri, un cane potente dal carattere dolce.",
    panoramica: "Il Grande Bovaro Svizzero è il più grande e probabilmente il più antico dei bovari svizzeri. Era usato per trainare carri e custodire le fattorie.",
    temperamento: "I Swissy sono forti, leali e affettuosi. Sono ottimi cani da famiglia e buoni con i bambini. Hanno bisogno di stare con le persone.",
    salute: "Predisposti a displasia dell'anca e del gomito, torsione gastrica, epilessia e incontinenza. Aspettativa di vita 8-11 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Non tollerano bene il caldo.",
    verdetto: "Il Grande Bovaro Svizzero è un compagno forte e affettuoso per famiglie. Richiede spazio e attenzione alla salute."
  },
  'greyhound.html': {
    meta: "Il Greyhound è il cane più veloce del mondo, elegante e sorprendentemente tranquillo. Dolce, gentile e rilassato.",
    hero: "Il Greyhound è il cane più veloce del mondo, capace di raggiungere i 70 km/h, ma sorprendentemente tranquillo in casa.",
    panoramica: "Il Greyhound è una delle razze più antiche, raffigurato nell'arte egizia di 4000 anni fa. È stato sviluppato per la caccia a vista alla lepre.",
    temperamento: "I Greyhound sono dolci, gentili e rilassati. Nonostante la velocità, adorano dormire sul divano. Sono sensibili e affettuosi.",
    salute: "Predisposti a torsione gastrica, osteosarcoma, problemi cardiaci e sensibilità all'anestesia. Aspettativa di vita 10-14 anni.",
    esercizio: "Esigenze di esercizio moderate. Amano correre ma sono anche felici di rilassarsi. Necessitano di un'area recintata per correre.",
    verdetto: "Il Greyhound è un compagno elegante e tranquillo, perfetto per appartamenti. Ideale per chi adotta ex-corridori."
  },
  'harrier.html': {
    meta: "L'Harrier è un segugio inglese resistente, simile a un Beagle grande. Allegro, amichevole e instancabile.",
    hero: "L'Harrier è un segugio inglese resistente, a metà tra il Beagle e l'English Foxhound.",
    panoramica: "L'Harrier è stato sviluppato in Inghilterra per la caccia alla lepre (hare). È più grande del Beagle ma più piccolo del Foxhound.",
    temperamento: "Gli Harrier sono allegri, amichevoli e socievoli. Sono ottimi con bambini e altri cani. Hanno un forte istinto da branco.",
    salute: "Generalmente sani ma predisposti a displasia dell'anca e problemi oculari. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di molto spazio e attività quotidiana. Amano correre e seguire tracce.",
    verdetto: "L'Harrier è un segugio allegro per famiglie attive con spazio. Richiede compagnia e esercizio."
  },
  'hokkaido.html': {
    meta: "L'Hokkaido è un antico cane giapponese resistente. Leale, coraggioso e devoto al proprietario.",
    hero: "L'Hokkaido è un antico cane giapponese, allevato per la caccia all'orso nell'isola più settentrionale del Giappone.",
    panoramica: "L'Hokkaido è stato portato nel Giappone settentrionale dal popolo Ainu oltre 1000 anni fa. È noto per la resistenza al freddo e il coraggio nella caccia all'orso.",
    temperamento: "Gli Hokkaido sono leali, coraggiosi e devoti. Sono riservati con gli estranei ma affettuosi con la famiglia. Hanno forte istinto da guardia.",
    salute: "Generalmente sani ma predisposti a displasia dell'anca, anomalia dell'occhio del Collie e allergie. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e attività sono importanti. Tollerano bene il freddo.",
    verdetto: "L'Hokkaido è un compagno leale per proprietari esperti. Richiede socializzazione e leadership."
  },
  'hovawart.html': {
    meta: "L'Hovawart è un antico cane da guardia tedesco. Versatile, leale e eccellente guardiano della famiglia.",
    hero: "L'Hovawart è un antico cane da guardia tedesco, il cui nome significa 'guardiano della proprietà'.",
    panoramica: "L'Hovawart è una razza tedesca medievale quasi estinta e poi ricostruita nel XX secolo. Il nome deriva dal tedesco antico 'hova' (proprietà) e 'wart' (guardiano).",
    temperamento: "Gli Hovawart sono leali, intelligenti e protettivi. Sono versatili nel lavoro e affettuosi con la famiglia. Maturano lentamente.",
    salute: "Generalmente sani ma predisposti a displasia dell'anca e ipotiroidismo. Aspettativa di vita 10-14 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e attività mentale sono importanti. Amano avere un lavoro.",
    verdetto: "L'Hovawart è un guardiano versatile per famiglie. Richiede pazienza per la maturazione lenta e socializzazione."
  },
  'ibizan-hound.html': {
    meta: "Il Podenco Ibicenco è un levriero elegante delle Isole Baleari. Atletico, giocherellone e con un aspetto unico.",
    hero: "Il Podenco Ibicenco è un levriero elegante originario di Ibiza, con un aspetto che ricorda l'antico Egitto.",
    panoramica: "Il Podenco Ibicenco è originario delle Isole Baleari, dove cacciava conigli. La sua somiglianza con i cani dell'antico Egitto suggerisce origini antichissime.",
    temperamento: "I Podenco sono atletici, giocherelloni e indipendenti. Sono affettuosi con la famiglia ma hanno un forte istinto predatorio. Sono sensibili.",
    salute: "Generalmente sani ma predisposti ad allergie, sordità e sensibilità all'anestesia. Aspettativa di vita 11-14 anni.",
    esercizio: "Esigenze di esercizio elevate. Amano correre e necessitano di un'area recintata alta. Sono eccellenti saltatori.",
    verdetto: "Il Podenco Ibicenco è un compagno atletico ed elegante. Richiede recinzioni alte e non adatto a case con piccoli animali."
  },
  'icelandic-sheepdog.html': {
    meta: "Il Pastore Islandese è l'unica razza originaria dell'Islanda. Allegro, amichevole e pieno di energia.",
    hero: "Il Pastore Islandese è l'unica razza canina originaria dell'Islanda, portato dai Vichinghi.",
    panoramica: "Il Pastore Islandese è stato portato in Islanda dai Vichinghi oltre 1000 anni fa. È stato usato per la conduzione delle pecore nelle montagne islandesi.",
    temperamento: "I Pastori Islandesi sono allegri, amichevoli e curiosi. Sono ottimi cani da famiglia e vanno d'accordo con tutti. Sono vocali.",
    salute: "Predisposti a displasia dell'anca, cataratta e criptorchidismo. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Amano le attività all'aperto.",
    verdetto: "Il Pastore Islandese è un compagno allegro e amichevole per famiglie. Richiede tolleranza per la vocalizzazione."
  },
  'irish-red-and-white-setter.html': {
    meta: "Il Setter Irlandese Rosso e Bianco è l'antenato del Setter Irlandese. Atletico, amichevole e ottimo cacciatore.",
    hero: "Il Setter Irlandese Rosso e Bianco è l'antenato del più famoso Setter Irlandese, con un mantello distintivo.",
    panoramica: "Il Setter Irlandese Rosso e Bianco è la versione originale del setter irlandese, quasi estinto nel XIX secolo quando la varietà tutta rossa divenne più popolare.",
    temperamento: "I Setter RB sono atletici, amichevoli e affettuosi. Sono ottimi cani da caccia e compagni di famiglia. Sono un po' più calmi del cugino rosso.",
    salute: "Predisposti a displasia dell'anca, atrofia retinica progressiva, malattia di von Willebrand e ipotiroidismo. Aspettativa di vita 11-15 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica quotidiana. Amano correre e cacciare.",
    verdetto: "Il Setter Irlandese RB è un compagno atletico per famiglie attive. Richiede esercizio e toelettatura."
  },
  'irish-water-spaniel.html': {
    meta: "L'Irish Water Spaniel è lo spaniel più alto con un mantello riccio distintivo. Intelligente, giocherellone e amante dell'acqua.",
    hero: "L'Irish Water Spaniel è lo spaniel più alto, noto per il suo mantello riccio e la coda a 'topo'.",
    panoramica: "L'Irish Water Spaniel è una delle razze spaniel più antiche, sviluppata in Irlanda per la caccia acquatica. La sua coda liscia è chiamata 'rat tail'.",
    temperamento: "Gli IWS sono intelligenti, giocherelloni e un po' birichini. Sono affettuosi con la famiglia ma possono essere riservati con gli estranei.",
    salute: "Predisposti a displasia dell'anca, ipotiroidismo, epilessia e problemi oculari. Aspettativa di vita 12-13 anni.",
    esercizio: "Esigenze di esercizio elevate. Amano nuotare e cacciare. Necessitano di attività fisica quotidiana.",
    verdetto: "L'Irish Water Spaniel è un compagno giocherellone per famiglie attive che amano l'acqua. Richiede toelettatura."
  },
  'irish-wolfhound.html': {
    meta: "L'Irish Wolfhound è il cane più alto del mondo, un gigante gentile dalla storia eroica. Dolce, paziente e dignitoso.",
    hero: "L'Irish Wolfhound è il cane più alto del mondo, un gigante gentile che un tempo cacciava i lupi.",
    panoramica: "L'Irish Wolfhound è una razza irlandese antichissima, usata per cacciare lupi e cervi. Quasi estinto nel XIX secolo, fu salvato dal Capitano George Graham.",
    temperamento: "Gli Irish Wolfhound sono dolci, pazienti e dignitosi. Nonostante la taglia, sono gentili con i bambini. Sono calmi in casa.",
    salute: "Purtroppo predisposti a cardiomiopatia dilatativa, torsione gastrica, osteosarcoma e shunt epatico. Aspettativa di vita breve: 6-8 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane sono importanti ma evitare sforzi eccessivi da cuccioli.",
    verdetto: "L'Irish Wolfhound è un gigante gentile per chi ha spazio. La breve aspettativa di vita richiede considerazione."
  },
  'italian-greyhound.html': {
    meta: "Il Piccolo Levriero Italiano è un elegante levriero in miniatura. Affettuoso, giocherellone e amante del comfort.",
    hero: "Il Piccolo Levriero Italiano è un elegante levriero in miniatura, noto per la sua grazia e sensibilità.",
    panoramica: "Il Piccolo Levriero Italiano è una razza antica, amata dalla nobiltà europea per secoli. Federico il Grande e la Regina Vittoria possedevano questi cani.",
    temperamento: "Gli IG sono affettuosi, giocherelloni e sensibili. Amano le coccole e il comfort. Possono essere timidi con gli estranei.",
    salute: "Predisposti a fratture (ossa delicate), problemi dentali, lussazione della rotula ed epilessia. Aspettativa di vita 14-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Amano correre ma anche rilassarsi. Sensibili al freddo.",
    verdetto: "Il Piccolo Levriero Italiano è un compagno elegante e affettuoso per chi cerca un cane delicato. Richiede protezione dal freddo."
  },
  'japanese-chin.html': {
    meta: "Il Chin Giapponese è un elegante cane da compagnia con origini reali. Affettuoso, intelligente e con un aspetto distintivo.",
    hero: "Il Chin Giapponese è un elegante cane da compagnia, il preferito della nobiltà giapponese per secoli.",
    panoramica: "Il Chin Giapponese era così prezioso che veniva dato solo come dono imperiale. La sua origine è probabilmente cinese, ma fu perfezionato in Giappone.",
    temperamento: "I Chin sono affettuosi, intelligenti e un po' felini nel comportamento. Sono puliti e amano stare in alto. Sono devoti al proprietario.",
    salute: "Predisposti a problemi cardiaci, lussazione della rotula, problemi oculari e difficoltà respiratorie. Aspettativa di vita 10-12 anni.",
    esercizio: "Esigenze di esercizio basse. Brevi passeggiate e gioco sono sufficienti. Sensibili al caldo.",
    verdetto: "Il Chin Giapponese è un compagno elegante e tranquillo per chi cerca un cane toy raffinato."
  },
  'japanese-spitz.html': {
    meta: "Lo Spitz Giapponese è un piccolo cane bianco allegro e vivace. Intelligente, affettuoso e facile da addestrare.",
    hero: "Lo Spitz Giapponese è un piccolo cane bianco allegro, noto per la sua personalità gioiosa e il mantello soffice.",
    panoramica: "Lo Spitz Giapponese è stato sviluppato in Giappone negli anni '20 e '30 da varie razze spitz. È simile al Samoiedo in miniatura.",
    temperamento: "Gli Spitz Giapponesi sono allegri, intelligenti e affettuosi. Sono ottimi cani da famiglia e facili da addestrare. Possono essere riservati con gli estranei.",
    salute: "Generalmente sani ma predisposti a lussazione della rotula e lacrimazione eccessiva. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Si adattano bene alla vita in appartamento.",
    verdetto: "Lo Spitz Giapponese è un compagno allegro e adattabile per famiglie. Richiede toelettatura regolare."
  },
  'kai-ken.html': {
    meta: "Il Kai Ken è un antico cane giapponese tigrato. Leale, intelligente e riservato.",
    hero: "Il Kai Ken è un antico cane giapponese, noto per il suo distintivo mantello tigrato e la lealtà.",
    panoramica: "Il Kai Ken è originario della provincia di Kai (oggi Yamanashi) in Giappone. Era usato per la caccia al cinghiale e al cervo in montagna.",
    temperamento: "I Kai Ken sono leali, intelligenti e riservati. Formano legami molto forti con il proprietario. Possono essere diffidenti con gli estranei.",
    salute: "Generalmente sani. Predisposti a displasia dell'anca e lussazione della rotula. Aspettativa di vita 12-16 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e attività sono importanti. Amano esplorare.",
    verdetto: "Il Kai Ken è un compagno leale per proprietari esperti che rispettano la sua natura riservata."
  },
  'keeshond.html': {
    meta: "Il Keeshond è un cane olandese allegro con una maschera distintiva. Amichevole, intelligente e ottimo cane da famiglia.",
    hero: "Il Keeshond è un cane olandese allegro, noto per la sua maschera 'occhiali' e la natura amichevole.",
    panoramica: "Il Keeshond era il simbolo dei patrioti olandesi nel XVIII secolo. Il nome deriva da Kees, il nome del cane del leader patriota.",
    temperamento: "I Keeshond sono amichevoli, intelligenti e giocherelloni. Sono ottimi cani da famiglia e buoni cani da guardia. Amano la compagnia.",
    salute: "Predisposti a displasia dell'anca, lussazione della rotula, ipotiroidismo e malattie cardiache. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Si adattano bene a vari stili di vita.",
    verdetto: "Il Keeshond è un compagno allegro e affettuoso per famiglie. Richiede toelettatura regolare."
  },
  'kerry-blue-terrier.html': {
    meta: "Il Kerry Blue Terrier è un terrier irlandese versatile con un mantello blu distintivo. Spiritoso, intelligente e leale.",
    hero: "Il Kerry Blue Terrier è un terrier irlandese versatile, noto per il suo splendido mantello blu-grigio.",
    panoramica: "Il Kerry Blue Terrier è originario della contea di Kerry in Irlanda. Era un cane da fattoria multiuso: cacciatore, guardiano e pastore.",
    temperamento: "I Kerry Blue sono spiritosi, intelligenti e leali. Sono affettuosi con la famiglia ma possono essere aggressivi con altri cani. Richiedono socializzazione.",
    salute: "Predisposti a displasia dell'anca, cataratta, cheratite, ipotiroidismo e problemi cutanei. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e gioco sono importanti. Hanno molta energia.",
    verdetto: "Il Kerry Blue Terrier è un compagno versatile per proprietari esperti. Richiede toelettatura e socializzazione."
  },
  'kishu-ken.html': {
    meta: "Il Kishu Ken è un antico cane giapponese da caccia. Leale, coraggioso e riservato.",
    hero: "Il Kishu Ken è un antico cane giapponese da caccia, noto per la sua lealtà e il coraggio.",
    panoramica: "Il Kishu Ken è originario della regione di Kishu (oggi Wakayama e Mie) in Giappone. Era usato per la caccia al cinghiale e al cervo.",
    temperamento: "I Kishu sono leali, coraggiosi e riservati. Sono devoti a una persona e possono essere diffidenti con gli estranei. Hanno forte istinto predatorio.",
    salute: "Generalmente sani. Predisposti a ipotiroidismo e allergie. Aspettativa di vita 11-13 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e attività sono importanti. Amano esplorare.",
    verdetto: "Il Kishu Ken è un compagno leale per proprietari esperti che possono offrire leadership e attività."
  },
  'komondor.html': {
    meta: "Il Komondor è un guardiano ungherese con un mantello a corde unico. Coraggioso, protettivo e indipendente.",
    hero: "Il Komondor è un guardiano ungherese maestoso, immediatamente riconoscibile per il suo mantello a corde.",
    panoramica: "Il Komondor è un antico guardiano del bestiame ungherese. Il suo mantello a corde lo proteggeva dai predatori e dal clima. È chiamato 'il re dei cani'.",
    temperamento: "I Komondor sono coraggiosi, protettivi e indipendenti. Sono devoti alla famiglia ma diffidenti con gli estranei. Richiedono un proprietario esperto.",
    salute: "Predisposti a displasia dell'anca, torsione gastrica, entropion e problemi cutanei sotto il mantello. Aspettativa di vita 10-12 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e pattugliamento del territorio. Necessitano di spazio.",
    verdetto: "Il Komondor è un guardiano formidabile per proprietari esperti. Il mantello richiede cure speciali."
  },
  'korean-jindo.html': {
    meta: "Il Jindo Coreano è un cane leale e indipendente dall'isola di Jindo. Intelligente, coraggioso e devoto.",
    hero: "Il Jindo Coreano è un cane leale e indipendente, tesoro nazionale della Corea del Sud.",
    panoramica: "Il Jindo Coreano proviene dall'isola di Jindo in Corea del Sud. È il cane nazionale coreano, protetto dalla legge come tesoro naturale.",
    temperamento: "I Jindo sono leali, intelligenti e indipendenti. Formano legami molto forti con il proprietario. Sono diffidenti con gli estranei.",
    salute: "Generalmente sani. Predisposti a ipotiroidismo e allergie. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e attività sono importanti. Hanno forte istinto predatorio.",
    verdetto: "Il Jindo Coreano è un compagno devoto per proprietari esperti che rispettano la sua indipendenza."
  },
  'kuvasz.html': {
    meta: "Il Kuvasz è un maestoso guardiano ungherese con un mantello bianco. Leale, protettivo e indipendente.",
    hero: "Il Kuvasz è un maestoso guardiano ungherese, noto per il suo splendido mantello bianco e la natura protettiva.",
    panoramica: "Il Kuvasz era il guardiano delle greggi reali ungheresi. Il nome potrebbe derivare dal turco 'kawasz' (guardia armata). Re Mattia Corvino ne allevava molti.",
    temperamento: "I Kuvasz sono leali, protettivi e indipendenti. Sono devoti alla famiglia ma diffidenti con gli estranei. Richiedono rispetto della loro indipendenza.",
    salute: "Predisposti a displasia dell'anca, osteocondrite, ipotiroidismo e torsione gastrica. Aspettativa di vita 10-12 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e spazio per pattugliare sono importanti.",
    verdetto: "Il Kuvasz è un guardiano maestoso per proprietari esperti con spazio. Richiede socializzazione precoce."
  },
  'lagotto-romagnolo.html': {
    meta: "Il Lagotto Romagnolo è un cane da tartufi italiano con un mantello riccio. Intelligente, affettuoso e instancabile cercatore.",
    hero: "Il Lagotto Romagnolo è il cane da tartufi per eccellenza, con un magnifico mantello riccio.",
    panoramica: "Il Lagotto Romagnolo è originario della Romagna, dove era usato come cane da riporto in acqua. Oggi è il cane da tartufi più famoso al mondo.",
    temperamento: "I Lagotto sono intelligenti, affettuosi e lavoratori. Sono ottimi cani da famiglia e adorano cercare. Sono facili da addestrare.",
    salute: "Predisposti a displasia dell'anca, epilessia giovanile e problemi oculari. Aspettativa di vita 15-17 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e attività di ricerca sono importanti. Amano lavorare.",
    verdetto: "Il Lagotto Romagnolo è un compagno versatile e affettuoso per famiglie attive. Perfetto per chi ama la ricerca tartufi!"
  },
  'lakeland-terrier.html': {
    meta: "Il Lakeland Terrier è un piccolo terrier inglese coraggioso. Vivace, sicuro e pieno di personalità.",
    hero: "Il Lakeland Terrier è un piccolo terrier inglese coraggioso, originario del Lake District.",
    panoramica: "Il Lakeland Terrier è stato sviluppato nel Lake District in Inghilterra per proteggere le pecore dalle volpi. Era abbastanza coraggioso da seguirle nelle tane.",
    temperamento: "I Lakeland sono vivaci, sicuri e coraggiosi. Hanno la tipica personalità terrier. Sono affettuosi con la famiglia.",
    salute: "Predisposti a malattia di Legg-Calvé-Perthes, lussazione della rotula e problemi oculari. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Hanno molta energia.",
    verdetto: "Il Lakeland Terrier è un compagno vivace per chi cerca un terrier attivo. Richiede stripping del mantello."
  },
  'landseer.html': {
    meta: "Il Landseer è un cane bianco e nero simile al Terranova. Dolce, coraggioso e eccellente nuotatore.",
    hero: "Il Landseer è un cane maestoso bianco e nero, noto per le sue abilità di salvataggio in acqua.",
    panoramica: "Il Landseer prende il nome dal pittore Edwin Landseer che li raffigurava spesso. Alcuni kennel club lo considerano una varietà del Terranova, altri una razza separata.",
    temperamento: "I Landseer sono dolci, pazienti e coraggiosi. Sono ottimi con i bambini e eccellenti nuotatori. Sono naturali salvatori.",
    salute: "Predisposti a displasia dell'anca e del gomito, torsione gastrica, problemi cardiaci e cistinuria. Aspettativa di vita 8-10 anni.",
    esercizio: "Esigenze di esercizio moderate. Amano nuotare. Passeggiate quotidiane sono importanti.",
    verdetto: "Il Landseer è un compagno dolce e coraggioso per famiglie. Richiede spazio e tolleranza per la bava."
  },
  'large-munsterlander.html': {
    meta: "Il Grande Münsterländer è un elegante cane da caccia tedesco. Versatile, intelligente e affettuoso.",
    hero: "Il Grande Münsterländer è un elegante cane da caccia tedesco, eccellente sia sulla terra che in acqua.",
    panoramica: "Il Grande Münsterländer è stato sviluppato nella regione di Münster in Germania. Era originariamente una varietà di colore del Deutsch Langhaar.",
    temperamento: "I Münsterländer sono intelligenti, versatili e affettuosi. Sono ottimi cani da caccia e compagni di famiglia. Sono facili da addestrare.",
    salute: "Predisposti a displasia dell'anca, cataratta e problemi cutanei. Aspettativa di vita 12-13 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica quotidiana. Amano cacciare e nuotare.",
    verdetto: "Il Grande Münsterländer è un compagno versatile per famiglie attive e cacciatori. Richiede esercizio regolare."
  },
  'leonberger.html': {
    meta: "Il Leonberger è un gigante gentile con una criniera leonina. Amichevole, paziente e perfetto per le famiglie.",
    hero: "Il Leonberger è un gigante gentile, noto per la sua criniera leonina e il carattere dolce.",
    panoramica: "Il Leonberger è stato creato a Leonberg, in Germania, nel XIX secolo. Secondo la leggenda, doveva assomigliare al leone dello stemma della città.",
    temperamento: "I Leonberger sono amichevoli, pazienti e gentili. Sono ottimi con i bambini e altri animali. Sono intelligenti e facili da addestrare.",
    salute: "Predisposti a displasia dell'anca e del gomito, osteosarcoma, torsione gastrica e polineuropatia. Aspettativa di vita 7-9 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e nuoto sono ideali. Evitare sforzi eccessivi da cuccioli.",
    verdetto: "Il Leonberger è un gigante gentile perfetto per famiglie con spazio. La breve aspettativa di vita richiede considerazione."
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
