import math


def classicDistanceTest(keyboardLayout, fileName):
    ### in this test position of fingers always at start poses (home row)
    text = open(fileName).read().lower().replace(' ', '')
    startPoses = keyboardLayout.getFingerStart()
    keysUnderEachFinger = keyboardLayout.getKeysUnderFingers()
    distance = 0

    for letter in text:
        for fingerIndex in range(10):
            if fingerIndex in (4, 5):
                continue

            for key in keysUnderEachFinger[fingerIndex]:
                if key.getPrimaryChar() == letter:
                    if key != startPoses[fingerIndex]:
                        distance += math.dist(startPoses[fingerIndex].getKeyPostion(), key.getKeyPostion())
    return distance


def oldSomeDistanceTest(keyboardLayout, fileName):
    ### in this test position of fingers is last key what they pressed (only in area what contains keys for that fingers)
    text = open(fileName).read().lower().replace(' ', '')
    keysUnderFingers = keyboardLayout.getKeysUnderFingers()
    lastKey = keyboardLayout.getFingerStart()
    distance = 0

    for letter in text:
        for fingerIndex in range(10):
            if fingerIndex in (4, 5):
                continue

            for key in keysUnderFingers[fingerIndex]:
                if key.getPrimaryChar() == letter and key != lastKey[fingerIndex]:
                    distance += math.dist(lastKey[fingerIndex].getKeyPostion(), key.getKeyPostion())
                    lastKey[fingerIndex] = key
                    break

    return distance


### TODO: try to understand why there another distance if i dont rewrite it \
### TODO: rewrite it: fingers should come back to fingerStart positions after 2-3 ticks
def someDistanceTest(keyboardLayout, fileName):
    text = open(fileName).read().lower().replace(' ', '')
    startPoses = keyboardLayout.getFingerStart()
    lastKey = startPoses
    keysUnderFingers = keyboardLayout.getKeysUnderFingers()
    counterOfSteps = [0 for _ in range(10)]
    distance = 0

    for letter in text:
        for fingerIndex in range(10):
            if fingerIndex in (4, 5):
                continue

            if counterOfSteps[fingerIndex] >= 1:
                lastKey[fingerIndex] = startPoses[fingerIndex]
                counterOfSteps[fingerIndex] = 0

            for key in keysUnderFingers[fingerIndex]:
                counterOfSteps[fingerIndex] += 1
                if key.getPrimaryChar() == letter and key != lastKey[fingerIndex]:
                    distance += math.dist(lastKey[fingerIndex].getKeyPostion(), key.getKeyPostion())
                    lastKey[fingerIndex] = key
                    break

    return distance

