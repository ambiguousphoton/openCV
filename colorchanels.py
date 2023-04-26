import cv2 as cv
import numpy as np
import rescale
img = rescale.rescale_Frames(cv.imread('photos/vy.jpg'))
# cv.imshow("orign",img)

blank = np.zeros(img.shape[:2],dtype="uint8")

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow("red",red)


merged = cv.merge([b,g,r])
cv.imshow("merged",merged)




cv.waitKey(0)

