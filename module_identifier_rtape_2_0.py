#Function 'Module Identifier Rtape
#This code takes an image, seperates the green band and binary thresholds
#the green band.
#The binary threshold keeps all green values above 100 while turning all green
#values below 99 off.
#The output is a black image with two white rectangles in the center of the image.
#21st January 2017
#Author: Bevan Tsui
#This code is licensed CC-BY-SA

#Loading required modules and image.
import numpy as np
import cv2
import argparse
from matplotlib import pyplot as plt
img = cv2.VideoCapture(0)



#Splitting the image into RGB bands.
while True
    _, frame = img.read()
    green = frame[:,:,1]
    ret, thresh1 = cv2.threshold(green,100,255,cv2.THRESH_BINARY)
    edge = cv2.Canny(green, 100, 255)
    cv2.imshow('threshold_B5', edge)



#Finding the height, width and channels of the image and printing them.



    #print(green)
    #cv2.imshow('blue',blue)
    #cv2.imshow('green',green)
    #cv2.imshow('red',red)

#Displays the thresholded image as black and white.


#Closes program
cv2.waitKey(0)
cv2.destroyAllWindows()

img.release(0)
