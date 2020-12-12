import cv2

img= cv2.imread("lena.jpg",1) # cv2.imread reades params are name and flag 0 for gs 1 for color -1 for as it is

print(img)   # print array of pixels

cv2.imshow("WINDOW NAME 1",img) # for showing we us eimshow with param are window name and  array
## if only till this then it will dissapear very quickly

k=cv2.waitKey(0)## wait for 5000 miliseconds if its 0 then forever till we close
if k==27:
    cv2.destroyAllWindows()## after waiting destroy all windows
elif k==ord('s'):
    cv2.imwrite("sexy.png",img)## for writing image we need to pass image name and array of ppi
    cv2.destroyAllWindows()
