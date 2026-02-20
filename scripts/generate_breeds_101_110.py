#!/usr/bin/env python3
"""Generate breed pages for breeds 101-110 (missing terriers)"""

import os

# Breed data for 101-110
BREEDS_101_110 = [
    {
        "id": "cairn-terrier", "name": "Cairn Terrier",
        "group": "terrier", "origin": "Scotland", "lifespan": "13-15 years",
        "size": {"height_cm": "23-33", "weight_kg": "6-8", "category": "small"},
        "ratings": {"size": 1, "energy": 4, "grooming": 2, "sociability": 4, "trainability": 3, "barking": 4, "kid_friendly": 4, "apartment_ok": 5},
        "characteristics": {"coat_type": "Double coat, shaggy outer", "coat_colors": ["cream", "wheaten", "red", "gray", "brindle"], "shedding": "low", "hypoallergenic": True},
        "temperament": ["cheerful", "alert", "busy", "hardy", "fearless"],
        "description": {
            "overview": "A small, hardy Scottish terrier made famous as Toto in The Wizard of Oz. Bred to hunt vermin among cairns (rock piles).",
            "temperament": "Cheerful and busy with typical terrier confidence. Alert, curious, and always ready for adventure.",
            "health": "Generally healthy. Watch for luxating patella, eye problems, and skin allergies.",
            "exercise": "Moderate exercise needs. Enjoys walks and play but adaptable to apartment life."
        },
        "verdict": {
            "best_for": ["Apartment dwellers", "Families with older children", "Active seniors", "Those wanting a spirited small dog"],
            "not_for": ["Homes with small pets", "Those wanting a calm lap dog", "Off-leash situations without training"],
            "summary": "The iconic Toto dog—cheerful, hardy, and full of terrier spirit in a small package."
        }
    },
    {
        "id": "norfolk-terrier", "name": "Norfolk Terrier",
        "group": "terrier", "origin": "England", "lifespan": "12-16 years",
        "size": {"height_cm": "23-25", "weight_kg": "5-6", "category": "small"},
        "ratings": {"size": 1, "energy": 4, "grooming": 2, "sociability": 4, "trainability": 3, "barking": 3, "kid_friendly": 4, "apartment_ok": 5},
        "characteristics": {"coat_type": "Hard, wiry, straight", "coat_colors": ["red", "wheaten", "black and tan", "grizzle"], "shedding": "low", "hypoallergenic": True},
        "temperament": ["fearless", "lovable", "alert", "gregarious", "spirited"],
        "description": {
            "overview": "One of the smallest working terriers, distinguished from the Norwich by its folded ears. Bred for ratting.",
            "temperament": "Fearless yet lovable, more gregarious than most terriers. Enjoys company of people and dogs.",
            "health": "Generally healthy. Watch for mitral valve disease, luxating patella, and hip dysplasia.",
            "exercise": "Moderate exercise needs. Enjoys walks and games but adapts well to various lifestyles."
        },
        "verdict": {
            "best_for": ["Apartment dwellers", "Families", "Those wanting a social terrier", "Active seniors"],
            "not_for": ["Homes with small pets", "Those wanting a guard dog", "Very sedentary owners"],
            "summary": "A lovable, social terrier that's more easygoing than most. Great apartment companion."
        }
    },
    {
        "id": "norwich-terrier", "name": "Norwich Terrier",
        "group": "terrier", "origin": "England", "lifespan": "12-15 years",
        "size": {"height_cm": "24-26", "weight_kg": "5-6", "category": "small"},
        "ratings": {"size": 1, "energy": 4, "grooming": 2, "sociability": 4, "trainability": 3, "barking": 3, "kid_friendly": 4, "apartment_ok": 5},
        "characteristics": {"coat_type": "Hard, wiry, straight", "coat_colors": ["red", "wheaten", "black and tan", "grizzle"], "shedding": "low", "hypoallergenic": True},
        "temperament": ["affectionate", "curious", "fearless", "happy", "spirited"],
        "description": {
            "overview": "Nearly identical to the Norfolk but with pricked ears. One of the smallest working terriers.",
            "temperament": "Affectionate and happy with fearless terrier spirit. Curious and eager to explore.",
            "health": "Generally healthy. Watch for breathing issues, epilepsy, and hip dysplasia.",
            "exercise": "Moderate exercise needs. Happy with daily walks and playtime."
        },
        "verdict": {
            "best_for": ["Apartment dwellers", "Families with children", "Those wanting a portable terrier", "Active seniors"],
            "not_for": ["Homes with small pets", "Those wanting a very quiet dog", "Sedentary owners"],
            "summary": "A happy, affectionate terrier with pricked ears. Perfect size for apartment living."
        }
    },
    {
        "id": "wire-fox-terrier", "name": "Wire Fox Terrier",
        "group": "terrier", "origin": "England", "lifespan": "12-15 years",
        "size": {"height_cm": "36-41", "weight_kg": "7-9", "category": "small"},
        "ratings": {"size": 2, "energy": 5, "grooming": 4, "sociability": 4, "trainability": 3, "barking": 4, "kid_friendly": 4, "apartment_ok": 3},
        "characteristics": {"coat_type": "Dense, wiry, twisted", "coat_colors": ["white with tan", "black markings"], "shedding": "low", "hypoallergenic": True},
        "temperament": ["alert", "quick", "keen", "friendly", "fearless"],
        "description": {
            "overview": "A classic English terrier bred for fox hunting, known for its distinctive wiry coat and keen expression.",
            "temperament": "Alert and quick with boundless energy. Friendly and confident but can be stubborn.",
            "health": "Generally healthy. Watch for luxating patella, eye problems, and skin issues.",
            "exercise": "High energy requiring plenty of daily exercise and mental stimulation."
        },
        "verdict": {
            "best_for": ["Active families", "Those wanting a show-quality terrier", "Experienced terrier owners", "Runners and hikers"],
            "not_for": ["Sedentary owners", "First-time dog owners", "Homes with small pets"],
            "summary": "A classic, elegant terrier with tons of energy. Needs experienced handling and lots of exercise."
        }
    },
    {
        "id": "smooth-fox-terrier", "name": "Smooth Fox Terrier",
        "group": "terrier", "origin": "England", "lifespan": "12-15 years",
        "size": {"height_cm": "36-41", "weight_kg": "7-9", "category": "small"},
        "ratings": {"size": 2, "energy": 5, "grooming": 1, "sociability": 4, "trainability": 3, "barking": 4, "kid_friendly": 4, "apartment_ok": 3},
        "characteristics": {"coat_type": "Smooth, flat, hard, dense", "coat_colors": ["white with tan", "black markings"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["alert", "lively", "keen", "friendly", "bold"],
        "description": {
            "overview": "The smooth-coated version of the Fox Terrier, equally energetic but with an easier-care coat.",
            "temperament": "Lively and bold with typical terrier confidence. Friendly but independent.",
            "health": "Generally healthy. Watch for deafness, luxating patella, and eye problems.",
            "exercise": "High energy requiring vigorous daily exercise and play."
        },
        "verdict": {
            "best_for": ["Active families", "Those wanting low-maintenance grooming", "Experienced terrier owners", "Active individuals"],
            "not_for": ["Sedentary owners", "Apartment living without exercise commitment", "Homes with small pets"],
            "summary": "All the Fox Terrier energy with an easier-care coat. Still needs lots of exercise."
        }
    },
    {
        "id": "lakeland-terrier", "name": "Lakeland Terrier",
        "group": "terrier", "origin": "England", "lifespan": "12-15 years",
        "size": {"height_cm": "33-38", "weight_kg": "7-8", "category": "small"},
        "ratings": {"size": 2, "energy": 4, "grooming": 3, "sociability": 3, "trainability": 3, "barking": 3, "kid_friendly": 4, "apartment_ok": 4},
        "characteristics": {"coat_type": "Dense, wiry, weather-resistant", "coat_colors": ["black and tan", "blue and tan", "red", "wheaten", "grizzle"], "shedding": "low", "hypoallergenic": True},
        "temperament": ["bold", "friendly", "confident", "zesty", "clever"],
        "description": {
            "overview": "A sturdy terrier from England's Lake District, bred to hunt foxes that preyed on sheep.",
            "temperament": "Bold and confident with a zesty personality. Friendly but has typical terrier independence.",
            "health": "Generally healthy breed with few genetic issues. Watch for eye problems.",
            "exercise": "Moderate to high exercise needs. Enjoys outdoor adventures and play."
        },
        "verdict": {
            "best_for": ["Active families", "Experienced terrier owners", "Those wanting a hypoallergenic dog", "Outdoor enthusiasts"],
            "not_for": ["First-time dog owners", "Homes with small pets", "Those wanting a calm dog"],
            "summary": "A bold, zesty terrier from the Lake District. Hardy and hypoallergenic with moderate exercise needs."
        }
    },
    {
        "id": "welsh-terrier", "name": "Welsh Terrier",
        "group": "terrier", "origin": "Wales", "lifespan": "12-15 years",
        "size": {"height_cm": "36-39", "weight_kg": "9-10", "category": "small"},
        "ratings": {"size": 2, "energy": 4, "grooming": 3, "sociability": 4, "trainability": 3, "barking": 3, "kid_friendly": 4, "apartment_ok": 3},
        "characteristics": {"coat_type": "Dense, hard, wiry", "coat_colors": ["black and tan"], "shedding": "low", "hypoallergenic": True},
        "temperament": ["friendly", "spirited", "alert", "intelligent", "game"],
        "description": {
            "overview": "One of the oldest terrier breeds, originally used for hunting badger, fox, and otter in Wales.",
            "temperament": "Friendly and spirited with a calmer disposition than many terriers. Intelligent and game.",
            "health": "Generally healthy. Watch for allergies, epilepsy, and eye problems.",
            "exercise": "Moderate to high exercise needs. Enjoys walks, play, and mental challenges."
        },
        "verdict": {
            "best_for": ["Active families", "Those wanting a calmer terrier", "Experienced dog owners", "Those wanting a hypoallergenic dog"],
            "not_for": ["Homes with small pets", "Very sedentary owners", "Those unwilling to groom regularly"],
            "summary": "A friendly Welsh terrier that's calmer than many. Great family dog with regular exercise."
        }
    },
    {
        "id": "skye-terrier", "name": "Skye Terrier",
        "group": "terrier", "origin": "Scotland", "lifespan": "12-14 years",
        "size": {"height_cm": "24-26", "weight_kg": "16-18", "category": "small"},
        "ratings": {"size": 2, "energy": 3, "grooming": 4, "sociability": 2, "trainability": 3, "barking": 3, "kid_friendly": 3, "apartment_ok": 4},
        "characteristics": {"coat_type": "Long, straight, flat", "coat_colors": ["black", "blue", "gray", "fawn", "cream"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["loyal", "dignified", "canny", "courageous", "good-tempered"],
        "description": {
            "overview": "An elegant Scottish terrier with a distinctive long coat, once a favorite of British royalty.",
            "temperament": "Loyal and dignified, more reserved than most terriers. Devoted to family but wary of strangers.",
            "health": "Prone to orthopedic issues due to long body. Watch for disc problems and premature closure of growth plates.",
            "exercise": "Moderate exercise needs. Avoid jumping and stairs as puppies to protect developing bones."
        },
        "verdict": {
            "best_for": ["Experienced dog owners", "Those wanting a loyal companion", "Quiet households", "Those committed to grooming"],
            "not_for": ["Families with young children", "Very social households", "Those wanting an easy-care coat"],
            "summary": "An elegant, loyal terrier that's more reserved than most. Needs careful exercise as puppies."
        }
    },
    {
        "id": "sealyham-terrier", "name": "Sealyham Terrier",
        "group": "terrier", "origin": "Wales", "lifespan": "12-14 years",
        "size": {"height_cm": "27-31", "weight_kg": "8-9", "category": "small"},
        "ratings": {"size": 2, "energy": 3, "grooming": 3, "sociability": 3, "trainability": 3, "barking": 3, "kid_friendly": 4, "apartment_ok": 4},
        "characteristics": {"coat_type": "Long, hard, wiry", "coat_colors": ["all white", "white with lemon", "tan", "badger markings"], "shedding": "low", "hypoallergenic": True},
        "temperament": ["outgoing", "friendly", "calm", "adaptable", "humorous"],
        "description": {
            "overview": "A rare Welsh terrier bred for hunting badger and otter, now prized as a charming companion.",
            "temperament": "More calm and adaptable than most terriers. Outgoing with a sense of humor.",
            "health": "Watch for eye problems (lens luxation, retinal dysplasia) and deafness. Generally healthy.",
            "exercise": "Moderate exercise needs. Enjoys walks but also happy to relax at home."
        },
        "verdict": {
            "best_for": ["Families", "Those wanting a calmer terrier", "Apartment dwellers", "Those interested in rare breeds"],
            "not_for": ["Those wanting a high-energy dog", "Homes with small pets", "Those unwilling to groom"],
            "summary": "A charming, calm terrier that's rarer than most. Great apartment companion with a sense of humor."
        }
    },
    {
        "id": "dandie-dinmont-terrier", "name": "Dandie Dinmont Terrier",
        "group": "terrier", "origin": "Scotland", "lifespan": "12-15 years",
        "size": {"height_cm": "20-28", "weight_kg": "8-11", "category": "small"},
        "ratings": {"size": 2, "energy": 3, "grooming": 3, "sociability": 3, "trainability": 3, "barking": 3, "kid_friendly": 4, "apartment_ok": 4},
        "characteristics": {"coat_type": "Crisp topcoat, soft undercoat", "coat_colors": ["pepper", "mustard"], "shedding": "low", "hypoallergenic": True},
        "temperament": ["independent", "determined", "dignified", "affectionate", "fun"],
        "description": {
            "overview": "A unique Scottish terrier named after a character in a Sir Walter Scott novel. Known for its distinctive silhouette.",
            "temperament": "Independent and dignified but affectionate with family. Calmer than many terriers but still determined.",
            "health": "Prone to back problems due to long body. Watch for intervertebral disc disease and glaucoma.",
            "exercise": "Moderate exercise needs. Avoid activities that strain the back."
        },
        "verdict": {
            "best_for": ["Experienced dog owners", "Those wanting a unique breed", "Quiet households", "Apartment dwellers"],
            "not_for": ["Those wanting a high-energy dog", "Families with rough-playing children", "Those wanting off-leash reliability"],
            "summary": "A unique, dignified terrier with a literary name. Calmer than most but needs back-care awareness."
        }
    },
]

# Page template
PAGE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="../favicon.ico" type="image/x-icon">
    <title>{name}: Breed Guide, Temperament & Care | BreedFinder</title>
    <meta name="description" content="Complete guide to the {name}: temperament, exercise needs, grooming, health issues, and whether this breed is right for you.">
    <link rel="canonical" href="https://breedfinder.org/breeds/{id}">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
        .rating-bar {{ background: #e2e8f0; position: relative; overflow: hidden; }}
        .rating-bar::after {{ content: ''; position: absolute; left: 0; top: 0; height: 100%; width: var(--rating); background: linear-gradient(90deg, #0ea5e9, #8b5cf6); border-radius: 9999px; }}
    </style>
</head>
<body class="bg-gradient-to-b from-slate-50 to-white min-h-screen text-slate-800">
    <header class="bg-white/80 backdrop-blur-md border-b border-slate-200/60 sticky top-0 z-50">
        <div class="max-w-5xl mx-auto px-4 py-4 flex items-center justify-between">
            <a href="../" class="flex items-center gap-3">
                <img src="../logo-192.png" class="w-10 h-10" alt="BreedFinder">
                <span class="text-xl font-bold">BreedFinder</span>
            </a>
            <nav class="flex items-center gap-6 text-sm font-medium">
                <a href="../quiz" class="text-slate-600 hover:text-sky-600">Breed Quiz</a>
            </nav>
        </div>
    </header>

    <main class="max-w-5xl mx-auto px-4 py-8">
        <nav class="text-sm text-slate-500 mb-6 flex items-center gap-2">
            <a href="../" class="hover:text-sky-600">Home</a>
            <i data-lucide="chevron-right" class="w-4 h-4"></i>
            <span class="text-slate-700 font-medium">{name}</span>
        </nav>

        <div class="bg-white rounded-3xl p-8 mb-8 shadow-sm border border-slate-100">
            <div class="flex flex-col md:flex-row gap-8">
                <div class="md:w-2/5">
                    <img src="../images/breeds/{id}.webp" alt="{name}" class="rounded-2xl w-full aspect-[4/5] object-cover border border-slate-200/50">
                </div>
                <div class="md:w-3/5">
                    <div class="flex items-center gap-2 mb-2">
                        <span class="bg-slate-100 text-slate-600 px-3 py-1 rounded-full text-sm">{group}</span>
                    </div>
                    <h1 class="text-4xl font-bold mb-3">{name}</h1>
                    <p class="text-slate-600 mb-6">{overview}</p>
                    
                    <div class="grid grid-cols-3 gap-4 mb-6">
                        <div class="text-center p-3 bg-slate-50 rounded-xl">
                            <div class="text-2xl mb-1">📏</div>
                            <div class="text-sm text-slate-500">Height</div>
                            <div class="font-semibold">{height} cm</div>
                        </div>
                        <div class="text-center p-3 bg-slate-50 rounded-xl">
                            <div class="text-2xl mb-1">⚖️</div>
                            <div class="text-sm text-slate-500">Weight</div>
                            <div class="font-semibold">{weight} kg</div>
                        </div>
                        <div class="text-center p-3 bg-slate-50 rounded-xl">
                            <div class="text-2xl mb-1">❤️</div>
                            <div class="text-sm text-slate-500">Lifespan</div>
                            <div class="font-semibold">{lifespan}</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Ratings -->
        <div class="bg-white rounded-2xl p-6 mb-8 shadow-sm border border-slate-100">
            <h2 class="text-xl font-bold mb-4">Breed Ratings</h2>
            <div class="grid md:grid-cols-2 gap-4">
                {ratings_html}
            </div>
        </div>

        <!-- Temperament -->
        <div class="bg-white rounded-2xl p-6 mb-8 shadow-sm border border-slate-100">
            <h2 class="text-xl font-bold mb-4">Temperament</h2>
            <div class="flex flex-wrap gap-2">
                {temperament_html}
            </div>
            <p class="mt-4 text-slate-600">{temperament_desc}</p>
        </div>

        <!-- Health & Exercise -->
        <div class="grid md:grid-cols-2 gap-6 mb-8">
            <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-100">
                <h2 class="text-xl font-bold mb-3">🏥 Health</h2>
                <p class="text-slate-600">{health}</p>
            </div>
            <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-100">
                <h2 class="text-xl font-bold mb-3">🏃 Exercise</h2>
                <p class="text-slate-600">{exercise}</p>
            </div>
        </div>

        <!-- Verdict -->
        <div class="bg-gradient-to-r from-sky-50 to-violet-50 rounded-2xl p-6 mb-8 border border-sky-100">
            <h2 class="text-xl font-bold mb-4">Is This Breed Right for You?</h2>
            <div class="grid md:grid-cols-2 gap-6">
                <div>
                    <h3 class="font-semibold text-emerald-700 mb-2">✅ Best For</h3>
                    <ul class="space-y-1 text-slate-600">{best_for_html}</ul>
                </div>
                <div>
                    <h3 class="font-semibold text-rose-700 mb-2">❌ Not Ideal For</h3>
                    <ul class="space-y-1 text-slate-600">{not_for_html}</ul>
                </div>
            </div>
            <p class="mt-4 text-slate-700 font-medium">{summary}</p>
        </div>

        <div class="flex gap-4">
            <a href="../quiz" class="bg-sky-600 hover:bg-sky-700 text-white px-6 py-3 rounded-xl font-semibold">Take Breed Quiz</a>
            <a href="../compare" class="bg-slate-200 hover:bg-slate-300 px-6 py-3 rounded-xl font-semibold">Compare Breeds</a>
        </div>
    </main>

    <footer class="bg-slate-900 text-white py-8 px-4 mt-12">
        <div class="max-w-5xl mx-auto text-center text-slate-400 text-sm">
            <p>© 2026 BreedFinder</p>
        </div>
    </footer>
    <script>lucide.createIcons();</script>
</body>
</html>'''

def generate_page(breed):
    ratings = breed['ratings']
    rating_labels = {
        'energy': 'Energy Level',
        'grooming': 'Grooming Needs',
        'trainability': 'Trainability',
        'kid_friendly': 'Kid Friendly',
        'apartment_ok': 'Apartment Friendly',
        'barking': 'Barking Level',
        'sociability': 'Sociability'
    }
    
    ratings_html = ""
    for key, label in rating_labels.items():
        if key in ratings:
            val = ratings[key]
            pct = val * 20
            ratings_html += f'''<div>
                    <div class="flex justify-between text-sm mb-1"><span>{label}</span><span>{val}/5</span></div>
                    <div class="rating-bar h-2 rounded-full" style="--rating: {pct}%"></div>
                </div>\n'''
    
    temperament_html = "".join([f'<span class="bg-emerald-50 text-emerald-700 px-3 py-1 rounded-full text-sm">{t.title()}</span>' for t in breed['temperament']])
    
    best_for_html = "".join([f'<li>• {item}</li>' for item in breed['verdict']['best_for']])
    not_for_html = "".join([f'<li>• {item}</li>' for item in breed['verdict']['not_for']])
    
    return PAGE_TEMPLATE.format(
        id=breed['id'],
        name=breed['name'],
        group=breed['group'].title(),
        overview=breed['description']['overview'],
        height=breed['size']['height_cm'],
        weight=breed['size']['weight_kg'],
        lifespan=breed['lifespan'],
        ratings_html=ratings_html,
        temperament_html=temperament_html,
        temperament_desc=breed['description']['temperament'],
        health=breed['description']['health'],
        exercise=breed['description']['exercise'],
        best_for_html=best_for_html,
        not_for_html=not_for_html,
        summary=breed['verdict']['summary']
    )

# Generate pages
breeds_dir = os.path.expanduser("~/clawd/dog-breed-guide/breeds")
os.makedirs(breeds_dir, exist_ok=True)

for breed in BREEDS_101_110:
    html = generate_page(breed)
    filepath = os.path.join(breeds_dir, f"{breed['id']}.html")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ {breed['name']}")

print(f"\n🎉 Generated {len(BREEDS_101_110)} breed pages!")
