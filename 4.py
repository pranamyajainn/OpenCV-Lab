import cv2

# Load the image
img = cv2.imread("test.jpg")

if img is not None:
    print("Original Image Properties:")
    print(" - Shape:", img.shape)
    print(" - Type:", img.dtype)
    print(" - Size:", img.size)

    # Convert to Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print("\nGrayscale Image Shape:", gray.shape)

    # Convert to HSV (used for color detection)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    print("HSV Image Shape:", hsv.shape)

    # Show all versions
    cv2.imshow("Original (BGR)", img)
    cv2.imshow("Grayscale", gray)
    cv2.imshow("HSV", hsv)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("❌ Image not found.")
