#   JSON KEY STRUCTURE (by keyboard layout analyzer)
#   primary --  char at non-shift layer
#   shift   --  char at shift layer (when u press SHIFT and some key)
#   finger  --  that should press this key (I think u can use other fingers if they make sense)
#   id      --  is key id (same key can have different key id at different keyboard (different type of kb))

### KEY STRUCTURE IN JSON FILE MUST CONTAIN THE FOLLOWING FIELDS: primary, finger, id


class Key(object):
    def __init__(self, keyStruct, keyboardType="standard"):
        for field in keyStruct:
            if field in "primary shift finger id":
                match field:
                    case "primary":
                        self.primary = chr(keyStruct["primary"])
                    case "shift":
                        self.shift = chr(keyStruct["shift"])
                    case "finger":
                        self.finger = keyStruct["finger"]
                    case "id":
                        self.id = keyStruct["id"]
            else:
                print("layout file contains strange json-key in list of keys:\t", field, end="\n\n")

        #   TODO rewrite this shit because id can be any
        if keyboardType == "standard":
            if 14 < self.id < 28:
                self.position = (self.id - 13, .5)   #   -13.5 + .5
            elif 28 < self.id < 40:
                self.position = (self.id - 26.75, 1.5)   # -13.5 - 13 + .75
            elif 41 < self.id < 52:
                self.position = (self.id - 39.25, 2.5)   #  ....
            else:
                self.position = (-999, -999)
        else:
            print("current version of layout generator dont work with non-standard keyb type | error in layout class in __init__ method", "\n\n\tkeyb type is:\t", keyboardType)

    def getPrimaryChar(self):
        return self.primary

    def getFinger(self):
        return self.finger

    def getKeyId(self):
        return self.id

    def getPosition(self):
        return self.position

    def getShiftChar(self):
        return self.shift
        # return hasattr(self, "shift") if self.shift else 0

    # def getNullKey(self, fingerId=0):
    #     self.primary = None
    #     self.shift = None
    #     self.id = None
    #     self.finger = fingerId
    #     return self
