import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../img/lena.bmp')
blur3 = cv2.blur(img, (3, 3))
blur5 = cv2.blur(img, (5, 5))
blur7 = cv2.blur(img, (7, 7))
plt.subplot(221), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(blur3), plt.title('Blurred3*3')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(blur5), plt.title('Blurred 5*5')
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(blur7), plt.title('Blurred 7*7')
plt.xticks([]), plt.yticks([])
plt.show()
median = cv2.medianBlur(img, 5)
cv2.imshow('median', median)
cv2.waitKey(0)
gaussian = cv2.GaussianBlur(img, (5, 5), 0)
plt.imshow(gaussian)
plt.show()
