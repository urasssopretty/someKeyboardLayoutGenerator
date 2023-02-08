#   JSON KEY STRUCTURE (by keyboard layout analyzer)
#   primary --  char at non-shift layer
#   shift   --  char at shift layer (when u press SHIFT and some key)
#   finger  --  that should press this key (I think u can use other fingers if they make sense)
#   id      --  is key id (same key can have different key id at different keyboard (different type of kb))

### KEY STRUCTURE IN JSON FILE MUST CONTAIN THE FOLLOWING FIELDS: primary, finger, id

class Key(object):
    def __init__(self, keyStruct, index, keyboardType):
        for jsonKey in keyStruct:
            if jsonKey == "shift":
                self.shift = keyStruct["shift"]
            elif jsonKey not in "primary finger id":
                print("file contains strange json-key in keys\n",
                      "more info:\n",
                      keyStruct)

        self.primary = keyStruct["primary"]
        self.finger = keyStruct["finger"]
        self.id = keyStruct["id"]

        if keyboardType == "standard":
            if self.id == 0:
                self.position = (0, 0)
            elif 0 < self.id < 5:
                self.position = (1 + self.id, 0)
            elif 4 < self.id < 9:
                self.position = (, 0)
            elif 0 < self.id < 5:
                self.position = (2, 0)



            # if keyID < 13:
            #     self.position = (';', 0)
            # elif keyID < 24:
            #     self.position = (index + 0.25, 1)
            # elif keyID < 34:
            #     self.position = (index + 0.5, 2)
            # else:
            #     self.position = (-999, -999)
        else:
            self.position(-9999, -9999)

    def getFingerID(self):
        return self.finger

    def getPosition(self):
        return self.position

    def getPrimary(self):
        return self.primary

    def getKeyID(self):
        return self.id