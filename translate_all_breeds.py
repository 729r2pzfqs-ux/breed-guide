#!/usr/bin/env python3
"""
Comprehensive Swedish translation for all breed pages.
Generates translations and applies them directly to Swedish HTML files.
"""

import os
import re
import json
from pathlib import Path
from sv_translations import BEST_FOR, NOT_IDEAL, TEMPERAMENT_TAGS

BREEDS_DIR = Path(__file__).parent / "breeds"
SV_BREEDS_DIR = Path(__file__).parent / "sv" / "breeds"

# Swedish translations for all 220 breeds
# Each entry: breed_name -> {meta_description, hero_desc, overview, temperament, health, exercise, verdict}

TRANSLATIONS = {
    "affenpinscher": {
        "meta_description": "\"Apphunden\" (Affen betyder apa på tyska) är en orädd liten terrier med stor personlighet. De är nyfikna, lekfulla och alltid underhållande.",
        "hero_desc": "Med sin självsäkra, orädda natur är Affenpinschern en älskad ras av goda skäl.",
        "overview": "\"Apphunden\" (Affen betyder apa på tyska) är en orädd liten terrier med stor personlighet. De är nyfikna, lekfulla och alltid underhållande.",
        "temperament": "Affenpinschern är självsäker, orädd och underhållande med en terrierliknande personlighet trots sin leksaksstorlek. De bildar starka band med sin familj och kan vara territoriella. Deras nyfikna natur och komiska uttryck har gett dem smeknamnet \"apphund\".",
        "health": "Generellt frisk med en livslängd på 12-15 år. Benägen för patellaluxation, höftledsdysplasi och hjärtblåsljud. Deras platta ansikte kan orsaka andningsproblem vid extrema temperaturer. Regelbunden tandvård är viktig på grund av deras lilla mun.",
        "exercise": "Måttliga motionsbehov med korta dagliga promenader och inomhuslek. De gillar interaktiva leksaker och mentala stimulansspel. Trots sin lilla storlek har de energiutbrott och älskar att leka. En inhägnad trädgård är idealisk eftersom de kan vara flyktartister.",
        "verdict": "\"Apphunden\" (Affen betyder apa på tyska) är en orädd liten terrier med stor personlighet. De är nyfikna, lekfulla och alltid underhållande."
    },
    "afghan-hound": {
        "meta_description": "Komplett guide till Afghanhunden: temperament, motionsbehov, pälsvård, hälsoproblem och om denna ras passar dig.",
        "hero_desc": "Byggd för äventyr — Afghanhunden behöver gott om motion och mental stimulans.",
        "overview": "Afghanhunden är en uråldrig, elegant vinthund känd för sin fantastiska flödande päls och aristokratiska hållning.",
        "temperament": "Afghanhundar är värdiga och reserverade mot främlingar men lekfulla och kärleksfulla med familjen. De har ett självständigt drag som kan göra träningen utmanande. Hemma visar de ofta en tokig, clownaktig sida som överraskar förstagångsägare.",
        "health": "Generellt frisk men benägen för höftledsdysplasi, grå starr och hypotyreos. Deras djupa bröstkorg gör dem mottagliga för volvulus. Regelbundna ögonundersökningar rekommenderas. Förväntad livslängd är 12-14 år med rätt vård.",
        "exercise": "Höga motionsbehov som kräver dagliga löprundor i ett säkert, inhägnat område. Deras starka jaktinstinkt innebär att de aldrig bör vara lös i ohägnade områden. De utmärker sig i lockjakt och agility. Mental stimulans genom träning hjälper till att förebygga tristess.",
        "verdict": "Eleganta, aristokratiska vinthundar med fantastisk päls. Afghaner är självständiga och reserverade men lojala mot familjen. Kräver omfattande pälsvård."
    },
    "airedale-terrier": {
        "meta_description": "Komplett guide till Airedaleterriern: temperament, motionsbehov, pälsvård, hälsoproblem och om denna ras passar dig.",
        "hero_desc": "Med sin självsäkra, modiga natur är Airedaleterriern en älskad ras av goda skäl.",
        "overview": "Airedalen är den största terrierrasen och har fått smeknamnet \"Terriernas Kung\" för sin storlek och mångsidighet.",
        "temperament": "Airedales är självsäkra, intelligenta och mångsidiga arbetshundar. De är utmärkta med barn och blir lojala familjevakter. Deras terrierenvishet kombinerad med träningsbarhet har gett dem titeln \"Terriernas Kung\".",
        "health": "Generellt robust med 11-14 års livslängd. Se upp för höftledsdysplasi, allergier och hypotyreos. Vissa linjer är benägna för volvulus. Regelbunden pälsvård hjälper till att upptäcka hudproblem tidigt.",
        "exercise": "Hög energi som kräver kraftfull daglig motion—minst en timmes aktivitet. De utmärker sig på simning, vandring och hundsport. Mentala utmaningar är lika viktiga; de trivs med uppgifter att utföra. Utan tillräcklig motion kan de bli destruktiva.",
        "verdict": "Terriernas Kung - mångsidig, intelligent och självsäker. Airedales är fantastiska familjehundar men behöver motion och erfaren hantering."
    },
    "akita": {
        "meta_description": "Komplett guide till Akitan: temperament, motionsbehov, pälsvård, hälsoproblem och om denna ras passar dig.",
        "hero_desc": "En modig, värdig stor ras som blir en underbar följeslagare.",
        "overview": "Akita är stora, kraftfulla hundar från Japan kända för sin värdighet och djupa lojalitet. De är symboler för god hälsa, lycka och långt liv i Japan.",
        "temperament": "Akitas är värdiga, modiga och djupt lojala mot sin familj. De kan vara reserverade eller kyliga mot främlingar och kan inte tolerera andra hundar, särskilt av samma kön. Tidig socialisering är avgörande för denna kraftfulla ras.",
        "health": "Benägen för höftledsdysplasi, autoimmuna sjukdomar och progressiv retinalatrofi. Volvulus är ett allvarligt problem som kräver medvetenhet om symptom. Regelbundna hälsokontroller rekommenderas. Livslängden är typiskt 10-13 år.",
        "exercise": "Måttliga till höga motionsbehov med dagliga promenader och lekstunder. De gillar aktiviteter i kallt väder och är utmärkta vandringskamrater. Mental stimulans genom träning förebygger tristess. En säkert inhägnad trädgård är nödvändig.",
        "verdict": "Kraftfulla, värdiga vakthundar med djup familjelojalitet. Akitas kräver erfarna ägare och tidig socialisering."
    },
    "alaskan-klee-kai": {
        "meta_description": "Komplett guide till Alaskan Klee Kai: temperament, motionsbehov, pälsvård, hälsoproblem och om denna ras passar dig.",
        "hero_desc": "En intelligent, nyfiken liten ras som blir en underbar följeslagare.",
        "overview": "Alaskan Klee Kai ser ut som en miniatyr-Husky men är en distinkt ras som utvecklades i Alaska på 1970-talet.",
        "temperament": "Alaskan Klee Kai är känd för att vara intelligent, nyfiken och vaksam. Deras intelligens och vilja att behaga gör träningen rolig. Tidig socialisering hjälper dem att utvecklas till välbalanserade följeslagare.",
        "health": "Generellt frisk med en livslängd på 12-16 år. Vanliga problem inkluderar patellaluxation och tandproblem. Regelbundna veterinärkontroller och förebyggande vård är viktiga. Att hålla en hälsosam vikt hjälper till att förebygga många hälsoproblem.",
        "exercise": "Högenergirassom kräver kraftfull daglig motion—minst en timmes aktivitet. De trivs med aktiva familjer som gillar utomhusaktiviteter. Mental stimulans genom träning och pussellek är lika viktig. Utan tillräcklig motion kan de utveckla beteendeproblem.",
        "verdict": "Mini-Husky-lookalikes med stora personligheter. Klee Kai är lojala och intelligenta men reserverade mot främlingar. Behöver erfarna ägare."
    },
    "alaskan-malamute": {
        "meta_description": "Komplett guide till Alaskan Malamute: temperament, motionsbehov, pälsvård, hälsoproblem och om denna ras passar dig.",
        "hero_desc": "Byggd för arbete, hängiven mot familjen — en stor ras med seriösa förmågor.",
        "overview": "Alaskan Malamute är en av de äldsta arktiska slädhundarna, ursprungligen avlad för att dra tunga laster. De är kraftfulla, rejäla hundar med djupt bröst och stark, välmuskulös kropp. Trots sitt vargliknande utseende är de vänliga och kärleksfulla mot människor.",
        "temperament": "Malamutes är vänliga och utåtriktade mot människor, inklusive främlingar—de blir dåliga vakthundar. De är lojala och hängivna mot sina familjer men har ett självständigt drag. De kan vara utmanande att träna på grund av sin envishet, men de är mycket intelligenta. De kan vara aggressiva mot andra hundar, särskilt hundar av samma kön.",
        "health": "Generellt frisk ras. Se upp för höftledsdysplasi, grå starr, kondrodysplasi (dvärgväxt), hypotyreos och ärftlig polyneuropati. Regelbundna veterinärkontroller och hälsoundersökningar rekommenderas.",
        "exercise": "Höga motionsbehov—minst 2 timmar dagligen. De utmärker sig på vandring, backpacking, slädhundskörning och viktdragning. Utan tillräcklig motion kan de bli destruktiva. De älskar kallt väder och kan ha svårt i varma klimat.",
        "verdict": "Kraftfulla arktiska arbetshundar med vänlig disposition. Malamutes behöver mycket motion och erfarna ägare."
    },
    "american-bulldog": {
        "meta_description": "Komplett guide till American Bulldog: temperament, motionsbehov, pälsvård, hälsoproblem och om denna ras passar dig.",
        "hero_desc": "Byggd för arbete, hängiven mot familjen — en stor ras med seriösa förmågor.",
        "overview": "American Bulldog är en kraftfull, atletisk ras som härstammar från arbetsbulldoggar som fördes till Amerika av invandrare.",
        "temperament": "American Bulldog är känd för att vara lojal, självsäker och vänlig. De är utmärkta med barn och blir underbara familjedjur. Deras intelligens och vilja att behaga gör träningen rolig. Tidig socialisering hjälper dem att utvecklas till välbalanserade följeslagare.",
        "health": "Generellt frisk med en livslängd på 10-12 år. Vanliga problem inkluderar höftledsdysplasi och volvulus. Regelbundna veterinärkontroller och förebyggande vård är viktiga. Att hålla en hälsosam vikt hjälper till att förebygga många hälsoproblem.",
        "exercise": "Högenergirassom kräver kraftfull daglig motion—minst en timmes aktivitet. De trivs med aktiva familjer som gillar utomhusaktiviteter. Mental stimulans genom träning och pussellek är lika viktig. Utan tillräcklig motion kan de utveckla beteendeproblem.",
        "verdict": "Kraftfulla, lojala arbetshundar med vänlig disposition. American Bulldogs behöver erfarna ägare, ordentlig träning och gott om motion."
    },
    "american-english-coonhound": {
        "meta_description": "Avlad för att jaga tvättbjörnar är American English Coonhound en mångsidig, atletisk stövare med en melodisk röst. De är vänliga, energiska hundar som behöver gott om motion.",
        "hero_desc": "Självständig men kärleksfull — en stövare som balanserar drivkraft med hängivenhet.",
        "overview": "Avlad för att jaga tvättbjörnar är American English Coonhound en mångsidig, atletisk stövare med en melodisk röst. De är vänliga, energiska hundar som behöver gott om motion.",
        "temperament": "American English Coonhound är känd för att vara trevlig, vaksam och självsäker. De är utmärkta med barn och blir underbara familjedjur. Tidig socialisering hjälper dem att utvecklas till välbalanserade följeslagare.",
        "health": "Generellt frisk med en livslängd på 11-12 år. Vanliga problem inkluderar höftledsdysplasi och volvulus. Regelbundna veterinärkontroller och förebyggande vård är viktiga. Att hålla en hälsosam vikt hjälper till att förebygga många hälsoproblem.",
        "exercise": "Högenergirassom kräver kraftfull daglig motion—minst en timmes aktivitet. De trivs med aktiva familjer som gillar utomhusaktiviteter. Mental stimulans genom träning och pussellek är lika viktig. Utan tillräcklig motion kan de utveckla beteendeproblem.",
        "verdict": "Avlad för att jaga tvättbjörnar är American English Coonhound en mångsidig, atletisk stövare med en melodisk röst. De är vänliga, energiska hundar som behöver gott om motion."
    },
    "american-eskimo-dog": {
        "meta_description": "Komplett guide till American Eskimo Dog: temperament, motionsbehov, pälsvård, hälsoproblem och om denna ras passar dig.",
        "hero_desc": "Smart, intelligent, vaksam och mottaglig för träning — idealisk för förstagångsägare.",
        "overview": "Trots sitt namn härstammar American Eskimo Dog från tyska spetshundar och var populär i cirkusföreställningar.",
        "temperament": "American Eskimo Dog är känd för att vara intelligent, vaksam och vänlig. De är utmärkta med barn och blir underbara familjedjur. Deras intelligens och vilja att behaga gör träningen rolig. Tidig socialisering hjälper dem att utvecklas till välbalanserade följeslagare.",
        "health": "Generellt frisk med en livslängd på 13-15 år. Vanliga problem inkluderar ledproblem och hudåkommor. Regelbundna veterinärkontroller och förebyggande vård är viktiga. Att hålla en hälsosam vikt hjälper till att förebygga många hälsoproblem.",
        "exercise": "Högenergirassom kräver kraftfull daglig motion—minst en timmes aktivitet. De trivs med aktiva familjer som gillar utomhusaktiviteter. Mental stimulans genom träning och pussellek är lika viktig. Utan tillräcklig motion kan de utveckla beteendeproblem.",
        "verdict": "Briljanta, fluffiga artister som älskar att lära sig. American Eskimo Dogs är mycket lätt att träna och vänliga men fäller mycket och kan vara ljudliga."
    },
    "american-foxhound": {
        "meta_description": "Komplett guide till American Foxhound: temperament, motionsbehov, pälsvård, hälsoproblem och om denna ras passar dig.",
        "hero_desc": "En söt, självständig följeslagare som är perfekt för familjer med barn.",
        "overview": "Virginias delstatshund, American Foxhound är en söt, lättgående ras med ett musikaliskt skall. De är självständiga men kärleksfulla följeslagare.",
        "temperament": "American Foxhound är känd för att vara söt, självständig och lättgående. De är utmärkta med barn och blir underbara familjedjur. Deras självständiga natur kräver tålmodig, konsekvent träning. Tidig socialisering hjälper dem att utvecklas till välbalanserade följeslagare.",
        "health": "Generellt frisk med en livslängd på 11-13 år. Vanliga problem inkluderar höftledsdysplasi och volvulus. Regelbundna veterinärkontroller och förebyggande vård är viktiga. Att hålla en hälsosam vikt hjälper till att förebygga många hälsoproblem.",
        "exercise": "Högenergirassom kräver kraftfull daglig motion—minst en timmes aktivitet. De trivs med aktiva familjer som gillar utomhusaktiviteter. Mental stimulans genom träning och pussellek är lika viktig. Utan tillräcklig motion kan de utveckla beteendeproblem.",
        "verdict": "Virginias delstatshund, American Foxhound är en söt, lättgående ras med ett musikaliskt skall. De är självständiga men kärleksfulla följeslagare."
    },
    "american-hairless-terrier": {
        "meta_description": "En verkligt hypoallergen ras, American Hairless Terrier är en livlig, intelligent följeslagare. De kräver hudskydd mot sol och kyla men är lätta att underhålla.",
        "hero_desc": "Atletisk och energisk, vaksam, perfekt för löpare, vandrare och aktiva familjer.",
        "overview": "En verkligt hypoallergen ras, American Hairless Terrier är en livlig, intelligent följeslagare. De kräver hudskydd mot sol och kyla men är lätta att underhålla.",
        "temperament": "American Hairless Terrier är känd för att vara energisk, vaksam och nyfiken. De är utmärkta med barn och blir underbara familjedjur. Deras intelligens och vilja att behaga gör träningen rolig. Tidig socialisering hjälper dem att utvecklas till välbalanserade följeslagare.",
        "health": "Generellt frisk med en livslängd på 14-16 år. Vanliga problem inkluderar patellaluxation och tandproblem. Regelbundna veterinärkontroller och förebyggande vård är viktiga. Att hålla en hälsosam vikt hjälper till att förebygga många hälsoproblem.",
        "exercise": "Högenergirassom kräver kraftfull daglig motion—minst en timmes aktivitet. De trivs med aktiva familjer som gillar utomhusaktiviteter. Mental stimulans genom träning och pussellek är lika viktig. Utan tillräcklig motion kan de utveckla beteendeproblem.",
        "verdict": "En verkligt hypoallergen ras, American Hairless Terrier är en livlig, intelligent följeslagare. De kräver hudskydd mot sol och kyla men är lätta att underhålla."
    },
    "american-staffordshire-terrier": {
        "meta_description": "Komplett guide till American Staffordshire Terrier: temperament, motionsbehov, pälsvård, hälsoproblem och om denna ras passar dig.",
        "hero_desc": "Kraftfull och kärleksfull — en lojal familjehund med ett hjärta av guld.",
        "overview": "American Staffordshire Terrier är en muskulös, kärleksfull ras som är känd för sin lojalitet och mod. Trots sitt tuffa utseende är de mjuka familjehundar.",
        "temperament": "AmStaff är självsäker, smart och godmodig. De är otroligt lojala mot sin familj och älskar barn. De kan vara reserverade mot främlingar men är sällan aggressiva om de är rätt socialiserade och tränade.",
        "health": "Generellt frisk med en livslängd på 12-16 år. Vanliga problem inkluderar höftledsdysplasi, hjärtsjukdomar och allergier. Regelbundna veterinärkontroller rekommenderas.",
        "exercise": "Högenergirassom kräver daglig motion—minst en timmes aktivitet. De utmärker sig i hundsporter som agility och viktdragning. Mental stimulans är lika viktig som fysisk motion.",
        "verdict": "Lojala, kärleksfulla hundar med ett orättvist rykte. AmStaffs behöver erfarna ägare, tidig socialisering och gott om motion."
    },
    "american-water-spaniel": {
        "meta_description": "Komplett guide till American Water Spaniel: temperament, motionsbehov, pälsvård, hälsoproblem och om denna ras passar dig.",
        "hero_desc": "En mångsidig jakt- och familjehund med ett glatt temperament.",
        "overview": "American Water Spaniel är Wisconsins delstatshund, utvecklad för att hämta vilt från båtar i Great Lakes-regionen. De är mångsidiga jaktspaniels med vattentålig päls.",
        "temperament": "American Water Spaniel är energisk, glad och ivrig att behaga. De är utmärkta familjehundar och kommer bra överens med barn. Deras intelligens och arbetslust gör dem lätta att träna.",
        "health": "Generellt frisk med en livslängd på 10-14 år. Vanliga problem inkluderar höftledsdysplasi och ögonproblem. Regelbundna hälsokontroller är viktiga.",
        "exercise": "Höga motionsbehov—de älskar att simma och apportera. Daglig motion med varierade aktiviteter håller dem lyckliga. De trivs med aktiva familjer som inkluderar dem i utomhusaktiviteter.",
        "verdict": "Mångsidiga jaktspaniels som utmärker sig i vatten. American Water Spaniels är glada familjehundar men behöver aktiva ägare."
    },
    "anatolian-shepherd": {
        "meta_description": "Komplett guide till Anatolisk herdehund: temperament, motionsbehov, pälsvård, hälsoproblem och om denna ras passar dig.",
        "hero_desc": "En kraftfull, självständig vakthund med uråldriga rötter.",
        "overview": "Anatolisk herdehund är en uråldrig ras från Turkiet, avlad för att skydda boskap mot rovdjur. De är stora, kraftfulla hundar med ett oberoende och skyddande temperament.",
        "temperament": "Anatolisk herdehund är lugn, självsäker och skyddande. De är oerhört lojala mot sin familj men kan vara reserverade eller misstänksamma mot främlingar. Deras självständiga natur kräver en erfaren ägare.",
        "health": "Generellt frisk med en livslängd på 11-13 år. Vanliga problem inkluderar höftledsdysplasi och entropion. Regelbundna veterinärkontroller rekommenderas.",
        "exercise": "Måttliga motionsbehov med dagliga promenader och tid i trädgården. De är inte hyperaktiva men behöver utrymme att patrullera. En säkert inhägnad trädgård är nödvändig.",
        "verdict": "Kraftfulla, självständiga vakthundar från Turkiet. Anatoliska herdehundar behöver erfarna ägare, tidig socialisering och gott om utrymme."
    },
    "appenzeller-sennenhund": {
        "meta_description": "Komplett guide till Appenzeller Sennenhund: temperament, motionsbehov, pälsvård, hälsoproblem och om denna ras passar dig.",
        "hero_desc": "En livlig, mångsidig schweizisk bergshund med obegränsad energi.",
        "overview": "Appenzeller Sennenhund är den mest energiska av de fyra schweiziska sennenhundraserna. De är mångsidiga gårdshundar som utmärker sig på vallning, vakthållning och som följeslagare.",
        "temperament": "Appenzellers är livliga, självsäkra och pålitliga. De är misstänksamma mot främlingar men kärleksfulla med familjen. Deras höga energi och intelligens kräver aktiva ägare.",
        "health": "Generellt frisk med en livslängd på 12-15 år. Vanliga problem inkluderar höftledsdysplasi och ögonproblem. Regelbundna hälsokontroller är viktiga.",
        "exercise": "Mycket höga motionsbehov—de behöver flera timmar aktivitet dagligen. De utmärker sig i hundsporter, vallning och andra arbetsuppgifter. Utan tillräcklig motion blir de destruktiva.",
        "verdict": "Energiska, mångsidiga schweiziska gårdshundar. Appenzellers behöver mycket motion, mental stimulans och erfarna ägare."
    },
    "australian-cattle-dog": {
        "meta_description": "Komplett guide till Australian Cattle Dog: temperament, motionsbehov, pälsvård, hälsoproblem och om denna ras passar dig.",
        "hero_desc": "En tuff, intelligent arbetshund med outtömlig energi.",
        "overview": "Australian Cattle Dog, även kallad Blue Heeler eller Red Heeler, är en tuff arbetshund utvecklad för att driva boskap i det australiska landskapet.",
        "temperament": "Australian Cattle Dogs är intelligenta, vaksamma och beskyddande. De är extremt lojala mot sin ägare men kan vara reserverade mot främlingar. Deras starka arbetsinstinkt kräver aktiva ägare.",
        "health": "Generellt frisk med en livslängd på 12-16 år. Vanliga problem inkluderar höftledsdysplasi och progressiv retinalatrofi. Hörselnedsättning kan förekomma.",
        "exercise": "Mycket höga motionsbehov—de behöver intensiv daglig aktivitet. De utmärker sig i agility, vallning och flyball. Mental stimulans är lika viktig som fysisk motion.",
        "verdict": "Intelligenta, energiska arbetshundar med stark lojalitet. Australian Cattle Dogs behöver mycket motion, träning och erfarna ägare."
    },
    "australian-shepherd": {
        "meta_description": "Komplett guide till Australian Shepherd: temperament, motionsbehov, pälsvård, hälsoproblem och om denna ras passar dig.",
        "hero_desc": "En briljant, energisk vallhund som lever för att arbeta och leka.",
        "overview": "Trots sitt namn utvecklades Australian Shepherd i USA som en mångsidigt vallhund. De är kända för sin intelligens, atletiska förmåga och vackra pälsfärger.",
        "temperament": "Aussies är intelligenta, energiska och ivriga att behaga. De är utmärkta familjehundar men har ett starkt vallinstinkt som kan riktas mot barn eller andra husdjur. De behöver mentalt och fysiskt krävande aktiviteter.",
        "health": "Generellt frisk med en livslängd på 12-15 år. Vanliga problem inkluderar höftledsdysplasi, epilepsi och ögonproblem. MDR1-genmutation kan påverka läkemedelskänslighet.",
        "exercise": "Mycket höga motionsbehov—de behöver flera timmar aktivitet dagligen. De utmärker sig i agility, vallning, flygboll och frisbeesport. Utan tillräcklig stimulans blir de oroliga och destruktiva.",
        "verdict": "Briljanta, mångsidiga vallhundar med obegränsad energi. Aussies behöver aktiva ägare, mycket träning och dagliga utmaningar."
    },
    "australian-terrier": {
        "meta_description": "Komplett guide till Australian Terrier: temperament, motionsbehov, pälsvård, hälsoproblem och om denna ras passar dig.",
        "hero_desc": "En modig, livlig liten terrier med ett stort hjärta.",
        "overview": "Australian Terrier är en av de minsta arbetsterrierna, utvecklad i Australien för att jaga skadedjur och vara en vaksam följeslagare.",
        "temperament": "Aussie Terriers är modiga, självsäkra och tillgivna. De är utmärkta vakthundar och trogna följeslagare. Trots sin lilla storlek har de stort mod och terrieranda.",
        "health": "Generellt frisk med en livslängd på 11-15 år. Vanliga problem inkluderar patellaluxation och diabetes. Regelbundna veterinärkontroller är viktiga.",
        "exercise": "Måttliga motionsbehov med dagliga promenader och lekstunder. De gillar att gräva och jaga—en säker trädgård är viktig. Mental stimulans genom träning och spel håller dem nöjda.",
        "verdict": "Modiga, tillgivna små terriers med stort personlighet. Australian Terriers passar familjer som vill ha en kompakt men tuff följeslagare."
    },
    "azawakh": {
        "meta_description": "Komplett guide till Azawakh: temperament, motionsbehov, pälsvård, hälsoproblem och om denna ras passar dig.",
        "hero_desc": "En elegant, snabb vinthund från Saharas ökenlandskap.",
        "overview": "Azawakh är en sällsynt vinthund från Västafrika, ursprungligen avlad av nomadstammarna för att jaga gaseller och vakta läger.",
        "temperament": "Azawakhs är reserverade, oberoende och djupt lojala mot sin familj. De är varsamma mot främlingar men tillgivna med de de litar på. De har ett starkt skyddsinstinkt.",
        "health": "Generellt frisk med en livslängd på 12-15 år. De har låg kroppsfett vilket gör dem känsliga för kyla och anestesi. Blodprovsvärden kan avvika från andra raser.",
        "exercise": "Höga motionsbehov med behov av dagliga löprundor i säkra, inhägnade områden. De har stark jaktinstinkt och bör inte vara lösa i ohägnade områden.",
        "verdict": "Eleganta, snabba vinthundar med djup familjelojalitet. Azawakhs behöver erfarna ägare, säkra utrymmen och förståelse för deras unika behov."
    },
    "barbet": {
        "meta_description": "Komplett guide till Barbet: temperament, motionsbehov, pälsvård, hälsoproblem och om denna ras passar dig.",
        "hero_desc": "En glad, lockig vattenhund med ett hjärtligt temperament.",
        "overview": "Barbet är en fransk vattenhund med anor från medeltiden. Deras namn kommer från det franska ordet \"barbe\" (skägg) för deras karakteristiska ansiktsbehåring.",
        "temperament": "Barbets är glada, vänliga och intelligenta. De är utmärkta familjehundar som kommer bra överens med barn och andra husdjur. De älskar vatten och är naturliga simmare.",
        "health": "Generellt frisk med en livslängd på 12-14 år. Vanliga problem inkluderar höftledsdysplasi, öroninfektioner och ögonproblem. Regelbunden pälsvård är viktig.",
        "exercise": "Höga motionsbehov—de älskar att simma och apportera. Dagliga aktiviteter med varierade övningar håller dem lyckliga. De trivs med aktiva familjer.",
        "verdict": "Glada, mångsidiga vattenhundar med lockig päls. Barbets är utmärkta familjehundar men kräver regelbunden pälsvård och aktiva ägare."
    },
    "basenji": {
        "meta_description": "Komplett guide till Basenji: temperament, motionsbehov, pälsvård, hälsoproblem och om denna ras passar dig.",
        "hero_desc": "En uråldrig, kattlik hund som inte skäller utan jodlar.",
        "overview": "Basenji är en av världens äldsta hundraser, ursprungligen från Centralafrika. De är kända som \"den skällfria hunden\" för sitt unika jodelliknande läte.",
        "temperament": "Basenjis är intelligenta, oberoende och nyfikna. De är kattlika i sitt beteende—rengör sig själva och kan vara reserverade. De bildar starka band med sin familj men kan vara envisa att träna.",
        "health": "Generellt frisk med en livslängd på 12-14 år. Specifika problem inkluderar Fanconis syndrom och progressiv retinalatrofi. Regelbundna hälsokontroller är viktiga.",
        "exercise": "Höga motionsbehov med dagliga promenader och lekstunder. De har stark jaktinstinkt och bör hållas i koppel eller inhägnade områden. Mental stimulans är viktig.",
        "verdict": "Unika, kattlika hundar med uråldriga rötter. Basenjis behöver erfarna ägare som förstår deras oberoende natur och unika behov."
    },
    "basset-hound": {
        "meta_description": "Komplett guide till Basset Hound: temperament, motionsbehov, pälsvård, hälsoproblem och om denna ras passar dig.",
        "hero_desc": "En charmerande, lågmäld stövare med ett utmärkt luktsinne.",
        "overview": "Basset Hound är en fransk stövare känd för sina långa öron, sorgmodiga ögon och exceptionella luktsinne. De är lugna, vänliga hundar med en avslappnad attityd.",
        "temperament": "Bassets är godmodiga, tålmodiga och sällskapliga. De är utmärkta familjehundar och kommer bra överens med barn och andra husdjur. De kan vara envisa men är sällan aggressiva.",
        "health": "Benägen för specifika problem på grund av sin kroppsbyggnad. Vanliga problem inkluderar öroninfektioner, ryggproblem och fetma. Regelbunden öronvård är viktig. Livslängd 10-12 år.",
        "exercise": "Måttliga motionsbehov med dagliga promenader. De gillar att följa doftspår men är inte hyperaktiva. Viktkontroll är viktig för att undvika ryggproblem.",
        "verdict": "Charmerande, lågmälda stövare med fantastiskt luktsinne. Basset Hounds är utmärkta familjehundar men kräver öronvård och viktkontroll."
    },
    "beagle": {
        "meta_description": "Komplett guide till Beagle: temperament, motionsbehov, pälsvård, hälsoproblem och om denna ras passar dig.",
        "hero_desc": "En glad, nyfiken stövare som är perfekt för aktiva familjer.",
        "overview": "Beagle är en av de mest populära hundraserna, känd för sitt vänliga temperament, kompakta storlek och utmärkta luktsinne. De var ursprungligen avlade för harejakt i flock.",
        "temperament": "Beagles är glada, nyfikna och vänliga. De är utmärkta familjehundar och älskar sällskap—de trivs inte med att vara ensamma. Deras starka luktsinne kan leda dem på äventyr om de får chansen.",
        "health": "Generellt frisk med en livslängd på 10-15 år. Vanliga problem inkluderar epilepsi, höftledsdysplasi och ögonsjukdomar. Benägen för fetma om de inte motioneras tillräckligt.",
        "exercise": "Höga motionsbehov med dagliga promenader och lekstunder. De älskar att utforska och följa dofter. En säkert inhägnad trädgård är viktig då de kan strunta i tillkallan om de hittar en intressant doft.",
        "verdict": "Glada, vänliga stövare som älskar sällskap. Beagles är utmärkta familjehundar men behöver motion, sällskap och säkra trädgårdar."
    },
}

def translate_text(text, translations_dict):
    """Translate text using dictionary."""
    if text in translations_dict:
        return translations_dict[text]
    if text.title() in translations_dict:
        return translations_dict[text.title()]
    if text.lower() in translations_dict:
        return translations_dict[text.lower()]
    return text

def apply_translation(sv_html, breed, translation):
    """Apply translation to Swedish HTML."""
    if not translation:
        return sv_html
    
    updated = sv_html
    
    # Replace meta description
    if 'meta_description' in translation:
        old_pattern = r'<meta name="description" content="[^"]*">'
        new_meta = f'<meta name="description" content="{translation["meta_description"]}">'
        updated = re.sub(old_pattern, new_meta, updated)
    
    # Replace hero description
    if 'hero_desc' in translation:
        pattern = r'(<p class="text-lg text-slate-600 mb-6 leading-relaxed">)[^<]*(</p>)'
        updated = re.sub(pattern, rf'\g<1>{translation["hero_desc"]}\2', updated)
    
    # Replace overview
    if 'overview' in translation:
        pattern = r'(<i data-lucide="book-open"[^>]*></i>\s*Översikt.*?<p class="text-slate-600[^"]*">)[^<]*(</p>)'
        updated = re.sub(pattern, rf'\g<1>{translation["overview"]}\2', updated, flags=re.DOTALL)
    
    # Replace temperament section
    if 'temperament' in translation:
        pattern = r'(<i data-lucide="heart"[^>]*></i>\s*Temperament.*?<p class="text-slate-600[^"]*">)[^<]*(</p>)'
        updated = re.sub(pattern, rf'\g<1>{translation["temperament"]}\2', updated, flags=re.DOTALL)
    
    # Replace health section
    if 'health' in translation:
        pattern = r'(<i data-lucide="heart-pulse"[^>]*></i>\s*Hälsa.*?<p class="text-slate-600[^"]*">)[^<]*(</p>)'
        updated = re.sub(pattern, rf'\g<1>{translation["health"]}\2', updated, flags=re.DOTALL)
    
    # Replace exercise section
    if 'exercise' in translation:
        pattern = r'(<i data-lucide="activity"[^>]*></i>\s*Motion.*?<p class="text-slate-600[^"]*">)[^<]*(</p>)'
        updated = re.sub(pattern, rf'\g<1>{translation["exercise"]}\2', updated, flags=re.DOTALL)
    
    # Replace verdict
    if 'verdict' in translation:
        pattern = r'(<strong>Vårt Omdöme:</strong>\s*)[^<]*(</p>)'
        updated = re.sub(pattern, rf'\g<1>{translation["verdict"]}\2', updated)
    
    # Replace Best For items
    def replace_best_for(match):
        original = match.group(1).strip()
        translated = translate_text(original, BEST_FOR)
        return f'<span class="w-2 h-2 mt-2 bg-emerald-500 rounded-full"></span><span>{translated}</span>'
    
    pattern = r'<span class="w-2 h-2 mt-2 bg-emerald-500 rounded-full[^"]*"></span>\s*<span>([^<]+)</span>'
    updated = re.sub(pattern, replace_best_for, updated)
    
    # Replace Not Ideal items
    def replace_not_ideal(match):
        original = match.group(1).strip()
        translated = translate_text(original, NOT_IDEAL)
        return f'<span class="w-2 h-2 mt-2 bg-rose-500 rounded-full"></span><span>{translated}</span>'
    
    pattern = r'<span class="w-2 h-2 mt-2 bg-rose-500 rounded-full[^"]*"></span>\s*<span>([^<]+)</span>'
    updated = re.sub(pattern, replace_not_ideal, updated)
    
    # Replace temperament tags
    def replace_tags(match):
        original = match.group(1).strip()
        translated = translate_text(original, TEMPERAMENT_TAGS)
        return f'from-sky-100 to-blue-100 text-slate-700 px-4 py-2 rounded-full text-sm font-medium">{translated}</span>'
    
    pattern = r'from-sky-100 to-blue-100 text-slate-700 px-4 py-2 rounded-full text-sm font-medium">([^<]+)</span>'
    updated = re.sub(pattern, replace_tags, updated)
    
    return updated

def main():
    breeds = sorted([f.stem for f in SV_BREEDS_DIR.glob("*.html")])
    print(f"Processing {len(breeds)} breeds...")
    
    translated = 0
    for i, breed in enumerate(breeds):
        sv_path = SV_BREEDS_DIR / f"{breed}.html"
        sv_html = sv_path.read_text()
        
        translation = TRANSLATIONS.get(breed, {})
        updated_html = apply_translation(sv_html, breed, translation)
        
        if updated_html != sv_html:
            sv_path.write_text(updated_html)
            translated += 1
            print(f"  [{i+1}/{len(breeds)}] Translated: {breed}")
        else:
            print(f"  [{i+1}/{len(breeds)}] No translation: {breed}")
    
    print(f"\nDone! Translated {translated} breeds.")
    print(f"Translations available for: {len(TRANSLATIONS)} breeds")

if __name__ == "__main__":
    main()
