import cv2
import numpy as np
#读文件
img=cv2.imread("D:\cv2\dog.jpeg")
print(img.shape)
#转变成单通道
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#二值化
ret,binary=cv2.threshold(gray,150,250,cv2.THRESH_BINARY)

#轮廓查找
contours,hierarchy=cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(contours)

print(gray.shape)
print(binary.shape)


cv2.imshow('img',img)
cv2.imshow('bin',binary)
cv2.waitKey()