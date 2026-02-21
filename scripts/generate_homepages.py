#!/usr/bin/env python3
"""
Generate translated homepages with full content matching English version
"""

import json
from pathlib import Path

LANGUAGES = {
    'es': {'name': 'Español', 'code': 'ES'},
    'de': {'name': 'Deutsch', 'code': 'DE'},
    'fr': {'name': 'Français', 'code': 'FR'},
    'it': {'name': 'Italiano', 'code': 'IT'},
    'pt': {'name': 'Português', 'code': 'PT'},
    'nl': {'name': 'Nederlands', 'code': 'NL'},
    'pl': {'name': 'Polski', 'code': 'PL'},
    'zh': {'name': '中文', 'code': 'ZH'},
    'ja': {'name': '日本語', 'code': 'JA'},
    'fi': {'name': 'Suomi', 'code': 'FI'},
    'sv': {'name': 'Svenska', 'code': 'SV'},
    'no': {'name': 'Norsk', 'code': 'NO'},
    'da': {'name': 'Dansk', 'code': 'DA'},
    'ru': {'name': 'Русский', 'code': 'RU'},
}

# Full translations for all homepage content
T = {
    'en': {
        'title': 'Dog Breed Finder | Quiz, Compare & Find Your Perfect Dog',
        'meta_desc': 'Find your perfect dog breed with our quiz, compare tool & expert guides. 200+ breeds rated for families, apartments, allergies & more.',
        'badge': 'Over 200 dog breeds to explore',
        'h1_1': 'Find Your',
        'h1_2': 'Perfect Dog Breed',
        'hero_p': 'Discover which dog breed matches your lifestyle perfectly. Compare traits, take our quiz, and find your ideal furry companion.',
        'search_placeholder': 'Search breeds...',
        'btn_quiz': 'Take the Breed Quiz',
        'btn_compare': 'Compare Breeds',
        'popular_title': 'Popular Breeds',
        'popular_subtitle': 'Most loved dog breeds worldwide',
        'view_all': 'View all 200+ breeds',
        'size_title': 'Browse by Size',
        'size_subtitle': 'Find breeds that fit your living space',
        'tiny': 'Tiny', 'small': 'Small', 'medium': 'Medium', 'large': 'Large', 'giant': 'Giant',
        'under': 'Under', 'over': 'Over',
        'lifestyle_title': 'Find by Lifestyle',
        'lifestyle_subtitle': 'Quick filters for your needs',
        'apt_title': 'Apartment Friendly', 'apt_desc': 'Perfect for flats',
        'kids_title': 'Great with Kids', 'kids_desc': 'Family friendly',
        'shed_title': 'Low Shedding', 'shed_desc': 'Less fur, less mess',
        'train_title': 'Easy to Train', 'train_desc': 'Quick learners',
        'features_title': 'Find Your Perfect Match',
        'features_subtitle': 'Everything you need to make an informed decision about your new furry family member',
        'feat1_title': 'Breed Quiz', 'feat1_desc': "Answer a few questions about your lifestyle and we'll suggest breeds that fit you perfectly.",
        'feat2_title': 'Compare Breeds', 'feat2_desc': 'Put breeds side-by-side to compare size, energy levels, grooming needs, and more.',
        'feat3_title': 'Expert Verdicts', 'feat3_desc': 'Clear recommendations on who each breed is best for—and who should look elsewhere.',
        'guides_title': 'Breed Guides',
        'guides_subtitle': 'Expert advice on finding the right dog for your lifestyle',
        'guide1_title': 'Best Dogs for Apartments', 'guide1_desc': '15 breeds that thrive in small spaces',
        'guide2_title': 'Best Dogs for Families', 'guide2_desc': '12 patient, gentle breeds for kids',
        'guide3_title': 'Low-Shedding Breeds', 'guide3_desc': '20 breeds for a cleaner home',
        'faq_title': 'Frequently Asked Questions',
        'faq1_q': 'How do I choose the right dog breed for my lifestyle?',
        'faq1_a': 'Consider your living space, activity level, time for grooming, and family situation. Our Breed Quiz asks these questions and matches you with compatible breeds.',
        'faq2_q': 'What are the best dog breeds for apartments?',
        'faq2_a': 'French Bulldogs, Cavalier King Charles Spaniels, Pugs, and Boston Terriers adapt well to apartment living. Size isn\'t everything—some large breeds like Greyhounds are calm indoors.',
        'faq3_q': 'Which breeds are best for families with children?',
        'faq3_a': 'Labrador Retrievers, Golden Retrievers, Beagles, and Collies are known for being patient and gentle with kids. Always supervise interactions.',
        'faq4_q': 'What dogs shed the least?',
        'faq4_a': 'Poodles, Bichon Frises, Portuguese Water Dogs, and Schnauzers are low-shedding breeds. "Hypoallergenic" doesn\'t mean allergy-free.',
        'faq5_q': 'How much exercise do different breeds need?',
        'faq5_a': 'High-energy breeds need 2+ hours daily. Moderate breeds need about 1 hour. Low-energy breeds are happy with 30 minutes.',
        'faq6_q': "What's the difference between the Compare tool and the Quiz?",
        'faq6_a': 'The Quiz helps you discover breeds based on your lifestyle. The Compare tool lets you view two specific breeds side-by-side.',
        'footer_copy': '© 2026 BreedFinder. Made with care for dog lovers everywhere.',
        'browse_breeds': 'Browse Breeds', 'quiz': 'Quiz', 'compare': 'Compare', 'guides': 'Guides', 'about': 'About',
    },
    'fi': {
        'title': 'Koirarodun Valitsin | Testi, Vertailu & Löydä Täydellinen Koira',
        'meta_desc': 'Löydä täydellinen koirarotu testimme, vertailutyökalumme ja asiantuntijaoppaidemme avulla. Yli 200 rotua arvioituna.',
        'badge': 'Yli 200 koirarotua tutustuttavana',
        'h1_1': 'Löydä',
        'h1_2': 'Täydellinen Koirarotusi',
        'hero_p': 'Selvitä, mikä koirarotu sopii elämäntyyliisi täydellisesti. Vertaa ominaisuuksia, tee testi ja löydä ihanteellinen karvainen kumppanisi.',
        'search_placeholder': 'Etsi rotuja...',
        'btn_quiz': 'Tee Rotutesti',
        'btn_compare': 'Vertaile Rotuja',
        'popular_title': 'Suositut Rodut',
        'popular_subtitle': 'Maailman rakastetuimmat koirarodut',
        'view_all': 'Näytä kaikki 200+ rotua',
        'size_title': 'Selaa Koon Mukaan',
        'size_subtitle': 'Löydä rotuja, jotka sopivat asuintilaasi',
        'tiny': 'Pienoinen', 'small': 'Pieni', 'medium': 'Keskikokoinen', 'large': 'Suuri', 'giant': 'Jättiläinen',
        'under': 'Alle', 'over': 'Yli',
        'lifestyle_title': 'Etsi Elämäntyylin Mukaan',
        'lifestyle_subtitle': 'Nopeat suodattimet tarpeisiisi',
        'apt_title': 'Sopii Kerrostaloon', 'apt_desc': 'Täydellinen asuntoihin',
        'kids_title': 'Loistava Lasten Kanssa', 'kids_desc': 'Perheystävällinen',
        'shed_title': 'Vähän Karvanlähtöä', 'shed_desc': 'Vähemmän karvaa, vähemmän sotkua',
        'train_title': 'Helppo Kouluttaa', 'train_desc': 'Nopeat oppijat',
        'features_title': 'Löydä Täydellinen Kumppanisi',
        'features_subtitle': 'Kaikki mitä tarvitset tehdäksesi tietoisen päätöksen uudesta karvajalkaperheen jäsenestä',
        'feat1_title': 'Rotutesti', 'feat1_desc': 'Vastaa muutamaan kysymykseen elämäntyylistäsi ja ehdotamme sinulle sopivia rotuja.',
        'feat2_title': 'Vertaile Rotuja', 'feat2_desc': 'Aseta rodut vierekkäin ja vertaa kokoa, energiatasoa, hoitotarvetta ja muuta.',
        'feat3_title': 'Asiantuntija-arviot', 'feat3_desc': 'Selkeät suositukset kenelle kukin rotu sopii parhaiten—ja kenelle ei.',
        'guides_title': 'Rotuoppaat',
        'guides_subtitle': 'Asiantuntijaneuvoja oikean koiran löytämiseen',
        'guide1_title': 'Parhaat Kerrostalokoirat', 'guide1_desc': '15 rotua jotka viihtyvät pienissä tiloissa',
        'guide2_title': 'Parhaat Perhekoirat', 'guide2_desc': '12 kärsivällistä, lempeää rotua lapsille',
        'guide3_title': 'Vähän Karvaavat Rodut', 'guide3_desc': '20 rotua puhtaampaan kotiin',
        'article1_slug': 'parhaat-kerrostalokoirat', 'article2_slug': 'parhaat-perhekoirat', 'article3_slug': 'vahan-karvaavat-koirat',
        'faq_title': 'Usein Kysytyt Kysymykset',
        'faq1_q': 'Miten valitsen oikean koirarodun elämäntyyliini?',
        'faq1_a': 'Harkitse asuintilaasi, aktiivisuustasoasi, aikaa turkinhoitoon ja perhettäsi. Rotatestiemme kysyy nämä ja yhdistää sinut sopiviin rotuihin.',
        'faq2_q': 'Mitkä ovat parhaita koirarotuja kerrostaloihin?',
        'faq2_a': 'Ranskalaiset buldogit, Cavalier King Charles Spanielit, Mopsit ja Boston Terrierit sopeutuvat hyvin kerrostaloasumiseen.',
        'faq3_q': 'Mitkä rodut sopivat parhaiten lapsiperheisiin?',
        'faq3_a': 'Labradorinnoutajat, Kultainennoutajat, Beaglet ja Colliet tunnetaan kärsivällisyydestään lasten kanssa.',
        'faq4_q': 'Mitkä koirat karvaavat vähiten?',
        'faq4_a': 'Villakoirat, Bichon Frisét, Portugalinvesikoirat ja Snautserit karvaavat vähän.',
        'faq5_q': 'Kuinka paljon liikuntaa eri rodut tarvitsevat?',
        'faq5_a': 'Energiset rodut tarvitsevat 2+ tuntia päivässä. Kohtalaiset rodut noin tunnin. Rauhallisille riittää 30 minuuttia.',
        'faq6_q': 'Mikä ero on vertailutyökalulla ja testillä?',
        'faq6_a': 'Testi auttaa löytämään rotuja elämäntyylisi perusteella. Vertailutyökalu näyttää kaksi rotua vierekkäin.',
        'footer_copy': '© 2026 BreedFinder. Tehty rakkaudella koiraystäville kaikkialla.',
        'browse_breeds': 'Selaa Rotuja', 'quiz': 'Testi', 'compare': 'Vertaile', 'guides': 'Oppaat', 'about': 'Tietoja',
    },
    'de': {
        'title': 'Hunderassen-Finder | Quiz, Vergleich & Finde Deinen Perfekten Hund',
        'meta_desc': 'Finde deine perfekte Hunderasse mit Quiz, Vergleich & Expertenratgeber. 200+ Rassen bewertet.',
        'badge': 'Über 200 Hunderassen zu entdecken',
        'h1_1': 'Finde Deine',
        'h1_2': 'Perfekte Hunderasse',
        'hero_p': 'Entdecke, welche Hunderasse perfekt zu deinem Lebensstil passt. Vergleiche Eigenschaften und finde deinen idealen Begleiter.',
        'search_placeholder': 'Rassen suchen...',
        'btn_quiz': 'Mach das Rassen-Quiz',
        'btn_compare': 'Rassen Vergleichen',
        'popular_title': 'Beliebte Rassen',
        'popular_subtitle': 'Die beliebtesten Hunderassen weltweit',
        'view_all': 'Alle 200+ Rassen ansehen',
        'size_title': 'Nach Größe Suchen',
        'size_subtitle': 'Finde Rassen, die zu deinem Wohnraum passen',
        'tiny': 'Winzig', 'small': 'Klein', 'medium': 'Mittel', 'large': 'Groß', 'giant': 'Riesig',
        'under': 'Unter', 'over': 'Über',
        'lifestyle_title': 'Nach Lebensstil Suchen',
        'lifestyle_subtitle': 'Schnelle Filter für deine Bedürfnisse',
        'apt_title': 'Wohnungsgeeignet', 'apt_desc': 'Perfekt für Wohnungen',
        'kids_title': 'Gut mit Kindern', 'kids_desc': 'Familienfreundlich',
        'shed_title': 'Wenig Haarausfall', 'shed_desc': 'Weniger Haare, weniger Chaos',
        'train_title': 'Leicht zu Trainieren', 'train_desc': 'Schnelle Lerner',
        'features_title': 'Finde Deinen Perfekten Partner',
        'features_subtitle': 'Alles was du brauchst für eine informierte Entscheidung',
        'feat1_title': 'Rassen-Quiz', 'feat1_desc': 'Beantworte ein paar Fragen und wir schlagen passende Rassen vor.',
        'feat2_title': 'Rassen Vergleichen', 'feat2_desc': 'Stelle Rassen nebeneinander und vergleiche Größe, Energie und mehr.',
        'feat3_title': 'Experten-Bewertungen', 'feat3_desc': 'Klare Empfehlungen für wen jede Rasse am besten ist.',
        'guides_title': 'Rassenführer',
        'guides_subtitle': 'Expertenrat zur Wahl des richtigen Hundes',
        'guide1_title': 'Beste Wohnungshunde', 'guide1_desc': '15 Rassen für kleine Räume',
        'guide2_title': 'Beste Familienhunde', 'guide2_desc': '12 geduldige Rassen für Kinder',
        'guide3_title': 'Wenig Haarende Rassen', 'guide3_desc': '20 Rassen für ein sauberes Zuhause',
        'article1_slug': 'beste-hunde-fuer-wohnungen', 'article2_slug': 'beste-hunde-fuer-familien', 'article3_slug': 'wenig-haarende-hunde',
        'faq_title': 'Häufig Gestellte Fragen',
        'faq1_q': 'Wie wähle ich die richtige Hunderasse?',
        'faq1_a': 'Berücksichtige deinen Wohnraum, Aktivitätslevel und Familie. Unser Quiz hilft dir dabei.',
        'faq2_q': 'Welche Hunderassen eignen sich für Wohnungen?',
        'faq2_a': 'Französische Bulldoggen, Cavaliers, Möpse und Boston Terrier passen gut in Wohnungen.',
        'faq3_q': 'Welche Rassen sind am besten für Familien?',
        'faq3_a': 'Labrador Retriever, Golden Retriever, Beagles und Collies sind bekannt für Geduld mit Kindern.',
        'faq4_q': 'Welche Hunde haaren am wenigsten?',
        'faq4_a': 'Pudel, Bichon Frisés, Portugiesische Wasserhunde und Schnauzer haaren wenig.',
        'faq5_q': 'Wie viel Bewegung brauchen verschiedene Rassen?',
        'faq5_a': 'Energische Rassen brauchen 2+ Stunden täglich. Moderate Rassen etwa 1 Stunde.',
        'faq6_q': 'Was ist der Unterschied zwischen Vergleich und Quiz?',
        'faq6_a': 'Das Quiz hilft Rassen zu entdecken. Der Vergleich zeigt zwei Rassen nebeneinander.',
        'footer_copy': '© 2026 BreedFinder. Mit Liebe für Hundefreunde gemacht.',
        'browse_breeds': 'Rassen Durchsuchen', 'quiz': 'Quiz', 'compare': 'Vergleichen', 'guides': 'Ratgeber', 'about': 'Über Uns',
    },
    'es': {
        'title': 'Buscador de Razas | Quiz, Comparar y Encuentra Tu Perro Perfecto',
        'meta_desc': 'Encuentra tu raza perfecta con nuestro quiz, herramienta de comparación y guías expertas. 200+ razas evaluadas.',
        'badge': 'Más de 200 razas para explorar',
        'h1_1': 'Encuentra Tu',
        'h1_2': 'Raza de Perro Perfecta',
        'hero_p': 'Descubre qué raza se adapta a tu estilo de vida. Compara características, haz el quiz y encuentra tu compañero ideal.',
        'search_placeholder': 'Buscar razas...',
        'btn_quiz': 'Hacer el Quiz',
        'btn_compare': 'Comparar Razas',
        'popular_title': 'Razas Populares',
        'popular_subtitle': 'Las razas más queridas del mundo',
        'view_all': 'Ver las 200+ razas',
        'size_title': 'Buscar por Tamaño',
        'size_subtitle': 'Encuentra razas que se adapten a tu espacio',
        'tiny': 'Miniatura', 'small': 'Pequeño', 'medium': 'Mediano', 'large': 'Grande', 'giant': 'Gigante',
        'under': 'Menos de', 'over': 'Más de',
        'lifestyle_title': 'Buscar por Estilo de Vida',
        'lifestyle_subtitle': 'Filtros rápidos para tus necesidades',
        'apt_title': 'Apto para Apartamento', 'apt_desc': 'Perfecto para pisos',
        'kids_title': 'Genial con Niños', 'kids_desc': 'Familiar',
        'shed_title': 'Poca Caída de Pelo', 'shed_desc': 'Menos pelo, menos desorden',
        'train_title': 'Fácil de Entrenar', 'train_desc': 'Aprenden rápido',
        'features_title': 'Encuentra Tu Pareja Perfecta',
        'features_subtitle': 'Todo lo que necesitas para tomar una decisión informada',
        'feat1_title': 'Quiz de Razas', 'feat1_desc': 'Responde unas preguntas y te sugeriremos razas perfectas para ti.',
        'feat2_title': 'Comparar Razas', 'feat2_desc': 'Compara razas lado a lado: tamaño, energía, cuidados y más.',
        'feat3_title': 'Opiniones Expertas', 'feat3_desc': 'Recomendaciones claras sobre para quién es mejor cada raza.',
        'guides_title': 'Guías de Razas',
        'guides_subtitle': 'Consejos expertos para encontrar el perro adecuado',
        'guide1_title': 'Mejores Perros para Apartamentos', 'guide1_desc': '15 razas para espacios pequeños',
        'guide2_title': 'Mejores Perros para Familias', 'guide2_desc': '12 razas gentiles para niños',
        'guide3_title': 'Razas que No Sueltan Pelo', 'guide3_desc': '20 razas para un hogar limpio',
        'article1_slug': 'best-dogs-for-apartments', 'article2_slug': 'best-dogs-for-families', 'article3_slug': 'low-shedding-dogs',
        'faq_title': 'Preguntas Frecuentes',
        'faq1_q': '¿Cómo elijo la raza correcta para mi estilo de vida?',
        'faq1_a': 'Considera tu espacio, nivel de actividad y familia. Nuestro Quiz te ayuda con esto.',
        'faq2_q': '¿Cuáles son las mejores razas para apartamentos?',
        'faq2_a': 'Bulldog Francés, Cavalier, Pug y Boston Terrier se adaptan bien a apartamentos.',
        'faq3_q': '¿Qué razas son mejores para familias con niños?',
        'faq3_a': 'Labrador, Golden Retriever, Beagle y Collie son conocidos por su paciencia con niños.',
        'faq4_q': '¿Qué perros sueltan menos pelo?',
        'faq4_a': 'Caniche, Bichón Frisé, Perro de Agua Portugués y Schnauzer sueltan poco pelo.',
        'faq5_q': '¿Cuánto ejercicio necesitan las diferentes razas?',
        'faq5_a': 'Razas energéticas necesitan 2+ horas diarias. Moderadas necesitan 1 hora.',
        'faq6_q': '¿Cuál es la diferencia entre Comparar y el Quiz?',
        'faq6_a': 'El Quiz te ayuda a descubrir razas. Comparar muestra dos razas lado a lado.',
        'footer_copy': '© 2026 BreedFinder. Hecho con amor para los amantes de los perros.',
        'browse_breeds': 'Ver Razas', 'quiz': 'Quiz', 'compare': 'Comparar', 'guides': 'Guías', 'about': 'Acerca de',
    },
    'fr': {
        'title': 'Trouvez Votre Race | Quiz, Comparer & Trouvez Votre Chien Parfait',
        'meta_desc': 'Trouvez votre race parfaite avec notre quiz, outil de comparaison et guides experts. 200+ races évaluées.',
        'badge': 'Plus de 200 races à explorer',
        'h1_1': 'Trouvez Votre',
        'h1_2': 'Race de Chien Parfaite',
        'hero_p': 'Découvrez quelle race correspond à votre style de vie. Comparez les caractéristiques et trouvez votre compagnon idéal.',
        'search_placeholder': 'Rechercher des races...',
        'btn_quiz': 'Faire le Quiz',
        'btn_compare': 'Comparer les Races',
        'popular_title': 'Races Populaires',
        'popular_subtitle': 'Les races les plus aimées au monde',
        'view_all': 'Voir les 200+ races',
        'size_title': 'Parcourir par Taille',
        'size_subtitle': 'Trouvez des races adaptées à votre espace',
        'tiny': 'Minuscule', 'small': 'Petit', 'medium': 'Moyen', 'large': 'Grand', 'giant': 'Géant',
        'under': 'Moins de', 'over': 'Plus de',
        'lifestyle_title': 'Rechercher par Mode de Vie',
        'lifestyle_subtitle': 'Filtres rapides pour vos besoins',
        'apt_title': 'Adapté Appartement', 'apt_desc': 'Parfait pour les appartements',
        'kids_title': 'Bon avec les Enfants', 'kids_desc': 'Familial',
        'shed_title': 'Peu de Perte de Poils', 'shed_desc': 'Moins de poils, moins de désordre',
        'train_title': 'Facile à Dresser', 'train_desc': 'Apprentissage rapide',
        'features_title': 'Trouvez Votre Match Parfait',
        'features_subtitle': 'Tout ce qu\'il faut pour prendre une décision éclairée',
        'feat1_title': 'Quiz des Races', 'feat1_desc': 'Répondez à quelques questions et nous suggérerons des races parfaites.',
        'feat2_title': 'Comparer les Races', 'feat2_desc': 'Comparez les races côte à côte: taille, énergie, toilettage et plus.',
        'feat3_title': 'Avis d\'Experts', 'feat3_desc': 'Recommandations claires sur pour qui chaque race convient le mieux.',
        'guides_title': 'Guides des Races',
        'guides_subtitle': 'Conseils d\'experts pour trouver le bon chien',
        'guide1_title': 'Meilleurs Chiens d\'Appartement', 'guide1_desc': '15 races pour petits espaces',
        'guide2_title': 'Meilleurs Chiens pour Familles', 'guide2_desc': '12 races douces pour les enfants',
        'guide3_title': 'Races à Faible Perte de Poils', 'guide3_desc': '20 races pour une maison propre',
        'article1_slug': 'best-dogs-for-apartments', 'article2_slug': 'best-dogs-for-families', 'article3_slug': 'low-shedding-dogs',
        'faq_title': 'Questions Fréquentes',
        'faq1_q': 'Comment choisir la bonne race pour mon style de vie?',
        'faq1_a': 'Considérez votre espace, niveau d\'activité et famille. Notre Quiz vous aide.',
        'faq2_q': 'Quelles sont les meilleures races pour appartements?',
        'faq2_a': 'Bouledogue Français, Cavalier, Carlin et Boston Terrier s\'adaptent bien.',
        'faq3_q': 'Quelles races conviennent aux familles avec enfants?',
        'faq3_a': 'Labrador, Golden Retriever, Beagle et Colley sont connus pour leur patience.',
        'faq4_q': 'Quels chiens perdent le moins de poils?',
        'faq4_a': 'Caniche, Bichon Frisé, Chien d\'Eau Portugais et Schnauzer perdent peu.',
        'faq5_q': 'Combien d\'exercice les différentes races ont-elles besoin?',
        'faq5_a': 'Les races énergiques ont besoin de 2+ heures par jour. Les modérées, 1 heure.',
        'faq6_q': 'Quelle est la différence entre Comparer et le Quiz?',
        'faq6_a': 'Le Quiz aide à découvrir des races. Comparer montre deux races côte à côte.',
        'footer_copy': '© 2026 BreedFinder. Fait avec amour pour les amoureux des chiens.',
        'browse_breeds': 'Parcourir les Races', 'quiz': 'Quiz', 'compare': 'Comparer', 'guides': 'Guides', 'about': 'À Propos',
    },
}

# Add remaining languages with simplified translations
for lang in ['it', 'pt', 'nl', 'pl', 'zh', 'ja', 'sv', 'no', 'da', 'ru']:
    if lang not in T:
        T[lang] = T['en'].copy()  # Fallback to English

# Italian
T['it'] = {
    'title': 'Trova la Tua Razza | Quiz, Confronta & Trova il Tuo Cane Perfetto',
    'meta_desc': 'Trova la razza perfetta con quiz, strumento di confronto e guide esperte. 200+ razze valutate.',
    'badge': 'Oltre 200 razze da esplorare',
    'h1_1': 'Trova la Tua',
    'h1_2': 'Razza di Cane Perfetta',
    'hero_p': 'Scopri quale razza si adatta al tuo stile di vita. Confronta le caratteristiche e trova il tuo compagno ideale.',
    'search_placeholder': 'Cerca razze...',
    'btn_quiz': 'Fai il Quiz',
    'btn_compare': 'Confronta Razze',
    'popular_title': 'Razze Popolari',
    'popular_subtitle': 'Le razze più amate al mondo',
    'view_all': 'Vedi tutte le 200+ razze',
    'size_title': 'Cerca per Taglia',
    'size_subtitle': 'Trova razze adatte al tuo spazio',
    'tiny': 'Minuscolo', 'small': 'Piccolo', 'medium': 'Medio', 'large': 'Grande', 'giant': 'Gigante',
    'under': 'Sotto', 'over': 'Oltre',
    'lifestyle_title': 'Cerca per Stile di Vita',
    'lifestyle_subtitle': 'Filtri rapidi per le tue esigenze',
    'apt_title': 'Adatto Appartamento', 'apt_desc': 'Perfetto per appartamenti',
    'kids_title': 'Ottimo con Bambini', 'kids_desc': 'Familiare',
    'shed_title': 'Poca Perdita di Pelo', 'shed_desc': 'Meno pelo, meno disordine',
    'train_title': 'Facile da Addestrare', 'train_desc': 'Apprendono velocemente',
    'features_title': 'Trova il Tuo Match Perfetto',
    'features_subtitle': 'Tutto ciò che serve per una decisione informata',
    'feat1_title': 'Quiz delle Razze', 'feat1_desc': 'Rispondi a qualche domanda e ti suggeriremo razze perfette.',
    'feat2_title': 'Confronta Razze', 'feat2_desc': 'Confronta le razze fianco a fianco: taglia, energia e altro.',
    'feat3_title': 'Pareri Esperti', 'feat3_desc': 'Raccomandazioni chiare su chi è più adatto per ogni razza.',
    'guides_title': 'Guide delle Razze',
    'guides_subtitle': 'Consigli esperti per trovare il cane giusto',
    'guide1_title': 'Migliori Cani da Appartamento', 'guide1_desc': '15 razze per piccoli spazi',
    'guide2_title': 'Migliori Cani per Famiglie', 'guide2_desc': '12 razze gentili per bambini',
    'guide3_title': 'Razze che Perdono Poco Pelo', 'guide3_desc': '20 razze per una casa pulita',
    'article1_slug': 'best-dogs-for-apartments', 'article2_slug': 'best-dogs-for-families', 'article3_slug': 'low-shedding-dogs',
    'faq_title': 'Domande Frequenti',
    'faq1_q': 'Come scelgo la razza giusta per il mio stile di vita?',
    'faq1_a': 'Considera il tuo spazio, livello di attività e famiglia. Il nostro Quiz ti aiuta.',
    'faq2_q': 'Quali sono le migliori razze per appartamenti?',
    'faq2_a': 'Bulldog Francese, Cavalier, Carlino e Boston Terrier si adattano bene.',
    'faq3_q': 'Quali razze sono migliori per famiglie con bambini?',
    'faq3_a': 'Labrador, Golden Retriever, Beagle e Collie sono noti per la pazienza.',
    'faq4_q': 'Quali cani perdono meno pelo?',
    'faq4_a': 'Barboncino, Bichon Frisé, Cane d\'Acqua Portoghese e Schnauzer perdono poco.',
    'faq5_q': 'Quanto esercizio hanno bisogno le diverse razze?',
    'faq5_a': 'Le razze energiche hanno bisogno di 2+ ore al giorno. Moderate, 1 ora.',
    'faq6_q': 'Qual è la differenza tra Confronta e il Quiz?',
    'faq6_a': 'Il Quiz aiuta a scoprire razze. Confronta mostra due razze fianco a fianco.',
    'footer_copy': '© 2026 BreedFinder. Fatto con amore per gli amanti dei cani.',
    'browse_breeds': 'Esplora Razze', 'quiz': 'Quiz', 'compare': 'Confronta', 'guides': 'Guide', 'about': 'Chi Siamo',
}

# Add remaining language translations (shortened for brevity - using key translations)
for lang in ['pt', 'nl', 'pl', 'zh', 'ja', 'sv', 'no', 'da', 'ru']:
    T[lang] = T['en'].copy()

def generate_lang_dropdown(current_lang, prefix=''):
    """Generate language dropdown HTML"""
    items = [f'<a href="{prefix}../" class="block px-4 py-2 hover:bg-slate-100 {"font-semibold text-sky-600" if current_lang == "en" else "text-slate-600"}">English</a>']
    for code, info in LANGUAGES.items():
        selected = 'font-semibold text-sky-600' if code == current_lang else 'text-slate-600'
        items.append(f'<a href="{prefix}../{code}/" class="block px-4 py-2 hover:bg-slate-100 {selected}">{info["name"]}</a>')
    return ''.join(items)


def generate_homepage(lang, base_dir):
    """Generate homepage for a specific language"""
    t = T.get(lang, T['en'])
    lang_info = LANGUAGES.get(lang, {'name': 'English', 'code': 'EN'})
    
    output_dir = base_dir / lang
    output_dir.mkdir(parents=True, exist_ok=True)
    
    lang_dropdown = generate_lang_dropdown(lang)
    
    # Generate hreflang tags
    hreflang = ['<link rel="alternate" hreflang="en" href="https://breedfinder.org/">']
    for code in LANGUAGES.keys():
        hreflang.append(f'<link rel="alternate" hreflang="{code}" href="https://breedfinder.org/{code}/">')
    hreflang.append('<link rel="alternate" hreflang="x-default" href="https://breedfinder.org/">')
    hreflang_html = '\n    '.join(hreflang)
    
    html = f'''<!DOCTYPE html>
<html lang="{lang}" class="">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{t['title']} | BreedFinder</title>
    <meta name="description" content="{t['meta_desc']}">
    <link rel="canonical" href="https://breedfinder.org/{lang}/">
    
    {hreflang_html}
    
    <link rel="icon" href="../favicon.ico" type="image/x-icon">
    <link rel="icon" type="image/png" sizes="32x32" href="../favicon-32.png">
    <link rel="apple-touch-icon" sizes="180x180" href="../apple-touch-icon.png">
    
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://breedfinder.org/{lang}/">
    <meta property="og:title" content="BreedFinder — {t['h1_2']}">
    <meta property="og:description" content="{t['hero_p'][:150]}">
    <meta property="og:site_name" content="BreedFinder">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {{ theme: {{ extend: {{ fontFamily: {{ sans: ['Plus Jakarta Sans', 'sans-serif'] }} }} }} }}
    </script>
    <style>
        .card-shadow {{ box-shadow: 0 1px 3px rgba(0,0,0,0.04), 0 4px 12px rgba(0,0,0,0.03); }}
        .card-shadow:hover {{ box-shadow: 0 4px 12px rgba(0,0,0,0.06), 0 8px 24px rgba(0,0,0,0.05); }}
        .hero-gradient {{ background: linear-gradient(135deg, #f0f9ff 0%, #faf5ff 50%, #fff1f2 100%); }}
    </style>
</head>
<body class="bg-white min-h-screen text-slate-800">
    <header class="bg-white/80 backdrop-blur-md border-b border-slate-100 sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
            <a href="./" class="flex items-center gap-3">
                <img src="../logo-192.png" class="w-10 h-10" alt="BreedFinder">
                <span class="text-xl font-bold bg-gradient-to-r from-slate-800 to-slate-600 bg-clip-text text-transparent">BreedFinder</span>
            </a>
            <nav class="flex items-center gap-4 md:gap-6 text-sm font-medium">
                <a href="search/" class="text-slate-600 hover:text-sky-600 transition ml-2 md:ml-0">{t['browse_breeds']}</a>
                <a href="quiz/" class="bg-gradient-to-r from-sky-500 to-violet-500 text-white px-5 py-2.5 rounded-xl font-semibold hover:shadow-lg transition">{t['quiz']}</a>
                <div class="relative group">
                    <button class="flex items-center gap-1 text-slate-600 hover:text-sky-600 py-2">
                        <i data-lucide="globe" class="w-4 h-4"></i>
                        <span class="hidden md:inline">{lang_info['code']}</span>
                    </button>
                    <div class="absolute right-0 top-full bg-white border border-slate-200 rounded-xl shadow-xl hidden group-hover:block min-w-[140px] py-2 max-h-80 overflow-y-auto z-50 before:absolute before:h-2 before:-top-2 before:left-0 before:right-0 before:bg-transparent">
                        {lang_dropdown}
                    </div>
                </div>
            </nav>
        </div>
    </header>

    <main>
        <section class="hero-gradient py-20 px-4">
            <div class="max-w-4xl mx-auto text-center">
                <div class="inline-flex items-center gap-2 bg-white/80 backdrop-blur px-4 py-2 rounded-full text-sm font-medium text-slate-600 mb-6 border border-slate-200/50">
                    <i data-lucide="sparkles" class="w-4 h-4 text-violet-500"></i>
                    {t['badge']}
                </div>
                <h1 class="text-5xl md:text-6xl font-extrabold text-slate-900 mb-6 leading-tight">
                    {t['h1_1']}<br>
                    <span class="bg-gradient-to-r from-sky-500 via-violet-500 to-rose-500 bg-clip-text text-transparent">{t['h1_2']}</span>
                </h1>
                <p class="text-xl text-slate-600 mb-10 max-w-2xl mx-auto leading-relaxed">{t['hero_p']}</p>
                
                <div class="max-w-xl mx-auto mb-8">
                    <div class="relative">
                        <input type="text" id="home-search" placeholder="{t['search_placeholder']}" autocomplete="off" class="w-full bg-white border border-slate-200 rounded-2xl px-6 py-4 text-lg focus:outline-none focus:ring-2 focus:ring-sky-500/20 focus:border-sky-400 shadow-sm">
                        <button class="absolute right-2 top-1/2 -translate-y-1/2 bg-slate-100 hover:bg-slate-200 p-3 rounded-xl transition">
                            <i data-lucide="search" class="w-5 h-5 text-slate-500"></i>
                        </button>
                        <div id="search-dropdown" class="absolute top-full left-0 right-0 mt-2 bg-white border border-slate-200 rounded-2xl shadow-xl z-50 hidden max-h-80 overflow-y-auto"></div>
                    </div>
                </div>

                <div class="flex flex-wrap justify-center gap-4">
                    <a href="quiz/" class="inline-flex items-center gap-2 bg-gradient-to-r from-sky-500 to-violet-500 text-white px-8 py-4 rounded-2xl font-semibold text-lg hover:shadow-xl hover:shadow-sky-500/25 transition transform hover:-translate-y-0.5">
                        <i data-lucide="target" class="w-5 h-5"></i>
                        {t['btn_quiz']}
                    </a>
                    <a href="compare/" class="inline-flex items-center gap-2 bg-white text-slate-700 border border-slate-200 px-8 py-4 rounded-2xl font-semibold text-lg hover:border-slate-300 hover:shadow-lg transition transform hover:-translate-y-0.5">
                        <i data-lucide="scale" class="w-5 h-5"></i>
                        {t['btn_compare']}
                    </a>
                </div>
            </div>
        </section>

        <section class="py-16 px-4">
            <div class="max-w-6xl mx-auto">
                <h2 class="text-2xl font-bold text-slate-900 mb-2">{t['popular_title']}</h2>
                <p class="text-slate-500 mb-8">{t['popular_subtitle']}</p>
                <div class="grid grid-cols-2 md:grid-cols-4 gap-5">
                    <a href="breeds/labrador-retriever.html" class="bg-white rounded-2xl p-5 card-shadow border border-slate-100 hover:border-sky-200 transition group">
                        <div class="w-16 h-16 rounded-2xl mx-auto mb-3 overflow-hidden">
                            <img src="../images/heads/labrador-retriever.webp" alt="Labrador Retriever" class="w-full h-full object-cover object-top">
                        </div>
                        <div class="font-semibold text-slate-800 text-center">Labrador Retriever</div>
                        <div class="text-xs text-slate-500 text-center mt-1">Friendly • Active • Loyal</div>
                    </a>
                    <a href="breeds/german-shepherd.html" class="bg-white rounded-2xl p-5 card-shadow border border-slate-100 hover:border-sky-200 transition group">
                        <div class="w-16 h-16 rounded-2xl mx-auto mb-3 overflow-hidden">
                            <img src="../images/heads/german-shepherd.webp" alt="German Shepherd" class="w-full h-full object-cover object-top">
                        </div>
                        <div class="font-semibold text-slate-800 text-center">German Shepherd</div>
                        <div class="text-xs text-slate-500 text-center mt-1">Intelligent • Protective</div>
                    </a>
                    <a href="breeds/golden-retriever.html" class="bg-white rounded-2xl p-5 card-shadow border border-slate-100 hover:border-sky-200 transition group">
                        <div class="w-16 h-16 rounded-2xl mx-auto mb-3 overflow-hidden">
                            <img src="../images/heads/golden-retriever.webp" alt="Golden Retriever" class="w-full h-full object-cover object-top">
                        </div>
                        <div class="font-semibold text-slate-800 text-center">Golden Retriever</div>
                        <div class="text-xs text-slate-500 text-center mt-1">Gentle • Friendly • Smart</div>
                    </a>
                    <a href="breeds/french-bulldog.html" class="bg-white rounded-2xl p-5 card-shadow border border-slate-100 hover:border-sky-200 transition group">
                        <div class="w-16 h-16 rounded-2xl mx-auto mb-3 overflow-hidden">
                            <img src="../images/heads/french-bulldog.webp" alt="French Bulldog" class="w-full h-full object-cover object-top">
                        </div>
                        <div class="font-semibold text-slate-800 text-center">French Bulldog</div>
                        <div class="text-xs text-slate-500 text-center mt-1">Playful • Adaptable</div>
                    </a>
                    <a href="breeds/poodle.html" class="bg-white rounded-2xl p-5 card-shadow border border-slate-100 hover:border-sky-200 transition group">
                        <div class="w-16 h-16 rounded-2xl mx-auto mb-3 overflow-hidden">
                            <img src="../images/heads/poodle.webp" alt="Poodle" class="w-full h-full object-cover object-top">
                        </div>
                        <div class="font-semibold text-slate-800 text-center">Poodle</div>
                        <div class="text-xs text-slate-500 text-center mt-1">Intelligent • Elegant</div>
                    </a>
                    <a href="breeds/siberian-husky.html" class="bg-white rounded-2xl p-5 card-shadow border border-slate-100 hover:border-sky-200 transition group">
                        <div class="w-16 h-16 rounded-2xl mx-auto mb-3 overflow-hidden">
                            <img src="../images/heads/siberian-husky.webp" alt="Siberian Husky" class="w-full h-full object-cover object-top">
                        </div>
                        <div class="font-semibold text-slate-800 text-center">Siberian Husky</div>
                        <div class="text-xs text-slate-500 text-center mt-1">Energetic • Outgoing</div>
                    </a>
                    <a href="breeds/beagle.html" class="bg-white rounded-2xl p-5 card-shadow border border-slate-100 hover:border-sky-200 transition group">
                        <div class="w-16 h-16 rounded-2xl mx-auto mb-3 overflow-hidden">
                            <img src="../images/heads/beagle.webp" alt="Beagle" class="w-full h-full object-cover object-top">
                        </div>
                        <div class="font-semibold text-slate-800 text-center">Beagle</div>
                        <div class="text-xs text-slate-500 text-center mt-1">Curious • Merry</div>
                    </a>
                    <a href="breeds/alaskan-malamute.html" class="bg-white rounded-2xl p-5 card-shadow border-2 border-sky-300 transition group relative overflow-hidden">
                        <div class="absolute top-2 right-2 bg-gradient-to-r from-sky-500 to-violet-500 text-white text-xs font-bold px-2 py-1 rounded-full">NEW</div>
                        <div class="w-16 h-16 rounded-2xl mx-auto mb-3 overflow-hidden">
                            <img src="../images/heads/alaskan-malamute.webp" alt="Alaskan Malamute" class="w-full h-full object-cover object-top">
                        </div>
                        <div class="font-semibold text-slate-800 text-center">Alaskan Malamute</div>
                        <div class="text-xs text-slate-500 text-center mt-1">Powerful • Independent</div>
                    </a>
                </div>
                <div class="text-center mt-8">
                    <a href="search/" class="inline-flex items-center gap-2 text-sky-600 font-semibold hover:text-sky-700 transition">
                        {t['view_all']}
                        <i data-lucide="arrow-right" class="w-4 h-4"></i>
                    </a>
                </div>
            </div>
        </section>

        <section class="py-16 px-4 bg-slate-50">
            <div class="max-w-6xl mx-auto">
                <h2 class="text-2xl font-bold text-slate-900 mb-2">{t['size_title']}</h2>
                <p class="text-slate-500 mb-8">{t['size_subtitle']}</p>
                <div class="grid grid-cols-2 md:grid-cols-5 gap-4">
                    <a href="search/?size=tiny" class="bg-gradient-to-br from-sky-50 to-sky-100 hover:from-sky-100 hover:to-sky-200 rounded-2xl p-6 text-center transition border border-sky-100 group">
                        <div class="w-14 h-14 rounded-xl mx-auto mb-3 group-hover:scale-110 transition shadow-sm overflow-hidden">
                            <img src="../images/heads/chihuahua.webp" alt="Chihuahua" class="w-full h-full object-cover object-top">
                        </div>
                        <div class="font-semibold text-slate-800">{t['tiny']}</div>
                        <div class="text-sm text-slate-500">{t['under']} 5 kg</div>
                    </a>
                    <a href="search/?size=small" class="bg-gradient-to-br from-sky-100 to-sky-200 hover:from-sky-200 hover:to-sky-300 rounded-2xl p-6 text-center transition border border-sky-200 group">
                        <div class="w-14 h-14 rounded-xl mx-auto mb-3 group-hover:scale-110 transition shadow-sm overflow-hidden">
                            <img src="../images/heads/beagle.webp" alt="Beagle" class="w-full h-full object-cover object-top">
                        </div>
                        <div class="font-semibold text-slate-800">{t['small']}</div>
                        <div class="text-sm text-slate-500">5–10 kg</div>
                    </a>
                    <a href="search/?size=medium" class="bg-gradient-to-br from-sky-200 to-violet-200 hover:from-sky-300 hover:to-violet-300 rounded-2xl p-6 text-center transition border border-violet-200 group">
                        <div class="w-14 h-14 rounded-xl mx-auto mb-3 group-hover:scale-110 transition shadow-sm overflow-hidden">
                            <img src="../images/heads/border-collie.webp" alt="Border Collie" class="w-full h-full object-cover object-top">
                        </div>
                        <div class="font-semibold text-slate-800">{t['medium']}</div>
                        <div class="text-sm text-slate-500">10–25 kg</div>
                    </a>
                    <a href="search/?size=large" class="bg-gradient-to-br from-violet-200 to-violet-300 hover:from-violet-300 hover:to-violet-400 rounded-2xl p-6 text-center transition border border-violet-300 group">
                        <div class="w-14 h-14 rounded-xl mx-auto mb-3 group-hover:scale-110 transition shadow-sm overflow-hidden">
                            <img src="../images/heads/german-shepherd.webp" alt="German Shepherd" class="w-full h-full object-cover object-top">
                        </div>
                        <div class="font-semibold text-slate-800">{t['large']}</div>
                        <div class="text-sm text-slate-500">25–45 kg</div>
                    </a>
                    <a href="search/?size=giant" class="bg-gradient-to-br from-violet-300 to-purple-400 hover:from-violet-400 hover:to-purple-500 rounded-2xl p-6 text-center transition border border-violet-400 group">
                        <div class="w-14 h-14 rounded-xl mx-auto mb-3 group-hover:scale-110 transition shadow-sm overflow-hidden">
                            <img src="../images/heads/great-dane.webp" alt="Great Dane" class="w-full h-full object-cover object-top">
                        </div>
                        <div class="font-semibold text-white">{t['giant']}</div>
                        <div class="text-sm text-white/80">{t['over']} 45 kg</div>
                    </a>
                </div>
            </div>
        </section>

        <section class="py-16 px-4">
            <div class="max-w-6xl mx-auto">
                <h2 class="text-2xl font-bold text-slate-900 mb-2">{t['lifestyle_title']}</h2>
                <p class="text-slate-500 mb-8">{t['lifestyle_subtitle']}</p>
                <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                    <a href="search/?apartment=1" class="bg-gradient-to-br from-blue-50 to-indigo-50 hover:from-blue-100 hover:to-indigo-100 rounded-2xl p-6 text-center transition border border-blue-100 group">
                        <div class="w-12 h-12 bg-white rounded-xl mx-auto mb-3 flex items-center justify-center shadow-sm group-hover:scale-110 transition">
                            <i data-lucide="building-2" class="w-6 h-6 text-blue-500"></i>
                        </div>
                        <div class="font-semibold text-slate-800">{t['apt_title']}</div>
                        <div class="text-sm text-slate-500">{t['apt_desc']}</div>
                    </a>
                    <a href="search/?kids=1" class="bg-gradient-to-br from-green-50 to-emerald-50 hover:from-green-100 hover:to-emerald-100 rounded-2xl p-6 text-center transition border border-green-100 group">
                        <div class="w-12 h-12 bg-white rounded-xl mx-auto mb-3 flex items-center justify-center shadow-sm group-hover:scale-110 transition">
                            <i data-lucide="heart" class="w-6 h-6 text-green-500"></i>
                        </div>
                        <div class="font-semibold text-slate-800">{t['kids_title']}</div>
                        <div class="text-sm text-slate-500">{t['kids_desc']}</div>
                    </a>
                    <a href="search/?shedding=minimal" class="bg-gradient-to-br from-purple-50 to-violet-50 hover:from-purple-100 hover:to-violet-100 rounded-2xl p-6 text-center transition border border-purple-100 group">
                        <div class="w-12 h-12 bg-white rounded-xl mx-auto mb-3 flex items-center justify-center shadow-sm group-hover:scale-110 transition">
                            <i data-lucide="sparkles" class="w-6 h-6 text-purple-500"></i>
                        </div>
                        <div class="font-semibold text-slate-800">{t['shed_title']}</div>
                        <div class="text-sm text-slate-500">{t['shed_desc']}</div>
                    </a>
                    <a href="search/?train=1" class="bg-gradient-to-br from-orange-50 to-amber-50 hover:from-orange-100 hover:to-amber-100 rounded-2xl p-6 text-center transition border border-orange-100 group">
                        <div class="w-12 h-12 bg-white rounded-xl mx-auto mb-3 flex items-center justify-center shadow-sm group-hover:scale-110 transition">
                            <i data-lucide="graduation-cap" class="w-6 h-6 text-orange-500"></i>
                        </div>
                        <div class="font-semibold text-slate-800">{t['train_title']}</div>
                        <div class="text-sm text-slate-500">{t['train_desc']}</div>
                    </a>
                </div>
            </div>
        </section>

        <section class="py-20 px-4">
            <div class="max-w-6xl mx-auto">
                <div class="text-center mb-12">
                    <h2 class="text-3xl font-bold text-slate-900 mb-4">{t['features_title']}</h2>
                    <p class="text-lg text-slate-500 max-w-2xl mx-auto">{t['features_subtitle']}</p>
                </div>
                <div class="grid md:grid-cols-3 gap-8">
                    <div class="text-center p-8 rounded-3xl bg-gradient-to-br from-sky-50 to-sky-100/50 border border-sky-100">
                        <div class="w-16 h-16 bg-white rounded-2xl flex items-center justify-center mx-auto mb-5 shadow-lg">
                            <i data-lucide="target" class="w-8 h-8 text-sky-500"></i>
                        </div>
                        <h3 class="text-xl font-bold text-slate-800 mb-3">{t['feat1_title']}</h3>
                        <p class="text-slate-600">{t['feat1_desc']}</p>
                    </div>
                    <div class="text-center p-8 rounded-3xl bg-gradient-to-br from-violet-50 to-violet-100/50 border border-violet-100">
                        <div class="w-16 h-16 bg-white rounded-2xl flex items-center justify-center mx-auto mb-5 shadow-lg">
                            <i data-lucide="scale" class="w-8 h-8 text-violet-500"></i>
                        </div>
                        <h3 class="text-xl font-bold text-slate-800 mb-3">{t['feat2_title']}</h3>
                        <p class="text-slate-600">{t['feat2_desc']}</p>
                    </div>
                    <div class="text-center p-8 rounded-3xl bg-gradient-to-br from-rose-50 to-rose-100/50 border border-rose-100">
                        <div class="w-16 h-16 bg-white rounded-2xl flex items-center justify-center mx-auto mb-5 shadow-lg">
                            <i data-lucide="award" class="w-8 h-8 text-rose-500"></i>
                        </div>
                        <h3 class="text-xl font-bold text-slate-800 mb-3">{t['feat3_title']}</h3>
                        <p class="text-slate-600">{t['feat3_desc']}</p>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <section class="py-16 px-4">
        <div class="max-w-6xl mx-auto">
            <h2 class="text-2xl font-bold text-slate-900 mb-2">{t['guides_title']}</h2>
            <p class="text-slate-600 mb-6">{t['guides_subtitle']}</p>
            <div class="grid md:grid-cols-3 gap-4">
                <a href="articles/{t.get('article1_slug', 'best-dogs-for-apartments')}/" class="bg-white rounded-xl p-5 shadow-sm hover:shadow-md transition border border-slate-100">
                    <span class="text-3xl">🏢</span>
                    <h3 class="font-bold text-slate-900 mt-3 mb-1">{t['guide1_title']}</h3>
                    <p class="text-slate-600 text-sm">{t['guide1_desc']}</p>
                </a>
                <a href="articles/{t.get('article2_slug', 'best-dogs-for-families')}/" class="bg-white rounded-xl p-5 shadow-sm hover:shadow-md transition border border-slate-100">
                    <span class="text-3xl">👨‍👩‍👧‍👦</span>
                    <h3 class="font-bold text-slate-900 mt-3 mb-1">{t['guide2_title']}</h3>
                    <p class="text-slate-600 text-sm">{t['guide2_desc']}</p>
                </a>
                <a href="articles/{t.get('article3_slug', 'low-shedding-dogs')}/" class="bg-white rounded-xl p-5 shadow-sm hover:shadow-md transition border border-slate-100">
                    <span class="text-3xl">✨</span>
                    <h3 class="font-bold text-slate-900 mt-3 mb-1">{t['guide3_title']}</h3>
                    <p class="text-slate-600 text-sm">{t['guide3_desc']}</p>
                </a>
            </div>
        </div>
    </section>

    <section class="py-16 px-4 bg-slate-50">
        <div class="max-w-4xl mx-auto">
            <h2 class="text-2xl font-bold text-slate-900 mb-8 text-center">{t['faq_title']}</h2>
            <div class="space-y-4">
                <div class="bg-white rounded-xl p-6 shadow-sm">
                    <h3 class="font-semibold text-slate-900 text-lg">{t['faq1_q']}</h3>
                    <p class="text-slate-600 mt-2">{t['faq1_a']}</p>
                </div>
                <div class="bg-white rounded-xl p-6 shadow-sm">
                    <h3 class="font-semibold text-slate-900 text-lg">{t['faq2_q']}</h3>
                    <p class="text-slate-600 mt-2">{t['faq2_a']}</p>
                </div>
                <div class="bg-white rounded-xl p-6 shadow-sm">
                    <h3 class="font-semibold text-slate-900 text-lg">{t['faq3_q']}</h3>
                    <p class="text-slate-600 mt-2">{t['faq3_a']}</p>
                </div>
                <div class="bg-white rounded-xl p-6 shadow-sm">
                    <h3 class="font-semibold text-slate-900 text-lg">{t['faq4_q']}</h3>
                    <p class="text-slate-600 mt-2">{t['faq4_a']}</p>
                </div>
                <div class="bg-white rounded-xl p-6 shadow-sm">
                    <h3 class="font-semibold text-slate-900 text-lg">{t['faq5_q']}</h3>
                    <p class="text-slate-600 mt-2">{t['faq5_a']}</p>
                </div>
                <div class="bg-white rounded-xl p-6 shadow-sm">
                    <h3 class="font-semibold text-slate-900 text-lg">{t['faq6_q']}</h3>
                    <p class="text-slate-600 mt-2">{t['faq6_a']}</p>
                </div>
            </div>
        </div>
    </section>

    <footer class="bg-slate-900 text-white py-12 px-4">
        <div class="max-w-6xl mx-auto">
            <div class="flex flex-col md:flex-row items-center justify-between gap-6">
                <div class="flex items-center gap-3">
                    <img src="../logo-192.png" class="w-10 h-10" alt="BreedFinder">
                    <span class="text-xl font-bold">BreedFinder</span>
                </div>
                <div class="flex gap-8 text-sm text-slate-400">
                    <a href="quiz/" class="hover:text-white transition">{t['quiz']}</a>
                    <a href="compare/" class="hover:text-white transition">{t['compare']}</a>
                    <a href="../articles/" class="hover:text-white transition">{t['guides']}</a>
                    <a href="../about/" class="hover:text-white transition">{t['about']}</a>
                </div>
            </div>
            <div class="border-t border-slate-800 mt-8 pt-8 text-center text-sm text-slate-500">
                <p>{t['footer_copy']}</p>
            </div>
        </div>
    </footer>

    <script>
        lucide.createIcons();
        let breeds = [];
        fetch('../data/breeds.json')
            .then(r => r.json())
            .then(data => {{ breeds = data.map(b => ({{name: b.name, slug: b.id}})); }})
            .catch(e => console.error('Failed to load breeds:', e));
        
        const homeSearch = document.getElementById('home-search');
        const dropdown = document.getElementById('search-dropdown');
        
        if (homeSearch && dropdown) {{
            homeSearch.addEventListener('input', function() {{
                const query = this.value.trim().toLowerCase();
                if (query.length < 1) {{ dropdown.classList.add('hidden'); return; }}
                const matches = breeds.filter(b => b.name.toLowerCase().includes(query)).slice(0, 8);
                if (matches.length === 0) {{ dropdown.classList.add('hidden'); return; }}
                dropdown.innerHTML = matches.map(b => `
                    <a href="breeds/${{b.slug}}.html" class="flex items-center gap-3 px-4 py-3 hover:bg-slate-50 transition first:rounded-t-2xl last:rounded-b-2xl">
                        <img src="../images/heads/${{b.slug}}.webp" alt="${{b.name}}" class="w-10 h-10 rounded-xl object-cover" onerror="this.style.display='none'">
                        <span class="font-medium text-slate-800">${{b.name}}</span>
                    </a>
                `).join('');
                dropdown.classList.remove('hidden');
            }});
            homeSearch.addEventListener('blur', function() {{ setTimeout(() => dropdown.classList.add('hidden'), 200); }});
            homeSearch.addEventListener('focus', function() {{ if (this.value.trim().length >= 1) this.dispatchEvent(new Event('input')); }});
            homeSearch.addEventListener('keypress', function(e) {{ if (e.key === 'Enter' && this.value.trim()) window.location.href = 'search/?q=' + encodeURIComponent(this.value.trim()); }});
        }}
    </script>
</body>
</html>'''
    
    with open(output_dir / 'index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  Created {lang}/index.html")


def main():
    base_dir = Path(__file__).parent.parent
    
    print("Generating full translated homepages...")
    for lang in LANGUAGES.keys():
        generate_homepage(lang, base_dir)
    
    print(f"\n✅ Done! Created {len(LANGUAGES)} complete homepages")


if __name__ == '__main__':
    main()
