import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread(r"C:\Users\Shivam Sundram\OneDrive\pp\IMG-20201203-WA0116-COLLAGE.jpg")

#edge detction using laplacian derivative

lap=cv.Laplacian(img,cv.CV_64F,ksize=3)
lap=np.uint8(np.absolute(lap))

# sobel x and sobel y

sobelx=cv.Sobel(img,cv.CV_64F,1,0)
sobely=cv.Sobel(img,cv.CV_64F,0,1)

sobelx=np.uint8(np.abs(sobelx))
sobely=np.uint8(np.abs(sobely))

# sobel x and y combined

sobel_xy=cv.bitwise_or(sobelx,sobely)

title=["lap","sobelx","sobely","sobelxy"]
images=[lap,sobelx,sobely,sobel_xy]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i])
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

plt.imshow(sobel_xy)
plt.xticks([])
plt.yticks([])
plt.show()

#---------------------------------------------------
# edge detection sobelxy in video

cap=cv.VideoCapture(0)

while(1):
    ret,img=cap.read()
    sobelx = cv.Sobel(img, cv.CV_64F, 1, 0)
    sobely = cv.Sobel(img, cv.CV_64F, 0, 1)

    sobelx = np.uint8(np.abs(sobelx))
    sobely = np.uint8(np.abs(sobely))
    sobel_xy = cv.bitwise_or(sobelx, sobely)
    cv.imshow("sobelxy",sobel_xy )
    cv.imshow("no-filter",img)
    k=cv.waitKey(1)
    if k==27:
        break
cv.destroyAllWindows()

##P.S. IT WORKS '''''''''''HAPPY FEELING''''''''''''