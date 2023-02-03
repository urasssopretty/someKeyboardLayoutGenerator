def distanceTest(KeyboardLayout, textFileName):
    text = open(textFileName).read().lower()
    keys = KeyboardLayout.getKeys()
    startPoses = KeyboardLayout.getFingerStart()
    keysUnderEachFinger = KeyboardLayout.getKeysUnderEachFinger()

    counter = 0
    # for letter in text:
    #     for fingerIndex in range(10):
    #         for key in keysUnderEachFinger[fingerIndex]:
    #             # if key.primary == letter and key.primary == startPoses[fingerIndex]:\
    #             # print(startPoses[fingerIndex])
    #             if key.primary == startPoses[fingerIndex]:
    #                 print("pipka")
                #     counter += 1

    return counter