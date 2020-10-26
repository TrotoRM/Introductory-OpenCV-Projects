import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture(0)


def getContours(img, img1):
    contours, Hierachy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    counter = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 300:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            width, height = w * 3, h * 3
            pts1 = np.float32([[x, y], [x, y + h], [x + w, y + h], [x + w, y]])
            pts2 = np.float32([[0, 0], [0, height], [width, height], [width, 0]])
            matrix = cv2.getPerspectiveTransform(pts1, pts2)
            imgOutput = cv2.warpPerspective(img1, matrix, (width, height))
            counter = counter + 1
            cv2.imshow("Stuff" + str(counter), imgOutput)
            cv2.rectangle(imgContour, (x,y), (x+w, y+h), (255, 0, 255), 2)
            cv2.circle(imgContour, (int(x + w/2), int(y + h/2)), 2, (255, 0, 255), 2)


while(cap.isOpened()):
    ret, img = cap.read()
    ret, dang = cap.read()
    img = imutils.resize(img, 800)
    dang = imutils.resize(dang, 800)
    imgContour = img

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 50)
    getContours(imgCanny, dang)


    cv2.imshow("Original", dang)
    cv2.imshow("Gray", imgGray)
    cv2.imshow("Blur", imgBlur)
    cv2.imshow("Edges", imgCanny)
    cv2.imshow("Contour", imgContour)
    k = cv2.waitKey(0)
    if k == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

