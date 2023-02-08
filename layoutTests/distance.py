import math


### test when pos of fingers is start pos at home row
def classicDistanceTest(KeyboardLayout, textFileName):
    text = open(textFileName).read().lower().replace(' ', '')
    keys = KeyboardLayout.getKeys()
    startPoses = KeyboardLayout.getFingerStart()
    keysUnderEachFinger = KeyboardLayout.getKeysUnderEachFinger()
    distance = 0

    for letter in text:
        for fingerIndex in range(10):
            if fingerIndex == 4 or fingerIndex == 5:
                continue

            for key in keysUnderEachFinger[fingerIndex]:
                if key.getPrimary() == letter:
                    if key != startPoses[fingerIndex]:
                        distance += math.dist(startPoses[fingerIndex].getPosition(), key.getPosition())

    return distance


def distanceTest(KeyboardLayout, textFileName):
    text = open(textFileName).read().lower().replace(' ', '')
    keys = KeyboardLayout.getKeys()
    startPoses = KeyboardLayout.getFingerStart()
    keysUnderEachFinger = KeyboardLayout.getKeysUnderEachFinger()
    lastKey = startPoses
    totalDistance = 0

    for letter in text:
        for fingerIndex in range(10):
            if fingerIndex == 4 or fingerIndex == 5:
                continue
            # print(fingerIndex)
            for key in keysUnderEachFinger[fingerIndex]:
                if key.getPrimary() == letter and key != lastKey[fingerIndex]:
                    totalDistance += math.dist(lastKey[fingerIndex].getPosition(), key.getPosition())
                    lastKey[fingerIndex] = key
                    continue
        break

    return totalDistance
