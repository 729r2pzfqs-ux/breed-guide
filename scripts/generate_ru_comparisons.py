#!/usr/bin/env python3
"""Generate Russian comparison articles with full translations."""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

RU_UI = {
    'all_breeds': 'Все Породы',
    'compare': 'Сравнить',
    'take_quiz': 'Пройти Тест',
    'comparisons': 'Сравнения',
    'side_by_side': 'Сравнение Бок о Бок',
    'attribute': 'Характеристика',
    'size': 'Размер',
    'lifespan': 'Продолжительность Жизни',
    'energy_level': 'Уровень Энергии',
    'grooming_needs': 'Потребности в Уходе',
    'trainability': 'Обучаемость',
    'kid_friendly': 'Дружелюбие к Детям',
    'apartment': 'Подходит для Квартиры',
    'shedding': 'Линька',
    'more_comparisons': 'Другие Сравнения',
    'back_to_compare': '← Назад к Сравнениям',
    'view_profile': 'Смотреть полный профиль →',
    'large': 'Крупный',
    'years': 'лет',
    'very_high': 'Очень Высокий',
    'high': 'Высокий',
    'moderate': 'Умеренный',
    'excellent': 'Отлично',
    'not_ideal': 'Не Идеально',
    'heavy': 'Сильная',
    'helping_find': 'Помогаем найти идеального компаньона.',
    'temperament': 'Темперамент',
    'exercise_needs': 'Потребности в Упражнениях',
    'grooming_req': 'Требования к Уходу',
    'which_right': 'Кто Подходит Именно Вам?',
    'choose_if': 'Выбирайте {breed}, если...',
    'bottom_line': 'Итог',
}

RU_TRAITS = {
    'Friendly': 'Дружелюбный', 'Outgoing': 'Общительный', 'Active': 'Активный', 'Gentle': 'Нежный',
    'Intelligent': 'Умный', 'Trusting': 'Доверчивый', 'Devoted': 'Преданный',
    'Reliable': 'Надёжный', 'Trustworthy': 'Верный', 'Kind': 'Добрый',
    'Playful': 'Игривый', 'Adaptable': 'Адаптивный', 'Smart': 'Смышлёный',
    'Affectionate': 'Ласковый', 'Patient': 'Терпеливый', 'Alert': 'Бдительный',
    'Bright': 'Сообразительный', 'Amusing': 'Забавный', 'Lively': 'Живой',
    'Confident': 'Уверенный', 'Courageous': 'Смелый', 'Loyal': 'Лояльный',
    'Versatile': 'Универсальный', 'Protective': 'Защитник', 'Hardworking': 'Трудолюбивый',
    'Intense': 'Интенсивный', 'Mischievous': 'Озорной', 'Dignified': 'Достойный',
    'Strong': 'Сильный', 'Faithful': 'Верный', 'Trainable': 'Обучаемый', 'Proud': 'Гордый',
}

COMPARISONS = {
    'labrador-vs-golden': {
        'slug': 'labrador-vs-golden-retriever',
        'breed1': 'Лабрадор-ретривер',
        'breed2': 'Золотистый ретривер',
        'breed1_slug': 'labrador-retriever',
        'breed2_slug': 'golden-retriever',
        'title': 'Лабрадор vs Золотистый ретривер: Полное Сравнение',
        'desc': 'Сравнение Лабрадора и Золотистого ретривера. Размер, темперамент, потребности в упражнениях и совместимость с семьёй.',
        'intro': 'Две самые любимые семейные породы в мире. Обе дружелюбные, умные и отлично ладят с детьми — но какая подходит именно вам?',
        'breed1_tagline': 'Самая Популярная Порода в Мире',
        'breed2_tagline': 'Любимец Семей',
        'breed1_desc': 'Лабрадор-ретривер — самая популярная порода собак в мире. Они дружелюбные, общительные и полны энергии и любви.',
        'breed2_desc': 'Золотистый ретривер — одна из самых популярных пород. Их дружелюбный и терпеливый характер делает их отличными семейными питомцами.',
        'breed1_traits': ['Friendly', 'Outgoing', 'Active', 'Gentle', 'Intelligent', 'Trusting'],
        'breed2_traits': ['Intelligent', 'Friendly', 'Devoted', 'Reliable', 'Trustworthy', 'Kind'],
        'breed1_temperament_desc': 'Лабрадоры славятся своей дружелюбностью и привязываются ко всей семье. Они хорошо ладят с соседями и другими собаками. Не обманывайтесь их спокойным характером — им нужно много упражнений!',
        'breed2_temperament_desc': 'Золотистые ретриверы общительны, надёжны и стремятся угодить. Они прекрасно ладят с детьми и другими животными. Их терпеливый и нежный характер делает их отличными терапевтическими собаками.',
        'breed1_exercise': 'Высокая энергия, требуется минимум 1-2 часа активных упражнений ежедневно. Любят плавать, приносить предметы и приключения на природе.',
        'breed2_exercise': 'Высокая энергия, но немного менее интенсивная, чем у Лабрадоров. Минимум 1 час упражнений в день. Отлично справляются с апортировкой, плаванием и походами.',
        'breed1_grooming': 'Еженедельное расчёсывание, больше во время линьки. Короткая густая шерсть относительно проста в уходе, но сильно линяет.',
        'breed2_grooming': 'Рекомендуется ежедневное расчёсывание во время линьки. Длинная шерсть требует больше внимания для предотвращения колтунов.',
        'breed1_reasons': ['Вы хотите максимальный уровень энергии', 'Вы предпочитаете меньше ухода', 'Вы хотите универсальную спортивную собаку', 'Вам нравится общительный, энтузиастичный характер', 'Важно разнообразие цветов (чёрный, жёлтый, шоколадный)'],
        'breed2_reasons': ['Вы предпочитаете более спокойный темперамент', 'Вам нравится струящаяся золотистая шерсть', 'Вы хотите отличную терапевтическую/служебную собаку', 'Вы цените нежный, терпеливый характер', 'Вас не пугает частое расчёсывание'],
        'bottom_line': 'Обе породы — исключительные семейные собаки. Лабрадоры немного энергичнее и проще в уходе за шерстью, тогда как Золотистые ретриверы известны своим нежным терпением и струящейся шерстью. Любой выбор принесёт годы любви и дружбы!'
    },
    'frenchie-vs-boston': {
        'slug': 'francuzskij-buldog-vs-boston-terer',
        'breed1': 'Французский бульдог',
        'breed2': 'Бостон-терьер',
        'breed1_slug': 'french-bulldog',
        'breed2_slug': 'boston-terrier',
        'title': 'Французский бульдог vs Бостон-терьер: Полное Сравнение',
        'desc': 'Сравнение Французского бульдога и Бостон-терьера. Компактные компаньоны в сравнении.',
        'intro': 'Две очаровательные компактные породы с большими личностями. Обе отлично подходят для квартиры — но какая лучше для вашего образа жизни?',
        'breed1_tagline': 'Очаровательный Француз',
        'breed2_tagline': 'Американский Джентльмен',
        'breed1_desc': 'Французский бульдог — очаровательная и адаптивная порода с игривым характером, известная своими ушами летучей мыши и ласковой натурой.',
        'breed2_desc': 'Бостон-терьер, известный как "Американский джентльмен", — живая маленькая собака с дружелюбным и весёлым темпераментом.',
        'breed1_traits': ['Playful', 'Adaptable', 'Smart', 'Affectionate', 'Patient', 'Alert'],
        'breed2_traits': ['Friendly', 'Bright', 'Amusing', 'Gentle', 'Lively', 'Intelligent'],
        'breed1_temperament_desc': 'Французские бульдоги спокойны и адаптивны, процветают как в городских квартирах, так и в загородных домах. Они игривы, но не гиперактивны, что делает их отличными компаньонами для разных образов жизни.',
        'breed2_temperament_desc': 'Бостон-терьеры живые, очень умные и имеют нежный характер. Они известны своими отметинами в виде смокинга и дружелюбной, забавной личностью.',
        'breed1_exercise': 'Умеренные потребности в упражнениях — коротких прогулок и игр достаточно. Избегайте чрезмерных нагрузок в жаркую погоду из-за плоской морды.',
        'breed2_exercise': 'Умеренная энергия, нужны ежедневные прогулки и игры. Более атлетичны, чем Французы, но тоже склонны к перегреву.',
        'breed1_grooming': 'Минимальный уход — еженедельное расчёсывание. Регулярно очищайте складки на морде для предотвращения инфекций.',
        'breed2_grooming': 'Низкий уход — периодическое расчёсывание. Их короткая шерсть проста в уходе.',
        'breed1_reasons': ['Вы хотите более спокойного, расслабленного компаньона', 'Вам нравится более крепкое телосложение', 'Вы живёте в квартире', 'Вы хотите минимальные требования к упражнениям', 'Вам нравятся милые уши летучей мыши'],
        'breed2_reasons': ['Вы хотите немного более активную собаку', 'Вам нравится смокинговый окрас', 'Вы хотите более легко обучаемую собаку', 'Вам нравится более атлетичное телосложение', 'Вы хотите породу с большей продолжительностью жизни'],
        'bottom_line': 'Обе — отличные квартирные собаки с большими личностями. Французы более спокойны и расслаблены, тогда как Бостоны немного энергичнее и атлетичнее. Обе покорят ваше сердце!'
    },
    'gsd-vs-malinois': {
        'slug': 'nemeckaja-ovcharka-vs-malinua',
        'breed1': 'Немецкая овчарка',
        'breed2': 'Бельгийская овчарка малинуа',
        'breed1_slug': 'german-shepherd',
        'breed2_slug': 'belgian-malinois',
        'title': 'Немецкая овчарка vs Малинуа: Полное Сравнение',
        'desc': 'Сравнение Немецкой овчарки и Малинуа. Две отличные рабочие собаки в сравнении.',
        'intro': 'Две из самых способных рабочих собак в мире. Обе превосходны в полицейской и военной работе — но имеют важные различия.',
        'breed1_tagline': 'Универсальный Защитник',
        'breed2_tagline': 'Элитная Рабочая Собака',
        'breed1_desc': 'Немецкая овчарка универсальна, умна и является одной из самых популярных рабочих пород в мире.',
        'breed2_desc': 'Бельгийская овчарка малинуа — интенсивная, высокопроизводительная рабочая собака, предпочитаемая полицией и военными по всему миру.',
        'breed1_traits': ['Confident', 'Courageous', 'Smart', 'Loyal', 'Versatile', 'Protective'],
        'breed2_traits': ['Confident', 'Smart', 'Hardworking', 'Alert', 'Intense', 'Protective'],
        'breed1_temperament_desc': 'Немецкие овчарки уверены, смелы и невероятно универсальны. Они формируют глубокие связи с семьёй и естественно защищают, не будучи агрессивными.',
        'breed2_temperament_desc': 'Малинуа — интенсивные, целеустремлённые рабочие собаки с бесконечной энергией. Им нужна работа, и они процветают у опытных владельцев, способных направить их энтузиазм.',
        'breed1_exercise': 'Высокие потребности в упражнениях — минимум 2 часа в день. Превосходны в различных собачьих видах спорта, следовой работе и послушании.',
        'breed2_exercise': 'Очень высокие потребности в упражнениях — 2+ часа интенсивной активности ежедневно. Нуждаются в умственной стимуляции так же, как и в физической.',
        'breed1_grooming': 'Умеренный уход — расчёсывание 2-3 раза в неделю. Сезонная сильная линька требует больше внимания.',
        'breed2_grooming': 'Лёгкий уход — еженедельное расчёсывание. Шерсть короче, чем у Немецкой овчарки, но тоже линяет сезонно.',
        'breed1_reasons': ['Вы хотите универсального семейного защитника', 'Вы предпочитаете немного более спокойную рабочую собаку', 'Вы новичок в рабочих породах', 'Вы хотите собаку, хорошую с детьми', 'Вам нравится классический внешний вид'],
        'breed2_reasons': ['Вы хотите максимальную целеустремлённость и интенсивность', 'Вы опытный владелец', 'Вы хотите элитную спортивную/рабочую собаку', 'Вы можете обеспечить интенсивные упражнения', 'Вы хотите более лёгкую, быструю собаку'],
        'bottom_line': 'Обе — исключительные рабочие собаки, но Малинуа более интенсивны и требуют опытных владельцев. Немецкие овчарки более универсальны и лучше подходят для семей. Выбирайте исходя из вашего уровня опыта и образа жизни.'
    },
    'husky-vs-malamute': {
        'slug': 'haski-vs-malamut',
        'breed1': 'Сибирский хаски',
        'breed2': 'Аляскинский маламут',
        'breed1_slug': 'siberian-husky',
        'breed2_slug': 'alaskan-malamute',
        'title': 'Сибирский хаски vs Аляскинский маламут: Полное Сравнение',
        'desc': 'Сравнение Хаски и Маламута. Арктические породы в сравнении.',
        'intro': 'Две величественные арктические породы с волчьей внешностью. Выглядят похоже, но имеют важные различия в размере и темпераменте.',
        'breed1_tagline': 'Быстрая Ездовая Собака',
        'breed2_tagline': 'Мощный Тягач',
        'breed1_desc': 'Сибирский хаски — атлетичная, выносливая ездовая собака, известная голубыми глазами и дружелюбным характером.',
        'breed2_desc': 'Аляскинский маламут — мощная, крепкая ездовая собака, выведенная для силы и выносливости.',
        'breed1_traits': ['Outgoing', 'Mischievous', 'Loyal', 'Friendly', 'Alert', 'Gentle'],
        'breed2_traits': ['Affectionate', 'Loyal', 'Playful', 'Dignified', 'Devoted', 'Strong'],
        'breed1_temperament_desc': 'Хаски дружелюбны, общительны и иногда озорны. Это стайные собаки, которые любят компанию и известны своей вокальностью и способностью к побегам.',
        'breed2_temperament_desc': 'Маламуты более величественны и менее озорны, чем Хаски. Они глубоко преданы, ласковы с семьёй, но могут быть более независимыми.',
        'breed1_exercise': 'Очень высокая энергия — созданы для бега на километры. Минимум 2 часа активных упражнений ежедневно. Любят бегать и тянуть.',
        'breed2_exercise': 'Высокая энергия, но больше выносливости, чем скорости. Подходят длительные прогулки и работа в упряжке. Могут перегреваться в тёплом климате.',
        'breed1_grooming': 'Интенсивный уход — расчёсывание несколько раз в неделю. Массивная линька ("сдувание шерсти") дважды в год.',
        'breed2_grooming': 'Интенсивный уход, как у Хаски. Их более густая шерсть требует регулярного расчёсывания для предотвращения колтунов.',
        'breed1_reasons': ['Вы хотите арктическую породу среднего размера', 'Вы предпочитаете более быструю, атлетичную собаку', 'Вам нравится разговорчивый, вокальный компаньон', 'Вы хотите впечатляющие голубые глаза', 'Вам нравится более игривый характер'],
        'breed2_reasons': ['Вы хотите более крупную, мощную собаку', 'Вы предпочитаете более спокойный, величественный темперамент', 'У вас есть опыт с сильными породами', 'Вы хотите более тихую собаку (меньше воя)', 'Вам нужна собака для тяжёлой работы'],
        'bottom_line': 'Хаски — атлеты среднего размера, которые любят бегать и "разговаривать". Маламуты — мощные гиганты, созданные для силы. Обе сильно линяют и нуждаются в большом количестве упражнений. Выбирайте исходя из предпочтений по размеру и желаемого темперамента.'
    },
    'poodle-vs-labrador': {
        'slug': 'pudel-vs-labrador',
        'breed1': 'Пудель',
        'breed2': 'Лабрадор-ретривер',
        'breed1_slug': 'poodle',
        'breed2_slug': 'labrador-retriever',
        'title': 'Пудель vs Лабрадор-ретривер: Полное Сравнение',
        'desc': 'Сравнение Пуделя и Лабрадора. Две умные и популярные породы в сравнении.',
        'intro': 'Две из самых умных и популярных пород собак. Обе отличные семейные собаки с очень разной шерстью.',
        'breed1_tagline': 'Элегантный Атлет',
        'breed2_tagline': 'Лучший Друг Каждого',
        'breed1_desc': 'Пудель исключительно умён и активен. За элегантной внешностью скрывается атлетичная и очень сообразительная собака.',
        'breed2_desc': 'Лабрадор-ретривер — самая популярная порода в мире, известная дружелюбным и общительным характером.',
        'breed1_traits': ['Intelligent', 'Active', 'Alert', 'Faithful', 'Trainable', 'Proud'],
        'breed2_traits': ['Friendly', 'Active', 'Outgoing', 'Gentle', 'Intelligent', 'Trusting'],
        'breed1_temperament_desc': 'Пудели исключительно умны и стремятся угодить. Не обманывайтесь модными стрижками — это атлетичные собаки, выведенные для охоты и апортировки.',
        'breed2_temperament_desc': 'Лабрадоры — воплощение дружелюбия — общительны со всеми, терпеливы с детьми и стремятся угодить. Это идеальный семейный компаньон.',
        'breed1_exercise': 'Высокая энергия, нужны ежедневные упражнения и умственная стимуляция. Превосходны в аджилити, послушании и различных собачьих видах спорта.',
        'breed2_exercise': 'Высокая энергия — минимум 1-2 часа в день. Любят плавать, приносить предметы и любую активность с людьми.',
        'breed1_grooming': 'Высокий уход — профессиональный груминг каждые 4-6 недель. Ежедневное расчёсывание предотвращает колтуны. Гипоаллергенная шерсть.',
        'breed2_grooming': 'Лёгкий уход, но много линьки. Еженедельное расчёсывание, больше во время линьки. Не гипоаллергенны.',
        'breed1_reasons': ['У вас аллергия (гипоаллергенны)', 'Вы хотите минимальную линьку', 'Вам нравится груминг или не пугают расходы', 'Вы хотите элегантный внешний вид', 'Вы хотите варианты размера (той/миниатюрный/стандартный)'],
        'breed2_reasons': ['Вы предпочитаете простой, недорогой уход', 'Вас не пугает линька', 'Вы хотите классическую семейную собаку', 'Вы предпочитаете более повседневный вид', 'Вы хотите ретривера, который любит воду'],
        'bottom_line': 'Обе высокоинтеллектуальны и легко обучаемы. Пудели предлагают гипоаллергенную шерсть, но требуют больше ухода. Лабрадоры проще в уходе, но сильно линяют. Обе — отличные семейные компаньоны!'
    }
}


def generate_article(comp_key, comp):
    ui = RU_UI
    breed1_traits = [RU_TRAITS.get(t, t) for t in comp['breed1_traits']]
    breed2_traits = [RU_TRAITS.get(t, t) for t in comp['breed2_traits']]
    
    breed1_tags = '\n                    '.join([f'<span class="bg-amber-100 text-amber-700 px-3 py-1 rounded-full text-sm font-medium">{t}</span>' for t in breed1_traits])
    breed2_tags = '\n                    '.join([f'<span class="bg-yellow-100 text-yellow-700 px-3 py-1 rounded-full text-sm font-medium">{t}</span>' for t in breed2_traits])
    
    breed1_reasons = '\n                        '.join([f'<li class="flex items-start gap-2"><span class="text-green-400">✓</span><span>{r}</span></li>' for r in comp['breed1_reasons']])
    breed2_reasons = '\n                        '.join([f'<li class="flex items-start gap-2"><span class="text-green-400">✓</span><span>{r}</span></li>' for r in comp['breed2_reasons']])
    
    related = [(k, v) for k, v in COMPARISONS.items() if k != comp_key][:3]
    related_html = '\n'.join([f'<a href="{r[1]["slug"]}.html" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md transition"><span class="font-semibold">{r[1]["breed1"]} vs {r[1]["breed2"]}</span></a>' for r in related])
    
    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-VEERQZ53LZ"></script>
    <script>window.dataLayer = window.dataLayer || []; function gtag(){{dataLayer.push(arguments);}} gtag("js", new Date()); gtag("config", "G-VEERQZ53LZ");</script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{comp['title']} | BreedFinder</title>
    <meta name="description" content="{comp['desc']}">
    <link rel="canonical" href="https://breedfinder.org/ru/compare/comparisons/{comp['slug']}.html">
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
                <a href="/breeds/" class="text-slate-600 hover:text-sky-700">{ui['all_breeds']}</a>
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
                    <a href="/breeds/{comp['breed1_slug']}" class="text-sky-700 font-semibold">{ui['view_profile']}</a>
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
                    <a href="/breeds/{comp['breed2_slug']}" class="text-sky-700 font-semibold">{ui['view_profile']}</a>
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
                <h3 class="text-xl font-bold text-amber-600 mb-4">🧠 {comp['breed1']} — {ui['temperament']}</h3>
                <div class="flex flex-wrap gap-2 mb-4">
                    {breed1_tags}
                </div>
                <p class="text-slate-600 text-sm">{comp['breed1_temperament_desc']}</p>
            </div>
            <div class="bg-white rounded-2xl p-6 shadow-lg">
                <h3 class="text-xl font-bold text-yellow-600 mb-4">🧠 {comp['breed2']} — {ui['temperament']}</h3>
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
    output_dir = BASE_DIR / 'ru' / 'compare' / 'comparisons'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for comp_key, comp in COMPARISONS.items():
        html = generate_article(comp_key, comp)
        path = output_dir / f"{comp['slug']}.html"
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ {path.name}")
    
    print(f"\n✅ Generated 5 fully translated Russian comparison articles")


if __name__ == '__main__':
    main()
