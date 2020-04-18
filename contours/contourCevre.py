from cv2 import cv2

img = cv2.imread("./sources/contour.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]

'''
area= cv2.contourArea(cnt)

print(area)

M=cv2.moments(cnt)

print(M['m00']) #Moments fonk dönen m00 area ya eşittir 
'''

perimeter =cv2.arcLength(cnt,True)
print(perimeter)



cv2.waitKey(0)