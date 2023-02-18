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


from classKeyboardKey import Key


class KeyboardLayout(object):
    def __init__(self, layoutFile):
        self.label = layoutFile["label"]
        self.keyboardType = layoutFile["keyboardType"]

        self.keys = []
        if self.keyboardType == "standard":
            keyList = layoutFile["keys"]
            for key in keyList:
                if 14 < key["id"] < 28 \
                        or 28 < key["id"] < 40 \
                        or 41 < key["id"] < 51:
                    self.keys.append(Key(key, "standard", ))
        else:
            print("ERROR\n", "\tnon \"standard\" type of keyboard not supported now")

        self.fingerStart = []
        fingerStart = layoutFile["fingerStart"]

        for index in range(1, len(fingerStart) + 1):
            for key in self.keys:
                if fingerStart[str(index)] == key.getKeyId()\
                        or fingerStart[str(index)] == 56:
                    self.fingerStart.append(key)
                    break

        for jsonKey in layoutFile:
            if jsonKey == "author":
                self.author = layoutFile["author"]
            elif jsonKey == "moreInfoUrl":
                self.moreInfoUrl = layoutFile["moreInfoUrl"]
            elif jsonKey == "moreInfoText":
                self.moreInfoText = layoutFile["moreInfoText"]

    # @classmethod
    def initFromArgs(self, label, fingerStart, keys, author="", keyboardType="standard", moreInfoUrl="", moreInfoText=""):
        self.label = label
        self.fingerStart = fingerStart
        self.keyboardType = keyboardType
        self.keys = keys
        self.fingerStart = fingerStart

        if not author:
            self.author: "keyboard layout generator by urasssopretty"
        else:
            self.author: author

        self.moreInfoUrl = moreInfoUrl
        self.moreInfoText = moreInfoText

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

    def initAbcLayout(self):
