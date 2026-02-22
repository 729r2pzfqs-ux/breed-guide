#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const breedsDir = path.join(__dirname, 'it/breeds');

const breedTranslations = {
  'bull-terrier.html': {
    meta: "Il Bull Terrier è un cane unico con la testa a forma di uovo. Giocherellone, coraggioso e pieno di personalità.",
    hero: "Il Bull Terrier è un cane unico e distintivo, noto per la sua testa caratteristica e la personalità esuberante.",
    panoramica: "Il Bull Terrier è stato sviluppato in Inghilterra nel XIX secolo incrociando Bulldog e terrier. La sua distintiva testa 'a uovo' è diventata il marchio della razza.",
    temperamento: "I Bull Terrier sono giocherelloni, coraggiosi e affettuosi. Sono pieni di energia e personalità. Possono essere testardi ma sono devoti alla famiglia.",
    salute: "Predisposti a sordità (nei bianchi), problemi cardiaci, lussazione della rotula e allergie cutanee. Aspettativa di vita 11-13 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica quotidiana e stimolazione mentale. Amano giocare.",
    verdetto: "Il Bull Terrier è un compagno energico e divertente per proprietari attivi. Richiede socializzazione precoce e addestramento costante."
  },
  'cairn-terrier.html': {
    meta: "Il Cairn Terrier è un piccolo terrier scozzese robusto e vivace. Coraggioso, intelligente e pieno di carattere.",
    hero: "Il Cairn Terrier è un piccolo terrier scozzese robusto, reso famoso da Toto ne 'Il Mago di Oz'.",
    panoramica: "Il Cairn Terrier è una delle razze scozzesi più antiche, usata per cacciare volpi e tassi tra i 'cairn' (cumuli di pietre). È famoso per aver interpretato Toto.",
    temperamento: "I Cairn sono coraggiosi, vivaci e indipendenti. Hanno la tipica personalità terrier: audaci e un po' testardi. Sono affettuosi con la famiglia.",
    salute: "Predisposti a lussazione della rotula, malattia di Legg-Calvé-Perthes, allergie e problemi oculari. Aspettativa di vita 13-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Hanno molta energia per la loro taglia.",
    verdetto: "Il Cairn Terrier è un compagno vivace e robusto, adatto a diverse situazioni. Richiede socializzazione con altri animali."
  },
  'canaan-dog.html': {
    meta: "Il Canaan Dog è un'antica razza israeliana, vigile e versatile. Intelligente, leale e naturalmente protettivo.",
    hero: "Il Canaan Dog è un'antica razza israeliana, uno dei cani più primitivi ancora esistenti.",
    panoramica: "Il Canaan Dog è l'antico cane dei pastori israeliani, sopravvissuto allo stato selvatico per secoli. È stato redomesticato nel XX secolo per lavorare come cane da guardia e guida.",
    temperamento: "I Canaan sono intelligenti, vigili e leali. Sono riservati con gli estranei ma devoti alla famiglia. Hanno istinti primitivi forti.",
    salute: "Generalmente molto sani grazie alla selezione naturale. Predisposti a displasia dell'anca e ipotiroidismo. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Necessitano di stimolazione mentale.",
    verdetto: "Il Canaan Dog è un compagno primitivo e affascinante per proprietari esperti. Richiede socializzazione precoce e leadership."
  },
  'cardigan-welsh-corgi.html': {
    meta: "Il Cardigan Welsh Corgi è un antico cane da pastore gallese con la coda. Intelligente, affettuoso e versatile.",
    hero: "Il Cardigan Welsh Corgi è l'antico cane da pastore gallese, distinguibile dal cugino Pembroke per la lunga coda.",
    panoramica: "Il Cardigan Welsh Corgi è una delle razze britanniche più antiche, portato in Galles dai Celti circa 3000 anni fa. A differenza del Pembroke, ha la coda lunga.",
    temperamento: "I Cardigan sono intelligenti, affettuosi e un po' riservati. Sono meno estroversi dei Pembroke ma altrettanto leali. Ottimi cani da guardia.",
    salute: "Predisposti a problemi alla schiena (IVDD), displasia dell'anca, atrofia retinica progressiva e problemi oculari. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Mantenere il peso forma è essenziale.",
    verdetto: "Il Cardigan Welsh Corgi è un compagno intelligente e affettuoso per famiglie. Richiede attenzione al peso e alla schiena."
  },
  'cesky-terrier.html': {
    meta: "Il Cesky Terrier è un terrier ceco elegante e calmo. Dolce, paziente e adatto alla vita familiare.",
    hero: "Il Cesky Terrier è un terrier ceco elegante, più calmo e docile rispetto ad altri terrier.",
    panoramica: "Il Cesky Terrier è stato creato in Cecoslovacchia nel 1948 incrociando Sealyham e Scottish Terrier. È una delle razze più rare al mondo.",
    temperamento: "I Cesky sono calmi, pazienti e affettuosi. Sono meno aggressivi di altri terrier. Ottimi con bambini e altri animali.",
    salute: "Predisposti a sindrome di Scotty Cramp, lussazione della rotula e problemi cardiaci. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono sufficienti. Si adattano bene a vari stili di vita.",
    verdetto: "Il Cesky Terrier è un compagno calmo e affettuoso, ideale per famiglie. Richiede toelettatura regolare."
  },
  'chesapeake-bay-retriever.html': {
    meta: "Il Chesapeake Bay Retriever è un cane da riporto americano resistente, eccellente in acque fredde. Forte, leale e protettivo.",
    hero: "Il Chesapeake Bay Retriever è un cane da riporto americano resistente, sviluppato per cacciare nelle gelide acque della baia di Chesapeake.",
    panoramica: "Il Chesapeake Bay Retriever è l'unico retriever sviluppato negli Stati Uniti. È stato creato per recuperare anatre nelle acque gelide della baia di Chesapeake.",
    temperamento: "I Chessie sono forti, leali e protettivi. Sono più indipendenti degli altri retriever. Possono essere riservati con gli estranei.",
    salute: "Predisposti a displasia dell'anca, atrofia retinica progressiva, torsione gastrica e mielopatia degenerativa. Aspettativa di vita 10-13 anni.",
    esercizio: "Esigenze di esercizio elevate. Amano l'acqua e la caccia. Necessitano di attività fisica quotidiana.",
    verdetto: "Il Chesapeake Bay Retriever è ideale per cacciatori e famiglie attive. Richiede socializzazione e un proprietario con esperienza."
  },
  'chinese-crested.html': {
    meta: "Il Chinese Crested è un cane elegante disponibile con e senza pelo. Affettuoso, giocherellone e unico.",
    hero: "Il Chinese Crested è un cane elegante e distintivo, disponibile nelle varietà 'Hairless' e 'Powderpuff'.",
    panoramica: "Il Chinese Crested, nonostante il nome, probabilmente non è originario della Cina. La varietà senza pelo è dovuta a un gene dominante incompleto.",
    temperamento: "I Chinese Crested sono affettuosi, giocherelloni e allegri. Amano stare con le persone e soffrono se lasciati soli. Sono ottimi cani da terapia.",
    salute: "Predisposti a problemi dentali (soprattutto gli Hairless), lussazione della rotula, malattia di Legg-Calvé-Perthes e allergie. Aspettativa di vita 13-18 anni.",
    esercizio: "Esigenze di esercizio basse-moderate. Brevi passeggiate e gioco sono sufficienti. Proteggere dal sole e dal freddo.",
    verdetto: "Il Chinese Crested è un compagno affettuoso e unico. Richiede protezione cutanea e cure dentali regolari."
  },
  'chinook.html': {
    meta: "Il Chinook è un raro cane da slitta americano, dolce e potente. Devoto alla famiglia e lavoratore instancabile.",
    hero: "Il Chinook è un raro cane da slitta americano, noto per la sua natura dolce e la forza di traino.",
    panoramica: "Il Chinook è stato sviluppato nel New Hampshire da Arthur Walden per il traino delle slitte. È il cane di stato del New Hampshire e una delle razze più rare.",
    temperamento: "I Chinook sono dolci, pazienti e devoti. Sono eccellenti con i bambini e altri animali. Amano lavorare e stare con la famiglia.",
    salute: "Predisposti a displasia dell'anca, convulsioni, allergie e criptorchidismo. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Amano trainare e le attività all'aperto. Necessitano di attività regolare.",
    verdetto: "Il Chinook è un compagno dolce e versatile per famiglie attive. Richiede esercizio regolare e compagnia."
  },
  'cirneco-delletna.html': {
    meta: "Il Cirneco dell'Etna è un antico segugio siciliano, elegante e agile. Indipendente, affettuoso e adattabile.",
    hero: "Il Cirneco dell'Etna è un antico segugio siciliano, sopravvissuto ai pendii dell'Etna per millenni.",
    panoramica: "Il Cirneco dell'Etna è una razza primitiva siciliana, cacciatore di conigli da oltre 2000 anni. Il suo nome deriva dal latino 'canis cyrenaicus'.",
    temperamento: "I Cirneco sono indipendenti, affettuosi e giocherelloni. Sono meno riservati di altri levrieri. Amano la compagnia della famiglia.",
    salute: "Generalmente molto sani. Predisposti a sensibilità al freddo e lesioni muscolari. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Amano correre e cacciare. Necessitano di un'area recintata sicura.",
    verdetto: "Il Cirneco dell'Etna è un compagno elegante e affettuoso per famiglie attive. Richiede protezione dal freddo."
  },
  'clumber-spaniel.html': {
    meta: "Il Clumber Spaniel è lo spaniel più grande e tranquillo. Dolce, leale e perfetto per la caccia lenta.",
    hero: "Il Clumber Spaniel è lo spaniel più grande, noto per la sua natura dolce e il passo deliberato.",
    panoramica: "Il Clumber Spaniel prende il nome da Clumber Park in Inghilterra. Era il preferito della nobiltà britannica per la caccia ai fagiani.",
    temperamento: "I Clumber sono dolci, leali e rilassati. Sono più calmi degli altri spaniel. Sono affettuosi con tutti ma possono sbavare.",
    salute: "Predisposti a displasia dell'anca, problemi alla schiena, entropion e torsione gastrica. Tendenza all'obesità. Aspettativa di vita 10-12 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane sono importanti. Non tollerano bene il caldo.",
    verdetto: "Il Clumber Spaniel è un compagno tranquillo e affettuoso per famiglie. Richiede attenzione al peso e tolleranza per la bava."
  },
  'coton-de-tulear.html': {
    meta: "Il Coton de Tuléar è un piccolo cane malgascio con un soffice mantello bianco. Allegro, affettuoso e giocherellone.",
    hero: "Il Coton de Tuléar è un piccolo cane malgascio, noto per il suo soffice mantello simile al cotone.",
    panoramica: "Il Coton de Tuléar è originario del Madagascar, dove era il cane reale dei nobili del Merina. Il nome deriva dalla città di Tuléar e dalla texture del mantello.",
    temperamento: "I Coton sono allegri, affettuosi e giocherelloni. Adorano le persone e sono ottimi cani da famiglia. Possono essere un po' vocali.",
    salute: "Predisposti a lussazione della rotula, displasia dell'anca, problemi oculari e allergie. Aspettativa di vita 15-19 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Si adattano bene alla vita in appartamento.",
    verdetto: "Il Coton de Tuléar è un compagno allegro e affettuoso, perfetto per famiglie. Richiede toelettatura regolare."
  },
  'curly-coated-retriever.html': {
    meta: "Il Curly-Coated Retriever è il più antico dei retriever, con un mantello riccio distintivo. Elegante, intelligente e indipendente.",
    hero: "Il Curly-Coated Retriever è il più antico dei retriever, distintivo per il suo mantello a riccioli stretti.",
    panoramica: "Il Curly-Coated Retriever è uno dei primi retriever sviluppati, probabilmente incrociando Poodle, Irish Water Spaniel e altri retriever.",
    temperamento: "I Curly sono intelligenti, eleganti e un po' riservati. Sono più indipendenti degli altri retriever. Sono affettuosi con la famiglia.",
    salute: "Predisposti a displasia dell'anca, problemi oculari, epilessia e alopecia. Aspettativa di vita 10-12 anni.",
    esercizio: "Esigenze di esercizio elevate. Amano nuotare e cacciare. Necessitano di attività fisica quotidiana.",
    verdetto: "Il Curly-Coated Retriever è un compagno elegante e versatile per famiglie attive. Richiede socializzazione."
  },
  'dandie-dinmont-terrier.html': {
    meta: "Il Dandie Dinmont Terrier è un terrier scozzese unico con un corpo lungo e una testa distintiva. Indipendente, coraggioso e affettuoso.",
    hero: "Il Dandie Dinmont Terrier è un terrier scozzese unico, con una silhouette inconfondibile e un carattere nobile.",
    panoramica: "Il Dandie Dinmont è l'unico cane che prende il nome da un personaggio letterario, dal romanzo 'Guy Mannering' di Walter Scott. Era usato per cacciare tassi e lontre.",
    temperamento: "I Dandie sono indipendenti, coraggiosi e affettuosi. Sono più calmi di altri terrier ma mantengono lo spirito combattivo. Sono devoti alla famiglia.",
    salute: "Predisposti a problemi alla schiena (IVDD), glaucoma e problemi cutanei. Aspettativa di vita 11-13 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono sufficienti. Evitare salti per proteggere la schiena.",
    verdetto: "Il Dandie Dinmont Terrier è un compagno unico e affettuoso per chi cerca un terrier più tranquillo."
  },
  'deutscher-wachtelhund.html': {
    meta: "Il Deutscher Wachtelhund è un versatile cane da caccia tedesco. Energico, intelligente e amichevole.",
    hero: "Il Deutscher Wachtelhund è un versatile cane da caccia tedesco, eccellente per la caccia in acqua e su terra.",
    panoramica: "Il Deutscher Wachtelhund, o Quaglia Tedesca, è stato sviluppato in Germania per la caccia versatile. È raro fuori dalla Germania.",
    temperamento: "I Wachtelhund sono energici, intelligenti e amichevoli. Sono versatili cacciatori e ottimi compagni. Sono socievoli con persone e altri cani.",
    salute: "Generalmente sani ma predisposti a displasia dell'anca e problemi alle orecchie. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica quotidiana e stimolazione mentale. Amano l'acqua.",
    verdetto: "Il Deutscher Wachtelhund è ideale per cacciatori e famiglie attive. Richiede esercizio regolare."
  },
  'dogo-argentino.html': {
    meta: "Il Dogo Argentino è un cane da caccia potente e atletico. Coraggioso, leale e protettivo.",
    hero: "Il Dogo Argentino è un cane da caccia argentino potente, sviluppato per la caccia grossa.",
    panoramica: "Il Dogo Argentino è stato creato in Argentina negli anni '20 per la caccia al puma e al cinghiale. È l'unica razza argentina riconosciuta.",
    temperamento: "I Dogo sono coraggiosi, leali e protettivi. Sono affettuosi con la famiglia ma necessitano di un proprietario esperto. Possono essere dominanti con altri cani.",
    salute: "Predisposti a sordità (nei bianchi), displasia dell'anca, ipotiroidismo e allergie cutanee. Aspettativa di vita 9-15 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica quotidiana e stimolazione mentale.",
    verdetto: "Il Dogo Argentino è un compagno leale per proprietari molto esperti. Richiede socializzazione precoce e addestramento costante."
  },
  'dogue-de-bordeaux.html': {
    meta: "Il Dogue de Bordeaux è un mastino francese potente con un'espressione distintiva. Calmo, leale e devoto.",
    hero: "Il Dogue de Bordeaux è un mastino francese potente, noto per la sua massiccia testa e l'espressione pensierosa.",
    panoramica: "Il Dogue de Bordeaux è una delle razze francesi più antiche, usata per la guardia, il traino e purtroppo i combattimenti. È famoso per il film 'Turner & Hooch'.",
    temperamento: "I Dogue sono calmi, leali e devoti. Sono affettuosi con la famiglia e protettivi. Possono essere diffidenti con gli estranei.",
    salute: "Predisposti a cardiomiopatia dilatativa, displasia dell'anca, torsione gastrica e problemi respiratori. Aspettativa di vita breve: 5-8 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane sono importanti. Non tollerano bene il caldo.",
    verdetto: "Il Dogue de Bordeaux è un guardiano devoto con una breve aspettativa di vita. Richiede tolleranza per la bava e attenzione alla salute."
  },
  'drentse-patrijshond.html': {
    meta: "Il Drentse Patrijshond è un versatile cane da caccia olandese. Amichevole, intelligente e devoto.",
    hero: "Il Drentse Patrijshond è un versatile cane da caccia olandese, noto per la sua natura amichevole e la versatilità sul campo.",
    panoramica: "Il Drentse Patrijshond è originario della provincia di Drenthe nei Paesi Bassi. È un cane da caccia versatile che eccelle sia sulla terra che in acqua.",
    temperamento: "I Drentse sono amichevoli, intelligenti e devoti. Sono ottimi cani da famiglia e compagni di caccia. Sono pazienti con i bambini.",
    salute: "Generalmente sani ma predisposti a displasia dell'anca e problemi oculari. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Necessitano di attività fisica quotidiana e stimolazione mentale.",
    verdetto: "Il Drentse Patrijshond è un compagno versatile per famiglie attive e cacciatori. Richiede esercizio regolare."
  },
  'dutch-shepherd.html': {
    meta: "Il Pastore Olandese è un cane da lavoro versatile e intelligente. Energico, leale e sempre pronto all'azione.",
    hero: "Il Pastore Olandese è un cane da lavoro versatile, noto per la sua intelligenza e il mantello tigrato distintivo.",
    panoramica: "Il Pastore Olandese era il cane da fattoria multiuso dei Paesi Bassi. È meno conosciuto dei cugini belgi e tedeschi ma altrettanto capace.",
    temperamento: "I Pastori Olandesi sono intelligenti, leali e energici. Sono versatili nel lavoro e affettuosi con la famiglia. Richiedono stimolazione costante.",
    salute: "Predisposti a displasia dell'anca, problemi oculari e allergie. Aspettativa di vita 11-14 anni.",
    esercizio: "Esigenze di esercizio molto elevate. Necessitano di lavoro fisico e mentale quotidiano. Eccellono negli sport cinofili.",
    verdetto: "Il Pastore Olandese è ideale per proprietari attivi che possono offrire lavoro e stimolazione. Non adatto a vita sedentaria."
  },
  'english-cocker-spaniel.html': {
    meta: "Il Cocker Spaniel Inglese è un cane da caccia allegro con un bel mantello fluente. Affettuoso, vivace e versatile.",
    hero: "Il Cocker Spaniel Inglese è un cane da caccia allegro e versatile, con un bellissimo mantello fluente.",
    panoramica: "Il Cocker Spaniel Inglese è la versione originale della razza, sviluppata in Inghilterra per la caccia alle beccacce (woodcock). È più alto e snello del cugino americano.",
    temperamento: "I Cocker Inglesi sono allegri, affettuosi e vivaci. Sono ottimi cani da famiglia e compagni di caccia. Adorano piacere.",
    salute: "Predisposti a problemi oculari, otiti croniche, displasia dell'anca e nefropatia familiare. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e gioco sono essenziali. Amano nuotare.",
    verdetto: "Il Cocker Spaniel Inglese è un compagno allegro e versatile per famiglie attive. Richiede toelettatura e cura delle orecchie."
  },
  'english-foxhound.html': {
    meta: "L'English Foxhound è un segugio elegante e resistente, sviluppato per la caccia alla volpe. Socievole, atletico e instancabile.",
    hero: "L'English Foxhound è un segugio elegante e resistente, l'aristocratico cacciatore di volpi inglese.",
    panoramica: "L'English Foxhound è stato sviluppato in Inghilterra nel XVI secolo per la caccia alla volpe a cavallo. È l'antenato dell'American Foxhound.",
    temperamento: "Gli English Foxhound sono socievoli, atletici e instancabili. Sono ottimi con altri cani ma necessitano di compagnia. Sono vocali.",
    salute: "Generalmente sani ma predisposti a displasia dell'anca, problemi renali e epilessia. Aspettativa di vita 10-13 anni.",
    esercizio: "Esigenze di esercizio molto elevate. Necessitano di molto spazio e attività quotidiana. Non adatti alla vita in appartamento.",
    verdetto: "L'English Foxhound è ideale per case rurali con molto spazio. Richiede compagnia canina e esercizio intenso."
  },
  'english-pointer.html': {
    meta: "Il Pointer Inglese è un cane da ferma elegante e atletico. Energico, amichevole e instancabile sul campo.",
    hero: "Il Pointer Inglese è un cane da ferma elegante e atletico, il re dei cani da caccia britannici.",
    panoramica: "Il Pointer Inglese è stato sviluppato nel XVII secolo per localizzare e 'puntare' la selvaggina prima che i cacciatori sparassero.",
    temperamento: "I Pointer sono energici, amichevoli e desiderosi di lavorare. Sono affettuosi con la famiglia e vanno d'accordo con altri cani.",
    salute: "Predisposti a displasia dell'anca, problemi oculari, epilessia e ipotiroidismo. Aspettativa di vita 12-17 anni.",
    esercizio: "Esigenze di esercizio molto elevate. Necessitano di almeno 2 ore di attività al giorno. Ideali per cacciatori.",
    verdetto: "Il Pointer Inglese è ideale per cacciatori e famiglie molto attive. Richiede enorme quantità di esercizio."
  },
  'english-setter.html': {
    meta: "Il Setter Inglese è un elegante cane da caccia con un bellissimo mantello maculato. Dolce, amichevole e atletico.",
    hero: "Il Setter Inglese è un elegante cane da caccia, noto per il suo bellissimo mantello belton e la natura dolce.",
    panoramica: "Il Setter Inglese è una delle razze da caccia più antiche, sviluppata oltre 400 anni fa. Il caratteristico mantello 'belton' può essere blu, arancio, limone o tricolore.",
    temperamento: "I Setter Inglesi sono dolci, amichevoli e affettuosi. Sono ottimi con bambini e altri animali. Possono essere un po' testardi.",
    salute: "Predisposti a displasia dell'anca e del gomito, sordità, ipotiroidismo e allergie. Aspettativa di vita 11-15 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica quotidiana. Amano correre e cacciare.",
    verdetto: "Il Setter Inglese è un compagno elegante e affettuoso per famiglie attive. Richiede esercizio e toelettatura regolare."
  },
  'english-springer-spaniel.html': {
    meta: "L'English Springer Spaniel è un cane da caccia energico e allegro. Amichevole, intelligente e sempre pronto all'azione.",
    hero: "L'English Springer Spaniel è un cane da caccia energico e allegro, eccellente sia sul campo che come compagno di famiglia.",
    panoramica: "L'English Springer Spaniel è così chiamato per il modo in cui 'fa saltare' (spring) la selvaggina. È uno degli spaniel da caccia più popolari.",
    temperamento: "Gli Springer sono energici, amichevoli e desiderosi di piacere. Sono ottimi cani da famiglia e compagni di caccia. Adorano l'acqua.",
    salute: "Predisposti a displasia dell'anca, problemi oculari, otiti e fosfofructochinasi. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di almeno un'ora di attività al giorno. Amano nuotare e riportare.",
    verdetto: "L'English Springer Spaniel è un compagno energico e affettuoso per famiglie attive. Richiede esercizio e cura delle orecchie."
  },
  'english-toy-spaniel.html': {
    meta: "L'English Toy Spaniel è un elegante cane da compagnia con un muso piatto. Dolce, tranquillo e affettuoso.",
    hero: "L'English Toy Spaniel è un elegante cane da compagnia, noto per la sua natura dolce e il portamento regale.",
    panoramica: "L'English Toy Spaniel, o King Charles Spaniel, era il preferito della nobiltà inglese. Non confonderlo con il Cavalier, che ha il muso più lungo.",
    temperamento: "Gli ETS sono dolci, tranquilli e affettuosi. Sono più calmi del Cavalier. Adorano stare sul divano con il proprietario.",
    salute: "Predisposti a problemi cardiaci (MVD), siringomielia, lussazione della rotula e problemi respiratori. Aspettativa di vita 10-12 anni.",
    esercizio: "Esigenze di esercizio basse. Brevi passeggiate e gioco sono sufficienti. Non tollerano bene il caldo.",
    verdetto: "L'English Toy Spaniel è un compagno tranquillo e affettuoso per chi cerca un cane rilassato. Attenzione ai problemi di salute."
  },
  'entlebucher-mountain-dog.html': {
    meta: "L'Entlebucher è il più piccolo dei bovari svizzeri. Energico, leale e sempre pronto a lavorare.",
    hero: "L'Entlebucher è il più piccolo dei quattro Bovari Svizzeri, compatto ma pieno di energia e determinazione.",
    panoramica: "L'Entlebucher Sennenhund prende il nome dalla valle di Entlebuch in Svizzera. È il più piccolo e raro dei bovari svizzeri.",
    temperamento: "Gli Entlebucher sono energici, leali e intelligenti. Sono ottimi cani da lavoro e compagni. Possono essere riservati con gli estranei.",
    salute: "Predisposti a displasia dell'anca, problemi oculari ed ectopia dell'uretere. Aspettativa di vita 11-15 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica e mentale quotidiana. Eccellono negli sport cinofili.",
    verdetto: "L'Entlebucher è un compagno energico e leale per famiglie attive. Richiede esercizio e stimolazione mentale."
  },
  'eurasier.html': {
    meta: "L'Eurasier è un cane tedesco equilibrato e affettuoso. Calmo, riservato e devoto alla famiglia.",
    hero: "L'Eurasier è un cane tedesco equilibrato, creato per essere il compagno di famiglia ideale.",
    panoramica: "L'Eurasier è stato sviluppato in Germania negli anni '60 incrociando Chow Chow, Wolfspitz e Samoiedo. L'obiettivo era creare un cane da famiglia equilibrato.",
    temperamento: "Gli Eurasier sono calmi, riservati e devoti. Sono affettuosi con la famiglia ma diffidenti con gli estranei. Non sono aggressivi.",
    salute: "Predisposti a displasia dell'anca, lussazione della rotula e ipotiroidismo. Aspettativa di vita 12-14 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Si adattano bene a vari stili di vita.",
    verdetto: "L'Eurasier è un compagno equilibrato e affettuoso per famiglie. Richiede socializzazione precoce."
  },
  'field-spaniel.html': {
    meta: "Il Field Spaniel è uno spaniel elegante e atletico. Dolce, sensibile e ottimo compagno di caccia.",
    hero: "Il Field Spaniel è uno spaniel elegante, più raro dei cugini Cocker e Springer ma altrettanto affettuoso.",
    panoramica: "Il Field Spaniel è stato sviluppato in Inghilterra nel XIX secolo. Quasi estinto a causa dell'allevamento estremo, oggi è più equilibrato ma resta raro.",
    temperamento: "I Field Spaniel sono dolci, sensibili e affettuosi. Sono più calmi degli Springer ma necessitano di compagnia. Possono essere un po' riservati.",
    salute: "Predisposti a displasia dell'anca, problemi oculari, otiti e ipotiroidismo. Aspettativa di vita 10-12 anni.",
    esercizio: "Esigenze di esercizio moderate-alte. Passeggiate quotidiane e gioco sono importanti. Amano nuotare.",
    verdetto: "Il Field Spaniel è un compagno elegante e affettuoso per famiglie. Richiede compagnia costante e toelettatura."
  },
  'finnish-lapphund.html': {
    meta: "Il Lapphund Finlandese è un cane spitz nordico dolce e amichevole. Intelligente, coraggioso e adattabile.",
    hero: "Il Lapphund Finlandese è un cane spitz nordico, sviluppato dai Sami per la conduzione delle renne.",
    panoramica: "Il Lapphund Finlandese era usato dai Sami della Lapponia per la conduzione delle renne. È un cane versatile adatto sia al lavoro che alla vita familiare.",
    temperamento: "I Lapphund sono amichevoli, intelligenti e coraggiosi. Sono ottimi cani da famiglia e vanno d'accordo con bambini e altri animali.",
    salute: "Predisposti a atrofia retinica progressiva, cataratta e displasia dell'anca. Aspettativa di vita 12-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Tollerano bene il freddo.",
    verdetto: "Il Lapphund Finlandese è un compagno amichevole e adattabile per famiglie. Richiede toelettatura regolare."
  },
  'finnish-spitz.html': {
    meta: "Il Finnish Spitz è il cane nazionale della Finlandia, noto per il suo abbaiare melodioso. Vivace, intelligente e indipendente.",
    hero: "Il Finnish Spitz è il cane nazionale della Finlandia, noto per il suo caratteristico abbaiare durante la caccia.",
    panoramica: "Il Finnish Spitz è usato in Finlandia per la caccia alla selvaggina da piuma. Abbaia per segnalare la posizione della preda, fino a 160 volte al minuto.",
    temperamento: "I Finnish Spitz sono vivaci, intelligenti e indipendenti. Sono affettuosi con la famiglia ma possono essere riservati con gli estranei. Sono vocali.",
    salute: "Generalmente sani ma predisposti a displasia dell'anca, lussazione della rotula e epilessia. Aspettativa di vita 13-15 anni.",
    esercizio: "Esigenze di esercizio moderate. Passeggiate quotidiane e gioco sono importanti. Amano le attività all'aperto.",
    verdetto: "Il Finnish Spitz è un compagno vivace e indipendente. Richiede tolleranza per la vocalizzazione e pazienza nell'addestramento."
  },
  'flat-coated-retriever.html': {
    meta: "Il Flat-Coated Retriever è il 'Peter Pan' dei retriever. Giocherellone, ottimista e eternamente giovane nel cuore.",
    hero: "Il Flat-Coated Retriever è il 'Peter Pan' dei retriever, noto per mantenere la sua giocosità da cucciolo per tutta la vita.",
    panoramica: "Il Flat-Coated Retriever era il retriever più popolare prima che Golden e Labrador lo superassero. È noto per la sua personalità esuberante.",
    temperamento: "I Flat-Coated sono giocherelloni, ottimisti e affettuosi. Rimangono cuccioli nel cuore tutta la vita. Sono amichevoli con tutti.",
    salute: "Purtroppo predisposti a tumori (sarcoma, linfoma), displasia dell'anca e torsione gastrica. Aspettativa di vita 8-10 anni.",
    esercizio: "Esigenze di esercizio elevate. Necessitano di attività fisica quotidiana. Amano nuotare e riportare.",
    verdetto: "Il Flat-Coated Retriever è un compagno gioioso per famiglie attive. L'alta incidenza di tumori richiede considerazione."
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
