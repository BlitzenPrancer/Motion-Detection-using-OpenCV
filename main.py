import cv2
cam = cv2.VideoCapture(0) # 0 denotes the default webcam
while cam.isOpened():
    ret, frame = cam.read()
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('cam', frame)
