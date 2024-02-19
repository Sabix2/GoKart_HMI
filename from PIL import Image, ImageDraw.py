from PIL import Image, ImageDraw

def cut_gauge_sector_from_image(image_path, angle):
    min_angle = -32
    max_angle = -5

    if angle < 0 or angle > 217:
        return "Invalid angle. Angle should be between 0 and 217."

    # Open the image
    img = Image.open(image_path)

    # Create a mask based on the angle
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)

    if angle > min_angle:
        draw.pieslice([(0, 0), img.size], max_angle, angle, fill=255)

    # Apply the mask to the image
    result = Image.new('RGBA', img.size, (255, 255, 255, 0))
    result.paste(img, mask=mask)

    # Save or display the result image
    result.show()

# Example usage:
image_path = "C:\Users\sebas\OneDrive\Desktop\Assembly.png"
angle_to_cut = 120
cut_gauge_sector_from_image(image_path, angle_to_cut)
