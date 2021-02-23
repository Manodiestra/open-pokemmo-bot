import pyautogui
import time

DELAY_BETWEEN_COMMANDS = 1

def main():

    # Initialize PyAutoGUI
    pyautogui.FAILSAFE = True

    # Countdown timer
    print("Starting", end="")
    for i in range(0, 10):
        print(".", end="")
        time.sleep(1)
    print("Go")

    # Get to the stairs
    holdKey('left')
    
    # Get down the stairs
    holdKey('down')
    
    # Turn towards the water
    holdKey('right', 0.4)

    # Move mouse to the pokemon with sweet scent
    moveMouseAndClick(1335, 443, 'left')

    # Use sweet scent
    moveMouseAndClick(1206, 599, 'left')
    
    # Wait for the battle to start
    time.sleep(15)

    # Use the attacks
    pressKey('z')
    pressKey('right')
    pressKey('z', 2)

    # Done
    print("Done")

def holdKey(key, seconds=1):
    pyautogui.keyDown(key)
    time.sleep(seconds)
    pyautogui.keyUp(key)
    time.sleep(DELAY_BETWEEN_COMMANDS)

def pressKey(key, times = 1, interval = 1):
    for i in range(0, times):
        pyautogui.press(key)
        time.sleep(interval)

def moveMouse(x, y):
    pyautogui.moveTo(x, y)

def moveMouseAndClick(x, y, button):
    pyautogui.click(x=x, y=y, button=button)

if __name__ == "__main__":
    main()