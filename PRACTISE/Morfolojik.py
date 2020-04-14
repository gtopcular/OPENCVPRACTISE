from cv2 import cv2 
import numpy as np

img = cv2.imread("C:\\Users\\Giray\\Desktop\\work\\helikopter.jpg")


kernel2= np.array([[1,0,5],[5,0,5],[7,2,3]],np.uint8)
kernel = np.ones((5,5),np.uint8)
kernel1= np.ones((3,3),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
erosion1 = cv2.erode(img,kernel1,iterations= 1)
erosion2 = cv2.erode(img,kernel2,iterations = 1)
cv2.imshow("goster",erosion)
cv2.imshow("goster 3x3",erosion1)
cv2.imshow ("goster 3x3k",erosion2)
cv2.waitKey(0)
cv2.destroyAllWindows