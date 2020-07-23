import cv2

# 图片读取操作

img = cv2.imread('C:/Users/HUAWEI/Desktop/Opencv/lane/lane_detect/img.jpg')

cv2.imshow('img_gray', img)

if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
    cv2.imwrite('img_gray.bmp', img)
