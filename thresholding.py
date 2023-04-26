import cv2 as cv
import rescale 
img = rescale.rescale_Frames(cv.imread('photos/vy.jpg'))
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

# simple thresholding
threshold,thresh = cv.threshold(gray,140,255,cv.THRESH_BINARY)
cv.imshow("simple threshold",thresh)

threshold,thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow("thresh inv",thresh_inv)

# adaptive thresholding
adaptive_thresholding = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,9,1)
cv.imshow("adaptive thresh",adaptive_thresholding)


cv.waitKey(0)