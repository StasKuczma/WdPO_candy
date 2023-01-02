import numpy as np
import cv2 as cv

img=cv.imread('img/00.jpg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

def empty_callback(value):
    pass


# create a black image, a window

cv.namedWindow('image')

# create trackbars for color change
cv.createTrackbar('lower', 'image', 0, 179 , empty_callback)
cv.createTrackbar('upper', 'image', 1, 179, empty_callback)
cv.createTrackbar('dark',  'image', 1, 255, empty_callback)


while True:
    # cv.imshow('image', img)

    # sleep for 10 ms waiting for user to press some key, return -1 on timeout
    key_code = cv.waitKey(10)
    if key_code == 27:
        # escape key pressed
        break

    # get current positions of four trackbars
    lower = cv.getTrackbarPos('lower', 'image')
    upper = cv.getTrackbarPos('upper', 'image')
    dark = cv.getTrackbarPos('upper', 'image')
    #b = cv.getTrackbarPos('B', 'image')
    #s = cv.getTrackbarPos(switch_trackbar_name, 'image')



    # assign the same BGR color to all pixels
    #img[:] = [0, g, r]
    lower_green = np.array([lower, 100, 20])
    upper_green = np.array([upper, 255, 255])
    kernel = np.ones((5, 5), np.uint8)

    mask = cv.inRange(hsv, lower_green, upper_green)

    closing = cv.morphologyEx(mask, cv.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=1)

    cv.imshow('image', closing)
    cv.imshow('mask', mask)

    # ret, thresh = cv.threshold(closing, 127, 255, 0)
    # contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    #
    # cv.drawContours(img, contours, -1, (0, 255, 0), 8)
    #
    # cv.imshow("contour", img)
#test commit


#dd34

# # zielony
# lower_green = np.array([35, 20, 40])
# upper_green = np.array([90, 255, 255])










#cv.imshow("window", img)
cv.waitKey(0)


