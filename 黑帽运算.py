import cv2
import numpy as np

img=cv2.imread("D:\cv2\dotinj.png")
kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))


dst=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey()