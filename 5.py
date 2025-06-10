import cv2

# Read image (use a clean image or one with salt & pepper noise)
img = cv2.imread("noisy_image.jpg")  # Replace with your image name

if img is not None:
    # 1. Normal Blur (Average Blur)
    blur = cv2.blur(img, (5, 5))

    # 2. Median Blur (good for salt & pepper noise)
    median = cv2.medianBlur(img, 5)

    # 3. Gaussian Blur (more natural blur)
    gaussian = cv2.GaussianBlur(img, (5, 5), 0)

    # 4. Bilateral Filter (smoothens while keeping edges sharp)
    bilateral = cv2.bilateralFilter(img, 9, 75, 75)

    # Show all images
    cv2.imshow("Original", img)
    cv2.imshow("Blur", blur)
    cv2.imshow("Median Blur", median)
    cv2.imshow("Gaussian Blur", gaussian)
    cv2.imshow("Bilateral Filter", bilateral)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("❌ Image not found.")
