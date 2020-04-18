from cv2 import cv2


img = cv2.imread("./sources/contour1.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,tresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contours,_ = cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img,contours,1,(0,0,255),3) #3. değerde -1 yazarsan resmin dışarıdaki çerçevesini de alır , 0 yazarsan sadece çerçeveyi alır , 1 yazarsan sadece şekli alır

cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()