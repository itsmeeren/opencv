import cv2 as cv
import numpy as np


#creating the blank image using numpy
blank=np.zeros((500,500,3),np.uint8)

#paint the image

# blank[200:300,300:350]=0,255,0
#
# cv.imshow('blank',blank)

img=cv.imread('im/cat.png')




cv.waitKey(0)

