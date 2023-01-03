import numpy as np
import cv2 as cv

# img=cv.imread('img/00.jpg')
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#
# def empty_callback(value):
#     pass
#
#
# # create a black image, a window
#
# cv.namedWindow('image')
#
# # create trackbars for color change
# cv.createTrackbar('lower', 'image', 0, 179 , empty_callback)
# cv.createTrackbar('upper', 'image', 1, 179, empty_callback)
# cv.createTrackbar('dark',  'image', 1, 255, empty_callback)
#
#
# while True:
#     # cv.imshow('image', img)
#
#     # sleep for 10 ms waiting for user to press some key, return -1 on timeout
#     key_code = cv.waitKey(10)
#     if key_code == 27:
#         # escape key pressed
#         break
#
#     # get current positions of four trackbars
#     lower = cv.getTrackbarPos('lower', 'image')
#     upper = cv.getTrackbarPos('upper', 'image')
#     dark = cv.getTrackbarPos('upper', 'image')
#     #b = cv.getTrackbarPos('B', 'image')
#     #s = cv.getTrackbarPos(switch_trackbar_name, 'image')
#
#
#
#     # assign the same BGR color to all pixels
#     #img[:] = [0, g, r]
#     lower_green = np.array([lower, 100, 20])
#     upper_green = np.array([upper, 255, 255])
#     kernel = np.ones((5, 5), np.uint8)
#
#     mask = cv.inRange(hsv, lower_green, upper_green)
#
#     closing = cv.morphologyEx(mask, cv.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=1)
#
#     cv.imshow('image', closing)
#     cv.imshow('mask', mask)
#
#     # ret, thresh = cv.threshold(closing, 127, 255, 0)
#     # contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
#     #
#     # cv.drawContours(img, contours, -1, (0, 255, 0), 8)
#     #
#     # cv.imshow("contour", img)
# #test commit
#
#
# #dd3
#
# # # zielony
# # lower_green = np.array([35, 20, 40])
# # upper_green = np.array([90, 255, 255])
#
#
#
#
#
#
#
#
#
#
# #cv.imshow("window", img)
# cv.waitKey(0)


i=2
img=cv.imread('data/'+str(i)+'.jpg')

scale_percent = 25  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
if(img.shape[1]>2000):
    img = cv.resize(img, dim, interpolation=cv.INTER_AREA)

#obraz wyskalowany
#blur
img = cv.medianBlur(img, 5)
#konwersja na hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)


#progi na zielony
lower_green = np.array([34, 100, 20])
upper_green = np.array([62, 255, 255])

#progi na zolty
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

#progi na bordo
lower_purple = np.array([155, 125, 5])
upper_purple = np.array([179, 255, 125])

#progi na czerwony
lower_red = np.array([140, 100, 160])
upper_red = np.array([179, 255, 255])


#maska
mask = cv.inRange(hsv, lower_green, upper_green)
mask_yellow = cv.inRange(hsv, lower_yellow, upper_yellow)
mask_purple = cv.inRange(hsv, lower_purple, upper_purple)
mask_red = cv.inRange(hsv, lower_red, upper_red)



blur = cv.medianBlur(mask, 5)
blur_yellow = cv.medianBlur(mask_yellow, 5)
blur_purple = cv.medianBlur(mask_purple, 5)
blur_red = cv.medianBlur(mask_red, 5)

closing = cv.morphologyEx(blur, cv.MORPH_CLOSE, np.ones((3, 3), np.uint8), iterations=2)
closing_yellow = cv.morphologyEx(blur_yellow, cv.MORPH_CLOSE, np.ones((3, 3), np.uint8), iterations=2)
closing_purple = cv.morphologyEx(blur_purple, cv.MORPH_CLOSE, np.ones((3, 3), np.uint8), iterations=2)
closing_red = cv.morphologyEx(blur_red, cv.MORPH_CLOSE, np.ones((3, 3), np.uint8), iterations=2)

res_green = cv.bitwise_and(img, img, mask=closing)
res_green2gray = cv.cvtColor(res_green, cv.COLOR_RGB2GRAY)

res_yellow = cv.bitwise_and(img, img, mask=closing_yellow)
res_yellow2gray = cv.cvtColor(res_yellow, cv.COLOR_RGB2GRAY)

res_purple = cv.bitwise_and(img, img, mask=closing_purple)
res_purple2gray = cv.cvtColor(res_purple, cv.COLOR_RGB2GRAY)

res_red = cv.bitwise_and(img, img, mask=closing_red)
res_red2gray = cv.cvtColor(res_red, cv.COLOR_RGB2GRAY)



# circles=None

circles = cv.HoughCircles(res_green2gray, cv.HOUGH_GRADIENT,
                          1.6, 40, param1=100, param2=12, minRadius=10,maxRadius=20)
circles_yellow = cv.HoughCircles(res_yellow2gray, cv.HOUGH_GRADIENT,
                          1.6, 40, param1=100, param2=12, minRadius=10,maxRadius=20)
circles_purple = cv.HoughCircles(res_purple2gray, cv.HOUGH_GRADIENT,
                          1.6, 40, param1=100, param2=12, minRadius=10,maxRadius=20)
circles_red = cv.HoughCircles(res_red2gray, cv.HOUGH_GRADIENT,
                          1.6, 40, param1=100, param2=12, minRadius=10,maxRadius=20)



#print(circles)
if circles is not None:
    circles = np.uint16(np.around(circles))
    green_size = circles.size / 3
    print('green=' + str(green_size))

    for i in circles[0, :]:
        # draw the outer circle
        cv.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
else:
    print('no green')
if circles_yellow is not None:
    circles_yellow = np.uint16(np.around(circles_yellow))
    yellow_size = circles_yellow.size / 3
    print('yellow=' + str(yellow_size))

    for i in circles_yellow[0, :]:
        # draw the outer circle
        cv.circle(img, (i[0], i[1]), i[2], (0, 255, 255), 2)
else:
    print('no yellow')

if circles_purple is not None:
    circles_purple = np.uint16(np.around(circles_purple))
    purple_size = circles_purple.size / 3
    print('purple=' + str(purple_size))

    for i in circles_purple[0, :]:
        # draw the outer circle
        cv.circle(img, (i[0], i[1]), i[2], (250, 230, 230), 2)
else:
    print('no purple')

if circles_red is not None:
    circles_red = np.uint16(np.around(circles_red))
    red_size = circles_red.size / 3
    print('red=' + str(red_size))

    for i in circles_red[0, :]:
        # draw the outer circle
        cv.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 2)
else:
    print('no red')








cv.imshow(str(1), img)
# cv.imshow(str(2), res_green2gray)





cv.waitKey(0)