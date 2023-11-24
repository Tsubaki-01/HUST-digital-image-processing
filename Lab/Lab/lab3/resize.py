import cv2
import numpy as np

img = cv2.imread('../img/flowerx.png')
# 下面的None 本应该是输出图像的尺寸，但是因为后边我们设置了缩放因子
# 因此这里为None
res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# OR
# 直接设置输出图像的尺寸，所以不用设置缩放因子
height, width = img.shape[:2]
res = cv2.resize(img, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)
cv2.imshow('res', res)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
