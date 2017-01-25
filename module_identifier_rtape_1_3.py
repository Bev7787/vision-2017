#Function 'Module Identifier Rtape
#This code takes an image, seperates the green band and binary thresholds
#the green band.
#The binary threshold keeps all green values above 100 while turning all green
#values below 99 off.
#The output is a black image with two white rectangles in the center of the image.
#21st January 2017
#Author: Bevan Tsui


#Loading required modules and image.
import numpy as np
import cv2
img = cv2.VideoCapture(0)

#Splitting the image into RGB bands.
def filtered_image(x):
    _, frame = x.read()
    green = frame[:,:,1]
    return filter_image
#Binary thresholding the green band.
def threshold_img(x):
    thresh1 = cv2.threshold(green,100,255,cv2.THRESH_BINARY)
    return thresh

#Finding the height, width and channels of the image and printing them.



#print(green)
#cv2.imshow('blue',blue)
#cv2.imshow('green',green)
#cv2.imshow('red',red)

#INTENSE CODING INTENSIFIES

#Displays the thresholded image as black and white.
#Problem here, needs def
if __name__ == "__main__":
    window = cv2.namedWindow("preview")
    bytes=''
    while True:
        bytes+=stream.read(1024)
        a = bytes.find('\xff\xd8')
        b = bytes.find('\xff\xd9')
        if a!=-1 and b!=-1:
            jpg = bytes[a:b+2]
            bytes= bytes[b+2:]
            image = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
            x, y, w, h, img = findTarget(filtered)
            image = cv2.resize(filtered, None, fx=ENLARGE_IMAGE_SCALE_FACTOR, fy=ENLARGE_IMAGE_SCALE_FACTOR, interpolation=cv2.INTER_CUBIC)
            cv2.imshow("preview", filtered)
            if cv2.waitKey(1) ==27:
                exit(0) 
