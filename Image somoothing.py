import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread("opencv-logo.png")

#homogneous filter    (averge of neighbouring kernels)
kernel=np.array((5,5),np.float32)/25
homo_filter=cv.filter2D(img,-1,kernel=kernel)

#blur
blur=cv.blur(img,(5,5))

# gaussian blur   (central have higher weights)
gaus_blur=cv.GaussianBlur(img,(5,5),0)

#median blur (best for salt and pepper noise)
median_blur=cv.medianBlur(img,5)

# bilateral blur ( best for edge smoothing)
bilateral_blur= cv.bilateralFilter(img,9,75,75)

title=["homogeneous filter","blur","gaussian blur","median blur","bilateral blur"]
images=[homo_filter,blur,gaus_blur,median_blur,bilateral_blur]

for i in range(5):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

#-------------------------------------------------------------------------------------------------------
# trying to smooth corner  in videos

cap=cv.VideoCapture(0)

while(1):
    ret,frame=cap.read()
    frame2=cv.bilateralFilter(frame,9,75,75)
    cv.imshow("filter", frame2)
    cv.imshow("no-filter",frame)
    k=cv.waitKey(1)
    if k==27:
        break
cv.destroyAllWindows()

##P.S. IT WORKS '''''''''''HAPPY FEELING''''''''''''