#Function 'Module Identifier Rtape
#This code takes an image, converts the image to HSV, then masks the image, and finds the
#weighted center of mass.
#Then, we get the position of the center of mass, draw a line through it, and return the value as
#a float between -1 and 1.
#The output is a black image with two white rectangles in the center of the image.
#27th January 2017
#Author: Bevan Tsui, Oliver Allshire


#Loading required modules and image.
import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread("B7.jpeg",1)
cv2.imshow('image',img)

height = img.shape[0]
width = img.shape[1]
#Splitting the image into RGB bands.

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#Setting the tolerances for the mask.

lower = np.array([130/2, 50.0/100*255, 15.0/100*255])
upper = np.array([160/2, 100.0/100*255, 100.0/100*255])

mask = cv2.inRange(hsv,lower,upper)

x = range(0, mask.shape[1])
y = range(0, mask.shape[0])

(X,Y) = np.meshgrid(x,y)

x_coord = int((X*mask).sum()/mask.sum().astype("float"))
print(x_coord)


cv2.line(mask, (x_coord, 60), (x_coord, 180), (255,255,0), thickness=2, lineType=8, shift=0)
width = mask.shape[1]
print (width)
pos = 2 * x_coord / float(width) - 1
print (pos)

#Finding the height, width and channels of the image and printing them.



#print(green)
#cv2.imshow('blue',blue)
#cv2.imshow('green',green)
#cv2.imshow('red',red)

#Displays the thresholded image as black and white.

cv2.imshow('threshold_B5',mask)

#Closes program
cv2.waitKey(0)
cv2.destroyAllWindows()
