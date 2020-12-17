import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img=cv.imread("lena.jpg")

#gaussian pyramid ( cv.pyrDown(img) and cv.PyrUp(img) )

# expanding one level an image of one level compressed wont give same results.
# as information is lossed during compression

ld1=cv.pyrDown(img)
lu1=cv.pyrUp(ld1)

title=["original","one level up","expanded for one level up"]
images=[img,ld1,lu1]

for i in range(3):

    cv.imshow("window"+str(i+1),images[i])
    cv.waitKey(0)
    cv.destroyAllWindows()

#laplacian pyramid
# diff in image and expanded version of compressed version

lappy=cv.subtract(img,lu1)
cv.imshow("lap pyramid",lappy)
cv.waitKey(0)
cv.destroyAllWindows()
