import cv2
import numpy as np
import os

# Use a relative path with forward slashes
image_path = 'assets/face.jpg'

# Check if the image file exists
if not os.path.exists(image_path):
    print(f"Error: The image file '{image_path}' was not found.")
else:
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Image not loaded properly. Check the path or file format.")
    else:
        # Convert to binary using adaptive threshold
        thresh = cv2.adaptiveThreshold(
            image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
        )

        # Display the threshold image
        cv2.imshow('Threshold Image', thresh)
        cv2.waitKey(0)  # Wait for a key press to close the window
        cv2.destroyAllWindows()

        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Simplify contours for easier processing
        simplified_contours = [cv2.approxPolyDP(cnt, 2, True) for cnt in contours]

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
