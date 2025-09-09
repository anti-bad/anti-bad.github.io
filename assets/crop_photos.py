#!/usr/bin/env python3
"""
Automatic photo cropping script for organizer headshots
Crops photos to focus on face/head region and saves to photo_crop directory
pip install opencv-python pillow
"""

import os
import cv2
import numpy as np
from PIL import Image, ImageEnhance
import argparse
import pathlib
import urllib.request

def resolve_haarcascade():
    """
    Resolve haarcascade path in several ways (works for headless builds):
    1) cv2.data.haarcascades (if available)
    2) OPENCV_HAAR_DIR env var
    3) local file next to this script: ./haarcascade_frontalface_default.xml
    4) ~/.cache/opencv-haar/haarcascade_frontalface_default.xml (download if missing)
    Returns: absolute path to xml or None if not found.
    """
    filename = 'haarcascade_frontalface_default.xml'

    # 1) cv2.data
    try:
        base = getattr(cv2, "data").haarcascades  # may fail in headless builds
        p = os.path.join(base, filename)
        if os.path.exists(p):
            return p
    except Exception:
        pass

    # 2) env var
    env_dir = os.environ.get("OPENCV_HAAR_DIR")
    if env_dir:
        p = os.path.join(env_dir, filename)
        if os.path.exists(p):
            return p

    # 3) local next to script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    local_p = os.path.join(script_dir, filename)
    if os.path.exists(local_p):
        return local_p

    # 4) cache (download if missing)
    cache_dir = os.path.join(pathlib.Path.home(), ".cache", "opencv-haar")
    os.makedirs(cache_dir, exist_ok=True)
    cache_p = os.path.join(cache_dir, filename)
    if not os.path.exists(cache_p):
        try:
            url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
            print(f"Downloading haarcascade to {cache_p} ...")
            urllib.request.urlretrieve(url, cache_p)
        except Exception as e:
            print(f"Warning: failed to download haarcascade: {e}")
            return None
    return cache_p if os.path.exists(cache_p) else None

def detect_and_crop_face(image_path, output_path, target_size=300):
    """
    Detect face in image and crop to square format centered on face
    """
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image {image_path}")
        return False
    
    # Convert to RGB for face detection
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Load OpenCV's pre-trained face detection classifier (robust to headless builds)
    haar_path = resolve_haarcascade()
    face_cascade = None
    if haar_path and os.path.exists(haar_path):
        face_cascade = cv2.CascadeClassifier(haar_path)
    else:
        print("Warning: Haarcascade not available (cv2.data missing and no xml found). "
              "Will use center crop when detection fails.")
    
    # Convert to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces (only if cascade is valid)
    faces = []
    if face_cascade is not None and not face_cascade.empty():
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))
    
    if len(faces) == 0:
        print(f"No face detected in {image_path}, using center crop")
        # Fallback to center crop
        h, w = image.shape[:2]
        size = min(h, w)
        start_x = (w - size) // 2
        start_y = (h - size) // 2
        cropped = image[start_y:start_y+size, start_x:start_x+size]
    else:
        # Use the largest detected face
        (x, y, w, h) = max(faces, key=lambda face: face[2] * face[3])
        
        # Calculate expanded crop area (include more head/shoulder area)
        expand_factor = 2.4  # Default expansion factor
        center_x = x + w // 2
        center_y = y + h // 2
        
        # Default: Shift center point up more conservatively to include hair
        center_y = max(0, center_y - int(h * 0.15))  # Move up by only 15% of face height
        
        # Apply special handling for specific individuals
        filename_lower = image_path.lower()
        
        if 'heather_lent' in filename_lower:
            center_y = center_y + int(h * 0.3)
        elif 'ansh_arora' in filename_lower:
            center_x = center_x + int(w * 0.2)
            center_y = center_y - int(h * 0.2)
            expand_factor = 1.8
        
        # Calculate crop size based on face size
        crop_size = int(max(w, h) * expand_factor)
        
        # Ensure crop area is within image bounds
        img_h, img_w = image.shape[:2]
        crop_size = min(crop_size, min(img_w, img_h))
        
        # Calculate crop boundaries
        start_x = max(0, center_x - crop_size // 2)
        end_x = min(img_w, start_x + crop_size)
        start_y = max(0, center_y - crop_size // 2)
        end_y = min(img_h, start_y + crop_size)
        
        # Adjust if crop area is at edge
        if end_x - start_x < crop_size:
            start_x = max(0, end_x - crop_size)
        if end_y - start_y < crop_size:
            start_y = max(0, end_y - crop_size)
        
        # Crop the image
        cropped = image[start_y:end_y, start_x:end_x]
    
    # Convert to PIL Image for resizing
    pil_image = Image.fromarray(cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB))
    
    # Resize to target size while maintaining aspect ratio
    pil_image = pil_image.resize((target_size, target_size), Image.Resampling.LANCZOS)
    
    # Enhance image quality slightly
    enhancer = ImageEnhance.Sharpness(pil_image)
    pil_image = enhancer.enhance(1.1)
    
    # Save the processed image
    pil_image.save(output_path, quality=95, optimize=True)
    print(f"Processed: {os.path.basename(image_path)} -> {os.path.basename(output_path)}")
    return True

def main():
    # Set up directories
    script_dir = os.path.dirname(os.path.abspath(__file__))
    photos_dir = os.path.join(script_dir, 'photos')
    output_dir = os.path.join(script_dir, 'photo_crop')
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Check if photos directory exists
    if not os.path.exists(photos_dir):
        print(f"Error: Photos directory not found: {photos_dir}")
        return
    
    # Get all image files from photos directory
    image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff'}
    image_files = []
    
    for filename in os.listdir(photos_dir):
        if any(filename.lower().endswith(ext) for ext in image_extensions):
            image_files.append(filename)
    
    if not image_files:
        print("No image files found in photos directory")
        return
    
    print(f"Found {len(image_files)} images to process:")
    for img in sorted(image_files):
        print(f"  - {img}")
    
    print(f"\nProcessing images...")
    print(f"Input directory: {photos_dir}")
    print(f"Output directory: {output_dir}")
    print("-" * 50)
    
    # Process each image
    success_count = 0
    for filename in sorted(image_files):
        input_path = os.path.join(photos_dir, filename)
        
        # Keep original extension
        name, ext = os.path.splitext(filename)
        output_filename = f"{name}{ext}"
        output_path = os.path.join(output_dir, output_filename)
        
        if detect_and_crop_face(input_path, output_path):
            success_count += 1
    
    print("-" * 50)
    print(f"Processing complete!")
    print(f"Successfully processed: {success_count}/{len(image_files)} images")
    print(f"Cropped images saved to: {output_dir}")
    
    if success_count > 0:
        print("\nNext steps:")
        print("1. Review the cropped images in photo_crop directory")
        print("2. Rename them to match original filenames if needed")
        print("3. Update index.md to use photos from photo_crop directory")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure you have OpenCV and Pillow installed:")
        print("pip install opencv-python pillow")
