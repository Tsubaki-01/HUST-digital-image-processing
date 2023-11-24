import numpy as np
import cv2 as cv

img1 = cv.imread('../img/flower2.jpg')
img2 = cv.imread('../img/diamond2.jpg')

img = cv.addWeighted(img1, 0.7, img2, 0.3, 0)

cv.imshow('test:', img)
cv.waitKey(0)
cv.destroyAllWindows()
