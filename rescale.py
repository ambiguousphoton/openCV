import cv2 as cv

def rescale_Frames(frame,scale=0.45):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width ,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)