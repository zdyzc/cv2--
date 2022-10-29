import cv2
import numpy as np

#创建一张图片
img=np.zeros((200,200),np.uint8)
img2=np.zeros((200,200),np.uint8)

img[20:120,20:120]=255
img2[80:180,80:180]=255

#非
#new_img=cv2.bitwise_not(img)

#与
new_img=cv2.bitwise_xor(img,img2)


cv2.imshow('img',img)
cv2.imshow('img2',img2)
cv2.imshow('new_img',new_img)
cv2.waitKey(0)