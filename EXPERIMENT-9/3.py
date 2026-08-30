import cv2
import numpy as np
from google.colab.patches import cv2_imshow
# Load the image
image = cv2.imread('/content/imgae fro exp 9.1.jpg')
# Define the size of the Averaging filter kernel
kernel_size = (5, 5) # You can adjust the size based on the desired
#smoothing level
# Create the Averaging filter kernel
kernel = np.ones(kernel_size, dtype=np.float32) / (kernel_size[0] *
kernel_size[1])
# Apply the Averaging filter for smoothing
smoothed_image = cv2.filter2D(image, -1, kernel)
# Display the original and smoothed images
cv2_imshow(image)
cv2_imshow(smoothed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()