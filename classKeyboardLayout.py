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
                result.append(Key(key))
                break

    return result


def getQwertyStartKeys():
    layoutFile = json.loads(open("layouts/qwerty.txt").read())

    return searchStartKeyFromId(layoutFile["fingerStart"], layoutFile["keys"])


def generateKeysFromFile(keys, keyboardType):
    usedId = []
    result = []

    if keyboardType == "standard":
        for key in keys:
            if key["id"] in usedId:
                print("ITS FUCKING ERROR!!!! RED ALARM!!!! | error u have non-individaul id for keys", key)
                continue
            else:
                usedId.append(key["id"])

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
        else:
            print("some field in json of layout not valid:\t" + field + "\n")


class KeyboardLayout(object):
    def __init__(self, layoutFile):
        self.label = layoutFile["label"]
        self.keyboardType = "standard"
        self.keys = getQwertyKeys()
        self.fingerStart = getQwertyStartKeys()

        validationFields(self, layoutFile)

    def getLabel(self):
        return self.label

    def getKeyboardType(self):
        return self.keyboardType

    def getKeys(self):
        return self.keys

    def getFingerStart(self):
        return self.fingerStart

    def getKeysUnderFingers(self):
        keysUnderFingers = [[] for _ in range(10)]

        for key in self.keys:
            for fingerIndex in range(10):
                if key.getFinger() == (fingerIndex + 1):
                    keysUnderFingers[fingerIndex].append(key)

        return keysUnderFingers

    def getRows(self):
        if self.keyboardType == "standard":
            return  [
                        self.keys[:13],
                        self.keys[13:24],
                        self.keys[24:34]
                    ]
        else:
            print("now we dont support another keyb type | error in getRows method in layout class")

    # def getKeyFromPrimary(self, primary):
    #     for key in self.keys:
    #         if key.getPrimary() == primary:
    #             return key

