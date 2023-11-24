import cv2
import numpy as np

img = cv2.imread('../img/1.jpg')
rows, cols, ch = img.shape
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (cols, rows))
cv2.circle(img, (56, 65), 0, (0, 0, 255), 4)
cv2.circle(img, (368, 53), 0, (0, 0, 255), 4)
cv2.circle(img, (28, 387), 0, (0, 0, 255), 4)
cv2.circle(img, (389, 390), 0, (0, 0, 255), 4)
cv2.circle(dst, (0, 0), 0, (0, 0, 255), 4)
cv2.circle(dst, (300, 0), 0, (0, 0, 255), 4)
cv2.circle(dst, (0, 300), 0, (0, 0, 255), 4)
cv2.circle(dst, (300, 300), 0, (0, 0, 255), 4)
cv2.imshow('Input', img)
cv2.imshow('Output', dst)
cv2.imwrite('PerspectiveTransformImg.jpg', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
