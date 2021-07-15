import cv2
cam = cv2.VideoCapture(0) # 0 denotes the default webcam
while cam.isOpened():
    ret, frame = cam.read()
    if cv2.waitKey(10) == ord('q'): # this makes the computer wait for 10 seconds until q key is pressed
        break
    cv2.imshow('cam', frame)
