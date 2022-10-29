import cv2
import numpy as np

back=cv2.imread("D:\cv2\OIP-C.jpg")
img0=cv2.imread("D:\cv2\OIP-C22.jpg")

#只有两张图片属性是一样的才可以进行融合
print(back.shape)
print(img0.shape)

result=cv2.addWeighted(img0,0.7,back,0.3,0)
cv2.imshow('add2',result)
cv2.waitKey(0)