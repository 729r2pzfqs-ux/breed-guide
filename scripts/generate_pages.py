#!/usr/bin/env python3
"""
Generate breed HTML pages from JSON data
"""

import os
import json
import glob

def rating_to_text(rating):
    """Convert 1-5 rating to text"""
    if rating <= 1: return "Very Low"
    if rating == 2: return "Low"
    if rating == 3: return "Moderate"
    if rating == 4: return "High"
    return "Very High"

def rating_to_percent(rating):
    """Convert 1-5 rating to percentage"""
    return rating * 20

def rating_to_color(rating):
    """Get color class for rating"""
    if rating <= 2: return "rose-500"
    if rating == 3: return "amber-600"
    return "sky-600"

def group_to_display(group):
    """Convert group slug to display name"""
    groups = {
        "sporting": "Sporting",
        "hound": "Hound",
        "working": "Working",
        "terrier": "Terrier",
        "toy": "Toy",
        "non-sporting": "Non-Sporting",
        "herding": "Herding",
        "miscellaneous": "Miscellaneous"
    }
    return groups.get(group, group.title())

def size_to_display(size):
    """Convert size slug to display name"""
    sizes = {
        "tiny": "Tiny",
        "small": "Small",
        "medium": "Medium",
        "large": "Large",
        "giant": "Giant"
    }
    return sizes.get(size, size.title())

def generate_breed_page(data):
    """Generate HTML page for a breed"""
    
    # Get ratings
    ratings = data.get("ratings", {})
    
    # Build temperament tags
    temperament_tags = ""
    for temp in data.get("temperament", []):
        temperament_tags += f'''<span class="bg-emerald-50 text-emerald-700 border border-emerald-200 px-4 py-2 rounded-full text-sm font-medium">{temp.title()}</span>\n                '''
    
    # Build best_for list
    best_for_items = ""
    for item in data.get("verdict", {}).get("best_for", []):
        best_for_items += f'''<li class="flex items-start gap-3">
                            <i data-lucide="circle" class="w-2 h-2 mt-2 text-emerald-500 fill-current"></i>
                            <span>{item}</span>
                        </li>\n                        '''
    
    # Build not_for list
    not_for_items = ""
    for item in data.get("verdict", {}).get("not_for", []):
        not_for_items += f'''<li class="flex items-start gap-3">
                            <i data-lucide="circle" class="w-2 h-2 mt-2 text-rose-500 fill-current"></i>
                            <span>{item}</span>
                        </li>\n                        '''
    
    size = data.get("size", {})
    desc = data.get("description", {})
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data["name"]}: Breed Guide, Temperament & Care | BreedFinder</title>
    <meta name="description" content="Complete guide to the {data["name"]}: temperament, exercise needs, grooming, health issues, and whether this breed is right for you.">
    <link rel="canonical" href="https://breedfinder.org/breeds/{data["id"]}">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{ sans: ['Plus Jakarta Sans', 'sans-serif'] }}
                }}
            }}
        }}
    </script>
    <style>
        .rating-bar {{ 
            background: #e2e8f0;
            position: relative;
            overflow: hidden;
        }}
        .rating-bar::after {{
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            height: 100%;
            width: var(--rating);
            background: linear-gradient(90deg, #0ea5e9, #8b5cf6);
            border-radius: 9999px;
        }}
        .card-shadow {{
            box-shadow: 0 1px 3px rgba(0,0,0,0.05), 0 4px 12px rgba(0,0,0,0.04);
        }}
    </style>
</head>
<body class="bg-gradient-to-b from-slate-50 to-white min-h-screen text-slate-800">
    <!-- Header -->
    <header class="bg-white/80 backdrop-blur-md border-b border-slate-200/60 sticky top-0 z-50">
        <div class="max-w-5xl mx-auto px-4 py-4 flex items-center justify-between">
            <a href="/" class="flex items-center gap-3">
                <div class="w-10 h-10 bg-gradient-to-br from-sky-500 to-violet-500 rounded-xl flex items-center justify-center text-white shadow-lg shadow-sky-500/20">
                    <i data-lucide="dog" class="w-5 h-5"></i>
                </div>
                <span class="text-xl font-bold bg-gradient-to-r from-slate-800 to-slate-600 bg-clip-text text-transparent">BreedFinder</span>
            </a>
            <nav class="flex items-center gap-6 text-sm font-medium">
                <a href="/breeds" class="text-slate-600 hover:text-sky-600 transition">All Breeds</a>
                <a href="/quiz" class="text-slate-600 hover:text-sky-600 transition">Breed Quiz</a>
            </nav>
        </div>
    </header>

    <main class="max-w-5xl mx-auto px-4 py-8">
        <!-- Breadcrumb -->
        <nav class="text-sm text-slate-500 mb-6 flex items-center gap-2">
            <a href="/" class="hover:text-sky-600 transition">Home</a>
            <i data-lucide="chevron-right" class="w-4 h-4 text-slate-300"></i>
            <a href="/breeds" class="hover:text-sky-600 transition">Breeds</a>
            <i data-lucide="chevron-right" class="w-4 h-4 text-slate-300"></i>
            <span class="text-slate-700 font-medium">{data["name"]}</span>
        </nav>

        <!-- Hero Card -->
        <div class="bg-white rounded-3xl p-8 mb-8 card-shadow border border-slate-100">
            <div class="flex flex-col md:flex-row gap-8">
                <!-- Image -->
                <div class="md:w-2/5">
                    <img src="/images/breeds/{data["id"]}.png" alt="{data["name"]}" class="rounded-2xl w-full aspect-[4/5] object-cover border border-slate-200/50" onerror="this.onerror=null; this.src=''; this.parentElement.innerHTML='<div class=\\'bg-gradient-to-br from-slate-100 to-slate-50 rounded-2xl aspect-[4/5] flex items-center justify-center border border-slate-200/50\\'><i data-lucide=\\'dog\\' class=\\'w-24 h-24 text-slate-300\\'></i></div>'; lucide.createIcons();">
                </div>
                
                <!-- Info -->
                <div class="md:w-3/5">
                    <div class="flex items-center gap-2 mb-3">
                        <span class="bg-sky-100 text-sky-700 text-xs font-semibold px-3 py-1 rounded-full">{group_to_display(data.get("group", ""))}</span>
                        <span class="bg-violet-100 text-violet-700 text-xs font-semibold px-3 py-1 rounded-full">{size_to_display(size.get("category", ""))}</span>
                    </div>
                    
                    <h1 class="text-4xl font-bold text-slate-900 mb-3">{data["name"]}</h1>
                    <p class="text-lg text-slate-600 mb-6 leading-relaxed">{desc.get("overview", "")[:200]}...</p>
                    
                    <div class="grid grid-cols-2 gap-4">
                        <div class="bg-slate-50 rounded-xl p-4">
                            <div class="text-xs font-medium text-slate-500 uppercase tracking-wide mb-1 flex items-center gap-1">
                                <i data-lucide="map-pin" class="w-3 h-3"></i> Origin
                            </div>
                            <div class="text-slate-800 font-semibold">{data.get("origin", "Unknown")}</div>
                        </div>
                        <div class="bg-slate-50 rounded-xl p-4">
                            <div class="text-xs font-medium text-slate-500 uppercase tracking-wide mb-1 flex items-center gap-1">
                                <i data-lucide="heart" class="w-3 h-3"></i> Lifespan
                            </div>
                            <div class="text-slate-800 font-semibold">{data.get("lifespan", "10-14 years")}</div>
                        </div>
                        <div class="bg-slate-50 rounded-xl p-4">
                            <div class="text-xs font-medium text-slate-500 uppercase tracking-wide mb-1 flex items-center gap-1">
                                <i data-lucide="ruler" class="w-3 h-3"></i> Height
                            </div>
                            <div class="text-slate-800 font-semibold">{size.get("height_cm", "N/A")} cm</div>
                        </div>
                        <div class="bg-slate-50 rounded-xl p-4">
                            <div class="text-xs font-medium text-slate-500 uppercase tracking-wide mb-1 flex items-center gap-1">
                                <i data-lucide="scale" class="w-3 h-3"></i> Weight
                            </div>
                            <div class="text-slate-800 font-semibold">{size.get("weight_kg", "N/A")} kg</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Ratings Card -->
        <div class="bg-white rounded-3xl p-8 mb-8 card-shadow border border-slate-100">
            <h2 class="text-2xl font-bold text-slate-900 mb-6 flex items-center gap-3">
                <span class="w-10 h-10 bg-gradient-to-br from-amber-400 to-orange-500 rounded-xl flex items-center justify-center text-white shadow-lg shadow-amber-500/20">
                    <i data-lucide="bar-chart-3" class="w-5 h-5"></i>
                </span>
                Breed Ratings
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                    <div class="flex justify-between text-sm mb-2">
                        <span class="font-medium text-slate-700 flex items-center gap-2"><i data-lucide="zap" class="w-4 h-4 text-slate-400"></i> Energy Level</span>
                        <span class="font-semibold text-{rating_to_color(ratings.get("energy", 3))}">{rating_to_text(ratings.get("energy", 3))}</span>
                    </div>
                    <div class="h-3 rounded-full rating-bar" style="--rating: {rating_to_percent(ratings.get("energy", 3))}%"></div>
                </div>
                <div>
                    <div class="flex justify-between text-sm mb-2">
                        <span class="font-medium text-slate-700 flex items-center gap-2"><i data-lucide="scissors" class="w-4 h-4 text-slate-400"></i> Grooming Needs</span>
                        <span class="font-semibold text-{rating_to_color(ratings.get("grooming", 3))}">{rating_to_text(ratings.get("grooming", 3))}</span>
                    </div>
                    <div class="h-3 rounded-full rating-bar" style="--rating: {rating_to_percent(ratings.get("grooming", 3))}%"></div>
                </div>
                <div>
                    <div class="flex justify-between text-sm mb-2">
                        <span class="font-medium text-slate-700 flex items-center gap-2"><i data-lucide="users" class="w-4 h-4 text-slate-400"></i> Sociability</span>
                        <span class="font-semibold text-{rating_to_color(ratings.get("sociability", 3))}">{rating_to_text(ratings.get("sociability", 3))}</span>
                    </div>
                    <div class="h-3 rounded-full rating-bar" style="--rating: {rating_to_percent(ratings.get("sociability", 3))}%"></div>
                </div>
                <div>
                    <div class="flex justify-between text-sm mb-2">
                        <span class="font-medium text-slate-700 flex items-center gap-2"><i data-lucide="graduation-cap" class="w-4 h-4 text-slate-400"></i> Trainability</span>
                        <span class="font-semibold text-{rating_to_color(ratings.get("trainability", 3))}">{rating_to_text(ratings.get("trainability", 3))}</span>
                    </div>
                    <div class="h-3 rounded-full rating-bar" style="--rating: {rating_to_percent(ratings.get("trainability", 3))}%"></div>
                </div>
                <div>
                    <div class="flex justify-between text-sm mb-2">
                        <span class="font-medium text-slate-700 flex items-center gap-2"><i data-lucide="baby" class="w-4 h-4 text-slate-400"></i> Kid Friendly</span>
                        <span class="font-semibold text-{rating_to_color(ratings.get("kid_friendly", 3))}">{rating_to_text(ratings.get("kid_friendly", 3))}</span>
                    </div>
                    <div class="h-3 rounded-full rating-bar" style="--rating: {rating_to_percent(ratings.get("kid_friendly", 3))}%"></div>
                </div>
                <div>
                    <div class="flex justify-between text-sm mb-2">
                        <span class="font-medium text-slate-700 flex items-center gap-2"><i data-lucide="building" class="w-4 h-4 text-slate-400"></i> Apartment Suitable</span>
                        <span class="font-semibold text-{rating_to_color(ratings.get("apartment_ok", 3))}">{rating_to_text(ratings.get("apartment_ok", 3))}</span>
                    </div>
                    <div class="h-3 rounded-full rating-bar" style="--rating: {rating_to_percent(ratings.get("apartment_ok", 3))}%"></div>
                </div>
            </div>
        </div>

        <!-- Temperament -->
        <div class="mb-8">
            <h2 class="text-2xl font-bold text-slate-900 mb-4">Temperament</h2>
            <div class="flex flex-wrap gap-2">
                {temperament_tags}
            </div>
        </div>

        <!-- Content Sections -->
        <div class="space-y-6">
            <details class="bg-white rounded-2xl card-shadow border border-slate-100 group" open>
                <summary class="p-6 cursor-pointer flex items-center justify-between">
                    <h2 class="text-xl font-bold text-slate-900 flex items-center gap-3">
                        <i data-lucide="book-open" class="w-5 h-5 text-sky-500"></i> Overview
                    </h2>
                    <i data-lucide="chevron-down" class="w-5 h-5 text-slate-400 group-open:rotate-180 transition-transform"></i>
                </summary>
                <div class="px-6 pb-6">
                    <p class="text-slate-600 leading-relaxed">{desc.get("overview", "")}</p>
                </div>
            </details>

            <details class="bg-white rounded-2xl card-shadow border border-slate-100 group">
                <summary class="p-6 cursor-pointer flex items-center justify-between">
                    <h2 class="text-xl font-bold text-slate-900 flex items-center gap-3">
                        <i data-lucide="heart" class="w-5 h-5 text-sky-500"></i> Temperament
                    </h2>
                    <i data-lucide="chevron-down" class="w-5 h-5 text-slate-400 group-open:rotate-180 transition-transform"></i>
                </summary>
                <div class="px-6 pb-6">
                    <p class="text-slate-600 leading-relaxed">{desc.get("temperament", "")}</p>
                </div>
            </details>

            <details class="bg-white rounded-2xl card-shadow border border-slate-100 group">
                <summary class="p-6 cursor-pointer flex items-center justify-between">
                    <h2 class="text-xl font-bold text-slate-900 flex items-center gap-3">
                        <i data-lucide="heart-pulse" class="w-5 h-5 text-sky-500"></i> Health
                    </h2>
                    <i data-lucide="chevron-down" class="w-5 h-5 text-slate-400 group-open:rotate-180 transition-transform"></i>
                </summary>
                <div class="px-6 pb-6">
                    <p class="text-slate-600 leading-relaxed">{desc.get("health", "")}</p>
                </div>
            </details>

            <details class="bg-white rounded-2xl card-shadow border border-slate-100 group">
                <summary class="p-6 cursor-pointer flex items-center justify-between">
                    <h2 class="text-xl font-bold text-slate-900 flex items-center gap-3">
                        <i data-lucide="activity" class="w-5 h-5 text-sky-500"></i> Exercise
                    </h2>
                    <i data-lucide="chevron-down" class="w-5 h-5 text-slate-400 group-open:rotate-180 transition-transform"></i>
                </summary>
                <div class="px-6 pb-6">
                    <p class="text-slate-600 leading-relaxed">{desc.get("exercise", "")}</p>
                </div>
            </details>
        </div>

        <!-- THE VERDICT -->
        <div class="mt-10 bg-gradient-to-br from-sky-50 via-violet-50 to-rose-50 rounded-3xl p-8 border border-sky-100">
            <h2 class="text-2xl font-bold text-slate-900 mb-6 flex items-center gap-3">
                <span class="w-10 h-10 bg-gradient-to-br from-sky-500 to-violet-500 rounded-xl flex items-center justify-center text-white shadow-lg shadow-sky-500/20">
                    <i data-lucide="target" class="w-5 h-5"></i>
                </span>
                Is This Breed Right for You?
            </h2>
            
            <div class="grid md:grid-cols-2 gap-8 mb-8">
                <div class="bg-white/70 backdrop-blur rounded-2xl p-6 border border-emerald-100">
                    <h3 class="font-bold text-emerald-700 mb-4 flex items-center gap-2">
                        <span class="w-6 h-6 bg-emerald-500 rounded-full flex items-center justify-center text-white">
                            <i data-lucide="check" class="w-4 h-4"></i>
                        </span>
                        Best For
                    </h3>
                    <ul class="space-y-3 text-slate-700">
                        {best_for_items}
                    </ul>
                </div>
                <div class="bg-white/70 backdrop-blur rounded-2xl p-6 border border-rose-100">
                    <h3 class="font-bold text-rose-700 mb-4 flex items-center gap-2">
                        <span class="w-6 h-6 bg-rose-500 rounded-full flex items-center justify-center text-white">
                            <i data-lucide="x" class="w-4 h-4"></i>
                        </span>
                        Not Ideal For
                    </h3>
                    <ul class="space-y-3 text-slate-700">
                        {not_for_items}
                    </ul>
                </div>
            </div>

            <div class="bg-white rounded-2xl p-6 border border-slate-200">
                <p class="text-lg text-slate-700 leading-relaxed"><strong class="text-slate-900">Our Verdict:</strong> {data.get("verdict", {}).get("summary", "")}</p>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="mt-16 bg-slate-50 border-t border-slate-200">
        <div class="max-w-5xl mx-auto px-4 py-8 text-center">
            <div class="flex items-center justify-center gap-3 mb-4">
                <div class="w-8 h-8 bg-gradient-to-br from-sky-500 to-violet-500 rounded-lg flex items-center justify-center text-white">
                    <i data-lucide="dog" class="w-4 h-4"></i>
                </div>
                <span class="font-bold text-slate-800">BreedFinder</span>
            </div>
            <p class="text-sm text-slate-500 mb-4">Find your perfect dog breed match</p>
            <div class="flex justify-center gap-6 text-sm text-slate-600">
                <a href="/breeds" class="hover:text-sky-600 transition">All Breeds</a>
                <a href="/quiz" class="hover:text-sky-600 transition">Breed Quiz</a>
                <a href="/about" class="hover:text-sky-600 transition">About</a>
            </div>
            <p class="text-xs text-slate-400 mt-6">© 2026 BreedFinder. Made with care for dog lovers.</p>
        </div>
    </footer>

    <script>lucide.createIcons();</script>
</body>
</html>'''
    
    return html

def main():
    print("🐕 BreedFinder Page Generator\n")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, "..", "data", "breeds")
    output_dir = os.path.join(script_dir, "..", "breeds")
    
    os.makedirs(output_dir, exist_ok=True)
    
    json_files = glob.glob(os.path.join(data_dir, "*.json"))
    
    print(f"Found {len(json_files)} breed JSON files\n")
    
    for json_file in sorted(json_files):
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        breed_id = data.get("id", os.path.basename(json_file).replace(".json", ""))
        output_path = os.path.join(output_dir, f"{breed_id}.html")
        
        html = generate_breed_page(data)
        
        with open(output_path, 'w') as f:
            f.write(html)
        
        print(f"✅ {data['name']} → breeds/{breed_id}.html")
    
    print(f"\n{'='*50}")
    print(f"✅ Generated {len(json_files)} breed pages in /breeds/")

if __name__ == "__main__":
    main()
