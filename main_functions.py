import cv2 as cv
import numpy as np

# 1 Gray-scale conversion

img=cv.imread('im/cat.png')
# cv.imread(img)
gray_image=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("cat",gray_image)

# 2 Blur an image

blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow("blur",blur)

# 3 Edge Cascade - for detecting the features of the image

canny=cv.Canny(gray_image,100,200)
cv.imshow("canny",canny)

# 4 Dilating the image - filling teh gaps between edges

dilated=cv.dilate(canny,(3,3),iterations=1)
cv.imshow("dilated",dilated)


# 5 Eroding - removing noises

eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow("eroded",eroded)
cv.waitKey(0)

# 6 cropping

cropped=img[100:200,200:400]
cv.imshow("cropped",cropped)