import cv2

# reading image
image = cv2.imread('./static/MVI_1421-00008.jpg')



# Converting to binary 
ret, thresh4 = cv2.threshold(image, 125, 255, cv2.THRESH_BINARY)



# Displying original image
cv2.imshow('original', cv2.resize(image, (0, 0), fx = 0.3, fy = 0.3))

# Displying converted image
cv2.imshow('1st image', cv2.resize(thresh4, (0, 0), fx = 0.3, fy = 0.3))



# Wait(display image) till any key is pressed
cv2.waitKey(0)


cv2.destroyAllWindows()


