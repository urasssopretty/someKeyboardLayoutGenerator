import json

#   json file structure (Keyboard layout analizer)
#   -   label
#   -   author
#   -   moreInfoUrl
#   -   moreInfoText
#   -   fingerStart
#   -   keyboardType
#   -   keys

# class Key(object):
#     def __init__(self, someKey):
#         self.primary = someKey["primary"]
#         self.shift = someKey["shift"]
#         self.finger = someKey["finger"]
#         self.id = someKey["id"]

    # def getFingerID(self):
    #     return self.finger


class KeyboardLayout(object):
    def __init__(self, fileName):
        file = json.loads(open(fileName).read())
        self.label = file["label"]
        self.author = file["author"]
        self.moreInfoUrl = file["moreInfoUrl"]
        self.moreInfoText = file["moreInfoText"]
        self.fingerStart = []
        for index in range(1, 11):
            self.fingerStart.append(file["fingerStart"][str(index)])

        self.keyboardType = file["keyboardType"]
        self.keys = file["keys"]
        # for keyIndex in range(len(file["keys"])):
        #     self.keys.append(Key(file["keys"][keyIndex]))
        print(self.keys[0])
        # self.keys = file["keys"]

    def getKeys(self):
        return list(self.keys)

    def getFingerStart(self):
        return  list(self.fingerStart)

    def getKeysUnderEachFinger(self):
        keysUnderEachFinger = [[], [], [], [], [], [], [], [], [], []]

        for key in self.keys:
            for keyIndex in range(10):
                # if key.getfingeris( == (keyIndex + 1):
                if key["finger"] == (keyIndex + 1):
                    keysUnderEachFinger[keyIndex].append(key)

        return keysUnderEachFinger

    def getRows(self):
        return  [
                    self.keys[:13],
                    self.keys[14:27],
                    self.keys[28]
                ]
