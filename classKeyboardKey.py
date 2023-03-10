#   JSON KEY STRUCTURE (by keyboard layout analyzer)
#   primary --  char at non-shift layer
#   shift   --  char at shift layer (when u press SHIFT and some key)
#   finger  --  that should press this key (I think u can use other fingers if they make sense)
#   id      --  is key id (same key can have different key id at different keyboard (different type of kb))

### KEY STRUCTURE IN JSON FILE MUST CONTAIN THE FOLLOWING FIELDS: primary, finger, id

def validateKeyboardType(keyboardType):
    if keyboardType != "standard":
        raise Exception("non standard keyboard type!!! | now its dont work")


def validateFields(keyStruct):
    presenceCounter = 0
    requiredFields = "primary finger id".split(" ")

    for field in keyStruct:
        if field not in "primary shift finger id position":
            print("layout file contains strange json-key in list of keys:\t", field)
        elif field in requiredFields:
            presenceCounter += 1

    if presenceCounter != len(requiredFields):
        raise Exception("key must contains next fields:\t", "primary, finger, id", keyStruct)


class Key(object):
    def __init__(self, keyStruct, keyboardType="standard"):
        validateKeyboardType(keyboardType)
        validateFields(keyStruct)

        self.position = [-999, -999]

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
                case "position":
                    self.position = keyStruct[field]

        if self.position == [-999, -999]:
            deltaX = [13, 26.75, 39.25]
            idRanges = [list(range(15, 28)), list(range(29, 40)), list(range(42, 52))]

            for index in range(len(idRanges)):
                if self.id in idRanges[index]:
                    self.position = [self.id - deltaX[index], index + 0.5]

    def getPrimaryChar(self):
        return self.primary

    def getFinger(self):
        return self.finger

    def getKeyId(self):
        return self.id

    def getPosition(self):
        return self.position

