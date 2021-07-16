import cv2
cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    # creating a difference between frame1 and frame2
    diff = cv2.absdiff(frame1, frame2)
    # converting difference to grey colour
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    # converting grey to blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('cam', blur)