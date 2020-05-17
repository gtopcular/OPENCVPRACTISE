from cv2 import cv2
import numpy as np

cap = cv2.VideoCapture("./sources/car.mp4")
_,ff = cap.read()
ff = cv2.resize(ff,(500,500))
fgray = cv2.cvtColor(ff,cv2.COLOR_BGR2GRAY)
fblur = cv2.GaussianBlur(fgray,(5,5),0)
while 1:
    _,frame = cap.read()
    frame = cv2.resize(frame,(500,500))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)

    diff = cv2.absdiff(fgray,gray)
    _,diff = cv2.threshold(diff,30,255,cv2.THRESH_BINARY)

    cv2.imshow("frame",frame)
    cv2.imshow("first",ff)
    cv2.imshow("diff",diff)
    

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()