import cv2 as cv
import numpy as np

# def resize(img,scale):
#     width = int(img.shape[1] * scale)
#     height = int(img.shape[0] * scale)
#     return cv.resize(img, (width, height))
# #load the face image
#
# img=cv.imread('im/multi-lady.jpeg')
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#
# haar_cascade=cv.CascadeClassifier('haar_face.xml')
# face_detect=haar_cascade.detectMultiScale(gray,1.1,6)
# print(f'no of faces detected: {len(face_detect)}')
#
# # We can draw the image around the faces detected
#
# for (x,y,w,h) in face_detect:
#     cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
# cv.imshow('Detection',resize(img,4.25))


img = cv.imread('mb_messi.jpg')
print(img.shape)
cropped=img[20:200,100:400]
cv.imshow('crop',cropped)
cv.imshow('img',img)
# 180 50

cv.waitKey(0)