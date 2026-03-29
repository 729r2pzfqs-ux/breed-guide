#!/usr/bin/env python3
"""Generate breed comparison pages for top 80 breeds × all pairs"""
import json, os, re

with open("data/breeds.json") as f:
    breeds_raw = json.load(f)

breed_map = {}
if isinstance(breeds_raw, dict):
    breed_map = breeds_raw
elif isinstance(breeds_raw, list):
    for b in breeds_raw:
        breed_map[b["id"]] = b

TOP_SLUGS = [
    "labrador-retriever", "french-bulldog", "golden-retriever", "german-shepherd",
    "poodle", "bulldog", "rottweiler", "beagle", "dachshund", "german-shorthaired-pointer",
    "pembroke-welsh-corgi", "australian-shepherd", "yorkshire-terrier", "cavalier-king-charles-spaniel",
    "doberman-pinscher", "boxer", "miniature-schnauzer", "cane-corso", "great-dane", "shih-tzu",
    "siberian-husky", "bernese-mountain-dog", "pomeranian", "boston-terrier", "havanese",
    "english-springer-spaniel", "brittany", "shetland-sheepdog", "cocker-spaniel", "border-collie",
    "vizsla", "belgian-malinois", "maltese", "weimaraner", "chihuahua",
    "rhodesian-ridgeback", "west-highland-white-terrier", "bichon-frise", "bloodhound", "akita",
    "portuguese-water-dog", "dalmatian", "papillon", "australian-cattle-dog",
    "bullmastiff", "samoyed", "scottish-terrier", "whippet", "collie",
    "basset-hound", "newfoundland", "russell-terrier", "chesapeake-bay-retriever", "shiba-inu",
    "airedale-terrier", "irish-setter", "alaskan-malamute", "english-cocker-spaniel",
    "staffordshire-bull-terrier", "american-staffordshire-terrier", "great-pyrenees", "miniature-pinscher",
    "italian-greyhound", "cairn-terrier", "old-english-sheepdog",
    "chow-chow", "belgian-tervuren", "greyhound", "norwegian-elkhound",
    "keeshond", "soft-coated-wheaten-terrier", "flat-coated-retriever", "leonberger",
    "lhasa-apso", "cardigan-welsh-corgi", "irish-wolfhound", "wirehaired-pointing-griffon"
]

valid = [s for s in TOP_SLUGS if s in breed_map]

# Get existing
existing = set()
for d in os.listdir("compare/comparisons"):
    if os.path.isdir(f"compare/comparisons/{d}"):
        existing.add(d)

def rating_to_label(val):
    if val <= 1: return "Very Low"
    if val <= 2: return "Low"
    if val <= 3: return "Moderate"
    if val <= 4: return "High"
    return "Very High"

def rating_to_color(label):
    if label in ("Very Low", "Low", "Minimal"): return "text-emerald-600"
    if label in ("Moderate", "Medium"): return "text-amber-500"
    return "text-rose-500"

def stars(val, max_val=5):
    filled = int(val)
    empty = max_val - filled
    return "★" * filled + "☆" * empty

def make_slug(a_id, b_id):
    a_name = breed_map[a_id]["name"]
    b_name = breed_map[b_id]["name"]
    # Short names for URL
    a_short = a_id
    b_short = b_id
    return f"{a_short}-vs-{b_short}"

def generate_page(a_id, b_id):
    a = breed_map[a_id]
    b = breed_map[b_id]
    slug = make_slug(a_id, b_id)
    
    a_name = a["name"]
    b_name = b["name"]
    a_r = a.get("ratings", {})
    b_r = b.get("ratings", {})
    
    # Comparison rows
    rows_data = [
        ("Size", a.get("size",{}).get("category","").title(), b.get("size",{}).get("category","").title()),
        ("Lifespan", a.get("lifespan",""), b.get("lifespan","")),
        ("Energy Level", rating_to_label(a_r.get("energy",3)), rating_to_label(b_r.get("energy",3))),
        ("Grooming Needs", rating_to_label(a_r.get("grooming",3)), rating_to_label(b_r.get("grooming",3))),
        ("Trainability", rating_to_label(a_r.get("trainability",3)), rating_to_label(b_r.get("trainability",3))),
        ("Kid-Friendly", rating_to_label(a_r.get("kid_friendly",3)), rating_to_label(b_r.get("kid_friendly",3))),
        ("Apartment Suitable", rating_to_label(a_r.get("apartment_ok",3)), rating_to_label(b_r.get("apartment_ok",3))),
        ("Sociability", rating_to_label(a_r.get("sociability",3)), rating_to_label(b_r.get("sociability",3))),
        ("Barking Level", rating_to_label(a_r.get("barking",3)), rating_to_label(b_r.get("barking",3))),
    ]
    
    # Build table rows with star ratings
    table_rows = ""
    rating_traits = {"Energy Level", "Grooming Needs", "Trainability", "Kid-Friendly", "Apartment Suitable", "Sociability", "Barking Level"}
    
    for i, (label, a_val, b_val) in enumerate(rows_data):
        bg = ' class="bg-slate-50/50"' if i % 2 == 0 else ""
        
        if label in rating_traits:
            # Get numeric rating for stars
            trait_key_map = {"Energy Level": "energy", "Grooming Needs": "grooming", "Trainability": "trainability", 
                           "Kid-Friendly": "kid_friendly", "Apartment Suitable": "apartment_ok", "Sociability": "sociability", "Barking Level": "barking"}
            key = trait_key_map.get(label, "")
            a_num = a_r.get(key, 3)
            b_num = b_r.get(key, 3)
            a_stars_str = stars(a_num)
            b_stars_str = stars(b_num)
            
            a_cell = f'''<td class="p-4 text-center">
<div class="flex justify-center gap-1"><span class="text-blue-500">{a_stars_str}</span></div>
<span class="text-sm text-slate-600">{a_val}</span></td>'''
            b_cell = f'''<td class="p-4 text-center">
<div class="flex justify-center gap-1"><span class="text-rose-500">{b_stars_str}</span></div>
<span class="text-sm text-slate-600">{b_val}</span></td>'''
        else:
            a_cell = f'<td class="p-4 text-center font-semibold">{a_val}</td>'
            b_cell = f'<td class="p-4 text-center font-semibold">{b_val}</td>'
        
        table_rows += f'<tr{bg}><td class="p-4 font-medium text-slate-700">{label}</td>{a_cell}{b_cell}</tr>\n'
    
    # Description (can be dict or string)
    a_desc_raw = a.get("description", {})
    b_desc_raw = b.get("description", {})
    a_desc = a_desc_raw.get("overview", "") if isinstance(a_desc_raw, dict) else str(a_desc_raw)
    b_desc = b_desc_raw.get("overview", "") if isinstance(b_desc_raw, dict) else str(b_desc_raw)
    if not a_desc: a_desc = f"The {a_name} is a {a.get('size',{}).get('category','medium')}-sized breed."
    if not b_desc: b_desc = f"The {b_name} is a {b.get('size',{}).get('category','medium')}-sized breed."
    
    # Taglines
    a_tag = a.get("tagline", "")
    b_tag = b.get("tagline", "")
    
    # Temperament
    a_temp = ", ".join(a.get("temperament", [])[:4]) if a.get("temperament") else "Loyal, Friendly"
    b_temp = ", ".join(b.get("temperament", [])[:4]) if b.get("temperament") else "Loyal, Friendly"
    
    # Analysis
    a_energy = rating_to_label(a_r.get("energy",3))
    b_energy = rating_to_label(b_r.get("energy",3))
    analysis = f"When comparing the {a_name} and {b_name}, both breeds bring unique qualities to the table. "
    analysis += f"The {a_name} is a {a.get('size',{}).get('category','medium')}-sized breed from {a.get('origin','unknown origin')} with a lifespan of {a.get('lifespan','10-12 years')}. "
    analysis += f"The {b_name} hails from {b.get('origin','unknown origin')} and typically lives {b.get('lifespan','10-12 years')}. "
    if a_r.get("energy",3) != b_r.get("energy",3):
        analysis += f"Energy-wise, the {a_name} is {a_energy.lower()} while the {b_name} is {b_energy.lower()}, which may influence your choice depending on your activity level. "
    analysis += f"Both breeds have their own grooming and training requirements — check the detailed comparison above to see which fits your lifestyle best."
    
    # FAQs
    faqs = [
        (f"What is the main difference between a {a_name} and a {b_name}?",
         f"The {a_name} is a {a.get('size',{}).get('category','medium')}-sized breed with {a_energy.lower()} energy, while the {b_name} is {b.get('size',{}).get('category','medium')}-sized with {b_energy.lower()} energy. They also differ in grooming needs, trainability, and temperament."),
        (f"Which is better for families, {a_name} or {b_name}?",
         f"The {a_name} has a kid-friendliness rating of {a_r.get('kid_friendly',3)}/5 while the {b_name} scores {b_r.get('kid_friendly',3)}/5. Both can be great family dogs with proper training and socialization."),
        (f"Which breed is easier to train?",
         f"The {a_name} has a trainability rating of {a_r.get('trainability',3)}/5 and the {b_name} scores {b_r.get('trainability',3)}/5. {'The ' + (a_name if a_r.get('trainability',3) > b_r.get('trainability',3) else b_name) + ' is generally easier to train.' if a_r.get('trainability',3) != b_r.get('trainability',3) else 'Both breeds have similar trainability.'}"),
        (f"Do {a_name}s or {b_name}s need more exercise?",
         f"The {a_name} has {a_energy.lower()} energy needs while the {b_name} has {b_energy.lower()} energy needs. {'Both need similar exercise.' if a_energy == b_energy else 'The ' + (a_name if a_r.get('energy',3) > b_r.get('energy',3) else b_name) + ' generally needs more exercise.'}"),
        (f"How long do {a_name}s and {b_name}s live?",
         f"The {a_name} typically lives {a.get('lifespan','10-12 years')}, while the {b_name} has an average lifespan of {b.get('lifespan','10-12 years')}."),
    ]
    
    faq_html = ""
    for q, ans in faqs:
        faq_html += f'''<details class="border-b border-slate-200 last:border-0">
<summary class="p-4 cursor-pointer font-medium text-slate-800 hover:text-emerald-700">{q}</summary>
<p class="px-4 pb-4 text-slate-600 text-sm leading-relaxed">{ans}</p>
</details>\n'''
    
    faq_schema = json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]
    })
    
    article_schema = json.dumps({
        "@context": "https://schema.org", "@type": "Article",
        "headline": f"{a_name} vs {b_name}: Complete Comparison",
        "author": {"@type": "Organization", "name": "BreedFinder"},
        "publisher": {"@type": "Organization", "name": "BreedFinder", "logo": {"@type": "ImageObject", "url": "https://breedfinder.org/logo-192.png"}},
        "dateModified": "2026-03-29"
    })
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-VEERQZ53LZ"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag("js",new Date());gtag("config","G-VEERQZ53LZ");</script>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{a_name} vs {b_name}: Complete Comparison | BreedFinder</title>
<meta name="description" content="{a_name} vs {b_name} comparison. Size, temperament, exercise, grooming, and family friendliness side by side. Find which breed is right for you.">
<link rel="canonical" href="/compare/comparisons/{slug}/">
<link rel="icon" href="/favicon.ico"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:title" content="{a_name} vs {b_name}: Complete Comparison">
<meta property="og:description" content="Compare {a_name} and {b_name} side by side.">
<meta property="og:url" content="https://breedfinder.org/compare/comparisons/{slug}/">
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@400;600;700&family=Inter:wght@400;500;600;700" rel="stylesheet">
<style>*{{font-family:'Inter',sans-serif}}</style>
<script type="application/ld+json">{article_schema}</script>
<script type="application/ld+json">{faq_schema}</script>
</head>
<body class="min-h-screen text-slate-800" style="background:linear-gradient(135deg,#f6f7f2 0%,#fff 50%,#eef1e8 100%)">
<header class="bg-white/80 backdrop-blur-md border-b border-slate-200/60 sticky top-0 z-50">
<div class="max-w-5xl mx-auto px-4 py-4 flex items-center justify-between">
<a href="/" class="flex items-center gap-3"><img src="/logo-192-green.png" alt="BreedFinder" class="h-10 w-10"><span class="text-xl font-bold">BreedFinder</span></a>
<nav class="flex items-center gap-3 sm:gap-6 text-sm font-medium">
<a href="/breeds/" class="hidden sm:block text-slate-600 hover:text-emerald-800">Breeds</a>
<a href="/compare/" class="text-slate-600 hover:text-emerald-800">Compare</a>
<a href="/quiz/" class="bg-emerald-600 text-white px-4 py-2 rounded-full hover:bg-emerald-700">Quiz</a>
</nav></div></header>

<main class="max-w-5xl mx-auto px-4 py-8">
<div class="text-sm text-slate-500 mb-4"><a href="/" class="hover:text-emerald-700">Home</a> > <a href="/compare/" class="hover:text-emerald-700">Compare</a> > {a_name} vs {b_name}</div>
<h1 class="text-3xl font-bold text-center mb-8" style="font-family:'Fraunces',serif">{a_name} vs {b_name}</h1>

<div class="grid md:grid-cols-2 gap-6 mb-8">
<div class="bg-white rounded-2xl shadow-lg overflow-hidden">
<div class="bg-gradient-to-r from-blue-500 to-blue-600 p-6 text-white text-center">
<img src="/images/heads/{a_id}.webp" alt="{a_name}" class="w-28 h-28 rounded-full mx-auto mb-3 object-cover border-4 border-white/30" onerror="this.style.display='none'">
<h2 class="text-xl font-bold">{a_name}</h2>
<p class="text-white/80 text-sm mt-1">{a_tag}</p></div>
<div class="p-5"><p class="text-slate-600 text-sm">{a_desc[:200] if len(a_desc) > 200 else a_desc}</p>
<div class="mt-3 flex flex-wrap gap-1">{" ".join(f'<span class="bg-blue-50 text-blue-700 px-2 py-0.5 rounded-full text-xs">{t}</span>' for t in a.get("temperament",[])[:4])}</div>
<a href="/breeds/{a_id}/" class="block mt-4 text-center text-blue-600 text-sm font-medium hover:underline">View Full Profile →</a></div></div>

<div class="bg-white rounded-2xl shadow-lg overflow-hidden">
<div class="bg-gradient-to-r from-rose-500 to-rose-600 p-6 text-white text-center">
<img src="/images/heads/{b_id}.webp" alt="{b_name}" class="w-28 h-28 rounded-full mx-auto mb-3 object-cover border-4 border-white/30" onerror="this.style.display='none'">
<h2 class="text-xl font-bold">{b_name}</h2>
<p class="text-white/80 text-sm mt-1">{b_tag}</p></div>
<div class="p-5"><p class="text-slate-600 text-sm">{b_desc[:200] if len(b_desc) > 200 else b_desc}</p>
<div class="mt-3 flex flex-wrap gap-1">{" ".join(f'<span class="bg-rose-50 text-rose-700 px-2 py-0.5 rounded-full text-xs">{t}</span>' for t in b.get("temperament",[])[:4])}</div>
<a href="/breeds/{b_id}/" class="block mt-4 text-center text-rose-600 text-sm font-medium hover:underline">View Full Profile →</a></div></div>
</div>

<div class="bg-white rounded-2xl shadow-lg overflow-hidden mb-8">
<div class="bg-gradient-to-r from-slate-800 to-slate-700 p-5 text-white"><h2 class="text-xl font-bold text-center">Side-by-Side Comparison</h2></div>
<table class="w-full text-sm">
<thead><tr class="bg-slate-100"><th class="p-3 text-left text-slate-600 font-medium">Trait</th><th class="p-3 text-center text-blue-600 font-bold">{a_name}</th><th class="p-3 text-center text-rose-600 font-bold">{b_name}</th></tr></thead>
<tbody>{table_rows}</tbody></table></div>

<div class="bg-white rounded-2xl shadow-lg p-6 mb-8">
<h2 class="text-xl font-bold mb-3">Detailed Analysis</h2>
<p class="text-slate-600 leading-relaxed">{analysis}</p></div>

<div class="bg-white rounded-2xl shadow-lg p-6 mb-8">
<h2 class="text-xl font-bold mb-3">Which Is Right For You?</h2>
<div class="grid md:grid-cols-2 gap-4">
<div class="bg-blue-50 rounded-xl p-4"><h3 class="font-bold text-blue-700 mb-2">Choose {a_name} if...</h3>
<ul class="text-sm text-slate-600 space-y-1"><li>You want a {a.get('size',{}).get('category','medium')}-sized {a.get('group','companion')} breed</li>
<li>You can provide {a_energy.lower()} levels of exercise</li>
<li>You're looking for a {a_temp.lower().split(',')[0].strip()} companion</li></ul></div>
<div class="bg-rose-50 rounded-xl p-4"><h3 class="font-bold text-rose-700 mb-2">Choose {b_name} if...</h3>
<ul class="text-sm text-slate-600 space-y-1"><li>You want a {b.get('size',{}).get('category','medium')}-sized {b.get('group','companion')} breed</li>
<li>You can provide {b_energy.lower()} levels of exercise</li>
<li>You're looking for a {b_temp.lower().split(',')[0].strip()} companion</li></ul></div></div></div>

<div class="bg-white rounded-2xl shadow-lg overflow-hidden mb-8">
<h2 class="text-xl font-bold p-6 pb-0">Frequently Asked Questions</h2>
<div class="p-6 pt-3">{faq_html}</div></div>

</main>
<footer class="border-t border-slate-200 py-6 text-center text-sm text-slate-500">
<p>© 2026 BreedFinder.org — <a href="/" class="hover:text-emerald-700">Home</a> · <a href="/breeds/" class="hover:text-emerald-700">Breeds</a> · <a href="/compare/" class="hover:text-emerald-700">Compare</a></p>
</footer></body></html>'''
    
    return slug, html

# Generate all pairs
count = 0
for i, a_id in enumerate(valid):
    for j in range(i + 1, len(valid)):
        b_id = valid[j]
        slug = make_slug(a_id, b_id)
        rev_slug = make_slug(b_id, a_id)
        
        if slug in existing or rev_slug in existing:
            continue
        
        slug, html = generate_page(a_id, b_id)
        out_dir = f"compare/comparisons/{slug}"
        os.makedirs(out_dir, exist_ok=True)
        with open(f"{out_dir}/index.html", "w") as f:
            f.write(html)
        existing.add(slug)
        count += 1
        
    if (i + 1) % 10 == 0:
        print(f"  ... breed {i+1}/{len(valid)}, {count} pages created")

print(f"\n✅ Created {count} new comparison pages")
print(f"Total comparisons: {len(existing)}")

# Update sitemap
with open("sitemap.xml", "r") as f:
    sitemap = f.read()

new_urls = ""
for d in sorted(existing):
    url = f"https://breedfinder.org/compare/comparisons/{d}/"
    if url not in sitemap:
        new_urls += f'  <url><loc>{url}</loc><priority>0.6</priority></url>\n'

if new_urls:
    sitemap = sitemap.replace("</urlset>", new_urls + "</urlset>")
    with open("sitemap.xml", "w") as f:
        f.write(sitemap)
    print(f"✅ Sitemap updated")
