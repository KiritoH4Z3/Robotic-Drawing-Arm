import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'assets/face.jpg'
image = cv2.imread(image_path)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray_image, 50, 150)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Prepare an image for drawing
contour_image = np.ones_like(gray_image) * 255

# Draw contours with varying line weights
for contour in contours:
    # Calculate line weight based on contour size (adjust scaling factor)
    line_weight = int(cv2.arcLength(contour, True) / 10000) + 1  # Increased scaling factor

    # Apply a threshold to limit the maximum line weight
    line_weight = min(line_weight, 2)  # Maximum line weight of 2

    # Draw the contour with the calculated line weight
    cv2.drawContours(contour_image, [contour], -1, (0, 0, 0), line_weight)

# Remove smaller lines using morphological operations
kernel = np.ones((3, 3), np.uint8)
contour_image = cv2.morphologyEx(contour_image, cv2.MORPH_OPEN, kernel, iterations=1)

# Show the result
plt.imshow(contour_image, cmap='gray')
plt.title('Pencil Sketch Contour Image')
plt.show()


# Convert contours to a format that the Arduino can understand
drawing_instructions = []
for contour in contours:
    for point in contour:
        x, y = point[0]
        drawing_instructions.append((x, y))

# Save the drawing instructions to a file
with open('drawing_instructions.txt', 'w') as f:
    for instruction in drawing_instructions:
        f.write(f"{instruction[0]},{instruction[1]}\n")

print("Drawing instructions have been saved.")
