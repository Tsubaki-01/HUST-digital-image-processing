import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../img/moon.jpg', 0)
# cv2.CV_64F 输出图像的深度（数据类型），可以使用-1, 与原图像保持一致 np.uint8
laplacian = cv2.Laplacian(img, cv2.CV_64F)
# 参数 1,0 为只在 x 方向求一阶导数，最大可以求 2 阶导数。
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
# 参数 0,1 为只在 y 方向求一阶导数，最大可以求 2 阶导数。
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

laplacian = cv2.convertScaleAbs(laplacian)
laplacian_minus = cv2.subtract(img, laplacian)

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()
plt.imshow(laplacian_minus, cmap='gray')
plt.show()
