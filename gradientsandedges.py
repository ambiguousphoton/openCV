import cv2 as cv
import rescale 
import numpy as np
img = rescale.rescale_Frames(cv.imread('photos/vy.jpg'))

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)


# sobel
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)

combinde = cv.bitwise_or(sobelx,sobely)
cv.imshow("soble x",sobelx)
cv.imshow("soble y",sobely)
cv.imshow("combined",combinde)

# canny edge detector
canny = cv.Canny(gray,150,175)
cv.imshow("canny",canny)

#laplacion
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("laplacion",lap)
cv.waitKey(0)