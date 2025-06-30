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
cap = cv2.VideoCapture('sample.mp4')  # Make sure this file exists

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Video', frame)

    # Print properties only for the first frame
    print("Frame dtype:", frame.dtype)
    print("Frame shape:", frame.shape)
    print("Frame size:", frame.size)
    break  # Remove this line if you want to play full video

cap.release()
cv2.destroyAllWindows()
