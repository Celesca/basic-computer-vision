import cv2

img = cv2.imread('lenna.png')

# Display Image
cv2.imshow('Original image', img)

# make a copy of the image
imageRectangle = img.copy()

# Define the starting and ending coordinates
start_point = (300,115)
end_point = (475, 225)

rec_img = cv2.rectangle(imageRectangle, start_point, end_point, (0, 0, 255), thickness=3, lineType=cv2.LINE_8)

# Display Image
cv2.imshow('Rectangle image', rec_img)

cv2.waitKey(0)
cv2.destroyAllWindows()