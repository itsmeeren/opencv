import numpy as np
import cv2 as cv

def resize(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    return cv.resize(frame,(width,height),interpolation=cv.INTER_AREA)

img=cv.imread('im/tom.jpeg')

#Blank Image

blank=np.zeros(img.shape[:2],np.uint8)

mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),75,255,-1)
cv.imshow('mask',resize(mask,3.25))
cv.imshow('img',resize(img,3.25))


# Now use mask in bitwise and

and_img=cv.bitwise_and(img,img,mask=mask)
cv.imshow('and',resize(and_img,3.25))

cv.waitKey(0)
