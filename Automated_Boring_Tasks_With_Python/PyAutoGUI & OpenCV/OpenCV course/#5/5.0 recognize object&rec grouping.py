# Import
import pyautogui
import time
import cv2 as cv
import os
import numpy as np
from Window_Capture import WindowCapture

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def findClickPositions(screen_image, object_image_path, threshold = 0.6, debug_mode = None):
    # Opencv
    wc_image = cv.imread(object_image_path, cv.IMREAD_UNCHANGED)

    wc_w = wc_image.shape[1]
    wc_h = wc_image.shape[0]

    results = cv.matchTemplate(screen_image, wc_image, cv.TM_CCOEFF_NORMED)
    print(results)

    cv.imshow("Results", results)


    ## Recognize all images

    locations = np.where(results >= threshold)
    print(locations)

    # Zip pictures
    locations = list(zip(*locations[::-1]))
    print(locations)

    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), wc_w, wc_h]
        rectangles.append(rect)
        rectangles.append(rect)


    # Group rectangles
    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)
    print(rectangles)

    # Draw on screen
    points = []
    if len(rectangles):
        print("Found")

        line_color = (0,255,0)
        line_type = cv.LINE_4
        marker_color = (0,225,0)
        marker_type = cv.MARKER_CROSS
        
        
        # Draw rectangles
        for (x, y, w, h) in rectangles:
            center_x = x + int(w/2)
            center_y = y + int(h/2)
        
            points.append((center_x, center_y))

            if debug_mode == "rectangles":
                # Determine box location and position
                top_left = (x,y)
                bottom_right = (x+w, y+h)

                cv.rectangle(screen_image, top_left, bottom_right, line_color, line_type)
            elif debug_mode == "points":
                cv.drawMarker(screen_image, (center_x, center_y), marker_color, marker_type, markerSize=40)

    if debug_mode:
        cv.imshow("Match", screen_image)

    return points

point = findClickPositions("Screen.png", "PrzechwytywanieA.png", threshold=0.6, debug_mode="points")
print(point)