import cv2

# Load the image
img = cv2.imread("test.jpg")  # Use your image name here

# Check if loaded
if img is not None:
    cv2.imshow("Image", img)             # Show the image
    cv2.imwrite("new_image.jpg", img)    # Save with a new name
    print("✅ Saved as new_image.jpg")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("❌ Couldn't load the image.")

# Start webcam
cam = cv2.VideoCapture(0)

# Check if working
if cam.isOpened():
    print("🎥 Webcam started. Press 'q' to quit.")
    while True:
        success, frame = cam.read()
        if not success:
            break
        cv2.imshow("Webcam", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
else:
    print("❌ Webcam not found.")

