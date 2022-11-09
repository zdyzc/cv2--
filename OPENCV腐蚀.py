import cv2
import numpy as np 

img=cv2.imread("D:\cv2\chess.png")#"D:\cv2\hujiao.jpg"D:\cv2\chess.png
#"D:\cv2\fushipengzhang1.jpg"
kernel=np.ones((3,3),np.uint8)
dst=cv2.erode(img,kernel,iterations=1)

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)