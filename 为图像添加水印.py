#1.引入一张图片
#2.要有一个logo，需要自己创建
#3.计算图片在什么地方添加，在添加的地方要变成黑色
#4.利用add，将logo与图处叠加到一起

import cv2
import numpy as np
#导入图片
imgback=cv2.imread("D:\cv2\OIP-C2.jpg")

#创建LOGO和mask
logo=np.zeros((200,200,3),np.uint8)
mask=np.zeros((200,200),np.uint8)

#绘制logo
logo[20:120,20:120]=[0,0,255]
logo[80:180,80:180]=[255,0,0]

mask[20:120,20:120]=255
mask[80:180,80:180]=255

#对mask按位求反
m=cv2.bitwise_not(mask)

#选择图片添加logo位置
roi=imgback[0:200,0:200]

#与m进行与操作
tmp=cv2.bitwise_and(roi,roi,mask=m)

dst=cv2.add(tmp,logo)

imgback[0:200,0:200]=dst

cv2.imshow('imgback',imgback)
cv2.imshow('dst',dst)
cv2.imshow('tmp',tmp)
cv2.imshow('m',m)
cv2.imshow('mask',mask)
cv2.imshow("logo",logo)

cv2.waitKey(0)