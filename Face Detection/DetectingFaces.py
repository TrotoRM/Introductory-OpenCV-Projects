import cv2
import imutils
import numpy as np


faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("Gattu.jpg")
img = imutils.resize(img, 400)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
    cv2.circle(img, (int(x + w/2), int(y + h/2)), 2, (255, 0, 255), 2)
cv2.imshow("Result", img)
cv2.waitKey(0)

