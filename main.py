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
    holdKey('right', 0.65)

    # Enter the door
    holdKey('up', 4)

def talkToNurse():
    # Start conversation with the nurse
    pressKey('z', 7, 5)

    # Go back to the entrance
    holdKey('down')

    # Mount the bike
    pressKey('3')

def listener(cont):
    cont = cont + 1

    if(cont < 5):
         # Countdown timer
        for i in range(0, 4):
            # Use the attacks
            if(i < 2):
                pressKey('z')
                pressKey('right')
                pressKey('z', 2)
                time.sleep(15)
            else:
                pressKey('z', 3, 2)
                time.sleep(15)

        # Move mouse to the pokemon with sweet scent
        moveMouseAndClick(1335, 443, 'left')
        # Use sweet scent
        moveMouseAndClick(1206, 599, 'left')
    else:
        returnToPokeCenter()
        talkToNurse()

    return cont

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
    cont = 0

    while (True):
        # Wait for the battle to start
        time.sleep(15)
        cont = listener(cont)
        if cont == 5:
            cont = 0
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
    time.sleep(DELAY_BETWEEN_COMMANDS)

def moveMouseAndClick(x, y, button):
    pyautogui.click(x=x, y=y, button=button)
    time.sleep(DELAY_BETWEEN_COMMANDS)

if __name__ == "__main__":
    main()