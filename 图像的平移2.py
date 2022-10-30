# import cv2
# import numpy as np


# img=cv2.imread("D:\cv2\OIP-C2.jpg")
# h,w,ch=img.shape
# M=np.float32([[1,0,400],[0,1,100]])
# new=cv2.warpAffine(img,M,(w,h))

# cv2.imshow('img',img)
# cv2.imshow('new',new)
# cv2.waitKey(0)

# import cv2
# import numpy as np


# img=cv2.imread("D:\cv2\OIP-C2.jpg")
# h,w,ch=img.shape
# #M=np.float32([[1,0,400],[0,1,100]])
# M=cv2.getRotationMatrix2D((200,200),90,0.5)
# new=cv2.warpAffine(img,M,(w,h))

# cv2.imshow('img',img)
# cv2.imshow('new',new)
# cv2.waitKey(0)

from turtle import ScrolledCanvas
import cv2
import numpy as np


img=cv2.imread("D:\cv2\OIP-C2.jpg")
h,w,ch=img.shape
#M=np.float32([[1,0,400],[0,1,100]])
#M=cv2.getRotationMatrix2D((200,200),90,0.5)
src=np.float32([[400,300],[800,300],[400,1000]])
dst=np.float32([[200,400],[600,500],[150,1100]])
M=cv2.getAffineTransform(src,dst)
new=cv2.warpAffine(img,M,(w,h))

cv2.imshow('img',img)
cv2.imshow('new',new)
cv2.waitKey(0)