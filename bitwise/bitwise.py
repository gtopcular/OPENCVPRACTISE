from cv2 import cv2
import numpy as np 

img1 = cv2.imread("./sources/bitwise-1.png")
img2 = cv2.imread("./sources/bitwise-2.png")

bit_and = cv2.bitwise_and(img2,img1)
bit_or = cv2.bitwise_or(img2,img1)
bit_xor = cv2.bitwise_xor(img1,img2)
bit_xor2 = cv2.bitwise_xor(img2,img1)

cv2.imshow("birlesim",bit_and)
cv2.imshow("birlesim or",bit_or)
cv2.imshow("birlesim xor",bit_xor)
cv2.imshow("birlesim xor2",bit_xor2)




cv2.waitKey(0)