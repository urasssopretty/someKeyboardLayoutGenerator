from classKeyboardLayout import *
from classKeyboardKey import *
from layoutTest.textTest import *
import string


def getKeyPosition(charCounters, character, keyboardType):
    if keyboardType != "standard":
        raise Exception("now layout generator dont work with non standard layouts!!!!",
                        "| error: math based generator in getKeyPosition")

    # ### rewrite for add one loop
    # for index in range(100):
    #     for pairIndex in range(len(charCounters)):
    #         if charCounters[pairIndex][0] == character:
    #             match pairIndex:
    #                 case 0:
    #                     return (2, 0.5)
    #                 case _:
    #                     return (-999, -999)

            # if 14 < key["id"] < 28 \
            #         or 28 < key["id"] < 40 \
            #         or 41 < key["id"] < 52:

    for pairIndex in range(len(charCounters)):
        if charCounters[pairIndex][0] == character:
            match pairIndex:
                case 0:
                    return (2, 0.5)
                case _:
                    return (-999, -999)


### TODO REWRITE IT beacuse key id must be in order from first to last but not like this
def getKeyId(charCounters, char, keyboardType):
    if keyboardType != "standard":
        raise Exception("non-standard types of keyb is unsupported now | error: math based generator in getKeyId")

    for pairIndex in range(len(charCounters)):
        if charCounters[pairIndex][0] == char:
            return pairIndex

    raise Exception("character in not declared!!!! | error: math based generator in getKeyID", char, "\n", charCounters)


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
                "id": getKeyId(charCounters, char, keyboardType),
                "position": getKeyPosition(charCounters, char, keyboardType),
                "finger": getFingerIndex(0)
            }
        )

    # for key in keys:
    #     print(key)

    # return KeyboardLayout()


# mathLayoutGenerator("testTexts/alice_in_wonderland.txt")
