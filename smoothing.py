import cv2 as cv
import rescale

img = rescale.rescale_Frames(cv.imread("photos/vy.jpg"))
# cv.imshow('img',img)
blur= cv.blur(img,(9,9))
cv.imshow('blr',blur)


gauss = cv.GaussianBlur(img,(9,9),0)
cv.imshow("gaus blur",gauss)

# Median blurr

Median = cv.medianBlur(img,9)
cv.imshow("med",Median)

#bilateral blurr

bilateral = cv.bilateralFilter(img,10,35,35)
cv.imshow("bilateral blurr",bilateral)


cv.waitKey(0)