import json
from classKeyboardKey import Key

#   json file structure (by Keyboard layout analizer)
#   -   label
#   -   author
#   -   moreInfoUrl
#   -   moreInfoText
#   -   fingerStart
#   -   keyboardType
#   -   keys


class KeyboardLayout(object):
    def __init__(self, fileName):
        file = json.loads(open(fileName).read())
        self.label = file["label"]
        self.author = file["author"]
        self.moreInfoUrl = file["moreInfoUrl"]
        self.moreInfoText = file["moreInfoText"]
        self.keyboardType = file["keyboardType"]
        self.keys = []
        if self.keyboardType == "standard":
            for index in range(len(file["keys"])):
                self.keys.append(Key(file["keys"][index], index))
        self.fingerStart = []
        for index in range(1, 11):
            startKeyId = file["fingerStart"][str(index)]
            for key in self.keys:
                if startKeyId == key.getKeyID():
                    self.fingerStart.append(key)
                    break

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
        return  [
                    self.keys[:12],
                    self.keys[13:24],
                    self.keys[24:34]
        ]
