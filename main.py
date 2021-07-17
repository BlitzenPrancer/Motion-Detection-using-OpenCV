import cv2
import winsound
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
    # creating threshold to get rid of the noise
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    # making things bigger with dilation
    dilated = cv2.dilate(thresh, None, iterations = 3)
    # finding contours
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # drawing contours
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2 )
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        # getting x, y, width,and height of contours greater than 5000
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x,y), (x + w, y + h), (0, 255, 0), 2)
        winsound.PlaySound('audio.wav', winsound.SND_ASYNC)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('cam', frame1)