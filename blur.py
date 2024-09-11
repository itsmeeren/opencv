import cv2 as cv
import numpy as np

img=cv.imread('im/tom.jpeg')

# 1 Average Blur
average=cv.blur(img,(3,3))

# 2 Median
median=cv.medianBlur(img,3)

# 3 Bilateral
bilateral=cv.bilateralFilter(img,5,15,15)

# 4 Gaussian blur
guassian=cv.GaussianBlur(img,(5,5),0)



