import json

#   json file structure (Keyboard layout analizer)
#   -   label
#   -   author
#   -   moreInfoUrl
#   -   moreInfoText
#   -   fingerStart
#   -   keyboardType
#   -   keys

class Key(object):
    def __init__(self, someKey, index):
        self.primary = someKey["primary"]
        self.shift = someKey["shift"]
        self.finger = someKey["finger"]
        self.id = someKey["id"]

        if index < 14:
            self.position = (index, 0)
        elif index < 28:
            self.position = (index + 0.25, 0)
        elif index < 40:
            self.position = (index + 0.5, 0)
        else:
            self.position = (-999, -999)

    def getFingerID(self):
        return self.finger

    def getPosition(self):
        return self.position

    def getPrimary(self):
        return self.primary

    def getKeyID(self):
        return self.id


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
                    self.keys[:13],
                    self.keys[14:27],
                    self.keys[28:]
                ]
