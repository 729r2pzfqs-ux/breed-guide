#!/usr/bin/env python3
"""Fix JSON-LD schema translations in Dutch breed pages."""

import os
import re
import json
from pathlib import Path

NL_BREEDS_DIR = Path(__file__).parent / "nl" / "breeds"

# Translation mappings for common English phrases to Dutch
TRANSLATIONS = [
    # Full sentence patterns - Health section
    (r"Generally healthy with a lifespan of (\d+-?\d*) years\. Common concerns include hip dysplasia and bloat and skin conditions\. Regular veterinary checkups and preventive care are important\. Maintaining a healthy weight helps prevent many health issues\.",
     r"Over het algemeen gezond met een levensverwachting van \1 jaar. Veelvoorkomende aandoeningen zijn heupdysplasie, opgeblazen maag en huidaandoeningen. Regelmatige veterinaire controles en preventieve zorg zijn belangrijk. Een gezond gewicht helpt veel gezondheidsproblemen te voorkomen."),
    (r"Generally healthy with a lifespan of (\d+-?\d*) years\. Common concerns include hip dysplasia and bloat\. Regular veterinary checkups and preventive care are important\. Maintaining a healthy weight helps prevent many health issues\.",
     r"Over het algemeen gezond met een levensverwachting van \1 jaar. Veelvoorkomende aandoeningen zijn heupdysplasie en opgeblazen maag. Regelmatige veterinaire controles en preventieve zorg zijn belangrijk. Een gezond gewicht helpt veel gezondheidsproblemen te voorkomen."),
    (r"Generally healthy with a lifespan of (\d+-?\d*) years\. Common concerns include joint problems and skin conditions\. Regular veterinary checkups and preventive care are important\. Maintaining a healthy weight helps prevent many health issues\.",
     r"Over het algemeen gezond met een levensverwachting van \1 jaar. Veelvoorkomende aandoeningen zijn gewrichtsproblemen en huidaandoeningen. Regelmatige veterinaire controles en preventieve zorg zijn belangrijk. Een gezond gewicht helpt veel gezondheidsproblemen te voorkomen."),
    (r"Generally healthy with a lifespan of (\d+-?\d*) years\. Common concerns include joint problems\. Regular veterinary checkups and preventive care are important\. Maintaining a healthy weight helps prevent many health issues\.",
     r"Over het algemeen gezond met een levensverwachting van \1 jaar. Veelvoorkomende aandoeningen zijn gewrichtsproblemen. Regelmatige veterinaire controles en preventieve zorg zijn belangrijk. Een gezond gewicht helpt veel gezondheidsproblemen te voorkomen."),
    (r"Generally healthy with a lifespan of (\d+-?\d*) years\. Common concerns include patellar luxation and dental issues and skin conditions\. Regular veterinary checkups and preventive care are important\. Maintaining a healthy weight helps prevent many health issues\.",
     r"Over het algemeen gezond met een levensverwachting van \1 jaar. Veelvoorkomende aandoeningen zijn patellaluxatie, gebitsklachten en huidaandoeningen. Regelmatige veterinaire controles en preventieve zorg zijn belangrijk. Een gezond gewicht helpt veel gezondheidsproblemen te voorkomen."),
    (r"Generally healthy with a lifespan of (\d+-?\d*) years\. Common concerns include patellar luxation and dental issues\. Regular veterinary checkups and preventive care are important\. Maintaining a healthy weight helps prevent many health issues\.",
     r"Over het algemeen gezond met een levensverwachting van \1 jaar. Veelvoorkomende aandoeningen zijn patellaluxatie en gebitsklachten. Regelmatige veterinaire controles en preventieve zorg zijn belangrijk. Een gezond gewicht helpt veel gezondheidsproblemen te voorkomen."),
    (r"Generally healthy but prone to hip dysplasia, cataracts, and hypothyroidism\. Their deep chest makes them susceptible to bloat\. Regular eye exams are recommended\. Life expectancy is (\d+-?\d*) years with proper care\.",
     r"Over het algemeen gezond, maar vatbaar voor heupdysplasie, staar en hypothyreoïdie. Hun diepe borst maakt hen vatbaar voor opgeblazen maag. Regelmatige oogonderzoeken worden aanbevolen. De levensverwachting is \1 jaar bij goede zorg."),

    # Exercise section full sentences
    (r"High energy ras requiring vigorous daily exercise—at least an hour of activity\. They thrive with actieve gezinnenes who enjoy outdoor activities\. Mental stimulation through training and puzzle toys is equally important\. Without adequate exercise, they may develop behavioral issues\.",
     "Hoogenergetisch ras dat intensieve dagelijkse beweging nodig heeft—minimaal een uur activiteit. Ze gedijen goed bij actieve gezinnen die van buitenactiviteiten houden. Mentale stimulatie door training en puzzelspeelgoed is even belangrijk. Zonder voldoende beweging kunnen ze gedragsproblemen ontwikkelen."),
    (r"High energy requiring vigorous daily exercise—at least an hour of activity\. They excel at swimming, hiking, and hond sports\. Mental challenges are equally important; they thrive with jobs to do\. Without adequate exercise, they may become destructive\.",
     "Hoge energie die dagelijks intensieve beweging vereist—minimaal een uur activiteit. Ze blinken uit in zwemmen, wandelen en hondensporten. Mentale uitdagingen zijn even belangrijk; ze gedijen het beste met taken om te doen. Zonder voldoende beweging kunnen ze destructief worden."),
    (r"High exercise needs—at least 2 hours daily\. They excel at hiking, backpacking, sledding, and weight pulling\. Without adequate exercise, they can become destructive\. They love cold weather and may struggle in hot climates\.",
     "Hoge bewegingsbehoefte—minimaal 2 uur per dag. Ze blinken uit in wandelen, trektochten, sleeën en gewichtstrekken. Zonder voldoende beweging kunnen ze destructief worden. Ze houden van koud weer en kunnen moeite hebben in warme klimaten."),

    # Grooming section patterns
    (r"Heavy shedders, especially twice a year during 'coat blow' season\. Regular brushing \(2-3 times per week, daily during shedding season\) is essential\. They're relatively clean honds and typically don't have a strong odor\.",
     "Verharen veel, vooral twee keer per jaar tijdens de rui. Regelmatig borstelen (2-3 keer per week, dagelijks tijdens de rui) is essentieel. Ze zijn relatief schone honden en hebben meestal geen sterke geur."),
    (r"Heavy shedders requiring regular brushing \(daily during shedding season\)\. Their feathered coat needs attention to prevent matting\.",
     "Verharen veel en vereisen regelmatig borstelen (dagelijks tijdens de rui). Hun gevederde vacht heeft aandacht nodig om klitten te voorkomen."),
    (r"Weekly brushing keeps coat healthy\. They shed heavily, especially during seasonal changes\. Regular nail trimming and ear cleaning needed\.",
     "Wekelijks borstelen houdt de vacht gezond. Ze verharen veel, vooral tijdens seizoenswisselingen. Regelmatig nagels knippen en oren schoonmaken is nodig."),
    (r"Requires regular grooming appropriate for their rough, harsh, wiry coat\.",
     "Vereist regelmatige verzorging passend bij hun ruwe, harde, draadachtige vacht."),
    (r"Requires regular grooming appropriate for their short, hard, beschermend coat\.",
     "Vereist regelmatige verzorging passend bij hun korte, harde, beschermende vacht."),
    (r"Requires regular grooming appropriate for their medium-length, hard coat\.",
     "Vereist regelmatige verzorging passend bij hun halflanghaar, harde vacht."),
    (r"Requires regular grooming appropriate for their hairless \(or coated variety\) coat\.",
     "Vereist regelmatige verzorging passend bij hun haarloze (of behaarde variëteit) huid."),
    (r"Requires regular grooming appropriate for their wavy or curly double coat coat\.",
     "Vereist regelmatige verzorging passend bij hun golvende of krullende dubbele vacht."),
    (r"Requires regular grooming appropriate for their double coat, short coat\.",
     "Vereist regelmatige verzorging passend bij hun dubbele, korte vacht."),
    (r"Requires regular grooming appropriate for their harsh, straight, dense coat\.",
     "Vereist regelmatige verzorging passend bij hun harde, rechte, dichte vacht."),
    (r"Requires regular grooming appropriate for their short, fine coat\.",
     "Vereist regelmatige verzorging passend bij hun korte, fijne vacht."),
    (r"Requires regular grooming appropriate for their long, woolly, curly coat\.",
     "Vereist regelmatige verzorging passend bij hun lange, wollige, krullende vacht."),
    (r"Requires regular grooming appropriate for their dense double coat coat\.",
     "Vereist regelmatige verzorging passend bij hun dichte dubbele vacht."),
    (r"Requires regular grooming appropriate for their",
     "Vereist regelmatige verzorging passend bij hun"),
    (r"dense double vacht with ruff vacht", "dichte dubbele vacht met kraag"),
    (r"fine, silky with feathering vacht", "fijne, zijdeachtige vacht met bevedering"),
    (r"long, dense, with feathering vacht", "lange, dichte vacht met bevedering"),
    (r"silky, medium-length with feathering vacht", "zijdeachtige, halflange vacht met bevedering"),
    (r"with ruff", "met kraag"),
    (r"with feathering", "met bevedering"),

    # Additional grooming patterns
    (r"Easy to groom\. Weekly brushing\. Moderate shedding with heavier periods twice a year\.",
     "Makkelijk te verzorgen. Wekelijks borstelen. Matige verharing met zwaardere periodes twee keer per jaar."),
    (r"Easy to groom—weekly brushing en regular facial fold cleaning\. Keep wrinkles dry to prevent infections\.",
     "Makkelijk te verzorgen—wekelijks borstelen en regelmatig plooien van het gezicht schoonmaken. Houd rimpels droog om infecties te voorkomen."),
    (r"Easy to maintain\. Weekly brushing en occasional baths\. Regular ear cleaning is important due to their floppy ears\.",
     "Makkelijk te onderhouden. Wekelijks borstelen en af en toe in bad. Regelmatige oorverzorging is belangrijk vanwege hun hangende oren."),
    (r"Heavy shedders—brush several times a week\. They 'blow' their vacht twice a year when daily brushing is needed\. Regular nail, ear, en dental care\.",
     "Verharen veel—meerdere keren per week borstelen. Ze verharen sterk twee keer per jaar wanneer dagelijks borstelen nodig is. Regelmatige nagel-, oor- en tandverzorging."),
    (r"Verharen veel en vereisen regelmatig borstelen\. They 'blow' their vacht seasonally\. Weekly brushing minimum, daily during shedding\.",
     "Verharen veel en vereisen regelmatig borstelen. Ze verharen sterk seizoensgebonden. Minimaal wekelijks borstelen, dagelijks tijdens de rui."),
    (r"Very easy to groom\. Weekly brushing en occasional baths\. Low maintenance vacht\.",
     "Zeer makkelijk te verzorgen. Wekelijks borstelen en af en toe in bad. Onderhoudsvriendelijke vacht."),
    (r"Weekly brushing\. Daily wrinkle cleaning to prevent infections\. Keep facial folds dry en clean\.",
     "Wekelijks borstelen. Dagelijks rimpels schoonmaken om infecties te voorkomen. Houd de plooien in het gezicht droog en schoon."),

    # Additional history patterns
    (r"Descended from Roman drover honden, Rottweilers were used to herd livestock en pull carts in German town of Rottweil\. They later became police, military, en guard honden\.",
     "Afstammend van Romeinse veedrijvershonden werden Rottweilers gebruikt om vee te hoeden en karren te trekken in de Duitse stad Rottweil. Later werden ze politie-, militaire en waakhonden."),

    # History section patterns
    (r"Despite name, Labrador Retrievers actually originated in Newfoundland, Canada, where they helped fishermen retrieve nets and catch escaping fish\. British nobles visiting Canada fell in love with ras and brought them to England\.",
     "Ondanks de naam zijn Labrador Retrievers eigenlijk afkomstig uit Newfoundland, Canada, waar ze vissers hielpen netten op te halen en ontsnapte vis te vangen. Britse edelen die Canada bezochten werden verliefd op het ras en brachten ze naar Engeland."),
    (r"Developed in Scotland during mid-19th century by Lord Tweedmouth, who crossed a yellow retriever with a Tweed Water Spaniel to create perfect gunhond for retrieving waterfowl\.",
     "Ontwikkeld in Schotland in het midden van de 19e eeuw door Lord Tweedmouth, die een gele retriever kruiste met een Tweed Water Spaniel om de perfecte jachthond te creëren voor het apporteren van watervogels."),
    (r"Developed in Germany in late 1800s by Captain Max von Stephanitz, who wanted to create ideal herding hond\. The ras quickly proved versatile and became popular worldwide for various working roles\.",
     "Ontwikkeld in Duitsland in de late jaren 1800 door Kapitein Max von Stephanitz, die de ideale herdershond wilde creëren. Het ras bleek al snel veelzijdig en werd wereldwijd populair voor verschillende werkrollen."),
    (r"Developed in Germany to hunt badgers—'dachshund' means 'badger hond\.' Their unique shape allowed them to dig into burrows and confront prey underground\.",
     "Ontwikkeld in Duitsland om dassen te jagen—'dachshund' betekent 'dashond'. Hun unieke vorm stelde hen in staat in holen te graven en prooi ondergronds te confronteren."),
    (r"Developed in 19th century Germany by crossing various rass to create ideal versatile hunting hond that could point, retrieve, and track on both land and water\.",
     "Ontwikkeld in 19e-eeuws Duitsland door verschillende rassen te kruisen om de ideale veelzijdige jachthond te creëren die kon voorstaan, apporteren en volgen op zowel land als water."),
    (r"Developed in Yorkshire, England during 1800s by Scottish weavers who brought terriers south\. Originally used to catch rats in textile mills\.",
     "Ontwikkeld in Yorkshire, Engeland in de jaren 1800 door Schotse wevers die terriërs naar het zuiden brachten. Oorspronkelijk gebruikt om ratten te vangen in textielfabrieken."),
    (r"Developed by Mahlemut Inuit people of Alaska's Norton Sound region, Malamutes were essential for survival in harsh Arctic environment\. They pulled heavy sleds, hunted seals, and protected their families from polar bears\. Unlike some rass created for speed, Malamutes were bred for strength and endurance\.",
     "Ontwikkeld door de Mahlemut Inuit van de Norton Sound-regio in Alaska, waren Malamutes essentieel voor overleving in de barre Arctische omgeving. Ze trokken zware sleeën, jaagden op zeehonden en beschermden hun families tegen ijsberen. In tegenstelling tot sommige rassen die voor snelheid zijn gefokt, werden Malamutes gefokt voor kracht en uithoudingsvermogen."),
    (r"Ancient ras developed in England for hunting rabbits\. Their excellent sense of smell made them valuable hunting metgezels\. Today they're also used as detection honds at airports\.",
     "Oud ras ontwikkeld in Engeland voor het jagen op konijnen. Hun uitstekende reukvermogen maakte hen waardevolle jachtmetgezellen. Tegenwoordig worden ze ook gebruikt als detectiehonden op luchthavens."),
    (r"Brought to Wales by Flemish weavers around 1100 AD\. Bred to herd cattle by nipping at their heels—their low stature helped them avoid kicks\.",
     "Gebracht naar Wales door Vlaamse wevers rond 1100 na Christus. Gefokt om vee te hoeden door in hun hielen te bijten—hun lage gestalte hielp hen trappen te ontwijken."),
    (r"Descended from English Bullhonds brought to France by lace workers\. French rasers developed distinctive bat ears and compact size that define ras today\.",
     "Afstammend van Engelse Bulldogs die door kantwerksters naar Frankrijk werden gebracht. Franse fokkers ontwikkelden de kenmerkende vleermuisoren en compacte bouw die het ras vandaag definiëren."),
    (r"The Affenpinscher originated in Germany\.",
     "De Affenpinscher is afkomstig uit Duitsland."),
    (r"The Azawakh originated in West Africa \(Mali, Niger, Burkina Faso\)\.",
     "De Azawakh is afkomstig uit West-Afrika (Mali, Niger, Burkina Faso)."),
    (r"The Bluetick Coonhound originated in United States\.",
     "De Bluetick Coonhound is afkomstig uit de Verenigde Staten."),
    (r"The Bouvier des Flandres originated in Belgium/Frankrijk\.",
     "De Bouvier des Flandres is afkomstig uit België/Frankrijk."),
    (r"The Chesapeake Bay Retriever originated in United States\.",
     "De Chesapeake Bay Retriever is afkomstig uit de Verenigde Staten."),
    (r"The Cirneco dell'Etna originated in Italy \(Sicily\)\.",
     "De Cirneco dell'Etna is afkomstig uit Italië (Sicilië)."),
    (r"The Deutscher Wachtelhund originated in Duitsland\.",
     "De Deutscher Wachtelhund is afkomstig uit Duitsland."),
    (r"The Drentse Patrijshond originated in Netherlands\.",
     "De Drentse Patrijshond is afkomstig uit Nederland."),
    (r"The Grand Basset Griffon Vendéen originated in Frankrijk\.",
     "De Grand Basset Griffon Vendéen is afkomstig uit Frankrijk."),
    (r"The Löwchen originated in Frankrijk/Duitsland\.",
     "De Löwchen is afkomstig uit Frankrijk/Duitsland."),
    (r"The Large Münsterländer originated in Duitsland\.",
     "De Grote Münsterländer is afkomstig uit Duitsland."),
    (r"The Nederlandse Kooikerhondje originated in Netherlands\.",
     "De Nederlandse Kooikerhondje is afkomstig uit Nederland."),
    (r"The Nova Scotia Duck Tolling Retriever originated in Canada\.",
     "De Nova Scotia Duck Tolling Retriever is afkomstig uit Canada."),
    (r"The Petit Basset Griffon Vendéen originated in Frankrijk\.",
     "De Petit Basset Griffon Vendéen is afkomstig uit Frankrijk."),
    (r"The Portuguese Podengo Pequeno originated in Portugal\.",
     "De Portuguese Podengo Pequeno is afkomstig uit Portugal."),
    (r"The Redbone Coonhound originated in United States\.",
     "De Redbone Coonhound is afkomstig uit de Verenigde Staten."),
    (r"The Small Münsterländer originated in Duitsland\.",
     "De Kleine Münsterländer is afkomstig uit Duitsland."),
    (r"The Treeing Walker Coonhound originated in United States\.",
     "De Treeing Walker Coonhound is afkomstig uit de Verenigde Staten."),
    (r"The White Swiss Shepherd originated in Switzerland\.",
     "De Witte Zwitserse Herder is afkomstig uit Zwitserland."),
    (r"the Amerikaanse Engelse Coonhound originated in United States\.",
     "De Amerikaanse Engelse Coonhound is afkomstig uit de Verenigde Staten."),
    (r"the Amerikaanse Foxhound originated in United States\.",
     "De Amerikaanse Foxhound is afkomstig uit de Verenigde Staten."),
    (r"the Amerikaanse Naakthond originated in United States\.",
     "De Amerikaanse Naakthond is afkomstig uit de Verenigde Staten."),
    (r"originated in United States", "is afkomstig uit de Verenigde Staten"),
    (r"originated in Netherlands", "is afkomstig uit Nederland"),
    (r"originated in Frankrijk", "is afkomstig uit Frankrijk"),
    (r"originated in Duitsland", "is afkomstig uit Duitsland"),
    (r"originated in", "is afkomstig uit"),
    (r"is afkomstig uit Switzerland", "is afkomstig uit Zwitserland"),
    (r"is afkomstig uit Australia", "is afkomstig uit Australië"),
    (r"is afkomstig uit Italy", "is afkomstig uit Italië"),
    (r"is afkomstig uit Belgium", "is afkomstig uit België"),
    (r"is afkomstig uit Spain", "is afkomstig uit Spanje"),
    (r"is afkomstig uit Japan", "is afkomstig uit Japan"),
    (r"is afkomstig uit China", "is afkomstig uit China"),
    (r"is afkomstig uit Hungary", "is afkomstig uit Hongarije"),
    (r"is afkomstig uit Poland", "is afkomstig uit Polen"),
    (r"is afkomstig uit Russia", "is afkomstig uit Rusland"),
    (r"is afkomstig uit Tibet", "is afkomstig uit Tibet"),
    (r"is afkomstig uit Ireland", "is afkomstig uit Ierland"),
    (r"is afkomstig uit Mexico", "is afkomstig uit Mexico"),
    (r"\bthe\b", "de"),
    (r"\bThe\b", "De"),
    
    # Bulldog history
    (r"Oorspronkelijk gefokt for bull-baiting in Engeland\. When sport was banned in 1835, fokkers worked to transform aggressive fighter into a zacht metgezel\.",
     "Oorspronkelijk gefokt voor stierengevechten in Engeland. Toen de sport in 1835 werd verboden, werkten fokkers eraan om de agressieve vechter om te vormen tot een zachtaardige metgezel."),
    (r"for bull-baiting in", "voor stierengevechten in"),
    (r"When sport was banned in 1835", "Toen de sport in 1835 werd verboden"),
    (r"fokkers worked to transform", "werkten fokkers eraan om"),
    (r"aggressive fighter into a zacht metgezel", "de agressieve vechter om te vormen tot een zachtaardige metgezel"),

    # Mixed patterns with "ras" or partial Dutch
    (r"High energy ras requiring", "Hoogenergetisch ras dat vereist"),
    (r"actieve gezinnenes", "actieve gezinnen"),

    # Additional health phrases
    (r"Prone to patellaluxatie, heupdysplasie, en hartgeruis\. Their flat face can cause breathing issues in extreme temperatures\. Regular dental care is essential due to their small mouth\.",
     "Vatbaar voor patellaluxatie, heupdysplasie en hartgeruis. Hun platte snuit kan ademhalingsproblemen veroorzaken bij extreme temperaturen. Regelmatige tandverzorging is essentieel vanwege hun kleine bek."),
    (r"Their flat face can cause breathing issues in extreme temperatures\.",
     "Hun platte snuit kan ademhalingsproblemen veroorzaken bij extreme temperaturen."),
    (r"Regular dental care is essential due to their small mouth\.",
     "Regelmatige tandverzorging is essentieel vanwege hun kleine bek."),

    # Additional temperament phrases
    (r"Malamutes are vriendelijk en outgoing with people, including strangers—they make poor guard honden\. Ze zijn trouw en toegewijd to their families but have an onafhankelijk streak\. Ze kunnen be challenging to train due to their koppigness, but ze zijn highly intelligent\. Ze kunnen be aggressive toward other honden, especially same-sex honden\.",
     "Malamutes zijn vriendelijk en extravert met mensen, inclusief vreemden—ze zijn slechte waakhonden. Ze zijn trouw en toegewijd aan hun families maar hebben een onafhankelijke inslag. Ze kunnen uitdagend zijn om te trainen vanwege hun koppigheid, maar ze zijn zeer intelligent. Ze kunnen agressief zijn naar andere honden, vooral honden van hetzelfde geslacht."),
    (r"make wonderful huisdieren\. Their intelligence en gretigness to please make training enjoyable\. Vroege socialisatie helps them develop into well-rounded metgezellen\.",
     "zijn geweldige huisdieren. Hun intelligentie en gretigheid om te behagen maken training plezierig. Vroege socialisatie helpt hen zich te ontwikkelen tot evenwichtige metgezellen."),
    (r"Their intelligence en gretigness to please make training enjoyable\.",
     "Hun intelligentie en gretigheid om te behagen maken training plezierig."),
    (r"Vroege socialisatie helps them develop into well-rounded metgezellen\.",
     "Vroege socialisatie helpt hen zich te ontwikkelen tot evenwichtige metgezellen."),

    # Common English phrases
    (r"Generally healthy with a lifespan of", "Over het algemeen gezond met een levensverwachting van"),
    (r"Common concerns include", "Veelvoorkomende aandoeningen zijn"),
    (r"Regular veterinary checkups and preventive care are important\.", "Regelmatige veterinaire controles en preventieve zorg zijn belangrijk."),
    (r"Maintaining a healthy weight helps prevent many health issues\.", "Een gezond gewicht helpt veel gezondheidsproblemen te voorkomen."),
    (r"Prone to hip dysplasia", "Vatbaar voor heupdysplasie"),
    (r"hip dysplasia", "heupdysplasie"),
    (r"\bbloat\b", "opgeblazen maag"),
    (r"skin conditions", "huidaandoeningen"),
    (r"joint problems", "gewrichtsproblemen"),
    (r"patellar luxation", "patellaluxatie"),
    (r"dental issues", "gebitsklachten"),
    (r"heart murmurs", "hartgeruis"),
    (r"eye conditions", "oogaandoeningen"),
    (r"autoimmune disorders", "auto-immuunziekten"),
    (r"progressive retinal atrophy", "progressieve retina-atrofie"),
    (r"Bloat is een serious concern requiring awareness of symptoms\.", "Maagdraaiing is een serieuze zorg die bewustzijn van symptomen vereist."),
    (r"Regular health screenings recommended\.", "Regelmatige gezondheidscontroles worden aanbevolen."),
    (r"Lifespan is typically", "De levensverwachting is meestal"),

    # Exercise phrases
    (r"High energy requiring vigorous daily exercise", "Hoge energie die intensieve dagelijkse beweging vereist"),
    (r"vigorous daily exercise", "intensieve dagelijkse beweging"),
    (r"at least an hour of activity", "minimaal een uur activiteit"),
    (r"They thrive with", "Ze gedijen goed bij"),
    (r"who enjoy outdoor activities", "die van buitenactiviteiten houden"),
    (r"Mental stimulation through training and puzzle toys is equally important\.", "Mentale stimulatie door training en puzzelspeelgoed is even belangrijk."),
    (r"Without adequate exercise, they may develop behavioral issues\.", "Zonder voldoende beweging kunnen ze gedragsproblemen ontwikkelen."),
    (r"Without adequate exercise, they may become destructive\.", "Zonder voldoende beweging kunnen ze destructief worden."),
    (r"Without adequate exercise, they can become destructive\.", "Zonder voldoende beweging kunnen ze destructief worden."),
    (r"They excel at swimming, hiking, and", "Ze blinken uit in zwemmen, wandelen en"),
    (r"hond sports", "hondensporten"),
    (r"Mental challenges are equally important", "Mentale uitdagingen zijn even belangrijk"),
    (r"they thrive with jobs to do", "ze gedijen het beste met taken om te doen"),

    # Grooming phrases
    (r"Heavy shedders requiring regular brushing", "Verharen veel en vereisen regelmatig borstelen"),
    (r"daily during shedding season", "dagelijks tijdens de rui"),
    (r"Their feathered coat needs attention to prevent matting\.", "Hun gevederde vacht heeft aandacht nodig om klitten te voorkomen."),
    (r"Weekly brushing keeps coat healthy\.", "Wekelijks borstelen houdt de vacht gezond."),
    (r"They shed heavily, especially during seasonal changes\.", "Ze verharen veel, vooral tijdens seizoenswisselingen."),
    (r"Regular nail trimming and ear cleaning needed\.", "Regelmatig nagels knippen en oren schoonmaken is nodig."),
    (r"coat coat", "vacht"),

    # History phrases
    (r"Despite name,", "Ondanks de naam,"),
    (r"actually originated in", "is eigenlijk afkomstig uit"),
    (r"Developed in", "Ontwikkeld in"),
    (r"Bred to", "Gefokt om"),
    (r"Originally used to", "Oorspronkelijk gebruikt om"),
    (r"Originally bred", "Oorspronkelijk gefokt"),
    (r"were bred for", "werden gefokt voor"),
    (r"was bred for", "werd gefokt voor"),
    (r"brought to", "gebracht naar"),
    (r"fell in love with", "werd verliefd op"),
    (r"who wanted to create", "die wilde creëren"),
    (r"quickly proved versatile", "bleek al snel veelzijdig"),
    (r"became popular worldwide", "werd wereldwijd populair"),
    (r"for various working roles", "voor verschillende werkrollen"),
    (r"during mid-19th century", "in het midden van de 19e eeuw"),
    (r"in late 1800s", "in de late jaren 1800"),
    (r"during 1800s", "in de jaren 1800"),
    (r"around 1100 AD", "rond 1100 na Christus"),

    # Common verbs and phrases
    (r"They're", "Ze zijn"),
    (r"they're", "ze zijn"),
    (r"They are", "Ze zijn"),
    (r"they are", "ze zijn"),
    (r"They have", "Ze hebben"),
    (r"they have", "ze hebben"),
    (r"They can", "Ze kunnen"),
    (r"they can", "ze kunnen"),
    (r"They may", "Ze kunnen"),
    (r"they may", "ze kunnen"),
    (r"They need", "Ze hebben nodig"),
    (r"they need", "ze hebben nodig"),
    (r"They excel at", "Ze blinken uit in"),
    (r"they excel at", "ze blinken uit in"),
    (r"They love", "Ze houden van"),
    (r"they love", "ze houden van"),

    # Dog-related terms
    (r"\bworking dogs\b", "werkhonden"),
    (r"\bworking dog\b", "werkhond"),
    (r"\btherapy dogs\b", "therapiehonden"),
    (r"\btherapy dog\b", "therapiehond"),
    (r"\bfamily pets\b", "huisdieren"),
    (r"\bfamily pet\b", "huisdier"),
    (r"\bguard dogs\b", "waakhonden"),
    (r"\bguard dog\b", "waakhond"),
    (r"\bwatchdogs\b", "waakhonden"),
    (r"\bwatchdog\b", "waakhond"),
    (r"\bherding dogs\b", "herdershonden"),
    (r"\bherding dog\b", "herdershond"),
    (r"\bhunting dogs\b", "jachthonden"),
    (r"\bhunting dog\b", "jachthond"),
    (r"\bdetection honds\b", "detectiehonden"),
    (r"\bdetection dogs\b", "detectiehonden"),
    (r"\bhonds\b", "honden"),
    (r"\bhond\b", "hond"),
    (r"\brass\b", "rassen"),
    (r"\brasers\b", "fokkers"),
    (r"\bgunhond\b", "jachthond"),
    (r"\bmetgezels\b", "metgezellen"),

    # Common adjectives
    (r"\bfriendly\b", "vriendelijk"),
    (r"\bloyal\b", "loyaal"),
    (r"\bintelligent\b", "intelligent"),
    (r"\bplayful\b", "speels"),
    (r"\bgentle\b", "zachtaardig"),
    (r"\bactive\b", "actief"),
    (r"\benergetic\b", "energiek"),
    (r"\bprotective\b", "beschermend"),
    (r"\baffectionate\b", "aanhankelijk"),
    (r"\bobedient\b", "gehoorzaam"),
    (r"\bversatile\b", "veelzijdig"),
    (r"\bexcellent\b", "uitstekend"),

    # Common phrases
    (r"with children", "met kinderen"),
    (r"make excellent", "zijn uitstekende"),
    (r"is known for being", "staat bekend om"),
    (r"are known for", "staan bekend om"),
    (r"Early socialization", "Vroege socialisatie"),
    (r"early socialization", "vroege socialisatie"),

    # Places
    (r"\bGermany\b", "Duitsland"),
    (r"\bEngland\b", "Engeland"),
    (r"\bScotland\b", "Schotland"),
    (r"\bFrance\b", "Frankrijk"),
    (r"\bCanada\b", "Canada"),
    (r"\bWales\b", "Wales"),

    # More specific patterns
    (r" coat\.", " vacht."),
    (r" coat ", " vacht "),
    (r" and ", " en "),
    (r"years\.", "jaar."),
    
    # More complete grooming phrases
    (r"Depends on vacht type\. Smooth coats need minimal care\. Wirehaired need stripping\. Longhaired need regular brushing\.",
     "Hangt af van het vachttype. Gladde vachten hebben minimale verzorging nodig. Draadharige vachten moeten getrimd worden. Langharige vachten moeten regelmatig geborsteld worden."),
    (r"High maintenance vacht requiring daily brushing en regular professional grooming\. Many eigenaren opt for shorter 'puppy cuts\.'",
     "Veeleisende vacht die dagelijks borstelen en regelmatige professionele verzorging vereist. Veel eigenaren kiezen voor kortere 'puppyknippen'."),
    (r"High maintenance vacht requiring professional grooming every 4-6 weeks\. Daily brushing to prevent matting\. The trade-off is minimal shedding\.",
     "Veeleisende vacht die elke 4-6 weken professionele verzorging vereist. Dagelijks borstelen om klitten te voorkomen. Het voordeel is minimale verharing."),
    
    # More grooming phrases
    (r"Easy to groom", "Makkelijk te verzorgen"),
    (r"Easy to maintain", "Makkelijk te onderhouden"),
    (r"Very easy to groom", "Zeer makkelijk te verzorgen"),
    (r"Weekly brushing", "Wekelijks borstelen"),
    (r"Heavy shedders", "Verharen veel"),
    (r"brush several times a week", "meerdere keren per week borstelen"),
    (r"They 'blow' their", "Ze verharen sterk hun"),
    (r"twice a year", "twee keer per jaar"),
    (r"when daily brushing is needed", "wanneer dagelijks borstelen nodig is"),
    (r"Regular nail, ear,", "Regelmatige nagel-, oor-"),
    (r"en dental care", "en tandverzorging"),
    (r"occasional baths", "af en toe in bad"),
    (r"Low maintenance", "Onderhoudsvriendelijk"),
    (r"Keep wrinkles dry to prevent infections", "Houd rimpels droog om infecties te voorkomen"),
    (r"Keep facial folds dry en clean", "Houd de plooien in het gezicht droog en schoon"),
    (r"Daily wrinkle cleaning to prevent infections", "Dagelijks rimpels schoonmaken om infecties te voorkomen"),
    (r"regular facial fold cleaning", "regelmatig plooien van het gezicht schoonmaken"),
    (r"Moderate shedding with heavier periods", "Matige verharing met zwaardere periodes"),
    (r"floppy ears", "hangende oren"),
    (r"Regular ear cleaning is important due to their", "Regelmatige oorverzorging is belangrijk vanwege hun"),
    (r"seasonally", "seizoensgebonden"),
    (r"minimum, daily during shedding", "minimaal, dagelijks tijdens de rui"),
    
    # More general phrases
    (r"outgoing with people", "extravert met mensen"),
    (r"including strangers", "inclusief vreemden"),
    (r"they make poor guard", "ze zijn slechte waak"),
    (r"to their families but have an", "aan hun families maar hebben een"),
    (r"onafhankelijk streak", "onafhankelijke inslag"),
    (r"be challenging to train due to their", "uitdagend zijn om te trainen vanwege hun"),
    (r"koppigness", "koppigheid"),
    (r"but ze zijn highly intelligent", "maar ze zijn zeer intelligent"),
    (r"be aggressive toward other", "agressief zijn naar andere"),
    (r"especially same-sex", "vooral van hetzelfde geslacht"),
    (r"make wonderful", "zijn geweldige"),
    (r"gretigness to please make training enjoyable", "gretigheid om te behagen maken training plezierig"),
    (r"helps them develop into well-rounded", "helpt hen zich te ontwikkelen tot evenwichtige"),
    (r"Prone to", "Vatbaar voor"),
    
    # More overview phrases
    (r"the Flatcoated Retriever is Peter Pan of retrievers—they never seem to grow up\. These cheerful, optimistic honden maintain their puppy-like enthusiasm well into adulthood\.",
     "De Flatcoated Retriever is de Peter Pan van de retrievers—ze lijken nooit volwassen te worden. Deze vrolijke, optimistische honden behouden hun puppyachtige enthousiasme tot ver in hun volwassenheid."),
    (r"the Franse Engelse Bullhond has enjoyed a surge in popularity\. The adaptable Frenchie is ideal metgezel for city dwellers—they don't need a lot of space en are content with short walks en indoor play\.",
     "De Franse Bulldog heeft een sterke toename in populariteit genoten. De aanpasbare Frenchie is een ideale metgezel voor stadsbewoners—ze hebben niet veel ruimte nodig en zijn tevreden met korte wandelingen en spelen binnenshuis."),
    (r"the Duitse Staande Korthaar is een veelzijdig hunting hond en all-purpose gun hond\. Ze zijn known for their power, speed, agility, en endurance—plus a striking appearance\.",
     "De Duitse Staande Korthaar is een veelzijdige jachthond en allround jachthond. Ze staan bekend om hun kracht, snelheid, behendigheid en uithoudingsvermogen—plus een opvallend uiterlijk."),
    (r"they never seem to grow up", "ze lijken nooit volwassen te worden"),
    (r"These cheerful, optimistic", "Deze vrolijke, optimistische"),
    (r"maintain their puppy-like enthusiasm well into adulthood", "behouden hun puppyachtige enthousiasme tot ver in hun volwassenheid"),
    (r"has enjoyed a surge in popularity", "heeft een sterke toename in populariteit genoten"),
    (r"The adaptable Frenchie is ideal metgezel for city dwellers", "De aanpasbare Frenchie is een ideale metgezel voor stadsbewoners"),
    (r"they don't need a lot of space", "ze hebben niet veel ruimte nodig"),
    (r"are content with short walks", "zijn tevreden met korte wandelingen"),
    (r"indoor play", "spelen binnenshuis"),
    (r"hunting hond", "jachthond"),
    (r"all-purpose gun hond", "allround jachthond"),
    (r"known for their power, speed, agility, en endurance", "bekend om hun kracht, snelheid, behendigheid en uithoudingsvermogen"),
    (r"plus a striking appearance", "plus een opvallend uiterlijk"),

    # More history phrases
    (r"Descended from", "Afstammend van"),
    (r"Roman drover honden", "Romeinse veedrijvershonden"),
    (r"were used to herd livestock", "werden gebruikt om vee te hoeden"),
    (r"en pull carts in German town of Rottweil", "en karren te trekken in de Duitse stad Rottweil"),
    (r"They later became", "Later werden ze"),
    (r"police, military, en guard honden", "politie-, militaire en waakhonden"),
]


def fix_jsonld_in_file(filepath: Path) -> bool:
    """Fix JSON-LD translations in a single file. Returns True if changes were made."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Find all JSON-LD script blocks
    pattern = r'(<script type="application/ld\+json">)(.*?)(</script>)'
    
    def fix_jsonld_block(match):
        prefix = match.group(1)
        json_content = match.group(2)
        suffix = match.group(3)
        
        # Apply translations to the JSON content
        for pat, replacement in TRANSLATIONS:
            json_content = re.sub(pat, replacement, json_content)
        
        return prefix + json_content + suffix
    
    content = re.sub(pattern, fix_jsonld_block, content, flags=re.DOTALL)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False


def main():
    """Fix all Dutch breed pages."""
    if not NL_BREEDS_DIR.exists():
        print(f"Directory not found: {NL_BREEDS_DIR}")
        return
    
    html_files = list(NL_BREEDS_DIR.glob("*.html"))
    print(f"Found {len(html_files)} HTML files in {NL_BREEDS_DIR}")
    
    fixed_count = 0
    for filepath in sorted(html_files):
        if fix_jsonld_in_file(filepath):
            print(f"Fixed: {filepath.name}")
            fixed_count += 1
    
    print(f"\nFixed {fixed_count} files")


if __name__ == "__main__":
    main()
