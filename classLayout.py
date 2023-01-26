import json

#   json file structure (Keyboard layout analizer)
#   -   label
#   -   author
#   -   moreInfoUrl
#   -   moreInfoText
#   -   fingerStart
#   -   keyboardType
#   -   keys

class singleKey(object):
    def __init__(self, primary, shift, finger, someKeyid):
        self.primaryLayer = primary
        self.shiftLayer = shift
        self.fingerID = finger
        self.keyID = someKeyid

class keyboardLayout(object):
    def __init__(self, fileName):
        file = json.loads(open(fileName).read())
        self.label = file["label"]
        self.author = file["author"]
        self.moreInfoUrl = file["moreInfoUrl"]
        self.moreInfoText = file["moreInfoText"]
        self.fingerStart = file["fingerStart"]
        self.keyboardType = file["keyboardType"]
        self.keys = file["keys"]

    def getKeys(self):
        return list(self.keys)

