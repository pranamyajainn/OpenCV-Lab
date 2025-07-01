import cv2

# Load image in grayscale
img = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

# Transpose the image (flip rows and columns)
img_transposed = cv2.transpose(img)

# Create SIFT detector
sift = cv2.SIFT_create()

# Detect keypoints and descriptors
kp1, des1 = sift.detectAndCompute(img, None)
kp2, des2 = sift.detectAndCompute(img_transposed, None)

# Match features using Brute-Force
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

# Apply Lowe’s ratio test to keep only good matches
good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append([m])

# Draw matches between original and transposed image
matched_img = cv2.drawMatchesKnn(img, kp1, img_transposed, kp2, good_matches, None, flags=2)

# Show the result
cv2.imshow("SIFT Matching - Original vs Transposed", matched_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
