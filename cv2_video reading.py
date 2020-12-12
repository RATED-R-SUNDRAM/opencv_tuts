import cv2

cap=cv2.VideoCapture(0) ##cap var is storing cv2.Videocapture() param is camera index try 0 or -1
fourcc= cv2.VideoWriter_fourcc(*'XVID')     # 2nd param of out
out=cv2.VideoWriter("thir_VIDEO.avi",fourcc,20.0,(640,480))  # out is cv2.videoWriter which has 4 params name fourcc,frames/sec,size

while(True):
    ret,frame = cap.read()    # cap.read() returns return value t or f in ret and frame array in frame
    cv2.imshow("WINDOW NAME", frame)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("WINDOW NAME", gray)
    out.write(gray)  # writing frame in output could have also wrote frame  one line above

    k=cv2.waitKey(0)
    if k==27:

        break

cap.release()
out.release()
cv2.destroyAllWindows()



