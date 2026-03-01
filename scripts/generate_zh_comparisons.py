#!/usr/bin/env python3
"""Generate Chinese comparison articles with full translations."""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

ZH_UI = {
    'all_breeds': '所有品种',
    'compare': '比较',
    'take_quiz': '做测试',
    'comparisons': '品种对比',
    'side_by_side': '并排比较',
    'attribute': '特征',
    'size': '体型',
    'lifespan': '寿命',
    'energy_level': '精力水平',
    'grooming_needs': '美容需求',
    'trainability': '可训练性',
    'kid_friendly': '儿童友好度',
    'apartment': '公寓适宜性',
    'shedding': '掉毛程度',
    'more_comparisons': '更多比较',
    'back_to_compare': '← 返回比较',
    'view_profile': '查看完整档案 →',
    'large': '大型',
    'years': '年',
    'very_high': '非常高',
    'high': '高',
    'moderate': '中等',
    'excellent': '优秀',
    'not_ideal': '不理想',
    'heavy': '大量',
    'helping_find': '帮助您找到完美的伙伴。',
    'temperament': '性格',
    'exercise_needs': '运动需求',
    'grooming_req': '美容要求',
    'which_right': '哪个适合您？',
    'choose_if': '如果您想要{breed}...',
    'bottom_line': '总结',
}

ZH_TRAITS = {
    'Friendly': '友善', 'Outgoing': '外向', 'Active': '活跃', 'Gentle': '温柔',
    'Intelligent': '聪明', 'Trusting': '信任', 'Devoted': '忠诚',
    'Reliable': '可靠', 'Trustworthy': '值得信赖', 'Kind': '善良',
    'Playful': '爱玩', 'Adaptable': '适应性强', 'Smart': '机灵',
    'Affectionate': '深情', 'Patient': '耐心', 'Alert': '警觉',
    'Bright': '聪慧', 'Amusing': '有趣', 'Lively': '活泼',
    'Confident': '自信', 'Courageous': '勇敢', 'Loyal': '忠实',
    'Versatile': '多才多艺', 'Protective': '保护性强', 'Hardworking': '勤劳',
    'Intense': '强烈', 'Mischievous': '淘气', 'Dignified': '有威严',
    'Strong': '强壮', 'Faithful': '忠诚', 'Trainable': '易训练', 'Proud': '骄傲',
}

COMPARISONS = {
    'labrador-vs-golden': {
        'slug': 'labrador-vs-golden-retriever',
        'breed1': '拉布拉多',
        'breed2': '金毛寻回犬',
        'breed1_slug': 'labrador-retriever',
        'breed2_slug': 'golden-retriever',
        'title': '拉布拉多 vs 金毛寻回犬：完整对比',
        'desc': '拉布拉多与金毛寻回犬比较。查看体型、性格、运动需求和家庭适合度。',
        'intro': '世界上最受欢迎的两种家庭犬。都很友善、聪明，与孩子相处融洽——但哪个适合您？',
        'breed1_tagline': '世界最受欢迎的品种',
        'breed2_tagline': '家庭最爱',
        'breed1_desc': '拉布拉多是世界上最受欢迎的犬种。它们友善、外向，充满能量和爱。',
        'breed2_desc': '金毛寻回犬是最受欢迎的品种之一。它们友善宽容的态度使它们成为出色的家庭宠物。',
        'breed1_traits': ['Friendly', 'Outgoing', 'Active', 'Gentle', 'Intelligent', 'Trusting'],
        'breed2_traits': ['Intelligent', 'Friendly', 'Devoted', 'Reliable', 'Trustworthy', 'Kind'],
        'breed1_temperament_desc': '拉布拉多以友善著称，与全家人都能建立联系。它们与邻居和其他狗相处融洽。不要被它们悠闲的性格所迷惑——它们需要大量运动！',
        'breed2_temperament_desc': '金毛寻回犬外向、可靠、渴望取悦。它们与孩子和其他动物相处融洽。耐心温和的性格使它们成为优秀的治疗犬。',
        'breed1_exercise': '高能量，每天需要至少1-2小时积极运动。喜欢游泳、捡球和户外冒险。',
        'breed2_exercise': '高能量，但比拉布拉多稍温和。每天至少1小时运动。擅长捡球、游泳和远足。',
        'breed1_grooming': '每周刷毛，换毛期需要更多。短而密的被毛相对容易打理，但掉毛多。',
        'breed2_grooming': '换毛期建议每天刷毛。较长的被毛需要更多注意以防止打结。',
        'breed1_reasons': ['您想要最高的能量水平', '您偏好较少的美容工作', '您想要一只多才多艺的运动犬', '您喜欢外向、热情的性格', '颜色多样性很重要（黑色、黄色、巧克力色）'],
        'breed2_reasons': ['您偏好稍微冷静的性格', '您喜欢飘逸的金色被毛', '您想要一只优秀的治疗/服务犬', '您欣赏温和、耐心的性格', '您不介意更频繁的刷毛'],
        'bottom_line': '两种品种都是出色的家庭犬。拉布拉多精力更充沛，被毛更容易打理，而金毛寻回犬以温和的耐心和飘逸的被毛著称。无论选择哪个，都将带来多年的爱与陪伴！'
    },
    'frenchie-vs-boston': {
        'slug': 'faguo-dougou-vs-boston-geng',
        'breed1': '法国斗牛犬',
        'breed2': '波士顿梗',
        'breed1_slug': 'french-bulldog',
        'breed2_slug': 'boston-terrier',
        'title': '法国斗牛犬 vs 波士顿梗：完整对比',
        'desc': '法国斗牛犬与波士顿梗比较。紧凑型伴侣犬对比。',
        'intro': '两种迷人的紧凑型品种，个性十足。都非常适合公寓生活——但哪个更适合您的生活方式？',
        'breed1_tagline': '迷人的法国狗',
        'breed2_tagline': '美国绅士',
        'breed1_desc': '法国斗牛犬是一种迷人且适应性强的品种，性格活泼，以蝙蝠耳和深情的天性著称。',
        'breed2_desc': '波士顿梗被称为"美国绅士"，是一种活泼的小型犬，性格友好开朗。',
        'breed1_traits': ['Playful', 'Adaptable', 'Smart', 'Affectionate', 'Patient', 'Alert'],
        'breed2_traits': ['Friendly', 'Bright', 'Amusing', 'Gentle', 'Lively', 'Intelligent'],
        'breed1_temperament_desc': '法国斗牛犬性格悠闲、适应性强，无论在城市公寓还是乡村住宅都能茁壮成长。它们爱玩但不过度活跃，是各种生活方式的理想伴侣。',
        'breed2_temperament_desc': '波士顿梗活泼、非常聪明、性格温和。以燕尾服式的斑纹和友好有趣的个性著称。',
        'breed1_exercise': '中等运动需求——短途散步和游戏时间就足够了。由于扁平的鼻子，炎热天气避免过度运动。',
        'breed2_exercise': '中等能量，需要每天散步和玩耍。比法斗更具运动性，但也容易过热。',
        'breed1_grooming': '最少美容——每周刷毛。定期清洁面部皱褶以防感染。',
        'breed2_grooming': '低维护——偶尔刷毛。短被毛易于打理。',
        'breed1_reasons': ['您想要更冷静、放松的伴侣', '您偏好更结实的体格', '您住在公寓里', '您想要最少的运动要求', '您喜欢可爱的蝙蝠耳'],
        'breed2_reasons': ['您想要稍微更活跃的狗', '您偏好燕尾服造型', '您想要更容易训练的狗', '您喜欢更具运动性的体格', '您想要寿命更长的品种'],
        'bottom_line': '两者都是出色的公寓犬，个性十足。法斗更冷静放松，波士顿稍微更有活力和运动性。两者都会偷走您的心！'
    },
    'gsd-vs-malinois': {
        'slug': 'demu-vs-malinuoa',
        'breed1': '德国牧羊犬',
        'breed2': '比利时马林诺斯',
        'breed1_slug': 'german-shepherd',
        'breed2_slug': 'belgian-malinois',
        'title': '德国牧羊犬 vs 比利时马林诺斯：完整对比',
        'desc': '德国牧羊犬与马林诺斯比较。两种优秀的工作犬对比。',
        'intro': '世界上最有能力的两种工作犬。都在警察和军事工作中表现出色——但有重要的区别。',
        'breed1_tagline': '多才多艺的守护者',
        'breed2_tagline': '精英工作犬',
        'breed1_desc': '德国牧羊犬多才多艺、聪明，是世界上最受欢迎的工作犬种之一。',
        'breed2_desc': '比利时马林诺斯是一种强烈的高性能工作犬，受到世界各地警察和军队的青睐。',
        'breed1_traits': ['Confident', 'Courageous', 'Smart', 'Loyal', 'Versatile', 'Protective'],
        'breed2_traits': ['Confident', 'Smart', 'Hardworking', 'Alert', 'Intense', 'Protective'],
        'breed1_temperament_desc': '德国牧羊犬自信、勇敢、多才多艺。它们与家人建立深厚的联系，天生具有保护性但不具攻击性。',
        'breed2_temperament_desc': '马林诺斯是强烈、有动力的工作犬，精力无穷。它们需要工作任务，在能够引导其动力的经验丰富的主人身边茁壮成长。',
        'breed1_exercise': '高运动需求——每天至少2小时。在各种犬类运动、追踪和服从训练中表现出色。',
        'breed2_exercise': '非常高的运动需求——每天2小时以上的剧烈活动。需要与身体运动一样多的精神刺激。',
        'breed1_grooming': '中等美容——每周刷毛2-3次。季节性大量掉毛需要更多注意。',
        'breed2_grooming': '简单美容——每周刷毛。被毛比德牧短，但也会季节性掉毛。',
        'breed1_reasons': ['您想要多才多艺的家庭守护者', '您偏好稍微冷静的工作犬', '您是工作犬品种的新手主人', '您想要与孩子相处好的狗', '您偏好经典外观'],
        'breed2_reasons': ['您想要最大的动力和强度', '您是经验丰富的主人', '您想要精英运动/工作犬', '您可以提供大量运动', '您想要更轻、更快的狗'],
        'bottom_line': '两者都是出色的工作犬，但马林诺斯更强烈，需要经验丰富的主人。德国牧羊犬更多才多艺，更适合家庭。根据您的经验水平和生活方式选择。'
    },
    'husky-vs-malamute': {
        'slug': 'hashiqi-vs-alasijia',
        'breed1': '西伯利亚哈士奇',
        'breed2': '阿拉斯加雪橇犬',
        'breed1_slug': 'siberian-husky',
        'breed2_slug': 'alaskan-malamute',
        'title': '西伯利亚哈士奇 vs 阿拉斯加雪橇犬：完整对比',
        'desc': '哈士奇与阿拉斯加比较。北极品种并排对比。',
        'intro': '两种具有狼一般外表的雄伟北极品种。看起来相似，但在体型和性格上有重要区别。',
        'breed1_tagline': '快速雪橇犬',
        'breed2_tagline': '强壮的拉力犬',
        'breed1_desc': '西伯利亚哈士奇是一种运动型、耐力强的雪橇犬，以蓝眼睛和友好的个性著称。',
        'breed2_desc': '阿拉斯加雪橇犬是一种强壮、结实的雪橇犬，为力量和耐力而培育。',
        'breed1_traits': ['Outgoing', 'Mischievous', 'Loyal', 'Friendly', 'Alert', 'Gentle'],
        'breed2_traits': ['Affectionate', 'Loyal', 'Playful', 'Dignified', 'Devoted', 'Strong'],
        'breed1_temperament_desc': '哈士奇友好、外向，有时淘气。它们是喜欢陪伴的群居犬，以爱叫和逃跑能力著称。',
        'breed2_temperament_desc': '阿拉斯加比哈士奇更有威严，不那么淘气。它们非常忠诚，对家人深情，但可能更独立。',
        'breed1_exercise': '非常高的能量——生来就是为了跑几公里。每天至少2小时积极运动。喜欢跑步和拉拽活动。',
        'breed2_exercise': '高能量，但更多是耐力而非速度。长途远足和拉拽工作都很合适。在温暖气候中可能过热。',
        'breed1_grooming': '大量美容——每周刷毛几次。每年两次大量掉毛（"吹毛"）。',
        'breed2_grooming': '与哈士奇相似的大量美容。较厚的被毛需要定期刷毛以防打结。',
        'breed1_reasons': ['您想要中型北极品种', '您偏好更快、更具运动性的狗', '您喜欢爱说话、爱叫的伴侣', '您想要令人印象深刻的蓝眼睛', '您喜欢更爱玩的个性'],
        'breed2_reasons': ['您想要更大、更强壮的狗', '您偏好更冷静、更有威严的性格', '您有强壮品种的经验', '您想要更安静的狗（嚎叫更少）', '您需要用于拉拽/雪橇工作的狗'],
        'bottom_line': '哈士奇是喜欢跑步和"说话"的中型运动员。阿拉斯加是为力量而生的强壮巨人。两者都大量掉毛，需要大量运动。根据体型偏好和期望的性格选择。'
    },
    'poodle-vs-labrador': {
        'slug': 'guibinguan-vs-labrador',
        'breed1': '贵宾犬',
        'breed2': '拉布拉多',
        'breed1_slug': 'poodle',
        'breed2_slug': 'labrador-retriever',
        'title': '贵宾犬 vs 拉布拉多：完整对比',
        'desc': '贵宾犬与拉布拉多比较。两种聪明且受欢迎的品种对比。',
        'intro': '两种最聪明、最受欢迎的犬种。都是出色的家庭犬，但被毛非常不同。',
        'breed1_tagline': '优雅的运动员',
        'breed2_tagline': '每个人的好朋友',
        'breed1_desc': '贵宾犬非常聪明且活跃。优雅的外表背后是一只运动能力强、非常聪明的狗。',
        'breed2_desc': '拉布拉多是世界上最受欢迎的品种，以友善和外向的天性著称。',
        'breed1_traits': ['Intelligent', 'Active', 'Alert', 'Faithful', 'Trainable', 'Proud'],
        'breed2_traits': ['Friendly', 'Active', 'Outgoing', 'Gentle', 'Intelligent', 'Trusting'],
        'breed1_temperament_desc': '贵宾犬非常聪明，渴望取悦。不要被花哨的造型所迷惑——它们是为狩猎和衔取而培育的运动犬。',
        'breed2_temperament_desc': '拉布拉多是最友善的狗——与每个人都很友好，对孩子有耐心，渴望取悦。它们是终极家庭伴侣。',
        'breed1_exercise': '高能量，需要每天运动和精神刺激。在敏捷、服从和各种犬类运动中表现出色。',
        'breed2_exercise': '高能量——每天至少1-2小时。喜欢游泳、衔取和与人类进行的任何活动。',
        'breed1_grooming': '高维护——每4-6周专业美容。每天刷毛防止打结。低过敏性被毛。',
        'breed2_grooming': '简单美容，但大量掉毛。每周刷毛，掉毛季节更多。不是低过敏性的。',
        'breed1_reasons': ['您有过敏症（低过敏性）', '您想要最少掉毛', '您喜欢美容或不介意费用', '您想要优雅的外观', '您想要体型选项（玩具型/迷你型/标准型）'],
        'breed2_reasons': ['您偏好简单、便宜的美容', '您不介意掉毛', '您想要经典的家庭犬', '您偏好更休闲的外观', '您想要一只爱水的寻回犬'],
        'bottom_line': '两者都非常聪明且易于训练。贵宾犬提供低过敏性被毛，但需要更多美容。拉布拉多更容易维护，但大量掉毛。两者都是出色的家庭伴侣！'
    }
}


def generate_article(comp_key, comp):
    ui = ZH_UI
    breed1_traits = [ZH_TRAITS.get(t, t) for t in comp['breed1_traits']]
    breed2_traits = [ZH_TRAITS.get(t, t) for t in comp['breed2_traits']]
    breed1_tags = '\n                    '.join([f'<span class="bg-amber-100 text-amber-700 px-3 py-1 rounded-full text-sm font-medium">{t}</span>' for t in breed1_traits])
    breed2_tags = '\n                    '.join([f'<span class="bg-yellow-100 text-yellow-700 px-3 py-1 rounded-full text-sm font-medium">{t}</span>' for t in breed2_traits])
    breed1_reasons = '\n                        '.join([f'<li class="flex items-start gap-2"><span class="text-green-400">✓</span><span>{r}</span></li>' for r in comp['breed1_reasons']])
    breed2_reasons = '\n                        '.join([f'<li class="flex items-start gap-2"><span class="text-green-400">✓</span><span>{r}</span></li>' for r in comp['breed2_reasons']])
    related = [(k, v) for k, v in COMPARISONS.items() if k != comp_key][:3]
    related_html = '\n'.join([f'<a href="{r[1]["slug"]}.html" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md transition"><span class="font-semibold">{r[1]["breed1"]} vs {r[1]["breed2"]}</span></a>' for r in related])
    
    return f'''<!DOCTYPE html>
<html lang="zh">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-VEERQZ53LZ"></script>
    <script>window.dataLayer = window.dataLayer || []; function gtag(){{dataLayer.push(arguments);}} gtag("js", new Date()); gtag("config", "G-VEERQZ53LZ");</script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{comp['title']} | BreedFinder</title>
    <meta name="description" content="{comp['desc']}">
    <link rel="canonical" href="https://breedfinder.org/zh/compare/comparisons/{comp['slug']}.html">
    <link rel="icon" href="../../../favicon.ico">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>* {{ font-family: 'Plus Jakarta Sans', sans-serif; }}</style>
</head>
<body class="bg-gradient-to-br from-sky-50 via-white to-blue-50 min-h-screen text-slate-800">
    <header class="bg-white/80 backdrop-blur-md border-b border-slate-100 sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
            <a href="../../" class="flex items-center gap-3"><img src="../../../logo-192.png" class="w-10 h-10" alt="BreedFinder"><span class="text-xl font-bold">BreedFinder</span></a>
            <nav class="flex items-center gap-6 text-sm font-medium">
                <a href="../../breeds" class="text-slate-600 hover:text-sky-700">{ui['all_breeds']}</a>
                <a href="../" class="text-slate-600 hover:text-sky-700">{ui['compare']}</a>
                <a href="../../quiz" class="bg-sky-500 text-white px-5 py-2.5 rounded-xl font-semibold">{ui['take_quiz']}</a>
            </nav>
        </div>
    </header>
    <main class="max-w-6xl mx-auto px-4 py-12">
        <nav class="text-sm text-slate-600 mb-8"><a href="../">{ui['compare']}</a> › <a href="./">{ui['comparisons']}</a> › {comp['breed1']} vs {comp['breed2']}</nav>
        <div class="text-center mb-12">
            <h1 class="text-4xl md:text-5xl font-extrabold mb-4"><span class="text-amber-500">{comp['breed1']}</span><span class="text-slate-600 mx-4">vs</span><span class="text-yellow-500">{comp['breed2']}</span></h1>
            <p class="text-lg text-slate-600 max-w-2xl mx-auto">{comp['intro']}</p>
        </div>
        <div class="grid md:grid-cols-2 gap-8 mb-12">
            <div class="bg-white rounded-3xl shadow-xl overflow-hidden">
                <div class="bg-gradient-to-r from-amber-500 to-amber-600 p-6 text-white text-center">
                    <img src="../../../images/heads/{comp['breed1_slug']}.webp" alt="{comp['breed1']}" class="w-32 h-32 rounded-full mx-auto mb-4 object-cover border-4 border-white/30">
                    <h2 class="text-2xl font-bold">{comp['breed1']}</h2><p class="text-amber-100">{comp['breed1_tagline']}</p>
                </div>
                <div class="p-6"><p class="text-slate-600 mb-4">{comp['breed1_desc']}</p><a href="../../breeds/{comp['breed1_slug']}" class="text-sky-700 font-semibold">{ui['view_profile']}</a></div>
            </div>
            <div class="bg-white rounded-3xl shadow-xl overflow-hidden">
                <div class="bg-gradient-to-r from-yellow-500 to-yellow-600 p-6 text-white text-center">
                    <img src="../../../images/heads/{comp['breed2_slug']}.webp" alt="{comp['breed2']}" class="w-32 h-32 rounded-full mx-auto mb-4 object-cover border-4 border-white/30">
                    <h2 class="text-2xl font-bold">{comp['breed2']}</h2><p class="text-yellow-100">{comp['breed2_tagline']}</p>
                </div>
                <div class="p-6"><p class="text-slate-600 mb-4">{comp['breed2_desc']}</p><a href="../../breeds/{comp['breed2_slug']}" class="text-sky-700 font-semibold">{ui['view_profile']}</a></div>
            </div>
        </div>
        <div class="bg-white rounded-3xl shadow-xl overflow-hidden mb-12">
            <div class="bg-slate-800 p-6 text-white"><h2 class="text-2xl font-bold text-center">{ui['side_by_side']}</h2></div>
            <table class="w-full">
                <thead><tr class="bg-slate-50"><th class="p-4 text-left">{ui['attribute']}</th><th class="p-4 text-center text-amber-600">{comp['breed1']}</th><th class="p-4 text-center text-yellow-600">{comp['breed2']}</th></tr></thead>
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
            <div class="bg-white rounded-2xl p-6 shadow-lg"><h3 class="text-xl font-bold text-amber-600 mb-4">🧠 {comp['breed1']} {ui['temperament']}</h3><div class="flex flex-wrap gap-2 mb-4">{breed1_tags}</div><p class="text-slate-600 text-sm">{comp['breed1_temperament_desc']}</p></div>
            <div class="bg-white rounded-2xl p-6 shadow-lg"><h3 class="text-xl font-bold text-yellow-600 mb-4">🧠 {comp['breed2']} {ui['temperament']}</h3><div class="flex flex-wrap gap-2 mb-4">{breed2_tags}</div><p class="text-slate-600 text-sm">{comp['breed2_temperament_desc']}</p></div>
        </div>
        <div class="grid md:grid-cols-2 gap-8 mb-12">
            <div class="bg-gradient-to-br from-sky-50 to-sky-100 rounded-2xl p-6"><h3 class="text-xl font-bold text-sky-700 mb-4">🏃 {ui['exercise_needs']}</h3><div class="space-y-4"><div><span class="font-semibold text-amber-600">{comp['breed1']}:</span><p class="text-slate-600 text-sm">{comp['breed1_exercise']}</p></div><div><span class="font-semibold text-yellow-600">{comp['breed2']}:</span><p class="text-slate-600 text-sm">{comp['breed2_exercise']}</p></div></div></div>
            <div class="bg-gradient-to-br from-sky-50 to-sky-100 rounded-2xl p-6"><h3 class="text-xl font-bold text-sky-700 mb-4">✂️ {ui['grooming_req']}</h3><div class="space-y-4"><div><span class="font-semibold text-amber-600">{comp['breed1']}:</span><p class="text-slate-600 text-sm">{comp['breed1_grooming']}</p></div><div><span class="font-semibold text-yellow-600">{comp['breed2']}:</span><p class="text-slate-600 text-sm">{comp['breed2_grooming']}</p></div></div></div>
        </div>
        <div class="bg-gradient-to-r from-slate-800 to-slate-700 rounded-3xl p-8 text-white mb-12">
            <h2 class="text-3xl font-bold text-center mb-8">🎯 {ui['which_right']}</h2>
            <div class="grid md:grid-cols-2 gap-8">
                <div class="bg-white/10 rounded-2xl p-6"><h3 class="text-xl font-bold text-amber-400 mb-4">{ui['choose_if'].format(breed=comp['breed1'])}</h3><ul class="space-y-2 text-slate-200">{breed1_reasons}</ul></div>
                <div class="bg-white/10 rounded-2xl p-6"><h3 class="text-xl font-bold text-yellow-400 mb-4">{ui['choose_if'].format(breed=comp['breed2'])}</h3><ul class="space-y-2 text-slate-200">{breed2_reasons}</ul></div>
            </div>
            <div class="mt-8 bg-white/5 rounded-xl p-6 text-center"><h4 class="text-lg font-semibold text-sky-300 mb-2">{ui['bottom_line']}</h4><p class="text-slate-300">{comp['bottom_line']}</p></div>
        </div>
        <div class="mb-12"><h2 class="text-2xl font-bold mb-6">{ui['more_comparisons']}</h2><div class="grid md:grid-cols-3 gap-4">{related_html}</div></div>
        <div class="text-center"><a href="../" class="text-sky-700 font-semibold">{ui['back_to_compare']}</a></div>
    </main>
    <footer class="border-t border-slate-100 mt-16 py-8"><div class="max-w-6xl mx-auto px-4 text-center text-slate-600 text-sm"><p>© 2026 BreedFinder. {ui['helping_find']}</p></div></footer>
</body>
</html>'''


def main():
    output_dir = BASE_DIR / 'zh' / 'compare' / 'comparisons'
    output_dir.mkdir(parents=True, exist_ok=True)
    for comp_key, comp in COMPARISONS.items():
        html = generate_article(comp_key, comp)
        path = output_dir / f"{comp['slug']}.html"
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ {path.name}")
    print(f"\n✅ Generated 5 fully translated Chinese comparison articles")

if __name__ == '__main__':
    main()
