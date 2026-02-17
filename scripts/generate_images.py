#!/usr/bin/env python3
"""
Batch generate dog breed images using Replicate API (Flux 1.1 Pro - best quality)
"""

import os
import replicate
import requests
import time

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
    return f"Ultra realistic studio photograph of {article} {breed} dog, sitting and facing camera, eye level perspective, neutral attentive expression, adult dog, ideal breed standard appearance. The dog is framed in a vertical 4:5 portrait composition, head centered, top of ears close to top edge, cropped at mid chest so paws are not visible, consistent head size across breeds. Soft diffused studio lighting, 85mm lens look, shallow depth of field, seamless light grey studio background with a subtle natural shadow under the dog for separation. Professional kennel club catalog photography style, no collar, no accessories, no text."

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
        # Using Flux 1.1 Pro (best quality)
        output = replicate.run(
            "black-forest-labs/flux-1.1-pro",
            input={
                "prompt": prompt,
                "aspect_ratio": "4:5",
                "output_format": "png",
                "safety_tolerance": 2
            }
        )
        
        # Download the image
        if output:
            img_url = str(output)
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
    print("🐕 BreedFinder Image Generator (Flux 1.1 Pro)")
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
        
        # Respect rate limits (10s between requests)
        time.sleep(10)
    
    print(f"\n{'='*50}")
    print(f"✅ Generated: {success}/{len(BREEDS)}")
    if failed:
        print(f"❌ Failed: {', '.join(failed)}")
    print(f"📁 Output: {output_dir}")

if __name__ == "__main__":
    main()
