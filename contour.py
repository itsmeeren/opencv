import numpy as np
import cv2 as cv

img=cv.imread('im/tom.jpeg')
def resize(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    return cv.resize(frame,(width,height),interpolation=cv.INTER_AREA)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#Defining the blank image using numpy
blank=np.zeros(img.shape,np.uint8)

#Extracting the feature using canny
jerry_canny=cv.Canny(img,125,175)
cv.imshow('jerry_canny',resize(jerry_canny,3.25))
countours,heirarchies=cv.findContours(jerry_canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE,) #Using canny
print(len(countours))

# Threshhold for pixels
ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)

countours,heirarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE,)
print(len(countours))

cv.imshow('thresh_image',resize(thresh,3.25))

#Drawing an image into blank image

cv.drawContours(blank,countours,-1,(0,255,0),1)
cv.imshow('contours',resize(blank,3.25))