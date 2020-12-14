import cv2

cap=cv2.VideoCapture(0) ##cap var is storing cv2.Videocapture() param is camera index try 0 or -1
fourcc= cv2.VideoWriter_fourcc(*'XVID')     # 2nd param of out

while(True):
    ret,frame = cap.read()    # cap.read() returns return value t or f in ret and frame array in frame
    cv2.imshow("WINDOW NAME", frame)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    object= gray[250:350,100:260]    ### selecting a region of our intrest
    """placing that particular section of video at 3 differrent places """
    gray[0:100,0:160] = object
    gray[350:450, 160:320] = object
    cv2.imshow("WINDOW NAME", gray)



    k=cv2.waitKey(1)
    if k==27:

        break

cap.release()

cv2.destroyAllWindows()