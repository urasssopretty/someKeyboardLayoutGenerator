import math

# def classicDistanceTest(KeyboardLayout, textFileName, outputMetrics="default"):
def classicDistanceTest(KeyboardLayout, textFileName):
    ### in this text pos of fingers always at start poses (home row)
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

def someDistanceTest(KeyboardLayout, textFileName):
    text = open(textFileName).read().lower().replace(' ', '')  # .replace('\n', '')
    keys = KeyboardLayout.getKeys()
    startPoses = KeyboardLayout.getFingerStart()
    keysUnderEachFinger = KeyboardLayout.getKeysUnderEachFinger()
    lastKey = startPoses
    distance = 0

    for letter in text:
        for fingerIndex in range(10):
            if fingerIndex == 4 or fingerIndex == 5:
                continue

            for key in keysUnderEachFinger[fingerIndex]:
                if key.getPrimary() == letter and key != lastKey[fingerIndex]:
                    distance += math.dist(lastKey[fingerIndex].getPosition(), key.getPosition())
                    lastKey[fingerIndex] = key
                    break

    return distance


