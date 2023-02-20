from classKeyboardLayout import *
from classKeyboardKey import *
from layoutTest.textTest import *
import string

def getFingerIndex(index):
    if index < 5:
        return index
    elif index == 5 or index == 6:
        return index


def mathLayoutGenerator(textFileName, keyboardType="standard"):
    abc = string.ascii_lowercase + " "
    text = open(textFileName).read()
    # charCounters = charStats(abc, text)
    charCounters = charStats(abc, text)
    keys = []
    key = {}
    fingerIndex = 0

    if keyboardType == "standard":
        for index in range(len(abc)):
            currentChar = abc[index]
            key["primary"] = currentChar

            if currentChar != " ":
                key["shift"] = currentChar.upper()

            #   TODO make a system for setFingerIndex
            key["finger"] = fingerIndex
            # if fingerIndex == 10:
            #     fingerIndex = 0
            # else:
            #     fingerIndex += 1

            key["id"] = index + 15
            keys.append(key)

    # return KeyboardLayout()


mathLayoutGenerator("testTextes/alice_in_wonderland.txt")
