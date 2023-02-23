#   JSON FILE STRUCTURE (by Keyboard layout analyzer)
#   label           -   name of layout
#   author          -   author name
#   moreInfoUrl     -   more information about layout
#   moreInfoText    -   brief description of the layout
#   fingerStart     -   list of id keys that should have a finger on it at the start of typing
#                       but in class its LIST OF KEYS
#   keyboardType    -   type of keyboard (how many keys, what form factor)
#   TODO need to rewrite this arg: (standard type its ANSI layout with 101/104 keys)
#   keys            -   list of keys

### FILE STRUCTURE MUST CONTAIN THE FOLLOWING FIELDS: label, fingerStart, keyboardType, keys

import json
from classKeyboardKey import Key


def getQwertyKeys():
    keys = []
    for key in json.loads(open("layouts/normalQwerty.txt").read())["keys"]:
        keys.append(Key(key))

    return keys


def searchStartKeyFromId(fingerStartIdDict, keys):
    result = []

    for startId in fingerStartIdDict.values():
        for key in keys:
            if key["id"] == startId:
                result.append(key)
                break

    return result


def getQwertyStartKeys():
    layoutFile = json.loads(open("layouts/qwerty.txt").read())

    return searchStartKeyFromId(layoutFile["fingerStart"], layoutFile["keys"])


def generateKeysFromFile(keys, keyboardType):
    result = []
    if keyboardType == "standard":
        for key in keys:
            if 14 < key["id"] < 28 \
                    or 28 < key["id"] < 40 \
                    or 41 < key["id"] < 52:
                result.append(Key(key))
    else:
        print("ERROR\n", "\tnon \"standard\" type of keyboard not supported now")
    return result


def validationFields(self, layoutFile):
    for field in layoutFile:
        if field in "label author moreInfoUrl moreInfoText fingerStart keyboardType keys":
            match field:
                case "keyboardType":
                    self.keyboardType = layoutFile["keyboardType"]
                case "keys":
                    self.keys = generateKeysFromFile(layoutFile["keys"], self.keyboardType)
                case "fingerStart":
                    self.fingerStart = searchStartKeyFromId(layoutFile["fingerStart"], layoutFile["keys"])
                case "author":
                    self.author = layoutFile["author"]
                case "moreInfoUrl":
                    self.moreInfoUrl = layoutFile["moreInfoUrl"]
                case "moreInfoText":
                    self.moreInfoText = layoutFile["moreInfoText"]
            # if field == "keyboardType":
            #     self.keyboardType = layoutFile["keyboardType"]
            # elif field == "keys":
            #     self.keys = generateKeysFromFile(layoutFile["keys"], self.keyboardType)
            # elif field == "fingerStart":
            #     self.fingerStart = searchStartKeyFromId(layoutFile["fingerStart"], layoutFile["keys"])
            # elif field == "author":
            #     self.author = layoutFile["author"]
            # elif field == "moreInfoUrl":
            #     self.moreInfoUrl = layoutFile["moreInfoUrl"]
            # elif field == "moreInfoText":
            #     self.moreInfoText = layoutFile["moreInfoText"]
        else:
            print("some field in json of layout not valid:\t" + field + "\n")


class KeyboardLayout(object):
    def __init__(self, layoutFile):
        self.label = layoutFile["label"]
        self.keyboardType = "standard"
        self.keys = getQwertyKeys()
        self.fingerStart = getQwertyStartKeys()

        validationFields(self, layoutFile)

    def getKeys(self):
        return list(self.keys)

    def getFingerStart(self):
        return list(self.fingerStart)

    def getKeysUnderEachFinger(self):
        keysUnderEachFinger = [[], [], [], [], [], [], [], [], [], []]

        for key in self.keys:
            for keyIndex in range(10):
                if key.getFinger() == (keyIndex + 1):
                    keysUnderEachFinger[keyIndex].append(key)

        return keysUnderEachFinger

    def getRows(self):
        if self.keyboardType == "standard":
            return  [
                        self.keys[:12],
                        self.keys[13:24],
                        self.keys[24:34]
                    ]
        else:
            return 1

    def getKeyFromPrimary(self, primary):
        for key in self.keys:
            if key.getPrimary() == primary:
                return key

    # def initAbcLayout(self):
