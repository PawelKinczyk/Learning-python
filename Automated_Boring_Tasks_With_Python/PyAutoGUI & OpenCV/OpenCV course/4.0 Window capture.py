import cv2 as cv
import numpy as np
import os
import pyautogui as pg
from time import time

import win32gui
import win32ui
import win32con


class WindowCapture:

    # properties
    w = 0
    h = 0
    hwnd = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0

    def __init__(self, windowname) -> None:
        pass
        self.hwnd = win32gui.FindWindow(None, windowname)
        if not self.hwnd:
            raise Exception(f"Window not found {self.windowname}")

        # get window size
        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]

        # cut window border and titlebar
        border_pixels = 8
        titlebar_pixels = 30
        self.w = self.w - (border_pixels * 2)
        self.h = self.h - titlebar_pixels - border_pixels
        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels

        # coordinates of screen
        self.offset_x = window_rect[0] + self.cropped_x
        self.offset_y = window_rect[1] + self.cropped_y

    # Get all open windows names
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), win32gui.GetWindowText(hwnd))

    win32gui.EnumWindows(winEnumHandler, None)

    def getPosition(self, pos):
        return (pos[0] + self.offset_x, pos[1]+self.offset_y)

    def screenshotGet(self):

        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj,
                   (self.cropped_x, self.cropped_y), win32con.SRCCOPY)
        # dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype="uint8")
        img.shape = (self.h, self.w, 4)
        img = img[..., :3]

        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        return img


os.chdir(os.path.dirname(os.path.abspath(__file__)))

wind = WindowCapture("Autodesk AutoCAD 2021 - [SZYB_PW_IS_RZUTY.dwg]")

loop_time = time()
while (True):

    screenshot = wind.screenshotGet()
    # screenshot = np.array(screenshot)
    # screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

    cv.imshow("Computer vision", screenshot)

    print(f"FPS {1/(time()-loop_time)}")
    loop_time = time()

    # press q with the output window to exit
    # waits 1ms every loop to process key press
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break


print("Done")
