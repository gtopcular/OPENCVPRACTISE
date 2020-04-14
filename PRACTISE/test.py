import cv2

img =cv2.imread('C:\\Users\\Giray\\Desktop\\helikopter.jpg',0)
cv2.imshow('helikopter.jpg',img)


dugme = cv2.waitKey(0)

if dugme == 27:
    cv2.destroyAllWindows()
else :
    cv2.imwrite("gri_helikopter.jpg",img)    