#!/usr/bin/env python3
"""
Full translation of breed pages for ES, FR, DE
Translates: descriptions, health, exercise, temperament, verdict sections
"""

import re
import json
from pathlib import Path

# Common phrase translations
PHRASES = {
    'es': {
        # Health section phrases
        'Generally healthy': 'Generalmente saludable',
        'prone to': 'propenso a',
        'hip dysplasia': 'displasia de cadera',
        'elbow dysplasia': 'displasia de codo',
        'eye conditions': 'problemas oculares',
        'heart disease': 'enfermedad cardíaca',
        'bloat': 'hinchazón',
        'obesity': 'obesidad',
        'allergies': 'alergias',
        'skin issues': 'problemas de piel',
        'ear infections': 'infecciones de oído',
        'dental problems': 'problemas dentales',
        'joint problems': 'problemas articulares',
        'breathing problems': 'problemas respiratorios',
        'Regular vet checkups': 'Chequeos veterinarios regulares',
        'recommended': 'recomendado',
        
        # Exercise section phrases
        'High energy': 'Alta energía',
        'Moderate energy': 'Energía moderada',
        'Low energy': 'Baja energía',
        'daily exercise': 'ejercicio diario',
        'needs': 'necesita',
        'requires': 'requiere',
        'hours': 'horas',
        'hour': 'hora',
        'minutes': 'minutos',
        'walks': 'paseos',
        'running': 'correr',
        'swimming': 'nadar',
        'mental stimulation': 'estimulación mental',
        'training': 'entrenamiento',
        'playtime': 'tiempo de juego',
        
        # Verdict phrases
        'The ultimate': 'El mejor',
        'perfect for': 'perfecto para',
        'ideal for': 'ideal para',
        'great for': 'genial para',
        'best for': 'mejor para',
        'not recommended for': 'no recomendado para',
        'families': 'familias',
        'children': 'niños',
        'apartments': 'apartamentos',
        'first-time owners': 'dueños primerizos',
        'active people': 'personas activas',
        'experienced owners': 'dueños con experiencia',
        
        # Common adjectives
        'friendly': 'amigable',
        'loyal': 'leal',
        'intelligent': 'inteligente',
        'gentle': 'gentil',
        'playful': 'juguetón',
        'protective': 'protector',
        'energetic': 'enérgico',
        'calm': 'tranquilo',
        'affectionate': 'cariñoso',
        'independent': 'independiente',
        'stubborn': 'terco',
        'patient': 'paciente',
        'loving': 'amoroso',
        'trainable': 'entrenable',
        'adaptable': 'adaptable',
        
        # Common nouns
        'family dog': 'perro familiar',
        'companion': 'compañero',
        'guard dog': 'perro guardián',
        'working dog': 'perro de trabajo',
        'hunting dog': 'perro de caza',
        'herding dog': 'perro pastor',
        'therapy dog': 'perro de terapia',
        'watchdog': 'perro guardián',
    },
    'fr': {
        'Generally healthy': 'Généralement en bonne santé',
        'prone to': 'sujet à',
        'hip dysplasia': 'dysplasie de la hanche',
        'elbow dysplasia': 'dysplasie du coude',
        'eye conditions': 'problèmes oculaires',
        'heart disease': 'maladie cardiaque',
        'bloat': 'ballonnement',
        'obesity': 'obésité',
        'allergies': 'allergies',
        'skin issues': 'problèmes de peau',
        'ear infections': 'infections auriculaires',
        'dental problems': 'problèmes dentaires',
        'joint problems': 'problèmes articulaires',
        'breathing problems': 'problèmes respiratoires',
        'Regular vet checkups': 'Examens vétérinaires réguliers',
        'recommended': 'recommandé',
        
        'High energy': 'Haute énergie',
        'Moderate energy': 'Énergie modérée',
        'Low energy': 'Faible énergie',
        'daily exercise': 'exercice quotidien',
        'needs': 'a besoin de',
        'requires': 'nécessite',
        'hours': 'heures',
        'hour': 'heure',
        'minutes': 'minutes',
        'walks': 'promenades',
        'running': 'course',
        'swimming': 'natation',
        'mental stimulation': 'stimulation mentale',
        'training': 'dressage',
        'playtime': 'temps de jeu',
        
        'The ultimate': 'Le meilleur',
        'perfect for': 'parfait pour',
        'ideal for': 'idéal pour',
        'great for': 'excellent pour',
        'best for': 'meilleur pour',
        'not recommended for': 'non recommandé pour',
        'families': 'familles',
        'children': 'enfants',
        'apartments': 'appartements',
        'first-time owners': 'premiers propriétaires',
        'active people': 'personnes actives',
        'experienced owners': 'propriétaires expérimentés',
        
        'friendly': 'amical',
        'loyal': 'loyal',
        'intelligent': 'intelligent',
        'gentle': 'doux',
        'playful': 'joueur',
        'protective': 'protecteur',
        'energetic': 'énergique',
        'calm': 'calme',
        'affectionate': 'affectueux',
        'independent': 'indépendant',
        'stubborn': 'têtu',
        'patient': 'patient',
        'loving': 'aimant',
        'trainable': 'facile à dresser',
        'adaptable': 'adaptable',
        
        'family dog': 'chien de famille',
        'companion': 'compagnon',
        'guard dog': 'chien de garde',
        'working dog': 'chien de travail',
        'hunting dog': 'chien de chasse',
        'herding dog': 'chien de berger',
        'therapy dog': 'chien de thérapie',
        'watchdog': 'chien de garde',
    },
    'de': {
        'Generally healthy': 'Im Allgemeinen gesund',
        'prone to': 'anfällig für',
        'hip dysplasia': 'Hüftdysplasie',
        'elbow dysplasia': 'Ellbogendysplasie',
        'eye conditions': 'Augenprobleme',
        'heart disease': 'Herzerkrankung',
        'bloat': 'Blähungen',
        'obesity': 'Fettleibigkeit',
        'allergies': 'Allergien',
        'skin issues': 'Hautprobleme',
        'ear infections': 'Ohreninfektionen',
        'dental problems': 'Zahnprobleme',
        'joint problems': 'Gelenkprobleme',
        'breathing problems': 'Atemprobleme',
        'Regular vet checkups': 'Regelmäßige Tierarztuntersuchungen',
        'recommended': 'empfohlen',
        
        'High energy': 'Hohe Energie',
        'Moderate energy': 'Moderate Energie',
        'Low energy': 'Niedrige Energie',
        'daily exercise': 'tägliche Bewegung',
        'needs': 'braucht',
        'requires': 'erfordert',
        'hours': 'Stunden',
        'hour': 'Stunde',
        'minutes': 'Minuten',
        'walks': 'Spaziergänge',
        'running': 'Laufen',
        'swimming': 'Schwimmen',
        'mental stimulation': 'geistige Stimulation',
        'training': 'Training',
        'playtime': 'Spielzeit',
        
        'The ultimate': 'Der ultimative',
        'perfect for': 'perfekt für',
        'ideal for': 'ideal für',
        'great for': 'großartig für',
        'best for': 'am besten für',
        'not recommended for': 'nicht empfohlen für',
        'families': 'Familien',
        'children': 'Kinder',
        'apartments': 'Wohnungen',
        'first-time owners': 'Erstbesitzer',
        'active people': 'aktive Menschen',
        'experienced owners': 'erfahrene Besitzer',
        
        'friendly': 'freundlich',
        'loyal': 'treu',
        'intelligent': 'intelligent',
        'gentle': 'sanft',
        'playful': 'verspielt',
        'protective': 'beschützend',
        'energetic': 'energisch',
        'calm': 'ruhig',
        'affectionate': 'liebevoll',
        'independent': 'unabhängig',
        'stubborn': 'stur',
        'patient': 'geduldig',
        'loving': 'liebend',
        'trainable': 'trainierbar',
        'adaptable': 'anpassungsfähig',
        
        'family dog': 'Familienhund',
        'companion': 'Begleiter',
        'guard dog': 'Wachhund',
        'working dog': 'Arbeitshund',
        'hunting dog': 'Jagdhund',
        'herding dog': 'Hütehund',
        'therapy dog': 'Therapiehund',
        'watchdog': 'Wachhund',
    },
}

# Popular breed full translations (Top 50)
BREED_TRANSLATIONS = {
    'labrador-retriever': {
        'es': {
            'overview': 'El Labrador Retriever es la raza de perro más popular de América por una buena razón. Son compañeros amigables, extrovertidos y llenos de energía que tienen más que suficiente cariño para toda la familia.',
            'temperament': 'Los Labs son famosamente amigables. Son compañeros hogareños que se vinculan con toda la familia y socializan bien con perros vecinos y humanos por igual. Pero no confunda su personalidad relajada con baja energía.',
            'health': 'Generalmente saludable, pero propenso a displasia de cadera y codo, trastornos cardíacos, condiciones oculares y colapso inducido por ejercicio. La obesidad es común, así que vigile su dieta.',
            'exercise': 'Raza de alta energía que requiere ejercicio diario vigoroso—al menos una hora de actividad. Prosperan con familias activas que disfrutan de actividades al aire libre. La estimulación mental a través del entrenamiento y juguetes de rompecabezas es igualmente importante.',
            'verdict': 'El perro familiar definitivo. Los Labrador Retrievers son amigables, pacientes y entrenables—perfectos para dueños primerizos y familias con niños. Necesitan mucho ejercicio y sueltan mucho pelo, pero su naturaleza amorosa los hace valer la pena.',
        },
        'fr': {
            'overview': 'Le Labrador Retriever est la race de chien la plus populaire d\'Amérique pour une bonne raison. Ce sont des compagnons amicaux, extravertis et pleins d\'entrain qui ont plus qu\'assez d\'affection pour toute la famille.',
            'temperament': 'Les Labs sont réputés pour leur amabilité. Ce sont des compagnons de maison qui créent des liens avec toute la famille et socialisent bien avec les chiens et humains voisins. Mais ne confondez pas leur personnalité décontractée avec un manque d\'énergie.',
            'health': 'Généralement en bonne santé, mais sujet à la dysplasie de la hanche et du coude, aux troubles cardiaques, aux problèmes oculaires et à l\'effondrement induit par l\'exercice. L\'obésité est fréquente, surveillez donc leur alimentation.',
            'exercise': 'Race à haute énergie nécessitant un exercice quotidien vigoureux—au moins une heure d\'activité. Ils s\'épanouissent avec des familles actives qui aiment les activités de plein air. La stimulation mentale par le dressage et les jouets puzzle est tout aussi importante.',
            'verdict': 'Le chien de famille par excellence. Les Labrador Retrievers sont amicaux, patients et faciles à dresser—parfaits pour les premiers propriétaires et les familles avec enfants. Ils ont besoin de beaucoup d\'exercice et perdent beaucoup de poils, mais leur nature aimante en vaut la peine.',
        },
        'de': {
            'overview': 'Der Labrador Retriever ist aus gutem Grund die beliebteste Hunderasse Amerikas. Sie sind freundliche, aufgeschlossene und temperamentvolle Begleiter, die mehr als genug Zuneigung für die ganze Familie haben.',
            'temperament': 'Labs sind berühmt für ihre Freundlichkeit. Sie sind gesellige Mitbewohner, die sich mit der ganzen Familie verbinden und gut mit Nachbarhunden und Menschen sozialisieren. Aber verwechseln Sie ihre entspannte Persönlichkeit nicht mit niedriger Energie.',
            'health': 'Im Allgemeinen gesund, aber anfällig für Hüft- und Ellbogendysplasie, Herzerkrankungen, Augenprobleme und belastungsbedingten Kollaps. Fettleibigkeit ist häufig, also achten Sie auf ihre Ernährung.',
            'exercise': 'Energiereiche Rasse, die täglich intensive Bewegung benötigt—mindestens eine Stunde Aktivität. Sie gedeihen mit aktiven Familien, die Outdoor-Aktivitäten genießen. Geistige Stimulation durch Training und Puzzlespielzeug ist ebenso wichtig.',
            'verdict': 'Der ultimative Familienhund. Labrador Retriever sind freundlich, geduldig und trainierbar—perfekt für Erstbesitzer und Familien mit Kindern. Sie brauchen viel Bewegung und haaren viel, aber ihre liebevolle Art macht sie es wert.',
        },
    },
    'german-shepherd': {
        'es': {
            'overview': 'El Pastor Alemán es un perro de trabajo versátil e inteligente conocido por su valentía y devoción. Son la segunda raza más popular en América y se destacan como perros de servicio, policía y familia.',
            'temperament': 'Los Pastores Alemanes son inteligentes, seguros y valientes. Son leales a su familia y pueden ser distantes con los extraños. La socialización temprana es crucial para prevenir la sobreprotección.',
            'health': 'Propenso a displasia de cadera y codo, mielopatía degenerativa, hinchazón y alergias. Elija criadores responsables que realicen pruebas de salud. La esperanza de vida es de 9-13 años.',
            'exercise': 'Raza de muy alta energía que necesita ejercicio físico y mental extenso. Al menos 2 horas de actividad diaria. Se destacan en obediencia, agilidad y trabajo de protección. El aburrimiento lleva a comportamientos destructivos.',
            'verdict': 'Excelente para dueños activos y experimentados que pueden proporcionar entrenamiento constante y ejercicio. No es ideal para dueños primerizos o familias sedentarias. Hacen compañeros leales e impresionantes perros guardianes.',
        },
        'fr': {
            'overview': 'Le Berger Allemand est un chien de travail polyvalent et intelligent connu pour son courage et sa dévotion. C\'est la deuxième race la plus populaire en Amérique et excelle comme chien de service, de police et de famille.',
            'temperament': 'Les Bergers Allemands sont intelligents, confiants et courageux. Ils sont loyaux envers leur famille et peuvent être distants avec les étrangers. Une socialisation précoce est cruciale pour éviter la surprotection.',
            'health': 'Sujet à la dysplasie de la hanche et du coude, à la myélopathie dégénérative, au ballonnement et aux allergies. Choisissez des éleveurs responsables qui effectuent des tests de santé. Espérance de vie de 9-13 ans.',
            'exercise': 'Race à très haute énergie nécessitant un exercice physique et mental extensif. Au moins 2 heures d\'activité quotidienne. Excellent en obéissance, agilité et travail de protection. L\'ennui mène à des comportements destructeurs.',
            'verdict': 'Excellent pour les propriétaires actifs et expérimentés qui peuvent fournir un entraînement et un exercice constants. Non idéal pour les premiers propriétaires ou les familles sédentaires. Font des compagnons loyaux et d\'impressionnants chiens de garde.',
        },
        'de': {
            'overview': 'Der Deutsche Schäferhund ist ein vielseitiger und intelligenter Arbeitshund, bekannt für seinen Mut und seine Hingabe. Er ist die zweitbeliebteste Rasse in Amerika und zeichnet sich als Dienst-, Polizei- und Familienhund aus.',
            'temperament': 'Deutsche Schäferhunde sind intelligent, selbstbewusst und mutig. Sie sind ihrer Familie treu und können Fremden gegenüber distanziert sein. Frühe Sozialisierung ist entscheidend, um Überbeschützung zu verhindern.',
            'health': 'Anfällig für Hüft- und Ellbogendysplasie, degenerative Myelopathie, Blähungen und Allergien. Wählen Sie verantwortungsvolle Züchter, die Gesundheitstests durchführen. Lebenserwartung 9-13 Jahre.',
            'exercise': 'Sehr energiereiche Rasse, die umfangreiche körperliche und geistige Bewegung benötigt. Mindestens 2 Stunden tägliche Aktivität. Hervorragend in Gehorsam, Agility und Schutzarbeit. Langeweile führt zu destruktivem Verhalten.',
            'verdict': 'Hervorragend für aktive, erfahrene Besitzer, die konsequentes Training und Bewegung bieten können. Nicht ideal für Erstbesitzer oder sesshafte Familien. Machen treue Begleiter und beeindruckende Wachhunde.',
        },
    },
    'golden-retriever': {
        'es': {
            'overview': 'El Golden Retriever es un perro devoto, amigable e inteligente. Su naturaleza tolerante y paciente los hace excelentes perros de familia y perros de terapia efectivos.',
            'temperament': 'Los Goldens son extrovertidos, confiables y ansiosos por complacer. Son juguetones y gentiles, manteniendo su comportamiento de cachorro hasta bien entrada la edad adulta. Se llevan bien con todos—niños, extraños y otras mascotas.',
            'health': 'Propenso a cáncer (especialmente hemangiosarcoma y linfoma), displasia de cadera, problemas cardíacos y condiciones oculares. Los chequeos regulares y mantener un peso saludable son esenciales.',
            'exercise': 'Raza activa que necesita 1-2 horas de ejercicio diario. Aman nadar, buscar y cualquier actividad que involucre a su familia. Excelentes en deportes caninos como agilidad y obediencia.',
            'verdict': 'El perro familiar ideal. Los Golden Retrievers son pacientes con los niños, fáciles de entrenar y se adaptan bien a la mayoría de los hogares. Sueltan mucho pelo y requieren ejercicio regular, pero su temperamento amoroso lo compensa.',
        },
        'fr': {
            'overview': 'Le Golden Retriever est un chien dévoué, amical et intelligent. Leur nature tolérante et patiente en fait d\'excellents chiens de famille et des chiens de thérapie efficaces.',
            'temperament': 'Les Goldens sont extravertis, fiables et désireux de plaire. Ils sont joueurs et doux, gardant leur comportement de chiot jusque tard dans l\'âge adulte. Ils s\'entendent avec tout le monde—enfants, étrangers et autres animaux.',
            'health': 'Sujet au cancer (en particulier hémangiosarcome et lymphome), à la dysplasie de la hanche, aux problèmes cardiaques et aux problèmes oculaires. Des examens réguliers et le maintien d\'un poids sain sont essentiels.',
            'exercise': 'Race active nécessitant 1-2 heures d\'exercice quotidien. Ils aiment nager, rapporter et toute activité impliquant leur famille. Excellent dans les sports canins comme l\'agilité et l\'obéissance.',
            'verdict': 'Le chien de famille idéal. Les Golden Retrievers sont patients avec les enfants, faciles à dresser et s\'adaptent bien à la plupart des foyers. Ils perdent beaucoup de poils et nécessitent un exercice régulier, mais leur tempérament aimant compense.',
        },
        'de': {
            'overview': 'Der Golden Retriever ist ein hingebungsvoller, freundlicher und intelligenter Hund. Ihre tolerante und geduldige Natur macht sie zu ausgezeichneten Familienhunden und effektiven Therapiehunden.',
            'temperament': 'Goldens sind aufgeschlossen, zuverlässig und begierig zu gefallen. Sie sind verspielt und sanft und behalten ihr Welpenverhalten bis ins hohe Alter. Sie verstehen sich mit jedem—Kindern, Fremden und anderen Haustieren.',
            'health': 'Anfällig für Krebs (besonders Hämangiosarkom und Lymphom), Hüftdysplasie, Herzprobleme und Augenprobleme. Regelmäßige Untersuchungen und ein gesundes Gewicht sind wichtig.',
            'exercise': 'Aktive Rasse, die 1-2 Stunden tägliche Bewegung braucht. Sie lieben Schwimmen, Apportieren und jede Aktivität mit ihrer Familie. Hervorragend in Hundesportarten wie Agility und Gehorsam.',
            'verdict': 'Der ideale Familienhund. Golden Retriever sind geduldig mit Kindern, leicht zu trainieren und passen sich gut an die meisten Haushalte an. Sie haaren viel und brauchen regelmäßige Bewegung, aber ihr liebevolles Temperament macht es wett.',
        },
    },
    'french-bulldog': {
        'es': {
            'overview': 'El Bulldog Francés es un compañero encantador con orejas de murciélago y una personalidad irresistible. Son adaptables, juguetones y requieren ejercicio mínimo.',
            'temperament': 'Los Frenchies son cariñosos, pacientes y alertas. Prosperan con la compañía humana y pueden desarrollar ansiedad por separación. Son buenos perros guardianes pero rara vez ladran excesivamente.',
            'health': 'Como raza braquicéfala, propensos a problemas respiratorios, sensibilidad al calor, alergias cutáneas y problemas de columna. Evite el ejercicio excesivo en clima cálido. Esperanza de vida 10-12 años.',
            'exercise': 'Raza de baja energía—paseos cortos y tiempo de juego son suficientes. Evite el ejercicio extenuante, especialmente en calor. Se contentan con ser perros de sofá. Cuidado con el sobrepeso.',
            'verdict': 'Perfecto para habitantes de apartamentos y dueños menos activos. Los Bulldogs Franceses son compañeros cariñosos que no requieren mucho ejercicio. Tenga en cuenta los posibles costos de salud debido a problemas de raza.',
        },
        'fr': {
            'overview': 'Le Bouledogue Français est un compagnon charmant avec des oreilles de chauve-souris et une personnalité irrésistible. Ils sont adaptables, joueurs et nécessitent un exercice minimal.',
            'temperament': 'Les Frenchies sont affectueux, patients et alertes. Ils prospèrent avec la compagnie humaine et peuvent développer une anxiété de séparation. Ce sont de bons chiens de garde mais aboient rarement excessivement.',
            'health': 'En tant que race brachycéphale, sujets aux problèmes respiratoires, sensibilité à la chaleur, allergies cutanées et problèmes de colonne vertébrale. Évitez l\'exercice excessif par temps chaud. Espérance de vie 10-12 ans.',
            'exercise': 'Race à faible énergie—de courtes promenades et du temps de jeu suffisent. Évitez l\'exercice intense, surtout par temps chaud. Contents d\'être des chiens de canapé. Attention au surpoids.',
            'verdict': 'Parfait pour les habitants d\'appartement et les propriétaires moins actifs. Les Bouledogues Français sont des compagnons affectueux qui ne nécessitent pas beaucoup d\'exercice. Soyez conscient des coûts de santé potentiels dus aux problèmes de race.',
        },
        'de': {
            'overview': 'Die Französische Bulldogge ist ein charmanter Begleiter mit Fledermausohren und einer unwiderstehlichen Persönlichkeit. Sie sind anpassungsfähig, verspielt und benötigen minimale Bewegung.',
            'temperament': 'Frenchies sind liebevoll, geduldig und wachsam. Sie gedeihen mit menschlicher Gesellschaft und können Trennungsangst entwickeln. Sie sind gute Wachhunde, bellen aber selten übermäßig.',
            'health': 'Als brachyzephale Rasse anfällig für Atemprobleme, Hitzeempfindlichkeit, Hautallergien und Wirbelsäulenprobleme. Vermeiden Sie übermäßige Bewegung bei heißem Wetter. Lebenserwartung 10-12 Jahre.',
            'exercise': 'Energiearme Rasse—kurze Spaziergänge und Spielzeit reichen aus. Vermeiden Sie anstrengende Bewegung, besonders bei Hitze. Zufrieden als Couchhunde. Achten Sie auf Übergewicht.',
            'verdict': 'Perfekt für Wohnungsbewohner und weniger aktive Besitzer. Französische Bulldoggen sind liebevolle Begleiter, die nicht viel Bewegung brauchen. Beachten Sie mögliche Gesundheitskosten aufgrund von Rasseproblemen.',
        },
    },
    'poodle': {
        'es': {
            'overview': 'El Caniche es una raza excepcionalmente inteligente y elegante que viene en tres tamaños: estándar, miniatura y toy. Son conocidos por su pelaje hipoalergénico y su apariencia distinguida.',
            'temperament': 'Los Caniches son orgullosos, inteligentes y activos. Son altamente entrenables y se destacan en obediencia y trucos. A pesar de su apariencia elegante, son perros atléticos y disfrutan de las actividades al aire libre.',
            'health': 'Propensos a displasia de cadera, problemas oculares, hinchazón (en estándar), enfermedad de Addison y epilepsia. Su largo pelaje requiere cuidado regular para prevenir enredos.',
            'exercise': 'Los Caniches Estándar necesitan ejercicio regular y estimulación mental. Los Miniatura y Toy requieren menos pero aún necesitan actividad diaria. Todos los tamaños disfrutan del agua y los deportes caninos.',
            'verdict': 'Excelente para alérgicos debido a su bajo desprendimiento. Los Caniches son perros versátiles que se adaptan bien a varios hogares. Requieren aseo regular y estimulación mental para prosperar.',
        },
        'fr': {
            'overview': 'Le Caniche est une race exceptionnellement intelligente et élégante qui existe en trois tailles : standard, miniature et toy. Ils sont connus pour leur pelage hypoallergénique et leur apparence distinguée.',
            'temperament': 'Les Caniches sont fiers, intelligents et actifs. Ils sont hautement dressables et excellent en obéissance et en tours. Malgré leur apparence élégante, ce sont des chiens athlétiques qui apprécient les activités de plein air.',
            'health': 'Sujets à la dysplasie de la hanche, aux problèmes oculaires, au ballonnement (standard), à la maladie d\'Addison et à l\'épilepsie. Leur long pelage nécessite un toilettage régulier pour éviter les nœuds.',
            'exercise': 'Les Caniches Standards ont besoin d\'exercice régulier et de stimulation mentale. Les Miniatures et Toys en ont besoin de moins mais ont quand même besoin d\'activité quotidienne. Toutes les tailles aiment l\'eau et les sports canins.',
            'verdict': 'Excellent pour les allergiques grâce à leur faible perte de poils. Les Caniches sont des chiens polyvalents qui s\'adaptent bien à divers foyers. Ils nécessitent un toilettage régulier et une stimulation mentale pour s\'épanouir.',
        },
        'de': {
            'overview': 'Der Pudel ist eine außergewöhnlich intelligente und elegante Rasse, die in drei Größen erhältlich ist: Standard, Miniatur und Toy. Sie sind bekannt für ihr hypoallergenes Fell und ihr distinguiertes Aussehen.',
            'temperament': 'Pudel sind stolz, intelligent und aktiv. Sie sind hochgradig trainierbar und zeichnen sich in Gehorsam und Tricks aus. Trotz ihres eleganten Aussehens sind sie athletische Hunde, die Outdoor-Aktivitäten genießen.',
            'health': 'Anfällig für Hüftdysplasie, Augenprobleme, Blähungen (Standard), Addison-Krankheit und Epilepsie. Ihr langes Fell erfordert regelmäßige Pflege, um Verfilzungen zu vermeiden.',
            'exercise': 'Standardpudel brauchen regelmäßige Bewegung und geistige Stimulation. Miniatur und Toy brauchen weniger, aber trotzdem tägliche Aktivität. Alle Größen lieben Wasser und Hundesportarten.',
            'verdict': 'Hervorragend für Allergiker aufgrund des geringen Haarausfalls. Pudel sind vielseitige Hunde, die sich gut an verschiedene Haushalte anpassen. Sie brauchen regelmäßige Pflege und geistige Stimulation, um zu gedeihen.',
        },
    },
    'beagle': {
        'es': {
            'overview': 'El Beagle es un sabueso alegre y amigable conocido por su excelente sentido del olfato y naturaleza amorosa. Son excelentes perros familiares y compañeros de caza.',
            'temperament': 'Los Beagles son curiosos, amigables y alegres. Son perros de manada que se llevan bien con otras mascotas y niños. Pueden ser tercos durante el entrenamiento pero responden bien a los premios de comida.',
            'health': 'Propensos a epilepsia, hipotiroidismo, displasia de cadera, problemas oculares y enfermedad de disco intervertebral. Tenga cuidado con la obesidad ya que aman la comida.',
            'exercise': 'Raza activa que necesita ejercicio diario regular. Paseos largos y tiempo de juego seguros son esenciales. Manténgalos con correa ya que seguirán olores. Jardín seguro recomendado.',
            'verdict': 'Genial para familias activas que pueden proporcionar ejercicio y compañía. Los Beagles son amigables y buenos con los niños pero pueden ser vocales. No ideal para hogares donde ladrar es un problema.',
        },
        'fr': {
            'overview': 'Le Beagle est un chien courant joyeux et amical connu pour son excellent sens de l\'odorat et sa nature aimante. Ce sont d\'excellents chiens de famille et compagnons de chasse.',
            'temperament': 'Les Beagles sont curieux, amicaux et joyeux. Ce sont des chiens de meute qui s\'entendent bien avec les autres animaux et les enfants. Ils peuvent être têtus pendant le dressage mais répondent bien aux récompenses alimentaires.',
            'health': 'Sujets à l\'épilepsie, l\'hypothyroïdie, la dysplasie de la hanche, les problèmes oculaires et la maladie du disque intervertébral. Attention à l\'obésité car ils adorent la nourriture.',
            'exercise': 'Race active nécessitant un exercice quotidien régulier. De longues promenades et du temps de jeu sécurisé sont essentiels. Gardez-les en laisse car ils suivront les odeurs. Jardin sécurisé recommandé.',
            'verdict': 'Excellent pour les familles actives qui peuvent fournir exercice et compagnie. Les Beagles sont amicaux et bons avec les enfants mais peuvent être vocaux. Non idéal pour les foyers où les aboiements sont un problème.',
        },
        'de': {
            'overview': 'Der Beagle ist ein fröhlicher und freundlicher Spürhund, bekannt für seinen ausgezeichneten Geruchssinn und seine liebevolle Natur. Sie sind ausgezeichnete Familienhunde und Jagdbegleiter.',
            'temperament': 'Beagles sind neugierig, freundlich und fröhlich. Sie sind Rudelhunde, die sich gut mit anderen Haustieren und Kindern verstehen. Sie können beim Training stur sein, reagieren aber gut auf Futterbelohnungen.',
            'health': 'Anfällig für Epilepsie, Hypothyreose, Hüftdysplasie, Augenprobleme und Bandscheibenerkrankungen. Achten Sie auf Fettleibigkeit, da sie Essen lieben.',
            'exercise': 'Aktive Rasse, die regelmäßige tägliche Bewegung braucht. Lange Spaziergänge und sichere Spielzeit sind wichtig. An der Leine halten, da sie Gerüchen folgen. Sicherer Garten empfohlen.',
            'verdict': 'Großartig für aktive Familien, die Bewegung und Gesellschaft bieten können. Beagles sind freundlich und gut mit Kindern, können aber laut sein. Nicht ideal für Haushalte, wo Bellen ein Problem ist.',
        },
    },
}

def translate_content(content, lang, phrases):
    """Translate content using phrase dictionary"""
    for eng, trans in phrases.items():
        # Case-insensitive replacement
        pattern = re.compile(re.escape(eng), re.IGNORECASE)
        content = pattern.sub(trans, content)
    return content


def process_breed_page(filepath, lang):
    """Process and translate a single breed page"""
    content = filepath.read_text(encoding='utf-8')
    breed_slug = filepath.stem
    
    # Check if we have full translation for this breed
    if breed_slug in BREED_TRANSLATIONS and lang in BREED_TRANSLATIONS[breed_slug]:
        trans = BREED_TRANSLATIONS[breed_slug][lang]
        
        # Replace overview section
        if 'overview' in trans:
            content = re.sub(
                r'(<i data-lucide="book-open"[^>]*></i>\s*Yleiskatsaus[\s\S]*?<div class="px-6 pb-6"><p class="text-slate-600">)(.*?)(</p></div>)',
                lambda m: m.group(1) + trans['overview'] + m.group(3),
                content,
                flags=re.IGNORECASE
            )
            # Also try other language patterns
            content = re.sub(
                r'(<div class="px-6 pb-6"><p class="text-slate-600">)(The [^<]{50,500}?)(</p></div>\s*</details>\s*<details)',
                lambda m: m.group(1) + trans['overview'] + m.group(3),
                content,
                count=1
            )
        
        # Replace temperament section
        if 'temperament' in trans:
            content = re.sub(
                r'(<i data-lucide="heart"[^>]*></i>\s*Luonne[\s\S]*?<div class="px-6 pb-6"><p class="text-slate-600">)(.*?)(</p></div>)',
                lambda m: m.group(1) + trans['temperament'] + m.group(3),
                content,
                flags=re.IGNORECASE
            )
        
        # Replace health section
        if 'health' in trans:
            content = re.sub(
                r'(<i data-lucide="heart-pulse"[^>]*></i>\s*Terveys[\s\S]*?<div class="px-6 pb-6"><p class="text-slate-600">)(.*?)(</p></div>)',
                lambda m: m.group(1) + trans['health'] + m.group(3),
                content,
                flags=re.IGNORECASE
            )
        
        # Replace exercise section
        if 'exercise' in trans:
            content = re.sub(
                r'(<i data-lucide="activity"[^>]*></i>\s*Liikunta[\s\S]*?<div class="px-6 pb-6"><p class="text-slate-600">)(.*?)(</p></div>)',
                lambda m: m.group(1) + trans['exercise'] + m.group(3),
                content,
                flags=re.IGNORECASE
            )
        
        # Replace verdict
        if 'verdict' in trans:
            content = re.sub(
                r'(<strong>Meidän Arvio:</strong>\s*)(.*?)(</p>)',
                lambda m: m.group(1) + trans['verdict'] + m.group(3),
                content,
                flags=re.IGNORECASE
            )
    
    # Apply phrase translations to remaining English content
    if lang in PHRASES:
        content = translate_content(content, lang, PHRASES[lang])
    
    return content


def main():
    base_dir = Path(__file__).parent.parent
    languages = ['es', 'de', 'fr']
    
    print("Translating breed pages for ES, DE, FR...")
    
    for lang in languages:
        breeds_dir = base_dir / lang / 'breeds'
        if not breeds_dir.exists():
            print(f"  Skipping {lang} - no breeds directory")
            continue
        
        count = 0
        for breed_file in breeds_dir.glob('*.html'):
            content = process_breed_page(breed_file, lang)
            breed_file.write_text(content, encoding='utf-8')
            count += 1
        
        # Count fully translated
        full_trans = sum(1 for b in BREED_TRANSLATIONS if lang in BREED_TRANSLATIONS.get(b, {}))
        print(f"  {lang.upper()}: {count} pages updated, {full_trans} fully translated")
    
    print(f"\n✅ Done! Translated ES, DE, FR breed pages")
    print(f"   Full translations: {list(BREED_TRANSLATIONS.keys())}")


if __name__ == '__main__':
    main()
