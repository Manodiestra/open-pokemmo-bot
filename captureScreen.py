import cv2 as cv
import numpy as np
import pyautogui

while(True):

    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
    screenshot = screenshot[...,:3]
    screenshot = np.ascontiguousarray(screenshot)
    
    
    cv.imshow('Computer Vision', screenshot)

    
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done')
