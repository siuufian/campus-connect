"""
Quick fix script to create a valid default.jpg image for the Campus Connect project.
Run this script: python fix_default_image_final.py
"""
from PIL import Image, ImageDraw
import os

def create_default_image():
    # Create a 300x300 image with a pleasant gradient background
    img = Image.new('RGB', (300, 300), color='#e3f2fd')
    draw = ImageDraw.Draw(img)
    
    # Draw outer circle (avatar background)
    draw.ellipse([60, 60, 240, 240], fill='#90caf9', outline='#42a5f5', width=3)
    
    # Draw head
    draw.ellipse([115, 95, 185, 165], fill='#ffffff')
    
    # Draw body (shoulders)
    draw.pieslice([80, 150, 220, 290], start=0, end=180, fill='#ffffff')
    
    # Get the media directory path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    media_dir = os.path.join(script_dir, 'media')
    
    # Create media directory if it doesn't exist
    os.makedirs(media_dir, exist_ok=True)
    
    # Save the image
    output_path = os.path.join(media_dir, 'default.jpg')
    img.save(output_path, 'JPEG', quality=95)
    
    # Verify the file
    file_size = os.path.getsize(output_path)
    print(f"✓ Successfully created default.jpg")
    print(f"✓ Location: {output_path}")
    print(f"✓ File size: {file_size:,} bytes")
    print(f"✓ Image dimensions: 300x300 pixels")
    
    # Verify it can be opened
    try:
        test_img = Image.open(output_path)
        print(f"✓ Image verification passed - format: {test_img.format}, mode: {test_img.mode}")
    except Exception as e:
        print(f"✗ Error verifying image: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("Creating default profile image for Campus Connect...")
    print("-" * 60)
    success = create_default_image()
    print("-" * 60)
    if success:
        print("\n✓ All done! You can now register users without errors.")
        print("  The corrupted default.jpg has been replaced with a valid image.")
    else:
        print("\n✗ There was an error. Please check the messages above.")
