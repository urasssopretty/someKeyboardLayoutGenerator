def fingerStats(layout, text):
    keys = layout.getKeys()
    keysPrimary = []
    keysUnderEachFinger = layout.getKeysUnderEachFinger()
    keyStats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for key in keys:
        keysPrimary.append(key.getPrimaryChar())

    for letter in text:
        for finger in range(10):
            if finger == 4 or finger == 5:
                continue

            for key in keysUnderEachFinger[finger]:
                if key.getPrimaryChar() == letter:
                    keyStats[finger] += 1

    return keyStats


def charStats(abc, text):
    charCounterList = []
    charCounterDict = {}

    for index in range(len(abc)):
        charCounterList.append(0)

    for letter in abc:
        charCounterDict[letter] = 0

    for char in text:
        for index in range(len(abc)):
            if abc[index] == char:
                charCounterList[index] += 1

    for index in range(len(abc)):
        charCounterDict[abc[index]] = charCounterList[index]

    # return charCounterList
    return charCounterDict
    # return counterArr, counterDict
