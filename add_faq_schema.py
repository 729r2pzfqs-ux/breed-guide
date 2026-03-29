#!/usr/bin/env python3
"""Add FAQPage schema to all breed pages + compare pages on breedfinder.org"""
import os, re, json

count = 0

def extract_breed_info(html):
    """Extract breed name and key info from page"""
    title_match = re.search(r'<h1[^>]*>([^<]+)</h1>', html)
    name = title_match.group(1).strip() if title_match else None
    if not name:
        title_match = re.search(r'<title>([^|<-]+)', html)
        name = title_match.group(1).strip().replace(' - Breed Guide', '').replace(' | BreedFinder', '') if title_match else None
    
    # Extract overview text
    overview_match = re.search(r'Overview.*?<p[^>]*>([^<]+)</p>', html, re.DOTALL)
    overview = overview_match.group(1).strip()[:200] if overview_match else ""
    
    # Extract temperament
    temp_match = re.search(r'Temperament.*?<p[^>]*>([^<]+)</p>', html, re.DOTALL)
    temperament = temp_match.group(1).strip()[:200] if temp_match else ""
    
    # Extract size/weight info
    size_info = re.findall(r'(\d+[-–]\d+)\s*(lbs|kg|inches|cm)', html)
    
    return name, overview, temperament, size_info

def build_breed_faqs(name, overview, temperament, size_info):
    """Generate FAQ pairs for a breed"""
    if not name:
        return []
    
    faqs = [
        (f"Is a {name} a good family dog?",
         f"{overview[:150]}..." if overview else f"The {name} can make a great family companion depending on your lifestyle. Check temperament, energy level, and size requirements on this page."),
        
        (f"How much exercise does a {name} need?",
         f"Exercise needs vary by individual dog, but the {name} generally requires regular daily activity. Check the exercise and energy level sections above for specific recommendations."),
        
        (f"Are {name}s easy to train?",
         f"{temperament[:150]}..." if temperament else f"Training ease depends on the breed's temperament and intelligence. The {name} has specific training characteristics detailed in the temperament section above."),
        
        (f"How much does a {name} cost?",
         f"The price of a {name} varies by breeder, location, and lineage. Expect to budget for initial purchase, veterinary care, food, grooming, and supplies. Adoption from a rescue is also an excellent option."),
        
        (f"Do {name}s shed a lot?",
         f"Shedding varies by breed. Check the grooming section above for specific information about the {name}'s coat type, grooming frequency, and shedding level."),
    ]
    return faqs

def process_breed(filepath):
    global count
    
    with open(filepath, "r") as f:
        html = f.read()
    
    if "FAQPage" in html:
        return
    
    name, overview, temperament, size_info = extract_breed_info(html)
    if not name:
        return
    
    faqs = build_breed_faqs(name, overview, temperament, size_info)
    if not faqs:
        return
    
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ]
    }
    
    tag = f'<script type="application/ld+json">{json.dumps(schema)}</script>'
    html = html.replace('</head>', tag + '\n</head>')
    
    with open(filepath, "w") as f:
        f.write(html)
    count += 1

# Process EN breed pages
print("🐕 Adding FAQPage schema to breed pages...")
for d in sorted(os.listdir("breeds")):
    p = f"breeds/{d}/index.html"
    if os.path.isfile(p):
        process_breed(p)

print(f"  ✅ EN breeds: {count}")

# Process language breed pages
lang_count = 0
for lang in sorted(os.listdir(".")):
    lang_breeds = f"{lang}/breeds"
    if os.path.isdir(lang_breeds) and lang not in [".", ".git", "breeds"]:
        for d in os.listdir(lang_breeds):
            p = f"{lang_breeds}/{d}/index.html"
            if os.path.isfile(p):
                process_breed(p)
                lang_count += 1

print(f"  ✅ Language breeds: {lang_count}")

# Process compare pages
compare_count = 0
compare_dir = "compare/comparisons"
if os.path.isdir(compare_dir):
    for d in os.listdir(compare_dir):
        p = f"{compare_dir}/{d}/index.html"
        if os.path.isfile(p):
            with open(p, "r") as f:
                html = f.read()
            if "FAQPage" in html:
                continue
            
            # Extract breed names from compare title
            title_match = re.search(r'<title>([^|<]+)', html)
            title = title_match.group(1).strip() if title_match else d.replace("-", " ")
            breeds = re.findall(r'vs\.?|compared', title, re.I)
            parts = re.split(r'\s+vs\.?\s+|\s+compared\s+', title, flags=re.I)
            
            if len(parts) >= 2:
                a, b = parts[0].strip(), parts[1].strip().split(' -')[0].strip().split(' |')[0].strip()
            else:
                a, b = "Breed A", "Breed B"
            
            faqs = [
                (f"What is the difference between {a} and {b}?",
                 f"Compare key differences in size, temperament, energy level, grooming needs, and health between {a} and {b} in the detailed comparison above."),
                (f"Which is better for families, {a} or {b}?",
                 f"Both breeds can be great family dogs depending on your specific situation. Compare their temperament, energy level, and size requirements above to decide."),
                (f"Which breed is easier to train, {a} or {b}?",
                 f"Training ease depends on breed intelligence and temperament. Check the trainability comparison above for specific details on {a} vs {b}."),
            ]
            
            schema = {
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]
            }
            
            tag = f'<script type="application/ld+json">{json.dumps(schema)}</script>'
            html = html.replace('</head>', tag + '\n</head>')
            
            with open(p, "w") as f:
                f.write(html)
            compare_count += 1

print(f"  ✅ Compare pages: {compare_count}")
print(f"\n✅ Total: {count + lang_count + compare_count} pages enriched")
