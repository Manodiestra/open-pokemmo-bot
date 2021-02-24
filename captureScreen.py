import cv2 as cv
import numpy as np
import pyautogui

def capture_screen():
    while(True):

        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        screenshot = screenshot[...,:3]
        screenshot = np.ascontiguousarray(screenshot)
        
        return screenshot
