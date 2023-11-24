import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../img/testgray.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.subplot(221), plt.imshow(img, 'gray'), plt.title('origin')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换成灰度图片

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

fshift = np.fft.fftshift(dft)
rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)

# 低通滤波器R
mask1 = np.zeros((rows, cols, 2), np.uint8)
mask1[crow - 10:crow + 10, ccol - 10:ccol + 10] = 1

# 高通滤波器B
mask2 = np.ones((rows, cols, 2), np.uint8)
mask2[crow - 40:crow + 40, ccol - 40:ccol + 40] = 0

# 带通滤波器G
mask3 = np.zeros((rows, cols, 2), np.uint8)
mask3[crow - 40:crow + 40, ccol - 40:ccol + 40] = 1
mask3[crow - 10:crow + 10, ccol - 10:ccol + 10] = 0

# 滤波操作
f1 = fshift * mask1
f2 = fshift * mask2
f3 = fshift * mask3

ishift1 = np.fft.ifftshift(f1)
iimg1 = cv2.idft(ishift1)
res1 = cv2.magnitude(iimg1[:, :, 0], iimg1[:, :, 1])
ishift2 = np.fft.ifftshift(f2)
iimg2 = cv2.idft(ishift2)
res2 = cv2.magnitude(iimg2[:, :, 0], iimg2[:, :, 1])
ishift3 = np.fft.ifftshift(f3)
iimg3 = cv2.idft(ishift3)
res3 = cv2.magnitude(iimg3[:, :, 0], iimg3[:, :, 1])

res1 = cv2.normalize(res1, res1, 0, 1, cv2.NORM_MINMAX)
res2 = cv2.normalize(res2, res2, 0, 1, cv2.NORM_MINMAX)
res3 = cv2.normalize(res3, res3, 0, 1, cv2.NORM_MINMAX)

res1 = cv2.convertScaleAbs(res1, alpha=(255.0))
res2 = cv2.convertScaleAbs(res2, alpha=(255.0))
res3 = cv2.convertScaleAbs(res3, alpha=(255.0))
res = cv2.merge([res1, res2, res3])

plt.subplot(222), plt.imshow(res1, cmap='gray'), plt.title('low')
plt.subplot(223), plt.imshow(res2, cmap='gray'), plt.title('high')
plt.subplot(224), plt.imshow(res3, cmap='gray'), plt.title('middle')
plt.figure()
plt.imshow(res)
plt.title('result')
plt.show()
