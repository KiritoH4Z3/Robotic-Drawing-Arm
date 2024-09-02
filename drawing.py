import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'assets/face.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply Gaussian blur to smooth out the image
blurred = cv2.GaussianBlur(image, (7, 7), 0)

# Use Canny edge detection
edges = cv2.Canny(blurred, 30, 100)

# Dilate and erode to enhance edges
dilated = cv2.dilate(edges, None, iterations=1)
eroded = cv2.erode(dilated, None, iterations=1)

# Find contours
contours, _ = cv2.findContours(eroded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Simplify contours for easier processing
simplified_contours = [cv2.approxPolyDP(cnt, 10, True) for cnt in contours]

# Prepare an image for drawing
contour_image = np.ones_like(image) * 255

# Draw simplified contours on a white background
cv2.drawContours(contour_image, simplified_contours, -1, (0, 0, 0), 1)

# Show the result
plt.imshow(contour_image, cmap='gray')
plt.title('Simplified Contour Image')
plt.show()

# Convert contours to a format that the Arduino can understand
drawing_instructions = []
for contour in simplified_contours:
    for point in contour:
        x, y = point[0]
        drawing_instructions.append((x, y))

# Save the drawing instructions to a file
with open('drawing_instructions.txt', 'w') as f:
    for instruction in drawing_instructions:
        f.write(f"{instruction[0]},{instruction[1]}\n")

print("Drawing instructions have been saved.")
