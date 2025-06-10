import cv2

# Simple thresholding
img1 = cv2.imread("coins.jpg", 0)  # Load in grayscale
if img1 is not None:
    bin1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)[1]
    bin1_inv = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY_INV)[1]

    cv2.imshow("Binary", bin1)
    cv2.imshow("Binary Inverted", bin1_inv)
else:
    print("coins.jpg not found")

# Adaptive thresholding
img2 = cv2.imread("handwritten.jpg", 0)
if img2 is not None:
    adap = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY, 11, 2)
    adap_inv = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY_INV, 11, 2)

    cv2.imshow("Adaptive", adap)
    cv2.imshow("Adaptive Inverted", adap_inv)
else:
    print("handwritten.jpg not found")

cv2.waitKey(0)
cv2.destroyAllWindows()
