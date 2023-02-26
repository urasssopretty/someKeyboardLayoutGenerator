from classKeyboardLayout import *
from classKeyboardKey import *
from layoutTest.textTest import *
import string


def getOrderedPositions(index):
    listOfPositions = [
        (5.25, 1.5),
        (8.25, 1.5),
        (4.25, 1.5),
        (9.25, 1.5),
        (3.25, 1.5),
        (10.25, 1.5),
        (2.25, 1.5),
        (11.25, 1.5),
        (6.25, 1.5),
        (7.25, 1.5),
        (3, 0.5),
        (4, 0.5),
        (5, 0.5),
        (6, 0.5),
        (8, 0.5),
        (9, 0.5),
        (10, 0.5),
        (12.25, 1.5),
        (4.75, 2.5),
        (5.75, 2.5),
        (6.75, 2.5),
        (7.75, 2.5),
        (8.75, 2.5),
        (2.75, 2.5),
        (3.75, 2.5),
        (7, 0.5),
        (11, 0.5),
        (12, 0.5),
        (13, 0.5),
        (14, 0.5),
        (2, 0.5),
        (9.75, 2.5),
        (10.75, 2.5),
        (11.75, 2.5),
    ]

    return listOfPositions[index]


def getKeyPosition(charCounters, character, keyboardType):
    if keyboardType != "standard":
        raise Exception("now layout generator dont work with non standard layouts!!!!",
                        "| error: math based generator in getKeyPosition")

    for pairIndex in range(len(charCounters)):
        if charCounters[pairIndex][0] == character:
            return getOrderedPositions(pairIndex)


### TODO REWRITE IT beacuse key id must be in order from first to last but not like this
def getKeyId(charCounters, char, keyboardType):
    if keyboardType != "standard":
        raise Exception("non-standard types of keyb is unsupported now | error: math based generator in getKeyId")

    for pairIndex in range(len(charCounters)):
        if charCounters[pairIndex][0] == char:
            return pairIndex

    raise Exception("character in not declared!!!! | error: math based generator in getKeyID", char, "\n", charCounters)


def getFingerIndex(position, keys):
    print(position)
    # if index < 5:
    #     return index
    # elif index == 5 or index == 6:
    #     return index


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

    characters = abc + ''.join(str(element) for element in list(shiftSpecialChars.keys()))
    # charCounters = charStats(characters, text)
    charCounters = sorted(charStats(characters, text).items(), key=lambda x: x[1], reverse=True)

    if keyboardType != "standard":
        raise Exception("HEY NOW ANOTHER KEYBOARD TYPE UNSUPPORTED | ERROR IN MATH BASED KEYB GENERATOR")

    keys = []

    for char in characters:
        keys.append(
            {
                "primary": char,
                "shift": shiftSpecialChars[char] if (char in shiftSpecialChars.keys()) else char.upper(),
                "position": getKeyPosition(charCounters, char, keyboardType),
                "id": getKeyId(charCounters, char, keyboardType),
                # FUCK HO TO DO THIS>?????
                "finger": getFingerIndex(["position"], keys)
            }
        )

    # for key in keys:
    #     print(key)

    # return KeyboardLayout()


# mathLayoutGenerator("testTexts/alice_in_wonderland.txt")
