import cv2
import numpy as np


img =cv2.imread("D:\cv2\math1.png")

img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#彩色图像转化为灰度图

ret,dst=cv2.threshold(img1,100,255,cv2.THRESH_BINARY)#RY_INV可以白黑转化颠倒

cv2.imshow('img',img)
cv2.imshow('gray',img1)
cv2.imshow('bin',dst)
cv2.waitKey(0)