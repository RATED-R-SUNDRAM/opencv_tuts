import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img=cv.imread("messi5.jpg")

#canny edge detection works by 5 steps edge detection

#GAUSSIAN FILTER
#GRADIENT CIRCULATION
#NON-MAXIMUM SUPRESSOR
#DOUBLE THRESHOLD
#EDGE DETECTION BY HYSTEREIS

canny=cv.Canny(img,10,200) ## threshold 1 and threshold 2 are provided manually add a trackbar for this

plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.show()
plt.imshow(canny)
plt.xticks([])
plt.yticks([])
plt.show()