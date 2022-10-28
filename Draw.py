from dataclasses import asdict
from pickletools import uint8
import cv2
import numpy as np

img=np.zeros((480,640,3),np.uint8)

#画线，坐标点(x,y)

# cv2.line(img,(0,0),(480,640),(101,200,122),5,0)
# cv2.line(img,(0,0),(300,640),(0,0,255),1,666666)

#画矩形
cv2.rectangle(img,(10,10),(100,100),(0,0,255),-1)

#画圆形
cv2.circle(img,(320,240),100,(0,0,255))
cv2.circle(img,(320,240),5,(0,0,255),-1)

#画椭圆\
#度数是顺时针的
#0度从左侧开始
cv2.ellipse(img,(320,240),(100,50),90,0,360,(0,0,255),-1)

#画多边形
pts=np.array([(300,10),(150,100),(450,100)],np.int32)
cv2.polylines(img,[pts],True,(66,60,255))

#填充多边形
# cv2.fillPoly(img,[pts],(255,255,255))

#绘制文本
cv2.putText(img,"Hellow World!",(10,400),cv2.FONT_HERSHEY_COMPLEX_SMALL,3,(250,0,0))

cv2.imshow('draw',img)


cv2.waitKey(0)
