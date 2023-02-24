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
    shiftSpecialChars = {"[": "{", "]": "}", "\\": "|", ";": ":", "'": "\"", ",": "<", ".": ">", "/": "?"}
    abc = string.ascii_lowercase
    characters = abc + "[]\;',./"    # + " "
    text = open(textFileName).read()
    # charCounters = charStats(abc, text)
    charCounters = charStats(characters, text)
    keys = []
    key = {}


    if keyboardType == "standard":
        for index in range(len(characters)):
            currentChar = characters[index]
            key["primary"] = currentChar

            if currentChar in shiftSpecialChars.keys():
                key["shift"] = shiftSpecialChars[currentChar]
            else:
                key["shift"] = currentChar.upper()

            #   TODO make a system for setFingerIndex
            key["finger"] = 0
            if index < 12:
                key["id"] = index + 15
            elif index < 24:
                key[id] = index + 18
            # elif index <

            keys.append(key)
    else:
        print("HEY NOW ANOTHER KEYBOARD TYPE DONT WORK | ERROR IN MATHBASED KEYB GENERATOR")

    # return KeyboardLayout()


# mathLayoutGenerator("testTexts/alice_in_wonderland.txt")
