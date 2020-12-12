import cv2

img= cv2.imread('lena.jpg',1)

img =cv2.line(img,(0,0),(2550,2550),(0,255,0),5) #cv2.line takes array and returns an array with line from cordinates color and thickness

img=cv2.arrowedLine(img,(100,100),(200,100),(100,100,100),4)## same as line just with an arrow

img=cv2.rectangle(img,(100,0),(0,100),(255,255,0),3) # drawing a rectangle with params imag initial and final cordinates,color and thickness
""" if in a closed fig thickness is -1 then that will be filled """

img=cv2.circle(img,(30,50),25,(200,100,155),-1)# again circle with params imag array and center and radius with color and thickness
"""since thickness is -1 so it will be filled """

img=cv2.putText(img,"SEXY BITCH",(10,500),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),10)


cv2.imshow("window name",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#--------------------------------------------------------------------------------------------
""" below is one example of using put text on the image or video we will now do a video display with data and time on it"""
import datetime

cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')   #### cv2.videowriter_fourcc
out=cv2.VideoWriter("trail.avi",fourcc,20,(640,480))#### no use of write just for practise i have included fourcc and out

cap.set(3,1280) ## cap.set(3,value) will set the width
cap.set(4, 720) ## cap.set(4,value) will set the height
while(cap.isOpened()):
    ret,frame=cap.read()

    text=str(datetime.datetime.now())


    cv2.putText(frame,text,(20,50),cv2.FONT_HERSHEY_DUPLEX,2,(100,200,250),2)
    cv2.imshow("windows",frame)
    k=cv2.waitKey(1)
    if k==27:
        break

cv2.destroyAllWindows()
