# Code from https://github.com/learncodebygaming/opencv_tutorials

import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture

cv.__version__
# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture("Autodesk AutoCAD 2021 - [SZYB_PW_IS_RZUTY.dwg]")
# # initialize the Vision class
# vision_limestone = Vision('PrzechwytywanieA.jpg')


loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # display the processed image
    # screenshot = cv.cvtColor(screenshot, cv.CV_8U)
    # points = vision_limestone.find(screenshot, 0.5, 'rectangles')
    cv.imshow("Unproc", screenshot)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    key=cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    elif key == ord("f"):
        cv.imwrite(f"pos/{loop_time}.jpg", screenshot)
    elif key == ord("d"):
        cv.imwrite(f"neg/{loop_time}.jpg", screenshot)

print('Done.')