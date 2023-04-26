import cv2 as cv
from rescale import rescale_Frames
myphoto = cv.imread('photos/WIN_20230313_15_53_48_Pro.jpg')
scaled_photo = rescale_Frames(myphoto)

cv.imshow('Vyoam',myphoto)
cv.imshow("small photo",scaled_photo)
cv.waitKey(0)

# basket = cv.VideoCapture('videos/basket.mp4')
# while True:
#     isTrue ,frame = basket.read()
#     frame_resized = rescale_Frames(frame)

#     cv.imshow('video',frame)
#     cv.imshow('small_video',frame_resized)
#     if cv.waitKey(20) and 0xFF==ord('d'):
#         break 
# basket.release()
# cv.destroyAllWindows()

