from unittest import result
import cv2
import numpy as np

tiankong=cv2.imread("D:\cv2\OIP-C.jpg")

#图的加法运算就是矩阵的加法运算
#因此，加法运算两张图必须是相等的
#print(tiankong.shape)

img=np.ones((234,332,3),np.uint8)*120
cv2.imshow('orig',tiankong)

result=cv2.add(tiankong,img)
cv2.imshow('result',result)
cv2.waitKey(0)