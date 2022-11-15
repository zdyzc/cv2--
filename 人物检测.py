import cv2
import numpy as np

cap=cv2.VideoCapture(0)##可以是设备编号，也可以直接给视频地址

bgsubmag=cv2.bgsegm.createBackgroundSubtractorMOG()#去背景
#形态学kernel
kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))


while True:
    ret,frame=cap.read()

    if ret==True :
        
        #灰度-二值化
        cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #去噪（高斯）
        bulr=cv2.GaussianBlur(frame,(3,3),5)
        #去背景，在原始图像上去噪效果比较更好，原始图像要二值化
        mask=bgsubmag.apply(bulr)#去背景
        #腐蚀
        erode=cv2.erode(mask,kernel)
        #膨胀#可以多加几次+，iterstions=n,可以进行调试看效果
        dilate=cv2.dilate(erode,kernel)
        #闭操作，去掉物体内部小块儿#可以多进行几次，复制粘贴
        close=cv2.morphologyEx(dilate,cv2.MORPH_CLOSE,kernel)
        close=cv2.morphologyEx(dilate,cv2.MORPH_CLOSE,kernel)
        close=cv2.morphologyEx(dilate,cv2.MORPH_CLOSE,kernel)
        #
        cnts,h=cv2.findContours(close,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #
        for (i,c) in enumerate(cnts):
            (x,y,w,h)=cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

        cv2.imshow('kuangren',frame)
        cv2.imshow('erode',mask)
        cv2.imshow('dilate',mask)
        cv2.imshow('video',mask)

    key=cv2.waitKey(1)
    if(key==27):
        break
cap.release()
cv2.destroyAllWindows()


