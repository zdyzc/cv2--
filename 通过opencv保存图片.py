import cv2
cv2.namedWindow("img",cv2.WINDOW_NORMAL)
img=cv2.imread("D:\\1.jpg")

while True:
    cv2.imshow('img',img)


    key = cv2.waitKey(0)

    if(key & 0xff==ord('q')):
        break
    elif(key & 0xff==ord('s')):
        cv2.imwrite("D:\\123.png",img)
cv2.destroyAllWindows