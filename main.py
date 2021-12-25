import pyautogui
import time
import findPokemon
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

def talkToReceptionist():
    print('Talking to receptionist')
    pressKey('z', 10, 1.1)
    time.sleep(1.4)

def walkToFishingSpot():
    print('Walk to fishing spot')
    holdKey('w', 1.8)
    holdKey('d', 1)
    holdKey('w', .4)

def catchFish():
    pressKey('s')
    pressKey('z')
    #Check if the magikarp fled
    fled = False
    for i in range(0, 4):
        fledResult = pyautogui.locateOnScreen('poke_img/fled_from.png')
        print('FLED:', fledResult)
        if (fledResult != None):
            fled = True
            break
    if (fled):
        return 'failed'
    else:
        time.sleep(.5)
        pressKey('z')
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
        pressKey('z')
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
            return result
    else:
        pressKey('z')
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
    pressKey('z', 3)

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

    # getToPosition()
    # cont = 0
    # while (True):
    #     # Wait for the battle to start
    #     time.sleep(15)
    #     cont = listener(cont)
    #     if cont == 5:
    #         cont = 0
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