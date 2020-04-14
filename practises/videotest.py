import cv2

yVid = cv2.VideoCapture("./sources/sokak.mp4")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
cikti = cv2.VideoWriter("./outputs/yenisokak.mp4",fourcc,20.0,(640,480))

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