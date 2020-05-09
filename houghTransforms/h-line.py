from cv2 import cv2 
import numpy as np 

img = cv2.imread("./sources/h-line.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,75,150,)#kaynak, min threshold değeri max threshold değeri

lines = cv2.HoughLinesP(edges,1,np.pi/180,50) # sonuna maxlineGap eklenerek boşluklar doldurulabilir

#
# print(lines)

for i in lines:
    x1,y1,x2,y2 = i[0]
    
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)

cv2.imshow("img",img)


cv2.waitKey(0)
cv2.destroyAllWindows()