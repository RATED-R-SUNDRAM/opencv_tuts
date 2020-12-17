import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

img2= cv.imread("smarties.png")
img=cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

_,b_img=cv.threshold(img,220,225,cv.THRESH_BINARY_INV)

kernel=np.ones((5,5),np.uint8)
dilation=cv.morphologyEx(b_img,cv.MORPH_DILATE,kernel=kernel,iterations=1)
erosion=cv.morphologyEx(b_img,cv.MORPH_ERODE,kernel=kernel,iterations=1)
opening=cv.morphologyEx(b_img,cv.MORPH_OPEN,kernel=kernel,iterations=1)
closing=cv.morphologyEx(b_img,cv.MORPH_CLOSE,kernel=kernel,iterations=1)
gradient=cv.morphologyEx(b_img,cv.MORPH_GRADIENT,kernel=kernel,iterations=1)
tophat=cv.morphologyEx(b_img,cv.MORPH_BLACKHAT,kernel=kernel,iterations=1)

title=["dilation","erosion","opening","closing","gradient","tophat"]
images=[dilation,erosion,opening,closing,gradient,tophat]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],"gray")
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])
plt.show()