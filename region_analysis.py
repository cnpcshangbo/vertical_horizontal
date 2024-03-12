#!.conda/bin/python
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import regionprops, label
from scipy.ndimage import rotate

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
    
    # Criteria for differentiating crack types (can be fine-tuned)
    if aspect_ratio > 1.2:
        horizontal_cracks.append(props.bbox)
    elif aspect_ratio < 0.8:
        vertical_cracks.append(props.bbox)
    else:
        # Assuming square-like regions are diagonal cracks
        # This is a simplification and might not be accurate
        orientation = props.orientation
        if -np.pi/4 <= orientation <= np.pi/4:
            horizontal_cracks.append(props.bbox)
        else:
            diagonal_cracks.append(props.bbox)

# Function to display cracks
def show_cracks(cracks, title):
    fig, ax = plt.subplots()
    ax.imshow(alpha_channel, cmap='gray')
    for bbox in cracks:
        y0, x0, y1, x1 = bbox
        rect = plt.Rectangle((x0, y0), x1-x0, y1-y0, linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(rect)
    ax.set_title(title)
    plt.show()

# Display the results
show_cracks(vertical_cracks, 'Vertical Cracks')
show_cracks(horizontal_cracks, 'Horizontal Cracks')
show_cracks(diagonal_cracks, 'Diagonal Cracks')

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Define a function to save images of cracks
def save_crack_images(cracks, title, save_path):
    fig, ax = plt.subplots()
    ax.imshow(alpha_channel, cmap='gray')  # Assuming 'alpha_channel' is your mask
    for bbox in cracks:
        y0, x0, y1, x1 = bbox
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, linewidth=1, edgecolor='r', facecolor='none'))
    ax.set_title(title)
    plt.axis('off')  # Turn off axis
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0)
    plt.close()

# Example usage:
save_crack_images(vertical_cracks, 'Vertical Cracks', 'vertical_cracks.png')
save_crack_images(horizontal_cracks, 'Horizontal Cracks', 'horizontal_cracks.png')
save_crack_images(diagonal_cracks, 'Diagonal Cracks', 'diagonal_cracks.png')
