import numpy as np
import cv2 as cv

img=cv.imread('im/cat.png')
#Translation


# -x -->Left
# -y --> UP
# y --> Down
# x --> Right

def translate(img,x,y):
    transform_matrix = np.float32([[1,0,x],[0,1,y]])
    dimension=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transform_matrix,dimension)

# Rotation

def rotate(img,angle,rotpoint=None):
    (width,height)=img.shape[:2]

    if rotpoint is None:
     rotpoint=(width/2,height/2)

    rotation_matrix=cv.getRotationMatrix2D(rotpoint,angle,1)
    dimension=(width,height)
    return cv.warpAffine(img,rotation_matrix,dimension)

#Flipping


#flipcode

# 1--> y-axis
# 0-->x-axis
# -1 --> along both x and y


flip=cv.flip(img,1)


cv.waitKey(0)