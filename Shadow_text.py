import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import matplotlib.font_manager as fm

# Ask the user to input the index of the font they want to use
input_text = str(input("Enter the text: "))

# Get the list of font files and their names
font_files = {f.name: f.fname for f in fm.fontManager.ttflist}

# Print the list of font names with their corresponding indices
font_names = list(font_files.keys())
for i, font_name in enumerate(font_names):
    print(f"{i}: {font_name}")

# Ask the user to input the index of the font they want to use
font_index = int(input("Enter the number corresponding to the font you want to use: "))

# Ensure the input is a valid index
if 0 <= font_index < len(font_names):
    chosen_font_name = font_names[font_index]
    chosen_font_file = font_files[chosen_font_name]
    print(f"You have chosen the font: {chosen_font_name}")
else:
    print("Invalid input. Please enter a number corresponding to a font.")

# Use the font file in your shadow text code
font_path = ImageFont.truetype(chosen_font_file, 70)

# Create a blank image with white background
image = np.zeros((300, 600), dtype=np.uint8)

# Set the text to be displayed
# input_text = "Hello, World!"

# Convert the image to RGB
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# Use PIL to draw text on the image
image_pil = Image.fromarray(image)
draw = ImageDraw.Draw(image_pil)

# Draw the shadow text
draw.text((20, 20), input_text, font=font_path, fill=(192, 192, 192))

# Draw the actual text
draw.text((10, 10), input_text, font=font_path, fill=(255, 255, 255))

# Convert the image back to a NumPy array
image = np.array(image_pil)

# Apply Gaussian blur to the image
image = cv2.GaussianBlur(image, (5, 5), 0)

# Display the image
cv2.imshow('Text Shadow', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
