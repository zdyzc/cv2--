import cv2

def callback():
    pass

cv2.namedWindow('color',cv2.WINDOW_AUTOSIZE)

img=cv2.imread("D:\cv2\OIP-C.jpg")
colorspaces=[cv2.COLOR_BGR2RGBA,cv2.COLOR_BAYER_BG2BGRA,cv2.COLOR_BAYER_BG2GRAY,cv2.COLOR_BGR2HSV_FULL,cv2.COLOR_BGR2YUV]
cv2.createTrackbar('curcolor','color',0,len(colorspaces),callback)
while True:
    v=cv2.getTrackbarPos('curcolor','color')
    #颜色空间转换API
    cvt_img=cv2.cvtColor(img,colorspaces[v])
    cv2.imshow('color',img)
    key=cv2.waitKey(10)
    if key & 0xff==ord('q'):
        break
cv2.destroyAllWindows()