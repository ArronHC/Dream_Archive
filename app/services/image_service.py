# app/services/image_service.py

from PIL import Image, ImageDraw, ImageFont

def text_to_image(text):
    # This is a placeholder for a more complex implementation
    img = Image.new('RGB', (800, 600), color = (255, 255, 255))
    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 15)
    except IOError:
        font = ImageFont.load_default()
    d.text((10,10), text, fill=(0,0,0), font=font)
    return img
