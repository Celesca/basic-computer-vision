import cv2

image = cv2.imread('lenna.png')

# Write image pixel
image[50:100,50:100] = 0

cv2.imshow('display', image)

# Image Properties
print(f'The size of the image is {image.shape}')
print(f'The data type of the image is {image.dtype}')
print(f'The dimensions of the image is {image.ndim}')

# Save image
cv2.imwrite("result.png", image)


cv2.waitKey(0)
cv2.destroyAllWindows()