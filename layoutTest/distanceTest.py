import math


def classicDistanceTest(keyboardLayout, fileName):
    ### in this test position of fingers always at start poses (home row)
    text = open(fileName).read().lower().replace(' ', '')
    startPoses = keyboardLayout.getFingerStart()

    # for key in startPoses:
    #     print(key.getPrimaryChar())
    #
    # print("\t len", len(startPoses))

    keysUnderEachFinger = keyboardLayout.getKeysUnderFingers()
    distance = 0

    ### TODO rewrite it for more performance
    ### не гонять все десять пальцев, а смотреть есть ли чар в списке чаров какого-либо пальца и тогда уже считать дистанцию
    for letter in text:

        # print(letter)

        for fingerIndex in range(10):
            if fingerIndex in (4, 5):
                continue

            # print("\t", fingerIndex)

            for key in keysUnderEachFinger[fingerIndex]:
                if key.getPrimaryChar() == letter and key != startPoses[fingerIndex]:
                    distance += math.dist(startPoses[fingerIndex].getPosition(), key.getPosition())

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
                    distance += math.dist(lastKey[fingerIndex].getPosition(), key.getPosition())
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
                    distance += math.dist(lastKey[fingerIndex].getPosition(), key.getPosition())
                    lastKey[fingerIndex] = key
                    break

    return distance

