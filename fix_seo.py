#!/usr/bin/env python3
"""
SEO Fix Script for breedfinder.org
Fixes short/broken meta descriptions and page titles.
"""
import os, re, sys

REPO = os.path.dirname(os.path.abspath(__file__))

# Templates per language. Only languages with templates get fixes.
# {breed} = breed name, {b1}/{b2} = compare breed names
T = {
    'en': {
        'breed_t': '{breed}: Complete Breed Profile & Care Guide | BreedFinder',
        'breed_t_short': '{breed}: Breed Guide, Temperament & Care | BreedFinder',
        'breed_d': 'Discover everything about the {breed} — personality traits, exercise requirements, grooming tips, common health concerns, and how to tell if this loyal breed is the right match for your home.',
        'breed_d_short': 'Learn about the {breed}: temperament, care needs, health, trainability, and whether this popular breed fits your lifestyle and family.',
        'compare_d': '{b1} vs {b2} — compare size, temperament, energy levels, grooming needs, and family suitability side by side to find the ideal breed for you.',
        'quiz_t': 'Dog Breed Quiz — Find Your Perfect Match | BreedFinder',
        'quiz_d': 'Take our free dog breed quiz to discover which of 200+ breeds matches your lifestyle, living space, and activity level. Personalized recommendations in minutes.',
        'search_t': 'Search Dog Breeds by Traits & Characteristics | BreedFinder',
        'search_d': 'Search and filter 200+ dog breeds by size, energy level, grooming needs, family friendliness, and more. Find the perfect dog breed for your lifestyle.',
        'compare_idx_t': 'Compare Dog Breeds Side by Side — Find Your Best Match | BreedFinder',
        'compare_idx_d': 'Compare any two dog breeds side by side on size, temperament, exercise needs, grooming, and family suitability. Make a confident, informed choice.',
        'about_t': 'About BreedFinder — Helping You Find the Perfect Dog Breed',
        'about_d': 'BreedFinder helps dog lovers find their ideal breed with expert guides, interactive quizzes, and side-by-side comparisons for 200+ recognized breeds worldwide.',
        'faq_t': 'Dog Breed FAQ — Common Questions Answered | BreedFinder',
        'faq_d': 'Get clear answers to the most common dog breed questions — from choosing the right breed for your family to understanding exercise needs, grooming, and more.',
        'articles_t': 'Dog Breed Articles & Expert Guides | BreedFinder',
        'articles_d': 'Browse expert articles on dog breeds — best family dogs, apartment-friendly breeds, low-maintenance and hypoallergenic options, and much more.',
    },
    'fi': {
        'breed_t': '{breed} — Rotuopas, Luonne ja Hoito | BreedFinder',
        'breed_d': 'Kattava opas rotuun {breed}: luonne, liikunta, turkinhoito, terveys ja sopivuus perheellesi. Selvitä, onko tämä rotu sinulle oikea valinta.',
        'compare_d': '{b1} vs {b2} — vertaile kokoa, luonnetta, energiatasoa, turkinhoitoa ja perhesopivuutta rinnakkain ja löydä ihanteellinen rotu.',
        'quiz_t': 'Koirarotutesti — Löydä Täydellinen Koirasi | BreedFinder',
        'quiz_d': 'Tee ilmainen koirarotutesti ja löydä yli 200 rodun joukosta sinulle ja elämäntyyliisi parhaiten sopiva koirarotu. Saat henkilökohtaiset suositukset.',
        'search_t': 'Hae Koirarotuja Ominaisuuksien Perusteella | BreedFinder',
        'search_d': 'Hae ja suodata yli 200 koirarotua koon, energiatason, turkinhoitotarpeiden ja perhesopivuuden perusteella. Löydä sinulle sopiva rotu.',
        'compare_idx_t': 'Vertaile Koirarotuja Rinnakkain | BreedFinder',
        'compare_idx_d': 'Vertaile mitä tahansa koirarotuja rinnakkain koon, luonteen, liikuntatarpeiden ja perhesopivuuden perusteella. Tee tietoinen valinta.',
        'about_t': 'Tietoa BreedFinderistä — Tehtävämme ja Yhteystiedot',
        'about_d': 'BreedFinder auttaa koiranystäviä löytämään ihanteellisen rotunsa asiantuntevilla oppailla, interaktiivisilla testeillä ja rotuvertailuilla yli 200 rodulle.',
        'faq_t': 'Koirarodut UKK — Vastauksia Yleisiin Kysymyksiin | BreedFinder',
        'faq_d': 'Selkeät vastaukset yleisimpiin koirarotuja koskeviin kysymyksiin — rodun valinnasta liikuntatarpeisiin, turkinhoitoon ja paljon muuhun.',
    },
    'de': {
        'breed_t': '{breed} — Rasseführer, Charakter & Pflege | BreedFinder',
        'breed_d': 'Umfassender Ratgeber zur Rasse {breed}: Charakter, Bewegungsbedarf, Fellpflege, Gesundheit und ob diese Rasse zu Ihrem Zuhause passt.',
        'compare_d': '{b1} vs {b2} — vergleichen Sie Größe, Charakter, Energieniveau, Pflegebedarf und Familientauglichkeit Seite an Seite.',
        'quiz_t': 'Hunderassen-Quiz — Finden Sie Ihren Perfekten Hund | BreedFinder',
        'quiz_d': 'Machen Sie unser kostenloses Hunderassen-Quiz und finden Sie heraus, welche der über 200 Rassen am besten zu Ihrem Lebensstil und Zuhause passt.',
        'search_t': 'Hunderassen nach Eigenschaften Suchen & Filtern | BreedFinder',
        'search_d': 'Suchen und filtern Sie über 200 Hunderassen nach Größe, Energielevel, Pflegebedarf und Familienfreundlichkeit. Finden Sie Ihre ideale Rasse.',
        'compare_idx_t': 'Hunderassen Vergleichen — Seite an Seite | BreedFinder',
        'compare_idx_d': 'Vergleichen Sie beliebige Hunderassen Seite an Seite nach Größe, Temperament, Bewegungsbedarf und Familienfreundlichkeit.',
        'about_t': 'Über BreedFinder — Unsere Mission und Kontakt | BreedFinder',
        'about_d': 'BreedFinder hilft Hundeliebhabern, ihre ideale Rasse zu finden — mit Expertenführern, interaktiven Quiz und Vergleichen für über 200 Rassen.',
        'faq_t': 'Hunderassen FAQ — Häufig Gestellte Fragen | BreedFinder',
        'faq_d': 'Klare Antworten auf die häufigsten Fragen zu Hunderassen — von der Rassenwahl bis zu Bewegungsbedarf, Pflege und Familientauglichkeit.',
    },
    'es': {
        'breed_t': '{breed} — Guía de Raza, Carácter y Cuidados | BreedFinder',
        'breed_d': 'Guía completa sobre la raza {breed}: carácter, ejercicio, aseo, salud y si esta raza es adecuada para tu hogar y familia. Descúbrelo todo aquí.',
        'compare_d': '{b1} vs {b2} — compara tamaño, temperamento, nivel de energía, necesidades de aseo y compatibilidad familiar lado a lado.',
        'quiz_t': 'Test de Razas de Perros — Encuentra Tu Perro Ideal | BreedFinder',
        'quiz_d': 'Haz nuestro test gratuito de razas caninas y descubre cuál de las más de 200 razas se adapta mejor a tu estilo de vida, hogar y actividad.',
        'search_t': 'Buscar Razas de Perros por Características | BreedFinder',
        'search_d': 'Busca y filtra más de 200 razas de perros por tamaño, nivel de energía, necesidades de aseo y compatibilidad familiar para encontrar tu raza.',
        'compare_idx_t': 'Comparar Razas de Perros Lado a Lado | BreedFinder',
        'compare_idx_d': 'Compara cualquier par de razas de perros lado a lado por tamaño, temperamento, ejercicio y compatibilidad familiar. Toma una decisión informada.',
        'about_t': 'Sobre BreedFinder — Nuestra Misión y Contacto | BreedFinder',
        'about_d': 'BreedFinder ayuda a los amantes de los perros a encontrar su raza ideal con guías expertas, cuestionarios interactivos y comparaciones de más de 200 razas.',
        'faq_t': 'Preguntas Frecuentes sobre Razas de Perros | BreedFinder',
        'faq_d': 'Respuestas claras a las preguntas más comunes sobre razas de perros — desde elegir la raza correcta hasta necesidades de ejercicio y cuidados.',
    },
    'fr': {
        'breed_t': '{breed} — Guide de Race, Caractère & Soins | BreedFinder',
        'breed_d': 'Guide complet sur la race {breed} : caractère, besoins en exercice, toilettage, santé et compatibilité avec votre foyer et votre famille.',
        'compare_d': '{b1} vs {b2} — comparez taille, tempérament, énergie, toilettage et compatibilité familiale côte à côte pour trouver la race idéale.',
        'quiz_t': 'Quiz Races de Chiens — Trouvez Votre Compagnon Idéal | BreedFinder',
        'quiz_d': 'Faites notre quiz gratuit sur les races de chiens et découvrez laquelle des 200+ races correspond le mieux à votre mode de vie et votre foyer.',
        'search_t': 'Rechercher des Races de Chiens par Caractéristiques | BreedFinder',
        'search_d': 'Recherchez et filtrez plus de 200 races de chiens par taille, énergie, toilettage et compatibilité familiale. Trouvez votre race idéale.',
        'compare_idx_t': 'Comparer des Races de Chiens Côte à Côte | BreedFinder',
        'compare_idx_d': 'Comparez deux races de chiens côte à côte par taille, tempérament, exercice et compatibilité familiale pour faire un choix éclairé.',
        'about_t': 'À Propos de BreedFinder — Notre Mission et Contact | BreedFinder',
        'about_d': 'BreedFinder aide les amoureux des chiens à trouver leur race idéale grâce à des guides experts, des quiz et des comparaisons de plus de 200 races.',
        'faq_t': 'FAQ Races de Chiens — Questions Fréquentes | BreedFinder',
        'faq_d': 'Réponses claires aux questions les plus courantes sur les races de chiens — du choix de race aux besoins en exercice, toilettage et bien plus.',
    },
    'it': {
        'breed_t': '{breed} — Guida alla Razza, Carattere e Cure | BreedFinder',
        'breed_d': 'Guida completa alla razza {breed}: carattere, esercizio fisico, toelettatura, salute e se questa razza è adatta alla tua famiglia e al tuo stile di vita.',
        'compare_d': '{b1} vs {b2} — confronta taglia, temperamento, livello di energia, toelettatura e compatibilità familiare fianco a fianco.',
        'quiz_t': 'Quiz Razze Canine — Trova il Tuo Cane Ideale | BreedFinder',
        'quiz_d': 'Fai il nostro quiz gratuito sulle razze canine e scopri quale delle oltre 200 razze si adatta meglio al tuo stile di vita e alla tua casa.',
        'search_t': 'Cerca Razze di Cani per Caratteristiche | BreedFinder',
        'search_d': 'Cerca e filtra oltre 200 razze canine per taglia, energia, toelettatura e compatibilità familiare. Trova la razza perfetta per te.',
        'compare_idx_t': 'Confronta Razze di Cani Fianco a Fianco | BreedFinder',
        'compare_idx_d': 'Confronta qualsiasi coppia di razze canine fianco a fianco per taglia, temperamento, esercizio e compatibilità familiare.',
        'about_t': 'Chi Siamo — La Missione di BreedFinder | BreedFinder',
        'about_d': 'BreedFinder aiuta gli amanti dei cani a trovare la razza ideale con guide esperte, quiz interattivi e confronti per oltre 200 razze riconosciute.',
        'faq_t': 'FAQ Razze Canine — Domande Frequenti | BreedFinder',
        'faq_d': 'Risposte chiare alle domande più comuni sulle razze canine — dalla scelta della razza alle esigenze di esercizio, toelettatura e altro ancora.',
    },
    'pt': {
        'breed_t': '{breed} — Guia da Raça, Temperamento e Cuidados | BreedFinder',
        'breed_d': 'Guia completo sobre a raça {breed}: temperamento, exercício, higiene, saúde e se esta raça é ideal para sua casa e família. Descubra tudo aqui.',
        'compare_d': '{b1} vs {b2} — compare tamanho, temperamento, nível de energia, necessidades de higiene e adequação familiar lado a lado.',
        'quiz_t': 'Teste de Raças de Cães — Encontre Seu Cão Perfeito | BreedFinder',
        'quiz_d': 'Faça nosso teste gratuito de raças caninas e descubra qual das mais de 200 raças combina melhor com seu estilo de vida, lar e rotina.',
        'search_t': 'Buscar Raças de Cães por Características | BreedFinder',
        'search_d': 'Busque e filtre mais de 200 raças de cães por tamanho, nível de energia, necessidades de higiene e compatibilidade familiar.',
        'compare_idx_t': 'Comparar Raças de Cães Lado a Lado | BreedFinder',
        'compare_idx_d': 'Compare qualquer par de raças de cães lado a lado por tamanho, temperamento, exercício e compatibilidade familiar. Faça uma escolha informada.',
        'about_t': 'Sobre o BreedFinder — Nossa Missão e Contato | BreedFinder',
        'about_d': 'O BreedFinder ajuda amantes de cães a encontrar sua raça ideal com guias especializados, quizzes interativos e comparações de mais de 200 raças.',
        'faq_t': 'FAQ sobre Raças de Cães — Perguntas Frequentes | BreedFinder',
        'faq_d': 'Respostas claras para as perguntas mais comuns sobre raças de cães — da escolha da raça às necessidades de exercício, higiene e muito mais.',
    },
    'nl': {
        'breed_t': '{breed} — Rassenwijzer, Karakter & Verzorging | BreedFinder',
        'breed_d': 'Complete gids over het ras {breed}: karakter, bewegingsbehoefte, vachtverzorging, gezondheid en of dit ras bij uw gezin en levensstijl past.',
        'compare_d': '{b1} vs {b2} — vergelijk grootte, temperament, energieniveau, vachtverzorging en gezinsvriendelijkheid naast elkaar.',
        'quiz_t': 'Hondenras Quiz — Vind Uw Ideale Hond | BreedFinder',
        'quiz_d': 'Doe onze gratis hondenras quiz en ontdek welke van de 200+ rassen het beste past bij uw levensstijl, woonsituatie en activiteitenniveau.',
        'search_t': 'Zoek Hondenrassen op Eigenschappen en Kenmerken | BreedFinder',
        'search_d': 'Zoek en filter meer dan 200 hondenrassen op grootte, energieniveau, vachtverzorging en gezinsvriendelijkheid. Vind uw ideale ras.',
        'compare_idx_t': 'Vergelijk Hondenrassen Naast Elkaar | BreedFinder',
        'compare_idx_d': 'Vergelijk elk paar hondenrassen naast elkaar op grootte, temperament, beweging en gezinsvriendelijkheid. Maak een weloverwogen keuze.',
        'about_t': 'Over BreedFinder — Onze Missie en Contact | BreedFinder',
        'about_d': 'BreedFinder helpt hondenliefhebbers hun ideale ras te vinden met expertgidsen, interactieve quizzen en vergelijkingen voor meer dan 200 rassen.',
        'faq_t': 'Hondenrassen FAQ — Veelgestelde Vragen | BreedFinder',
        'faq_d': 'Duidelijke antwoorden op de meest gestelde vragen over hondenrassen — van raskeuze tot bewegingsbehoefte, verzorging en meer.',
    },
    'ja': {
        'breed_t': '{breed} — 犬種ガイド・性格・飼い方 | BreedFinder',
        'breed_d': '{breed}の完全ガイド：性格、運動量、被毛の手入れ、健康上の注意点、そしてこの犬種があなたの家庭に合っているかを詳しく解説します。',
        'compare_d': '{b1}と{b2}の比較 — 体格、性格、運動量、被毛の手入れ、家族との相性を並べて比較。あなたに合った犬種を見つけましょう。',
        'quiz_t': '犬種診断クイズ — あなたにぴったりの犬種を発見 | BreedFinder',
        'quiz_d': '無料の犬種診断クイズで、200以上の犬種からあなたのライフスタイル、住環境、活動レベルに合った犬種を見つけましょう。',
        'search_t': '特徴から犬種を検索・フィルタリング | BreedFinder',
        'search_d': '200以上の犬種をサイズ、エネルギーレベル、被毛の手入れ、家族との相性で検索・フィルタリング。理想の犬種を見つけましょう。',
        'compare_idx_t': '犬種を並べて比較 — あなたに合った犬種を発見 | BreedFinder',
        'compare_idx_d': '任意の犬種ペアを体格、性格、運動量、家族との相性で並べて比較。自信を持って犬種を選びましょう。',
        'about_t': 'BreedFinderについて — 私たちのミッション | BreedFinder',
        'about_d': 'BreedFinderは犬好きの方が理想の犬種を見つけるお手伝いをします。専門家ガイド、インタラクティブクイズ、200以上の犬種の比較を提供。',
        'faq_t': '犬種FAQ — よくある質問と回答 | BreedFinder',
        'faq_d': '犬種に関するよくある質問に明確に回答します。犬種の選び方から運動量、被毛の手入れ、家族との相性まで幅広くカバー。',
    },
    'pl': {
        'breed_t': '{breed} — Przewodnik po Rasie, Charakter i Opieka | BreedFinder',
        'breed_d': 'Kompletny przewodnik po rasie {breed}: charakter, potrzeby ruchowe, pielęgnacja, zdrowie i czy ta rasa jest odpowiednia dla Twojego domu i rodziny.',
        'compare_d': '{b1} vs {b2} — porównaj rozmiar, temperament, poziom energii, pielęgnację i przyjazność rodzinną obok siebie.',
        'quiz_t': 'Quiz o Rasach Psów — Znajdź Idealnego Psa | BreedFinder',
        'quiz_d': 'Rozwiąż nasz darmowy quiz o rasach psów i odkryj, która z ponad 200 ras najlepiej pasuje do Twojego stylu życia, domu i aktywności.',
        'search_t': 'Szukaj Ras Psów według Cech i Właściwości | BreedFinder',
        'search_d': 'Szukaj i filtruj ponad 200 ras psów według rozmiaru, poziomu energii, pielęgnacji i przyjazności rodzinnej. Znajdź idealną rasę.',
        'compare_idx_t': 'Porównaj Rasy Psów Obok Siebie | BreedFinder',
        'compare_idx_d': 'Porównaj dowolną parę ras psów obok siebie pod względem rozmiaru, temperamentu, ćwiczeń i przyjazności rodzinnej.',
        'about_t': 'O BreedFinder — Nasza Misja i Kontakt | BreedFinder',
        'about_d': 'BreedFinder pomaga miłośnikom psów znaleźć idealną rasę dzięki poradnikom ekspertów, interaktywnym quizom i porównaniom ponad 200 ras.',
        'faq_t': 'FAQ o Rasach Psów — Najczęściej Zadawane Pytania | BreedFinder',
        'faq_d': 'Jasne odpowiedzi na najczęstsze pytania o rasach psów — od wyboru rasy po potrzeby ruchowe, pielęgnację i wiele więcej.',
    },
    'da': {
        'breed_t': '{breed} — Raceguide, Temperament & Pleje | BreedFinder',
        'breed_d': 'Komplet guide til racen {breed}: temperament, motionsbehov, pelspleje, sundhed og om denne race passer til dit hjem og din familie.',
        'compare_d': '{b1} vs {b2} — sammenlign størrelse, temperament, energiniveau, pelspleje og familievenlighed side om side.',
        'quiz_t': 'Hunderace-Quiz — Find Din Perfekte Hund | BreedFinder',
        'quiz_d': 'Tag vores gratis hunderace quiz og find ud af, hvilken af 200+ racer der passer bedst til din livsstil, bolig og aktivitetsniveau.',
        'search_t': 'Søg Hunderacer efter Egenskaber og Kendetegn | BreedFinder',
        'search_d': 'Søg og filtrer over 200 hunderacer efter størrelse, energiniveau, pelspleje og familievenlighed. Find den perfekte race for dig.',
        'compare_idx_t': 'Sammenlign Hunderacer Side om Side | BreedFinder',
        'compare_idx_d': 'Sammenlign ethvert par hunderacer side om side efter størrelse, temperament, motion og familievenlighed. Træf et informeret valg.',
        'about_t': 'Om BreedFinder — Vores Mission og Kontakt | BreedFinder',
        'about_d': 'BreedFinder hjælper hundeelskere med at finde deres ideelle race med ekspertguider, interaktive quizzer og sammenligninger af over 200 racer.',
        'faq_t': 'Hunderacer FAQ — Ofte Stillede Spørgsmål | BreedFinder',
        'faq_d': 'Klare svar på de mest stillede spørgsmål om hunderacer — fra racevalg til motionsbehov, pelspleje og meget mere.',
    },
    'no': {
        'breed_t': '{breed} — Raseguide, Temperament & Stell | BreedFinder',
        'breed_d': 'Komplett guide til rasen {breed}: temperament, mosjonsbehov, pelsstell, helse og om denne rasen passer for ditt hjem og din familie.',
        'compare_d': '{b1} vs {b2} — sammenlign størrelse, temperament, energinivå, pelsstell og familievennlighet side ved side.',
        'quiz_t': 'Hunderase-Quiz — Finn Din Perfekte Hund | BreedFinder',
        'quiz_d': 'Ta vår gratis hunderase quiz og finn ut hvilken av 200+ raser som passer best til din livsstil, bolig og aktivitetsnivå.',
        'search_t': 'Søk Hunderaser etter Egenskaper og Kjennetegn | BreedFinder',
        'search_d': 'Søk og filtrer over 200 hunderaser etter størrelse, energinivå, pelsstell og familievennlighet. Finn den perfekte rasen for deg.',
        'compare_idx_t': 'Sammenlign Hunderaser Side ved Side | BreedFinder',
        'compare_idx_d': 'Sammenlign ethvert par hunderaser side ved side etter størrelse, temperament, mosjon og familievennlighet. Ta et informert valg.',
        'about_t': 'Om BreedFinder — Vårt Oppdrag og Kontakt | BreedFinder',
        'about_d': 'BreedFinder hjelper hundeelskere med å finne sin ideelle rase med ekspertguider, interaktive quizer og sammenligninger av over 200 raser.',
        'faq_t': 'Hunderaser FAQ — Vanlige Spørsmål | BreedFinder',
        'faq_d': 'Klare svar på de vanligste spørsmålene om hunderaser — fra rasevalg til mosjonsbehov, pelsstell og mye mer.',
    },
    'sv': {
        'breed_t': '{breed} — Rasguide, Temperament & Skötsel | BreedFinder',
        'breed_d': 'Komplett guide till rasen {breed}: temperament, motionsbehov, pälsvård, hälsa och om denna ras passar för ditt hem och din familj.',
        'compare_d': '{b1} vs {b2} — jämför storlek, temperament, energinivå, pälsvård och familjevänlighet sida vid sida.',
        'quiz_t': 'Hundras-Quiz — Hitta Din Perfekta Hund | BreedFinder',
        'quiz_d': 'Gör vårt gratis hundras quiz och ta reda på vilken av 200+ raser som passar bäst för din livsstil, boende och aktivitetsnivå.',
        'search_t': 'Sök Hundraser efter Egenskaper och Karaktärsdrag | BreedFinder',
        'search_d': 'Sök och filtrera över 200 hundraser efter storlek, energinivå, pälsvård och familjevänlighet. Hitta den perfekta rasen för dig.',
        'compare_idx_t': 'Jämför Hundraser Sida vid Sida | BreedFinder',
        'compare_idx_d': 'Jämför valfritt par hundraser sida vid sida efter storlek, temperament, motion och familjevänlighet. Gör ett välgrundat val.',
        'about_t': 'Om BreedFinder — Vårt Uppdrag och Kontakt | BreedFinder',
        'about_d': 'BreedFinder hjälper hundälskare att hitta sin idealiska ras med expertguider, interaktiva quiz och jämförelser för över 200 raser.',
        'faq_t': 'Hundraser FAQ — Vanliga Frågor | BreedFinder',
        'faq_d': 'Tydliga svar på de vanligaste frågorna om hundraser — från rasval till motionsbehov, pälsvård och mycket mer.',
    },
    'ru': {
        'breed_t': '{breed} — Гид по Породе, Характер и Уход | BreedFinder',
        'breed_d': 'Полное руководство по породе {breed}: характер, физические нагрузки, уход за шерстью, здоровье и подходит ли эта порода вашей семье и образу жизни.',
        'compare_d': '{b1} vs {b2} — сравните размер, темперамент, уровень энергии, уход и дружелюбность к семье бок о бок.',
        'quiz_t': 'Тест на Породу Собаки — Найдите Идеальную Собаку | BreedFinder',
        'quiz_d': 'Пройдите наш бесплатный тест на породу собаки и узнайте, какая из 200+ пород лучше всего подходит для вашего образа жизни и жилья.',
        'search_t': 'Поиск Пород Собак по Характеристикам | BreedFinder',
        'search_d': 'Ищите и фильтруйте более 200 пород собак по размеру, уровню энергии, уходу и дружелюбности к семье. Найдите идеальную породу.',
        'compare_idx_t': 'Сравните Породы Собак Бок о Бок | BreedFinder',
        'compare_idx_d': 'Сравните любую пару пород собак бок о бок по размеру, темпераменту, физическим нагрузкам и семейной совместимости.',
        'about_t': 'О BreedFinder — Наша Миссия и Контакты | BreedFinder',
        'about_d': 'BreedFinder помогает любителям собак найти идеальную породу с помощью экспертных руководств, интерактивных тестов и сравнений более 200 пород.',
        'faq_t': 'FAQ о Породах Собак — Частые Вопросы | BreedFinder',
        'faq_d': 'Четкие ответы на самые частые вопросы о породах собак — от выбора породы до потребностей в физических нагрузках, уходе и многом другом.',
    },
    'tr': {
        'breed_t': '{breed} — Irk Rehberi, Karakter ve Bakım | BreedFinder',
        'breed_d': '{breed} ırkı hakkında kapsamlı rehber: karakter, egzersiz ihtiyaçları, tüy bakımı, sağlık ve bu ırkın evinize ve ailenize uygun olup olmadığı.',
        'compare_d': '{b1} vs {b2} — boyut, mizaç, enerji seviyesi, bakım ve aile uygunluğunu yan yana karşılaştırın. İdeal ırkınızı bulun.',
        'quiz_t': 'Köpek Irkı Testi — Mükemmel Köpeğinizi Bulun | BreedFinder',
        'quiz_d': 'Ücretsiz köpek ırkı testimizi yapın ve 200+ ırk arasından yaşam tarzınıza, evinize ve aktivite düzeyinize en uygun olanı keşfedin.',
        'search_t': 'Özelliklere Göre Köpek Irkı Arama ve Filtreleme | BreedFinder',
        'search_d': '200+ köpek ırkını boyut, enerji seviyesi, bakım ihtiyaçları ve aile uygunluğuna göre arayın ve filtreleyin. İdeal ırkınızı bulun.',
        'compare_idx_t': 'Köpek Irklarını Yan Yana Karşılaştırın | BreedFinder',
        'compare_idx_d': 'Herhangi iki köpek ırkını boyut, mizaç, egzersiz ve aile uygunluğuna göre yan yana karşılaştırın. Bilinçli bir seçim yapın.',
        'about_t': 'BreedFinder Hakkında — Misyonumuz ve İletişim | BreedFinder',
        'about_d': 'BreedFinder, köpek severlerin uzman rehberler, interaktif testler ve 200+ ırk karşılaştırması ile ideal ırkı bulmalarına yardımcı olur.',
        'faq_t': 'Köpek Irkları SSS — Sık Sorulan Sorular | BreedFinder',
        'faq_d': 'Köpek ırkları hakkında en sık sorulan sorulara net yanıtlar — ırk seçiminden egzersiz ihtiyaçlarına, bakıma ve çok daha fazlasına.',
    },
    'zh': {
        'breed_t': '{breed} — 品种指南、性格与护理 | BreedFinder',
        'breed_d': '{breed}完全指南：了解性格特点、运动需求、毛发护理、健康注意事项，以及这个品种是否适合你的家庭和生活方式。',
        'compare_d': '{b1}与{b2}对比 — 并排比较体型、性格、精力水平、护理需求和家庭适合度，找到理想的犬种。',
        'quiz_t': '犬种测试 — 找到你的完美狗狗 | BreedFinder',
        'quiz_d': '参加我们的免费犬种测试，从200多个品种中找到最适合你生活方式、住房条件和活动水平的犬种。',
        'search_t': '按特征搜索和筛选犬种 | BreedFinder',
        'search_d': '按体型、精力水平、护理需求和家庭适合度搜索和筛选200多个犬种。找到最适合你的品种。',
        'compare_idx_t': '并排比较犬种 — 找到最佳匹配 | BreedFinder',
        'compare_idx_d': '将任意两个犬种并排比较体型、性格、运动量和家庭适合度，做出明智的选择。',
        'about_t': '关于BreedFinder — 我们的使命与联系方式 | BreedFinder',
        'about_d': 'BreedFinder通过专家指南、互动测试和200多个犬种的比较，帮助爱犬人士找到理想的品种。',
        'faq_t': '犬种常见问题解答 | BreedFinder',
        'faq_d': '关于犬种的常见问题的清晰解答 — 从品种选择到运动需求、护理等方方面面。',
    },
}

title_re = re.compile(r'<title>(.*?)</title>', re.DOTALL)
desc_re = re.compile(r'(<meta\s+name=["\x27]description["\x27]\s+content=["\x27])(.*?)(["\x27]\s*/?>)', re.DOTALL)

def breed_name_from_title(title):
    for sep in [': ', ' — ', ' - ', ' | ']:
        if sep in title:
            return title.split(sep)[0].strip()
    return title.replace(' | BreedFinder', '').strip()

def compare_breeds_from_title(title):
    m = re.match(r'(.+?)\s+vs\.?\s+(.+?)(?:\s*[:|—\-])', title)
    if m: return m.group(1).strip(), m.group(2).strip()
    m = re.match(r'(.+?)\s+vs\.?\s+(.+?)$', title.split(' | ')[0] if ' | ' in title else title)
    if m: return m.group(1).strip(), m.group(2).strip()
    return None, None

def get_lang(path):
    parts = path.replace('\\', '/').split('/')
    for lc in T.keys():
        if lc != 'en' and lc in parts:
            return lc
    return 'en'

def get_page_type(path):
    if '/breeds/' in path: return 'breed'
    if '/compare/comparisons/' in path: return 'compare'
    if '/compare/' in path: return 'compare_idx'
    if '/faq/' in path: return 'faq'
    if '/about/' in path: return 'about'
    if '/quiz/' in path: return 'quiz'
    if '/search/' in path: return 'search'
    if '/articles/' in path:
        # Distinguish article index from individual articles
        after = path.split('/articles/')[-1]
        if after in ('index.html', 'index/index.html', '') or after.startswith('index'):
            return 'articles_idx'
        return 'article'
    return 'other'

def get_tmpl(lang, key):
    """Get template for language, returns None if not available (never falls back to English for non-EN)"""
    cfg = T.get(lang, {})
    return cfg.get(key)

def process_file(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    if 'http-equiv="refresh"' in content[:500]:
        return None
    
    lang = get_lang(path)
    ptype = get_page_type(path)
    
    tm = title_re.search(content)
    if not tm: return None
    old_title = tm.group(1).strip()
    
    dm = desc_re.search(content)
    old_desc = dm.group(2).strip() if dm else ''
    
    new_title = old_title
    new_desc = old_desc
    title_changed = False
    desc_changed = False
    
    breed = breed_name_from_title(old_title)
    
    # === FIX TITLE ===
    if len(old_title) < 50:
        tmpl = None
        if ptype == 'breed':
            tmpl = get_tmpl(lang, 'breed_t')
        elif ptype == 'quiz':
            tmpl = get_tmpl(lang, 'quiz_t')
        elif ptype == 'search':
            tmpl = get_tmpl(lang, 'search_t')
        elif ptype == 'compare_idx':
            tmpl = get_tmpl(lang, 'compare_idx_t')
        elif ptype == 'about':
            tmpl = get_tmpl(lang, 'about_t')
        elif ptype == 'faq':
            tmpl = get_tmpl(lang, 'faq_t')
        elif ptype == 'articles_idx':
            tmpl = get_tmpl(lang, 'articles_t')
        
        if tmpl and ptype == 'breed':
            candidate = tmpl.format(breed=breed)
            # For very long breed names, try the short variant 
            if len(candidate) > 70 and lang == 'en':
                short = get_tmpl('en', 'breed_t_short')
                if short:
                    candidate = short.format(breed=breed)
            new_title = candidate
            title_changed = True
        elif tmpl:
            new_title = tmpl
            title_changed = True
    
    # === FIX DESCRIPTION ===
    needs_desc_fix = (len(old_desc) < 120) or (len(old_desc) > 165)
    
    if ptype == 'breed' and needs_desc_fix:
        tmpl = get_tmpl(lang, 'breed_d')
        if tmpl:
            candidate = tmpl.format(breed=breed)
            # If too long, try short variant (EN only)
            if len(candidate) > 165 and lang == 'en':
                short = get_tmpl('en', 'breed_d_short')
                if short:
                    candidate = short.format(breed=breed)
            if len(candidate) > 165:
                candidate = candidate[:160] + '...'
            new_desc = candidate
            desc_changed = True
    
    elif ptype == 'compare' and len(old_desc) < 120:
        b1, b2 = compare_breeds_from_title(old_title)
        tmpl = get_tmpl(lang, 'compare_d')
        if b1 and b2 and tmpl:
            candidate = tmpl.format(b1=b1, b2=b2)
            if len(candidate) > 165:
                candidate = candidate[:160] + '...'
            new_desc = candidate
            desc_changed = True
    
    elif ptype in ('quiz', 'search', 'compare_idx', 'about', 'faq', 'articles_idx') and len(old_desc) < 120:
        key = ptype + '_d'
        tmpl = get_tmpl(lang, key)
        if tmpl:
            new_desc = tmpl
            desc_changed = True
    
    if not title_changed and not desc_changed:
        return None
    
    new_content = content
    
    if title_changed:
        new_content = new_content.replace(
            '<title>' + tm.group(1) + '</title>',
            '<title>' + new_title + '</title>',
            1
        )
        # Update og:title too
        og_re = re.compile(r'(<meta\s+property=["\x27]og:title["\x27]\s+content=["\x27])(.*?)(["\x27]\s*/?>)')
        og_m = og_re.search(new_content)
        if og_m:
            og_val = new_title.rsplit(' | BreedFinder', 1)[0]
            new_content = new_content[:og_m.start()] + og_m.group(1) + og_val + og_m.group(3) + new_content[og_m.end():]
    
    if desc_changed:
        if dm:
            # Find desc tag again in potentially modified content
            dm2 = desc_re.search(new_content)
            if dm2:
                new_content = new_content[:dm2.start()] + dm2.group(1) + new_desc + dm2.group(3) + new_content[dm2.end():]
        else:
            # Insert meta desc after title
            title_end = new_content.find('</title>') + len('</title>')
            new_content = new_content[:title_end] + '\n    <meta name="description" content="' + new_desc + '">' + new_content[title_end:]
        
        # Update og:description too if short
        og_d_re = re.compile(r'(<meta\s+property=["\x27]og:description["\x27]\s+content=["\x27])(.*?)(["\x27]\s*/?>)')
        og_dm = og_d_re.search(new_content)
        if og_dm and len(og_dm.group(2).strip()) < 100:
            new_content = new_content[:og_dm.start()] + og_dm.group(1) + new_desc + og_dm.group(3) + new_content[og_dm.end():]
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return {
        'path': os.path.relpath(path, REPO),
        'title_changed': title_changed,
        'desc_changed': desc_changed,
        'old_title': old_title,
        'new_title': new_title,
        'old_desc': old_desc,
        'new_desc': new_desc,
    }


def main():
    files_changed = 0
    titles_fixed = 0
    descs_fixed = 0
    examples_by_lang = {}
    
    for root, dirs, files in os.walk(REPO):
        if '.git' in root: continue
        for f in files:
            if not f.endswith('.html'): continue
            path = os.path.join(root, f)
            result = process_file(path)
            if result:
                files_changed += 1
                lang = get_lang(path)
                if result['title_changed']: titles_fixed += 1
                if result['desc_changed']: descs_fixed += 1
                if lang not in examples_by_lang:
                    examples_by_lang[lang] = []
                if len(examples_by_lang[lang]) < 3:
                    examples_by_lang[lang].append(result)
    
    print(f'\n=== SEO FIX RESULTS ===')
    print(f'Total files changed: {files_changed}')
    print(f'Titles improved: {titles_fixed}')
    print(f'Descriptions improved: {descs_fixed}')
    
    for lang in sorted(examples_by_lang.keys()):
        print(f'\n--- {lang.upper()} examples ---')
        for ex in examples_by_lang[lang]:
            print(f'  {ex["path"]}:')
            if ex['title_changed']:
                print(f'    TITLE [{len(ex["old_title"])}→{len(ex["new_title"])}]: "{ex["old_title"]}" → "{ex["new_title"]}"')
            if ex['desc_changed']:
                od = ex["old_desc"][:60] + '...' if len(ex["old_desc"]) > 60 else ex["old_desc"]
                nd = ex["new_desc"][:60] + '...' if len(ex["new_desc"]) > 60 else ex["new_desc"]
                print(f'    DESC  [{len(ex["old_desc"])}→{len(ex["new_desc"])}]: "{od}" → "{nd}"')

if __name__ == '__main__':
    main()
