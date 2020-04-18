from cv2 import cv2
import numpy as np

cap = cv2.VideoCapture(0)

sensitivity = 15                              #  HSV
lower_white = np.array([0,0,168+sensitivity]) #CODE
upper_white = np.array([172,15+sensitivity,255]) #  WHITE

while (True) :
    _,frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv,lower_white,upper_white)

    res = cv2.bitwise_and(frame,frame,mask=mask) # bu kullanım özel kullanımdır...

    cv2.imshow("frame",frame)

    cv2.imshow("mask",mask)

    cv2.imshow("result",res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break