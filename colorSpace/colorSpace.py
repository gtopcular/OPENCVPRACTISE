from cv2 import cv2

img = cv2.imread("./sources/colorspace.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("img", img)

cv2.imshow("gray", gray)

cv2.waitKey(0)
