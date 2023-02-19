# Import
import pyautogui
import time
import cv2 as cv
import os
import numpy as np

# # Recognize elements with pyautogui 
# a = list(pyautogui.locateAllOnScreen('Automated_Boring_Tasks_With_Python/PyAutoGUI/PrzechwytywanieA.png', confidence=0.7))
# b = list(pyautogui.locateAllOnScreen('Automated_Boring_Tasks_With_Python/PyAutoGUI/PrzechwytywanieB.png', confidence=0.7))
# c = list(pyautogui.locateAllOnScreen('Automated_Boring_Tasks_With_Python/PyAutoGUI/PrzechwytywanieC.png', confidence=0.7))
# d = list(pyautogui.locateAllOnScreen('Automated_Boring_Tasks_With_Python/PyAutoGUI/PrzechwytywanieD.png', confidence=0.7))

# print(a)
# print(b)
# print(c)
# print(d)

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Opencv
wc_image = cv.imread("PrzechwytywanieA.png", cv.IMREAD_UNCHANGED)
screen_image = cv.imread("Screen.png", cv.IMREAD_UNCHANGED)

results = cv.matchTemplate(screen_image, wc_image, cv.TM_CCOEFF_NORMED)

# results=np.concatenate(results,r)
print("result")
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

# Draw on screen

if locations:
    print("Found")

    wc_w = wc_image.shape[1]
    wc_h = wc_image.shape[0]
    line_color = (0,255,0)
    line_type = cv.LINE_4

    for loc in locations:
        top_left = loc
        bottom_right = (top_left[0] +wc_w, top_left[1] + wc_h)

        cv.rectangle(screen_image, top_left, bottom_right, line_color, line_type)

    cv.imshow("Match", screen_image)
    cv.waitKey()

else:
    print("Not")
# ## 1.0 First version to recognize one object
# min_val, max_val, min_loc, max_loc = cv.minMaxLoc(results)

# print(f"Best top left match: {max_loc}")
# print(f"Best confidence: {max_val}")

# threshold = 0.7

# if max_val >= threshold:
#     print("Found")
    
#     # get dim of image
#     wc_w = wc_image.shape[1]
#     wc_h = wc_image.shape[0]

#     top_left = max_loc
#     bottom_right = (top_left[0]+ wc_w, top_left[1] + wc_h)

#     cv.rectangle(screen_image, top_left, bottom_right,
#                   color=(0,255,0), thickness=2, lineType=cv.LINE_4)
    
#     cv.imshow("Results", screen_image)
#     cv.waitKey()

# else:
#     print("Not found")