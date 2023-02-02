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
    def __init__(self, someKey):
        self.primaryLayer = someKey["primary"]
        self.shiftLayer = someKey["shift"]
        self.fingerID = someKey["finger"]
        self.keyID = someKey["id"]
    # def __init__(self, primary, shift, finger, someKeyid):
    #     self.primaryLayer = primary
    #     self.shiftLayer = shift
    #     self.fingerID = finger
    #     self.keyID = someKeyid

    def getFingerID(self):
        return self.fingerID


class KeyboardLayout(object):
    def __init__(self, fileName):
        file = json.loads(open(fileName).read())
        self.label = file["label"]
        self.author = file["author"]
        self.moreInfoUrl = file["moreInfoUrl"]
        self.moreInfoText = file["moreInfoText"]
        self.fingerStart = file["fingerStart"]
        self.keyboardType = file["keyboardType"]
        self.keys = []
        for keyIndex in range(len(file["keys"])):
            self.keys.append(Key(file["keys"][keyIndex]))
        # self.keys = file["keys"]

    def getKeys(self):
        return list(self.keys)

    def getFingerStart(self):
        return  list(self.fingerStart)

