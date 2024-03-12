#!.conda/bin/python
import numpy as np
from skimage.measure import label, regionprops
from PIL import Image, ImageDraw

# Load the red mask image
red_mask_image_path = './masks/red_mask.png'
red_mask = Image.open(red_mask_image_path)

# Convert to numpy array and get the alpha channel as the mask
red_mask_np = np.array(red_mask)
alpha_channel = red_mask_np[:, :, 3]  # Assuming the alpha channel is the last one

# Label connected components
labeled_mask = label(alpha_channel)

# Analyze properties of labeled regions
regions = regionprops(labeled_mask)

# Placeholder for categorized cracks
vertical_cracks = []
horizontal_cracks = []
diagonal_cracks = []

# Classify based on orientation and aspect ratio
for props in regions:
    y0, x0, y1, x1 = props.bbox
    region_height = y1 - y0
    region_width = x1 - x0
    aspect_ratio = region_width / float(region_height)

    # Store the coordinates of the region (connected component) instead of the bounding box
    if aspect_ratio > 2:
        horizontal_cracks.extend(props.coords)
    elif aspect_ratio < 0.5:
        vertical_cracks.extend(props.coords)
    else:
        # Diagonal classification can be refined as needed
        orientation = props.orientation
        if -np.pi/4 <= orientation <= np.pi/4:
            horizontal_cracks.extend(props.coords)
        else:
            diagonal_cracks.extend(props.coords)

# Function to create and save a mask with the connected components
def save_crack_mask(coords_list, mask_path, image_shape):
    # Create an empty image with transparent background
    crack_mask = Image.new('RGBA', (image_shape[1], image_shape[0]), (0, 0, 0, 0))
    draw = ImageDraw.Draw(crack_mask)

    # Draw each pixel for the classified cracks
    for coord in coords_list:
        draw.point((coord[1], coord[0]), fill=(255, 0, 0, 255))  # (x, y)

    # Save the mask
    crack_mask.save(mask_path)

# Image shape needed for mask creation
image_shape = alpha_channel.shape

import os
# Create the directory if it doesn't exist
if not os.path.exists('3masks'):
    os.makedirs('3masks')

# Save masks for each type of crack
save_crack_mask(vertical_cracks, '3masks/vertical_crack_mask.png', image_shape)
save_crack_mask(horizontal_cracks, '3masks/horizontal_crack_mask.png', image_shape)
save_crack_mask(diagonal_cracks, '3masks/diagonal_crack_mask.png', image_shape)
