import cv2
from cv2 import imread
import numpy as np

image = imread('./static/MVI_1421-00008.jpg')
img = cv2.cvtColor(image[0:870, 470:1282], cv2.COLOR_BGR2GRAY)

#Hough circle
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, minDist=15, param1=50, param2=18, minRadius=12, maxRadius=20)
c = 0
if circles is not None:
    for i in circles[0, :]:
        c = c+1
        cv2.circle(img, (int(i[0]), int(i[1])), 2, (0, 0, 255), 3)
        print((int(i[0]), int(i[1])))

print(c)
cv2.imshow('img_gray', img)
cv2.waitKey(0)
cv2.destroyAllWindows()