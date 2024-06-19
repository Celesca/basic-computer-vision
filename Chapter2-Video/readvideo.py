import cv2

cap = cv2.VideoCapture("./road2.mp4")

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()