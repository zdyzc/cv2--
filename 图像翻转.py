from multiprocessing.connection import wait
import cv2
import numpy as np

img=cv2.imread("D:\cv2\OIP-C2.jpg")
new=cv2.flip(img,0)
new1=cv2.flip(img,1)
new2=cv2.flip(img,-1)

cv2.imshow('img',img)
cv2.imshow('new',new)
cv2.imshow('new1',new1)
cv2.imshow('new2',new2)
cv2.waitKey(0)