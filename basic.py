import cv2 as cv
import rescale 
img = cv.imread("photos/vy.jpg")
img = rescale.rescale_Frames(img)


# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("",gray)


# # blurring
# blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
# # cv.imshow("",blur)

# # edge cascade
# canny = cv.Canny(blur,125,170)
# dilated = cv.dilate(canny,(7,7),iterations=3)
# cv.imshow('Contours',canny)
# cv.imshow('Contours-dilated',dilated)

# eroded = cv.erode(dilated,(7,7),iterations=1)
# cv.imshow("eroded",eroded)


resized = cv.resize(img,(500,500))
cv.imshow("r",resized)

cropped = resized[50:200, 200:400]
cv.imshow("cropped",cropped)


cv.waitKey(0)
