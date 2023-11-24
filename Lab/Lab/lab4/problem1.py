import cv2
import numpy as np

# 加载图像
img = cv2.imread('../img/Fig.png')

hsi = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, i = cv2.split(hsi)
i_eq = cv2.equalizeHist(i)
hsi_eq = cv2.merge([h, s, i_eq])
img_eq = cv2.cvtColor(hsi_eq, cv2.COLOR_HSV2BGR)

b, g, r = cv2.split(img)
b_eq = cv2.equalizeHist(b)
g_eq = cv2.equalizeHist(g)
r_eq = cv2.equalizeHist(r)
bgr_eq = cv2.merge([b_eq, g_eq, r_eq])

cv2.imshow('Original Image', img)
cv2.imshow('Equalized Image HSI', img_eq)
cv2.imshow('Equalized Image BGR', bgr_eq)
cv2.waitKey(0)


cv2.destroyAllWindows()
