#!/usr/bin/env python3
"""Generate Portuguese comparison articles with full translations."""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

PT_UI = {
    'all_breeds': 'Todas as Raças',
    'compare': 'Comparar',
    'take_quiz': 'Fazer Quiz',
    'comparisons': 'Comparações',
    'side_by_side': 'Comparação Lado a Lado',
    'attribute': 'Atributo',
    'size': 'Tamanho',
    'lifespan': 'Expectativa de Vida',
    'energy_level': 'Nível de Energia',
    'grooming_needs': 'Necessidades de Tosa',
    'trainability': 'Treinabilidade',
    'kid_friendly': 'Bom com Crianças',
    'apartment': 'Apto para Apartamento',
    'shedding': 'Queda de Pelo',
    'more_comparisons': 'Mais Comparações',
    'back_to_compare': '← Voltar para Comparar',
    'view_profile': 'Ver perfil completo →',
    'large': 'Grande',
    'years': 'anos',
    'very_high': 'Muito Alto',
    'high': 'Alto',
    'moderate': 'Moderado',
    'excellent': 'Excelente',
    'not_ideal': 'Não Ideal',
    'heavy': 'Intensa',
    'helping_find': 'Ajudando você a encontrar seu companheiro perfeito.',
    'temperament': 'Temperamento',
    'exercise_needs': 'Necessidades de Exercício',
    'grooming_req': 'Requisitos de Tosa',
    'which_right': 'Qual é o Certo para Você?',
    'choose_if': 'Escolha um {breed} se...',
    'bottom_line': 'Conclusão',
}

PT_TRAITS = {
    'Friendly': 'Amigável', 'Outgoing': 'Extrovertido', 'Active': 'Ativo', 'Gentle': 'Gentil',
    'Intelligent': 'Inteligente', 'Trusting': 'Confiante', 'Devoted': 'Devotado',
    'Reliable': 'Confiável', 'Trustworthy': 'Leal', 'Kind': 'Bondoso',
    'Playful': 'Brincalhão', 'Adaptable': 'Adaptável', 'Smart': 'Esperto',
    'Affectionate': 'Afetuoso', 'Patient': 'Paciente', 'Alert': 'Alerta',
    'Bright': 'Brilhante', 'Amusing': 'Divertido', 'Lively': 'Animado',
    'Confident': 'Confiante', 'Courageous': 'Corajoso', 'Loyal': 'Leal',
    'Versatile': 'Versátil', 'Protective': 'Protetor', 'Hardworking': 'Trabalhador',
    'Intense': 'Intenso', 'Mischievous': 'Travesso', 'Dignified': 'Digno',
    'Strong': 'Forte', 'Faithful': 'Fiel', 'Trainable': 'Treinável', 'Proud': 'Orgulhoso',
}

COMPARISONS = {
    'labrador-vs-golden': {
        'slug': 'labrador-vs-golden-retriever',
        'breed1': 'Labrador Retriever',
        'breed2': 'Golden Retriever',
        'breed1_slug': 'labrador-retriever',
        'breed2_slug': 'golden-retriever',
        'title': 'Labrador Retriever vs Golden Retriever: Comparação Completa',
        'desc': 'Comparação Labrador vs Golden Retriever. Veja tamanho, temperamento, necessidades de exercício e adequação familiar.',
        'intro': 'Duas das raças familiares mais amadas do mundo. Ambas são amigáveis, inteligentes e ótimas com crianças—mas qual é a certa para você?',
        'breed1_tagline': 'Raça #1 do Mundo',
        'breed2_tagline': 'O Favorito das Famílias',
        'breed1_desc': 'O Labrador Retriever é a raça de cão mais popular do mundo. São amigáveis, extrovertidos e companheiros cheios de energia e amor.',
        'breed2_desc': 'O Golden Retriever é uma das raças mais populares. Sua atitude amigável e tolerante os torna ótimos animais de estimação familiares.',
        'breed1_traits': ['Friendly', 'Outgoing', 'Active', 'Gentle', 'Intelligent', 'Trusting'],
        'breed2_traits': ['Intelligent', 'Friendly', 'Devoted', 'Reliable', 'Trustworthy', 'Kind'],
        'breed1_temperament_desc': 'Labradores são famosos por sua simpatia e criam laços com toda a família. Socializam bem com vizinhos e outros cães. Não se deixe enganar por sua personalidade tranquila—eles precisam de muito exercício!',
        'breed2_temperament_desc': 'Golden Retrievers são extrovertidos, confiáveis e ansiosos para agradar. São maravilhosos com crianças e outros animais. Sua natureza paciente e gentil os torna excelentes cães de terapia.',
        'breed1_exercise': 'Alta energia, necessitando de pelo menos 1-2 horas de exercício ativo diário. Adoram nadar, buscar objetos e aventuras ao ar livre.',
        'breed2_exercise': 'Alta energia, mas um pouco menos intenso que Labradores. Pelo menos 1 hora de exercício diário. Excelentes em buscar, nadar e caminhadas.',
        'breed1_grooming': 'Escovação semanal, mais durante a temporada de queda de pelo. Pelagem curta e densa é relativamente fácil de manter, mas solta muito pelo.',
        'breed2_grooming': 'Escovação diária recomendada durante a temporada de queda. Pelagem mais longa precisa de mais atenção para evitar nós.',
        'breed1_reasons': ['Você quer o maior nível de energia', 'Você prefere um pouco menos de tosa', 'Você quer um cão esportivo versátil', 'Você ama uma personalidade extrovertida e entusiasmada', 'Variedade de cores importa (preto, amarelo, chocolate)'],
        'breed2_reasons': ['Você prefere um temperamento um pouco mais calmo', 'Você ama a pelagem dourada fluida', 'Você quer um excelente cão de terapia/serviço', 'Você aprecia uma disposição gentil e paciente', 'Você não se importa com escovação mais frequente'],
        'bottom_line': 'Ambas as raças são cães de família excepcionais. Labradores são um pouco mais energéticos e mais fáceis de manter em termos de pelagem, enquanto Golden Retrievers são conhecidos por sua paciência gentil e pelagem fluida. Qualquer escolha trará anos de amor e companheirismo!'
    },
    'frenchie-vs-boston': {
        'slug': 'buldogue-frances-vs-boston-terrier',
        'breed1': 'Buldogue Francês',
        'breed2': 'Boston Terrier',
        'breed1_slug': 'french-bulldog',
        'breed2_slug': 'boston-terrier',
        'title': 'Buldogue Francês vs Boston Terrier: Comparação Completa',
        'desc': 'Comparação Buldogue Francês vs Boston Terrier. Companheiros compactos comparados.',
        'intro': 'Duas raças charmosas e compactas com grandes personalidades. Ambas ótimas para vida em apartamento—mas qual se adapta ao seu estilo de vida?',
        'breed1_tagline': 'O Francês Charmoso',
        'breed2_tagline': 'O Cavalheiro Americano',
        'breed1_desc': 'O Buldogue Francês é uma raça charmosa e adaptável com personalidade brincalhona, conhecido por suas orelhas de morcego e natureza afetuosa.',
        'breed2_desc': 'O Boston Terrier, conhecido como "O Cavalheiro Americano", é um cão pequeno e animado com temperamento amigável e alegre.',
        'breed1_traits': ['Playful', 'Adaptable', 'Smart', 'Affectionate', 'Patient', 'Alert'],
        'breed2_traits': ['Friendly', 'Bright', 'Amusing', 'Gentle', 'Lively', 'Intelligent'],
        'breed1_temperament_desc': 'Buldogues Franceses são tranquilos e adaptáveis, prosperando em apartamentos urbanos ou casas no campo. São brincalhões, mas não hiperativos, tornando-os excelentes companheiros para vários estilos de vida.',
        'breed2_temperament_desc': 'Boston Terriers são animados, muito inteligentes e têm uma disposição gentil. São conhecidos por suas marcas tipo smoking e personalidade amigável e divertida.',
        'breed1_exercise': 'Necessidades moderadas de exercício—caminhadas curtas e sessões de brincadeira são suficientes. Evite esforço excessivo em clima quente devido ao focinho achatado.',
        'breed2_exercise': 'Energia moderada, necessitando de caminhadas diárias e brincadeiras. Mais atlético que Frenchies, mas ainda propenso ao superaquecimento.',
        'breed1_grooming': 'Tosa mínima—escovação semanal. Limpe as rugas faciais regularmente para prevenir infecções.',
        'breed2_grooming': 'Baixa manutenção—escovação ocasional. Sua pelagem curta é fácil de cuidar.',
        'breed1_reasons': ['Você quer um companheiro mais calmo e relaxado', 'Você prefere uma constituição mais robusta', 'Você mora em apartamento', 'Você quer requisitos mínimos de exercício', 'Você ama as adoráveis orelhas de morcego'],
        'breed2_reasons': ['Você quer um cão um pouco mais ativo', 'Você prefere o visual de smoking', 'Você quer um cão mais fácil de treinar', 'Você gosta de uma constituição mais atlética', 'Você quer uma raça que vive mais'],
        'bottom_line': 'Ambos são excelentes cães de apartamento com grandes personalidades. Frenchies são mais calmos e relaxados, enquanto Bostons são um pouco mais energéticos e atléticos. Ambos vão roubar seu coração!'
    },
    'gsd-vs-malinois': {
        'slug': 'pastor-alemao-vs-malinois',
        'breed1': 'Pastor Alemão',
        'breed2': 'Malinois Belga',
        'breed1_slug': 'german-shepherd',
        'breed2_slug': 'belgian-malinois',
        'title': 'Pastor Alemão vs Malinois Belga: Comparação Completa',
        'desc': 'Comparação Pastor Alemão vs Malinois. Dois excelentes cães de trabalho comparados.',
        'intro': 'Dois dos cães de trabalho mais capazes do mundo. Ambos se destacam em trabalho policial e militar—mas têm diferenças importantes.',
        'breed1_tagline': 'O Protetor Versátil',
        'breed2_tagline': 'Cão de Trabalho de Elite',
        'breed1_desc': 'O Pastor Alemão é versátil, inteligente e uma das raças de trabalho mais populares do mundo.',
        'breed2_desc': 'O Malinois Belga é um cão de trabalho intenso e de alto desempenho, preferido por polícias e militares em todo o mundo.',
        'breed1_traits': ['Confident', 'Courageous', 'Smart', 'Loyal', 'Versatile', 'Protective'],
        'breed2_traits': ['Confident', 'Smart', 'Hardworking', 'Alert', 'Intense', 'Protective'],
        'breed1_temperament_desc': 'Pastores Alemães são confiantes, corajosos e incrivelmente versáteis. Criam laços profundos com a família e são naturalmente protetores sem serem agressivos.',
        'breed2_temperament_desc': 'Malinois são cães de trabalho intensos e motivados com energia infinita. Precisam de uma tarefa e prosperam com donos experientes que podem canalizar sua motivação.',
        'breed1_exercise': 'Altas necessidades de exercício—pelo menos 2 horas diárias. Excelentes em vários esportes caninos, rastreamento e obediência.',
        'breed2_exercise': 'Necessidades de exercício muito altas—2+ horas de atividade intensa diária. Precisam de estimulação mental tanto quanto exercício físico.',
        'breed1_grooming': 'Tosa moderada—escove 2-3 vezes por semana. Queda de pelo sazonal intensa requer mais atenção.',
        'breed2_grooming': 'Tosa fácil—escovação semanal. Pelagem mais curta que o Pastor Alemão, mas ainda solta pelo sazonalmente.',
        'breed1_reasons': ['Você quer um protetor familiar versátil', 'Você prefere um cão de trabalho um pouco mais calmo', 'Você é dono de primeira viagem de raça de trabalho', 'Você quer um cão bom com crianças', 'Você prefere o visual clássico'],
        'breed2_reasons': ['Você quer máxima motivação e intensidade', 'Você é um dono experiente', 'Você quer um cão de esporte/trabalho de elite', 'Você pode fornecer exercício extensivo', 'Você quer um cão mais leve e rápido'],
        'bottom_line': 'Ambos são cães de trabalho excepcionais, mas Malinois são mais intensos e requerem donos experientes. Pastores Alemães são mais versáteis e mais adequados para famílias. Escolha baseado no seu nível de experiência e estilo de vida.'
    },
    'husky-vs-malamute': {
        'slug': 'husky-vs-malamute',
        'breed1': 'Husky Siberiano',
        'breed2': 'Malamute do Alasca',
        'breed1_slug': 'siberian-husky',
        'breed2_slug': 'alaskan-malamute',
        'title': 'Husky Siberiano vs Malamute do Alasca: Comparação Completa',
        'desc': 'Comparação Husky vs Malamute. Raças árticas comparadas lado a lado.',
        'intro': 'Duas raças árticas majestosas com aparência de lobo. Parecem semelhantes, mas têm diferenças importantes em tamanho e temperamento.',
        'breed1_tagline': 'O Cão de Trenó Veloz',
        'breed2_tagline': 'O Poderoso Puxador',
        'breed1_desc': 'O Husky Siberiano é um cão de trenó atlético e resistente, conhecido por seus olhos azuis e personalidade amigável.',
        'breed2_desc': 'O Malamute do Alasca é um cão de trenó poderoso e robusto, criado para força e resistência.',
        'breed1_traits': ['Outgoing', 'Mischievous', 'Loyal', 'Friendly', 'Alert', 'Gentle'],
        'breed2_traits': ['Affectionate', 'Loyal', 'Playful', 'Dignified', 'Devoted', 'Strong'],
        'breed1_temperament_desc': 'Huskies são amigáveis, extrovertidos e às vezes travessos. São cães de matilha que amam companhia e são conhecidos por sua natureza vocal e habilidades de fuga.',
        'breed2_temperament_desc': 'Malamutes são mais dignos e menos travessos que Huskies. São profundamente leais, afetuosos com a família, mas podem ser mais independentes.',
        'breed1_exercise': 'Energia muito alta—projetados para correr quilômetros. Pelo menos 2 horas de exercício ativo diário. Adoram correr e atividades de tração.',
        'breed2_exercise': 'Alta energia, mas com mais resistência que velocidade. Longas caminhadas e trabalho de tração são adequados. Podem superaquecer em climas quentes.',
        'breed1_grooming': 'Tosa extensiva—escove várias vezes por semana. Queda de pelo massiva ("soprar a pelagem") duas vezes ao ano.',
        'breed2_grooming': 'Tosa extensiva como o Husky. Sua pelagem mais espessa requer escovação regular para evitar nós.',
        'breed1_reasons': ['Você quer uma raça ártica de médio porte', 'Você prefere um cão mais rápido e atlético', 'Você gosta de um companheiro falante e vocal', 'Você quer olhos azuis impressionantes', 'Você gosta de uma personalidade mais brincalhona'],
        'breed2_reasons': ['Você quer um cão maior e mais poderoso', 'Você prefere um temperamento mais calmo e digno', 'Você tem experiência com raças fortes', 'Você quer um cão mais silencioso (menos uivos)', 'Você precisa de um cão para tração/puxar'],
        'bottom_line': 'Huskies são atletas de médio porte que adoram correr e "conversar". Malamutes são gigantes poderosos construídos para força. Ambos soltam muito pelo e precisam de muito exercício. Escolha baseado na preferência de tamanho e temperamento desejado.'
    },
    'poodle-vs-labrador': {
        'slug': 'poodle-vs-labrador',
        'breed1': 'Poodle',
        'breed2': 'Labrador Retriever',
        'breed1_slug': 'poodle',
        'breed2_slug': 'labrador-retriever',
        'title': 'Poodle vs Labrador Retriever: Comparação Completa',
        'desc': 'Comparação Poodle vs Labrador. Duas raças inteligentes e populares comparadas.',
        'intro': 'Duas das raças de cães mais inteligentes e populares. Ambas são excelentes cães de família com pelagens muito diferentes.',
        'breed1_tagline': 'O Atleta Elegante',
        'breed2_tagline': 'O Melhor Amigo de Todos',
        'breed1_desc': 'O Poodle é excepcionalmente inteligente e ativo. Por trás da aparência elegante há um cão atlético e muito esperto.',
        'breed2_desc': 'O Labrador Retriever é a raça mais popular do mundo, conhecida por sua natureza amigável e extrovertida.',
        'breed1_traits': ['Intelligent', 'Active', 'Alert', 'Faithful', 'Trainable', 'Proud'],
        'breed2_traits': ['Friendly', 'Active', 'Outgoing', 'Gentle', 'Intelligent', 'Trusting'],
        'breed1_temperament_desc': 'Poodles são excepcionalmente inteligentes e ansiosos para agradar. Não se deixe enganar pelos cortes elegantes—são cães atléticos criados para caça e busca.',
        'breed2_temperament_desc': 'Labradores são o cão amigável por excelência—extrovertidos com todos, pacientes com crianças e ansiosos para agradar. São o companheiro familiar definitivo.',
        'breed1_exercise': 'Alta energia, necessitando de exercício diário e estimulação mental. Excelentes em agility, obediência e vários esportes caninos.',
        'breed2_exercise': 'Alta energia—pelo menos 1-2 horas diárias. Adoram nadar, buscar objetos e qualquer atividade com seus humanos.',
        'breed1_grooming': 'Alta manutenção—tosa profissional a cada 4-6 semanas. Escovação diária previne nós. Pelagem hipoalergênica.',
        'breed2_grooming': 'Tosa fácil, mas muita queda de pelo. Escovação semanal, mais durante a temporada de queda. Não é hipoalergênico.',
        'breed1_reasons': ['Você tem alergias (hipoalergênico)', 'Você quer mínima queda de pelo', 'Você gosta de tosa ou não se importa com o custo', 'Você quer uma aparência elegante', 'Você quer opções de tamanho (toy/mini/standard)'],
        'breed2_reasons': ['Você prefere tosa fácil e barata', 'Você não se importa com queda de pelo', 'Você quer o cão de família clássico', 'Você prefere um visual mais casual', 'Você quer um retriever que ama água'],
        'bottom_line': 'Ambos são altamente inteligentes e fáceis de treinar. Poodles oferecem pelagem hipoalergênica, mas precisam de mais tosa. Labradores são mais fáceis de manter, mas soltam muito pelo. Ambos são companheiros familiares excelentes!'
    }
}


def generate_article(comp_key, comp):
    ui = PT_UI
    breed1_traits = [PT_TRAITS.get(t, t) for t in comp['breed1_traits']]
    breed2_traits = [PT_TRAITS.get(t, t) for t in comp['breed2_traits']]
    
    breed1_tags = '\n                    '.join([f'<span class="bg-amber-100 text-amber-700 px-3 py-1 rounded-full text-sm font-medium">{t}</span>' for t in breed1_traits])
    breed2_tags = '\n                    '.join([f'<span class="bg-yellow-100 text-yellow-700 px-3 py-1 rounded-full text-sm font-medium">{t}</span>' for t in breed2_traits])
    
    breed1_reasons = '\n                        '.join([f'<li class="flex items-start gap-2"><span class="text-green-400">✓</span><span>{r}</span></li>' for r in comp['breed1_reasons']])
    breed2_reasons = '\n                        '.join([f'<li class="flex items-start gap-2"><span class="text-green-400">✓</span><span>{r}</span></li>' for r in comp['breed2_reasons']])
    
    related = [(k, v) for k, v in COMPARISONS.items() if k != comp_key][:3]
    related_html = '\n'.join([f'<a href="{r[1]["slug"]}.html" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md transition"><span class="font-semibold">{r[1]["breed1"]} vs {r[1]["breed2"]}</span></a>' for r in related])
    
    return f'''<!DOCTYPE html>
<html lang="pt">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-VEERQZ53LZ"></script>
    <script>window.dataLayer = window.dataLayer || []; function gtag(){{dataLayer.push(arguments);}} gtag("js", new Date()); gtag("config", "G-VEERQZ53LZ");</script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{comp['title']} | BreedFinder</title>
    <meta name="description" content="{comp['desc']}">
    <link rel="canonical" href="https://breedfinder.org/pt/compare/comparisons/{comp['slug']}.html">
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
    output_dir = BASE_DIR / 'pt' / 'compare' / 'comparisons'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for comp_key, comp in COMPARISONS.items():
        html = generate_article(comp_key, comp)
        path = output_dir / f"{comp['slug']}.html"
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ {path.name}")
    
    print(f"\n✅ Generated 5 fully translated Portuguese comparison articles")


if __name__ == '__main__':
    main()
