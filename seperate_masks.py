from PIL import Image
import numpy as np

# Load the image
image_path = 'S1078754.png'
image = Image.open(image_path)

# Convert the image to RGBA if it is not already in that mode
image = image.convert("RGBA")

# Split into separate channels and create masks
r, g, b, a = image.split()

# Process the red channel
# Create a mask where the red channel has content, and other channels are ignored
red_mask = Image.merge("RGBA", (r, Image.new('L', r.size, 0), Image.new('L', r.size, 0), r))

# Process the green channel
# Create a mask where the green channel has content, and other channels are ignored
green_mask = Image.merge("RGBA", (Image.new('L', g.size, 0), g, Image.new('L', g.size, 0), g))

# Save the masks to separate files
# red_mask_path = 'masks/red_mask.png'
# green_mask_path = 'masks/green_mask.png'

import os

# Define the directory path
directory = 'masks'

# Create the 'masks' directory if it does not exist
if not os.path.exists(directory):
    os.makedirs(directory)
    
# Define the full paths for red and green masks
red_mask_path = os.path.join(directory, 'red_mask.png')
green_mask_path = os.path.join(directory, 'green_mask.png')

red_mask.save(red_mask_path)
green_mask.save(green_mask_path)

# Provide the paths to the saved mask images
red_mask_path, green_mask_path
