
class Key(object):
    def __init__(self, someKey, index):
        self.primary = someKey["primary"]
        self.shift = someKey["shift"]
        self.finger = someKey["finger"]
        self.id = someKey["id"]

        if index < 13:
            self.position = (index, 0)
        elif index < 24:
            self.position = (index + 0.25, 1)
        elif index < 34:
            self.position = (index + 0.5, 2)
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