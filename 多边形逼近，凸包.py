import cv2
import numpy as np
def drawShape(src,points):
    i=0
    while i <len(points):
        if (i==len(points)-1):
            x,y=points[i][0]
            x1,y1=points[0][0]
            cv2.line(src,(x,y),(x1,y1),(0,255,0),1) 
        else:

            x,y=points[i][0]
            x1,y1=points[i+1][0]
            cv2.line(src,(x,y),(x1,y1),(0,255,0),1) 
        i+=1
#读文件
img=cv2.imread("D:\cv2\hand.png")
# img=cv2.imread("D:\cv2\dingmao.bmp")
print(img.shape)
#转变成单通道
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#二值化
ret,binary=cv2.threshold(gray,150,250,cv2.THRESH_BINARY)

#轮廓查找
contours,hierarchy=cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#绘制轮廓
cv2.drawContours(img,contours,0,(0,255,0),0)

# #计算面积
# area=cv2.contourArea(contours[0])
# print("area=%d"%(area))
# #计算周长
# len=cv2.arcLength(contours[0],True)#true  false  闭合 非闭合
# print("len=%d"%(len))

# print(contours)

# print(gray.shape)
# print(binary.shape)
e=30#数值越小，描边效果越好但是数据量多吃性能，相反越差
approx=cv2.approxPolyDP(contours[0],e,True)#逼近
drawShape(img,approx)

hull=cv2.convexHull(contours[0])
drawShape(img,hull)
cv2.imshow('img',img)
# cv2.imshow('bin',binary)
cv2.waitKey() 