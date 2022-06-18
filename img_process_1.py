from logging import NullHandler
import cv2
import numpy as np

# Load the image
image = cv2.imread('./static/MVI_1421-00008.jpg')



# Converting to binary

ret, thresh1 = cv2.threshold(image, 125, 255, cv2.THRESH_BINARY)

ret1, thresh2 = cv2.threshold(image, 120, 255,cv2.THRESH_BINARY_INV)





# Flood fill
h,w,chn = image.shape
seed = (0,0)
mask = np.zeros((h+2,w+2),np.uint8)

floodflags = 4
floodflags |= cv2.FLOODFILL_MASK_ONLY
floodflags |= (255 << 8)

num,im,mask,rect = cv2.floodFill(thresh2, mask, seed, (255,0,0), (10,)*3, (10,)*3, floodflags)

cv2.imwrite("./static/flood_fill_img.jpg", mask)

flood_fill_img = cv2.imread('/home/madhu/dev/raghu/image_processing/static/flood_fill_img.jpg')



# Display images
def display():
    images = [image, thresh1, thresh2, flood_fill_img]
    titles = ['1: Original', '2: Binary Threshold', '3 : Binary Threshold Inverted', '4 : Flood filled image']
    count = len(images)
    
    for i in range(0,count):
        cv2.imshow(titles[i], cv2.resize(images[i], (0, 0), fx = 0.3, fy = 0.3))

    cv2.waitKey(0)

    cv2.destroyAllWindows()


display()