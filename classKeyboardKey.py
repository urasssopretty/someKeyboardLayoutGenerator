#   JSON KEY STRUCTURE (by keyboard layout analyzer)
#   primary --  char at non-shift layer
#   shift   --  char at shift layer (when u press SHIFT and some key)
#   finger  --  that should press this key (I think u can use other fingers if they make sense)
#   id      --  is key id (same key can have different key id at different keyboard (different type of kb))

### KEY STRUCTURE IN JSON FILE MUST CONTAIN THE FOLLOWING FIELDS: primary, finger, id


class Key(object):
    def __init__(self, keyStruct, keyboardType):
        for fieldName in keyStruct:
            # if fieldName == "shift" and keyStruct["shift"] > 0:
            if fieldName == "shift":
                self.shift = chr(keyStruct["shift"])
            elif fieldName not in "primary finger id":
                print("file contains strange json-key in keys array\n",
                      "more info:\n",
                      keyStruct)

        self.primary = chr(keyStruct["primary"])
        self.finger = keyStruct["finger"]
        self.id = keyStruct["id"]

        #   I think about to add filed "size" for keys, but I want to have open "standard" of json keyb layout
        #   so now if key will be a wide (non 1u size) only if a next key have a some distance from pos of current key
        if keyboardType == "standard":
            if 14 < self.id < 28:
                self.position = (self.id - 13, .5)   #   -13.5 + .5
            elif 28 < self.id < 40:
                self.position = (self.id - 26.75, 1.5)   # -13.5 - 13 + .75
            elif 41 < self.id < 51:
                self.position = (self.id - 39.25, 2.5)   #  ....
            else:
                self.position = (-999, -999)
        else:
            self.position = (-9999, -9999)

    def createIsntanceFromFields(self, primary, finger, id, shift=0):
        self.primary: primary
        self.finger: finger
        self.id: id
        if shift:
            self.shift: shift

    def getPrimary(self):
        return self.primary

    def getFinger(self):
        return self.finger

    def getKeyId(self):
        return self.id

    def getPosition(self):
        return self.position

    def getShift(self):
        return hasattr(self, "shift") if self.shift else 0

    def getNullKey(self, fingerId=1):
        self.primary = None
        self.shift = None
        self.id = None
        self.finger = fingerId
        return self
