import cv2 as cv
import numpy as np

def callback(x):
    print(x)



cv.namedWindow("window4")
cv.createTrackbar("l_h","window4",0,255,callback)   ## tracker for lower value of hue
cv.createTrackbar("l_s","window4",0,255,callback)   ## tracker for lower value of saturation
cv.createTrackbar("l_v","window4",0,255,callback)   ## tracker for lower value of value
cv.createTrackbar("u_h","window4",255,255,callback)   ## tracker for upper value of hue
cv.createTrackbar("u_s","window4",255,255,callback)   ## tracker for upper value of saturation
cv.createTrackbar("u_v","window4",255,255,callback)   ## tracker for upper value of value




while(1):
    img = cv.imread("smarties.png")
    hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    l_h = cv.getTrackbarPos("l_h", "window4")
    l_s = cv.getTrackbarPos("l_s", "window4")
    l_v = cv.getTrackbarPos("l_v", "window4")
    u_h = cv.getTrackbarPos("u_h", "window4")
    u_s = cv.getTrackbarPos("u_s", "window4")
    u_v = cv.getTrackbarPos("u_v", "window4")
    l_b=np.array([l_h,l_s,l_v])
    u_b=np.array([u_h,u_s,u_v])
    mask=cv.inRange(hsv,l_b,u_b)  # mask is always defined as cv.inrange(src,lowbound,hihbound)
    res=cv.bitwise_and(img,img,mask=mask)


    cv.imshow("window",img)
    cv.imshow("window2",mask)
    cv.imshow("window3",res)
    k=cv.waitKey(1)
    if k==27:
        break
"""
cap=cv.VideoCapture(0)
while(1):
    ret,img=cap.read()
    hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    l_b=np.array([110,50,50])
    u_b=np.array([130,255,255])
    mask=cv.inRange(hsv,l_b,u_b)  # mask is always defined as cv.inrange(src,lowbound,hihbound)
    res=cv.bitwise_and(img,img,mask=mask)


    cv.imshow("window",img)
    cv.imshow("window2",mask)
    cv.imshow("window3",res)
    k=cv.waitKey(1)
    if k==27:
        break
        """
cv.destroyAllindows()
