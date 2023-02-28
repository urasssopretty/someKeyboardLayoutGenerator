#   JSON KEY STRUCTURE (by keyboard layout analyzer)
#   primary --  char at non-shift layer
#   shift   --  char at shift layer (when u press SHIFT and some key)
#   finger  --  that should press this key (I think u can use other fingers if they make sense)
#   id      --  is key id (same key can have different key id at different keyboard (different type of kb))

### KEY STRUCTURE IN JSON FILE MUST CONTAIN THE FOLLOWING FIELDS: primary, finger, id

def validateFields(keyStruct):
    # for field in keyStruct:
    #     if field not in "primary shift finger id":
    #         raise Exception("layout file contains strange json-key in list of keys:\t", field)
    # print(keyStruct.keys())
    somelist = "primary shift finger id".split(" ")

    if somelist not in keyStruct.keys:
        raise Exception("layout file contains strange json-key in list of keys:\t", keyStruct.keys)


class Key(object):
    def __init__(self, keyStruct, keyboardType="standard"):
        if keyboardType != "standard":
            raise Exception("non standard keyb type!!! | now its dont work")

        validateFields(keyStruct)

        for field in keyStruct:
            match field:
                case "primary":
                    self.primary = chr(keyStruct[field])
                case "shift":
                    self.shift = chr(keyStruct[field])
                case "finger":
                    self.finger = keyStruct[field]
                case "id":
                    self.id = keyStruct[field]

        self.position = (-999, -999)

        deltaX = [13, 26.75, 39.25]
        idRanges = [list(range(15, 28)), list(range(29, 40)), list(range(42, 52))]

        for index in range(len(idRanges)):
            if self.id in idRanges[index]:
                self.position = (self.id - deltaX[index], index - 0.5)

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
