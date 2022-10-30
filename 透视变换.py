import cv2
import numpy as np

src=np.float32([[10,110],[210,110],[0,400],[250,390]])
dst=np.float32([[0,0],[230,1],[0,300],[230,300]])

img=cv2.imread("D:\cv2\R-C.jpg")

M=cv2.getPerspectiveTransform(src,dst)

new=cv2.warpPerspective(img,M,(230,300))


cv2.imshow('Orign',img)
cv2.imshow('New',new)
cv2.waitKey(0)

#实际上就是切割图像重新展示