import cv2 as cv

img= cv.imread("messi5.jpg")
img2= cv.imread("opencv-logo.png")

print(img2.shape)  ## returns shape height width and channel(3 for colored only one for grayscale)
print(img2.size)   ## returns the no. pixels

b,g,r=cv.split(img)  ## splitting in 3 components for an colored image
img=cv.merge((b,g,r)) ## merging the 3 components


"""ROI is one of the most handy things is to get a portion of image by slicing
the original array and then placing the slice over some other position in the 
array of image"""

object=img[280:340,330:390] ## copying a section of image from array in this case the region ball is present
img[273:333,100:160]=object ## placig thet section over some other place in the image \

cv.imshow("window",img)
cv.waitKey(0)
cv.destroyAllWindows()


"""for adding 2 images there is no complexity simply cv.add(img,img2) will work
even for weighted add cv.addweighted(img,ratio1,img2,ratio2) will agaian work


but the complexity lies in the fact that image should be of same size so 
cv,resize(array,(dimension)) should be used"""

img=cv.resize(img,(512,512))
img2=cv.resize(img2,(512,512))   ## resizing before adding

add=cv.add(img,img2)             ## simple add
wadd=cv.addWeighted(img,0.8,img2,0.2,0) ## wighted add

cv.imshow("window2",add)
cv.imshow("window3",wadd)
cv.waitKey(0)
cv.destroyAllWindows()
