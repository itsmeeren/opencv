import numpy as np
import cv2 as cv

blank=np.zeros((400,400),np.uint8)
# cv.imshow('blank',blank)

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
cv.imshow('rectangle',rectangle)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('circle',circle)

# Bitwise operations

# 1 Bitwise AND

# returns the intersection of the image

bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow('bitwise_and',bitwise_and)

# 2 Bitwise OR

# It superimposes the image
bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow('bitwise_or',bitwise_or)

# 3 Bitwise XOR

# returns the non -intersecting part of the image

bitwise_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow('bitwise_xor',bitwise_xor)

# Bitwise NOT

# inverts the pixels (black --> white)

bitwise_not=cv.bitwise_not(bitwise_and)


cv.waitKey(0)