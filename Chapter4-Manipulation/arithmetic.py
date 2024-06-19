import cv2
import numpy as np

img = cv2.imread('lenna.png')

# Blank image
blank_image = np.zeros((img.shape), np.uint8)

blank_image[100:200, 100:200,1] = 100

new_image = cv2.add(img, blank_image)

cv2.imshow("result", new_image )
cv2.waitKey(0)
cv2.destroyAllWindows()