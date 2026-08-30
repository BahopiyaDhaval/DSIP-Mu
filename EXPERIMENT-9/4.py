import cv2
import numpy as np
from google.colab.patches import cv2_imshow
# Load the image
image = cv2.imread('/content/imgae fro exp 9.jpg')
# Define the size of the median filter kernel (should be an odd number)
kernel_size = 5 # You can adjust the size based on the desired
#smoothing level
# Apply the Median filter for smoothing
smoothed_image = cv2.medianBlur(image, kernel_size)
# Display the original and smoothed images
cv2_imshow(image)
cv2_imshow(smoothed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()