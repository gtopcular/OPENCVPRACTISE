from cv2 import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#cv2.line(img,(100,50),(200,360),(100,0,0),5)
#cv2.rectangle(img,(100,50),(200,360),(100,0,0),5)
cv2.circle(img,(50,50),30,(255,0,0),-1)

cv2.imshow("img",img)

cv2.waitKey()