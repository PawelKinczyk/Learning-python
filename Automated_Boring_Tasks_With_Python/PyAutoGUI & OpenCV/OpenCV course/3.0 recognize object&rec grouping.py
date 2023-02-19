# Import
import pyautogui
import time
import cv2 as cv
import os
import numpy as np

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Opencv
wc_image = cv.imread("PrzechwytywanieA.png", cv.IMREAD_UNCHANGED)
screen_image = cv.imread("Screen.png", cv.IMREAD_UNCHANGED)

wc_w = wc_image.shape[1]
wc_h = wc_image.shape[0]
screen_image_w =screen_image.shape[1]
screen_image_h = screen_image.shape[0]

results = cv.matchTemplate(screen_image, wc_image, cv.TM_CCOEFF_NORMED)
print(results)

cv.imshow("Results", results)
# cv.waitKey()

## 2.0 Recognize all images
threshold = 0.7
locations = np.where(results >= threshold)
print(locations)

# Zip pictures
locations = list(zip(*locations[::-1]))
print(locations)

rectangles = []
for loc in locations:
    rect = [int(loc[0]), int(loc[1]), wc_w, wc_h]
    rectangles.append(rect)
print(rectangles)
# Draw on screen

if len(rectangles):
    print("Found")


    line_color = (0,255,0)
    line_type = cv.LINE_4

    for (x, y, w, h) in rectangles:
        top_left = (x,y)
        bottom_right = (x+w, y+h)

        cv.rectangle(screen_image, top_left, bottom_right, line_color, line_type)

    cv.imshow("Match", screen_image)
    cv.waitKey()

else:
    print("Not")