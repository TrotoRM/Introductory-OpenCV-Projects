import cv2
import imutils
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # img = cv2.imread("cool.png")
    #img = imutils.resize(img, 400)

    ret, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 6)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
        cv2.circle(img, (int(x + w/2), int(y + h/2)), 2, (255, 0, 255), 2)
    cv2.imshow("Result", img)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

