import cv2
import numpy as np

# 1. Make a white image of 400x400 pixels
img = np.ones((400, 400, 3), dtype=np.uint8) * 255

# 2. Draw a blue circle at position (100, 100), radius 50
cv2.circle(img, (100, 100), 50, (255, 0, 0), 2)
# (image, center_position, radius, color, thickness)

# 3. Draw a green filled rectangle from point (200, 50) to point (350, 150)
cv2.rectangle(img, (200, 50), (350, 150), (0, 255, 0), -1)
# (image, first_corner, opposite_corner, color, -1 means filled)

# 4. Draw a red line from point (50, 300) to point (350, 300)
cv2.line(img, (50, 300), (350, 300), (0, 0, 255), 3)
# (image, starting_point, ending_point, color, thickness)

# 5. Write your USN or name at the bottom-left corner
cv2.putText(img, "1MS21AI001", (10, 390), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
# (image, text, position, font, size, color, thickness)

# 6. Show and save the image
cv2.imshow("Drawing", img)
cv2.imwrite("drawing_output.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
