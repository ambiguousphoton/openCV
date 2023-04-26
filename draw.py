import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
# cv.imshow("blank", blank)
# # painting the img
# blank[200:300,000:500] = 0,0,255
# cv.imshow("",blank)

# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)
# # cv.imshow("rectangle",blank)

# cv.circle(blank,((blank.shape[1]//2),blank.shape[0]//2),40,(0,0,255),thickness=3)
# # cv.imshow("c",blank)

# cv.line(blank,(0,53),(400,300),(255,255,255),thickness=3)

cv.putText(blank,"Jai shree ram",(150,255),cv.FONT_HERSHEY_TRIPLEX,1,(0,0,255),2)

cv.imshow("mix",blank)
cv.waitKey(0)

