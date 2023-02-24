def fingerStats(layout, text):
    keysUnderFingers = layout.getKeysUnderFingers()
    keyStats = [0 for _ in range(10)]
    flag = False

    for letter in text:
        for finger in range(10):
            if finger == 4 and letter == " ":
                keyStats[4] += 1
                break

            for key in keysUnderFingers[finger]:
                if key.getPrimaryChar() == letter:
                    keyStats[finger] += 1
                    break

    return keyStats


def charStats(abc, text):
    charCounterList = [0 for _ in range(len(abc))]

    for char in text:
        for index in range(len(abc)):
            if abc[index] == char:
                charCounterList[index] += 1

    return dict(zip(abc, charCounterList))
