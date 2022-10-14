from ipaddress import v4_int_to_packed
import cv2
from cv2 import waitKey

#创建VideoWriter媒体文件
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
vw=cv2.VideoWriter('D:\\cv2\\out.mp4',fourcc,25,(640,480))

#创建窗口()
cv2.namedWindow("video",cv2.WINDOW_NORMAL)

##将窗口重新设定大小
cv2.resizeWindow("video",640,480)
 
#获取视频设备/从视频文件中读取视频帧

cap =cv2.VideoCapture(0)

##判断摄像头是否非打开状态
while cap.isOpened:
    #从摄像头读视频帧
    ret,frame =cap.read()
    
    if ret==True:
        #将视频帧在窗口中显示
        cv2.imshow("video",frame)
        cv2.resizeWindow("video",640,480)

        #写数据到多媒体文件
        vw.write(frame)
        
        #等待键盘事件，如果为q，退出
        key = waitKey(1)
        if(key & 0xFF==ord('q')):
            break
    else:
        break
#释放VideoCapture
cap.release()

#释放videoWriter
vw.release()

cv2.destroyAllWindows