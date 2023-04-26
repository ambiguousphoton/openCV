import cv2 as cv
import numpy as np
import rescale 
img  = rescale.rescale_Frames(cv.imread('photos/vy.jpg'))
cv.imshow("img",img)
blank = np.zeros(img.shape[:2],dtype="uint8")
cv.imshow("blank",blank)
mask  = cv.circle(blank,(img.shape[1]//2+54,img.shape[0]//2+18),100,255,-1)
cv.imshow("mask",mask)


maskedimg = cv.bitwise_and(img,img,mask=mask)
cv.imshow("masked img" ,maskedimg)
cv.waitKey(0)