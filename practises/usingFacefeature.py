from cv2 import cv2
import numpy as np 

def findMaxContour(x):
    max_i = 0
    max_area = 0

    for i in range(len(x)):
        area_face = cv2.contourArea(x[i])
        if max_area < area_face:
            max_area = area_face
            max_i = i

    try:
        cnt = x[max_i]
    except:
        x = [0]
        cnt = x[0]
    
    return cnt

cap = cv2.VideoCapture(0)

while 1:
    _,frame = cap.read()
    frame = cv2.flip(frame,1)

    roi = frame[50:350,200:400] #[y1:y2,x1:x2]

    cv2.rectangle(frame,(200,50),(400,350),(0,0,255),0)

    hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    lower_color = np.array ([0,45,79],dtype=np.uint8)
    upper_color = np.array ([17,255,255],dtype=np.uint8)

    mask = cv2.inRange(hsv,lower_color,upper_color)
    kernel = np.ones((3,3),np.uint8)
    mask = cv2.dilate(mask,kernel,iterations=1)
    mask = cv2.medianBlur(mask,15)

    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) >0:
        try:
            c = findMaxContour(contours)
            extLeft = tuple(c[c[:,:, 0].argmin()][0])
            extRight = tuple(c[c[:,:, 0].argmax()][0])
            extTop = tuple(c[c[:,:, 1].argmin()][0])
            extBottom =tuple(c[c[:,:, 1].argmax()][0])

            cv2.circle(roi,extLeft,5,(0,255,0),2)
            cv2.circle(roi,extRight,5,(0,255,0),2)
            cv2.circle(roi,extTop,5,(0,255,0),2)
            cv2.circle(roi,extBottom,5,(0,255,0),2)

            cv2.line(roi,extLeft,extTop,(0,255,0),2)
            cv2.line(roi,extTop,extRight,(0,255,0),2)
            cv2.line(roi,extRight,extBottom,(0,255,0),2)
            cv2.line(roi,extBottom,extLeft,(0,255,0),2)
        except:
            pass
    else:
        pass        
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
    
    cv2.imshow("frame",frame)
    cv2.imshow("maskroi",mask)
    
cap.release()
cv2.destroyAllWindows()