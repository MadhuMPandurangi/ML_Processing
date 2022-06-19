from logging import NullHandler
import cv2
import numpy as np

class Flood_fill:
    # Load the image
    image = cv2.imread('./static/MVI_1421-00008.jpg')

    # Converting to binary
    ret1, thresh1 = cv2.threshold(image, 120, 255,cv2.THRESH_BINARY_INV)


    # Flood fill
    h,w,chn = image.shape
    seed = (0,0)
    mask = np.zeros((h+2,w+2),np.uint8)

    floodflags = 4
    floodflags |= cv2.FLOODFILL_MASK_ONLY
    floodflags |= (255 << 8)

    num,im,mask,rect = cv2.floodFill(thresh1, mask, seed, (255,0,0), (10,)*3, (10,)*3, floodflags)

    cv2.imwrite("./static/flood_fill_img.jpg", mask)

    flood_fill_img = mask



    # Display images
    def display(self):
        images = [self.image, self.thresh1, self.flood_fill_img]
        titles = ['1 : Original', '2 : Binary Threshold Inverted', '3 : Flood filled image']
        count = len(images)
        
        for i in range(0,count):
            cv2.imshow(titles[i], cv2.resize(images[i], (0, 0), fx = 0.3, fy = 0.3))

        cv2.waitKey(0)

        cv2.destroyAllWindows()



# Driver code
flood_fill_obj = Flood_fill()
flood_fill_obj.display()
