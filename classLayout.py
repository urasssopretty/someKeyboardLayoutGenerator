import testLayout
import json

class singleKey(object):
    def __init__(self, primary, shift, finger, someKeyid):
        self.primaryLayer = primary
        self.shiftLayer = shift
        self.fingerID = finger
        self.keyID = someKeyid


class keyboardLayout(object):
    def __init__(self, label, author="", fingerStart, keys):
        self.label = label
        self.fingerStartKeys = fingerStart
        self.keys = keys

    def getKeys(self):
        return list(self.keys)

    def createLayoutFromFile(self, fileName):
        layout = json.loads(fileName)
        return keyboardLayout

