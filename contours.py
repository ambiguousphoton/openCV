import cv2 as cv

import numpy as np

import rescale 
img = rescale.rescale_Frames(cv.imread("photos/vy.jpg"))
# cv.imshow("img",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)

# blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)

# canny = cv.Canny(blur,125,175)
# cv.imshow("canny",canny)

blank = np.zeros(img.shape,dtype="uint8")
# cv.imshow("blank",blank)

ret ,thresh = cv.threshold(gray,125,250,cv.THRESH_BINARY)
# cv.imshow("thresh",thresh)

contours , hierarchies  = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow("countours drawn blank img",blank)

print(f'{len(contours)} in this image')
cv.waitKey(0)
# dhanywad
