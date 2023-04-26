import cv2 as cv

import numpy as np

img = cv.imread("photos/vy.jpg")

# def translate(img,x,y):
#     transMatrix = np.float32([[1,0,x],[0,1,y]])
#     dim = (img.shape[1] ,img.shape[0])
#     return cv.warpAffine(img, transMatrix, dim)
# translated = translate(img,-100,100)
# cv.imshow("t",translated)

# def rotate(img,angle,rot_point=None):
#     (height,width) = img.shape[:2]
#     if not rot_point:
#         rot_point = (width//2,height//2)
#     rotMat = cv.getRotationMatrix2D(rot_point,angle,1.0)
#     dim = (width,height)
#     return cv.warpAffine(img, rotMat,dim)

# rotated = rotate(img,-45,(3,3))
# cv.imshow("r",rotated)


# resizing
# resized = cv.resize(img, (500,500) ,interpolation=cv.INTER_CUBIC)
# cv.imshow('resized',resized)

flip = cv.flip(img,-1)
cv.imshow("f",flip)

# cropping
cropped  = img[200:400,300:400]
cv.imshow("crop",cropped)


cv.waitKey(0)