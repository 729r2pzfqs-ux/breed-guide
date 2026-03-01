#!/usr/bin/env python3
"""Generate Japanese comparison articles with full translations."""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

JA_UI = {
    'all_breeds': 'すべての犬種',
    'compare': '比較',
    'take_quiz': 'クイズを受ける',
    'comparisons': '比較記事',
    'side_by_side': '並べて比較',
    'attribute': '属性',
    'size': 'サイズ',
    'lifespan': '寿命',
    'energy_level': 'エネルギーレベル',
    'grooming_needs': 'グルーミングの必要性',
    'trainability': 'しつけのしやすさ',
    'kid_friendly': '子供との相性',
    'apartment': 'マンション向き',
    'shedding': '抜け毛',
    'more_comparisons': 'その他の比較',
    'back_to_compare': '← 比較に戻る',
    'view_profile': '詳細プロフィールを見る →',
    'large': '大型',
    'years': '年',
    'very_high': '非常に高い',
    'high': '高い',
    'moderate': '普通',
    'excellent': '優秀',
    'not_ideal': '不向き',
    'heavy': '多い',
    'helping_find': 'あなたにぴったりのパートナーを見つけるお手伝いをします。',
    'temperament': '性格',
    'exercise_needs': '運動の必要性',
    'grooming_req': 'グルーミング要件',
    'which_right': 'どちらがあなたに合っていますか？',
    'choose_if': '{breed}を選ぶなら...',
    'bottom_line': 'まとめ',
}

JA_TRAITS = {
    'Friendly': 'フレンドリー', 'Outgoing': '社交的', 'Active': '活発', 'Gentle': '穏やか',
    'Intelligent': '賢い', 'Trusting': '信頼性がある', 'Devoted': '献身的',
    'Reliable': '頼りになる', 'Trustworthy': '信用できる', 'Kind': '優しい',
    'Playful': '遊び好き', 'Adaptable': '適応力がある', 'Smart': '賢い',
    'Affectionate': '愛情深い', 'Patient': '忍耐強い', 'Alert': '警戒心がある',
    'Bright': '明るい', 'Amusing': '楽しい', 'Lively': '元気',
    'Confident': '自信がある', 'Courageous': '勇敢', 'Loyal': '忠実',
    'Versatile': '万能', 'Protective': '保護的', 'Hardworking': '勤勉',
    'Intense': '激しい', 'Mischievous': 'いたずら好き', 'Dignified': '威厳がある',
    'Strong': '力強い', 'Faithful': '誠実', 'Trainable': '訓練しやすい', 'Proud': '誇り高い',
}

COMPARISONS = {
    'labrador-vs-golden': {
        'slug': 'labrador-vs-golden-retriever',
        'breed1': 'ラブラドール・レトリバー',
        'breed2': 'ゴールデン・レトリバー',
        'breed1_slug': 'labrador-retriever',
        'breed2_slug': 'golden-retriever',
        'title': 'ラブラドール vs ゴールデン・レトリバー：徹底比較',
        'desc': 'ラブラドールとゴールデン・レトリバーの比較。サイズ、性格、運動量、家族との相性を見てみましょう。',
        'intro': '世界で最も愛されている家庭犬の2種類。どちらもフレンドリーで賢く、子供との相性も抜群ですが、どちらがあなたに合っているでしょうか？',
        'breed1_tagline': '世界一人気の犬種',
        'breed2_tagline': '家族のお気に入り',
        'breed1_desc': 'ラブラドール・レトリバーは世界で最も人気のある犬種です。フレンドリーで社交的、エネルギーと愛情にあふれた仲間です。',
        'breed2_desc': 'ゴールデン・レトリバーは最も人気のある犬種の一つです。友好的で寛容な性格で、素晴らしい家庭犬になります。',
        'breed1_traits': ['Friendly', 'Outgoing', 'Active', 'Gentle', 'Intelligent', 'Trusting'],
        'breed2_traits': ['Intelligent', 'Friendly', 'Devoted', 'Reliable', 'Trustworthy', 'Kind'],
        'breed1_temperament_desc': 'ラブラドールはその親しみやすさで有名で、家族全員と絆を深めます。近所の人や他の犬ともうまく付き合います。のんびりした性格に騙されないでください—たくさんの運動が必要です！',
        'breed2_temperament_desc': 'ゴールデン・レトリバーは社交的で信頼でき、喜ばせることに熱心です。子供や他の動物との相性も抜群です。忍耐強く穏やかな性格から、優れたセラピー犬になります。',
        'breed1_exercise': '高エネルギーで、毎日少なくとも1〜2時間の活発な運動が必要です。泳ぎ、ボール遊び、アウトドアの冒険が大好きです。',
        'breed2_exercise': '高エネルギーですが、ラブラドールより少し落ち着いています。毎日少なくとも1時間の運動が必要。取ってこい、水泳、ハイキングが得意です。',
        'breed1_grooming': '週に1回のブラッシング、換毛期はより頻繁に。短く密な被毛は比較的手入れが簡単ですが、抜け毛は多いです。',
        'breed2_grooming': '換毛期は毎日のブラッシングがおすすめ。長い被毛は毛玉を防ぐためにより注意が必要です。',
        'breed1_reasons': ['最高のエネルギーレベルが欲しい', 'グルーミングは少なめがいい', '万能なスポーツ犬が欲しい', '外向的で熱心な性格が好き', '色のバリエーションが大事（黒、黄、チョコレート）'],
        'breed2_reasons': ['少し落ち着いた性格が好み', '流れるような金色の被毛が好き', '優れたセラピー犬/介助犬が欲しい', '穏やかで忍耐強い性格を重視', '頻繁なブラッシングは気にならない'],
        'bottom_line': 'どちらも素晴らしい家庭犬です。ラブラドールは少しエネルギッシュで被毛の手入れが楽、ゴールデン・レトリバーは穏やかな忍耐強さと流れる被毛で知られています。どちらを選んでも、何年もの愛と友情をもたらしてくれます！'
    },
    'frenchie-vs-boston': {
        'slug': 'french-bulldog-vs-boston-terrier',
        'breed1': 'フレンチ・ブルドッグ',
        'breed2': 'ボストン・テリア',
        'breed1_slug': 'french-bulldog',
        'breed2_slug': 'boston-terrier',
        'title': 'フレンチ・ブルドッグ vs ボストン・テリア：徹底比較',
        'desc': 'フレンチ・ブルドッグとボストン・テリアの比較。コンパクトな仲間を比べてみましょう。',
        'intro': '大きな個性を持つ2つの魅力的でコンパクトな犬種。どちらもマンション生活に最適ですが、どちらがあなたのライフスタイルに合っているでしょうか？',
        'breed1_tagline': '魅力的なフランス犬',
        'breed2_tagline': 'アメリカの紳士',
        'breed1_desc': 'フレンチ・ブルドッグは魅力的で適応力のある犬種で、遊び心のある性格、コウモリ耳、愛情深い性格で知られています。',
        'breed2_desc': 'ボストン・テリアは「アメリカの紳士」として知られ、フレンドリーで陽気な性格の小型で活発な犬です。',
        'breed1_traits': ['Playful', 'Adaptable', 'Smart', 'Affectionate', 'Patient', 'Alert'],
        'breed2_traits': ['Friendly', 'Bright', 'Amusing', 'Gentle', 'Lively', 'Intelligent'],
        'breed1_temperament_desc': 'フレンチ・ブルドッグはのんびりして適応力があり、都会のマンションでも田舎の家でも元気に過ごします。遊び好きですが活発すぎず、様々なライフスタイルに合う素晴らしい仲間です。',
        'breed2_temperament_desc': 'ボストン・テリアは活発で非常に賢く、穏やかな性格を持っています。タキシードのような模様とフレンドリーで楽しい性格で知られています。',
        'breed1_exercise': '適度な運動で十分—短い散歩と遊びの時間で大丈夫です。平らな鼻のため、暑い天候での過度な運動は避けてください。',
        'breed2_exercise': '適度なエネルギーで、毎日の散歩と遊びが必要です。フレンチーより運動能力がありますが、やはり暑さに弱いです。',
        'breed1_grooming': '最小限のグルーミング—週1回のブラッシング。感染症を防ぐため、顔のしわを定期的に拭いてください。',
        'breed2_grooming': '手入れが簡単—時々ブラッシング。短い被毛は手入れが簡単です。',
        'breed1_reasons': ['より落ち着いたのんびりした仲間が欲しい', 'がっしりした体型が好み', 'マンションに住んでいる', '運動量は最小限がいい', '愛らしいコウモリ耳が好き'],
        'breed2_reasons': ['少し活発な犬が欲しい', 'タキシードルックが好き', 'しつけしやすい犬が欲しい', '運動能力のある体型が好み', '寿命が長い犬種がいい'],
        'bottom_line': 'どちらも大きな個性を持つ素晴らしいマンション犬です。フレンチーはより落ち着いてのんびり、ボストンは少しエネルギッシュで運動能力があります。どちらもあなたの心を奪うでしょう！'
    },
    'gsd-vs-malinois': {
        'slug': 'german-shepherd-vs-malinois',
        'breed1': 'ジャーマン・シェパード',
        'breed2': 'ベルジアン・マリノア',
        'breed1_slug': 'german-shepherd',
        'breed2_slug': 'belgian-malinois',
        'title': 'ジャーマン・シェパード vs ベルジアン・マリノア：徹底比較',
        'desc': 'ジャーマン・シェパードとマリノアの比較。2つの優れた作業犬を比べます。',
        'intro': '世界で最も優秀な作業犬の2種類。どちらも警察や軍で活躍していますが、重要な違いがあります。',
        'breed1_tagline': '万能な守護者',
        'breed2_tagline': 'エリート作業犬',
        'breed1_desc': 'ジャーマン・シェパードは万能で賢く、世界で最も人気のある作業犬種の一つです。',
        'breed2_desc': 'ベルジアン・マリノアは激しく高性能な作業犬で、世界中の警察や軍に好まれています。',
        'breed1_traits': ['Confident', 'Courageous', 'Smart', 'Loyal', 'Versatile', 'Protective'],
        'breed2_traits': ['Confident', 'Smart', 'Hardworking', 'Alert', 'Intense', 'Protective'],
        'breed1_temperament_desc': 'ジャーマン・シェパードは自信があり、勇敢で、非常に万能です。家族と深い絆を築き、攻撃的にならずに自然と保護的です。',
        'breed2_temperament_desc': 'マリノアは無限のエネルギーを持つ激しくやる気のある作業犬です。仕事が必要で、そのやる気を引き出せる経験豊富な飼い主のもとで活躍します。',
        'breed1_exercise': '高い運動ニーズ—毎日少なくとも2時間。様々な犬のスポーツ、追跡、服従訓練に優れています。',
        'breed2_exercise': '非常に高い運動ニーズ—毎日2時間以上の激しい活動。精神的刺激も身体運動と同じくらい必要です。',
        'breed1_grooming': '適度なグルーミング—週2〜3回ブラッシング。換毛期には重い抜け毛により注意が必要です。',
        'breed2_grooming': '手入れ簡単—週1回のブラッシング。ジャーマン・シェパードより被毛が短いですが、季節の換毛はあります。',
        'breed1_reasons': ['万能な家族の守護者が欲しい', '少し落ち着いた作業犬が好み', '作業犬種を初めて飼う', '子供に良い犬が欲しい', 'クラシックな外見が好き'],
        'breed2_reasons': ['最大のやる気と激しさが欲しい', '経験豊富な飼い主である', 'エリートスポーツ/作業犬が欲しい', '十分な運動を提供できる', 'より軽くて速い犬が欲しい'],
        'bottom_line': 'どちらも優れた作業犬ですが、マリノアはより激しく、経験豊富な飼い主が必要です。ジャーマン・シェパードはより万能で、家族向きです。経験レベルとライフスタイルに基づいて選んでください。'
    },
    'husky-vs-malamute': {
        'slug': 'husky-vs-malamute',
        'breed1': 'シベリアン・ハスキー',
        'breed2': 'アラスカン・マラミュート',
        'breed1_slug': 'siberian-husky',
        'breed2_slug': 'alaskan-malamute',
        'title': 'シベリアン・ハスキー vs アラスカン・マラミュート：徹底比較',
        'desc': 'ハスキーとマラミュートの比較。北極犬種を並べて比べます。',
        'intro': 'オオカミのような外見を持つ2つの雄大な北極犬種。似ていますが、サイズと性格に重要な違いがあります。',
        'breed1_tagline': '速い犬ぞり犬',
        'breed2_tagline': 'パワフルな運搬犬',
        'breed1_desc': 'シベリアン・ハスキーは運動能力と耐久性のある犬ぞり犬で、青い目とフレンドリーな性格で知られています。',
        'breed2_desc': 'アラスカン・マラミュートは力強く頑丈な犬ぞり犬で、力と持久力のために育てられました。',
        'breed1_traits': ['Outgoing', 'Mischievous', 'Loyal', 'Friendly', 'Alert', 'Gentle'],
        'breed2_traits': ['Affectionate', 'Loyal', 'Playful', 'Dignified', 'Devoted', 'Strong'],
        'breed1_temperament_desc': 'ハスキーはフレンドリーで社交的で、時にはいたずら好きです。仲間を愛する群れの犬で、よく吠えることと脱走の才能で知られています。',
        'breed2_temperament_desc': 'マラミュートはハスキーより威厳があり、いたずらは少ないです。非常に忠実で、家族に愛情深いですが、より独立心が強いこともあります。',
        'breed1_exercise': '非常に高いエネルギー—何キロも走るように設計されています。毎日少なくとも2時間の活発な運動が必要。走ることと引っ張る活動が大好きです。',
        'breed2_exercise': '高いエネルギーですが、速さより持久力。長いハイキングと引っ張り作業が適しています。暑い気候では過熱する可能性があります。',
        'breed1_grooming': '広範なグルーミング—週に数回ブラッシング。年2回の大量の換毛（「被毛を吹く」）があります。',
        'breed2_grooming': 'ハスキーと同様の広範なグルーミング。より厚い被毛は毛玉を防ぐために定期的なブラッシングが必要です。',
        'breed1_reasons': ['中型の北極犬種が欲しい', 'より速く運動能力のある犬が好み', 'おしゃべりで声を出す仲間が好き', '印象的な青い目が欲しい', 'より遊び好きな性格が好き'],
        'breed2_reasons': ['より大きく力強い犬が欲しい', 'より落ち着いた威厳のある性格が好み', '強い犬種の経験がある', 'より静かな犬が欲しい（遠吠えが少ない）', '引っ張り/運搬用の犬が必要'],
        'bottom_line': 'ハスキーは走ることと「話すこと」が大好きな中型アスリートです。マラミュートは力のために作られた力強い巨人です。どちらも抜け毛が多く、たくさんの運動が必要です。サイズの好みと望む性格に基づいて選んでください。'
    },
    'poodle-vs-labrador': {
        'slug': 'poodle-vs-labrador',
        'breed1': 'プードル',
        'breed2': 'ラブラドール・レトリバー',
        'breed1_slug': 'poodle',
        'breed2_slug': 'labrador-retriever',
        'title': 'プードル vs ラブラドール・レトリバー：徹底比較',
        'desc': 'プードルとラブラドールの比較。2つの賢く人気のある犬種を比べます。',
        'intro': '最も賢く人気のある犬種の2つ。どちらも素晴らしい家庭犬ですが、被毛が大きく異なります。',
        'breed1_tagline': 'エレガントなアスリート',
        'breed2_tagline': 'みんなの親友',
        'breed1_desc': 'プードルは非常に賢く活発です。エレガントな外見の裏には、運動能力があり非常に賢い犬がいます。',
        'breed2_desc': 'ラブラドール・レトリバーは世界で最も人気のある犬種で、フレンドリーで社交的な性格で知られています。',
        'breed1_traits': ['Intelligent', 'Active', 'Alert', 'Faithful', 'Trainable', 'Proud'],
        'breed2_traits': ['Friendly', 'Active', 'Outgoing', 'Gentle', 'Intelligent', 'Trusting'],
        'breed1_temperament_desc': 'プードルは非常に賢く、喜ばせることに熱心です。ファンシーなカットに騙されないでください—狩猟と回収のために育てられた運動能力のある犬です。',
        'breed2_temperament_desc': 'ラブラドールは究極のフレンドリー犬—誰にでも社交的で、子供に忍耐強く、喜ばせることに熱心です。究極の家族の仲間です。',
        'breed1_exercise': '高エネルギーで、毎日の運動と精神的刺激が必要。アジリティ、服従、様々な犬のスポーツに優れています。',
        'breed2_exercise': '高エネルギー—毎日少なくとも1〜2時間。泳ぎ、取ってこい、人間との活動が大好きです。',
        'breed1_grooming': '高メンテナンス—4〜6週間ごとにプロのグルーミング。毎日のブラッシングで毛玉を防ぎます。低アレルギー性の被毛。',
        'breed2_grooming': '手入れ簡単ですが、抜け毛が多いです。週1回のブラッシング、換毛期はより頻繁に。低アレルギー性ではありません。',
        'breed1_reasons': ['アレルギーがある（低アレルギー性）', '抜け毛を最小限にしたい', 'グルーミングが好きまたは費用は気にしない', 'エレガントな外見が欲しい', 'サイズのオプションが欲しい（トイ/ミニ/スタンダード）'],
        'breed2_reasons': ['簡単で安価なグルーミングが好み', '抜け毛は気にならない', 'クラシックな家庭犬が欲しい', 'よりカジュアルな外見が好み', '水が好きなレトリバーが欲しい'],
        'bottom_line': 'どちらも非常に賢くしつけが簡単です。プードルは低アレルギー性の被毛を提供しますが、グルーミングが必要です。ラブラドールは手入れが簡単ですが、抜け毛が多いです。どちらも素晴らしい家族の仲間です！'
    }
}


def generate_article(comp_key, comp):
    ui = JA_UI
    breed1_traits = [JA_TRAITS.get(t, t) for t in comp['breed1_traits']]
    breed2_traits = [JA_TRAITS.get(t, t) for t in comp['breed2_traits']]
    
    breed1_tags = '\n                    '.join([f'<span class="bg-amber-100 text-amber-700 px-3 py-1 rounded-full text-sm font-medium">{t}</span>' for t in breed1_traits])
    breed2_tags = '\n                    '.join([f'<span class="bg-yellow-100 text-yellow-700 px-3 py-1 rounded-full text-sm font-medium">{t}</span>' for t in breed2_traits])
    
    breed1_reasons = '\n                        '.join([f'<li class="flex items-start gap-2"><span class="text-green-400">✓</span><span>{r}</span></li>' for r in comp['breed1_reasons']])
    breed2_reasons = '\n                        '.join([f'<li class="flex items-start gap-2"><span class="text-green-400">✓</span><span>{r}</span></li>' for r in comp['breed2_reasons']])
    
    related = [(k, v) for k, v in COMPARISONS.items() if k != comp_key][:3]
    related_html = '\n'.join([f'<a href="{r[1]["slug"]}.html" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md transition"><span class="font-semibold">{r[1]["breed1"]} vs {r[1]["breed2"]}</span></a>' for r in related])
    
    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-VEERQZ53LZ"></script>
    <script>window.dataLayer = window.dataLayer || []; function gtag(){{dataLayer.push(arguments);}} gtag("js", new Date()); gtag("config", "G-VEERQZ53LZ");</script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{comp['title']} | BreedFinder</title>
    <meta name="description" content="{comp['desc']}">
    <link rel="canonical" href="https://breedfinder.org/ja/compare/comparisons/{comp['slug']}.html">
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
                <h3 class="text-xl font-bold text-amber-600 mb-4">🧠 {comp['breed1']}の{ui['temperament']}</h3>
                <div class="flex flex-wrap gap-2 mb-4">
                    {breed1_tags}
                </div>
                <p class="text-slate-600 text-sm">{comp['breed1_temperament_desc']}</p>
            </div>
            <div class="bg-white rounded-2xl p-6 shadow-lg">
                <h3 class="text-xl font-bold text-yellow-600 mb-4">🧠 {comp['breed2']}の{ui['temperament']}</h3>
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
    output_dir = BASE_DIR / 'ja' / 'compare' / 'comparisons'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for comp_key, comp in COMPARISONS.items():
        html = generate_article(comp_key, comp)
        path = output_dir / f"{comp['slug']}.html"
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ {path.name}")
    
    print(f"\n✅ Generated 5 fully translated Japanese comparison articles")


if __name__ == '__main__':
    main()
