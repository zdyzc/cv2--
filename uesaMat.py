import cv2
import numpy as np

imga=cv2.imread("D:\cv2\OIP-C.jpg")
#浅拷贝
imgb=imga

#深拷贝
imgc=imga.copy()


imga[10:60,10:60]=[0,0,255]

cv2.imshow('imga',imga)
cv2.imshow('imgb',imgb)
cv2.imshow('imgc',imgc)

cv2.waitKey(0)