import cv2
import numpy as np

img=cv2.imread("D:\cv2\chess.png")

kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

dst=cv2.dilate(img,kernel,iterations=1)#iterations是腐蚀次数，主要是让白色变
dst1=cv2.erode(img,kernel,iterations=1)
cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.imshow('dst1',dst1)
cv2.waitKey(0)