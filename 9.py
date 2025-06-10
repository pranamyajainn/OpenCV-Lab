import cv2

# Read the img in black and white
img = cv2.imread("shapes.jpg", 0)

if img is not None:
    # Apply binary threshold
    result = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]

    # Find contours
    contours = cv2.findContours(result, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    # Convert original img to color so we can draw in color
    color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    # Draw all contours in green
    cv2.drawContours(color_img, contours, -1, (0, 255, 0), 2)

    # Show images
    cv2.imshow("Original", img)
    cv2.imshow("Threshold", result)
    cv2.imshow("Contours", color_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("File not found.")
