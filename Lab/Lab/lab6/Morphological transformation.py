import cv2
import numpy as np

img = cv2.imread('../img/lab6_1.png', 0)
img2 = cv2.imread('../img/lab6_2.png', 0)
img3 = cv2.imread('../img/lab6_3.png', 0)
kernel = np.ones((5, 5), np.uint8)
# 腐蚀erode
erosion = cv2.erode(img, kernel, iterations=1)
cv2.imshow('erosion', erosion)
cv2.resizeWindow('erosion', 300, 300)
# 膨胀dilate
dilation = cv2.dilate(img, kernel, iterations=1)
cv2.imshow('dilation', dilation)
cv2.resizeWindow('dilation', 300, 300)
# 形态学开操作：先腐蚀再膨胀
opening = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel)
cv2.imshow('opening', opening)
cv2.resizeWindow('opening', 300, 300)
# 形态学闭操作：先膨胀再腐蚀
closing = cv2.morphologyEx(img3, cv2.MORPH_CLOSE, kernel)
cv2.imshow('closing', closing)
cv2.resizeWindow('closing', 300, 300)
# 形态学梯度操作：膨胀的图像减去腐蚀的图像
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('gradient', gradient)
cv2.resizeWindow('gradient', 300, 300)
cv2.waitKey(0)
