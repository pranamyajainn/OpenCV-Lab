import cv2
import numpy as np

# Load image in color and grayscale
img = cv2.imread("box.jpg")
gray = cv2.imread("box.jpg", 0)

if img is not None and gray is not None:
    gray = np.float32(gray)

    # Apply Harris
    result = cv2.cornerHarris(gray, 2, 3, 0.04)
    result = cv2.dilate(result, None)

    # Make two copies to show different threshold outputs
    low = img.copy()
    high = img.copy()

    # Low threshold (more corners)
    low[result > 0.01 * result.max()] = [0, 0, 255]   # red

    # High threshold (fewer, stronger corners)
    high[result > 0.02 * result.max()] = [0, 255, 0]  # green

    # Show both for comparison
    cv2.imshow("Corners - Low Threshold", low)
    cv2.imshow("Corners - High Threshold", high)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found.")
