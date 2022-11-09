import cv2
import numpy as np

img=cv2.imread("D:\cv2\j.png")
kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))#3*3效果看起来好一点


dst=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)