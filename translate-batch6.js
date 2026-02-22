#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const breedsDir = path.join(__dirname, 'it/breeds');

const breedTranslations = {
  'lhasa-apso.html': {
    meta: "Il Lhasa Apso è un antico cane tibetano da guardia. Indipendente, vigile e affettuoso con la famiglia.",
    hero: "Il Lhasa Apso è un antico cane tibetano, guardiano dei monasteri dell'Himalaya da migliaia di anni.",
    panoramica: "Il Lhasa Apso era il guardiano dei monasteri tibetani. Il nome significa 'cane barbuto di Lhasa'. Era considerato sacro e portava fortuna.",
    temperamento: "I Lhasa sono indipendenti, vigili e affettuosi. Sono riservati con gli estranei ma devoti alla famiglia. Possono essere testardi.",
    salute: "Predisposti a displasia dell'anca, problemi oculari, problemi renali e allergie cutanee. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono sufficienti. Si adattano bene alla vita in appartamento.",
    verdetto: "Il Lhasa Apso è un compagno dignitoso e affettuoso per chi apprezza la sua indipendenza. Richiede toelettatura regolare."
  },
  'lowchen.html': {
    meta: "Il Löwchen è un piccolo 'cane leone' allegro e affettuoso. Giocherellone, intelligente e ottimo compagno.",
    hero: "Il Löwchen, o 'Piccolo Cane Leone', è un compagno allegro con una tosatura distintiva simile a un leone.",
    panoramica: "Il Löwchen è una razza antica, raffigurata nell'arte dal Rinascimento. La tosatura a leone è tradizionale. Era quasi estinto negli anni '60.",
    temperamento: "I Löwchen sono allegri, affettuosi e giocherelloni. Sono ottimi cani da famiglia e facili da addestrare. Amano la compagnia.",
    salute: "Predisposti a lussazione della rotula, atrofia retinica progressiva e cataratta. Aspettativa di vita 13-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Si adattano bene a vari stili di vita.",
    verdetto: "Il Löwchen è un compagno allegro e affettuoso per famiglie. Richiede toelettatura regolare."
  },
  'manchester-terrier.html': {
    meta: "Il Manchester Terrier è un elegante terrier inglese, eccellente cacciatore di topi. Vivace, intelligente e leale.",
    hero: "Il Manchester Terrier è un elegante terrier inglese, sviluppato per la caccia ai topi nell'era industriale.",
    panoramica: "Il Manchester Terrier è stato sviluppato a Manchester durante la Rivoluzione Industriale come cacciatore di topi. Disponibile in due varietà: Standard e Toy.",
    temperamento: "I Manchester sono vivaci, intelligenti e leali. Sono affettuosi con la famiglia ma riservati con gli estranei. Hanno forte istinto predatorio.",
    salute: "Predisposti a malattia di von Willebrand, lussazione della rotula e problemi oculari. Aspettativa di vita 15-17 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Hanno molta energia.",
    verdetto: "Il Manchester Terrier è un compagno elegante e leale per chi cerca un terrier atletico."
  },
  'mastiff.html': {
    meta: "Il Mastiff Inglese è uno dei cani più grandi e antichi. Dolce, protettivo e sorprendentemente tranquillo.",
    hero: "Il Mastiff Inglese è uno dei cani più grandi e antichi, un gigante gentile dalla storia millenaria.",
    panoramica: "Il Mastiff è una delle razze più antiche, usata dai Celti e poi dai Romani. Erano cani da guerra, da guardia e purtroppo gladiatori.",
    temperamento: "I Mastiff sono dolci, protettivi e calmi. Sono ottimi con i bambini e naturali guardiani. Sono coraggiosi ma non aggressivi.",
    salute: "Predisposti a displasia dell'anca e del gomito, torsione gastrica, cardiomiopatia e problemi oculari. Aspettativa di vita 6-10 anni.",
    esercizio: "Esigenze di esercizio basse-moderate. Passeggiate quotidiane sono importanti ma evitare sforzi eccessivi.",
    verdetto: "Il Mastiff è un guardiano gentile per famiglie con spazio. Richiede tolleranza per la bava e attenzione alla salute."
  },
  'miniature-american-shepherd.html': {
    meta: "Il Pastore Americano Miniatura è un piccolo cane da pastore intelligente. Versatile, energico e devoto.",
    hero: "Il Pastore Americano Miniatura è la versione più piccola dell'Australian Shepherd, altrettanto intelligente e versatile.",
    panoramica: "Il Pastore Americano Miniatura è stato sviluppato in California negli anni '60 selezionando Australian Shepherd più piccoli. È una razza riconosciuta dal 2015.",
    temperamento: "I MAS sono intelligenti, energici e devoti. Sono versatili nel lavoro e ottimi cani da famiglia. Sono facili da addestrare.",
    salute: "Predisposti a displasia dell'anca, problemi oculari, epilessia e gene MDR1. Aspettativa di vita 12-13 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica e mentale quotidiana. Eccellono negli sport cinofili.",
    verdetto: "Il Pastore Americano Miniatura è un compagno versatile per famiglie attive. Richiede stimolazione costante."
  },
  'miniature-pinscher.html': {
    meta: "Il Pinscher Nano è un piccolo cane vivace e sicuro di sé. Coraggioso, energico e pieno di personalità.",
    hero: "Il Pinscher Nano è un piccolo cane dal grande ego, noto come il 'Re dei Toy' per il suo portamento fiero.",
    panoramica: "Il Pinscher Nano è una razza tedesca antica, non un Dobermann in miniatura come spesso si crede. Era usato come cacciatore di topi nelle stalle.",
    temperamento: "I Min Pin sono vivaci, sicuri di sé e curiosi. Non si rendono conto delle loro piccole dimensioni. Possono essere testardi.",
    salute: "Predisposti a lussazione della rotula, malattia di Legg-Calvé-Perthes, problemi cardiaci ed epilessia. Aspettativa di vita 12-16 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Hanno molta energia.",
    verdetto: "Il Pinscher Nano è un compagno vivace e sicuro per chi cerca un cane toy con personalità."
  },
  'mudi.html': {
    meta: "Il Mudi è un cane da pastore ungherese versatile e raro. Intelligente, energico e coraggioso.",
    hero: "Il Mudi è un cane da pastore ungherese versatile, il più raro dei tre pastori ungheresi.",
    panoramica: "Il Mudi è il più raro dei cani da pastore ungheresi (insieme a Puli e Pumi). È versatile: pastore, cacciatore e cane da guardia.",
    temperamento: "I Mudi sono intelligenti, energici e coraggiosi. Sono versatili nel lavoro e devoti alla famiglia. Possono essere riservati con gli estranei.",
    salute: "Predisposti a displasia dell'anca, epilessia e problemi oculari. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica e mentale quotidiana. Eccellono negli sport cinofili.",
    verdetto: "Il Mudi è un compagno versatile per proprietari attivi. Richiede stimolazione e socializzazione."
  },
  'neapolitan-mastiff.html': {
    meta: "Il Mastino Napoletano è un antico guardiano italiano con pelle rugosa. Protettivo, leale e maestoso.",
    hero: "Il Mastino Napoletano è un antico guardiano italiano, immediatamente riconoscibile per la sua pelle abbondante e rugosa.",
    panoramica: "Il Mastino Napoletano discende dai molossi romani. Era il guardiano delle proprietà nel sud Italia. La razza fu salvata dall'estinzione nel dopoguerra.",
    temperamento: "I Mastini Napoletani sono protettivi, leali e calmi. Sono devoti alla famiglia e naturali guardiani. Richiedono un proprietario esperto.",
    salute: "Predisposti a displasia dell'anca, cardiomiopatia, entropion, problemi cutanei e torsione gastrica. Aspettativa di vita 7-9 anni.",
    esercizio: "Esigenze di esercizio basse-moderate. Passeggiate quotidiane sono importanti. Non tollerano il caldo.",
    verdetto: "Il Mastino Napoletano è un guardiano formidabile per proprietari esperti. Richiede tolleranza per la bava."
  },
  'nederlandse-kooikerhondje.html': {
    meta: "Il Kooikerhondje è un cane da caccia olandese allegro e agile. Amichevole, attento e con un bel mantello bianco e rosso.",
    hero: "Il Kooikerhondje è un cane da caccia olandese allegro, usato per attirare le anatre nelle trappole.",
    panoramica: "Il Kooikerhondje era usato nei 'koois' (trappole per anatre) nei Paesi Bassi. Attirava le anatre curiose verso le reti. Quasi estinto, fu salvato dopo la guerra.",
    temperamento: "I Kooiker sono allegri, attenti e adattabili. Sono ottimi cani da famiglia ma possono essere riservati con gli estranei.",
    salute: "Predisposti a malattia di von Willebrand, cataratta, lussazione della rotula ed epilessia. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Amano l'acqua.",
    verdetto: "Il Kooikerhondje è un compagno allegro e agile per famiglie. Richiede socializzazione."
  },
  'norfolk-terrier.html': {
    meta: "Il Norfolk Terrier è un piccolo terrier inglese con le orecchie pendenti. Vivace, coraggioso e affettuoso.",
    hero: "Il Norfolk Terrier è un piccolo terrier inglese vivace, distinguibile dal Norwich per le orecchie pendenti.",
    panoramica: "Il Norfolk Terrier era originariamente la stessa razza del Norwich Terrier. Furono separati nel 1964: Norfolk con orecchie pendenti, Norwich con orecchie erette.",
    temperamento: "I Norfolk sono vivaci, coraggiosi e affettuosi. Sono più socievoli di molti terrier. Sono ottimi cani da famiglia.",
    salute: "Predisposti a lussazione della rotula, problemi cardiaci e sindrome delle vie aeree superiori. Aspettativa di vita 12-16 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Hanno energia da terrier.",
    verdetto: "Il Norfolk Terrier è un compagno vivace e affettuoso, meno aggressivo di altri terrier."
  },
  'norwegian-buhund.html': {
    meta: "Il Buhund Norvegese è un cane spitz versatile e allegro. Energico, intelligente e ottimo cane da famiglia.",
    hero: "Il Buhund Norvegese è un cane spitz versatile, compagno dei Vichinghi per oltre mille anni.",
    panoramica: "Il Buhund Norvegese accompagnava i Vichinghi nei loro viaggi. Era un cane da fattoria multiuso: pastore, guardiano e compagno.",
    temperamento: "I Buhund sono energici, intelligenti e allegri. Sono ottimi cani da famiglia e facili da addestrare. Possono essere vocali.",
    salute: "Predisposti a displasia dell'anca, problemi oculari e malattia di von Willebrand. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e attività sono importanti. Amano avere un lavoro.",
    verdetto: "Il Buhund Norvegese è un compagno allegro e versatile per famiglie attive."
  },
  'norwegian-elkhound.html': {
    meta: "L'Elkhound Norvegese è un antico cane da caccia vichingo. Leale, coraggioso e resistente.",
    hero: "L'Elkhound Norvegese è un antico cane da caccia vichingo, usato per cacciare alci e orsi.",
    panoramica: "L'Elkhound Norvegese è una delle razze più antiche, compagno dei Vichinghi. Era usato per la caccia all'alce e come cane da guardia.",
    temperamento: "Gli Elkhound sono leali, coraggiosi e indipendenti. Sono affettuosi con la famiglia ma possono essere riservati con gli estranei. Sono vocali.",
    salute: "Predisposti a displasia dell'anca, atrofia retinica progressiva, cisti renali e ipotiroidismo. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e attività sono importanti. Tollerano bene il freddo.",
    verdetto: "L'Elkhound Norvegese è un compagno leale per famiglie attive in climi freschi."
  },
  'norwegian-lundehund.html': {
    meta: "Il Lundehund Norvegese è un cane unico con caratteristiche fisiche straordinarie. Agile, curioso e raro.",
    hero: "Il Lundehund Norvegese è un cane unico con sei dita e articolazioni flessibili, sviluppato per cacciare pulcinella di mare.",
    panoramica: "Il Lundehund era usato per cacciare pulcinella di mare (Lunde) sulle scogliere norvegesi. Ha sei dita per piede e può piegare la testa all'indietro. Quasi estinto, fu salvato nel dopoguerra.",
    temperamento: "I Lundehund sono curiosi, giocherelloni e indipendenti. Possono essere riservati con gli estranei. Sono sensibili e gentili.",
    salute: "Predisposti alla sindrome di Lundehund (malattie intestinali gravi), problemi oculari. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Sono agili arrampicatori.",
    verdetto: "Il Lundehund è un compagno unico per chi apprezza le sue caratteristiche speciali. Richiede dieta attenta."
  },
  'norwich-terrier.html': {
    meta: "Il Norwich Terrier è un piccolo terrier inglese con le orecchie erette. Coraggioso, allegro e affettuoso.",
    hero: "Il Norwich Terrier è un piccolo terrier inglese coraggioso, uno dei più piccoli terrier da lavoro.",
    panoramica: "Il Norwich Terrier era usato a Cambridge per la caccia ai topi. Si distingue dal Norfolk per le orecchie erette.",
    temperamento: "I Norwich sono coraggiosi, allegri e affettuosi. Sono meno aggressivi con altri cani rispetto a molti terrier. Sono ottimi compagni.",
    salute: "Predisposti a sindrome delle vie aeree superiori, lussazione della rotula e problemi dentali. Aspettativa di vita 12-16 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Hanno energia da terrier.",
    verdetto: "Il Norwich Terrier è un compagno vivace e affettuoso per chi cerca un piccolo terrier."
  },
  'nova-scotia-duck-tolling-retriever.html': {
    meta: "Il Toller è un retriever canadese unico che attira le anatre giocando. Intelligente, energico e affettuoso.",
    hero: "Il Nova Scotia Duck Tolling Retriever è un cane unico che attira le anatre con il suo gioco vivace.",
    panoramica: "Il Toller fu sviluppato in Nuova Scozia per 'tolling' - attirare le anatre curiose a riva giocando, poi recuperarle dopo lo sparo. È il retriever più piccolo.",
    temperamento: "I Toller sono intelligenti, energici e affettuosi. Sono versatili e amano lavorare. Possono essere riservati con gli estranei.",
    salute: "Predisposti a displasia dell'anca, atrofia retinica progressiva, malattie autoimmuni e sordità. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica e mentale quotidiana. Amano l'acqua.",
    verdetto: "Il Toller è un compagno versatile per famiglie molto attive. Richiede stimolazione costante."
  },
  'old-english-sheepdog.html': {
    meta: "Il Bobtail è un cane da pastore inglese con un mantello fluente. Allegro, adattabile e ottimo con le famiglie.",
    hero: "Il Bobtail, o Old English Sheepdog, è un cane da pastore allegro con un iconico mantello grigio e bianco.",
    panoramica: "Il Bobtail era usato in Inghilterra per la conduzione del bestiame al mercato. La coda veniva tagliata per indicare lo status di cane da lavoro (esentasse).",
    temperamento: "I Bobtail sono allegri, adattabili e affettuosi. Sono ottimi con i bambini e amano la famiglia. Possono essere un po' testardi.",
    salute: "Predisposti a displasia dell'anca, cataratta, ipotiroidismo e sordità. Aspettativa di vita 10-12 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Non tollerano bene il caldo.",
    verdetto: "Il Bobtail è un compagno allegro per famiglie. Richiede toelettatura intensiva."
  },
  'otterhound.html': {
    meta: "L'Otterhound è un raro segugio inglese con un mantello ruvido. Amichevole, indipendente e instancabile in acqua.",
    hero: "L'Otterhound è un raro segugio inglese, sviluppato per la caccia alla lontra con un mantello impermeabile.",
    panoramica: "L'Otterhound è uno dei segugi più rari, con meno di 1000 esemplari al mondo. Era usato per la caccia alla lontra, ora vietata.",
    temperamento: "Gli Otterhound sono amichevoli, indipendenti e allegri. Sono ottimi con bambini e altri cani. Sono vocali e seguono l'olfatto.",
    salute: "Predisposti a displasia dell'anca, torsione gastrica, epilessia e trombocitopatia. Aspettativa di vita 10-13 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Amano nuotare e seguire tracce. Necessitano di un giardino recintato.",
    verdetto: "L'Otterhound è un compagno raro e allegro per chi ha spazio e ama l'acqua."
  },
  'parson-russell-terrier.html': {
    meta: "Il Parson Russell Terrier è un terrier atletico e vivace. Intelligente, coraggioso e pieno di energia.",
    hero: "Il Parson Russell Terrier è la versione più alta del Jack Russell, atletico e pieno di energia.",
    panoramica: "Il Parson Russell prende il nome dal reverendo John Russell che sviluppò la razza. È più alto e con gambe più lunghe del Jack Russell.",
    temperamento: "I Parson sono intelligenti, coraggiosi e vivaci. Hanno molta energia e personalità. Possono essere testardi.",
    salute: "Predisposti a lussazione della rotula, sordità, atassia e malattia di Legg-Calvé-Perthes. Aspettativa di vita 13-15 anni.",
    esercizio: "Esigenze di esercizio molto elevate. Necessitano di attività intensa quotidiana. Eccellono negli sport cinofili.",
    verdetto: "Il Parson Russell è un compagno energico per proprietari molto attivi."
  },
  'pekingese.html': {
    meta: "Il Pechinese è un antico cane imperiale cinese. Dignitoso, indipendente e devoto al proprietario.",
    hero: "Il Pechinese è un antico cane imperiale cinese, compagno degli imperatori per oltre 2000 anni.",
    panoramica: "Il Pechinese era così sacro che rubarne uno era punito con la morte. Era chiamato 'cane leone' e 'cane manica'. Fu portato in Occidente dopo il sacco del Palazzo d'Estate.",
    temperamento: "I Pechinesi sono dignitosi, indipendenti e affettuosi. Sono devoti al proprietario ma possono essere testardi. Non tollerano manipolazioni eccessive.",
    salute: "Predisposti a problemi respiratori (BOAS), problemi oculari, problemi alla schiena e colpo di calore. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio basse. Brevi passeggiate e gioco sono sufficienti. Evitare il caldo.",
    verdetto: "Il Pechinese è un compagno dignitoso per chi rispetta la sua indipendenza. Richiede toelettatura e attenzione al caldo."
  },
  'pembroke-welsh-corgi.html': {
    meta: "Il Pembroke Welsh Corgi è un piccolo cane da pastore energico, il preferito della Regina Elisabetta II.",
    hero: "Il Pembroke Welsh Corgi è un piccolo cane da pastore energico, amato dalla Regina Elisabetta II per tutta la sua vita.",
    panoramica: "Il Pembroke Welsh Corgi è originario del Galles, dove conduceva il bestiame. È più piccolo e senza coda rispetto al Cardigan. Era il preferito della Regina Elisabetta II.",
    temperamento: "I Corgi sono intelligenti, vivaci e affettuosi. Sono ottimi cani da famiglia e hanno una grande personalità. Possono essere vocali.",
    salute: "Predisposti a problemi alla schiena (IVDD), displasia dell'anca, mielopatia degenerativa e problemi oculari. Aspettativa di vita 12-13 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e gioco sono essenziali. Mantenere il peso forma.",
    verdetto: "Il Pembroke Welsh Corgi è un compagno vivace e affettuoso per famiglie. Attenzione al peso e alla schiena."
  },
  'peruvian-inca-orchid.html': {
    meta: "Il Perro Sin Pelo del Perù è un antico cane senza pelo. Elegante, affettuoso e con la pelle sensibile.",
    hero: "Il Perro Sin Pelo del Perù è un antico cane senza pelo, tesoro nazionale del Perù.",
    panoramica: "Il Perro Sin Pelo del Perù è una razza antica, raffigurata nella ceramica delle civiltà preincaiche. È disponibile in tre taglie e in varietà con e senza pelo.",
    temperamento: "I PIO sono affettuosi, intelligenti e riservati con gli estranei. Sono devoti alla famiglia e sensibili. Possono essere protettivi.",
    salute: "Predisposti a problemi cutanei (necessitano protezione solare), problemi dentali e IBD. Aspettativa di vita 11-12 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono sufficienti. Proteggere dal sole e dal freddo.",
    verdetto: "Il Perro Sin Pelo del Perù è un compagno elegante per chi può curare la sua pelle delicata."
  },
  'petit-basset-griffon-vendeen.html': {
    meta: "Il Petit Basset Griffon Vendéen è un allegro segugio francese. Vivace, socievole e instancabile.",
    hero: "Il Petit Basset Griffon Vendéen è un allegro segugio francese, più piccolo del Grand Basset.",
    panoramica: "Il PBGV è originario della Vandea in Francia, sviluppato per la caccia al coniglio. È un cane allegro e socievole.",
    temperamento: "I PBGV sono allegri, vivaci e socievoli. Sono ottimi con bambini e altri cani. Hanno un forte istinto da segugio e sono vocali.",
    salute: "Predisposti a problemi oculari, epilessia, ipotiroidismo e problemi alla tiroide. Aspettativa di vita 14-16 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e opportunità di seguire tracce sono importanti.",
    verdetto: "Il PBGV è un compagno allegro e socievole per famiglie. Richiede toelettatura e recinzione sicura."
  },
  'pharaoh-hound.html': {
    meta: "Il Pharaoh Hound è un levriero elegante dall'aspetto antico. Atletico, affettuoso e arrossisce di emozione.",
    hero: "Il Pharaoh Hound è un levriero elegante che arrossisce quando è felice - orecchie e naso diventano rosa!",
    panoramica: "Il Pharaoh Hound è il cane nazionale di Malta, dove è chiamato Kelb tal-Fenek (cane coniglio). È una delle razze più antiche, simile ai cani egizi.",
    temperamento: "I Pharaoh Hound sono atletici, affettuosi e giocherelloni. Sono sensibili e intelligenti. Arrossiscono letteralmente quando sono emozionati.",
    salute: "Generalmente sani ma predisposti a sensibilità all'anestesia e displasia dell'anca. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio elevate. Amano correre e necessitano di un'area recintata. Hanno forte istinto predatorio.",
    verdetto: "Il Pharaoh Hound è un compagno elegante e affettuoso per famiglie attive. Non adatto a case con piccoli animali."
  },
  'plott-hound.html': {
    meta: "Il Plott Hound è un segugio americano per la caccia all'orso. Coraggioso, leale e con un mantello tigrato.",
    hero: "Il Plott Hound è il cane di stato della Carolina del Nord, un segugio coraggioso per la caccia grossa.",
    panoramica: "Il Plott Hound fu portato negli Appalachi dalla famiglia Plott nel 1750. È l'unico coonhound senza antenati inglesi - discende dai cani da caccia tedeschi.",
    temperamento: "I Plott sono coraggiosi, leali e determinati. Sono ottimi cani da caccia e compagni. Possono essere riservati con gli estranei.",
    salute: "Predisposti a displasia dell'anca, torsione gastrica e infezioni alle orecchie. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di molto spazio e attività quotidiana. Amano seguire tracce.",
    verdetto: "Il Plott Hound è un compagno leale per cacciatori e famiglie rurali. Richiede spazio e attività."
  },
  'polish-lowland-sheepdog.html': {
    meta: "Il Pastore Polacco di Pianura è un cane da pastore robusto con un mantello lungo. Intelligente, vivace e ottimo guardiano.",
    hero: "Il Pastore Polacco di Pianura è un cane da pastore robusto, antenato del Bearded Collie.",
    panoramica: "Il PON (Polski Owczarek Nizinny) è una razza polacca antica usata per la conduzione del bestiame. Fu quasi estinto dopo la guerra ma salvato da allevatori dedicati.",
    temperamento: "I PON sono intelligenti, vivaci e indipendenti. Sono ottimi guardiani e devoti alla famiglia. Possono essere testardi.",
    salute: "Predisposti a displasia dell'anca, atrofia retinica progressiva e ipotiroidismo. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e attività mentale sono importanti.",
    verdetto: "Il PON è un compagno intelligente e vigile per famiglie. Richiede toelettatura e socializzazione."
  },
  'portuguese-podengo-pequeno.html': {
    meta: "Il Podengo Portoghese Piccolo è un cacciatore di conigli agile e vivace. Allegro, intelligente e pieno di energia.",
    hero: "Il Podengo Portoghese Piccolo è un cacciatore di conigli agile, il più piccolo dei Podengo.",
    panoramica: "Il Podengo Portoghese esiste in tre taglie. Il Piccolo era usato per cacciare conigli nelle tane e tra i cespugli. È una razza primitiva e resistente.",
    temperamento: "I Podengo Piccoli sono vivaci, intelligenti e allegri. Sono affettuosi con la famiglia ma possono essere riservati con gli estranei. Hanno forte istinto predatorio.",
    salute: "Generalmente sani. Predisposti a lussazione della rotula e problemi dentali. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e gioco sono importanti. Amano correre.",
    verdetto: "Il Podengo Piccolo è un compagno vivace per famiglie attive. Richiede recinzione sicura."
  },
  'pudelpointer.html': {
    meta: "Il Pudelpointer è un cane da caccia tedesco versatile. Intelligente, energico e eccellente in acqua.",
    hero: "Il Pudelpointer è un cane da caccia tedesco versatile, incrocio tra Poodle e Pointer.",
    panoramica: "Il Pudelpointer fu creato in Germania nel XIX secolo incrociando Poodle e Pointer per ottenere un cane da caccia versatile eccellente sia in acqua che sulla terra.",
    temperamento: "I Pudelpointer sono intelligenti, energici e versatili. Sono ottimi cani da caccia e compagni. Sono facili da addestrare.",
    salute: "Generalmente sani. Predisposti a displasia dell'anca ed epilessia. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica quotidiana. Eccellono nella caccia.",
    verdetto: "Il Pudelpointer è un compagno versatile per cacciatori e famiglie attive. Richiede esercizio regolare."
  },
  'puli.html': {
    meta: "Il Puli è un cane ungherese con un mantello a corde unico. Energico, intelligente e sempre vigile.",
    hero: "Il Puli è un cane ungherese con un iconico mantello a corde, un acrobata tra i cani da pastore.",
    panoramica: "Il Puli era il cane da pastore dei Magiari. Il suo mantello a corde si sviluppa naturalmente e lo proteggeva dal clima e dai predatori.",
    temperamento: "I Puli sono energici, intelligenti e vigili. Sono eccellenti guardiani e molto legati alla famiglia. Possono essere riservati con gli estranei.",
    salute: "Predisposti a displasia dell'anca, atrofia retinica progressiva e cataratta. Aspettativa di vita 10-15 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica e mentale quotidiana. Sono agili e atletici.",
    verdetto: "Il Puli è un compagno unico per proprietari attivi. Il mantello richiede cure speciali."
  },
  'pumi.html': {
    meta: "Il Pumi è un cane ungherese con orecchie distintive. Energico, intelligente e sempre pronto all'azione.",
    hero: "Il Pumi è un cane ungherese energico con caratteristiche orecchie semi-erette e ricci.",
    panoramica: "Il Pumi è nato dall'incrocio tra Puli e terrier nel XVII-XVIII secolo. Era usato per la conduzione del bestiame nelle fattorie ungheresi.",
    temperamento: "I Pumi sono energici, intelligenti e vivaci. Sono ottimi cani da lavoro e compagni. Possono essere vocali e riservati con gli estranei.",
    salute: "Predisposti a displasia dell'anca, lussazione della rotula e malattia degenerativa delle articolazioni. Aspettativa di vita 12-13 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica e mentale quotidiana. Eccellono negli sport cinofili.",
    verdetto: "Il Pumi è un compagno energico per proprietari attivi. Richiede stimolazione costante."
  },
  'pyrenean-shepherd.html': {
    meta: "Il Pastore dei Pirenei è un piccolo cane da pastore francese. Energico, intelligente e instancabile.",
    hero: "Il Pastore dei Pirenei è il compagno di lavoro del Grande Pirenei, piccolo ma incredibilmente energico.",
    panoramica: "Il Pastore dei Pirenei conduceva le greggi mentre il Grande Pirenei le proteggeva. È uno dei cani più energici e intelligenti.",
    temperamento: "I Pastori dei Pirenei sono energici, intelligenti e sensibili. Sono devoti alla famiglia ma riservati con gli estranei. Hanno bisogno di lavorare.",
    salute: "Predisposti a displasia dell'anca, epilessia e problemi oculari. Aspettativa di vita 17-19 anni (tra le più lunghe).",
    esercizio: "Esigenze di esercizio molto elevate. Necessitano di attività fisica e mentale intensa. Non adatti a vita sedentaria.",
    verdetto: "Il Pastore dei Pirenei è per proprietari molto attivi che possono offrire lavoro costante."
  },
  'rat-terrier.html': {
    meta: "Il Rat Terrier è un terrier americano versatile. Intelligente, vivace e eccellente cacciatore di roditori.",
    hero: "Il Rat Terrier è un terrier americano versatile, sviluppato per essere il cacciatore di roditori perfetto.",
    panoramica: "Il Rat Terrier fu sviluppato negli Stati Uniti incrociando vari terrier e altri cani. Era il cane da fattoria americano per eccellenza.",
    temperamento: "I Rat Terrier sono intelligenti, vivaci e affettuosi. Sono più calmi di molti terrier. Sono ottimi cani da famiglia.",
    salute: "Predisposti a lussazione della rotula, displasia dell'anca, allergie e malattia di Legg-Calvé-Perthes. Aspettativa di vita 12-18 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Hanno energia terrier.",
    verdetto: "Il Rat Terrier è un compagno versatile e affettuoso per famiglie."
  },
  'redbone-coonhound.html': {
    meta: "Il Redbone Coonhound è un segugio americano dal mantello rosso. Amichevole, rilassato e con una voce melodiosa.",
    hero: "Il Redbone Coonhound è un segugio americano dal bellissimo mantello rosso, noto per la voce melodiosa.",
    panoramica: "Il Redbone Coonhound fu sviluppato nel sud degli Stati Uniti per la caccia al procione e ad altra selvaggina. Il mantello rosso è il suo marchio distintivo.",
    temperamento: "I Redbone sono amichevoli, rilassati e affettuosi. Sono ottimi con bambini e altri cani. Sono vocali e seguono l'olfatto.",
    salute: "Predisposti a displasia dell'anca, infezioni alle orecchie e obesità. Aspettativa di vita 11-12 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Necessitano di spazio e attività quotidiana. Amano seguire tracce.",
    verdetto: "Il Redbone Coonhound è un compagno rilassato per famiglie con spazio. Richiede esercizio e tolleranza per l'abbaio."
  },
  'rhodesian-ridgeback.html': {
    meta: "Il Rhodesian Ridgeback è un cane sudafricano potente con una cresta distintiva. Leale, protettivo e atletico.",
    hero: "Il Rhodesian Ridgeback è un cane sudafricano potente, noto per la cresta di pelo sul dorso e il coraggio nella caccia al leone.",
    panoramica: "Il Rhodesian Ridgeback fu sviluppato in Rhodesia (oggi Zimbabwe) per la caccia al leone. Non combatteva i leoni, ma li teneva a bada finché arrivavano i cacciatori.",
    temperamento: "I Ridgeback sono leali, protettivi e atletici. Sono affettuosi con la famiglia ma riservati con gli estranei. Richiedono un proprietario esperto.",
    salute: "Predisposti a displasia dell'anca e del gomito, ipotiroidismo, seno dermoide e torsione gastrica. Aspettativa di vita 10-12 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica quotidiana. Amano correre.",
    verdetto: "Il Rhodesian Ridgeback è un compagno leale per proprietari esperti. Richiede socializzazione e leadership."
  },
  'russell-terrier.html': {
    meta: "Il Russell Terrier è un piccolo terrier vivace e coraggioso. Intelligente, energico e pieno di carattere.",
    hero: "Il Russell Terrier è la versione più corta della famiglia Jack Russell, altrettanto vivace e coraggioso.",
    panoramica: "Il Russell Terrier è la versione più bassa e proporzionata del Jack Russell originale. È stato riconosciuto come razza separata per distinguerlo dal Parson Russell più alto.",
    temperamento: "I Russell sono intelligenti, coraggiosi e vivaci. Hanno molta personalità e energia. Possono essere testardi.",
    salute: "Predisposti a lussazione della rotula, sordità e malattia di Legg-Calvé-Perthes. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività intensa quotidiana. Eccellono negli sport cinofili.",
    verdetto: "Il Russell Terrier è un compagno energico per proprietari attivi che possono gestire la sua personalità."
  },
  'russian-toy.html': {
    meta: "Il Russian Toy è uno dei cani più piccoli al mondo. Elegante, vivace e devoto al proprietario.",
    hero: "Il Russian Toy è uno dei cani più piccoli al mondo, elegante e pieno di personalità.",
    panoramica: "Il Russian Toy fu sviluppato in Russia dall'English Toy Terrier. Quasi estinto durante la Rivoluzione, fu salvato da allevatori dedicati. Disponibile a pelo lungo e corto.",
    temperamento: "I Russian Toy sono vivaci, intelligenti e devoti. Sono affettuosi con il proprietario ma possono essere riservati con gli estranei. Sono coraggiosi nonostante la taglia.",
    salute: "Predisposti a lussazione della rotula, malattia di Legg-Calvé-Perthes e problemi dentali. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio basse. Brevi passeggiate e gioco sono sufficienti. Sensibili al freddo.",
    verdetto: "Il Russian Toy è un compagno elegante e devoto per chi cerca un cane toy raffinato."
  },
  'saluki.html': {
    meta: "Il Saluki è uno dei levrieri più antichi, elegante e veloce. Indipendente, gentile e fedele.",
    hero: "Il Saluki è uno dei cani più antichi, un levriero elegante che cacciava con i faraoni egizi.",
    panoramica: "Il Saluki è una delle razze più antiche, raffigurato nelle tombe egizie di 4000 anni fa. Era così prezioso che i beduini lo trattavano come membro della famiglia.",
    temperamento: "I Saluki sono indipendenti, gentili e fedeli. Sono riservati ma affettuosi con la famiglia. Hanno un forte istinto predatorio.",
    salute: "Generalmente sani ma predisposti a cardiomiopatia, ipotiroidismo e sensibilità all'anestesia. Aspettativa di vita 10-17 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Amano correre e necessitano di un'area recintata. Tranquilli in casa.",
    verdetto: "Il Saluki è un compagno elegante per chi apprezza un cane indipendente. Non adatto a case con piccoli animali."
  },
  'schipperke.html': {
    meta: "Lo Schipperke è un piccolo cane belga nero, il 'piccolo capitano'. Vivace, curioso e un ottimo cane da guardia.",
    hero: "Lo Schipperke è un piccolo cane belga nero, chiamato il 'piccolo capitano' per il suo ruolo sulle chiatte.",
    panoramica: "Lo Schipperke era il cane delle chiatte belghe, dove cacciava i topi e faceva la guardia. Il nome potrebbe significare 'piccolo capitano' o 'piccolo pastore'.",
    temperamento: "Gli Schipperke sono vivaci, curiosi e coraggiosi. Sono ottimi cani da guardia e molto devoti. Possono essere testardi.",
    salute: "Predisposti a mucopolisaccaridosi, displasia dell'anca e problemi oculari. Aspettativa di vita 12-16 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Hanno molta energia.",
    verdetto: "Lo Schipperke è un compagno vivace e vigile per chi cerca un piccolo cane da guardia."
  },
  'scottish-deerhound.html': {
    meta: "Il Deerhound Scozzese è un levriero maestoso dalla storia reale. Gentile, dignitoso e sorprendentemente tranquillo.",
    hero: "Il Deerhound Scozzese è un levriero maestoso, il 'Segugio Reale della Scozia'.",
    panoramica: "Il Deerhound Scozzese era così prezioso che solo i nobili potevano possederne uno. Era usato per la caccia al cervo rosso nelle Highlands.",
    temperamento: "I Deerhound sono gentili, dignitosi e affettuosi. Sono tranquilli in casa ma veloci sul campo. Sono ottimi con i bambini.",
    salute: "Predisposti a cardiomiopatia dilatativa, torsione gastrica, osteosarcoma e cistinuria. Aspettativa di vita 8-11 anni.",
    esercizio: "Esigenze di esercizio moderate. Amano correre ma sono anche felici di rilassarsi. Necessitano di spazio sicuro per correre.",
    verdetto: "Il Deerhound è un compagno maestoso e gentile per chi ha spazio. La breve aspettativa di vita richiede considerazione."
  },
  'scottish-terrier.html': {
    meta: "Lo Scottish Terrier è un terrier dignitoso e indipendente. Coraggioso, sicuro e con una barba distintiva.",
    hero: "Lo Scottish Terrier è un terrier dignitoso con una silhouette inconfondibile, il 'Diehard'.",
    panoramica: "Lo Scottish Terrier, o Scottie, è uno dei terrier scozzesi più antichi. Era usato per la caccia a tassi e volpi. È il cane del gioco Monopoly.",
    temperamento: "Gli Scottie sono dignitosi, indipendenti e coraggiosi. Possono essere riservati con gli estranei. Sono leali ma testardi.",
    salute: "Predisposti a crampi dello Scottie, malattia di von Willebrand, cancro alla vescica e problemi cutanei. Aspettativa di vita 12 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Non amano il caldo.",
    verdetto: "Lo Scottish Terrier è un compagno dignitoso per chi apprezza la sua indipendenza. Richiede toelettatura."
  },
  'sealyham-terrier.html': {
    meta: "Il Sealyham Terrier è un terrier gallese robusto e allegro. Coraggioso, adattabile e con un carattere affascinante.",
    hero: "Il Sealyham Terrier è un terrier gallese robusto, un tempo il preferito di Hollywood.",
    panoramica: "Il Sealyham fu sviluppato a Sealyham House in Galles per la caccia a tassi e lontre. Era molto popolare negli anni '20-'40 ma oggi è raro.",
    temperamento: "I Sealyham sono coraggiosi, allegri e adattabili. Sono più calmi di molti terrier. Sono affettuosi e divertenti.",
    salute: "Predisposti a sordità, problemi oculari e displasia della retina. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono sufficienti. Sono versatili.",
    verdetto: "Il Sealyham è un terrier raro e affascinante per chi cerca qualcosa di speciale. Richiede toelettatura."
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
