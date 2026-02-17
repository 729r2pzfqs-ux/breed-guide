#!/usr/bin/env python3
"""Crop breed images to head shots (top-center square crop)"""

from PIL import Image
import os

INPUT_DIR = "images/breeds"
OUTPUT_DIR = "images/heads"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for img_file in sorted(os.listdir(INPUT_DIR)):
    if not img_file.endswith('.png'):
        continue
    
    img_path = os.path.join(INPUT_DIR, img_file)
    img = Image.open(img_path)
    w, h = img.size
    
    # Square crop from top-center (captures head)
    # Use 70% of width as the crop size, focused on top
    size = int(min(w, h * 0.75))
    left = (w - size) // 2
    top = 0
    
    img_cropped = img.crop((left, top, left + size, top + size))
    
    # Resize to consistent 400x400
    img_cropped = img_cropped.resize((400, 400), Image.LANCZOS)
    
    output_path = os.path.join(OUTPUT_DIR, img_file)
    img_cropped.save(output_path, quality=90)
    print(f"✓ {img_file}")

print(f"\nDone! Cropped {len(os.listdir(OUTPUT_DIR))} images to {OUTPUT_DIR}/")
