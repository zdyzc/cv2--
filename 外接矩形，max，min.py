import cv2
import numpy as np
def drawShape(src,points):
    i=0
    while i <len(points):
        if (i==len(points)-1):
            x,y=points[i][0]
            x1,y1=points[0][0]
            cv2.line(src,(x,y),(x1,y1),(0,255,0),1) 
        else:

            x,y=points[i][0]
            x1,y1=points[i+1][0]
            cv2.line(src,(x,y),(x1,y1),(0,255,0),1) 
        i+=1
#读文件
img=cv2.imread("D:\cv2\hello.jpeg")
# img=cv2.imread("D:\cv2\dingmao.bmp")
print(img.shape)
#转变成单通道
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#二值化
ret,binary=cv2.threshold(gray,150,250,cv2.THRESH_BINARY)

#轮廓查找
contours,hierarchy=cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#绘制轮廓
cv2.drawContours(img,contours,0,(0,255,0),0)


r=cv2.minAreaRect(contours[1])
box=cv2.boxPoints(r)
box=np.int0(box)
cv2.drawContours(img,[box],0,(0,255,0),2)


x,y,w,h=cv2.boundingRect(contours[1])
cv2.rectangle(img,(x,y),(x+w,x+h),(255,0,0),2)

cv2.imshow('img',img)
cv2.waitKey() 