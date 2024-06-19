import cv2

image = cv2.imread('lenna.png')

# Convert image to HSV
image_hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

cv2.imshow('display', image_hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()