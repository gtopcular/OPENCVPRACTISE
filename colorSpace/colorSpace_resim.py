from cv2 import cv2
import numpy as np


img = cv2.imread(".\\sources\\filter.png")

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_blue=np.array([110,50,50])
upper_blue=np.array([130,255,255])

mask = cv2.inRange(hsv,lower_blue,upper_blue)
cv2.imshow("MASK",mask)
cv2.imshow("VİDEO",img)

cv2.waitKey(0)

vid.realese()
cv2.destroyAllWindows()
