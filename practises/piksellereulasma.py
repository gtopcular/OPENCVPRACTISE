import cv2 
import numpy as np

img = cv2.imread(".\\sources\\helikopter.jpg")
#cv2.imshow("image",img)

px = img[411,100]

blue = img[411,100,0] #blue pikseli almak için 0
green = img[411,100,1] #green pikseli için 1
red = img[411,100,2] #red pikseli için 2

#print(blue,green,red)

print(img.shape)  #piksel bilgileri sonuncusu kanal bilgisi

print(img.size) #toplam piksel sayısı 

############ ROI --> region of image  ##########

kuyruk = img[156 : 256,0 : 80] #resmin belli bir bölümünü kesme
cv2.imshow("kuyruk",kuyruk)

img[200:300,300:380] = kuyruk #kesilen kısmı resme yapıştırma

cv2.imshow("image",img)


cv2.waitKey(0)

  