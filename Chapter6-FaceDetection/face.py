import cv2

face_cascade = cv2.CascadeClassifier(f'{cv2.data.haarcascades}haarcascade_frontalface_default.xml')

img = cv2.imread('20240501_161358.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Classifier มาค้นหาใบหน้าในภาพ
faces = face_cascade.detectMultiScale(gray, 1.5, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

# fits the screen
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()