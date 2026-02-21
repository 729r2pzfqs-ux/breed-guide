#!/usr/bin/env python3
"""Generate translated quiz pages for all languages"""

import json
from pathlib import Path

LANGUAGES = {
    'es': 'Español', 'de': 'Deutsch', 'fr': 'Français', 'it': 'Italiano',
    'pt': 'Português', 'nl': 'Nederlands', 'pl': 'Polski', 'zh': '中文',
    'ja': '日本語', 'fi': 'Suomi', 'sv': 'Svenska', 'no': 'Norsk',
    'da': 'Dansk', 'ru': 'Русский'
}

# Quiz translations - ALL 14 languages
T = {
    'en': {
        'title': 'Find Your Perfect Dog',
        'badge': '5 quick questions',
        'subtitle': "Answer a few questions about your lifestyle and we'll match you with ideal breeds.",
        'start_btn': 'Start Quiz →',
        'question': 'Question',
        'of': 'of',
        'back': 'Back',
        'next': 'Next',
        'see_results': 'See My Matches',
        'your_matches': 'Your Perfect Matches',
        'matches_desc': 'Based on your answers, these breeds are ideal for you',
        'why_match': 'Why this matches you:',
        'view_profile': 'View Profile',
        'compare': 'Compare Top 2',
        'retake': '← Retake Quiz',
        'browse': 'Browse Breeds',
        'quiz': 'Quiz',
        'q1': 'How active is your lifestyle?',
        'q1_a1': '🛋️ Relaxed — I prefer quiet evenings',
        'q1_a2': '🚶 Moderate — Daily walks are fine',
        'q1_a3': '🏃 Active — I exercise regularly',
        'q1_a4': '⚡ Very Active — Outdoors is my life',
        'q2': 'How much space do you have?',
        'q2_a1': '🏢 Small apartment',
        'q2_a2': '🏠 House/larger apartment',
        'q2_a3': '🏡 House with yard',
        'q2_a4': '🌳 Large property / rural',
        'q3': 'Who will the dog live with?',
        'q3_a1': '👤 Just me',
        'q3_a2': '👫 Me and partner',
        'q3_a3': '👨‍👩‍👧 Family with older kids',
        'q3_a4': '👶 Family with young children',
        'q4': 'How much grooming can you handle?',
        'q4_a1': '✨ Minimal — low maintenance please',
        'q4_a2': '🪥 Some — weekly brushing is ok',
        'q4_a3': '💇 Regular — I can commit to grooming',
        'q4_a4': '🐩 High — I enjoy grooming',
        'q5': 'What size dog do you prefer?',
        'q5_a1': '🐕 Small (under 10 kg)',
        'q5_a2': '🐕 Medium (10-25 kg)',
        'q5_a3': '🐕 Large (25-45 kg)',
        'q5_a4': '🐕 Giant (over 45 kg)',
        'match_pct': '% Match',
    },
    'fi': {
        'title': 'Löydä Täydellinen Koirasi',
        'badge': '5 nopeaa kysymystä',
        'subtitle': 'Vastaa muutamaan kysymykseen elämäntyylistäsi ja löydämme sinulle sopivat rodut.',
        'start_btn': 'Aloita Testi →',
        'question': 'Kysymys', 'of': '/', 'back': 'Takaisin', 'next': 'Seuraava',
        'see_results': 'Näytä Tulokset',
        'your_matches': 'Sinulle Sopivat Rodut',
        'matches_desc': 'Vastaustesi perusteella nämä rodut sopivat sinulle',
        'why_match': 'Miksi tämä sopii sinulle:',
        'view_profile': 'Katso Profiili', 'compare': 'Vertaa Top 2',
        'retake': '← Tee Testi Uudelleen', 'browse': 'Selaa Rotuja', 'quiz': 'Testi',
        'q1': 'Kuinka aktiivinen elämäntyylisi on?',
        'q1_a1': '🛋️ Rauhallinen — Pidän hiljaisista illoista',
        'q1_a2': '🚶 Kohtalainen — Päivittäiset kävelyt sopivat',
        'q1_a3': '🏃 Aktiivinen — Liikun säännöllisesti',
        'q1_a4': '⚡ Erittäin aktiivinen — Ulkoilu on elämäni',
        'q2': 'Kuinka paljon tilaa sinulla on?',
        'q2_a1': '🏢 Pieni kerrostaloasunto', 'q2_a2': '🏠 Talo / isompi asunto',
        'q2_a3': '🏡 Talo pihalla', 'q2_a4': '🌳 Suuri tontti / maaseutu',
        'q3': 'Kenen kanssa koira asuu?',
        'q3_a1': '👤 Vain minun', 'q3_a2': '👫 Minun ja kumppanin',
        'q3_a3': '👨‍👩‍👧 Perhe isompien lasten kanssa', 'q3_a4': '👶 Perhe pienten lasten kanssa',
        'q4': 'Kuinka paljon turkinhoitoa jaksat?',
        'q4_a1': '✨ Minimaalinen — helppohoitoinen kiitos',
        'q4_a2': '🪥 Jonkin verran — viikoittainen harjaus ok',
        'q4_a3': '💇 Säännöllinen — voin sitoutua hoitoon',
        'q4_a4': '🐩 Paljon — nautin turkin hoidosta',
        'q5': 'Minkä kokoisen koiran haluat?',
        'q5_a1': '🐕 Pieni (alle 10 kg)', 'q5_a2': '🐕 Keskikokoinen (10-25 kg)',
        'q5_a3': '🐕 Suuri (25-45 kg)', 'q5_a4': '🐕 Jättiläinen (yli 45 kg)',
        'match_pct': '% Sopivuus',
    },
    'de': {
        'title': 'Finde Deinen Perfekten Hund',
        'badge': '5 schnelle Fragen',
        'subtitle': 'Beantworte ein paar Fragen zu deinem Lebensstil und wir finden passende Rassen.',
        'start_btn': 'Quiz Starten →',
        'question': 'Frage', 'of': 'von', 'back': 'Zurück', 'next': 'Weiter',
        'see_results': 'Ergebnisse Anzeigen',
        'your_matches': 'Deine Perfekten Matches',
        'matches_desc': 'Basierend auf deinen Antworten sind diese Rassen ideal für dich',
        'why_match': 'Warum das zu dir passt:',
        'view_profile': 'Profil Ansehen', 'compare': 'Top 2 Vergleichen',
        'retake': '← Quiz Wiederholen', 'browse': 'Rassen Durchsuchen', 'quiz': 'Quiz',
        'q1': 'Wie aktiv ist dein Lebensstil?',
        'q1_a1': '🛋️ Entspannt — Ich mag ruhige Abende',
        'q1_a2': '🚶 Moderat — Tägliche Spaziergänge sind ok',
        'q1_a3': '🏃 Aktiv — Ich trainiere regelmäßig',
        'q1_a4': '⚡ Sehr Aktiv — Draußen ist mein Leben',
        'q2': 'Wie viel Platz hast du?',
        'q2_a1': '🏢 Kleine Wohnung', 'q2_a2': '🏠 Haus / größere Wohnung',
        'q2_a3': '🏡 Haus mit Garten', 'q2_a4': '🌳 Großes Grundstück / ländlich',
        'q3': 'Mit wem wird der Hund leben?',
        'q3_a1': '👤 Nur ich', 'q3_a2': '👫 Ich und Partner',
        'q3_a3': '👨‍👩‍👧 Familie mit älteren Kindern', 'q3_a4': '👶 Familie mit kleinen Kindern',
        'q4': 'Wie viel Pflege kannst du bewältigen?',
        'q4_a1': '✨ Minimal — pflegeleicht bitte',
        'q4_a2': '🪥 Etwas — wöchentliches Bürsten ok',
        'q4_a3': '💇 Regelmäßig — ich kann mich zur Pflege verpflichten',
        'q4_a4': '🐩 Viel — ich genieße die Pflege',
        'q5': 'Welche Größe bevorzugst du?',
        'q5_a1': '🐕 Klein (unter 10 kg)', 'q5_a2': '🐕 Mittel (10-25 kg)',
        'q5_a3': '🐕 Groß (25-45 kg)', 'q5_a4': '🐕 Riesig (über 45 kg)',
        'match_pct': '% Match',
    },
    'es': {
        'title': 'Encuentra Tu Perro Perfecto',
        'badge': '5 preguntas rápidas',
        'subtitle': 'Responde algunas preguntas sobre tu estilo de vida y te encontraremos razas ideales.',
        'start_btn': 'Comenzar Quiz →',
        'question': 'Pregunta', 'of': 'de', 'back': 'Atrás', 'next': 'Siguiente',
        'see_results': 'Ver Resultados',
        'your_matches': 'Tus Razas Perfectas',
        'matches_desc': 'Según tus respuestas, estas razas son ideales para ti',
        'why_match': 'Por qué te conviene:',
        'view_profile': 'Ver Perfil', 'compare': 'Comparar Top 2',
        'retake': '← Repetir Quiz', 'browse': 'Ver Razas', 'quiz': 'Quiz',
        'q1': '¿Qué tan activo es tu estilo de vida?',
        'q1_a1': '🛋️ Relajado — Prefiero noches tranquilas',
        'q1_a2': '🚶 Moderado — Paseos diarios están bien',
        'q1_a3': '🏃 Activo — Hago ejercicio regularmente',
        'q1_a4': '⚡ Muy Activo — Vivo al aire libre',
        'q2': '¿Cuánto espacio tienes?',
        'q2_a1': '🏢 Apartamento pequeño', 'q2_a2': '🏠 Casa / apartamento grande',
        'q2_a3': '🏡 Casa con jardín', 'q2_a4': '🌳 Propiedad grande / rural',
        'q3': '¿Con quién vivirá el perro?',
        'q3_a1': '👤 Solo yo', 'q3_a2': '👫 Yo y mi pareja',
        'q3_a3': '👨‍👩‍👧 Familia con niños mayores', 'q3_a4': '👶 Familia con niños pequeños',
        'q4': '¿Cuánto aseo puedes manejar?',
        'q4_a1': '✨ Mínimo — bajo mantenimiento por favor',
        'q4_a2': '🪥 Algo — cepillado semanal está bien',
        'q4_a3': '💇 Regular — puedo comprometerme',
        'q4_a4': '🐩 Mucho — disfruto el aseo',
        'q5': '¿Qué tamaño de perro prefieres?',
        'q5_a1': '🐕 Pequeño (menos de 10 kg)', 'q5_a2': '🐕 Mediano (10-25 kg)',
        'q5_a3': '🐕 Grande (25-45 kg)', 'q5_a4': '🐕 Gigante (más de 45 kg)',
        'match_pct': '% Compatibilidad',
    },
    'fr': {
        'title': 'Trouvez Votre Chien Parfait',
        'badge': '5 questions rapides',
        'subtitle': 'Répondez à quelques questions sur votre style de vie et nous trouverons les races idéales.',
        'start_btn': 'Commencer le Quiz →',
        'question': 'Question', 'of': 'sur', 'back': 'Retour', 'next': 'Suivant',
        'see_results': 'Voir les Résultats',
        'your_matches': 'Vos Races Parfaites',
        'matches_desc': 'Selon vos réponses, ces races sont idéales pour vous',
        'why_match': 'Pourquoi ça vous convient:',
        'view_profile': 'Voir le Profil', 'compare': 'Comparer Top 2',
        'retake': '← Refaire le Quiz', 'browse': 'Parcourir les Races', 'quiz': 'Quiz',
        'q1': 'Quel est votre niveau d\'activité?',
        'q1_a1': '🛋️ Détendu — Je préfère les soirées calmes',
        'q1_a2': '🚶 Modéré — Les promenades quotidiennes me conviennent',
        'q1_a3': '🏃 Actif — Je fais de l\'exercice régulièrement',
        'q1_a4': '⚡ Très Actif — Le plein air c\'est ma vie',
        'q2': 'Combien d\'espace avez-vous?',
        'q2_a1': '🏢 Petit appartement', 'q2_a2': '🏠 Maison / grand appartement',
        'q2_a3': '🏡 Maison avec jardin', 'q2_a4': '🌳 Grande propriété / rural',
        'q3': 'Avec qui vivra le chien?',
        'q3_a1': '👤 Juste moi', 'q3_a2': '👫 Moi et mon partenaire',
        'q3_a3': '👨‍👩‍👧 Famille avec enfants plus âgés', 'q3_a4': '👶 Famille avec jeunes enfants',
        'q4': 'Combien de toilettage pouvez-vous gérer?',
        'q4_a1': '✨ Minimal — peu d\'entretien svp',
        'q4_a2': '🪥 Un peu — brossage hebdomadaire ok',
        'q4_a3': '💇 Régulier — je peux m\'engager',
        'q4_a4': '🐩 Beaucoup — j\'aime le toilettage',
        'q5': 'Quelle taille de chien préférez-vous?',
        'q5_a1': '🐕 Petit (moins de 10 kg)', 'q5_a2': '🐕 Moyen (10-25 kg)',
        'q5_a3': '🐕 Grand (25-45 kg)', 'q5_a4': '🐕 Géant (plus de 45 kg)',
        'match_pct': '% Compatibilité',
    },
    'it': {
        'title': 'Trova il Tuo Cane Perfetto',
        'badge': '5 domande veloci',
        'subtitle': 'Rispondi a qualche domanda sul tuo stile di vita e troveremo le razze ideali.',
        'start_btn': 'Inizia il Quiz →',
        'question': 'Domanda', 'of': 'di', 'back': 'Indietro', 'next': 'Avanti',
        'see_results': 'Vedi Risultati',
        'your_matches': 'Le Tue Razze Perfette',
        'matches_desc': 'In base alle tue risposte, queste razze sono ideali per te',
        'why_match': 'Perché fa per te:',
        'view_profile': 'Vedi Profilo', 'compare': 'Confronta Top 2',
        'retake': '← Ripeti Quiz', 'browse': 'Esplora Razze', 'quiz': 'Quiz',
        'q1': 'Quanto è attivo il tuo stile di vita?',
        'q1_a1': '🛋️ Rilassato — Preferisco serate tranquille',
        'q1_a2': '🚶 Moderato — Passeggiate quotidiane vanno bene',
        'q1_a3': '🏃 Attivo — Mi alleno regolarmente',
        'q1_a4': '⚡ Molto Attivo — Vivo all\'aria aperta',
        'q2': 'Quanto spazio hai?',
        'q2_a1': '🏢 Piccolo appartamento', 'q2_a2': '🏠 Casa / appartamento grande',
        'q2_a3': '🏡 Casa con giardino', 'q2_a4': '🌳 Grande proprietà / rurale',
        'q3': 'Con chi vivrà il cane?',
        'q3_a1': '👤 Solo io', 'q3_a2': '👫 Io e partner',
        'q3_a3': '👨‍👩‍👧 Famiglia con figli grandi', 'q3_a4': '👶 Famiglia con bambini piccoli',
        'q4': 'Quanta toelettatura puoi gestire?',
        'q4_a1': '✨ Minima — poca manutenzione per favore',
        'q4_a2': '🪥 Un po\' — spazzolatura settimanale ok',
        'q4_a3': '💇 Regolare — posso impegnarmi',
        'q4_a4': '🐩 Molta — mi piace la toelettatura',
        'q5': 'Che taglia di cane preferisci?',
        'q5_a1': '🐕 Piccolo (sotto 10 kg)', 'q5_a2': '🐕 Medio (10-25 kg)',
        'q5_a3': '🐕 Grande (25-45 kg)', 'q5_a4': '🐕 Gigante (oltre 45 kg)',
        'match_pct': '% Compatibilità',
    },
    'pt': {
        'title': 'Encontre Seu Cão Perfeito',
        'badge': '5 perguntas rápidas',
        'subtitle': 'Responda algumas perguntas sobre seu estilo de vida e encontraremos raças ideais.',
        'start_btn': 'Começar Quiz →',
        'question': 'Pergunta', 'of': 'de', 'back': 'Voltar', 'next': 'Próximo',
        'see_results': 'Ver Resultados',
        'your_matches': 'Suas Raças Perfeitas',
        'matches_desc': 'Com base nas suas respostas, estas raças são ideais para você',
        'why_match': 'Por que combina com você:',
        'view_profile': 'Ver Perfil', 'compare': 'Comparar Top 2',
        'retake': '← Refazer Quiz', 'browse': 'Explorar Raças', 'quiz': 'Quiz',
        'q1': 'Quão ativo é seu estilo de vida?',
        'q1_a1': '🛋️ Relaxado — Prefiro noites tranquilas',
        'q1_a2': '🚶 Moderado — Caminhadas diárias estão bem',
        'q1_a3': '🏃 Ativo — Me exercito regularmente',
        'q1_a4': '⚡ Muito Ativo — Vivo ao ar livre',
        'q2': 'Quanto espaço você tem?',
        'q2_a1': '🏢 Apartamento pequeno', 'q2_a2': '🏠 Casa / apartamento grande',
        'q2_a3': '🏡 Casa com quintal', 'q2_a4': '🌳 Grande propriedade / rural',
        'q3': 'Com quem o cão vai morar?',
        'q3_a1': '👤 Só eu', 'q3_a2': '👫 Eu e parceiro(a)',
        'q3_a3': '👨‍👩‍👧 Família com filhos maiores', 'q3_a4': '👶 Família com crianças pequenas',
        'q4': 'Quanta tosa você pode fazer?',
        'q4_a1': '✨ Mínima — baixa manutenção por favor',
        'q4_a2': '🪥 Alguma — escovação semanal ok',
        'q4_a3': '💇 Regular — posso me comprometer',
        'q4_a4': '🐩 Muita — gosto de tosar',
        'q5': 'Qual tamanho de cão você prefere?',
        'q5_a1': '🐕 Pequeno (menos de 10 kg)', 'q5_a2': '🐕 Médio (10-25 kg)',
        'q5_a3': '🐕 Grande (25-45 kg)', 'q5_a4': '🐕 Gigante (mais de 45 kg)',
        'match_pct': '% Compatibilidade',
    },
    'nl': {
        'title': 'Vind Je Perfecte Hond',
        'badge': '5 snelle vragen',
        'subtitle': 'Beantwoord een paar vragen over je levensstijl en we vinden de ideale rassen.',
        'start_btn': 'Start Quiz →',
        'question': 'Vraag', 'of': 'van', 'back': 'Terug', 'next': 'Volgende',
        'see_results': 'Bekijk Resultaten',
        'your_matches': 'Jouw Perfecte Matches',
        'matches_desc': 'Op basis van je antwoorden zijn deze rassen ideaal voor jou',
        'why_match': 'Waarom dit bij je past:',
        'view_profile': 'Bekijk Profiel', 'compare': 'Vergelijk Top 2',
        'retake': '← Quiz Opnieuw', 'browse': 'Rassen Bekijken', 'quiz': 'Quiz',
        'q1': 'Hoe actief is je levensstijl?',
        'q1_a1': '🛋️ Ontspannen — Ik hou van rustige avonden',
        'q1_a2': '🚶 Matig — Dagelijkse wandelingen zijn prima',
        'q1_a3': '🏃 Actief — Ik sport regelmatig',
        'q1_a4': '⚡ Zeer Actief — Buiten is mijn leven',
        'q2': 'Hoeveel ruimte heb je?',
        'q2_a1': '🏢 Klein appartement', 'q2_a2': '🏠 Huis / groot appartement',
        'q2_a3': '🏡 Huis met tuin', 'q2_a4': '🌳 Groot terrein / landelijk',
        'q3': 'Met wie gaat de hond leven?',
        'q3_a1': '👤 Alleen ik', 'q3_a2': '👫 Ik en partner',
        'q3_a3': '👨‍👩‍👧 Gezin met oudere kinderen', 'q3_a4': '👶 Gezin met jonge kinderen',
        'q4': 'Hoeveel verzorging kun je aan?',
        'q4_a1': '✨ Minimaal — weinig onderhoud graag',
        'q4_a2': '🪥 Wat — wekelijks borstelen is ok',
        'q4_a3': '💇 Regelmatig — ik kan me toewijden',
        'q4_a4': '🐩 Veel — ik geniet van verzorgen',
        'q5': 'Welke maat hond heb je liever?',
        'q5_a1': '🐕 Klein (onder 10 kg)', 'q5_a2': '🐕 Middel (10-25 kg)',
        'q5_a3': '🐕 Groot (25-45 kg)', 'q5_a4': '🐕 Reus (boven 45 kg)',
        'match_pct': '% Match',
    },
    'pl': {
        'title': 'Znajdź Swojego Idealnego Psa',
        'badge': '5 szybkich pytań',
        'subtitle': 'Odpowiedz na kilka pytań o swoim stylu życia, a znajdziemy idealne rasy.',
        'start_btn': 'Rozpocznij Quiz →',
        'question': 'Pytanie', 'of': 'z', 'back': 'Wstecz', 'next': 'Dalej',
        'see_results': 'Zobacz Wyniki',
        'your_matches': 'Twoje Idealne Rasy',
        'matches_desc': 'Na podstawie twoich odpowiedzi, te rasy są idealne dla ciebie',
        'why_match': 'Dlaczego to pasuje:',
        'view_profile': 'Zobacz Profil', 'compare': 'Porównaj Top 2',
        'retake': '← Powtórz Quiz', 'browse': 'Przeglądaj Rasy', 'quiz': 'Quiz',
        'q1': 'Jak aktywny jest twój styl życia?',
        'q1_a1': '🛋️ Spokojny — Wolę ciche wieczory',
        'q1_a2': '🚶 Umiarkowany — Codzienne spacery są ok',
        'q1_a3': '🏃 Aktywny — Ćwiczę regularnie',
        'q1_a4': '⚡ Bardzo Aktywny — Żyję na świeżym powietrzu',
        'q2': 'Ile masz miejsca?',
        'q2_a1': '🏢 Małe mieszkanie', 'q2_a2': '🏠 Dom / duże mieszkanie',
        'q2_a3': '🏡 Dom z ogrodem', 'q2_a4': '🌳 Duża posiadłość / wieś',
        'q3': 'Z kim będzie mieszkał pies?',
        'q3_a1': '👤 Tylko ja', 'q3_a2': '👫 Ja i partner',
        'q3_a3': '👨‍👩‍👧 Rodzina ze starszymi dziećmi', 'q3_a4': '👶 Rodzina z małymi dziećmi',
        'q4': 'Ile pielęgnacji możesz zapewnić?',
        'q4_a1': '✨ Minimalna — mało wymagająca proszę',
        'q4_a2': '🪥 Trochę — tygodniowe szczotkowanie ok',
        'q4_a3': '💇 Regularna — mogę się zaangażować',
        'q4_a4': '🐩 Dużo — lubię pielęgnować',
        'q5': 'Jaki rozmiar psa wolisz?',
        'q5_a1': '🐕 Mały (poniżej 10 kg)', 'q5_a2': '🐕 Średni (10-25 kg)',
        'q5_a3': '🐕 Duży (25-45 kg)', 'q5_a4': '🐕 Olbrzym (powyżej 45 kg)',
        'match_pct': '% Dopasowanie',
    },
    'sv': {
        'title': 'Hitta Din Perfekta Hund',
        'badge': '5 snabba frågor',
        'subtitle': 'Svara på några frågor om din livsstil så hittar vi de ideala raserna.',
        'start_btn': 'Starta Quiz →',
        'question': 'Fråga', 'of': 'av', 'back': 'Tillbaka', 'next': 'Nästa',
        'see_results': 'Se Resultat',
        'your_matches': 'Dina Perfekta Matcher',
        'matches_desc': 'Baserat på dina svar är dessa raser ideala för dig',
        'why_match': 'Varför detta passar dig:',
        'view_profile': 'Se Profil', 'compare': 'Jämför Top 2',
        'retake': '← Gör Om Quiz', 'browse': 'Bläddra Raser', 'quiz': 'Quiz',
        'q1': 'Hur aktiv är din livsstil?',
        'q1_a1': '🛋️ Avslappnad — Jag föredrar lugna kvällar',
        'q1_a2': '🚶 Måttlig — Dagliga promenader är ok',
        'q1_a3': '🏃 Aktiv — Jag tränar regelbundet',
        'q1_a4': '⚡ Mycket Aktiv — Utomhus är mitt liv',
        'q2': 'Hur mycket utrymme har du?',
        'q2_a1': '🏢 Liten lägenhet', 'q2_a2': '🏠 Hus / stor lägenhet',
        'q2_a3': '🏡 Hus med trädgård', 'q2_a4': '🌳 Stor tomt / lantligt',
        'q3': 'Vem kommer hunden bo med?',
        'q3_a1': '👤 Bara jag', 'q3_a2': '👫 Jag och partner',
        'q3_a3': '👨‍👩‍👧 Familj med äldre barn', 'q3_a4': '👶 Familj med små barn',
        'q4': 'Hur mycket pälsvård klarar du?',
        'q4_a1': '✨ Minimal — lågunderhåll tack',
        'q4_a2': '🪥 Lite — veckovis borstning ok',
        'q4_a3': '💇 Regelbunden — jag kan engagera mig',
        'q4_a4': '🐩 Mycket — jag gillar pälsvård',
        'q5': 'Vilken storlek hund föredrar du?',
        'q5_a1': '🐕 Liten (under 10 kg)', 'q5_a2': '🐕 Medel (10-25 kg)',
        'q5_a3': '🐕 Stor (25-45 kg)', 'q5_a4': '🐕 Jätte (över 45 kg)',
        'match_pct': '% Match',
    },
    'no': {
        'title': 'Finn Din Perfekte Hund',
        'badge': '5 raske spørsmål',
        'subtitle': 'Svar på noen spørsmål om livsstilen din, så finner vi de ideelle rasene.',
        'start_btn': 'Start Quiz →',
        'question': 'Spørsmål', 'of': 'av', 'back': 'Tilbake', 'next': 'Neste',
        'see_results': 'Se Resultater',
        'your_matches': 'Dine Perfekte Matcher',
        'matches_desc': 'Basert på svarene dine er disse rasene ideelle for deg',
        'why_match': 'Hvorfor dette passer deg:',
        'view_profile': 'Se Profil', 'compare': 'Sammenlign Top 2',
        'retake': '← Ta Quiz På Nytt', 'browse': 'Bla Gjennom Raser', 'quiz': 'Quiz',
        'q1': 'Hvor aktiv er livsstilen din?',
        'q1_a1': '🛋️ Avslappet — Jeg foretrekker rolige kvelder',
        'q1_a2': '🚶 Moderat — Daglige turer er greit',
        'q1_a3': '🏃 Aktiv — Jeg trener regelmessig',
        'q1_a4': '⚡ Veldig Aktiv — Utendørs er livet mitt',
        'q2': 'Hvor mye plass har du?',
        'q2_a1': '🏢 Liten leilighet', 'q2_a2': '🏠 Hus / stor leilighet',
        'q2_a3': '🏡 Hus med hage', 'q2_a4': '🌳 Stor tomt / landlig',
        'q3': 'Hvem skal hunden bo med?',
        'q3_a1': '👤 Bare meg', 'q3_a2': '👫 Meg og partner',
        'q3_a3': '👨‍👩‍👧 Familie med eldre barn', 'q3_a4': '👶 Familie med små barn',
        'q4': 'Hvor mye stell klarer du?',
        'q4_a1': '✨ Minimalt — lite vedlikehold takk',
        'q4_a2': '🪥 Litt — ukentlig børsting ok',
        'q4_a3': '💇 Regelmessig — jeg kan forplikte meg',
        'q4_a4': '🐩 Mye — jeg liker stell',
        'q5': 'Hvilken størrelse hund foretrekker du?',
        'q5_a1': '🐕 Liten (under 10 kg)', 'q5_a2': '🐕 Middels (10-25 kg)',
        'q5_a3': '🐕 Stor (25-45 kg)', 'q5_a4': '🐕 Kjempe (over 45 kg)',
        'match_pct': '% Match',
    },
    'da': {
        'title': 'Find Din Perfekte Hund',
        'badge': '5 hurtige spørgsmål',
        'subtitle': 'Besvar et par spørgsmål om din livsstil, og vi finder de ideelle racer.',
        'start_btn': 'Start Quiz →',
        'question': 'Spørgsmål', 'of': 'af', 'back': 'Tilbage', 'next': 'Næste',
        'see_results': 'Se Resultater',
        'your_matches': 'Dine Perfekte Matches',
        'matches_desc': 'Baseret på dine svar er disse racer ideelle for dig',
        'why_match': 'Hvorfor dette passer dig:',
        'view_profile': 'Se Profil', 'compare': 'Sammenlign Top 2',
        'retake': '← Tag Quiz Igen', 'browse': 'Gennemse Racer', 'quiz': 'Quiz',
        'q1': 'Hvor aktiv er din livsstil?',
        'q1_a1': '🛋️ Afslappet — Jeg foretrækker rolige aftener',
        'q1_a2': '🚶 Moderat — Daglige gåture er fint',
        'q1_a3': '🏃 Aktiv — Jeg træner regelmæssigt',
        'q1_a4': '⚡ Meget Aktiv — Udendørs er mit liv',
        'q2': 'Hvor meget plads har du?',
        'q2_a1': '🏢 Lille lejlighed', 'q2_a2': '🏠 Hus / stor lejlighed',
        'q2_a3': '🏡 Hus med have', 'q2_a4': '🌳 Stor grund / landligt',
        'q3': 'Hvem skal hunden bo med?',
        'q3_a1': '👤 Kun mig', 'q3_a2': '👫 Mig og partner',
        'q3_a3': '👨‍👩‍👧 Familie med ældre børn', 'q3_a4': '👶 Familie med små børn',
        'q4': 'Hvor meget pleje kan du klare?',
        'q4_a1': '✨ Minimal — lidt vedligeholdelse tak',
        'q4_a2': '🪥 Lidt — ugentlig børstning ok',
        'q4_a3': '💇 Regelmæssig — jeg kan forpligte mig',
        'q4_a4': '🐩 Meget — jeg nyder pleje',
        'q5': 'Hvilken størrelse hund foretrækker du?',
        'q5_a1': '🐕 Lille (under 10 kg)', 'q5_a2': '🐕 Mellem (10-25 kg)',
        'q5_a3': '🐕 Stor (25-45 kg)', 'q5_a4': '🐕 Kæmpe (over 45 kg)',
        'match_pct': '% Match',
    },
    'zh': {
        'title': '找到您的完美狗狗',
        'badge': '5个快速问题',
        'subtitle': '回答几个关于您生活方式的问题，我们将为您找到理想的品种。',
        'start_btn': '开始测验 →',
        'question': '问题', 'of': '/', 'back': '返回', 'next': '下一个',
        'see_results': '查看结果',
        'your_matches': '您的完美匹配',
        'matches_desc': '根据您的回答，这些品种非常适合您',
        'why_match': '为什么适合您：',
        'view_profile': '查看资料', 'compare': '比较前2名',
        'retake': '← 重新测验', 'browse': '浏览品种', 'quiz': '测验',
        'q1': '您的生活方式有多活跃？',
        'q1_a1': '🛋️ 放松 — 我喜欢安静的夜晚',
        'q1_a2': '🚶 适度 — 每天散步就好',
        'q1_a3': '🏃 活跃 — 我定期锻炼',
        'q1_a4': '⚡ 非常活跃 — 户外是我的生活',
        'q2': '您有多少空间？',
        'q2_a1': '🏢 小公寓', 'q2_a2': '🏠 房子/大公寓',
        'q2_a3': '🏡 带院子的房子', 'q2_a4': '🌳 大型房产/乡村',
        'q3': '狗狗将和谁一起生活？',
        'q3_a1': '👤 只有我', 'q3_a2': '👫 我和伴侣',
        'q3_a3': '👨‍👩‍👧 有大孩子的家庭', 'q3_a4': '👶 有小孩子的家庭',
        'q4': '您能处理多少美容工作？',
        'q4_a1': '✨ 最少 — 低维护请',
        'q4_a2': '🪥 一些 — 每周刷毛可以',
        'q4_a3': '💇 定期 — 我可以承诺',
        'q4_a4': '🐩 很多 — 我喜欢美容',
        'q5': '您喜欢多大的狗？',
        'q5_a1': '🐕 小型（10公斤以下）', 'q5_a2': '🐕 中型（10-25公斤）',
        'q5_a3': '🐕 大型（25-45公斤）', 'q5_a4': '🐕 巨型（45公斤以上）',
        'match_pct': '% 匹配',
    },
    'ja': {
        'title': 'あなたにぴったりの犬を見つけよう',
        'badge': '5つの簡単な質問',
        'subtitle': 'ライフスタイルについていくつかの質問に答えると、理想的な犬種をご提案します。',
        'start_btn': 'クイズを始める →',
        'question': '質問', 'of': '/', 'back': '戻る', 'next': '次へ',
        'see_results': '結果を見る',
        'your_matches': 'あなたにぴったりの犬種',
        'matches_desc': 'あなたの回答に基づいて、これらの犬種が理想的です',
        'why_match': 'おすすめの理由：',
        'view_profile': 'プロフィールを見る', 'compare': 'トップ2を比較',
        'retake': '← クイズをやり直す', 'browse': '犬種を見る', 'quiz': 'クイズ',
        'q1': 'あなたのライフスタイルはどのくらい活動的ですか？',
        'q1_a1': '🛋️ リラックス — 静かな夜が好き',
        'q1_a2': '🚶 普通 — 毎日の散歩で十分',
        'q1_a3': '🏃 アクティブ — 定期的に運動する',
        'q1_a4': '⚡ とてもアクティブ — アウトドアが大好き',
        'q2': 'どのくらいのスペースがありますか？',
        'q2_a1': '🏢 小さなアパート', 'q2_a2': '🏠 家/大きなアパート',
        'q2_a3': '🏡 庭付きの家', 'q2_a4': '🌳 広い敷地/田舎',
        'q3': '犬は誰と暮らしますか？',
        'q3_a1': '👤 私だけ', 'q3_a2': '👫 私とパートナー',
        'q3_a3': '👨‍👩‍👧 年上の子供がいる家族', 'q3_a4': '👶 小さな子供がいる家族',
        'q4': 'どのくらいグルーミングできますか？',
        'q4_a1': '✨ 最小限 — 手入れが簡単なのがいい',
        'q4_a2': '🪥 少し — 週1回のブラッシングはOK',
        'q4_a3': '💇 定期的 — しっかりお手入れできる',
        'q4_a4': '🐩 たくさん — グルーミングが好き',
        'q5': 'どのサイズの犬が好きですか？',
        'q5_a1': '🐕 小型（10kg未満）', 'q5_a2': '🐕 中型（10-25kg）',
        'q5_a3': '🐕 大型（25-45kg）', 'q5_a4': '🐕 超大型（45kg以上）',
        'match_pct': '% マッチ',
    },
    'ru': {
        'title': 'Найдите Свою Идеальную Собаку',
        'badge': '5 быстрых вопросов',
        'subtitle': 'Ответьте на несколько вопросов о вашем образе жизни, и мы подберём идеальные породы.',
        'start_btn': 'Начать Тест →',
        'question': 'Вопрос', 'of': 'из', 'back': 'Назад', 'next': 'Далее',
        'see_results': 'Показать Результаты',
        'your_matches': 'Ваши Идеальные Породы',
        'matches_desc': 'На основе ваших ответов эти породы идеально вам подходят',
        'why_match': 'Почему это вам подходит:',
        'view_profile': 'Смотреть Профиль', 'compare': 'Сравнить Топ-2',
        'retake': '← Пройти Снова', 'browse': 'Смотреть Породы', 'quiz': 'Тест',
        'q1': 'Насколько активен ваш образ жизни?',
        'q1_a1': '🛋️ Спокойный — Предпочитаю тихие вечера',
        'q1_a2': '🚶 Умеренный — Ежедневные прогулки подходят',
        'q1_a3': '🏃 Активный — Регулярно занимаюсь спортом',
        'q1_a4': '⚡ Очень Активный — Живу на свежем воздухе',
        'q2': 'Сколько у вас места?',
        'q2_a1': '🏢 Маленькая квартира', 'q2_a2': '🏠 Дом / большая квартира',
        'q2_a3': '🏡 Дом с двором', 'q2_a4': '🌳 Большой участок / сельская местность',
        'q3': 'С кем будет жить собака?',
        'q3_a1': '👤 Только я', 'q3_a2': '👫 Я и партнёр',
        'q3_a3': '👨‍👩‍👧 Семья со старшими детьми', 'q3_a4': '👶 Семья с маленькими детьми',
        'q4': 'Сколько ухода вы можете обеспечить?',
        'q4_a1': '✨ Минимальный — мало ухода пожалуйста',
        'q4_a2': '🪥 Немного — еженедельное расчёсывание ок',
        'q4_a3': '💇 Регулярный — могу посвятить время',
        'q4_a4': '🐩 Много — мне нравится уход',
        'q5': 'Какой размер собаки вы предпочитаете?',
        'q5_a1': '🐕 Маленькая (до 10 кг)', 'q5_a2': '🐕 Средняя (10-25 кг)',
        'q5_a3': '🐕 Большая (25-45 кг)', 'q5_a4': '🐕 Гигантская (более 45 кг)',
        'match_pct': '% Совпадение',
    },
}


def generate_quiz_html(lang, t, breeds_js):
    """Generate quiz HTML for a language"""
    
    depth = '../' if lang == 'en' else '../../'
    
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{t['title']} | BreedFinder</title>
    <link rel="icon" href="{depth}favicon.ico">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    </style>
</head>
<body class="bg-gradient-to-br from-sky-50 via-white to-violet-50 min-h-screen text-slate-800">
    <header class="bg-white/80 backdrop-blur-md border-b border-slate-100 sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
            <a href="../" class="flex items-center gap-3">
                <img src="{depth}logo-192.png" class="w-10 h-10" alt="BreedFinder">
                <span class="text-xl font-bold text-slate-800">BreedFinder</span>
            </a>
            <nav class="flex items-center gap-4 text-sm font-medium">
                <a href="../search/" class="hidden md:block text-slate-600 hover:text-sky-600">{t['browse']}</a>
                <a href="./" class="bg-gradient-to-r from-sky-500 to-violet-500 text-white px-4 py-2 rounded-xl">{t['quiz']}</a>
            </nav>
        </div>
    </header>

    <main class="max-w-2xl mx-auto px-4 py-12">
        <div id="quiz-container">
            <div id="quiz-intro" class="text-center">
                <div class="inline-flex items-center gap-2 bg-white px-4 py-2 rounded-full shadow-sm border text-sm text-slate-600 mb-6">
                    <span>🎯</span>
                    <span>{t['badge']}</span>
                </div>
                <h1 class="text-4xl md:text-5xl font-extrabold mb-4">
                    <span class="bg-gradient-to-r from-sky-500 to-violet-500 bg-clip-text text-transparent">{t['title']}</span>
                </h1>
                <p class="text-lg text-slate-600 mb-8">{t['subtitle']}</p>
                <button onclick="startQuiz()" class="bg-gradient-to-r from-sky-500 to-violet-500 text-white px-8 py-4 rounded-2xl font-bold text-lg hover:shadow-xl transition">
                    {t['start_btn']}
                </button>
            </div>

            <div id="quiz-questions" class="hidden">
                <div class="bg-white rounded-3xl shadow-xl p-8">
                    <div class="mb-8">
                        <div class="flex justify-between text-sm text-slate-500 mb-2">
                            <span>{t['question']} <span id="current-q">1</span> {t['of']} 5</span>
                            <span id="progress-text">20%</span>
                        </div>
                        <div class="h-2 bg-slate-100 rounded-full overflow-hidden">
                            <div id="progress-bar" class="h-full bg-gradient-to-r from-sky-500 to-violet-500 transition-all duration-300" style="width: 20%"></div>
                        </div>
                    </div>
                    <h2 id="question-text" class="text-2xl font-bold mb-6"></h2>
                    <div id="answers" class="space-y-3"></div>
                    <div class="flex justify-between mt-8">
                        <button id="back-btn" onclick="prevQuestion()" class="px-6 py-3 text-slate-600 hover:text-slate-800 hidden">{t['back']}</button>
                        <button id="next-btn" onclick="nextQuestion()" class="ml-auto bg-gradient-to-r from-sky-500 to-violet-500 text-white px-6 py-3 rounded-xl font-semibold disabled:opacity-50" disabled>{t['next']}</button>
                    </div>
                </div>
            </div>

            <div id="quiz-results" class="hidden">
                <div class="text-center mb-8">
                    <h2 class="text-3xl font-extrabold mb-2">{t['your_matches']}</h2>
                    <p class="text-slate-600">{t['matches_desc']}</p>
                </div>
                <div id="results-list" class="space-y-4"></div>
                <div class="flex justify-center gap-4 mt-8">
                    <button onclick="location.reload()" class="px-6 py-3 border border-slate-200 rounded-xl hover:bg-slate-50">{t['retake']}</button>
                    <a href="../compare/" id="compare-link" class="px-6 py-3 bg-gradient-to-r from-sky-500 to-violet-500 text-white rounded-xl font-semibold">{t['compare']}</a>
                </div>
            </div>
        </div>
    </main>

    <script>
        const questions = [
            {{ q: "{t['q1']}", answers: ["{t['q1_a1']}", "{t['q1_a2']}", "{t['q1_a3']}", "{t['q1_a4']}"], tags: [["low-energy"], ["moderate-energy"], ["high-energy"], ["high-energy"]] }},
            {{ q: "{t['q2']}", answers: ["{t['q2_a1']}", "{t['q2_a2']}", "{t['q2_a3']}", "{t['q2_a4']}"], tags: [["apartment", "small"], ["medium"], ["large"], ["large"]] }},
            {{ q: "{t['q3']}", answers: ["{t['q3_a1']}", "{t['q3_a2']}", "{t['q3_a3']}", "{t['q3_a4']}"], tags: [[], [], ["family-friendly"], ["family-friendly"]] }},
            {{ q: "{t['q4']}", answers: ["{t['q4_a1']}", "{t['q4_a2']}", "{t['q4_a3']}", "{t['q4_a4']}"], tags: [["low-grooming"], [], [], ["high-grooming"]] }},
            {{ q: "{t['q5']}", answers: ["{t['q5_a1']}", "{t['q5_a2']}", "{t['q5_a3']}", "{t['q5_a4']}"], tags: [["small"], ["medium"], ["large"], ["large"]] }}
        ];

        const breeds = [
{breeds_js}
        ];

        let currentQ = 0;
        let answers = [];
        let selectedTags = [];

        function startQuiz() {{
            document.getElementById('quiz-intro').classList.add('hidden');
            document.getElementById('quiz-questions').classList.remove('hidden');
            showQuestion(0);
        }}

        function showQuestion(idx) {{
            const q = questions[idx];
            document.getElementById('question-text').textContent = q.q;
            document.getElementById('current-q').textContent = idx + 1;
            document.getElementById('progress-bar').style.width = ((idx + 1) * 20) + '%';
            document.getElementById('progress-text').textContent = ((idx + 1) * 20) + '%';
            
            const answersDiv = document.getElementById('answers');
            answersDiv.innerHTML = q.answers.map((a, i) => `
                <button onclick="selectAnswer(${{i}})" class="answer-btn w-full text-left p-4 rounded-xl border-2 border-slate-200 hover:border-sky-400 transition ${{answers[idx] === i ? 'border-sky-500 bg-sky-50' : ''}}">
                    ${{a}}
                </button>
            `).join('');
            
            document.getElementById('back-btn').classList.toggle('hidden', idx === 0);
            document.getElementById('next-btn').textContent = idx === 4 ? '{t['see_results']}' : '{t['next']}';
            document.getElementById('next-btn').disabled = answers[idx] === undefined;
        }}

        function selectAnswer(idx) {{
            answers[currentQ] = idx;
            selectedTags[currentQ] = questions[currentQ].tags[idx];
            document.querySelectorAll('.answer-btn').forEach((btn, i) => {{
                btn.classList.toggle('border-sky-500', i === idx);
                btn.classList.toggle('bg-sky-50', i === idx);
            }});
            document.getElementById('next-btn').disabled = false;
        }}

        function nextQuestion() {{
            if (currentQ < 4) {{
                currentQ++;
                showQuestion(currentQ);
            }} else {{
                showResults();
            }}
        }}

        function prevQuestion() {{
            if (currentQ > 0) {{
                currentQ--;
                showQuestion(currentQ);
            }}
        }}

        function showResults() {{
            document.getElementById('quiz-questions').classList.add('hidden');
            document.getElementById('quiz-results').classList.remove('hidden');
            
            const userTags = selectedTags.flat();
            const scored = breeds.map(b => {{
                const matches = b.tags.filter(t => userTags.includes(t)).length;
                return {{ ...b, score: matches, pct: Math.round((matches / Math.max(userTags.length, 1)) * 100) }};
            }}).sort((a, b) => b.score - a.score).slice(0, 5);
            
            document.getElementById('results-list').innerHTML = scored.map((b, i) => `
                <div class="bg-white rounded-2xl p-6 shadow-sm border flex gap-4 items-center">
                    <img src="{depth}images/heads/${{b.slug}}.webp" class="w-20 h-20 rounded-xl object-cover" alt="${{b.name}}">
                    <div class="flex-1">
                        <div class="flex items-center gap-2 mb-1">
                            <span class="text-xl font-bold">${{b.name}}</span>
                            <span class="bg-gradient-to-r from-sky-500 to-violet-500 text-white text-xs px-2 py-1 rounded-full">${{b.pct}}{t['match_pct']}</span>
                        </div>
                        <p class="text-sm text-slate-600">{t['why_match']} ${{b.tags.filter(t => userTags.includes(t)).join(', ')}}</p>
                    </div>
                    <a href="../breeds/${{b.slug}}.html" class="text-sky-600 hover:text-sky-700 font-semibold text-sm">{t['view_profile']} →</a>
                </div>
            `).join('');
            
            if (scored.length >= 2) {{
                document.getElementById('compare-link').href = `../compare/?breed1=${{scored[0].slug}}&breed2=${{scored[1].slug}}`;
            }}
        }}
    </script>
</body>
</html>'''


def main():
    base_dir = Path(__file__).parent.parent
    
    # Load breeds data
    with open(base_dir / 'data' / 'breeds.json') as f:
        breeds = json.load(f)
    
    # Generate breeds JS
    def get_tags(b):
        tags = []
        r = b.get('ratings', {})
        energy = r.get('energy', 3)
        if energy >= 4: tags.append('high-energy')
        elif energy <= 2: tags.append('low-energy')
        else: tags.append('moderate-energy')
        
        size = b.get('size', {}).get('category', 'medium')
        if size in ['tiny', 'small']: tags.append('small')
        elif size == 'medium': tags.append('medium')
        else: tags.append('large')
        
        if r.get('kid_friendly', 3) >= 4: tags.append('family-friendly')
        if r.get('apartment_ok', 3) >= 4: tags.append('apartment')
        if r.get('grooming', 3) <= 2: tags.append('low-grooming')
        elif r.get('grooming', 3) >= 4: tags.append('high-grooming')
        
        return tags
    
    breeds_entries = []
    for b in breeds:
        tags = get_tags(b)
        breeds_entries.append(f'            {{ name: "{b["name"]}", slug: "{b["id"]}", tags: {json.dumps(tags)} }}')
    breeds_js = ',\n'.join(breeds_entries)
    
    print("Generating translated quiz pages...")
    
    for lang in LANGUAGES:
        t = T.get(lang, T['en'])
        lang_dir = base_dir / lang / 'quiz'
        lang_dir.mkdir(parents=True, exist_ok=True)
        
        html = generate_quiz_html(lang, t, breeds_js)
        with open(lang_dir / 'index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  Created {lang}/quiz/index.html")
    
    print(f"\n✅ Done! Created {len(LANGUAGES)} quiz pages")


if __name__ == '__main__':
    main()
