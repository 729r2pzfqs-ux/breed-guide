#!/usr/bin/env python3
"""Generate Polish comparison articles with full translations."""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

PL_UI = {
    'all_breeds': 'Wszystkie Rasy',
    'compare': 'Porównaj',
    'take_quiz': 'Zrób Quiz',
    'comparisons': 'Porównania',
    'side_by_side': 'Porównanie Obok Siebie',
    'attribute': 'Cecha',
    'size': 'Rozmiar',
    'lifespan': 'Długość Życia',
    'energy_level': 'Poziom Energii',
    'grooming_needs': 'Potrzeby Pielęgnacyjne',
    'trainability': 'Podatność na Szkolenie',
    'kid_friendly': 'Przyjazny Dzieciom',
    'apartment': 'Nadaje się do Mieszkania',
    'shedding': 'Linienie',
    'more_comparisons': 'Więcej Porównań',
    'back_to_compare': '← Wróć do Porównań',
    'view_profile': 'Zobacz pełny profil →',
    'large': 'Duży',
    'years': 'lat',
    'very_high': 'Bardzo Wysoki',
    'high': 'Wysoki',
    'moderate': 'Umiarkowany',
    'excellent': 'Doskonały',
    'not_ideal': 'Nieodpowiedni',
    'heavy': 'Intensywne',
    'helping_find': 'Pomagamy znaleźć idealnego towarzysza.',
    'temperament': 'Temperament',
    'exercise_needs': 'Potrzeby Ruchowe',
    'grooming_req': 'Wymagania Pielęgnacyjne',
    'which_right': 'Który Jest dla Ciebie?',
    'choose_if': 'Wybierz {breed}, jeśli...',
    'bottom_line': 'Podsumowanie',
}

PL_TRAITS = {
    'Friendly': 'Przyjazny', 'Outgoing': 'Towarzyski', 'Active': 'Aktywny', 'Gentle': 'Łagodny',
    'Intelligent': 'Inteligentny', 'Trusting': 'Ufny', 'Devoted': 'Oddany',
    'Reliable': 'Niezawodny', 'Trustworthy': 'Godny Zaufania', 'Kind': 'Dobry',
    'Playful': 'Zabawny', 'Adaptable': 'Adaptowalny', 'Smart': 'Bystry',
    'Affectionate': 'Czuły', 'Patient': 'Cierpliwy', 'Alert': 'Czujny',
    'Bright': 'Bystry', 'Amusing': 'Zabawny', 'Lively': 'Żywiołowy',
    'Confident': 'Pewny Siebie', 'Courageous': 'Odważny', 'Loyal': 'Lojalny',
    'Versatile': 'Wszechstronny', 'Protective': 'Opiekuńczy', 'Hardworking': 'Pracowity',
    'Intense': 'Intensywny', 'Mischievous': 'Psotny', 'Dignified': 'Dostojny',
    'Strong': 'Silny', 'Faithful': 'Wierny', 'Trainable': 'Łatwy do Szkolenia', 'Proud': 'Dumny',
}

COMPARISONS = {
    'labrador-vs-golden': {
        'slug': 'labrador-vs-golden-retriever',
        'breed1': 'Labrador Retriever',
        'breed2': 'Golden Retriever',
        'breed1_slug': 'labrador-retriever',
        'breed2_slug': 'golden-retriever',
        'title': 'Labrador Retriever vs Golden Retriever: Pełne Porównanie',
        'desc': 'Porównanie Labrador vs Golden Retriever. Zobacz rozmiar, temperament, potrzeby ruchowe i dopasowanie do rodziny.',
        'intro': 'Dwie z najbardziej kochanych ras rodzinnych na świecie. Obie są przyjazne, inteligentne i świetne z dziećmi—ale która jest odpowiednia dla ciebie?',
        'breed1_tagline': 'Najpopularniejsza Rasa na Świecie',
        'breed2_tagline': 'Ulubieniec Rodzin',
        'breed1_desc': 'Labrador Retriever to najpopularniejsza rasa psów na świecie. Są przyjazne, towarzyskie i pełne energii oraz miłości.',
        'breed2_desc': 'Golden Retriever to jedna z najpopularniejszych ras. Ich przyjazne i tolerancyjne usposobienie czyni je fantastycznymi zwierzętami rodzinnymi.',
        'breed1_traits': ['Friendly', 'Outgoing', 'Active', 'Gentle', 'Intelligent', 'Trusting'],
        'breed2_traits': ['Intelligent', 'Friendly', 'Devoted', 'Reliable', 'Trustworthy', 'Kind'],
        'breed1_temperament_desc': 'Labradory są słynne ze swojej przyjazności i tworzą więzi z całą rodziną. Dobrze socjalizują się z sąsiadami i innymi psami. Nie daj się zwieść ich spokojnej osobowości—potrzebują dużo ruchu!',
        'breed2_temperament_desc': 'Golden Retrievery są towarzyskie, niezawodne i chętne do zadowolenia. Są wspaniałe z dziećmi i innymi zwierzętami. Ich cierpliwa i łagodna natura czyni je doskonałymi psami terapeutycznymi.',
        'breed1_exercise': 'Wysoka energia, wymaga co najmniej 1-2 godzin aktywnego ruchu dziennie. Uwielbiają pływać, aportować i przygody na świeżym powietrzu.',
        'breed2_exercise': 'Wysoka energia, ale nieco mniej intensywna niż Labradory. Co najmniej 1 godzina ruchu dziennie. Doskonałe w aportowaniu, pływaniu i wędrówkach.',
        'breed1_grooming': 'Cotygodniowe szczotkowanie, więcej w okresie linienia. Krótka, gęsta sierść jest stosunkowo łatwa w utrzymaniu, ale mocno linieje.',
        'breed2_grooming': 'Zalecane codzienne szczotkowanie w okresie linienia. Dłuższa sierść wymaga więcej uwagi, aby zapobiec kołtunom.',
        'breed1_reasons': ['Chcesz najwyższy poziom energii', 'Wolisz trochę mniej pielęgnacji', 'Chcesz wszechstronnego psa sportowego', 'Lubisz towarzyską, entuzjastyczną osobowość', 'Ważna jest różnorodność kolorów (czarny, żółty, czekoladowy)'],
        'breed2_reasons': ['Wolisz nieco spokojniejszy temperament', 'Kochasz płynącą złotą sierść', 'Chcesz doskonałego psa terapeutycznego/służbowego', 'Cenisz łagodne, cierpliwe usposobienie', 'Nie przeszkadza ci częstsze szczotkowanie'],
        'bottom_line': 'Obie rasy to wyjątkowe psy rodzinne. Labradory są nieco bardziej energiczne i łatwiejsze w pielęgnacji sierści, podczas gdy Golden Retrievery słyną z łagodnej cierpliwości i płynącej sierści. Którykolwiek wybierzesz, zapewni lata miłości i towarzystwa!'
    },
    'frenchie-vs-boston': {
        'slug': 'buldog-francuski-vs-boston-terrier',
        'breed1': 'Buldog Francuski',
        'breed2': 'Boston Terrier',
        'breed1_slug': 'french-bulldog',
        'breed2_slug': 'boston-terrier',
        'title': 'Buldog Francuski vs Boston Terrier: Pełne Porównanie',
        'desc': 'Porównanie Buldog Francuski vs Boston Terrier. Kompaktowi towarzysze porównani.',
        'intro': 'Dwie urocze, kompaktowe rasy z wielkimi osobowościami. Obie świetne do życia w mieszkaniu—ale która pasuje do twojego stylu życia?',
        'breed1_tagline': 'Uroczy Francuz',
        'breed2_tagline': 'Amerykański Dżentelmen',
        'breed1_desc': 'Buldog Francuski to urocza i adaptowalna rasa o zabawnej osobowości, znana z uszu nietoperza i czułej natury.',
        'breed2_desc': 'Boston Terrier, znany jako "Amerykański Dżentelmen", to żywiołowy mały pies o przyjaznym i wesołym temperamencie.',
        'breed1_traits': ['Playful', 'Adaptable', 'Smart', 'Affectionate', 'Patient', 'Alert'],
        'breed2_traits': ['Friendly', 'Bright', 'Amusing', 'Gentle', 'Lively', 'Intelligent'],
        'breed1_temperament_desc': 'Buldogi Francuskie są spokojne i adaptowalne, dobrze się czują zarówno w miejskich mieszkaniach, jak i wiejskich domach. Są zabawne, ale nie hiperaktywne, co czyni je doskonałymi towarzyszami dla różnych stylów życia.',
        'breed2_temperament_desc': 'Boston Terriery są żywiołowe, bardzo inteligentne i mają łagodne usposobienie. Znane są ze swoich smokingowych znaczeń i przyjaznej, zabawnej osobowości.',
        'breed1_exercise': 'Umiarkowane potrzeby ruchowe—krótkie spacery i sesje zabawy wystarczą. Unikaj nadmiernego wysiłku w upalne dni ze względu na płaski nos.',
        'breed2_exercise': 'Umiarkowana energia, wymaga codziennych spacerów i zabawy. Bardziej atletyczny niż Buldogi, ale też podatny na przegrzanie.',
        'breed1_grooming': 'Minimalna pielęgnacja—cotygodniowe szczotkowanie. Regularnie czyść fałdy na twarzy, aby zapobiec infekcjom.',
        'breed2_grooming': 'Niska pielęgnacja—okazjonalne szczotkowanie. Ich krótka sierść jest łatwa w utrzymaniu.',
        'breed1_reasons': ['Chcesz spokojniejszego, wyluzowanego towarzysza', 'Wolisz bardziej kręgą budowę', 'Mieszkasz w mieszkaniu', 'Chcesz minimalnych wymagań ruchowych', 'Kochasz urocze uszy nietoperza'],
        'breed2_reasons': ['Chcesz nieco bardziej aktywnego psa', 'Wolisz smokingowy wygląd', 'Chcesz łatwiejszego do szkolenia psa', 'Lubisz bardziej atletyczną budowę', 'Chcesz dłużej żyjącą rasę'],
        'bottom_line': 'Oba są doskonałymi psami mieszkaniowymi z wielkimi osobowościami. Buldogi są spokojniejsze i bardziej wyluzowane, podczas gdy Bostony są nieco bardziej energiczne i atletyczne. Oba skradną twoje serce!'
    },
    'gsd-vs-malinois': {
        'slug': 'owczarek-niemiecki-vs-owczarek-belgijski',
        'breed1': 'Owczarek Niemiecki',
        'breed2': 'Owczarek Belgijski Malinois',
        'breed1_slug': 'german-shepherd',
        'breed2_slug': 'belgian-malinois',
        'title': 'Owczarek Niemiecki vs Owczarek Belgijski Malinois: Pełne Porównanie',
        'desc': 'Porównanie Owczarek Niemiecki vs Malinois. Dwa doskonałe psy robocze porównane.',
        'intro': 'Dwa z najbardziej zdolnych psów roboczych na świecie. Oba doskonałe w pracy policyjnej i wojskowej—ale mają ważne różnice.',
        'breed1_tagline': 'Wszechstronny Obrońca',
        'breed2_tagline': 'Elitarny Pies Roboczy',
        'breed1_desc': 'Owczarek Niemiecki jest wszechstronny, inteligentny i jedną z najpopularniejszych ras roboczych na świecie.',
        'breed2_desc': 'Owczarek Belgijski Malinois to intensywny, wysokowydajny pies roboczy, preferowany przez policję i wojsko na całym świecie.',
        'breed1_traits': ['Confident', 'Courageous', 'Smart', 'Loyal', 'Versatile', 'Protective'],
        'breed2_traits': ['Confident', 'Smart', 'Hardworking', 'Alert', 'Intense', 'Protective'],
        'breed1_temperament_desc': 'Owczarki Niemieckie są pewne siebie, odważne i niesamowicie wszechstronne. Tworzą głębokie więzi z rodziną i są naturalnie opiekuńcze, nie będąc agresywnymi.',
        'breed2_temperament_desc': 'Malinois to intensywne, zdeterminowane psy robocze z nieskończoną energią. Potrzebują zadania i rozwijają się u doświadczonych właścicieli, którzy potrafią ukierunkować ich zapał.',
        'breed1_exercise': 'Wysokie potrzeby ruchowe—co najmniej 2 godziny dziennie. Doskonałe w różnych sportach psich, tropienia i posłuszeństwa.',
        'breed2_exercise': 'Bardzo wysokie potrzeby ruchowe—2+ godziny intensywnej aktywności dziennie. Potrzebują stymulacji mentalnej tak samo jak fizycznej.',
        'breed1_grooming': 'Umiarkowana pielęgnacja—szczotkowanie 2-3 razy w tygodniu. Sezonowe intensywne linienie wymaga więcej uwagi.',
        'breed2_grooming': 'Łatwa pielęgnacja—cotygodniowe szczotkowanie. Krótsza sierść niż Owczarek Niemiecki, ale też sezonowo linieje.',
        'breed1_reasons': ['Chcesz wszechstronnego obrońcę rodziny', 'Wolisz nieco spokojniejszego psa roboczego', 'Jesteś początkującym właścicielem rasy roboczej', 'Chcesz psa dobrego z dziećmi', 'Wolisz klasyczny wygląd'],
        'breed2_reasons': ['Chcesz maksymalnej determinacji i intensywności', 'Jesteś doświadczonym właścicielem', 'Chcesz elitarnego psa sportowego/roboczego', 'Możesz zapewnić intensywny ruch', 'Chcesz lżejszego, szybszego psa'],
        'bottom_line': 'Oba to wyjątkowe psy robocze, ale Malinois są bardziej intensywne i wymagają doświadczonych właścicieli. Owczarki Niemieckie są bardziej wszechstronne i lepiej nadają się dla rodzin. Wybierz na podstawie swojego poziomu doświadczenia i stylu życia.'
    },
    'husky-vs-malamute': {
        'slug': 'husky-vs-malamute',
        'breed1': 'Siberian Husky',
        'breed2': 'Alaskan Malamute',
        'breed1_slug': 'siberian-husky',
        'breed2_slug': 'alaskan-malamute',
        'title': 'Siberian Husky vs Alaskan Malamute: Pełne Porównanie',
        'desc': 'Porównanie Husky vs Malamute. Rasy arktyczne porównane obok siebie.',
        'intro': 'Dwie majestatyczne rasy arktyczne o wilczym wyglądzie. Wyglądają podobnie, ale mają ważne różnice w rozmiarze i temperamencie.',
        'breed1_tagline': 'Szybki Pies Zaprzęgowy',
        'breed2_tagline': 'Potężny Ciągacz',
        'breed1_desc': 'Siberian Husky to atletyczny, wytrzymały pies zaprzęgowy, znany z niebieskich oczu i przyjaznej osobowości.',
        'breed2_desc': 'Alaskan Malamute to potężny, solidny pies zaprzęgowy, hodowany dla siły i wytrzymałości.',
        'breed1_traits': ['Outgoing', 'Mischievous', 'Loyal', 'Friendly', 'Alert', 'Gentle'],
        'breed2_traits': ['Affectionate', 'Loyal', 'Playful', 'Dignified', 'Devoted', 'Strong'],
        'breed1_temperament_desc': 'Husky są przyjazne, towarzyskie i czasem psotne. To psy stadne, które kochają towarzystwo i są znane z wokalnego charakteru i zdolności do ucieczek.',
        'breed2_temperament_desc': 'Malamute są bardziej dostojne i mniej psotne niż Husky. Są głęboko lojalne, czułe wobec rodziny, ale mogą być bardziej niezależne.',
        'breed1_exercise': 'Bardzo wysoka energia—zaprojektowane do biegania kilometrów. Co najmniej 2 godziny aktywnego ruchu dziennie. Uwielbiają biegać i ciągnąć.',
        'breed2_exercise': 'Wysoka energia, ale więcej wytrzymałości niż prędkości. Długie wędrówki i praca ciągnąca są odpowiednie. Mogą się przegrzać w ciepłym klimacie.',
        'breed1_grooming': 'Intensywna pielęgnacja—szczotkowanie kilka razy w tygodniu. Masywne linienie ("zdmuchiwanie sierści") dwa razy w roku.',
        'breed2_grooming': 'Intensywna pielęgnacja jak Husky. Ich gęstsza sierść wymaga regularnego szczotkowania, aby zapobiec kołtunom.',
        'breed1_reasons': ['Chcesz średniej wielkości rasę arktyczną', 'Wolisz szybszego, bardziej atletycznego psa', 'Lubisz gadatliwego, wokalnego towarzysza', 'Chcesz imponujące niebieskie oczy', 'Lubisz bardziej zabawną osobowość'],
        'breed2_reasons': ['Chcesz większego, potężniejszego psa', 'Wolisz spokojniejszy, dostojniejszy temperament', 'Masz doświadczenie z silnymi rasami', 'Chcesz cichszego psa (mniej wycia)', 'Potrzebujesz psa do ciągnięcia/zaprzęgu'],
        'bottom_line': 'Husky to średniej wielkości atleci, którzy kochają biegać i "rozmawiać". Malamute to potężne olbrzymy zbudowane dla siły. Oba mocno linieją i potrzebują dużo ruchu. Wybierz na podstawie preferencji rozmiaru i pożądanego temperamentu.'
    },
    'poodle-vs-labrador': {
        'slug': 'pudel-vs-labrador',
        'breed1': 'Pudel',
        'breed2': 'Labrador Retriever',
        'breed1_slug': 'poodle',
        'breed2_slug': 'labrador-retriever',
        'title': 'Pudel vs Labrador Retriever: Pełne Porównanie',
        'desc': 'Porównanie Pudel vs Labrador. Dwie inteligentne i popularne rasy porównane.',
        'intro': 'Dwie z najbardziej inteligentnych i popularnych ras psów. Obie doskonałe psy rodzinne z bardzo różnymi sierściami.',
        'breed1_tagline': 'Elegancki Atleta',
        'breed2_tagline': 'Najlepszy Przyjaciel Wszystkich',
        'breed1_desc': 'Pudel jest wyjątkowo inteligentny i aktywny. Za eleganckim wyglądem kryje się atletyczny i bardzo bystry pies.',
        'breed2_desc': 'Labrador Retriever to najpopularniejsza rasa na świecie, znana z przyjaznej i towarzyskiej natury.',
        'breed1_traits': ['Intelligent', 'Active', 'Alert', 'Faithful', 'Trainable', 'Proud'],
        'breed2_traits': ['Friendly', 'Active', 'Outgoing', 'Gentle', 'Intelligent', 'Trusting'],
        'breed1_temperament_desc': 'Pudle są wyjątkowo inteligentne i chętne do zadowolenia. Nie daj się zwieść wymyślnym fryzurom—to atletyczne psy hodowane do polowania i aportowania.',
        'breed2_temperament_desc': 'Labradory to ucieleśnienie przyjaznego psa—towarzyskie ze wszystkimi, cierpliwe z dziećmi i chętne do zadowolenia. To idealny towarzysz rodzinny.',
        'breed1_exercise': 'Wysoka energia, wymaga codziennego ruchu i stymulacji mentalnej. Doskonałe w agility, posłuszeństwie i różnych sportach psich.',
        'breed2_exercise': 'Wysoka energia—co najmniej 1-2 godziny dziennie. Uwielbiają pływać, aportować i każdą aktywność z ludźmi.',
        'breed1_grooming': 'Wysoka pielęgnacja—profesjonalna pielęgnacja co 4-6 tygodni. Codzienne szczotkowanie zapobiega kołtunom. Sierść hipoalergiczna.',
        'breed2_grooming': 'Łatwa pielęgnacja, ale dużo linienia. Cotygodniowe szczotkowanie, więcej w okresie linienia. Nie jest hipoalergiczny.',
        'breed1_reasons': ['Masz alergie (hipoalergiczny)', 'Chcesz minimalne linienie', 'Lubisz pielęgnację lub nie przeszkadzają ci koszty', 'Chcesz elegancki wygląd', 'Chcesz opcje rozmiaru (toy/miniatura/standard)'],
        'breed2_reasons': ['Wolisz łatwą, tanią pielęgnację', 'Nie przeszkadza ci linienie', 'Chcesz klasycznego psa rodzinnego', 'Wolisz bardziej casualowy wygląd', 'Chcesz retrievera, który kocha wodę'],
        'bottom_line': 'Oba są wysoce inteligentne i łatwe do szkolenia. Pudle oferują hipoalergiczną sierść, ale wymagają więcej pielęgnacji. Labradory są łatwiejsze w utrzymaniu, ale mocno linieją. Oba to doskonali towarzysze rodzinni!'
    }
}


def generate_article(comp_key, comp):
    ui = PL_UI
    breed1_traits = [PL_TRAITS.get(t, t) for t in comp['breed1_traits']]
    breed2_traits = [PL_TRAITS.get(t, t) for t in comp['breed2_traits']]
    
    breed1_tags = '\n                    '.join([f'<span class="bg-amber-100 text-amber-700 px-3 py-1 rounded-full text-sm font-medium">{t}</span>' for t in breed1_traits])
    breed2_tags = '\n                    '.join([f'<span class="bg-yellow-100 text-yellow-700 px-3 py-1 rounded-full text-sm font-medium">{t}</span>' for t in breed2_traits])
    
    breed1_reasons = '\n                        '.join([f'<li class="flex items-start gap-2"><span class="text-green-400">✓</span><span>{r}</span></li>' for r in comp['breed1_reasons']])
    breed2_reasons = '\n                        '.join([f'<li class="flex items-start gap-2"><span class="text-green-400">✓</span><span>{r}</span></li>' for r in comp['breed2_reasons']])
    
    related = [(k, v) for k, v in COMPARISONS.items() if k != comp_key][:3]
    related_html = '\n'.join([f'<a href="{r[1]["slug"]}.html" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md transition"><span class="font-semibold">{r[1]["breed1"]} vs {r[1]["breed2"]}</span></a>' for r in related])
    
    return f'''<!DOCTYPE html>
<html lang="pl">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-VEERQZ53LZ"></script>
    <script>window.dataLayer = window.dataLayer || []; function gtag(){{dataLayer.push(arguments);}} gtag("js", new Date()); gtag("config", "G-VEERQZ53LZ");</script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{comp['title']} | BreedFinder</title>
    <meta name="description" content="{comp['desc']}">
    <link rel="canonical" href="https://breedfinder.org/pl/compare/comparisons/{comp['slug']}.html">
    <link rel="icon" href="../../../favicon.ico">
    <meta property="og:title" content="{comp['title']}">
    <meta property="og:description" content="{comp['desc']}">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>* {{ font-family: 'Plus Jakarta Sans', sans-serif; }}</style>
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"Article","headline":"{comp['title']}","description":"{comp['desc']}","author":{{"@type":"Organization","name":"BreedFinder"}},"publisher":{{"@type":"Organization","name":"BreedFinder","logo":{{"@type":"ImageObject","url":"https://breedfinder.org/logo-192.png"}}}}}}
    </script>
</head>
<body class="bg-gradient-to-br from-sky-50 via-white to-blue-50 min-h-screen text-slate-800">
    <header class="bg-white/80 backdrop-blur-md border-b border-slate-100 sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
            <a href="../../" class="flex items-center gap-3">
                <img src="../../../logo-192.png" class="w-10 h-10" alt="BreedFinder">
                <span class="text-xl font-bold">BreedFinder</span>
            </a>
            <nav class="flex items-center gap-6 text-sm font-medium">
                <a href="../../breeds/" class="text-slate-600 hover:text-sky-700">{ui['all_breeds']}</a>
                <a href="../" class="text-slate-600 hover:text-sky-700">{ui['compare']}</a>
                <a href="../../quiz" class="bg-sky-500 text-white px-5 py-2.5 rounded-xl font-semibold">{ui['take_quiz']}</a>
            </nav>
        </div>
    </header>

    <main class="max-w-6xl mx-auto px-4 py-12">
        <nav class="text-sm text-slate-600 mb-8">
            <a href="../">{ui['compare']}</a> › <a href="./">{ui['comparisons']}</a> › {comp['breed1']} vs {comp['breed2']}
        </nav>

        <div class="text-center mb-12">
            <h1 class="text-4xl md:text-5xl font-extrabold mb-4">
                <span class="text-amber-500">{comp['breed1']}</span>
                <span class="text-slate-600 mx-4">vs</span>
                <span class="text-yellow-500">{comp['breed2']}</span>
            </h1>
            <p class="text-lg text-slate-600 max-w-2xl mx-auto">{comp['intro']}</p>
        </div>

        <div class="grid md:grid-cols-2 gap-8 mb-12">
            <div class="bg-white rounded-3xl shadow-xl overflow-hidden">
                <div class="bg-gradient-to-r from-amber-500 to-amber-600 p-6 text-white text-center">
                    <img src="../../../images/heads/{comp['breed1_slug']}.webp" alt="{comp['breed1']}" class="w-32 h-32 rounded-full mx-auto mb-4 object-cover border-4 border-white/30">
                    <h2 class="text-2xl font-bold">{comp['breed1']}</h2>
                    <p class="text-amber-100">{comp['breed1_tagline']}</p>
                </div>
                <div class="p-6">
                    <p class="text-slate-600 mb-4">{comp['breed1_desc']}</p>
                    <a href="../../breeds/{comp['breed1_slug']}" class="text-sky-700 font-semibold">{ui['view_profile']}</a>
                </div>
            </div>
            <div class="bg-white rounded-3xl shadow-xl overflow-hidden">
                <div class="bg-gradient-to-r from-yellow-500 to-yellow-600 p-6 text-white text-center">
                    <img src="../../../images/heads/{comp['breed2_slug']}.webp" alt="{comp['breed2']}" class="w-32 h-32 rounded-full mx-auto mb-4 object-cover border-4 border-white/30">
                    <h2 class="text-2xl font-bold">{comp['breed2']}</h2>
                    <p class="text-yellow-100">{comp['breed2_tagline']}</p>
                </div>
                <div class="p-6">
                    <p class="text-slate-600 mb-4">{comp['breed2_desc']}</p>
                    <a href="../../breeds/{comp['breed2_slug']}" class="text-sky-700 font-semibold">{ui['view_profile']}</a>
                </div>
            </div>
        </div>

        <div class="bg-white rounded-3xl shadow-xl overflow-hidden mb-12">
            <div class="bg-slate-800 p-6 text-white">
                <h2 class="text-2xl font-bold text-center">{ui['side_by_side']}</h2>
            </div>
            <table class="w-full">
                <thead><tr class="bg-slate-50">
                    <th class="p-4 text-left">{ui['attribute']}</th>
                    <th class="p-4 text-center text-amber-600">{comp['breed1']}</th>
                    <th class="p-4 text-center text-yellow-600">{comp['breed2']}</th>
                </tr></thead>
                <tbody class="divide-y divide-slate-100">
                    <tr><td class="p-4">📏 {ui['size']}</td><td class="p-4 text-center font-semibold">{ui['large']}</td><td class="p-4 text-center font-semibold">{ui['large']}</td></tr>
                    <tr class="bg-slate-50/50"><td class="p-4">⏳ {ui['lifespan']}</td><td class="p-4 text-center">10-12 {ui['years']}</td><td class="p-4 text-center">10-12 {ui['years']}</td></tr>
                    <tr><td class="p-4">⚡ {ui['energy_level']}</td><td class="p-4 text-center"><span class="text-amber-500">●●●●●</span><br><span class="text-sm">{ui['very_high']}</span></td><td class="p-4 text-center"><span class="text-yellow-500">●●●●○</span><br><span class="text-sm">{ui['high']}</span></td></tr>
                    <tr class="bg-slate-50/50"><td class="p-4">✂️ {ui['grooming_needs']}</td><td class="p-4 text-center"><span class="text-amber-500">●●○○○</span><br><span class="text-sm">{ui['moderate']}</span></td><td class="p-4 text-center"><span class="text-yellow-500">●●●○○</span><br><span class="text-sm">{ui['moderate']}</span></td></tr>
                    <tr><td class="p-4">🎓 {ui['trainability']}</td><td class="p-4 text-center"><span class="text-amber-500">●●●●●</span><br><span class="text-sm">{ui['excellent']}</span></td><td class="p-4 text-center"><span class="text-yellow-500">●●●●●</span><br><span class="text-sm">{ui['excellent']}</span></td></tr>
                    <tr class="bg-slate-50/50"><td class="p-4">👶 {ui['kid_friendly']}</td><td class="p-4 text-center"><span class="text-amber-500">●●●●●</span><br><span class="text-sm">{ui['excellent']}</span></td><td class="p-4 text-center"><span class="text-yellow-500">●●●●●</span><br><span class="text-sm">{ui['excellent']}</span></td></tr>
                    <tr><td class="p-4">🏠 {ui['apartment']}</td><td class="p-4 text-center"><span class="text-amber-500">●●○○○</span><br><span class="text-sm">{ui['not_ideal']}</span></td><td class="p-4 text-center"><span class="text-yellow-500">●●○○○</span><br><span class="text-sm">{ui['not_ideal']}</span></td></tr>
                    <tr class="bg-slate-50/50"><td class="p-4">🐕 {ui['shedding']}</td><td class="p-4 text-center font-semibold text-amber-600">{ui['high']}</td><td class="p-4 text-center font-semibold text-yellow-600">{ui['heavy']}</td></tr>
                </tbody>
            </table>
        </div>

        <div class="grid md:grid-cols-2 gap-8 mb-12">
            <div class="bg-white rounded-2xl p-6 shadow-lg">
                <h3 class="text-xl font-bold text-amber-600 mb-4">🧠 {comp['breed1']} {ui['temperament']}</h3>
                <div class="flex flex-wrap gap-2 mb-4">
                    {breed1_tags}
                </div>
                <p class="text-slate-600 text-sm">{comp['breed1_temperament_desc']}</p>
            </div>
            <div class="bg-white rounded-2xl p-6 shadow-lg">
                <h3 class="text-xl font-bold text-yellow-600 mb-4">🧠 {comp['breed2']} {ui['temperament']}</h3>
                <div class="flex flex-wrap gap-2 mb-4">
                    {breed2_tags}
                </div>
                <p class="text-slate-600 text-sm">{comp['breed2_temperament_desc']}</p>
            </div>
        </div>

        <div class="grid md:grid-cols-2 gap-8 mb-12">
            <div class="bg-gradient-to-br from-sky-50 to-sky-100 rounded-2xl p-6">
                <h3 class="text-xl font-bold text-sky-700 mb-4">🏃 {ui['exercise_needs']}</h3>
                <div class="space-y-4">
                    <div><span class="font-semibold text-amber-600">{comp['breed1']}:</span><p class="text-slate-600 text-sm">{comp['breed1_exercise']}</p></div>
                    <div><span class="font-semibold text-yellow-600">{comp['breed2']}:</span><p class="text-slate-600 text-sm">{comp['breed2_exercise']}</p></div>
                </div>
            </div>
            <div class="bg-gradient-to-br from-sky-50 to-sky-100 rounded-2xl p-6">
                <h3 class="text-xl font-bold text-sky-700 mb-4">✂️ {ui['grooming_req']}</h3>
                <div class="space-y-4">
                    <div><span class="font-semibold text-amber-600">{comp['breed1']}:</span><p class="text-slate-600 text-sm">{comp['breed1_grooming']}</p></div>
                    <div><span class="font-semibold text-yellow-600">{comp['breed2']}:</span><p class="text-slate-600 text-sm">{comp['breed2_grooming']}</p></div>
                </div>
            </div>
        </div>

        <div class="bg-gradient-to-r from-slate-800 to-slate-700 rounded-3xl p-8 text-white mb-12">
            <h2 class="text-3xl font-bold text-center mb-8">🎯 {ui['which_right']}</h2>
            <div class="grid md:grid-cols-2 gap-8">
                <div class="bg-white/10 rounded-2xl p-6">
                    <h3 class="text-xl font-bold text-amber-400 mb-4">{ui['choose_if'].format(breed=comp['breed1'])}</h3>
                    <ul class="space-y-2 text-slate-200">
                        {breed1_reasons}
                    </ul>
                </div>
                <div class="bg-white/10 rounded-2xl p-6">
                    <h3 class="text-xl font-bold text-yellow-400 mb-4">{ui['choose_if'].format(breed=comp['breed2'])}</h3>
                    <ul class="space-y-2 text-slate-200">
                        {breed2_reasons}
                    </ul>
                </div>
            </div>
            <div class="mt-8 bg-white/5 rounded-xl p-6 text-center">
                <h4 class="text-lg font-semibold text-sky-300 mb-2">{ui['bottom_line']}</h4>
                <p class="text-slate-300">{comp['bottom_line']}</p>
            </div>
        </div>

        <div class="mb-12">
            <h2 class="text-2xl font-bold mb-6">{ui['more_comparisons']}</h2>
            <div class="grid md:grid-cols-3 gap-4">{related_html}</div>
        </div>

        <div class="text-center">
            <a href="../" class="text-sky-700 font-semibold">{ui['back_to_compare']}</a>
        </div>
    </main>

    <footer class="border-t border-slate-100 mt-16 py-8">
        <div class="max-w-6xl mx-auto px-4 text-center text-slate-600 text-sm">
            <p>© 2026 BreedFinder. {ui['helping_find']}</p>
        </div>
    </footer>
</body>
</html>'''


def main():
    output_dir = BASE_DIR / 'pl' / 'compare' / 'comparisons'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for comp_key, comp in COMPARISONS.items():
        html = generate_article(comp_key, comp)
        path = output_dir / f"{comp['slug']}.html"
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ {path.name}")
    
    print(f"\n✅ Generated 5 fully translated Polish comparison articles")


if __name__ == '__main__':
    main()
