import numpy as np
import cv2

img = cv2.imread('../img/gray_img1.jpg', 0)
img1 = cv2.add(img, 80)
img2 = cv2.subtract(img, 80)
img3 = cv2.multiply(img, 1.5)

cv2.imshow('img', img)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
