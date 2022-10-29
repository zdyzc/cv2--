import cv2
import numpy as np

black = cv2.imread("D:\cv2\OIP-C2.jpg")
new=cv2.resize(black,None,fx=2,fy=2)

print(black.shape)

cv2.imshow('black',black)
cv2.imshow('new',new)
cv2.waitKey(0)