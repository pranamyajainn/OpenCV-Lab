import cv2

# Read image
img = cv2.imread("test.jpg")  # Use any image you have

if img is not None:
    # Show original properties
    print("📷 Original Image")
    print("  - Shape:", img.shape)
    print("  - Data Type:", img.dtype)
    print("  - Size:", img.size)

    # --- Resize image (make it half the size) ---
    resized = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))

    print("\n🔍 Resized Image")
    print("  - Shape:", resized.shape)
    print("  - Data Type:", resized.dtype)
    print("  - Size:", resized.size)

    # --- Crop image (take top-left 100x100 region) ---
    cropped = img[0:100, 0:100]  # [rows, cols]

    print("\n✂️ Cropped Image")
    print("  - Shape:", cropped.shape)
    print("  - Data Type:", cropped.dtype)
    print("  - Size:", cropped.size)

    # --- Display all images in separate windows ---
    cv2.imshow("Original Image", img)
    cv2.imshow("Resized Image", resized)
    cv2.imshow("Cropped Image", cropped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("❌ Could not load image.")
