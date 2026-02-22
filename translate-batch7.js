#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const breedsDir = path.join(__dirname, 'it/breeds');

const breedTranslations = {
  'shikoku.html': {
    meta: "Lo Shikoku è un antico cane giapponese da caccia. Leale, coraggioso e primitivo nel carattere.",
    hero: "Lo Shikoku è un antico cane giapponese, uno dei sei cani nativi del Giappone.",
    panoramica: "Lo Shikoku è originario dell'isola giapponese di Shikoku, dove cacciava cinghiali nelle montagne. È considerato più primitivo dello Shiba Inu.",
    temperamento: "Gli Shikoku sono leali, coraggiosi e vigili. Sono devoti al proprietario ma possono essere riservati con gli estranei. Hanno forte istinto predatorio.",
    salute: "Generalmente sani. Predisposti a displasia dell'anca e ipotiroidismo. Aspettativa di vita 10-12 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e attività sono importanti. Amano esplorare.",
    verdetto: "Lo Shikoku è un compagno primitivo per proprietari esperti che comprendono i cani giapponesi."
  },
  'silky-terrier.html': {
    meta: "Il Silky Terrier è un piccolo terrier australiano con un mantello setoso. Vivace, sicuro e pieno di carattere.",
    hero: "Il Silky Terrier è un piccolo terrier australiano elegante, con un magnifico mantello blu e tan.",
    panoramica: "Il Silky Terrier fu sviluppato in Australia incrociando Yorkshire Terrier e Australian Terrier. È più grande dello Yorkie e più terrier nel temperamento.",
    temperamento: "I Silky sono vivaci, sicuri e intelligenti. Hanno la tipica personalità terrier. Sono affettuosi ma possono essere testardi.",
    salute: "Predisposti a lussazione della rotula, collasso tracheale, malattia di Legg-Calvé-Perthes e diabete. Aspettativa di vita 13-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Hanno energia da terrier.",
    verdetto: "Il Silky Terrier è un compagno vivace per chi cerca un terrier toy elegante. Richiede toelettatura."
  },
  'skye-terrier.html': {
    meta: "Lo Skye Terrier è un elegante terrier scozzese con un lungo mantello. Coraggioso, leale e dignitoso.",
    hero: "Lo Skye Terrier è un elegante terrier scozzese, noto per il lungo mantello che tocca terra.",
    panoramica: "Lo Skye Terrier è originario dell'Isola di Skye in Scozia. Era il preferito della Regina Vittoria. Greyfriars Bobby, il cane più fedele, era uno Skye.",
    temperamento: "Gli Skye sono coraggiosi, leali e dignitosi. Sono devoti a una persona. Possono essere riservati con gli estranei.",
    salute: "Predisposti a problemi alla schiena (evitare salti), ipotiroidismo e malattie autoimmuni. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Evitare salti per la schiena.",
    verdetto: "Lo Skye Terrier è un compagno elegante e leale. Richiede toelettatura e attenzione alla schiena."
  },
  'sloughi.html': {
    meta: "Lo Sloughi è un levriero nordafricano elegante e veloce. Riservato, gentile e profondamente fedele.",
    hero: "Lo Sloughi è un levriero nordafricano elegante, il 'levriero arabo'.",
    panoramica: "Lo Sloughi è originario del Nordafrica, dove era molto apprezzato dai beduini per la caccia alla gazzella e alla lepre. È simile al Saluki ma più robusto.",
    temperamento: "Gli Sloughi sono riservati, gentili e fedeli. Formano legami profondi con il proprietario. Possono essere timidi con gli estranei.",
    salute: "Generalmente sani. Predisposti a atrofia retinica progressiva e sensibilità all'anestesia. Aspettativa di vita 12-16 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Amano correre e necessitano di un'area recintata. Tranquilli in casa.",
    verdetto: "Lo Sloughi è un compagno elegante per chi apprezza un cane sensibile e riservato."
  },
  'small-munsterlander.html': {
    meta: "Il Piccolo Münsterländer è un elegante cane da caccia tedesco. Intelligente, versatile e affettuoso.",
    hero: "Il Piccolo Münsterländer è un elegante cane da caccia tedesco, più piccolo del Grande Münsterländer.",
    panoramica: "Il Piccolo Münsterländer è una razza tedesca da caccia versatile. Nonostante il nome, non è una versione ridotta del Grande Münsterländer ma una razza separata.",
    temperamento: "I Piccoli Münsterländer sono intelligenti, versatili e affettuosi. Sono ottimi cani da famiglia e compagni di caccia. Sono facili da addestrare.",
    salute: "Generalmente sani. Predisposti a displasia dell'anca e problemi oculari. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica quotidiana. Amano cacciare e nuotare.",
    verdetto: "Il Piccolo Münsterländer è un compagno versatile per famiglie attive e cacciatori."
  },
  'smooth-fox-terrier.html': {
    meta: "Il Fox Terrier a Pelo Liscio è un terrier classico elegante. Vivace, coraggioso e pieno di carattere.",
    hero: "Il Fox Terrier a Pelo Liscio è un terrier classico, il prototipo del terrier da esposizione.",
    panoramica: "Il Fox Terrier a Pelo Liscio è uno dei terrier più antichi, sviluppato in Inghilterra per la caccia alla volpe. Era il compagno di molti esploratori e avventurieri.",
    temperamento: "I Smooth Fox Terrier sono vivaci, coraggiosi e intelligenti. Hanno molta energia e personalità. Possono essere testardi.",
    salute: "Predisposti a sordità, lussazione della rotula e malattia di Legg-Calvé-Perthes. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica quotidiana. Sono atleti naturali.",
    verdetto: "Il Fox Terrier a Pelo Liscio è un compagno energico per proprietari attivi."
  },
  'soft-coated-wheaten-terrier.html': {
    meta: "Il Soft-Coated Wheaten Terrier è un terrier irlandese allegro con un morbido mantello color grano. Amichevole, giocherellone ed esuberante.",
    hero: "Il Soft-Coated Wheaten Terrier è un terrier irlandese allegro, con un morbido mantello color grano.",
    panoramica: "Il Wheaten era il cane da fattoria irlandese multiuso: cacciatore, guardiano e pastore. Era il 'terrier del povero'. Il mantello matura al color grano verso i due anni.",
    temperamento: "I Wheaten sono allegri, amichevoli ed esuberanti. Sono meno aggressivi di altri terrier. Sono ottimi cani da famiglia.",
    salute: "Predisposti a enteropatia proteino-disperdente, nefropatia, displasia dell'anca e allergie. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e gioco sono importanti. Sono energici.",
    verdetto: "Il Wheaten è un terrier allegro e amichevole per famiglie. Richiede toelettatura regolare."
  },
  'spanish-water-dog.html': {
    meta: "Il Cane d'Acqua Spagnolo è un cane da lavoro versatile con un mantello riccio. Intelligente, atletico e devoto.",
    hero: "Il Cane d'Acqua Spagnolo è un cane da lavoro versatile, usato per la pastorizia e la caccia in acqua.",
    panoramica: "Il Cane d'Acqua Spagnolo è una razza antica usata nella penisola iberica per la pastorizia, la caccia e come aiutante dei pescatori. Il mantello forma naturalmente corde.",
    temperamento: "Gli SWD sono intelligenti, atletici e devoti. Sono versatili nel lavoro e affettuosi con la famiglia. Possono essere riservati con gli estranei.",
    salute: "Predisposti a displasia dell'anca, atrofia retinica progressiva, allergie e ipotiroidismo. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio elevate. Amano nuotare e lavorare. Necessitano di stimolazione fisica e mentale.",
    verdetto: "Il Cane d'Acqua Spagnolo è un compagno versatile per proprietari attivi. Richiede cure del mantello."
  },
  'spinone-italiano.html': {
    meta: "Lo Spinone Italiano è un antico cane da caccia italiano. Dolce, paziente e instancabile sul campo.",
    hero: "Lo Spinone Italiano è un antico cane da caccia italiano, noto per la sua dolcezza e il mantello ruvido.",
    panoramica: "Lo Spinone Italiano è una delle razze da caccia più antiche, con origini che risalgono a oltre 2000 anni fa. Il nome deriva da 'spino', il cespuglio spinoso dove cacciava.",
    temperamento: "Gli Spinone sono dolci, pazienti e socievoli. Sono ottimi cani da famiglia e compagni di caccia. Sono calmi in casa.",
    salute: "Predisposti a displasia dell'anca, torsione gastrica, entropion ed atassia cerebellare. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e caccia sono ideali. Non sono velocisti ma hanno resistenza.",
    verdetto: "Lo Spinone Italiano è un compagno dolce e versatile per famiglie. Richiede toelettatura del mantello ruvido."
  },
  'staffordshire-bull-terrier.html': {
    meta: "Lo Staffordshire Bull Terrier è un cane coraggioso e affettuoso. Leale, giocherellone e ottimo con i bambini.",
    hero: "Lo Staffordshire Bull Terrier è un cane coraggioso e affettuoso, soprannominato 'nanny dog' per l'amore verso i bambini.",
    panoramica: "Lo Staffordshire Bull Terrier discende dai cani da combattimento inglesi. Oggi è un amato cane da famiglia, noto per la dolcezza con i bambini.",
    temperamento: "Gli Staffie sono coraggiosi, affettuosi e giocherelloni. Sono eccellenti con i bambini e devoti alla famiglia. Possono essere dominanti con altri cani.",
    salute: "Predisposti a displasia dell'anca e del gomito, cataratta, problemi cutanei e L-2HGA. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e gioco sono essenziali. Sono muscolosi e atletici.",
    verdetto: "Lo Staffie è un compagno leale e affettuoso per famiglie. Richiede socializzazione con altri cani."
  },
  'standard-schnauzer.html': {
    meta: "Lo Schnauzer Standard è un cane tedesco versatile e vigile. Intelligente, leale e spiritoso.",
    hero: "Lo Schnauzer Standard è la taglia originale dello Schnauzer, un cane tedesco versatile e vigile.",
    panoramica: "Lo Schnauzer Standard è la taglia originale, da cui derivano Gigante e Nano. Era un cane da fattoria multiuso in Germania: guardiano, cacciatore di ratti e compagno.",
    temperamento: "Gli Schnauzer Standard sono intelligenti, leali e spiritosi. Sono ottimi cani da guardia e compagni. Possono essere testardi.",
    salute: "Predisposti a displasia dell'anca, problemi oculari e malattie cardiache. Aspettativa di vita 13-16 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e attività mentale sono importanti. Sono versatili.",
    verdetto: "Lo Schnauzer Standard è un compagno versatile per famiglie. Richiede toelettatura regolare."
  },
  'sussex-spaniel.html': {
    meta: "Il Sussex Spaniel è un raro spaniel inglese dal mantello dorato. Calmo, affettuoso e con un'espressione malinconica.",
    hero: "Il Sussex Spaniel è un raro spaniel inglese, noto per il suo ricco mantello dorato e l'espressione pensierosa.",
    panoramica: "Il Sussex Spaniel fu sviluppato nel Sussex, in Inghilterra, per la caccia nel terreno fitto. È uno degli spaniel più rari e più antichi.",
    temperamento: "I Sussex sono calmi, affettuosi e leali. Sono più tranquilli degli altri spaniel. Possono essere vocali.",
    salute: "Predisposti a displasia dell'anca, problemi cardiaci e sindrome dell'esercizio indotto. Aspettativa di vita 13-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane sono importanti. Sono più lenti degli altri spaniel.",
    verdetto: "Il Sussex Spaniel è un compagno raro e affettuoso per chi cerca uno spaniel più tranquillo."
  },
  'swedish-vallhund.html': {
    meta: "Il Vallhund Svedese è un antico cane vichingo simile al Corgi. Energico, intelligente e versatile.",
    hero: "Il Vallhund Svedese è un antico cane vichingo, il Corgi scandinavo.",
    panoramica: "Il Vallhund Svedese accompagnava i Vichinghi oltre 1000 anni fa. È dibattuto se sia l'antenato del Corgi o viceversa. Era usato per la conduzione del bestiame.",
    temperamento: "I Vallhund sono energici, intelligenti e allegri. Sono ottimi cani da famiglia e versatili nel lavoro. Possono essere vocali.",
    salute: "Predisposti a retinopatia svedese del Vallhund, displasia dell'anca e problemi alla schiena. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e gioco sono importanti. Hanno molta energia.",
    verdetto: "Il Vallhund Svedese è un compagno energico e versatile per famiglie attive."
  },
  'thai-ridgeback.html': {
    meta: "Il Thai Ridgeback è un antico cane thailandese con una cresta distintiva. Indipendente, atletico e protettivo.",
    hero: "Il Thai Ridgeback è un antico cane thailandese, una delle uniche tre razze con la cresta sul dorso.",
    panoramica: "Il Thai Ridgeback è una razza primitiva thailandese, sviluppata in isolamento per secoli. La cresta di pelo sul dorso cresce in direzione opposta.",
    temperamento: "I Thai Ridgeback sono indipendenti, atletici e protettivi. Sono riservati con gli estranei. Richiedono un proprietario esperto.",
    salute: "Generalmente sani. Predisposti a seno dermoide e displasia dell'anca. Aspettativa di vita 12-13 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e attività sono importanti. Sono atleti naturali.",
    verdetto: "Il Thai Ridgeback è un compagno primitivo per proprietari molto esperti."
  },
  'tibetan-mastiff.html': {
    meta: "Il Mastino Tibetano è un guardiano maestoso dell'Himalaya. Indipendente, protettivo e impressionante.",
    hero: "Il Mastino Tibetano è un guardiano maestoso, protettore delle greggi e dei monasteri himalayani da migliaia di anni.",
    panoramica: "Il Mastino Tibetano è una delle razze più antiche e primitive. Era il guardiano dei monasteri e delle greggi tibetane. È diventato molto costoso in Cina.",
    temperamento: "I Mastini Tibetani sono indipendenti, protettivi e calmi. Sono devoti alla famiglia ma riservati con gli estranei. Richiedono un proprietario esperto.",
    salute: "Predisposti a displasia dell'anca e del gomito, ipotiroidismo e problemi oculari. Aspettativa di vita 10-12 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e pattugliamento del territorio. Sono più attivi di notte.",
    verdetto: "Il Mastino Tibetano è un guardiano formidabile per proprietari molto esperti con spazio."
  },
  'tibetan-spaniel.html': {
    meta: "Il Tibetan Spaniel è un antico cane tibetano da compagnia. Intelligente, giocherellone e affettuoso.",
    hero: "Il Tibetan Spaniel è un antico cane tibetano, sentinella dei monasteri himalayani.",
    panoramica: "Il Tibetan Spaniel era tenuto dai monaci tibetani come sentinella e compagno. Girava le ruote della preghiera e avvisava i mastini dei visitatori.",
    temperamento: "I Tibbie sono intelligenti, giocherelloni e affettuosi. Sono indipendenti ma devoti. Sono ottimi cani da appartamento.",
    salute: "Predisposti ad atrofia retinica progressiva, lussazione della rotula e allergie. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono sufficienti. Amano osservare da punti alti.",
    verdetto: "Il Tibetan Spaniel è un compagno intelligente e affettuoso per appartamenti."
  },
  'tibetan-terrier.html': {
    meta: "Il Tibetan Terrier è un antico cane tibetano portafortuna. Affettuoso, intelligente e versatile.",
    hero: "Il Tibetan Terrier è un antico cane tibetano, considerato portatore di fortuna e mai venduto, solo donato.",
    panoramica: "Il Tibetan Terrier non è un vero terrier ma era così chiamato per la taglia. Era il 'Santo Cane del Tibet', compagno dei monaci e portafortuna.",
    temperamento: "I Tibetan Terrier sono affettuosi, intelligenti e sensibili. Sono ottimi cani da famiglia. Possono essere riservati con gli estranei.",
    salute: "Predisposti a atrofia retinica progressiva, lussazione del cristallino, displasia dell'anca e cataratta. Aspettativa di vita 15-16 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Sono agili e atletici.",
    verdetto: "Il Tibetan Terrier è un compagno affettuoso e versatile per famiglie. Richiede toelettatura."
  },
  'toy-fox-terrier.html': {
    meta: "Il Toy Fox Terrier è un piccolo terrier americano vivace. Intelligente, coraggioso e pieno di personalità.",
    hero: "Il Toy Fox Terrier è un piccolo terrier americano, che combina l'eleganza del toy con lo spirito del terrier.",
    panoramica: "Il Toy Fox Terrier fu sviluppato negli Stati Uniti riducendo il Smooth Fox Terrier. Era usato nei circhi e come cane da fattoria per i topi.",
    temperamento: "I TFT sono vivaci, intelligenti e coraggiosi. Hanno la personalità terrier in un corpo toy. Sono affettuosi e leali.",
    salute: "Predisposti a lussazione della rotula, malattia di Legg-Calvé-Perthes e allergie. Aspettativa di vita 13-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Hanno energia da terrier.",
    verdetto: "Il Toy Fox Terrier è un compagno vivace per chi cerca un terrier in formato compatto."
  },
  'treeing-walker-coonhound.html': {
    meta: "Il Treeing Walker Coonhound è un segugio americano veloce e resistente. Amichevole, intelligente e vocale.",
    hero: "Il Treeing Walker Coonhound è un segugio americano veloce, il 'popolo scelta' tra i coonhound.",
    panoramica: "Il Treeing Walker Coonhound discende dai Walker Foxhound. È chiamato 'treeing' perché costringe la preda a salire sugli alberi e la tiene lì abbaiando.",
    temperamento: "I Treeing Walker sono amichevoli, intelligenti e socievoli. Sono ottimi con bambini e altri cani. Sono molto vocali.",
    salute: "Predisposti a displasia dell'anca, infezioni alle orecchie e poliradiculoneurite. Aspettativa di vita 12-13 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di molto spazio e attività quotidiana. Amano seguire tracce.",
    verdetto: "Il Treeing Walker Coonhound è un compagno amichevole per case rurali. Richiede spazio e tolleranza per l'abbaio."
  },
  'welsh-springer-spaniel.html': {
    meta: "Il Welsh Springer Spaniel è un cane da caccia gallese allegro. Affettuoso, leale e versatile.",
    hero: "Il Welsh Springer Spaniel è un cane da caccia gallese, con un distintivo mantello rosso e bianco.",
    panoramica: "Il Welsh Springer Spaniel è una razza antica, raffigurata nell'arte medievale. È il fratello maggiore del Cocker e più antico dell'English Springer.",
    temperamento: "I Welsh Springer sono affettuosi, leali e allegri. Sono ottimi cani da famiglia e versatili sul campo. Possono essere riservati con gli estranei.",
    salute: "Predisposti a displasia dell'anca, problemi oculari, epilessia e allergie. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e gioco sono importanti. Amano l'acqua.",
    verdetto: "Il Welsh Springer è un compagno leale e versatile per famiglie attive."
  },
  'welsh-terrier.html': {
    meta: "Il Welsh Terrier è un terrier gallese vivace e amichevole. Intelligente, coraggioso e con un bel mantello nero focato.",
    hero: "Il Welsh Terrier è un terrier gallese vivace, una delle razze terrier più antiche.",
    panoramica: "Il Welsh Terrier è una delle razze terrier più antiche, sviluppata in Galles per la caccia a volpi, tassi e lontre. È simile all'Airedale ma più piccolo.",
    temperamento: "I Welsh Terrier sono vivaci, amichevoli e intelligenti. Sono meno aggressivi di alcuni terrier. Sono ottimi cani da famiglia.",
    salute: "Predisposti a problemi oculari, epilessia e allergie. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e gioco sono importanti. Hanno energia da terrier.",
    verdetto: "Il Welsh Terrier è un terrier amichevole e adattabile per famiglie. Richiede stripping."
  },
  'white-swiss-shepherd.html': {
    meta: "Il Pastore Svizzero Bianco è un elegante cane da pastore bianco. Gentile, intelligente e devoto.",
    hero: "Il Pastore Svizzero Bianco è un elegante cane da pastore, la versione bianca del Pastore Tedesco.",
    panoramica: "Il Pastore Svizzero Bianco discende dai Pastori Tedeschi bianchi, che erano discriminati in Germania. La Svizzera li ha preservati come razza separata.",
    temperamento: "I Pastori Svizzeri Bianchi sono gentili, intelligenti e devoti. Sono meno intensi dei Pastori Tedeschi. Sono ottimi cani da famiglia.",
    salute: "Predisposti a displasia dell'anca e del gomito, mielopatia degenerativa e allergie. Aspettativa di vita 12 anni.",
    esercizio: "Esigenze di esercizio elevate. Passeggiate quotidiane e attività mentale sono importanti. Sono versatili.",
    verdetto: "Il Pastore Svizzero Bianco è un compagno elegante e devoto per famiglie attive."
  },
  'wire-fox-terrier.html': {
    meta: "Il Fox Terrier a Pelo Ruvido è un terrier classico con un mantello distintivo. Vivace, coraggioso e pieno di carattere.",
    hero: "Il Fox Terrier a Pelo Ruvido è un terrier classico, il cane più premiato a Westminster.",
    panoramica: "Il Fox Terrier a Pelo Ruvido fu sviluppato separatamente dal Pelo Liscio, nonostante la somiglianza. Ha vinto più Best in Show a Westminster di qualsiasi altra razza.",
    temperamento: "I Wire Fox Terrier sono vivaci, coraggiosi e intelligenti. Hanno molta energia e personalità. Possono essere testardi.",
    salute: "Predisposti a sordità, lussazione della rotula e miopatia. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica quotidiana. Sono atleti naturali.",
    verdetto: "Il Wire Fox Terrier è un compagno energico per proprietari attivi. Richiede stripping."
  },
  'wirehaired-pointing-griffon.html': {
    meta: "Il Griffone a Pelo Duro è un versatile cane da caccia con un mantello ruvido. Intelligente, affettuoso e instancabile.",
    hero: "Il Griffone a Pelo Duro è un versatile cane da caccia, chiamato 'il gundog supremo'.",
    panoramica: "Il Griffone a Pelo Duro fu creato in Olanda e Francia da Eduard Korthals. È considerato uno dei cani da caccia più versatili.",
    temperamento: "I Griffone sono intelligenti, affettuosi e desiderosi di piacere. Sono ottimi cani da famiglia e compagni di caccia. Sono socievoli.",
    salute: "Predisposti a displasia dell'anca, problemi oculari e ipotiroidismo. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica quotidiana. Amano cacciare e nuotare.",
    verdetto: "Il Griffone a Pelo Duro è un compagno versatile per cacciatori e famiglie attive."
  },
  'wirehaired-vizsla.html': {
    meta: "Il Vizsla a Pelo Duro è un cane da caccia ungherese robusto. Affettuoso, versatile e con un mantello protettivo.",
    hero: "Il Vizsla a Pelo Duro è la versione robusta del Vizsla, con un mantello che protegge da rovi e freddo.",
    panoramica: "Il Vizsla a Pelo Duro fu sviluppato in Ungheria negli anni '30 incrociando Vizsla con German Wirehaired Pointer per creare un cane più robusto.",
    temperamento: "I Wirehaired Vizsla sono affettuosi, versatili e leali. Sono ottimi cani da famiglia e compagni di caccia. Sono meno intensi del Vizsla a pelo corto.",
    salute: "Predisposti a displasia dell'anca, problemi oculari e allergie. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica quotidiana. Amano cacciare.",
    verdetto: "Il Wirehaired Vizsla è un compagno versatile per famiglie attive e cacciatori."
  },
  'xoloitzcuintli.html': {
    meta: "Lo Xoloitzcuintli è un antico cane messicano senza pelo. Calmo, affettuoso e con una storia affascinante.",
    hero: "Lo Xoloitzcuintli è un antico cane messicano, sacro agli Aztechi e ai Maya.",
    panoramica: "Lo Xoloitzcuintli (Xolo) ha oltre 3000 anni di storia. Era sacro per gli Aztechi, che credevano guidasse le anime nell'aldilà. Disponibile con e senza pelo, in tre taglie.",
    temperamento: "Gli Xolo sono calmi, affettuosi e vigili. Sono riservati con gli estranei ma devoti alla famiglia. Sono intelligenti e sensibili.",
    salute: "Predisposti a problemi cutanei (gli Hairless necessitano protezione), problemi dentali e allergie. Aspettativa di vita 13-18 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono sufficienti. Proteggere dal sole e dal freddo.",
    verdetto: "Lo Xolo è un compagno antico e affascinante per chi può curare la sua pelle speciale."
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
