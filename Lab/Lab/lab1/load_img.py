import numpy as np
import cv2 as cv

img = cv.imread('../img/img1.jpg')
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY, )
cv.imwrite('../img/gray_img1.jpg', gray_img)
