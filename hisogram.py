import cv2 as cv
import rescale
import matplotlib.pyplot as plt
import numpy as np

img = rescale.rescale_Frames(cv.imread("photos/vy.jpg"))
cv.imshow("1",img)
 

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("",gray)

blank = np.zeros(img.shape[:2],dtype="uint8")
mask = cv.circle(blank,(img.shape[1]//2+54,img.shape[0]//2+18),100,255,-1)
masked = cv.bitwise_and(img,img,mask=mask)

cv.imshow('masked again',masked)



# # gray_histogram
# gray_histogram = cv.calcHist([gray],[0],mask,[256],[0,256])
# plt.figure("gray histogram")
# plt.xlabel("bins")
# plt.ylabel("no of pixels")
# plt.plot(gray_histogram)
# plt.xlim([0,256])
# plt.show()


plt.figure()
plt.xlabel("bins")
plt.ylabel("no of pixels")
colors = ('b','g','r')
for i ,col in enumerate(colors):
    hist = cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()
# cv.waitKey(0)
