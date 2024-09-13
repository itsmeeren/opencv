import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
def resize(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    return cv.resize(frame,(width,height),interpolation=cv.INTER_AREA)


# img=cv.imread('im/tom.jpeg')
#
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#
# #color channel split and merge
#
# b,g,r=cv.split(img)
# blank=np.zeros(img.shape[:2],np.uint8)
#
# blue_img=cv.merge((b,blank,blank))
# cv.imshow('blue',blue_img)
# green_img=cv.merge((blank,g,blank))
# cv.imshow('green',green_img)
# red_img=cv.merge((blank,blank,r))
# cv.imshow('red',red_img)

# img=cv.imread("im/tom.jpeg")
#
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# # cv.imshow('gray',resize(gray,scale=3.25))
#
#
# threshold,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
# cv.imshow('thresh',resize(thresh,scale=3.25))
#
# adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,9)
# cv.imshow('adaptive_thresh',resize(adaptive_thresh,3.25))
#
# adaptive_thresh1=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,13,5)
# cv.imshow('adaptive_thresh1',resize(adaptive_thresh1,3.25))

# cv.imshow('img',img)

img=cv.imread('im/la')


cv.waitKey(0)