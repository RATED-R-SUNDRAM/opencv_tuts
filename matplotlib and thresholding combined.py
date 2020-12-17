import matplotlib.pyplot as plt
import cv2 as cv
"""
img=cv.imread("lena.jpg")
cv.imshow("window",img)

img=cv.cvtColor(img,cv.COLOR_BGR2RGB) ### converted the image from bgr to rgb as matplotlib reads in rgb format and cv.imshow reads in bgr format
cap=cv.VideoCapture(0)
plt.imshow(img)  # we have used plt.imshow() not not not plt.plot()
plt.show()       # for roi now we dont have to worry about cordinates it will be eaily done as in matplotlib it is shown

cv.waitKey(0)
cv.destroyAllWindows()
"""

#----------------------------------------------------------
# implementation of thresholding  using cordinates from matplotlib

img=cv.imread("gradient.png")

_,th1=cv.threshold(img,127,255,cv.THRESH_BINARY)
_,th2=cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
_,th3=cv.threshold(img,127,255,cv.THRESH_TRUNC)
_,th4=cv.threshold(img,127,255,cv.THRESH_TOZERO)
_,th5=cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)


title=["BINARY","BINARY INV","TRUNC","TOZERO","TOZERO INV"]
array=[th1,th2,th3,th4,th5]

for i in range(5):
    plt.subplot(2,3,i+1)
    plt.imshow(array[i],"gray")
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])
plt.show()