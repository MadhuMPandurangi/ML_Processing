import cv2

# Load the image
image = cv2.imread('./static/MVI_1421-00008.jpg')


# Converting to binary and display

ret, thresh4 = cv2.threshold(image, 125, 255, cv2.THRESH_BINARY)

ret1, thresh = cv2.threshold(image, 120, 255,cv2.THRESH_BINARY_INV)

cv2.imshow('original', cv2.resize(image, (0, 0), fx = 0.3, fy = 0.3))

cv2.imshow('1st image', cv2.resize(thresh4, (0, 0), fx = 0.3, fy = 0.3))

cv2.imshow('2nd image', cv2.resize(thresh, (0, 0), fx = 0.3, fy = 0.3))

cv2.waitKey(0)

cv2.destroyAllWindows()






