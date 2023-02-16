#   JSON FILE STRUCTURE (by Keyboard layout analyzer)
#   label           -   name of layout
#   author          -   author name
#   moreInfoUrl     -   more information about layout
#   moreInfoText    -   brief description of the layout
#   fingerStart     -   list of id keys that should have a finger on it at the start of typing
#                       but in class its LIST OF KEYS
#   keyboardType    -   type of keyboard (how many keys, what form factor) (standard type its ANSI layout with 101/104 keys)
#   keys            -   list of keys

### FILE STRUCTURE MUST CONTAIN THE FOLLOWING FIELDS: label, fingerStart, keyboardType, keys


from classKeyboardKey import Key


class KeyboardLayout(object):
    def __init__(self, layoutFile):
        self.label = layoutFile["label"]
        self.keyboardType = layoutFile["keyboardType"]

        self.keys = []
        if self.keyboardType == "standard":
            keyList = layoutFile["keys"]
            for key in keyList:
                if 14 < key["id"] < 28\
                        or 28 < key["id"] < 40\
                        or 41 < key["id"] < 51:
                    self.keys.append(Key(key, "standard", ))
        else:
            print("ERROR\n", "\tnon \"standard\" type of keyboard not supported now")

        self.fingerStart = []
        fingersStartKeyId = layoutFile["fingerStart"]

        for index in range(1, len(fingersStartKeyId) + 1):
            for key in self.keys:
                if fingersStartKeyId[str(index)] == key.getKeyId()\
                        or fingersStartKeyId[str(index)] == 56:
                    self.fingerStart.append(key)
                    break

        for jsonKey in layoutFile:
            if jsonKey == "author":
                self.author = layoutFile["author"]
            elif jsonKey == "moreInfoUrl":
                self.moreInfoUrl = layoutFile["moreInfoUrl"]
            elif jsonKey == "moreInfoText":
                self.moreInfoText = layoutFile["moreInfoText"]

    # def __init(self, label, keyboardType, keys, fingerStart, author="keyboard layout generator by primate"):
    #     self.label = label
    #     self.keyboardType = keyboardType
    #     self.keys = keys
    #     self.fingerStart = fingerStart
    #     self.author = author

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

class KeyboardLayoutFromFile(KeyboardLayout):
    def __init__(self, label, keyboardType, keys, fingerStart, author="", moreInfoUrl="", moreInfoText=""):
        self.label: label
        self.keyboardType: keyboardType
        self.keys: keys
        self.fingerStart: fingerStart

        if author == "":
            self.author = "keyboard layout generator by p8"
        else:
            self.author = author

        if moreInfoUrl != "":
            self.moreInfoUrl = moreInfoUrl

        if moreInfoText != "":
            self.moreInfoText = moreInfoText


