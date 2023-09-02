import pyautogui
import time
import sys
import random

from utils import *
from constants import *
from config import *

def checkPokedex():
    time.sleep(.2)
    pressKey('n')
    time.sleep(1 + randomTime() * 3)
    pressKey('n')

def checkTrainer():
    time.sleep(.2)
    pressKey('c')
    time.sleep(1 + randomTime() * 3)
    pressKey('c')

def talkToReceptionist():
    print('Talking to receptionist')
    pressKey('space', 11, 1.1)
    time.sleep(1.4)

def walkToFishingSpot():
    print('Walk to fishing spot')
    holdKey('w', 2.2)
    holdKey('d', 1.4)
    holdKey('w', .4)

def catchFish():
    pressKey('s')
    pressKey('space')
    # Check if the magikarp fled
    for i in range(0, 4):
        fledResult = pyautogui.locateOnScreen('poke_img/720_fled_from.png')
        if (fledResult != None):
            print('FLED:', fledResult)
            return 'failed'
    else:
        time.sleep(.5)
        pressKey('space')
        # verify pokemon summary is shown
        time.sleep(13)
        for i in range(3):
            pokeSummaryShown = pyautogui.locateOnScreen('poke_img/720_pokemon_summary_' + str(i) + '.png')
            if (pokeSummaryShown != None):
                print('Pokemon Summary', pokeSummaryShown)
                return 'success'
        return 'failed'

def tryToFish():
    print('Try to catch a fish')
    # Randomize start time
    time.sleep(randomTime())
    pressKey(OLD_ROD_KEY)
    # Wait for fishing timer
    time.sleep(2.2)
    # Check if fish was hooked
    for i in range(4):
        noFishHooked = pyautogui.locateOnScreen('poke_img/720_not_even_a_nibble_' + str(i) + '.png')
        fishIsHooked = pyautogui.locateOnScreen('poke_img/720_landed_a_pokemon_' + str(i) + '.png')
        print('hooked', fishIsHooked, noFishHooked)
        if (noFishHooked != None or fishIsHooked != None):
            break
    hooked = False
    if (fishIsHooked != None):
        hooked = True
    elif (noFishHooked == None):
        return 'Failed to identify hook'
    if (hooked):
        print('Fish is hooked!')
        # Dismiss "Landed a Pokemon" message
        pressKey('space')
        # Wait for battle to start
        time.sleep(5.9)
        result = catchFish()
        if (result == 'success'):
            time.sleep(randomTime())
            # Dismiss summary screen
            pressKey('esc')
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
        if (result == 'Failed to identify hook'):
            return

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
        num = randomTime()
        if (num < .08):
            checkPokedex()
        elif (num > .95):
            checkTrainer()
        result = tryToFish()
        print('Fish result:', result)
        if (result == 'success'):
            numFish -= 1
        if (result == 'Failed to identify hook'):
            return
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

def walkToIsland5Grass():
    # Mount bike
    pressKey('4')
    # Ride to spot

def island5Payday():
    walkToIsland5Grass()

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



if __name__ == "__main__":
    main()
