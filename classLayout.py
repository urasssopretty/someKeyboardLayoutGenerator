import testLayout
import json

class singleKey(object):
    def __init__(self, primary, shift, finger, someKeyid):
        self.primaryLayer = primary
        self.shiftLayer = shift
        self.fingerID = finger
        self.keyID = someKeyid

#   struct of json
#   -   label
#   -   author
#   -   moreInfoUrl
#   -   moreInfoText
#   -   fingerStart
#   -   keyboardType
#   -   keys

class keyboardLayout(object):
    # def __init__(self, label, author, moreInfoUrl, moreInfoText, fingerStart, keyboardType, keys):
    # self.keys = keys
    # self.author = author
    # self.moreInfoUrl = moreInfoUrl
    # self.moreInfoText = moreInfoText
    # self.fingerStartKeys = fingerStart
    # self.keyboardType = keyboardType
    # self.keys = keys

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

    def createLayoutFromFile(self, fileName):
        layout = json.loads(fileName)
        return keyboardLayout

