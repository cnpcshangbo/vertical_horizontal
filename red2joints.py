import cv2
import numpy as np

# Load red_mask image
red_mask = cv2.imread('masks/red_mask.png', cv2.IMREAD_GRAYSCALE)

# Apply Canny edge detection
edges = cv2.Canny(red_mask, 100, 200)

# Save edges to a mask file
cv2.imwrite('masks/edges.png', edges)

# Calculate gradient angles
sobelx = cv2.Sobel(red_mask, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(red_mask, cv2.CV_64F, 0, 1, ksize=5)
gradient = np.arctan2(sobely, sobelx) * 180 / np.pi

# Classify cracks based on orientation
# vertical_cracks = edges[np.where((gradient > -45) & (gradient < 45))]
# horizontal_cracks = edges[np.where((gradient >= 45) & (gradient <= 135))]
# other_cracks = edges[np.where((gradient < -135) | (gradient > 135))]

# Visualize classified cracks (optional)
# Overlay color-coded markings on red_mask image

# Further analysis or processing as needed
# Classify cracks based on orientation
vertical_cracks = np.zeros_like(red_mask)
vertical_cracks[np.where((gradient > -45) & (gradient < 45))] = 255

horizontal_cracks = np.zeros_like(red_mask)
horizontal_cracks[np.where((gradient >= 45) & (gradient <= 135))] = 255

other_cracks = np.zeros_like(red_mask)
other_cracks[np.where((gradient < -135) | (gradient > 135))] = 255

rest_cracks = np.zeros_like(red_mask)
rest_cracks[np.where((gradient > -135) & (gradient < -45))] = 255


# Save classified cracks to separate mask files
cv2.imwrite('masks/vertical_cracks.png', vertical_cracks)
cv2.imwrite('masks/horizontal_cracks.png', horizontal_cracks)
cv2.imwrite('masks/other_cracks.png', other_cracks)
cv2.imwrite('masks/rest_cracks.png', rest_cracks)