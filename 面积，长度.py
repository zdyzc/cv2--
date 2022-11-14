import cv2
import numpy as np
#读文件
img=cv2.imread("D:\cv2\OIP-C11111.jfif")
# img=cv2.imread("D:\cv2\dingmao.bmp")
print(img.shape)
#转变成单通道
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#二值化
ret,binary=cv2.threshold(gray,150,250,cv2.THRESH_BINARY)

#轮廓查找
contours,hierarchy=cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#绘制轮廓
cv2.drawContours(img,contours,-1,(0,255,0),0)

#计算面积
area=cv2.contourArea(contours[0])
print("area=%d"%(area))
#计算周长
len=cv2.arcLength(contours[0],True)#true  false  闭合 非闭合
print("len=%d"%(len))

# print(contours)

# print(gray.shape)
# print(binary.shape)


# cv2.imshow('img',img)
# cv2.imshow('bin',binary)
# cv2.waitKey() 