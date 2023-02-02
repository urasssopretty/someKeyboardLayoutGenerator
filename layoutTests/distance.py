def distanceTest(KeyboardLayout, FileName):
    text = open(FileName).read().lower()
    keys = KeyboardLayout.getKeys()
    startPoses = KeyboardLayout.getFingerStart()

    # rows = [
    #     keys[:13],      #   UPPER ROW
    #     keys[14:27],    #   HOME ROW
    #     keys[28:]       #   BOTTOM ROW
    # ]

    # for i in range(keys.size()):
    #

    keysUnderEachFinger = [[], [], [], [], [], [], [], [], [], []]

    for key in keys:
        for keyIndex in range(10):
            lastUsedFingerIndex = key.getFingerID()
            if lastUsedFingerIndex == (keyIndex + 1):
                keysUnderEachFinger[keyIndex].append(lastUsedFingerIndex)

    for i in range(len(keysUnderEachFinger)):
        print(keysUnderEachFinger[i])

    return 0