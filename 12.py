#Edge detection, line detection, corner detection
import cv2
import numpy as np

# Load image
img = cv2.imread('sample.jpg')  # Make sure this image is in your folder
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

# ------------------------
# 1. EDGE DETECTION (CANNY)
edges = cv2.Canny(gray, 100, 200)  # Detect edges
cv2.imshow("1. Canny Edge Detection", edges)
cv2.waitKey(0)

# ------------------------
# 2. LINE DETECTION (HOUGH)
# Use Canny edges again
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)

# Draw lines on a copy of original
line_img = img.copy()
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(line_img, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Draw green lines

cv2.imshow("2. Hough Line Detection", line_img)
cv2.waitKey(0)

# ------------------------
# 3. CORNER DETECTION (HARRIS)
gray_float = np.float32(gray)  # Harris needs float32 image
corners = cv2.cornerHarris(gray_float, 2, 3, 0.04)

# Make corners visible
corners = cv2.dilate(corners, None)  # Enlarge corner points

# Show corners in red on original image
corner_img = img.copy()
corner_img[corners > 0.01 * corners.max()] = [0, 0, 255]  # Red color

cv2.imshow("3. Harris Corner Detection", corner_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
