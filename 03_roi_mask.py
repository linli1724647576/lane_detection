import cv2
import numpy as np

edge_img = cv2.imread('C:/Users/HUAWEI/Desktop/Opencv/lane/lane_detect/img.jpg', cv2.IMREAD_GRAYSCALE)

mask = np.zeros_like(edge_img)
# 填充多边形
mask = cv2.fillPoly(mask,
                    np.array([[[0, 368], [300, 210], [340, 210], [640, 368]]]),
                    color=255)
#与运算
masked_edge_img = cv2.bitwise_and(edge_img, mask)
cv2.imwrite('masked_edge_img.jpg', masked_edge_img)
cv2.imshow('masked', masked_edge_img)
cv2.waitKey(0)


