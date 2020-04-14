import cv2

yVid = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
cikti = cv2.VideoWriter("C:\\Users\\Giray\\Desktop\\selamınaleyküm.mp4",fourcc,20.0,(640,480))

while(True):
   deger,kare= yVid.read()
   if deger == True :
     cikti.write(kare)
     cv2.imshow("SOKAK",kare)
   if cv2.waitKey(1)& 0xFF == ord("a"):
      break

yVid.release()
cikti.release()
cv2.destroyAllWindows()