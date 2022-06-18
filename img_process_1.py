

import cv2

image = cv2.imread('./static/MVI_1421-00008.jpg')

cv2.imshow('original', image)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# set1
ret, thresh4 = cv2.threshold(gray_image, 125, 255, cv2.THRESH_BINARY)

cv2.imshow('1st image', thresh4)

cv2.waitKey(0)


cv2.destroyAllWindows()


