import math


def classicDistanceTest(keyboardLayout, fileName):
    ### in this text pos of fingers always at start poses (home row)
    text = open(fileName).read().lower().replace(' ', '')
    keys = keyboardLayout.getKeys()
    startPoses = keyboardLayout.getFingerStart()
    keysUnderEachFinger = keyboardLayout.getKeysUnderFingers()
    distance = 0

    for letter in text:
        for fingerIndex in range(10):
            if fingerIndex == 4 or fingerIndex == 5:
                continue

            for key in keysUnderEachFinger[fingerIndex]:
                if key.getPrimaryChar() == letter:
                    if key != startPoses[fingerIndex]:
                        distance += math.dist(startPoses[fingerIndex].getPosition(), key.getPosition())
    return distance


def oldSomeDistanceTest(keyboardLayout, fileName):
    text = open(fileName).read().lower().replace(' ', '')  # .replace('\n', '')
    keys = keyboardLayout.getKeys()
    startPoses = keyboardLayout.getFingerStart()
    keysUnderFingers = keyboardLayout.getKeysUnderFingers()
    lastKey = startPoses
    distance = 0

    for letter in text:
        for fingerIndex in range(10):
            if fingerIndex == 4 or fingerIndex == 5:
                continue

            for key in keysUnderFingers[fingerIndex]:
                if key.getPrimaryChar() == letter and key != lastKey[fingerIndex]:
                    distance += math.dist(lastKey[fingerIndex].getPosition(), key.getPosition())
                    lastKey[fingerIndex] = key
                    break

    return distance


def someDistanceTest(keyboardLayout, fileName):
    text = open(fileName).read().lower().replace(' ', '')
    keys = keyboardLayout.getKeys()
    startPoses = keyboardLayout.getFingerStart()
    keysUnderFingers = keyboardLayout.getKeysUnderFingers()
    lastKey = startPoses
    distance = 0
    counterOfSteps = [[] for _ in range(10)]

    return 0

