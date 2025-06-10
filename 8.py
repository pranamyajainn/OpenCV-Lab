import cv2

# Read the img in black and white
img = cv2.imread("object.jpg", 0)

if img is not None:
    # Find edges using Canny
    edges = cv2.Canny(img, 100, 200)

    # Show the original and edge result
    cv2.imshow("Original", img)
    cv2.imshow("Edges", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("File not found.")
