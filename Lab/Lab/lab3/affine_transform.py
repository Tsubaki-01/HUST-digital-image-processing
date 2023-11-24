import cv2
import numpy as np

img = cv2.imread('../img/img1.jpg')
rows, cols, ch = img.shape
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[100, 100], [200, 50], [100, 250]])
M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.circle(img, (50, 50), 0, (0, 0, 255), 4)
cv2.circle(img, (200, 50), 0, (0, 0, 255), 4)
cv2.circle(img, (50, 200), 0, (0, 0, 255), 4)
cv2.circle(dst, (100, 100), 0, (0, 0, 255), 4)
cv2.circle(dst, (200, 50), 0, (0, 0, 255), 4)
cv2.circle(dst, (100, 250), 0, (0, 0, 255), 4)
cv2.imshow('Input', img)
cv2.imshow('Output', dst)
cv2.imwrite('AffineTransformImg.jpg', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
