
try:
    # standard library imports
    import cv2
    from cv2 import floodFill
    import numpy as np

    # local class imports
    from img_process_1_floodfill import Flood_fill
except Exception as e:
    print("Some Modules are missing: {}".format(e))    


# Cropping Image for further processing
class Crop:
    #print("shape of the image: ", Flood_fill().mask.shape)
    crop = np.zeros(Flood_fill().mask.shape)
    def crop_image(self):
        # size format is [x1:x2, y1:y2]
        self.crop = Flood_fill().mask[0:870, 360:1282]
        cv2.imshow('Cropped Image',self.crop)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

crop_obj = Crop()
crop_obj.crop_image()
