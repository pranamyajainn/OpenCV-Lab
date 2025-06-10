import cv2

# ----- IMAGE PART -----
# Load an image from file
img = cv2.imread("test.jpg")  # Replace with your image file

if img is not None:
    print("Image loaded successfully!")
    print("Type:", img.dtype)       # Data type of pixel values
    print("Shape:", img.shape)      # Height, Width, Channels
    print("Size:", img.size)        # Total number of pixels (H × W × C)

    cv2.imshow("Image", img)        # Show the image
    cv2.waitKey(0)                  # Wait until a key is pressed
    cv2.destroyAllWindows()
else:
    print("Could not load image.")

# ----- VIDEO PART -----
# Open webcam (0 = default camera)
cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Webcam not accessible.")
else:
    print("Showing webcam. Press 'q' to quit.")

    while True:
        ret, frame = cam.read()         # Read each frame
        if not ret:
            break

        cv2.imshow("Webcam", frame)     # Show frame

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
