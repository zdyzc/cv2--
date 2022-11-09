import cv2
import numpy as np

img=cv2.imread("D:\cv2\chess.png")

kernel=cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))
kernel1=cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
kernel2=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
print(kernel)
print(kernel1)
print(kernel2)
dst=cv2.erode(img,kernel,iterations=6)#iterations是腐蚀次数，主要是让白色变少成为黑色

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)