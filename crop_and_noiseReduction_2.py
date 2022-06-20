
try:
    # standard library imports
    import cv2
    import numpy as np

    # local class imports
    from floodfill_1 import Flood_fill
except Exception as e:
    print("Some Modules are missing: {}".format(e))    


# Cropping Image for further processing
class NoiceReduction:
    #print("shape of the image: ", Flood_fill().mask.shape)
    crop = np.zeros(Flood_fill().mask.shape)
    inv_crop = np.zeros(Flood_fill().mask.shape)
    opening = np.zeros(Flood_fill().mask.shape)
    erosion = np.zeros(Flood_fill().mask.shape)


    def crop_reduceNoise(self):
        # size format is [x1:x2, y1:y2] -> [rows, columns]
        self.crop = Flood_fill().mask[0:870, 360:1282]
        kernel_opening = np.ones((25,25), np.uint8)
        kernel_erosion = np.ones((39,39), np.uint8)
        ret1, self.inv_crop = cv2.threshold(self.crop, 120, 255,cv2.THRESH_BINARY_INV)
        self.opening = cv2.morphologyEx(self.inv_crop, cv2.MORPH_OPEN, kernel_opening)
        self.erosion = cv2.erode(self.opening,kernel_erosion,iterations = 1)



    def display(self):
        images = [self.crop, self.inv_crop, self.opening, self.erosion]
        titles = ['Cropped Image', 'Inverted Cropped Image','Opening Image','Erotion image']
        count = len(images)
        
        for i in range(0,count):
            cv2.imshow(titles[i], images[i])

        cv2.waitKey(0)

        cv2.destroyAllWindows()    


NR_obj = NoiceReduction()
NR_obj.crop_reduceNoise()
#NR_obj.display()

cv2.imshow('Noise reduced image', NR_obj.erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()    
