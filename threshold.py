import numpy as np
import cv2 as cv

img=cv.imread('im/tom.jpeg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

threshold,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('threshold',thresh)

# we can find the inverse using both methods
thresh_inv_1 = cv.bitwise_not(thresh)
threshold_inv,thresh_inv=cv.threshold(gray,125,255,cv.THRESH_BINARY_INV)

# Adaptive Thresholding

adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('adaptive_thresh',adaptive_thresh)
cv.waitKey(0)