import numpy as np

a=np.array([1,2,3])

b=np.array([[1,2,3],[4,5,6]])
print(a)
print(b)

#定义zero矩阵
c=np.ones((640,480,3)),np.uint8
print(c)

#定义full矩阵
e=np.full((8,8,3),255,np.uint8)
print(e)
 #定义单元矩阵identity
f=np.identity(2)
print(f)

g=np.eye(5,7,k=3)
print(g)