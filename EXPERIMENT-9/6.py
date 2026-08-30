import cv2
import numpy as np
from google.colab.patches import cv2_imshow
# Load the image
image = cv2.imread('/content/imgae fro exp 9.jpg')
# Apply Gaussian smoothing to reduce noise (optional but recommended)
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
# Create a Laplacian kernel for sharpening
laplacian_kernel = np.array([[0, -1, 0],
[-1, 5, -1],
[0, -1, 0]], dtype=np.float32)
# Apply the Laplacian filter for sharpening
sharpened_image = cv2.filter2D(blurred_image, -1, laplacian_kernel)
# Display the original image, blurred image, and sharpened image
cv2_imshow(image)
cv2_imshow(blurred_image)
cv2_imshow(sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()