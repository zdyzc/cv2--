import cv2
import numpy as np

black=cv2.imread("D:\cv2\OIP-C2.jpg")
new=cv2.rotate(black,cv2.ROTATE_90_CLOCKWISE)
new1=cv2.rotate(black,cv2.ROTATE_180)
new2=cv2.rotate(black,cv2.ROTATE_90_COUNTERCLOCKWISE)


cv2.imshow('black',black)
cv2.imshow('new',new)
cv2.imshow('new1',new1)
cv2.imshow('new2',new2)
cv2.waitKey(0)