#1.创建矩阵
# import numpy as np

# a=np.array([1,2,3])

# b=np.array([[1,2,3],[4,5,6]])
# print(a)
# print(b)

# #定义zero矩阵
# c=np.ones((640,480,3)),np.uint8
# print(c)

# #定义full矩阵
# e=np.full((8,8,3),255,np.uint8)
# print(e)
#  #定义单元矩阵identity
# f=np.identity(2)
# print(f)

# g=np.eye(5,7,k=3)
# print(g)

#//////2.检索和赋值
# from pickletools import uint8
# import numpy as np
# import cv2

# img=np.zeros((480,640,3),np.uint8)
# #从矩阵中都某个元素的值
# print(img[100,100])
# count=0
# #向矩阵中某个元素赋值
# while count<200:
#  #BGR
#     img[count,100]=[0,0,255]
#     count+=1
# cv2.imshow('img',img)
# key=cv2.waitKey(0)
# if key & 0XFF==ord('q'):
#     cv2.destroyAllWindows()


#3.获取子矩阵
from pickletools import uint8
import numpy as np
import cv2

img=np.zeros((480,640,3),np.uint8)
roi=img[100:400,100:600]
roi[:,:]=[0,0,255]
roi[10:200,10:200]=[0,255,0]
cv2.imshow('img',roi)
key=cv2.waitKey(0)
if key & 0XFF==ord('q'):
    cv2.destroyAllWindows()
