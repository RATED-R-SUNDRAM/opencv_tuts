import numpy as np
import cv2 as cv

"""we will do two things
* on a black screen increase trackbar of b,g,r and change its color
* for an image change its gray scale and color by a switch trackbar with a no. given by another trckbar"""


def callback(x): # the call back function usually of this stature
    print(x)
"""

img = cv.imread("lena.jpg")
cv.namedWindow("window")
cv.createTrackbar("B","window",0,255,callback)  ### creating trackar with 5 params and including  a call back
cv.createTrackbar("G","window",0,255,callback)   
cv.createTrackbar("R","window",0,255,callback)

while(1):
    cv.imshow("window",img)
    k=cv.waitKey(1)      # wait key is 1 as it wait for 1 sec and the loop starts again
    if k==27:
        break
    img[:]=[cv.getTrackbarPos("B","window"),cv.getTrackbarPos("G","window"),cv.getTrackbarPos("R","window")]  # updating colors in the image 


"""

cv.namedWindow("window1")


cv.createTrackbar("switch","window1",0,1,callback)
cv.createTrackbar("value","window1",0,1000,callback)
while(1):

    """the logic of the loop here is in each time in the loop we read rthe array from the iamge
    and each time based on the value of switch we do conversion to grey
    """
    img = cv.imread("lena.jpg")
    if cv.getTrackbarPos("switch","window1")==1:
        img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    else:
        pass
    pos=str(cv.getTrackbarPos("value","window1"))
    img = np.array(img)
    cv.putText("img",pos, (25, 20), cv.FONT_HERSHEY_DUPLEX, 3, (200, 150, 100))
    cv.imshow("window1", img)
    k = cv.waitKey(1)
    if k == 27:
        break



cv.destroyAllWindows()