import pyautogui
import time
import random

from utils import *
from config import *


def flyToIsland6PC():
    pressKey(FLY)
    pressKey(UP)
    pressKey(LEFT)
    pressKey(A_BUTTON)


def getNewEncounter():
    inBattle = False
    while(not inBattle):
        holdKey(RIGHT, .6)
        holdKey(LEFT, .6)
        holdKey(RIGHT, .6)
        holdKey(LEFT, .6)
        inBattle = checkForBattle()


def fightLoop():
    numBattles = 0
    while(numBattles < 5):
        getNewEncounter()


def resolveBattle():
    inBattle = True
    while(inBattle):
        pressKey(UP)
        pressKey(LEFT)
        pressKey(A_BUTTON)
        pressKey(A_BUTTON)
        # Check if battle is still going
        inBattle = checkIfWeAreInBattle()


def checkIfWeAreInBattle():
    time.sleep(2)
    for i in range(1):
        areInBattle = pyautogui.locateOnScreen('poke_img/my_bike_self_' + str(i) + '.png')
        print('Battle detection results', areInBattle)
        if (areInBattle != None):
            return True
    return False


def checkForBattle():
    time.sleep(3)
    pressKey(DOWN)
    for i in range(2):
        faceIsSeen = pyautogui.locateOnScreen('poke_img/my_bike_self_' + str(i) + '.png')
        print('FACE', faceIsSeen)
        if (faceIsSeen != None):
            # Not in battle
            print('YAY')
            return False
        else:
            # check if we are in battle
            inBattle = checkIfWeAreInBattle()
            if (inBattle):
                return True
    # error, we don't know where we are
    return 'error'


def walkToIsland6Grass():
    # Mount bike
    pressKey(BIKE_KEY)
    # Go There
    holdKey(RIGHT, 1.6)
    arrivedAtCorner = False
    while(not arrivedAtCorner):
        holdKey(DOWN, 1)
        inBattle = checkForBattle()
        if (inBattle == "error"):
            print("There was a error detecting if we are in battle")
            return
        if (inBattle):
            resolveBattle()
        else:
            arrivedAtCorner = True


def island6Payday():
    walkToIsland6Grass()
    fightLoop()
    getNewEncounter()

