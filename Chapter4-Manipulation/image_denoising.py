import cv2
 
# Reading the image
image = cv2.imread('apple.png')
 
# Showing the image
cv2.imshow('Original', image)

# Applying the filter
# เอาคค่า pixel ข้างๆมาบวกแล้วเฉลี่ยให้ค่าสีเท่ากัน ทำให้ภาพเท่ากันทุกผืน
smoothimg = cv2.blur(image, (5, 5))
cv2.imshow('AvarageBlur', smoothimg)

# เบลอตรงกลางเยอะเป็นพิเศษ และะค่อยๆจาง ทำให้ขอบยังคม Noise จะหายไปนิดๆ

smoothimg = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('GaussianBlur', smoothimg)

# Noise ที่เล็กๆ หายไป แต่ขอบยังอยู่ Filter ที่มีขนาดใหญ่ ให้มีความถี่สูง
# เปลี่ยนค่า Pixel ต่ำไปสูง ความถี่จะสูง มันจะลบตัวความถี่ต่ำ

smoothimg = cv2.bilateralFilter(image, 5, 75, 75)
cv2.imshow('bilateralFilter', smoothimg)

# เบลอพิเศษ คงขอบและความถี่พิเศษไว้ แต่อันไหนเป็นความถี่น้อยๆ จะหายไป
# เช่น กระ สิว จุด ทำให้ขอบยังคม สิวก็จะหายไป Surface Blur

smoothimg = cv2.medianBlur(image, 5)
cv2.imshow('medianBlur', smoothimg)

 
cv2.waitKey()
cv2.destroyAllWindows()