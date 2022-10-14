import cv2

cv2.namedWindow("img",cv2.WINDOW_NORMAL)
img=cv2.imread("D:\\1.jpg")
cv2.imshow('img',img)
key=cv2.waitKey(0)
print(key)
print('q')
print(ord('q'))
if(key & 0xff==ord('q')):
    print(111)
    cv2.destroyAllWindows
