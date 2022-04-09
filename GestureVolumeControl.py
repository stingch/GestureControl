import cv2
import time
import numpy as np

### parameters ###
wCam, hCam = 640, 480   # 影像的寬、高
previous_time = 0 # 用來計算fps的參數

# 設定串流畫面
cap = cv2.VideoCapture(0)   # 設定串流的相機，預設為0
cap.set(3, wCam)    # 3代表設定的是串流影像的寬度
cap.set(4, hCam)    # 4代表設定的是串流影像的高度


while True:
    succes, img = cap.read()
    current_time = time.time()  # 用來計算fps的參數
    fps = (1 / current_time - previous_time)   # 計算兩次迴圈執行的時間差
    previous_time = current_time
    cv2.putText(img, f'FPS:{int(fps)}', (40, 50), cv2.FONT_HERSHEY_SIMPLEX,
     1, (97, 108, 110), 2)  # cv2.putText(影像, 文字, 座標, 字型, 大小, 顏色, 線條寬度)
     