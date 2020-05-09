from cv2 import cv2
import numpy as np

img = cv2.imread("./sources/coins.jpg")
img2 = cv2.imread("./sources/balls.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

img1_blur = cv2.medianBlur(gray,5)
img2_blur = cv2.medianBlur(gray2,5)

#circles = cv2.HoughCircles(img1_blur,cv2.HOUGH_GRADIENT,1,img.shape[0]/4,param1=200,param2=10,minRadius=30,maxRadius=70)
circles = cv2.HoughCircles(img2_blur,cv2.HOUGH_GRADIENT,1,img2.shape[0]/15,param1=200,param2=10,minRadius=15,maxRadius=70)
#img.shape[0]/64 bir kalıptır duruma göre değiştirebilir (circles arası mesafeler)
#param1 = gradian
#param2 = threshold değeri ikiside methoda özel tanımlıdır direk girilen değerler girilmeli



if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(img2,(i[0],i[1]),i[2],(255,0,0),2)

cv2.imshow("img",img2)

cv2.waitKey(0)