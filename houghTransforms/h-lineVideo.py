from cv2 import cv2
import numpy as np 

vid = cv2.VideoCapture("./sources/line.mp4")


while 1:
    ret,frame = vid.read()
    frame = cv2.resize(frame,(640,480))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([18,94,140],np.uint8)
    upper_yellow = np.array([48,255,255],np.uint8)

    mask = cv2.inRange(hsv,lower_yellow,upper_yellow)
    edges = cv2.Canny(mask,75,250)

    lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap = 50)
    #maxlinegap değeri belirliyoruz ki aralardaki boşluklar kapansın
    #çizgi bir bütün şeklinde olsun

    for i in lines:
        x1,y1,x2,y2 = i[0]
        cv2.line(frame,(x1,y1),(x2,y2),(255,0,0),3)

    cv2.imshow("frame",frame)    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break



vid.release()
cv2.destroyAllWindows()