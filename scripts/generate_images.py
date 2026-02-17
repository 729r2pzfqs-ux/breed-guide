#!/usr/bin/env python3
"""
Batch generate dog breed images using Replicate API (Flux model)
Cost: ~$0.03 per image = ~$1.50 total for 50 breeds
"""

import os
import replicate
import requests
import time

# Get API key from environment
# export REPLICATE_API_TOKEN=your_token_here

BREEDS = [
    "Labrador Retriever", "German Shepherd", "Golden Retriever", "French Bulldog",
    "Bulldog", "Poodle", "Beagle", "Rottweiler", "German Shorthaired Pointer",
    "Dachshund", "Pembroke Welsh Corgi", "Yorkshire Terrier", "Boxer",
    "Siberian Husky", "Australian Shepherd", "Great Dane", "Doberman Pinscher",
    "Cavalier King Charles Spaniel", "Miniature Schnauzer", "Shih Tzu",
    "Boston Terrier", "Bernese Mountain Dog", "Pomeranian", "Havanese",
    "Shetland Sheepdog", "Brittany", "English Springer Spaniel", "Cocker Spaniel",
    "Chihuahua", "Border Collie", "Vizsla", "Pug", "Weimaraner",
    "Belgian Malinois", "Maltese", "Rough Collie", "Basset Hound", "Newfoundland",
    "Rhodesian Ridgeback", "Shiba Inu", "West Highland White Terrier",
    "Bichon Frise", "Akita", "Samoyed", "Portuguese Water Dog", "St. Bernard",
    "Bull Terrier", "Miniature American Shepherd", "Australian Cattle Dog",
    "Alaskan Malamute"
]

def breed_to_slug(breed):
    """Convert breed name to file slug"""
    return breed.lower().replace(" ", "-").replace(".", "")

def generate_prompt(breed):
    """Generate the image prompt for a breed"""
    article = "an" if breed[0].lower() in "aeiou" else "a"
    return f"Ultra realistic studio photograph of {article} {breed} dog, sitting and facing camera, eye level perspective, neutral attentive expression, adult dog, ideal breed standard appearance, soft diffused studio lighting, 85mm lens look, shallow depth of field, seamless light grey studio background, centered composition, camera positioned farther back, consistent head size across breeds, top of ears near top margin, cropped at mid chest, paws not visible, subtle natural shadow under dog for separation, professional kennel club catalog photography style, no collar, no accessories, no text"

def generate_image(breed, output_dir="images"):
    """Generate a single breed image"""
    slug = breed_to_slug(breed)
    output_path = os.path.join(output_dir, f"{slug}.png")
    
    # Skip if already exists
    if os.path.exists(output_path):
        print(f"⏭️  Skipping {breed} (already exists)")
        return True
    
    prompt = generate_prompt(breed)
    print(f"🎨 Generating {breed}...")
    
    try:
        # Using Flux Schnell (fast, good quality, cheap)
        output = replicate.run(
            "black-forest-labs/flux-schnell",
            input={
                "prompt": prompt,
                "aspect_ratio": "4:5",
                "output_format": "png",
                "output_quality": 90
            }
        )
        
        # Download the image
        if output and len(output) > 0:
            img_url = output[0]
            response = requests.get(img_url)
            
            os.makedirs(output_dir, exist_ok=True)
            with open(output_path, 'wb') as f:
                f.write(response.content)
            
            print(f"✅ Saved {slug}.png")
            return True
        else:
            print(f"❌ No output for {breed}")
            return False
            
    except Exception as e:
        print(f"❌ Error generating {breed}: {e}")
        return False

def main():
    print("🐕 BreedFinder Image Generator")
    print(f"📦 {len(BREEDS)} breeds to generate\n")
    
    # Check API key
    if not os.environ.get("REPLICATE_API_TOKEN"):
        print("❌ Error: REPLICATE_API_TOKEN not set")
        print("   Run: export REPLICATE_API_TOKEN=your_token_here")
        return
    
    output_dir = os.path.join(os.path.dirname(__file__), "..", "images", "breeds")
    
    success = 0
    failed = []
    
    for i, breed in enumerate(BREEDS, 1):
        print(f"\n[{i}/{len(BREEDS)}]", end=" ")
        if generate_image(breed, output_dir):
            success += 1
        else:
            failed.append(breed)
        
        # Respect rate limits (6/min with <$5 credit = 10s between)
        time.sleep(12)
    
    print(f"\n{'='*50}")
    print(f"✅ Generated: {success}/{len(BREEDS)}")
    if failed:
        print(f"❌ Failed: {', '.join(failed)}")
    print(f"📁 Output: {output_dir}")

if __name__ == "__main__":
    main()
