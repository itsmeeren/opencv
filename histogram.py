import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
img=cv.imread('im/tom.jpeg')

#Grayscale histogram
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

histogram=cv.calcHist([gray],[0],None,[256],[0,256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.xlim([0,256])
plt.plot(histogram)
plt.show()

# Colour histogram
colors=('b','g','r')
for i,color in enumerate(colors):
    histogram=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histogram,color=color)
    plt.xlim([0,256])
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")

plt.show()





cv.waitKey(0)