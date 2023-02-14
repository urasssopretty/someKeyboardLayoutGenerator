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
            somekeys = layoutFile["keys"]
            for key in somekeys:
                if key["primary"] > 0:
                    self.keys.append(Key(key, "standard"))
        else:
            print("ERROR\n", "\tnon \"standard\" type of keyboard not supported now")

        self.fingerStart = []
        startKeyId = layoutFile["fingerStart"]
        for keyID in startKeyId:
            for key in self.keys:
                if keyID == key.getKeyID():
                    self.fingerStart.append(key)
                    break

        # for index in range(1, 11):
        #     startKeyId = layoutFile["fingerStart"][str(index)]
        #     for key in self.keys:
        #         if startKeyId == key.getKeyID():
        #             self.fingerStart.append(key)
        #             break

        for jsonKey in layoutFile:
            if jsonKey == "author":
                self.author = layoutFile["author"]
            elif jsonKey == "moreInfoUrl":
                self.moreInfoUrl = layoutFile["moreInfoUrl"]
            elif jsonKey == "moreInfoText":
                self.moreInfoText = layoutFile["moreInfoText"]

    def getKeys(self):
        return list(self.keys)

    def getFingerStart(self):
        return list(self.fingerStart)

    def getKeysUnderEachFinger(self):
        keysUnderEachFinger = [[], [], [], [], [], [], [], [], [], []]

        for key in self.keys:
            for keyIndex in range(10):
                # if key["finger"] == (keyIndex + 1):
                if key.getFingerID() == (keyIndex + 1):
                    keysUnderEachFinger[keyIndex].append(key)

        return keysUnderEachFinger

    def getRows(self):
        if self.keyboardType == "standard":
            return  [
                        self.keys[13:28],
                        self.keys[29:41],
                        self.keys[42:53:]
                    ]
            # return  [
            #             self.keys[:12],
            #             self.keys[13:24],
            #             self.keys[24:34]
            #         ]
        else:
            return -999
