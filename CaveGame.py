import random
import time


def displayintro():
    print("You are in a land full of dragons! there are two caves in front of you")
    print("You have to chose one of theese caves!")


def chosenCave():
    cave = ""
    while cave != "1" and cave != "2":
        print("which cave will you go into? (1 or 2)")
        cave = input()

    return cave


def checkCave(chosenCave):
    print("you approach the cave...")
    time.sleep(2)
    print("its dark and spoooky")
    time.sleep(3)
    print("A large dragon jumps out in front of you! He starts charging his breath")
    print("")
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print("THE DRAGON GIVES YOU HIS TREASURE!")
    else:
        print("You are burning...")
        time.sleep(2)
        print("you died.")


playAgain = "yes"
while playAgain == "yes" or playAgain == "y":

    displayintro()

    caveNumber = chosenCave()

    checkCave(caveNumber)

    print("do you wanna play again? (yes or no)")
    playAgain = input()