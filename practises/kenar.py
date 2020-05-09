from cv2 import cv2
import numpy as np

img = cv2.imread("./sources/contour.png")
w,h = img.shape[:2]

print(w)
print(h)



kernel= np.array([[1,1,1],[1,-8,1],[1,1,1]],np.uint8)


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

deneme = cv2.Laplacian(gray,cv2.CV_8U,(3,3))


cv2.imshow("orginal",img)

cv2.imshow("deneme",deneme)



cv2.waitKey(0)
cv2.destroyAllWindows