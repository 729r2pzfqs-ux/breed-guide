#!/usr/bin/env python3
"""
Generate translated article pages for all 14 languages
"""

import json
from pathlib import Path

LANGUAGES = ['es', 'de', 'fr', 'it', 'pt', 'nl', 'pl', 'zh', 'ja', 'fi', 'sv', 'no', 'da', 'ru']

# Common UI translations
UI = {
    'en': {'back': '← Back', 'quiz_btn': 'Take the Breed Quiz →', 'compare_btn': 'Compare Breeds', 'footer': '© 2026 BreedFinder. Made with care for dog lovers everywhere.'},
    'fi': {'back': '← Takaisin', 'quiz_btn': 'Tee Rotutesti →', 'compare_btn': 'Vertaile Rotuja', 'footer': '© 2026 BreedFinder. Tehty rakkaudella koiraystäville.'},
    'de': {'back': '← Zurück', 'quiz_btn': 'Mach das Quiz →', 'compare_btn': 'Rassen Vergleichen', 'footer': '© 2026 BreedFinder. Mit Liebe für Hundefreunde.'},
    'es': {'back': '← Volver', 'quiz_btn': 'Hacer el Quiz →', 'compare_btn': 'Comparar Razas', 'footer': '© 2026 BreedFinder. Hecho con amor para los amantes de los perros.'},
    'fr': {'back': '← Retour', 'quiz_btn': 'Faire le Quiz →', 'compare_btn': 'Comparer les Races', 'footer': '© 2026 BreedFinder. Fait avec amour pour les amoureux des chiens.'},
    'it': {'back': '← Indietro', 'quiz_btn': 'Fai il Quiz →', 'compare_btn': 'Confronta Razze', 'footer': '© 2026 BreedFinder. Fatto con amore per gli amanti dei cani.'},
    'pt': {'back': '← Voltar', 'quiz_btn': 'Fazer o Quiz →', 'compare_btn': 'Comparar Raças', 'footer': '© 2026 BreedFinder. Feito com carinho para os amantes de cães.'},
    'nl': {'back': '← Terug', 'quiz_btn': 'Doe de Quiz →', 'compare_btn': 'Rassen Vergelijken', 'footer': '© 2026 BreedFinder. Gemaakt met liefde voor hondenliefhebbers.'},
    'pl': {'back': '← Wstecz', 'quiz_btn': 'Zrób Quiz →', 'compare_btn': 'Porównaj Rasy', 'footer': '© 2026 BreedFinder. Stworzone z miłością dla miłośników psów.'},
    'sv': {'back': '← Tillbaka', 'quiz_btn': 'Gör Quizet →', 'compare_btn': 'Jämför Raser', 'footer': '© 2026 BreedFinder. Gjord med kärlek för hundälskare.'},
    'no': {'back': '← Tilbake', 'quiz_btn': 'Ta Quizen →', 'compare_btn': 'Sammenlign Raser', 'footer': '© 2026 BreedFinder. Laget med kjærlighet for hundeelskere.'},
    'da': {'back': '← Tilbage', 'quiz_btn': 'Tag Quizzen →', 'compare_btn': 'Sammenlign Racer', 'footer': '© 2026 BreedFinder. Lavet med kærlighed til hundeelskere.'},
    'zh': {'back': '← 返回', 'quiz_btn': '参加测验 →', 'compare_btn': '比较品种', 'footer': '© 2026 BreedFinder. 为爱狗人士精心制作。'},
    'ja': {'back': '← 戻る', 'quiz_btn': 'クイズに挑戦 →', 'compare_btn': '犬種を比較', 'footer': '© 2026 BreedFinder. 犬好きのために愛を込めて。'},
    'ru': {'back': '← Назад', 'quiz_btn': 'Пройти тест →', 'compare_btn': 'Сравнить породы', 'footer': '© 2026 BreedFinder. Сделано с любовью для любителей собак.'},
}

# APARTMENTS ARTICLE
APARTMENTS = {
    'en': {
        'slug': 'best-dogs-for-apartments', 'badge': 'GUIDE', 'badge_color': 'sky',
        'title': '15 Best Dog Breeds for Apartments',
        'meta_desc': 'Looking for apartment-friendly dogs? These 15 breeds thrive in small spaces.',
        'subtitle': "Think you need a house with a yard? These breeds thrive in cozy spaces.",
        'intro': "Living in an apartment doesn't mean you can't have a dog. The key factors are <strong>energy level, barking tendency, and adaptability</strong>.",
        'tip_box': '<strong>Surprising fact:</strong> Some large breeds like Greyhounds make excellent apartment dogs, while small breeds like Jack Russells need lots of space.',
        'sec1_title': '🏆 Top 5 Apartment Dogs',
        'sec2_title': '🐕 Medium-Sized Apartment Dogs', 
        'sec3_title': '🦴 Large Apartment Dogs',
        'quiet_title': '🔇 Quietest Breeds', 'quiet_intro': 'These breeds rarely bark:',
        'avoid_title': '⚠️ Breeds to Avoid', 'avoid_intro': 'High energy or barking issues:',
        'tips_title': '💡 Tips for Apartment Owners',
        'cta_title': 'Find Your Match', 'cta_text': 'Take our quiz to find your perfect apartment dog.',
    },
    'fi': {
        'slug': 'parhaat-kerrostalokoirat', 'badge': 'OPAS', 'badge_color': 'sky',
        'title': '15 Parasta Koirarotua Kerrostaloon',
        'meta_desc': 'Etsitkö kerrostaloon sopivaa koiraa? Nämä 15 rotua viihtyvät pienissä tiloissa.',
        'subtitle': 'Nämä rodut viihtyvät kodikkaissa tiloissa ilman pihaa.',
        'intro': 'Kerrostalossa asuminen ei tarkoita, ettet voisi omistaa koiraa. Tärkeimmät tekijät ovat <strong>energiataso, haukkumisalttius ja sopeutuvuus</strong>.',
        'tip_box': '<strong>Yllättävä fakta:</strong> Jotkut suuret rodut kuten Vinttikoirat ovat erinomaisia kerrostalokoiria, kun taas pienet rodut kuten Jack Russellit tarvitsevat paljon tilaa.',
        'sec1_title': '🏆 Top 5 Kerrostalokoiraa',
        'sec2_title': '🐕 Keskikokoiset Kerrostalokoirat',
        'sec3_title': '🦴 Suuret Kerrostalokoirat',
        'quiet_title': '🔇 Hiljaisimmat Rodut', 'quiet_intro': 'Nämä rodut haukkuvat harvoin:',
        'avoid_title': '⚠️ Vältettävät Rodut', 'avoid_intro': 'Korkea energia tai haukkumisongelma:',
        'tips_title': '💡 Vinkkejä Kerrostaloasujalle',
        'cta_title': 'Löydä Sopivasi', 'cta_text': 'Tee testimme löytääksesi täydellisen kerrostalokoiran.',
    },
    'de': {
        'slug': 'beste-hunde-fuer-wohnungen', 'badge': 'RATGEBER', 'badge_color': 'sky',
        'title': '15 Beste Hunderassen für Wohnungen',
        'meta_desc': 'Suchst du einen wohnungsfreundlichen Hund? Diese 15 Rassen gedeihen in kleinen Räumen.',
        'subtitle': 'Diese Rassen fühlen sich in gemütlichen Räumen wohl.',
        'intro': 'In einer Wohnung zu leben bedeutet nicht, dass du keinen Hund haben kannst. Die wichtigsten Faktoren sind <strong>Energielevel, Bellneigung und Anpassungsfähigkeit</strong>.',
        'tip_box': '<strong>Überraschend:</strong> Große Rassen wie Windhunde sind ausgezeichnete Wohnungshunde, während kleine wie Jack Russells viel Platz brauchen.',
        'sec1_title': '🏆 Top 5 Wohnungshunde',
        'sec2_title': '🐕 Mittelgroße Wohnungshunde',
        'sec3_title': '🦴 Große Wohnungshunde',
        'quiet_title': '🔇 Leiseste Rassen', 'quiet_intro': 'Diese Rassen bellen selten:',
        'avoid_title': '⚠️ Zu Vermeidende Rassen', 'avoid_intro': 'Hohe Energie oder Bellprobleme:',
        'tips_title': '💡 Tipps für Wohnungsbesitzer',
        'cta_title': 'Finde Deinen Match', 'cta_text': 'Mach unser Quiz für den perfekten Wohnungshund.',
    },
    'es': {
        'slug': 'mejores-perros-para-apartamentos', 'badge': 'GUÍA', 'badge_color': 'sky',
        'title': '15 Mejores Razas de Perros para Apartamentos',
        'meta_desc': '¿Buscas perros aptos para apartamentos? Estas 15 razas prosperan en espacios pequeños.',
        'subtitle': 'Estas razas se adaptan perfectamente a espacios acogedores.',
        'intro': 'Vivir en un apartamento no significa que no puedas tener un perro. Los factores clave son <strong>nivel de energía, tendencia a ladrar y adaptabilidad</strong>.',
        'tip_box': '<strong>Dato sorprendente:</strong> Algunas razas grandes como los Galgos son excelentes para apartamentos, mientras que razas pequeñas como los Jack Russell necesitan mucho espacio.',
        'sec1_title': '🏆 Top 5 Perros de Apartamento',
        'sec2_title': '🐕 Perros Medianos para Apartamento',
        'sec3_title': '🦴 Perros Grandes para Apartamento',
        'quiet_title': '🔇 Razas Más Silenciosas', 'quiet_intro': 'Estas razas rara vez ladran:',
        'avoid_title': '⚠️ Razas a Evitar', 'avoid_intro': 'Alta energía o problemas de ladrido:',
        'tips_title': '💡 Consejos para Dueños de Apartamento',
        'cta_title': 'Encuentra Tu Match', 'cta_text': 'Haz nuestro quiz para encontrar tu perro de apartamento perfecto.',
    },
    'fr': {
        'slug': 'meilleurs-chiens-pour-appartements', 'badge': 'GUIDE', 'badge_color': 'sky',
        'title': '15 Meilleures Races de Chiens pour Appartements',
        'meta_desc': 'Vous cherchez des chiens adaptés aux appartements? Ces 15 races s\'épanouissent dans les petits espaces.',
        'subtitle': 'Ces races s\'adaptent parfaitement aux espaces confortables.',
        'intro': 'Vivre en appartement ne signifie pas que vous ne pouvez pas avoir un chien. Les facteurs clés sont <strong>le niveau d\'énergie, la tendance à aboyer et l\'adaptabilité</strong>.',
        'tip_box': '<strong>Fait surprenant:</strong> Certaines grandes races comme les Lévriers sont excellents en appartement, tandis que les petites races comme les Jack Russell ont besoin de beaucoup d\'espace.',
        'sec1_title': '🏆 Top 5 Chiens d\'Appartement',
        'sec2_title': '🐕 Chiens Moyens pour Appartement',
        'sec3_title': '🦴 Grands Chiens pour Appartement',
        'quiet_title': '🔇 Races les Plus Silencieuses', 'quiet_intro': 'Ces races aboient rarement:',
        'avoid_title': '⚠️ Races à Éviter', 'avoid_intro': 'Haute énergie ou problèmes d\'aboiement:',
        'tips_title': '💡 Conseils pour Propriétaires d\'Appartement',
        'cta_title': 'Trouvez Votre Match', 'cta_text': 'Faites notre quiz pour trouver votre chien d\'appartement idéal.',
    },
    'it': {
        'slug': 'migliori-cani-per-appartamenti', 'badge': 'GUIDA', 'badge_color': 'sky',
        'title': '15 Migliori Razze di Cani per Appartamenti',
        'meta_desc': 'Cerchi cani adatti agli appartamenti? Queste 15 razze prosperano in spazi piccoli.',
        'subtitle': 'Queste razze si adattano perfettamente agli spazi accoglienti.',
        'intro': 'Vivere in appartamento non significa che non puoi avere un cane. I fattori chiave sono <strong>livello di energia, tendenza ad abbaiare e adattabilità</strong>.',
        'tip_box': '<strong>Fatto sorprendente:</strong> Alcune razze grandi come i Levrieri sono eccellenti per gli appartamenti, mentre razze piccole come i Jack Russell hanno bisogno di molto spazio.',
        'sec1_title': '🏆 Top 5 Cani da Appartamento',
        'sec2_title': '🐕 Cani Medi per Appartamento',
        'sec3_title': '🦴 Cani Grandi per Appartamento',
        'quiet_title': '🔇 Razze Più Silenziose', 'quiet_intro': 'Queste razze abbaiano raramente:',
        'avoid_title': '⚠️ Razze da Evitare', 'avoid_intro': 'Alta energia o problemi di abbaio:',
        'tips_title': '💡 Consigli per Proprietari di Appartamento',
        'cta_title': 'Trova il Tuo Match', 'cta_text': 'Fai il nostro quiz per trovare il tuo cane da appartamento ideale.',
    },
    'pt': {
        'slug': 'melhores-caes-para-apartamentos', 'badge': 'GUIA', 'badge_color': 'sky',
        'title': '15 Melhores Raças de Cães para Apartamentos',
        'meta_desc': 'Procurando cães adequados para apartamentos? Estas 15 raças prosperam em espaços pequenos.',
        'subtitle': 'Estas raças se adaptam perfeitamente a espaços aconchegantes.',
        'intro': 'Morar em apartamento não significa que você não pode ter um cão. Os fatores-chave são <strong>nível de energia, tendência a latir e adaptabilidade</strong>.',
        'tip_box': '<strong>Fato surpreendente:</strong> Algumas raças grandes como Galgos são excelentes para apartamentos, enquanto raças pequenas como Jack Russells precisam de muito espaço.',
        'sec1_title': '🏆 Top 5 Cães de Apartamento',
        'sec2_title': '🐕 Cães Médios para Apartamento',
        'sec3_title': '🦴 Cães Grandes para Apartamento',
        'quiet_title': '🔇 Raças Mais Silenciosas', 'quiet_intro': 'Estas raças raramente latem:',
        'avoid_title': '⚠️ Raças a Evitar', 'avoid_intro': 'Alta energia ou problemas de latido:',
        'tips_title': '💡 Dicas para Donos de Apartamento',
        'cta_title': 'Encontre Seu Match', 'cta_text': 'Faça nosso quiz para encontrar seu cão de apartamento perfeito.',
    },
    'nl': {
        'slug': 'beste-honden-voor-appartementen', 'badge': 'GIDS', 'badge_color': 'sky',
        'title': '15 Beste Hondenrassen voor Appartementen',
        'meta_desc': 'Op zoek naar appartementvriendelijke honden? Deze 15 rassen gedijen in kleine ruimtes.',
        'subtitle': 'Deze rassen passen perfect in gezellige ruimtes.',
        'intro': 'In een appartement wonen betekent niet dat je geen hond kunt hebben. De belangrijkste factoren zijn <strong>energieniveau, blafneiging en aanpassingsvermogen</strong>.',
        'tip_box': '<strong>Verrassend feit:</strong> Grote rassen zoals Greyhounds zijn uitstekende appartementshonden, terwijl kleine rassen zoals Jack Russells veel ruimte nodig hebben.',
        'sec1_title': '🏆 Top 5 Appartementshonden',
        'sec2_title': '🐕 Middelgrote Appartementshonden',
        'sec3_title': '🦴 Grote Appartementshonden',
        'quiet_title': '🔇 Stilste Rassen', 'quiet_intro': 'Deze rassen blaffen zelden:',
        'avoid_title': '⚠️ Te Vermijden Rassen', 'avoid_intro': 'Hoge energie of blafproblemen:',
        'tips_title': '💡 Tips voor Appartementseigenaren',
        'cta_title': 'Vind Je Match', 'cta_text': 'Doe onze quiz om je perfecte appartementshond te vinden.',
    },
    'pl': {
        'slug': 'najlepsze-psy-do-mieszkan', 'badge': 'PRZEWODNIK', 'badge_color': 'sky',
        'title': '15 Najlepszych Ras Psów do Mieszkań',
        'meta_desc': 'Szukasz psów odpowiednich do mieszkań? Te 15 ras świetnie się czuje w małych przestrzeniach.',
        'subtitle': 'Te rasy doskonale adaptują się do przytulnych przestrzeni.',
        'intro': 'Mieszkanie w bloku nie oznacza, że nie możesz mieć psa. Kluczowe czynniki to <strong>poziom energii, skłonność do szczekania i zdolność adaptacji</strong>.',
        'tip_box': '<strong>Zaskakujący fakt:</strong> Niektóre duże rasy jak Charty są świetnymi psami do mieszkań, podczas gdy małe rasy jak Jack Russelle potrzebują dużo miejsca.',
        'sec1_title': '🏆 Top 5 Psów do Mieszkań',
        'sec2_title': '🐕 Średnie Psy do Mieszkań',
        'sec3_title': '🦴 Duże Psy do Mieszkań',
        'quiet_title': '🔇 Najcichsze Rasy', 'quiet_intro': 'Te rasy rzadko szczekają:',
        'avoid_title': '⚠️ Rasy do Unikania', 'avoid_intro': 'Wysoka energia lub problemy ze szczekaniem:',
        'tips_title': '💡 Wskazówki dla Właścicieli Mieszkań',
        'cta_title': 'Znajdź Swojego Psa', 'cta_text': 'Zrób nasz quiz, aby znaleźć idealnego psa do mieszkania.',
    },
    'sv': {
        'slug': 'basta-hundar-for-lagenheter', 'badge': 'GUIDE', 'badge_color': 'sky',
        'title': '15 Bästa Hundraser för Lägenheter',
        'meta_desc': 'Letar du efter lägenhetsvänliga hundar? Dessa 15 raser trivs i små utrymmen.',
        'subtitle': 'Dessa raser trivs perfekt i mysiga utrymmen.',
        'intro': 'Att bo i lägenhet betyder inte att du inte kan ha en hund. De viktigaste faktorerna är <strong>energinivå, skälltendens och anpassningsförmåga</strong>.',
        'tip_box': '<strong>Överraskande fakta:</strong> Stora raser som Greyhounds är utmärkta lägenhetshundar, medan små raser som Jack Russells behöver mycket utrymme.',
        'sec1_title': '🏆 Topp 5 Lägenhetshundar',
        'sec2_title': '🐕 Medelstora Lägenhetshundar',
        'sec3_title': '🦴 Stora Lägenhetshundar',
        'quiet_title': '🔇 Tystaste Raser', 'quiet_intro': 'Dessa raser skäller sällan:',
        'avoid_title': '⚠️ Raser att Undvika', 'avoid_intro': 'Hög energi eller skällproblem:',
        'tips_title': '💡 Tips för Lägenhetsägare',
        'cta_title': 'Hitta Din Match', 'cta_text': 'Gör vårt quiz för att hitta din perfekta lägenhetshund.',
    },
    'no': {
        'slug': 'beste-hunder-for-leiligheter', 'badge': 'GUIDE', 'badge_color': 'sky',
        'title': '15 Beste Hunderaser for Leiligheter',
        'meta_desc': 'Leter du etter leilighetsvennlige hunder? Disse 15 rasene trives i små rom.',
        'subtitle': 'Disse rasene trives perfekt i koselige rom.',
        'intro': 'Å bo i leilighet betyr ikke at du ikke kan ha en hund. De viktigste faktorene er <strong>energinivå, bjeffetendens og tilpasningsevne</strong>.',
        'tip_box': '<strong>Overraskende fakta:</strong> Store raser som Greyhounds er utmerkede leilighetshunder, mens små raser som Jack Russells trenger mye plass.',
        'sec1_title': '🏆 Topp 5 Leilighetshunder',
        'sec2_title': '🐕 Mellomstore Leilighetshunder',
        'sec3_title': '🦴 Store Leilighetshunder',
        'quiet_title': '🔇 Stilleste Raser', 'quiet_intro': 'Disse rasene bjeffer sjelden:',
        'avoid_title': '⚠️ Raser å Unngå', 'avoid_intro': 'Høy energi eller bjeffproblemer:',
        'tips_title': '💡 Tips for Leilighetseiere',
        'cta_title': 'Finn Din Match', 'cta_text': 'Ta vår quiz for å finne din perfekte leilighetshund.',
    },
    'da': {
        'slug': 'bedste-hunde-til-lejligheder', 'badge': 'GUIDE', 'badge_color': 'sky',
        'title': '15 Bedste Hunderacer til Lejligheder',
        'meta_desc': 'Leder du efter lejlighedsvenlige hunde? Disse 15 racer trives i små rum.',
        'subtitle': 'Disse racer trives perfekt i hyggelige rum.',
        'intro': 'At bo i lejlighed betyder ikke, at du ikke kan have en hund. De vigtigste faktorer er <strong>energiniveau, gøtilbøjelighed og tilpasningsevne</strong>.',
        'tip_box': '<strong>Overraskende fakta:</strong> Store racer som Greyhounds er fremragende lejlighedshunde, mens små racer som Jack Russells har brug for meget plads.',
        'sec1_title': '🏆 Top 5 Lejlighedshunde',
        'sec2_title': '🐕 Mellemstore Lejlighedshunde',
        'sec3_title': '🦴 Store Lejlighedshunde',
        'quiet_title': '🔇 Stilleste Racer', 'quiet_intro': 'Disse racer gør sjældent:',
        'avoid_title': '⚠️ Racer at Undgå', 'avoid_intro': 'Høj energi eller gøproblemer:',
        'tips_title': '💡 Tips til Lejlighedsejere',
        'cta_title': 'Find Dit Match', 'cta_text': 'Tag vores quiz for at finde din perfekte lejlighedshund.',
    },
    'zh': {
        'slug': 'zui-hao-de-gongyu-quan', 'badge': '指南', 'badge_color': 'sky',
        'title': '15种最适合公寓的犬种',
        'meta_desc': '正在寻找适合公寓的狗狗？这15个品种在小空间中茁壮成长。',
        'subtitle': '这些品种非常适合温馨的小空间。',
        'intro': '住在公寓并不意味着你不能养狗。关键因素是<strong>能量水平、吠叫倾向和适应性</strong>。',
        'tip_box': '<strong>令人惊讶的事实：</strong>一些大型犬如灵缇犬是优秀的公寓犬，而小型犬如杰克罗素梗需要大量空间。',
        'sec1_title': '🏆 公寓犬前5名',
        'sec2_title': '🐕 中型公寓犬',
        'sec3_title': '🦴 大型公寓犬',
        'quiet_title': '🔇 最安静的品种', 'quiet_intro': '这些品种很少吠叫：',
        'avoid_title': '⚠️ 应避免的品种', 'avoid_intro': '高能量或吠叫问题：',
        'tips_title': '💡 公寓主人提示',
        'cta_title': '找到你的匹配', 'cta_text': '参加我们的测验，找到你理想的公寓犬。',
    },
    'ja': {
        'slug': 'manshon-ni-tekishita-inu', 'badge': 'ガイド', 'badge_color': 'sky',
        'title': 'マンションに最適な犬種15選',
        'meta_desc': 'マンション向きの犬をお探しですか？この15犬種は小さなスペースで活躍します。',
        'subtitle': 'これらの犬種は居心地の良い空間に最適です。',
        'intro': 'マンション暮らしだからといって、犬を飼えないわけではありません。重要な要素は<strong>エネルギーレベル、吠える傾向、適応性</strong>です。',
        'tip_box': '<strong>意外な事実：</strong>グレイハウンドのような大型犬は優れたマンション犬ですが、ジャックラッセルのような小型犬は多くのスペースを必要とします。',
        'sec1_title': '🏆 マンション犬トップ5',
        'sec2_title': '🐕 中型マンション犬',
        'sec3_title': '🦴 大型マンション犬',
        'quiet_title': '🔇 最も静かな犬種', 'quiet_intro': 'これらの犬種はめったに吠えません：',
        'avoid_title': '⚠️ 避けるべき犬種', 'avoid_intro': '高エネルギーまたは吠える問題：',
        'tips_title': '💡 マンション飼い主へのヒント',
        'cta_title': 'あなたに合った犬を見つける', 'cta_text': 'クイズに参加して、理想のマンション犬を見つけましょう。',
    },
    'ru': {
        'slug': 'luchshie-sobaki-dlya-kvartir', 'badge': 'ГАЙД', 'badge_color': 'sky',
        'title': '15 Лучших Пород Собак для Квартиры',
        'meta_desc': 'Ищете собак для квартиры? Эти 15 пород прекрасно чувствуют себя в небольших помещениях.',
        'subtitle': 'Эти породы идеально подходят для уютных пространств.',
        'intro': 'Жизнь в квартире не означает, что вы не можете завести собаку. Ключевые факторы — <strong>уровень энергии, склонность к лаю и адаптивность</strong>.',
        'tip_box': '<strong>Удивительный факт:</strong> Крупные породы, такие как грейхаунды, отлично подходят для квартир, тогда как мелкие породы, такие как джек-рассел-терьеры, нуждаются в большом пространстве.',
        'sec1_title': '🏆 Топ-5 Квартирных Собак',
        'sec2_title': '🐕 Средние Квартирные Собаки',
        'sec3_title': '🦴 Крупные Квартирные Собаки',
        'quiet_title': '🔇 Самые Тихие Породы', 'quiet_intro': 'Эти породы редко лают:',
        'avoid_title': '⚠️ Породы, Которых Следует Избегать', 'avoid_intro': 'Высокая энергия или проблемы с лаем:',
        'tips_title': '💡 Советы Владельцам Квартир',
        'cta_title': 'Найдите Свою Пару', 'cta_text': 'Пройдите наш тест, чтобы найти идеальную квартирную собаку.',
    },
}

# FAMILIES ARTICLE
FAMILIES = {
    'en': {
        'slug': 'best-dogs-for-families', 'badge': 'FAMILY GUIDE', 'badge_color': 'rose',
        'title': '12 Best Dog Breeds for Families with Kids',
        'meta_desc': 'Finding a family dog? These 12 breeds are patient, gentle, and great with children.',
        'subtitle': 'These breeds are known for patience, gentleness, and love for children.',
        'intro': 'The right family dog becomes a best friend and protector for your children. The best family dogs are <strong>patient, tolerant, and gentle by nature</strong>.',
        'tip_box': '<strong>Important:</strong> Always supervise interactions between dogs and young children. Teach kids how to handle dogs respectfully.',
    },
    'fi': {
        'slug': 'parhaat-perhekoirat', 'badge': 'PERHEOPAS', 'badge_color': 'rose',
        'title': '12 Parasta Koirarotua Lapsiperheille',
        'meta_desc': 'Etsitkö perhekoiraa? Nämä 12 rotua ovat kärsivällisiä ja loistavia lasten kanssa.',
        'subtitle': 'Nämä rodut tunnetaan kärsivällisyydestään ja rakkaudestaan lapsia kohtaan.',
        'intro': 'Oikea perhekoira tulee lastesi parhaaksi ystäväksi ja suojelijaksi. Parhaat perhekoirat ovat <strong>kärsivällisiä, suvaitsevaisia ja luonnostaan lempeitä</strong>.',
        'tip_box': '<strong>Tärkeää:</strong> Valvo aina koiran ja pienten lasten kohtaamisia. Opeta lapsille koiran kunnioittava käsittely.',
    },
    'de': {
        'slug': 'beste-hunde-fuer-familien', 'badge': 'FAMILIENRATGEBER', 'badge_color': 'rose',
        'title': '12 Beste Hunderassen für Familien mit Kindern',
        'meta_desc': 'Suchst du einen Familienhund? Diese 12 Rassen sind geduldig und großartig mit Kindern.',
        'subtitle': 'Diese Rassen sind bekannt für Geduld und Liebe zu Kindern.',
        'intro': 'Der richtige Familienhund wird zum besten Freund und Beschützer deiner Kinder. Die besten Familienhunde sind <strong>geduldig, tolerant und von Natur aus sanft</strong>.',
        'tip_box': '<strong>Wichtig:</strong> Beaufsichtige immer Interaktionen zwischen Hunden und kleinen Kindern.',
    },
    'es': {
        'slug': 'mejores-perros-para-familias', 'badge': 'GUÍA FAMILIAR', 'badge_color': 'rose',
        'title': '12 Mejores Razas de Perros para Familias con Niños',
        'meta_desc': '¿Buscas un perro familiar? Estas 12 razas son pacientes y geniales con los niños.',
        'subtitle': 'Estas razas son conocidas por su paciencia y amor por los niños.',
        'intro': 'El perro familiar adecuado se convierte en el mejor amigo y protector de tus hijos. Los mejores perros familiares son <strong>pacientes, tolerantes y gentiles por naturaleza</strong>.',
        'tip_box': '<strong>Importante:</strong> Siempre supervisa las interacciones entre perros y niños pequeños.',
    },
    'fr': {
        'slug': 'meilleurs-chiens-pour-familles', 'badge': 'GUIDE FAMILIAL', 'badge_color': 'rose',
        'title': '12 Meilleures Races de Chiens pour Familles avec Enfants',
        'meta_desc': 'Vous cherchez un chien de famille? Ces 12 races sont patientes et excellentes avec les enfants.',
        'subtitle': 'Ces races sont connues pour leur patience et leur amour des enfants.',
        'intro': 'Le bon chien de famille devient le meilleur ami et protecteur de vos enfants. Les meilleurs chiens de famille sont <strong>patients, tolérants et naturellement doux</strong>.',
        'tip_box': '<strong>Important:</strong> Supervisez toujours les interactions entre chiens et jeunes enfants.',
    },
    'it': {
        'slug': 'migliori-cani-per-famiglie', 'badge': 'GUIDA FAMILIARE', 'badge_color': 'rose',
        'title': '12 Migliori Razze di Cani per Famiglie con Bambini',
        'meta_desc': 'Cerchi un cane di famiglia? Queste 12 razze sono pazienti e ottime con i bambini.',
        'subtitle': 'Queste razze sono conosciute per la pazienza e l\'amore per i bambini.',
        'intro': 'Il cane di famiglia giusto diventa il migliore amico e protettore dei tuoi figli. I migliori cani di famiglia sono <strong>pazienti, tolleranti e naturalmente gentili</strong>.',
        'tip_box': '<strong>Importante:</strong> Supervisiona sempre le interazioni tra cani e bambini piccoli.',
    },
    'pt': {
        'slug': 'melhores-caes-para-familias', 'badge': 'GUIA FAMILIAR', 'badge_color': 'rose',
        'title': '12 Melhores Raças de Cães para Famílias com Crianças',
        'meta_desc': 'Procurando um cão de família? Estas 12 raças são pacientes e ótimas com crianças.',
        'subtitle': 'Estas raças são conhecidas pela paciência e amor pelas crianças.',
        'intro': 'O cão de família certo se torna o melhor amigo e protetor de seus filhos. Os melhores cães de família são <strong>pacientes, tolerantes e naturalmente gentis</strong>.',
        'tip_box': '<strong>Importante:</strong> Sempre supervisione as interações entre cães e crianças pequenas.',
    },
    'nl': {
        'slug': 'beste-honden-voor-gezinnen', 'badge': 'FAMILIEGIDS', 'badge_color': 'rose',
        'title': '12 Beste Hondenrassen voor Gezinnen met Kinderen',
        'meta_desc': 'Op zoek naar een familiehond? Deze 12 rassen zijn geduldig en geweldig met kinderen.',
        'subtitle': 'Deze rassen staan bekend om hun geduld en liefde voor kinderen.',
        'intro': 'De juiste familiehond wordt de beste vriend en beschermer van je kinderen. De beste familiehonden zijn <strong>geduldig, tolerant en van nature zachtaardig</strong>.',
        'tip_box': '<strong>Belangrijk:</strong> Houd altijd toezicht op interacties tussen honden en jonge kinderen.',
    },
    'pl': {
        'slug': 'najlepsze-psy-dla-rodzin', 'badge': 'PRZEWODNIK RODZINNY', 'badge_color': 'rose',
        'title': '12 Najlepszych Ras Psów dla Rodzin z Dziećmi',
        'meta_desc': 'Szukasz psa rodzinnego? Te 12 ras jest cierpliwych i świetnych z dziećmi.',
        'subtitle': 'Te rasy są znane z cierpliwości i miłości do dzieci.',
        'intro': 'Właściwy pies rodzinny staje się najlepszym przyjacielem i obrońcą twoich dzieci. Najlepsze psy rodzinne są <strong>cierpliwe, tolerancyjne i z natury łagodne</strong>.',
        'tip_box': '<strong>Ważne:</strong> Zawsze nadzoruj interakcje między psami a małymi dziećmi.',
    },
    'sv': {
        'slug': 'basta-hundar-for-familjer', 'badge': 'FAMILJEGUIDE', 'badge_color': 'rose',
        'title': '12 Bästa Hundraser för Familjer med Barn',
        'meta_desc': 'Letar du efter en familjehund? Dessa 12 raser är tålmodiga och fantastiska med barn.',
        'subtitle': 'Dessa raser är kända för sin tålmodighet och kärlek till barn.',
        'intro': 'Rätt familjehund blir dina barns bästa vän och beskyddare. De bästa familjehundarna är <strong>tålmodiga, toleranta och naturligt milda</strong>.',
        'tip_box': '<strong>Viktigt:</strong> Övervaka alltid interaktioner mellan hundar och små barn.',
    },
    'no': {
        'slug': 'beste-hunder-for-familier', 'badge': 'FAMILIEGUIDE', 'badge_color': 'rose',
        'title': '12 Beste Hunderaser for Familier med Barn',
        'meta_desc': 'Leter du etter en familiehund? Disse 12 rasene er tålmodige og fantastiske med barn.',
        'subtitle': 'Disse rasene er kjent for sin tålmodighet og kjærlighet til barn.',
        'intro': 'Riktig familiehund blir barnas beste venn og beskytter. De beste familiehundene er <strong>tålmodige, tolerante og naturlig milde</strong>.',
        'tip_box': '<strong>Viktig:</strong> Overvåk alltid samspill mellom hunder og små barn.',
    },
    'da': {
        'slug': 'bedste-hunde-til-familier', 'badge': 'FAMILIEGUIDE', 'badge_color': 'rose',
        'title': '12 Bedste Hunderacer til Familier med Børn',
        'meta_desc': 'Leder du efter en familiehund? Disse 12 racer er tålmodige og fantastiske med børn.',
        'subtitle': 'Disse racer er kendt for deres tålmodighed og kærlighed til børn.',
        'intro': 'Den rigtige familiehund bliver dine børns bedste ven og beskytter. De bedste familiehunde er <strong>tålmodige, tolerante og naturligt milde</strong>.',
        'tip_box': '<strong>Vigtigt:</strong> Overvåg altid interaktioner mellem hunde og små børn.',
    },
    'zh': {
        'slug': 'zui-hao-de-jiating-quan', 'badge': '家庭指南', 'badge_color': 'rose',
        'title': '12种最适合有孩子家庭的犬种',
        'meta_desc': '正在寻找家庭犬？这12个品种耐心且非常适合儿童。',
        'subtitle': '这些品种以耐心和对孩子的爱而闻名。',
        'intro': '合适的家庭犬会成为孩子最好的朋友和保护者。最好的家庭犬<strong>耐心、宽容且天性温和</strong>。',
        'tip_box': '<strong>重要提示：</strong>始终监督狗狗和幼儿之间的互动。',
    },
    'ja': {
        'slug': 'kazoku-ni-tekishita-inu', 'badge': 'ファミリーガイド', 'badge_color': 'rose',
        'title': '子供のいる家族に最適な犬種12選',
        'meta_desc': '家族犬をお探しですか？この12犬種は忍耐強く、子供に最適です。',
        'subtitle': 'これらの犬種は忍耐と子供への愛情で知られています。',
        'intro': '適切な家族犬は、お子さんの親友であり守護者になります。最高の家族犬は<strong>忍耐強く、寛容で、生まれつき穏やか</strong>です。',
        'tip_box': '<strong>重要：</strong>犬と幼い子供の交流は常に監視してください。',
    },
    'ru': {
        'slug': 'luchshie-sobaki-dlya-semey', 'badge': 'СЕМЕЙНЫЙ ГАЙД', 'badge_color': 'rose',
        'title': '12 Лучших Пород Собак для Семей с Детьми',
        'meta_desc': 'Ищете семейную собаку? Эти 12 пород терпеливы и отлично ладят с детьми.',
        'subtitle': 'Эти породы известны терпением и любовью к детям.',
        'intro': 'Правильная семейная собака станет лучшим другом и защитником ваших детей. Лучшие семейные собаки <strong>терпеливы, толерантны и от природы нежны</strong>.',
        'tip_box': '<strong>Важно:</strong> Всегда контролируйте взаимодействие собак с маленькими детьми.',
    },
}

# LOW SHEDDING ARTICLE
SHEDDING = {
    'en': {
        'slug': 'low-shedding-dogs', 'badge': 'GROOMING GUIDE', 'badge_color': 'emerald',
        'title': '20 Best Low-Shedding Dog Breeds',
        'meta_desc': 'Hate vacuuming dog hair? These 20 low-shedding breeds keep your home cleaner.',
        'subtitle': "Love dogs but hate fur on your couch? These breeds keep shedding to a minimum.",
        'intro': "All dogs shed at least a little. But some breeds shed so minimally you'll barely notice. Many low-shedding dogs have <strong>hair that grows continuously</strong> rather than fur.",
        'tip_box': '<strong>The trade-off:</strong> Most low-shedding breeds require regular professional grooming (every 4-8 weeks). Less vacuuming, more grooming appointments!',
    },
    'fi': {
        'slug': 'vahan-karvaavat-koirat', 'badge': 'HOITO-OPAS', 'badge_color': 'emerald',
        'title': '20 Parasta Vähän Karvaavaa Koirarotua',
        'meta_desc': 'Vihaatko koirankarvojen imurointia? Nämä 20 rotua pitävät kotisi siistimpänä.',
        'subtitle': 'Rakastatko koiria mutta vihaat karvoja sohvalla? Nämä rodut karvaavat minimaalisesti.',
        'intro': 'Kaikki koirat karvaavat ainakin vähän. Mutta jotkut rodut karvaavat niin vähän, ettet juuri huomaa. Monilla on <strong>jatkuvasti kasvavat karvat</strong> turkin sijaan.',
        'tip_box': '<strong>Vaihtokauppa:</strong> Useimmat vähän karvaavat rodut vaativat säännöllistä ammattitrimmaus (4-8 viikon välein). Vähemmän imurointia, enemmän trimmausaikoja!',
    },
    'de': {
        'slug': 'wenig-haarende-hunde', 'badge': 'PFLEGERAT', 'badge_color': 'emerald',
        'title': '20 Beste Wenig Haarende Hunderassen',
        'meta_desc': 'Hasst du Hundehaare? Diese 20 Rassen halten dein Zuhause sauberer.',
        'subtitle': 'Liebst du Hunde aber hasst Fell auf der Couch? Diese Rassen haaren minimal.',
        'intro': 'Alle Hunde haaren zumindest ein wenig. Aber einige Rassen haaren so minimal, dass du es kaum bemerkst. Viele haben <strong>kontinuierlich wachsendes Haar</strong> statt Fell.',
        'tip_box': '<strong>Der Kompromiss:</strong> Die meisten wenig haarenden Rassen brauchen regelmäßige professionelle Pflege (alle 4-8 Wochen). Weniger Staubsaugen, mehr Pflege!',
    },
    'es': {
        'slug': 'perros-que-no-sueltan-pelo', 'badge': 'GUÍA DE CUIDADO', 'badge_color': 'emerald',
        'title': '20 Mejores Razas de Perros que No Sueltan Pelo',
        'meta_desc': '¿Odias aspirar pelo de perro? Estas 20 razas mantienen tu hogar más limpio.',
        'subtitle': '¿Amas a los perros pero odias el pelo en el sofá? Estas razas sueltan pelo mínimamente.',
        'intro': 'Todos los perros sueltan algo de pelo. Pero algunas razas sueltan tan poco que apenas lo notarás. Muchos tienen <strong>pelo que crece continuamente</strong> en lugar de pelaje.',
        'tip_box': '<strong>El compromiso:</strong> La mayoría de las razas que no sueltan pelo requieren peluquería profesional regular (cada 4-8 semanas). ¡Menos aspirar, más citas de peluquería!',
    },
    'fr': {
        'slug': 'chiens-qui-ne-perdent-pas-leurs-poils', 'badge': 'GUIDE TOILETTAGE', 'badge_color': 'emerald',
        'title': '20 Meilleures Races de Chiens qui Ne Perdent Pas Leurs Poils',
        'meta_desc': 'Vous détestez passer l\'aspirateur? Ces 20 races gardent votre maison plus propre.',
        'subtitle': 'Vous aimez les chiens mais détestez les poils sur le canapé? Ces races perdent peu.',
        'intro': 'Tous les chiens perdent au moins un peu de poils. Mais certaines races en perdent si peu que vous le remarquerez à peine. Beaucoup ont des <strong>poils qui poussent continuellement</strong>.',
        'tip_box': '<strong>Le compromis:</strong> La plupart des races à faible perte de poils nécessitent un toilettage professionnel régulier (toutes les 4-8 semaines).',
    },
    'it': {
        'slug': 'cani-che-non-perdono-pelo', 'badge': 'GUIDA TOELETTATURA', 'badge_color': 'emerald',
        'title': '20 Migliori Razze di Cani che Non Perdono Pelo',
        'meta_desc': 'Odi aspirare i peli del cane? Queste 20 razze mantengono la tua casa più pulita.',
        'subtitle': 'Ami i cani ma odi i peli sul divano? Queste razze perdono pochissimo pelo.',
        'intro': 'Tutti i cani perdono almeno un po\' di pelo. Ma alcune razze ne perdono così poco che quasi non te ne accorgi. Molti hanno <strong>pelo che cresce continuamente</strong>.',
        'tip_box': '<strong>Il compromesso:</strong> La maggior parte delle razze a bassa perdita di pelo richiede toelettatura professionale regolare (ogni 4-8 settimane).',
    },
    'pt': {
        'slug': 'caes-que-nao-soltam-pelo', 'badge': 'GUIA DE TOSA', 'badge_color': 'emerald',
        'title': '20 Melhores Raças de Cães que Não Soltam Pelo',
        'meta_desc': 'Odeia aspirar pelos de cachorro? Estas 20 raças mantêm sua casa mais limpa.',
        'subtitle': 'Ama cães mas odeia pelos no sofá? Estas raças soltam pelo minimamente.',
        'intro': 'Todos os cães soltam pelo pelo menos um pouco. Mas algumas raças soltam tão pouco que você mal notará. Muitos têm <strong>pelo que cresce continuamente</strong>.',
        'tip_box': '<strong>O compromisso:</strong> A maioria das raças de baixa queda de pelo requer tosa profissional regular (a cada 4-8 semanas).',
    },
    'nl': {
        'slug': 'honden-die-niet-verharen', 'badge': 'VERZORGINGSGIDS', 'badge_color': 'emerald',
        'title': '20 Beste Hondenrassen die Niet Verharen',
        'meta_desc': 'Haat je stofzuigen? Deze 20 rassen houden je huis schoner.',
        'subtitle': 'Hou je van honden maar haat je haar op de bank? Deze rassen verharen minimaal.',
        'intro': 'Alle honden verharen minstens een beetje. Maar sommige rassen verharen zo weinig dat je het nauwelijks merkt. Veel hebben <strong>haar dat continu groeit</strong>.',
        'tip_box': '<strong>De afweging:</strong> De meeste weinig verharende rassen hebben regelmatige professionele verzorging nodig (elke 4-8 weken).',
    },
    'pl': {
        'slug': 'psy-ktore-nie-linieja', 'badge': 'PRZEWODNIK PIELĘGNACJI', 'badge_color': 'emerald',
        'title': '20 Najlepszych Ras Psów, Które Nie Linieją',
        'meta_desc': 'Nie znosisz odkurzania psiej sierści? Te 20 ras utrzyma twój dom w czystości.',
        'subtitle': 'Kochasz psy ale nie znosisz sierści na kanapie? Te rasy linieją minimalnie.',
        'intro': 'Wszystkie psy linieją przynajmniej trochę. Ale niektóre rasy linieją tak mało, że ledwo to zauważysz. Wiele ma <strong>sierść, która rośnie ciągle</strong>.',
        'tip_box': '<strong>Kompromis:</strong> Większość ras o niskim linieniu wymaga regularnej profesjonalnej pielęgnacji (co 4-8 tygodni).',
    },
    'sv': {
        'slug': 'hundar-som-inte-faller', 'badge': 'PÄLSVÅRDSGUIDE', 'badge_color': 'emerald',
        'title': '20 Bästa Hundraser som Inte Fäller',
        'meta_desc': 'Hatar du att dammsuga? Dessa 20 raser håller ditt hem renare.',
        'subtitle': 'Älskar du hundar men hatar päls på soffan? Dessa raser fäller minimalt.',
        'intro': 'Alla hundar fäller åtminstone lite. Men vissa raser fäller så lite att du knappt märker det. Många har <strong>hår som växer kontinuerligt</strong>.',
        'tip_box': '<strong>Kompromissen:</strong> De flesta lågfällande raser kräver regelbunden professionell trimning (var 4-8 vecka).',
    },
    'no': {
        'slug': 'hunder-som-ikke-feller', 'badge': 'PELSPLEIEGUIDE', 'badge_color': 'emerald',
        'title': '20 Beste Hunderaser som Ikke Feller',
        'meta_desc': 'Hater du å støvsuge? Disse 20 rasene holder hjemmet ditt renere.',
        'subtitle': 'Elsker du hunder men hater pels på sofaen? Disse rasene feller minimalt.',
        'intro': 'Alle hunder feller i det minste litt. Men noen raser feller så lite at du knapt merker det. Mange har <strong>hår som vokser kontinuerlig</strong>.',
        'tip_box': '<strong>Kompromisset:</strong> De fleste lavfellende raser krever regelmessig profesjonell trimming (hver 4-8 uke).',
    },
    'da': {
        'slug': 'hunde-der-ikke-falder', 'badge': 'PLEJEGUIDE', 'badge_color': 'emerald',
        'title': '20 Bedste Hunderacer der Ikke Fælder',
        'meta_desc': 'Hader du at støvsuge? Disse 20 racer holder dit hjem renere.',
        'subtitle': 'Elsker du hunde men hader pels på sofaen? Disse racer fælder minimalt.',
        'intro': 'Alle hunde fælder i det mindste lidt. Men nogle racer fælder så lidt, at du knap nok bemærker det. Mange har <strong>hår der vokser kontinuerligt</strong>.',
        'tip_box': '<strong>Kompromisset:</strong> De fleste lavfældende racer kræver regelmæssig professionel trimning (hver 4-8 uge).',
    },
    'zh': {
        'slug': 'bu-diao-mao-de-gou', 'badge': '美容指南', 'badge_color': 'emerald',
        'title': '20种最佳低掉毛犬种',
        'meta_desc': '讨厌吸尘狗毛？这20个品种让你的家更干净。',
        'subtitle': '爱狗但讨厌沙发上的毛？这些品种掉毛极少。',
        'intro': '所有狗都会掉一点毛。但有些品种掉毛很少，你几乎不会注意到。许多品种的<strong>毛发持续生长</strong>。',
        'tip_box': '<strong>权衡：</strong>大多数低掉毛品种需要定期专业美容（每4-8周）。少吸尘，多美容！',
    },
    'ja': {
        'slug': 'ke-ga-nukenai-inu', 'badge': 'グルーミングガイド', 'badge_color': 'emerald',
        'title': '抜け毛が少ない犬種20選',
        'meta_desc': '犬の毛の掃除機がけが嫌い？この20犬種は家をきれいに保ちます。',
        'subtitle': '犬は好きだけどソファの毛は嫌い？これらの犬種は抜け毛が最小限。',
        'intro': 'すべての犬は少なくとも少しは毛が抜けます。しかし、一部の犬種はほとんど気付かないほど少ない。多くは<strong>継続的に伸びる毛</strong>を持っています。',
        'tip_box': '<strong>トレードオフ：</strong>ほとんどの低抜け毛犬種は定期的なプロのグルーミングが必要です（4-8週ごと）。',
    },
    'ru': {
        'slug': 'sobaki-kotorye-ne-linyayut', 'badge': 'ГАЙД ПО УХОДУ', 'badge_color': 'emerald',
        'title': '20 Лучших Пород Собак, Которые Не Линяют',
        'meta_desc': 'Ненавидите пылесосить шерсть? Эти 20 пород сохранят ваш дом чище.',
        'subtitle': 'Любите собак, но ненавидите шерсть на диване? Эти породы линяют минимально.',
        'intro': 'Все собаки линяют хотя бы немного. Но некоторые породы линяют так мало, что вы едва заметите. У многих <strong>шерсть растет непрерывно</strong>.',
        'tip_box': '<strong>Компромисс:</strong> Большинство малолиняющих пород требуют регулярного профессионального ухода (каждые 4-8 недель).',
    },
}


def generate_article_html(article_type, lang):
    """Generate article HTML for a specific language"""
    
    if article_type == 'apartments':
        t = APARTMENTS.get(lang, APARTMENTS['en'])
    elif article_type == 'families':
        t = FAMILIES.get(lang, FAMILIES['en'])
    else:
        t = SHEDDING.get(lang, SHEDDING['en'])
    
    ui = UI.get(lang, UI['en'])
    depth = '../../' if lang == 'en' else '../../../'
    lang_path = '' if lang == 'en' else f'{lang}/'
    
    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{t['title']} | BreedFinder</title>
    <meta name="description" content="{t['meta_desc']}">
    <link rel="canonical" href="https://breedfinder.org/{lang_path}articles/{t['slug']}/">
    <link rel="icon" href="{depth}favicon.ico">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
        .prose h2 {{ font-size: 1.5rem; font-weight: 700; margin-top: 2rem; margin-bottom: 1rem; color: #0f172a; }}
        .prose p {{ margin-bottom: 1rem; color: #475569; line-height: 1.8; }}
    </style>
</head>
<body class="bg-slate-50 text-slate-900">
    <header class="bg-white border-b border-slate-200 py-4 px-4">
        <div class="max-w-4xl mx-auto flex items-center justify-between">
            <a href="{depth}{lang_path}" class="flex items-center gap-2">
                <img src="{depth}logo-192.png" class="w-10 h-10 rounded-xl" alt="BreedFinder">
                <span class="text-xl font-bold">BreedFinder</span>
            </a>
            <a href="{depth}{lang_path}" class="text-slate-600 hover:text-slate-900 text-sm">{ui['back']}</a>
        </div>
    </header>

    <main class="px-4 py-12">
        <article class="max-w-3xl mx-auto">
            <div class="mb-8">
                <span class="text-{t['badge_color']}-600 font-medium text-sm">{t['badge']}</span>
                <h1 class="text-3xl md:text-4xl font-bold mt-2 mb-4">{t['title']}</h1>
                <p class="text-slate-600 text-lg">{t['subtitle']}</p>
            </div>

            <div class="prose max-w-none">
                <p class="text-lg">{t['intro']}</p>

                <div class="bg-{t['badge_color']}-50 border-l-4 border-{t['badge_color']}-500 p-4 rounded-r-xl my-6">
                    <p class="text-{t['badge_color']}-900 mb-0">{t['tip_box']}</p>
                </div>

                <h2>{t.get('cta_title', 'Find Your Match')}</h2>
                <p>{t.get('cta_text', 'Take our quiz to find breeds that match your lifestyle.')}</p>

                <div class="flex gap-4 mt-6">
                    <a href="{depth}{lang_path}quiz/" class="inline-block bg-{t['badge_color']}-600 hover:bg-{t['badge_color']}-700 text-white font-semibold px-6 py-3 rounded-xl">{ui['quiz_btn']}</a>
                    <a href="{depth}{lang_path}compare/" class="inline-block bg-slate-200 hover:bg-slate-300 text-slate-800 font-semibold px-6 py-3 rounded-xl">{ui['compare_btn']}</a>
                </div>
            </div>
        </article>
    </main>

    <footer class="bg-slate-900 text-white py-8 px-4 mt-12">
        <div class="max-w-4xl mx-auto text-center text-slate-400 text-sm">
            <p>{ui['footer']}</p>
        </div>
    </footer>
</body>
</html>'''
    
    return html, t['slug']


def main():
    base_dir = Path(__file__).parent.parent
    
    print("Generating translated articles...")
    count = 0
    
    for lang in LANGUAGES:
        lang_dir = base_dir / lang / 'articles'
        lang_dir.mkdir(parents=True, exist_ok=True)
        
        for article_type in ['apartments', 'families', 'shedding']:
            html, slug = generate_article_html(article_type, lang)
            
            article_dir = lang_dir / slug
            article_dir.mkdir(parents=True, exist_ok=True)
            
            with open(article_dir / 'index.html', 'w', encoding='utf-8') as f:
                f.write(html)
            
            count += 1
            print(f"  Created {lang}/articles/{slug}/")
    
    print(f"\n✅ Done! Created {count} translated article pages")


if __name__ == '__main__':
    main()
