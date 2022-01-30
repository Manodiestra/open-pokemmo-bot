import pyautogui
import time
import sys
import random

DELAY_BETWEEN_COMMANDS = .1

def startCountDown():
    # Countdown timer
    print("Starting", end="")
    for i in range(0, 3):
        print(".", end="")
        time.sleep(1)
    print("Go")

def randomeTime():
    return random.randrange(5, 100) / 100

def checkPokedex():
    time.sleep(.2)
    pressKey('n')
    time.sleep(1 + randomeTime() * 3)
    pressKey('n')

def checkTrainer():
    time.sleep(.2)
    pressKey('c')
    time.sleep(1 + randomeTime() * 3)
    pressKey('c')

def talkToReceptionist():
    print('Talking to receptionist')
    pressKey('space', 10, 1.1)
    time.sleep(1.4)

def walkToFishingSpot():
    print('Walk to fishing spot')
    holdKey('w', 1.8)
    holdKey('d', 1)
    holdKey('w', .4)

def catchFish():
    pressKey('s')
    pressKey('space')
    #Check if the magikarp fled
    fled = False
    for i in range(0, 4):
        fledResult = pyautogui.locateOnScreen('poke_img/fled_from.png')
        if (fledResult != None):
            fled = True
            break
    if (fled):
        print('FLED:', fledResult)
        return 'failed'
    else:
        time.sleep(.5)
        pressKey('space')
        return 'success'

def tryToFish():
    print('Try to catch a fish')
    # Randomize start time
    time.sleep(randomeTime())
    pressKey('2')
    # Wait for fishing timer
    time.sleep(2.2)
    # Check if fish was hooked
    notHooked = pyautogui.locateOnScreen('poke_img/Not_even_a_nibble.png')
    hooked = False
    if (notHooked == None):
        hooked = True
    if (hooked):
        # Dismiss "Landed a Pokemon" message
        pressKey('space')
        # Wait for battle to start
        time.sleep(5.9)
        result = catchFish()
        if (result == 'success'):
            # Wait for catch and pokemon summary
            # to pop up
            time.sleep(12.6 + randomeTime())
            # Dismiss summary screen
            pressKey('esc')
            return result
        else:
            # Wait to make sure the "Fled" message
            # wasn't missied
            time.sleep(12.6 + randomeTime())
            pokeSummary = pyautogui.locateOnScreen('poke_img/pokemon_summary.png')
            if (pokeSummary != None):
                # The pokemon was caught
                result = "success"
            return result
    else:
        pressKey('space')
        return 'failed'

def simpleFishLoop():
    # Check if the user specified how many
    # fish to catch
    numFish = 0
    if (len(sys.argv) >= 3):
        numFish = int(sys.argv[2])
    else:
        numFish = 1
    while(numFish > 0):
        result = tryToFish()
        print('Fish result:', result)
        if (result == 'success'):
            numFish -= 1

def kantoFish():
    print('Begin Kanto safari fish!')
    # interact with receptionist
    holdKey('w', .4)
    talkToReceptionist()
    # walk to fishing spot
    walkToFishingSpot()
    # start fishing loop
    numFish = 30
    while(numFish > 0):
        num = randomeTime()
        if (num < .08):
            checkPokedex()
        elif (num > .95):
            checkTrainer()
        result = tryToFish()
        print('Fish result:', result)
        if (result == 'success'):
            numFish -= 1
    # Finish safari sequence
    time.sleep(1)
    pressKey('esc')
    pressKey('space', 3)

def walkToIsland2Grass():
    # Mount bike
    pressKey('4')
    # Ride to spot
    holdKey('d', .55)
    holdKey('w', .35)
    holdKey('d', .7)
    holdKey('w', 1)
    holdKey('a', .7)
    holdKey('w', 1)

def island2Payday():
    walkToIsland2Grass()

def main():
    # Initialize PyAutoGUI
    pyautogui.FAILSAFE = True

    if (len(sys.argv) == 1):
        print("Loading default fisher")
        startCountDown()
        kantoFish();
    elif (sys.argv[1] == "fish"):
        print("Fishing...")
        startCountDown()
        simpleFishLoop()
    elif (sys.argv[1] == "payday"):
        print("Payday time...")
        startCountDown()
        island2Payday()

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