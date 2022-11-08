import cv2
import numpy as np


img=cv2.imread("D:\cv2\chess.png")

#s索贝尔算子y方向边缘
# d1=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
d1=cv2.Scharr(img,cv2.CV_64F,1,0)#沙尔
#x方向边缘
# d2=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
d2=cv2.Scharr(img,cv2.CV_64F,0,1)#沙尔


#拉普拉斯
ldst=cv2.Laplacian(img,cv2.CV_64F,ksize=5)#这个会刚清晰一点，据观察

#两张图片合在一块儿
dst=d1+d2#Python
dst2=cv2.add(d1,d2)
#我把两个方向一块
d3=cv2.Sobel(img,cv2.CV_64F,1,1,ksize=5)#实验很明显，这个方法效果并不好，最好分开方向，在做相加

cv2.imshow('img',img)
cv2.imshow('d1',d1)
cv2.imshow('d2',d2)
cv2.imshow('d3',d3)
cv2.imshow('dst',dst)
cv2.imshow('dst2',dst2)
cv2.imshow('ldst',ldst)

cv2.waitKey(0)