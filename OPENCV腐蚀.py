import cv2
import numpy as np 

img=cv2.imread("D:\cv2\chess.png")#"D:\cv2\hujiao.jpg"D:\cv2\chess.png
#"D:\cv2\fushipengzhang1.jpg"
kernel=np.ones((3,3),np.uint8)
dst=cv2.erode(img,kernel,iterations=6)#iterations是腐蚀次数，主要是让白色变少成为黑色

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)