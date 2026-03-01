#!/usr/bin/env python3
"""Generate Turkish comparison articles with full translations."""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

TR_UI = {
    'all_breeds': 'Tüm Irklar',
    'compare': 'Karşılaştır',
    'take_quiz': 'Testi Çöz',
    'comparisons': 'Karşılaştırmalar',
    'side_by_side': 'Yan Yana Karşılaştırma',
    'attribute': 'Özellik',
    'size': 'Boyut',
    'lifespan': 'Yaşam Süresi',
    'energy_level': 'Enerji Seviyesi',
    'grooming_needs': 'Bakım İhtiyacı',
    'trainability': 'Eğitilebilirlik',
    'kid_friendly': 'Çocuklarla Uyumu',
    'apartment': 'Daireye Uygunluk',
    'shedding': 'Tüy Dökümü',
    'more_comparisons': 'Diğer Karşılaştırmalar',
    'back_to_compare': '← Karşılaştırmaya Dön',
    'view_profile': 'Tam profili gör →',
    'large': 'Büyük',
    'years': 'yıl',
    'very_high': 'Çok Yüksek',
    'high': 'Yüksek',
    'moderate': 'Orta',
    'excellent': 'Mükemmel',
    'not_ideal': 'Uygun Değil',
    'heavy': 'Yoğun',
    'helping_find': 'Mükemmel dostunuzu bulmanıza yardımcı oluyoruz.',
    'temperament': 'Mizaç',
    'exercise_needs': 'Egzersiz İhtiyacı',
    'grooming_req': 'Bakım Gereksinimleri',
    'which_right': 'Hangisi Size Uygun?',
    'choose_if': '{breed} seçin eğer...',
    'bottom_line': 'Sonuç',
}

TR_TRAITS = {
    'Friendly': 'Dost Canlısı', 'Outgoing': 'Sosyal', 'Active': 'Aktif', 'Gentle': 'Nazik',
    'Intelligent': 'Zeki', 'Trusting': 'Güvenilir', 'Devoted': 'Sadık',
    'Reliable': 'Güvenilir', 'Trustworthy': 'Sadık', 'Kind': 'İyi Kalpli',
    'Playful': 'Oyuncu', 'Adaptable': 'Uyumlu', 'Smart': 'Akıllı',
    'Affectionate': 'Sevecen', 'Patient': 'Sabırlı', 'Alert': 'Uyanık',
    'Bright': 'Zeki', 'Amusing': 'Eğlenceli', 'Lively': 'Canlı',
    'Confident': 'Özgüvenli', 'Courageous': 'Cesur', 'Loyal': 'Sadık',
    'Versatile': 'Çok Yönlü', 'Protective': 'Koruyucu', 'Hardworking': 'Çalışkan',
    'Intense': 'Yoğun', 'Mischievous': 'Yaramaz', 'Dignified': 'Onurlu',
    'Strong': 'Güçlü', 'Faithful': 'Vefalı', 'Trainable': 'Eğitilebilir', 'Proud': 'Gururlu',
}

COMPARISONS = {
    'labrador-vs-golden': {
        'slug': 'labrador-vs-golden-retriever',
        'breed1': 'Labrador Retriever',
        'breed2': 'Golden Retriever',
        'breed1_slug': 'labrador-retriever',
        'breed2_slug': 'golden-retriever',
        'title': 'Labrador vs Golden Retriever: Tam Karşılaştırma',
        'desc': 'Labrador vs Golden Retriever karşılaştırması. Boyut, mizaç, egzersiz ihtiyacı ve aile uyumunu görün.',
        'intro': 'Dünyanın en sevilen iki aile köpeği. Her ikisi de dost canlısı, zeki ve çocuklarla harika—ama hangisi size uygun?',
        'breed1_tagline': 'Dünyanın En Popüler Irkı',
        'breed2_tagline': 'Ailelerin Favorisi',
        'breed1_desc': 'Labrador Retriever dünyanın en popüler köpek ırkıdır. Dost canlısı, sosyal ve enerji ile sevgi dolu arkadaşlardır.',
        'breed2_desc': 'Golden Retriever en popüler ırklardan biridir. Dost canlısı ve hoşgörülü tutumları onları harika aile dostları yapar.',
        'breed1_traits': ['Friendly', 'Outgoing', 'Active', 'Gentle', 'Intelligent', 'Trusting'],
        'breed2_traits': ['Intelligent', 'Friendly', 'Devoted', 'Reliable', 'Trustworthy', 'Kind'],
        'breed1_temperament_desc': 'Labradorlar arkadaş canlılıklarıyla ünlüdür ve tüm aileyle bağ kurarlar. Komşularla ve diğer köpeklerle iyi geçinirler. Rahat kişiliklerine aldanmayın—çok fazla egzersiz ihtiyaçları var!',
        'breed2_temperament_desc': 'Golden Retrieverlar sosyal, güvenilir ve memnun etmeye heveslidir. Çocuklar ve diğer hayvanlarla harikadırlar. Sabırlı ve nazik yapıları onları mükemmel terapi köpeği yapar.',
        'breed1_exercise': 'Yüksek enerji, günde en az 1-2 saat aktif egzersiz gerektirir. Yüzmeyi, getir oyununu ve açık hava maceralarını severler.',
        'breed2_exercise': 'Yüksek enerji, ancak Labradorlardan biraz daha az yoğun. Günde en az 1 saat egzersiz. Getirmede, yüzmede ve yürüyüşte mükemmeldir.',
        'breed1_grooming': 'Haftalık fırçalama, tüy dökümü döneminde daha fazla. Kısa, yoğun tüy bakımı nispeten kolay ama çok döker.',
        'breed2_grooming': 'Tüy dökümü döneminde günlük fırçalama önerilir. Uzun tüy, düğümleri önlemek için daha fazla dikkat gerektirir.',
        'breed1_reasons': ['En yüksek enerji seviyesini istiyorsunuz', 'Biraz daha az bakım tercih ediyorsunuz', 'Çok yönlü bir spor köpeği istiyorsunuz', 'Sosyal, coşkulu bir kişiliği seviyorsunuz', 'Renk çeşitliliği önemli (siyah, sarı, çikolata)'],
        'breed2_reasons': ['Biraz daha sakin bir mizaç tercih ediyorsunuz', 'Akıcı altın rengi tüyü seviyorsunuz', 'Mükemmel bir terapi/hizmet köpeği istiyorsunuz', 'Nazik, sabırlı bir yapıyı takdir ediyorsunuz', 'Daha sık fırçalamayı umursamıyorsunuz'],
        'bottom_line': 'Her iki ırk da olağanüstü aile köpekleridir. Labradorlar biraz daha enerjik ve tüy bakımı daha kolaydır, Golden Retrieverlar ise nazik sabırları ve akıcı tüyleriyle bilinir. Hangisini seçerseniz seçin, yıllarca sevgi ve arkadaşlık kazanırsınız!'
    },
    'frenchie-vs-boston': {
        'slug': 'fransiz-bulldogu-vs-boston-terrier',
        'breed1': 'Fransız Bulldogu',
        'breed2': 'Boston Terrier',
        'breed1_slug': 'french-bulldog',
        'breed2_slug': 'boston-terrier',
        'title': 'Fransız Bulldogu vs Boston Terrier: Tam Karşılaştırma',
        'desc': 'Fransız Bulldogu vs Boston Terrier karşılaştırması. Kompakt dostlar karşılaştırılıyor.',
        'intro': 'Büyük kişiliklere sahip iki çekici, kompakt ırk. Her ikisi de daire yaşamı için mükemmel—ama hangisi yaşam tarzınıza uyuyor?',
        'breed1_tagline': 'Büyüleyici Fransız',
        'breed2_tagline': 'Amerikan Centilmeni',
        'breed1_desc': 'Fransız Bulldogu, yarasa kulakları ve sevecen doğasıyla bilinen, oyuncu kişiliğe sahip büyüleyici ve uyumlu bir ırktır.',
        'breed2_desc': 'Boston Terrier, "Amerikan Centilmeni" olarak bilinir, dost canlısı ve neşeli mizaca sahip canlı küçük bir köpektir.',
        'breed1_traits': ['Playful', 'Adaptable', 'Smart', 'Affectionate', 'Patient', 'Alert'],
        'breed2_traits': ['Friendly', 'Bright', 'Amusing', 'Gentle', 'Lively', 'Intelligent'],
        'breed1_temperament_desc': 'Fransız Bulldogları rahat ve uyumludur, şehir dairelerinde veya kırsal evlerde gelişirler. Oyuncu ama hiperaktif değillerdir, çeşitli yaşam tarzları için mükemmel arkadaş olurlar.',
        'breed2_temperament_desc': 'Boston Terrierlar canlı, çok zeki ve nazik bir yapıya sahiptir. Smokin benzeri işaretleri ve dost canlısı, eğlenceli kişilikleriyle bilinirler.',
        'breed1_exercise': 'Orta düzey egzersiz ihtiyacı—kısa yürüyüşler ve oyun seansları yeterlidir. Düz burun nedeniyle sıcak havada aşırı yorgunluktan kaçının.',
        'breed2_exercise': 'Orta enerji, günlük yürüyüş ve oyun gerektirir. Fransızlardan daha atletik ama yine de aşırı ısınmaya eğilimli.',
        'breed1_grooming': 'Minimal bakım—haftalık fırçalama. Enfeksiyonları önlemek için yüz kıvrımlarını düzenli olarak temizleyin.',
        'breed2_grooming': 'Düşük bakım—ara sıra fırçalama. Kısa tüyleri bakımı kolaydır.',
        'breed1_reasons': ['Daha sakin, rahat bir arkadaş istiyorsunuz', 'Daha sağlam bir yapıyı tercih ediyorsunuz', 'Dairede yaşıyorsunuz', 'Minimum egzersiz gereksinimi istiyorsunuz', 'Sevimli yarasa kulaklarını seviyorsunuz'],
        'breed2_reasons': ['Biraz daha aktif bir köpek istiyorsunuz', 'Smokin görünümünü tercih ediyorsunuz', 'Daha kolay eğitilebilir bir köpek istiyorsunuz', 'Daha atletik bir yapıyı seviyorsunuz', 'Daha uzun ömürlü bir ırk istiyorsunuz'],
        'bottom_line': 'Her ikisi de büyük kişiliklere sahip mükemmel daire köpekleridir. Fransızlar daha sakin ve rahat, Bostonlar ise biraz daha enerjik ve atletiktir. Her ikisi de kalbinizi çalacak!'
    },
    'gsd-vs-malinois': {
        'slug': 'alman-kurdu-vs-malinois',
        'breed1': 'Alman Kurdu',
        'breed2': 'Belçika Malinois',
        'breed1_slug': 'german-shepherd',
        'breed2_slug': 'belgian-malinois',
        'title': 'Alman Kurdu vs Belçika Malinois: Tam Karşılaştırma',
        'desc': 'Alman Kurdu vs Malinois karşılaştırması. İki mükemmel çalışma köpeği karşılaştırılıyor.',
        'intro': 'Dünyanın en yetenekli iki çalışma köpeği. Her ikisi de polis ve askeri işlerde mükemmeldir—ama önemli farklılıkları var.',
        'breed1_tagline': 'Çok Yönlü Koruyucu',
        'breed2_tagline': 'Elit Çalışma Köpeği',
        'breed1_desc': 'Alman Kurdu çok yönlü, zeki ve dünyanın en popüler çalışma ırklarından biridir.',
        'breed2_desc': 'Belçika Malinois, dünya genelinde polis ve ordunun tercih ettiği yoğun, yüksek performanslı bir çalışma köpeğidir.',
        'breed1_traits': ['Confident', 'Courageous', 'Smart', 'Loyal', 'Versatile', 'Protective'],
        'breed2_traits': ['Confident', 'Smart', 'Hardworking', 'Alert', 'Intense', 'Protective'],
        'breed1_temperament_desc': 'Alman Kurtları özgüvenli, cesur ve inanılmaz derecede çok yönlüdür. Aileyle derin bağlar kurarlar ve agresif olmadan doğal olarak koruyucudurlar.',
        'breed2_temperament_desc': 'Malinoislar sonsuz enerjiye sahip yoğun, kararlı çalışma köpekleridir. Bir göreve ihtiyaç duyarlar ve motivasyonlarını yönlendirebilen deneyimli sahiplerle gelişirler.',
        'breed1_exercise': 'Yüksek egzersiz ihtiyacı—günde en az 2 saat. Çeşitli köpek sporlarında, iz takibinde ve itaat eğitiminde mükemmeldir.',
        'breed2_exercise': 'Çok yüksek egzersiz ihtiyacı—günde 2+ saat yoğun aktivite. Fiziksel egzersiz kadar zihinsel uyarıma da ihtiyaç duyar.',
        'breed1_grooming': 'Orta düzey bakım—haftada 2-3 kez fırçalama. Mevsimsel yoğun tüy dökümü daha fazla dikkat gerektirir.',
        'breed2_grooming': 'Kolay bakım—haftalık fırçalama. Alman Kurdundan daha kısa tüy, ama mevsimsel olarak döker.',
        'breed1_reasons': ['Çok yönlü bir aile koruyucusu istiyorsunuz', 'Biraz daha sakin bir çalışma köpeği tercih ediyorsunuz', 'Çalışma ırkı konusunda ilk kez sahipseniz', 'Çocuklarla iyi olan bir köpek istiyorsunuz', 'Klasik görünümü tercih ediyorsunuz'],
        'breed2_reasons': ['Maksimum motivasyon ve yoğunluk istiyorsunuz', 'Deneyimli bir sahipsiniz', 'Elit spor/çalışma köpeği istiyorsunuz', 'Kapsamlı egzersiz sağlayabiliyorsunuz', 'Daha hafif, daha hızlı bir köpek istiyorsunuz'],
        'bottom_line': 'Her ikisi de olağanüstü çalışma köpekleridir, ancak Malinoislar daha yoğundur ve deneyimli sahipler gerektirir. Alman Kurtları daha çok yönlüdür ve aileler için daha uygundur. Deneyim seviyenize ve yaşam tarzınıza göre seçin.'
    },
    'husky-vs-malamute': {
        'slug': 'husky-vs-malamute',
        'breed1': 'Sibirya Husky',
        'breed2': 'Alaska Malamute',
        'breed1_slug': 'siberian-husky',
        'breed2_slug': 'alaskan-malamute',
        'title': 'Sibirya Husky vs Alaska Malamute: Tam Karşılaştırma',
        'desc': 'Husky vs Malamute karşılaştırması. Arktik ırklar yan yana karşılaştırılıyor.',
        'intro': 'Kurt görünümlü iki görkemli arktik ırk. Benzer görünürler ama boyut ve mizaçta önemli farklılıkları var.',
        'breed1_tagline': 'Hızlı Kızak Köpeği',
        'breed2_tagline': 'Güçlü Çekici',
        'breed1_desc': 'Sibirya Husky, mavi gözleri ve dost canlısı kişiliğiyle bilinen atletik, dayanıklı bir kızak köpeğidir.',
        'breed2_desc': 'Alaska Malamute, güç ve dayanıklılık için yetiştirilmiş güçlü, sağlam bir kızak köpeğidir.',
        'breed1_traits': ['Outgoing', 'Mischievous', 'Loyal', 'Friendly', 'Alert', 'Gentle'],
        'breed2_traits': ['Affectionate', 'Loyal', 'Playful', 'Dignified', 'Devoted', 'Strong'],
        'breed1_temperament_desc': 'Huskiler dost canlısı, sosyal ve bazen yaramazdır. Arkadaşlık seven sürü köpekleridir ve sesli yapıları ile kaçma yetenekleriyle bilinirler.',
        'breed2_temperament_desc': 'Malamuteler Huskylerden daha onurlu ve daha az yaramazdır. Aileye derinden sadık ve sevecendirler ama daha bağımsız olabilirler.',
        'breed1_exercise': 'Çok yüksek enerji—kilometrelerce koşmak için tasarlanmış. Günde en az 2 saat aktif egzersiz. Koşmayı ve çekme aktivitelerini severler.',
        'breed2_exercise': 'Yüksek enerji, ama hızdan çok dayanıklılık. Uzun yürüyüşler ve çekme işi uygundur. Sıcak iklimlerde aşırı ısınabilirler.',
        'breed1_grooming': 'Kapsamlı bakım—haftada birkaç kez fırçalama. Yılda iki kez yoğun tüy dökümü ("tüy üfleme").',
        'breed2_grooming': 'Husky gibi kapsamlı bakım. Daha kalın tüyleri düğümleri önlemek için düzenli fırçalama gerektirir.',
        'breed1_reasons': ['Orta boy arktik ırk istiyorsunuz', 'Daha hızlı, daha atletik bir köpek tercih ediyorsunuz', 'Konuşkan, sesli bir arkadaş seviyorsunuz', 'Etkileyici mavi gözler istiyorsunuz', 'Daha oyuncu bir kişiliği seviyorsunuz'],
        'breed2_reasons': ['Daha büyük, daha güçlü bir köpek istiyorsunuz', 'Daha sakin, daha onurlu bir mizaç tercih ediyorsunuz', 'Güçlü ırklarla deneyiminiz var', 'Daha sessiz bir köpek istiyorsunuz (daha az uluma)', 'Çekme/kızak işi için köpeğe ihtiyacınız var'],
        'bottom_line': 'Huskyler koşmayı ve "konuşmayı" seven orta boy atletlerdir. Malamuteler güç için yapılmış güçlü devlerdir. Her ikisi de çok döker ve bol egzersiz gerektirir. Boyut tercihine ve istenen mizaca göre seçin.'
    },
    'poodle-vs-labrador': {
        'slug': 'kaniş-vs-labrador',
        'breed1': 'Kaniş',
        'breed2': 'Labrador Retriever',
        'breed1_slug': 'poodle',
        'breed2_slug': 'labrador-retriever',
        'title': 'Kaniş vs Labrador Retriever: Tam Karşılaştırma',
        'desc': 'Kaniş vs Labrador karşılaştırması. İki zeki ve popüler ırk karşılaştırılıyor.',
        'intro': 'En zeki ve popüler iki köpek ırkı. Her ikisi de mükemmel aile köpekleri, çok farklı tüyleri var.',
        'breed1_tagline': 'Zarif Atlet',
        'breed2_tagline': 'Herkesin En İyi Arkadaşı',
        'breed1_desc': 'Kaniş olağanüstü zeki ve aktiftir. Zarif görünümün arkasında atletik ve çok akıllı bir köpek var.',
        'breed2_desc': 'Labrador Retriever dünyanın en popüler ırkıdır, dost canlısı ve sosyal doğasıyla bilinir.',
        'breed1_traits': ['Intelligent', 'Active', 'Alert', 'Faithful', 'Trainable', 'Proud'],
        'breed2_traits': ['Friendly', 'Active', 'Outgoing', 'Gentle', 'Intelligent', 'Trusting'],
        'breed1_temperament_desc': 'Kanişler olağanüstü zeki ve memnun etmeye heveslidir. Şık kesimlerine aldanmayın—av ve getirme için yetiştirilmiş atletik köpeklerdir.',
        'breed2_temperament_desc': 'Labradorlar en arkadaş canlısı köpektir—herkesle sosyal, çocuklarla sabırlı ve memnun etmeye hevesli. Mükemmel aile arkadaşıdırlar.',
        'breed1_exercise': 'Yüksek enerji, günlük egzersiz ve zihinsel uyarı gerektirir. Çeviklik, itaat ve çeşitli köpek sporlarında mükemmeldir.',
        'breed2_exercise': 'Yüksek enerji—günde en az 1-2 saat. Yüzmeyi, getirmeyi ve insanlarıyla her aktiviteyi severler.',
        'breed1_grooming': 'Yüksek bakım—4-6 haftada bir profesyonel bakım. Günlük fırçalama düğümleri önler. Hipoalerjenik tüy.',
        'breed2_grooming': 'Kolay bakım, ama çok döker. Haftalık fırçalama, dökme mevsiminde daha fazla. Hipoalerjenik değil.',
        'breed1_reasons': ['Alerjiniz var (hipoalerjenik)', 'Minimum tüy dökümü istiyorsunuz', 'Bakımı seviyorsunuz veya maliyeti umursamıyorsunuz', 'Zarif bir görünüm istiyorsunuz', 'Boyut seçenekleri istiyorsunuz (oyuncak/minyatür/standart)'],
        'breed2_reasons': ['Kolay, ucuz bakımı tercih ediyorsunuz', 'Tüy dökümünü umursamıyorsunuz', 'Klasik aile köpeği istiyorsunuz', 'Daha gündelik bir görünümü tercih ediyorsunuz', 'Su seven bir retriever istiyorsunuz'],
        'bottom_line': 'Her ikisi de çok zeki ve eğitimi kolaydır. Kanişler hipoalerjenik tüy sunar ama daha fazla bakım gerektirir. Labradorların bakımı daha kolaydır ama çok dökerler. Her ikisi de mükemmel aile arkadaşlarıdır!'
    }
}


def generate_article(comp_key, comp):
    ui = TR_UI
    breed1_traits = [TR_TRAITS.get(t, t) for t in comp['breed1_traits']]
    breed2_traits = [TR_TRAITS.get(t, t) for t in comp['breed2_traits']]
    breed1_tags = '\n                    '.join([f'<span class="bg-amber-100 text-amber-700 px-3 py-1 rounded-full text-sm font-medium">{t}</span>' for t in breed1_traits])
    breed2_tags = '\n                    '.join([f'<span class="bg-yellow-100 text-yellow-700 px-3 py-1 rounded-full text-sm font-medium">{t}</span>' for t in breed2_traits])
    breed1_reasons = '\n                        '.join([f'<li class="flex items-start gap-2"><span class="text-green-400">✓</span><span>{r}</span></li>' for r in comp['breed1_reasons']])
    breed2_reasons = '\n                        '.join([f'<li class="flex items-start gap-2"><span class="text-green-400">✓</span><span>{r}</span></li>' for r in comp['breed2_reasons']])
    related = [(k, v) for k, v in COMPARISONS.items() if k != comp_key][:3]
    related_html = '\n'.join([f'<a href="{r[1]["slug"]}.html" class="bg-white p-4 rounded-xl shadow-sm hover:shadow-md transition"><span class="font-semibold">{r[1]["breed1"]} vs {r[1]["breed2"]}</span></a>' for r in related])
    
    return f'''<!DOCTYPE html>
<html lang="tr">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-VEERQZ53LZ"></script>
    <script>window.dataLayer = window.dataLayer || []; function gtag(){{dataLayer.push(arguments);}} gtag("js", new Date()); gtag("config", "G-VEERQZ53LZ");</script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{comp['title']} | BreedFinder</title>
    <meta name="description" content="{comp['desc']}">
    <link rel="canonical" href="https://breedfinder.org/tr/compare/comparisons/{comp['slug']}.html">
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
    output_dir = BASE_DIR / 'tr' / 'compare' / 'comparisons'
    output_dir.mkdir(parents=True, exist_ok=True)
    for comp_key, comp in COMPARISONS.items():
        html = generate_article(comp_key, comp)
        path = output_dir / f"{comp['slug']}.html"
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✅ {path.name}")
    print(f"\n✅ Generated 5 fully translated Turkish comparison articles")

if __name__ == '__main__':
    main()
