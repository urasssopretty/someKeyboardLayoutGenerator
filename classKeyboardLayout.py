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
    # return [Key(key) for key in json.load(open("layouts/normalQwerty.txt"))["keys"] if key["id"] in (list(range(15, 28)) + list(range(29, 40)) + list(range(42, 52)))]

    keys = []
    for key in json.loads(open("layouts/normalQwerty.txt").read())["keys"]:
        if key["id"] in (list(range(15, 28)) + list(range(29, 40)) + list(range(42, 52))):
            keys.append(Key(key))

    return keys


def searchStartKeyFromId(fingerStartIdDict, keys):
    return [Key(key) for key in keys if key["id"] in fingerStartIdDict.values()]


def getQwertyStartKeys():
    layoutFile = json.loads(open("layouts/qwerty.txt").read())

    return searchStartKeyFromId(layoutFile["fingerStart"], layoutFile["keys"])


#   TODO RENAME THIS
def generateKeysFromFile(keys, keyboardType):
    usedId = []
    result = []

    if keyboardType != "standard":
        raise Exception("ERROR\n", "\tnon \"standard\" type of keyboard not supported now")

    for key in keys:
        if key["id"] in usedId:
            raise Exception("ITS FUCKING ERROR!!!! RED ALARM!!!! | error u have non individual id for keys", key)
        elif key["id"] in (list(range(15, 28)) + list(range(29, 40)) + list(range(42, 52))):
            result.append(Key(key))

        usedId.append(key["id"])

    return result


def validationFields(self, layout):
    for field in layout:
        if field in "label author moreInfoUrl moreInfoText fingerStart keyboardType keys":
            match field:
                case "keyboardType":
                    self.keyboardType = layout["keyboardType"]
                case "keys":
                    self.keys = generateKeysFromFile(layout["keys"], self.keyboardType)
                    # print(self.keys)
                case "fingerStart":
                    self.fingerStart = searchStartKeyFromId(layout["fingerStart"], layout["keys"])
                case "author":
                    self.author = layout["author"]
                case "moreInfoUrl":
                    self.moreInfoUrl = layout["moreInfoUrl"]
                case "moreInfoText":
                    self.moreInfoText = layout["moreInfoText"]
        else:
            print("some field in json of layout not valid:\t" + field + "\n")


class KeyboardLayout(object):
    def __init__(self, layoutDict):
        self.label = layoutDict["label"]
        self.keyboardType = "standard"
        self.keys = getQwertyKeys()
        self.fingerStart = getQwertyStartKeys()

        # for key in getQwertyKeys():
        #     print(key.getPrimaryChar(), key.getKeyId())

        validationFields(self, layoutDict)

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

