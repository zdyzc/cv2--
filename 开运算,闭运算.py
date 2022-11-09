import cv2
import numpy as np

img=cv2.imread("D:\cv2\dotinj.png")
img1=cv2.imread("D:\cv2\j.png")
kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))

# dst=cv2.dilate(img,kernel,iterations=1)#iterations是腐蚀次数，主要是让白色变
# dst1=cv2.erode(img,kernel,iterations=1)

dst1=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
dst2=cv2.morphologyEx(img1,cv2.MORPH_OPEN,kernel)
cv2.imshow('img',img)
cv2.imshow('img',img1)
#cv2.imshow('dst',dst)
cv2.imshow('dst1',dst1)#闭运算
cv2.imshow('dst2',dst2)#开运算
cv2.waitKey(0)