import pyautogui
import time
import findPokemon

DELAY_BETWEEN_COMMANDS = 1

def getToPosition():
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

def returnToPokeCenter():
    # Turns away from the water
    holdKey('left', 0.4)

    # Get up the stairs
    holdKey('up')

    # Get to the PokeCenter door
    holdKey('right')

    # Enter the door
    holdKey('up')

def talkToNurse():
    # Start conversation with the nurse
    pressKey('z', 7, 5)

    # Go back to the entrance
    holdKey('down')

def listener():
    if(findPokemon.find_pokemon('shelmet')):
        # Countdown timer
        for i in range(0, 4):
            # Use the attacks
            pressKey('z')
            pressKey('right')
            pressKey('z', 2)
            time.sleep(15)

    # Move mouse to the pokemon with sweet scent
    moveMouseAndClick(1335, 443, 'left')
    # Use sweet scent
    moveMouseAndClick(1206, 599, 'left')

    if(findPokemon.find_pokemon('noPP')):
        returnToPokeCenter()
        talkToNurse()
        getToPosition()

def main():
    # Initialize PyAutoGUI
    pyautogui.FAILSAFE = True

    # Countdown timer
    print("Starting", end="")
    for i in range(0, 10):
        print(".", end="")
        time.sleep(1)
    print("Go")
    
    getToPosition()

    while (True):
        # Wait for the battle to start
        time.sleep(15)
        listener()
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
        time.sleep(DELAY_BETWEEN_COMMANDS)

def moveMouse(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(DELAY_BETWEEN_COMMANDS)

def moveMouseAndClick(x, y, button):
    pyautogui.click(x=x, y=y, button=button)
    time.sleep(DELAY_BETWEEN_COMMANDS)

if __name__ == "__main__":
    main()