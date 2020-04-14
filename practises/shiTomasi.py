from cv2 import cv2
import numpy as np

img = cv2.imread("./sources/contour.png")
img2 = cv2.imread("./sources/text.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray1 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
gray1 = np.float32(gray1)

corners = cv2.goodFeaturesToTrack(gray,50,0.01,10) 
corners1 = cv2.goodFeaturesToTrack(gray1,50,0.01,10) 
#işlem yapılacak resim,bulunacak köşe sayısı,kalite(girilen değer deneysel)
#noktalar arası mesafe 

corners = np.int0(corners)
corners1 = np.int0(corners1)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,(0,0,255),-1)
for corner in corners1:
    x,y = corner.ravel()
    cv2.circle(img2,(x,y),3,(0,0,255),-1)

cv2.imshow("img",img)
cv2.imshow("img2",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()