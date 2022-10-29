import cv2
import numpy as np


img=cv2.imread("D:\cv2\OIP-C2.jpg")
h,w,ch=img.shape
M=np.float32([[1,0,400],[0,1,100]])
new=cv2.warpAffine(img,M,(w,h))

cv2.imshow('img',img)
cv2.imshow('new',new)
cv2.waitKey(0)