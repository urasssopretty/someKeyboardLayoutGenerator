from classKeyboardLayout import *
from classKeyboardKey import *
from layoutTest.textTest import *
import string


def getKeyPostion(charCounters, char, keyboardType):
def getFingerIndex(index):
    if index < 5:
        return index
    elif index == 5 or index == 6:
        return index


def mathLayoutGenerator(textFileName, keyboardType, abc=string.ascii_lowercase):
    text = open(textFileName).read().lower().replace(" ", "")

    shiftSpecialChars = {
                            "[": "{",
                            "]": "}",
                            "\\": "|",
                            ";": ":",
                            "'": "\"",
                            ",": "<",
                            ".": ">",
                            "/": "?"
                        }
    characters = abc + str(shiftSpecialChars.keys())
    charCounters = sorted(charStats(characters, text).items(), key=lambda x: x[1], reverse=True)

    if keyboardType == "standard":
        keys = [0 for _ in range(len(characters))]
        key = {}

        for char in characters:
            key["primary"] = char
            key["shift"] = shiftSpecialChars[char] if ( char in shiftSpecialChars.keys() ) else char.upper()
            key["position"] = getKeyPostion(charCounters, char, keyboardType)
            key["finger"] = getFingerIndex()
            key["id"] = getKeyId()

            keys.append(key)
    else:
        print("HEY NOW ANOTHER KEYBOARD TYPE UNSUPPORTED | ERROR IN MATH BASED KEYB GENERATOR")

    # return KeyboardLayout()


# mathLayoutGenerator("testTexts/alice_in_wonderland.txt")
