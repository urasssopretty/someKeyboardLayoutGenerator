from operator import itemgetter
from classKeyboardLayout import *
# from classKeyboardKey import *
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


def getKeyPosition(charCounters, character):
    for pairIndex in range(len(charCounters)):
        if charCounters[pairIndex][0] == character:
            return getOrderedPositions(pairIndex)


### TODO REWRITE IT beacuse key id must be in order from first to last but not like this
def getKeyId(charCounters, char):
    for pairIndex in range(len(charCounters)):
        if charCounters[pairIndex][0] == char:
            return pairIndex

    raise Exception("character in not declared!!!! | error: math based generator in getKeyID", char, "\n", charCounters)


def getFingerIndex(position, keys):
    xvalue = position[0]

    if 1 < xvalue < 6:
        return int(xvalue - 2)
    elif int(xvalue) == 6:
        return 3
    elif int(xvalue) == 7:
        return 6
    elif 7 < xvalue < 12:
        return int(xvalue - 2)
    elif 11 < xvalue < 15:
        return  9
    else:
        return -1


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
        keyPosition = getKeyPosition(charCounters, char)
        keys.append(
            {
                "primary": char,
                "shift": shiftSpecialChars[char] if (char in shiftSpecialChars.keys()) else char.upper(),
                "position": keyPosition,
                "id": getKeyId(charCounters, char),
                "finger": getFingerIndex(keyPosition, keys)
            }
        )

    # rows = [[] for _ in range(3)]
    #
    # for key in keys:
    #     match key["position"][1]:
    #         case 0.5:
    #             rows[0].append(key)
    #         case 1.5:
    #             rows[1].append(key)
    #         case 2.5:
    #             rows[2].append(key)
    #
    # for row in rows:
    #     for key in sorted(row, key=lambda d: d["position"][0]):
    #         print(key["primary"], key["finger"], key["position"])
    #     print()

    # return KeyboardLayout()

