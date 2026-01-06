import os
import sys

# Add the project directory to the path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

from PIL import Image, ImageDraw

# Create a 300x300 image with a light gray background
img = Image.new('RGB', (300, 300), color='#e0e0e0')
draw = ImageDraw.Draw(img)

# Draw a circle for avatar placeholder
circle_color = '#9e9e9e'
draw.ellipse([50, 50, 250, 250], fill=circle_color)

# Draw a simple person icon
# Head
draw.ellipse([125, 90, 175, 140], fill='#ffffff')
# Body
draw.ellipse([100, 140, 200, 240], fill='#ffffff')

# Save the image
media_path = os.path.join(project_dir, 'media')
os.makedirs(media_path, exist_ok=True)
img.save(os.path.join(media_path, 'default.jpg'), 'JPEG', quality=95)

print("✓ Default image created successfully at media/default.jpg")
print(f"✓ Image size: {os.path.getsize(os.path.join(media_path, 'default.jpg'))} bytes")
