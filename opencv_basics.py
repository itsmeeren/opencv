
import numpy as np
import cv2 as cv

#reading the image
img = cv.imread('im/cat.png')
cv.imshow('cat',img)

#video capturing 0  for webcam

video=cv.VideoCapture('cat.mp4')

while True:
    isTrue, frame = video.read()
    cv.imshow('video',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv.destroyAllWindows()



#resizing the image to perticular dimension


#This works for video, image, live video
def resize(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    return cv.resize(frame,(width,height),interpolation=cv.INTER_AREA)


#This only works for live video

def Liveresize(width,height):
    video.set(3,width)
    video.set(4,height)


cv.imshow('image',resize(img,0.21))
cv.waitKey(0)


#paint the image

#creating the blank image using numpy
blank=np.zeros((500,500,3),np.uint8)

blank[200:300,300:350]=0,255,0

cv.imshow('blank',blank)

# img=cv.imread('im/cat.png')
# cv.imshow('cat',img)

#rectangle
cv.rectangle(img,(400,400),(500,500),(255,0,0),thickness=2)

cv.imshow('cat',img)


#writing text

cv.putText(blank,"lol",(blank.shape[1]//2,blank.shape[0]//2),cv.FONT_HERSHEY_TRIPLEX,1,(0,0,255),2)
cv.imshow('lol',blank)


