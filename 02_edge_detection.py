import cv2

img = cv2.imread('C:/Users/HUAWEI/Desktop/Opencv/lane/lane_detect/img.jpg', cv2.IMREAD_GRAYSCALE)

edge_img = cv2.Canny(img, 50, 100)

cv2.imwrite('edges_img.jpg', edge_img)
cv2.imshow('edges', edge_img)
cv2.waitKey(0)