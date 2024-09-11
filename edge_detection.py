import cv2 as cv
import numpy as np

def resize(img,scale):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    return cv.resize(img, (width, height))


img=cv.imread('im/tom.jpeg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)


# 1 laplacian method

lap=cv.Laplacian(gray,cv.CV_64F)# d depth --> datadepth

lap=np.uint8(np.absolute(lap)) # Laplacian operator may have negetive and posiive values as well so taking absolute
# cv.imshow('lap',resize(lap,3.25))

# 2 Sobel method

# finds the gradients of the image in both direction x and y
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)

cv.imshow('sobelx',resize(sobelx,3.25))
cv.imshow('sobely',resize(sobely,3.25))

# For joining both use bitwise_or

combined_sobel =cv.bitwise_or(sobelx,sobely)
cv.imshow('combined_sobel',resize(combined_sobel,3.25))

# 3 Canny method
canny=cv.Canny(gray,100,200)
cv.imshow('canny',resize(canny,3.25))


cv.waitKey(0)