import cv2
import numpy as np

frame = cv2.imread('../img/lab6_problem.jpg')
frame = cv2.resize(frame, (300, 300))
# 转换到HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# 设定蓝色的阈值
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])
# 根据阈值构建掩模
mask = cv2.inRange(hsv, lower_blue, upper_blue)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
mask = cv2.erode(mask, kernel)
mask = cv2.dilate(mask, kernel, iterations=2)
mask = cv2.erode(mask, kernel)

edge = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('edge1', edge)
frame_edge = np.copy(frame)

for i in range(frame_edge.shape[0]):
    for j in range(frame_edge.shape[1]):
        if edge[i][j] > 0:
            frame_edge[i][j] = [0, 0, 255]

row, col = np.where(edge > 0)

min_row = np.min(row)
min_col = np.min(col)
max_row = np.max(row)
max_col = np.max(col)

cv2.rectangle(frame_edge, (min_col, min_row), (max_col, max_row), color=(0,255,0), thickness=5)

# 对原图像和掩模进行位运算
res = cv2.bitwise_and(frame, frame, mask=mask)

# 显示图像
cv2.imshow('frame', frame)
cv2.resizeWindow('frame', 300, 300)
cv2.imshow('mask', mask)
cv2.resizeWindow('mask', 300, 300)
cv2.imshow('res', res)
cv2.resizeWindow('res', 300, 300)
cv2.imshow('edge', frame_edge)
cv2.resizeWindow('edge', 300, 300)

cv2.waitKey(0)
# 关闭窗口
cv2.destroyAllWindows()
