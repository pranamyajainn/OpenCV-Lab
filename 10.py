#identify color object and draw contours 
import cv2
import numpy as np

# Load image
img = cv2.imread('color_objects.jpg')  # Replace with your image path

# Convert to HSV (Hue, Saturation, Value) – better for color detection
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define HSV ranges for Red, Green, Blue
color_ranges = [
    ("Red",   [0, 120, 70],   [10, 255, 255]),
    ("Green", [36, 25, 25],   [86, 255, 255]),
    ("Blue",  [94, 80, 2],    [126, 255, 255])
]

# Loop through each color
for name, lower, upper in color_ranges:
    # Convert to numpy arrays
    lower_np = np.array(lower)
    upper_np = np.array(upper)

    # Create a mask for the color
    mask = cv2.inRange(hsv, lower_np, upper_np)

    # Find contours of that color
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangle and label if area is big enough
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:  # Ignore small dots
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(img, (x, y), (x+w, y+h), (255,255,255), 2)
            cv2.putText(img, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)

# Show the final image
cv2.imshow("Color Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
