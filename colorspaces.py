import cv2 as cv
import matplotlib.pyplot as plt
import rescale 


img = rescale.rescale_Frames(cv.imread("photos/vy.jpg"))
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("g",gray)

# hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow("hsv",hsv)

# lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow("lab",lab)

rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("rgb",rgb)

plt.imshow(rgb)
plt.show()


cv.waitKey(0)

