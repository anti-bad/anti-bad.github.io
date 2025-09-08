#!/usr/bin/env python3

from PIL import Image
import os

def rotate_image():
    # Input and output paths
    input_path = "./pill-horizontal.png"
    output_path = "./pill-horizontal-rotated.png"
    
    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found")
        return
    
    # Open and rotate the image
    with Image.open(input_path) as img:
        # Resize to make it larger (scale by 3.0x)
        width, height = img.size
        img = img.resize((int(width * 3.0), int(height * 3.0)), Image.Resampling.LANCZOS)
        
        # Rotate by 45 degrees (clockwise)
        rotated = img.rotate(45, expand=True, fillcolor=(255, 255, 255, 0))
        
        # Crop to remove blank areas - get the bounding box of non-transparent pixels
        bbox = rotated.getbbox()
        if bbox:
            rotated = rotated.crop(bbox)
        
        # Save the rotated image
        rotated.save(output_path, "PNG")
        print(f"Rotated image saved as: {output_path}")

if __name__ == "__main__":
    rotate_image()