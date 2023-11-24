import cv2
import numpy as np

img = cv2.imread('../img/Fig6A.jpg')
ref = cv2.imread('../img/Fig6B.jpg')

img_res = []

for c in range(3):

    h_img = cv2.calcHist([img[:, :, c]], [0], None, [256], [0, 256])
    h_ref = cv2.calcHist([ref[:, :, c]], [0], None, [256], [0, 256])

    cdf_img = h_img.cumsum()
    cdf_ref = h_ref.cumsum()
    c_h_img = cdf_img / cdf_img.max()
    c_h_ref = cdf_ref / cdf_ref.max()

    # 利用累积直方图进行直方图规定化
    pixel_map = np.zeros((256, 1), dtype='uint8')
    for i in range(256):
        diff = abs(c_h_img[i] - c_h_ref)
        idx = np.argmin(diff)
        pixel_map[i] = idx

    img_res.append(cv2.LUT(img[:, :, c], pixel_map))
img_res = np.array(img_res)
print(img_res.shape)
res = cv2.merge(img_res)

cv2.imshow('', res)
cv2.imshow(';', ref)
#
# # 将图像分解为R，G，B通道
# b, g, r = cv2.split(img)
#
# # 对每个通道应用直方图均衡化
# b_histogram_equalized = cv2.equalizeHist(b)
# g_histogram_equalized = cv2.equalizeHist(g)
# r_histogram_equalized = cv2.equalizeHist(r)
#
# # 将处理后的通道再重新合并到一起
# img_output = cv2.merge([b_histogram_equalized, g_histogram_equalized, r_histogram_equalized])
#
# # 输出处理后的图像
# cv2.imshow('Histogram Equalization', img_output)
# cv2.waitKey()
cv2.waitKey(0)
cv2.destroyAllWindows()
