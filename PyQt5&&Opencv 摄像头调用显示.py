import sys
import cv2
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy


class videoWidget(QWidget):
    """
    窗口类：定义了窗口里有哪些组件
    """
    def __init__(self):
        super().__init__()
        # 状态变量
        self.inverse = False  # 镜像标记（False表示不镜像，True表示镜像）
        self.gray = False     # 灰度标记（False表示彩色，True表示灰度）

        # 布局定义
        self.main_layout = QHBoxLayout()   # 定义水平布局
        self.left_layout = QVBoxLayout()   # 定义左栏布局
        self.right_layout = QVBoxLayout()  # 定义右栏布局
        self.spacer_1 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)  # 弹簧（用来垂直压缩组件）

        # 组件定义
        self.video_label = QLabel()        # 定义放图像的标签组件
        self.btn_inverse = QPushButton()   # 定义镜像切换按钮
        self.btn_gray = QPushButton()      # 定义彩色/灰度切换按钮

        # 初始化界面布局
        self.setLayout(self.main_layout)   # 将布局应用到窗口
        self.main_layout.addLayout(self.left_layout)   # 将左栏布局加入主布局
        self.main_layout.addLayout(self.right_layout)  # 将右栏布局加入主布局
        self.left_layout.addWidget(self.video_label)   # 将标签组件加入左栏布局
        self.right_layout.addItem(self.spacer_1)       # 将弹簧加入右栏布局，它会把右栏布局的组件往下压
        self.right_layout.addWidget(self.btn_inverse)  # 将镜像切换按钮加入右栏布局
        self.right_layout.addWidget(self.btn_gray)     # 将彩色/灰度切换按钮加入右栏布局

        # 设置按钮文字
        self.btn_inverse.setText("镜像切换")
        self.btn_gray.setText("灰度图像")

        # 连接按钮触发函数
        self.btn_inverse.clicked.connect(self.btn_inverse_clicked)
        self.btn_gray.clicked.connect(self.btn_gray_clicked)

    # 镜像切换按钮触发函数
    def btn_inverse_clicked(self):
        self.inverse = not self.inverse  # 反转镜像标记

    # 彩色/灰度切换按钮触发函数
    def btn_gray_clicked(self):
        self.gray = not self.gray        # 反转灰度标记


if __name__ == "__main__":
    app = QApplication(sys.argv)  # qt应用入口
    widget = videoWidget()        # 定义窗口
    widget.show()                 # 显示窗口
    cap = cv2.VideoCapture(0)     # 开启0号摄像头（如果电脑只有一个摄像头就是0号，多个摄像头分别是0,1,2...）
    while cap.isOpened():         # 循环读入每帧画面
        ret, img = cap.read()     # 读入图像 ret表示是否正确读入(bool)，img为读入的图像
        if widget.inverse:        # 如果镜像标记是True
            img = cv2.flip(img, 1)  # 翻转图片
        if widget.gray:           # 如果灰度标记是True
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 将图片转为灰度
            widget.video_label.setPixmap(QPixmap.fromImage(QImage(img, img.shape[1], img.shape[0], QImage.Format_Grayscale8)))  # 在标签中插入灰度图片
        else:
            widget.video_label.setPixmap(QPixmap.fromImage(QImage(img, img.shape[1], img.shape[0], QImage.Format_BGR888)))  # 在标签中插入彩色图片
        cv2.waitKey(1)            # 等待1ms（cap.read()的时候也会等待到收到最新帧）
    app.exec()                    # qt应用结束
