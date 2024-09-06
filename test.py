import cv2 as cv
import numpy as np


#creating the blank image using numpy
blank=np.zeros((500,500,3),np.uint8)

#paint the image

# blank[200:300,300:350]=0,255,0
#
# cv.imshow('blank',blank)

img=cv.imread('im/cat.png')

def resize(img,scale=0.75):
 width=int(img.shape[1]*scale)
 height=int(img.shape[0]*scale)
 return cv.resize(img,(width,height),interpolation=cv.INTER_AREA)

canny=resize(cv.Canny(img,100,200),0.75)

dilated=cv.dilate(canny,(7,7),iterations=1)
cv.imshow("dilated",dilated)
# cv.imshow('canny',canny)
cv.waitKey(0)

