from classKeyboardLayout import *
from classKeyboardKey import *
from layoutTest.textTest import *
import string


def mathLayoutGenerator(textFileName):
    abc = string.ascii_lowercase
    text = open(textFileName).read()
    charCounters = charStats(abc, text)
    keys = {}
    fingerIndex = 0

    for index in range(len(abc)):
        keys["primary"] = abc[index]
        keys["shift"] = abc[index].upper()
        keys["finger"] = fingerIndex
        if fingerIndex == 10:
            fingerIndex = 0
        else:
            fingerIndex += 1
        keys["id"] = index + 15

    # return KeyboardLayout()


mathLayoutGenerator("testTextes/alice_in_wonderland.txt")
