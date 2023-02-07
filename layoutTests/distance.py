import math

### test when pos of fingers is start pos at home row
def classicDistnceTest(KeyboardLayout, textFileName):
    text = open(textFileName).read().lower().replace(' ', '')
    keys = KeyboardLayout.getKeys()
    startPoses = KeyboardLayout.getFingerStart()
    keysUnderEachFinger = KeyboardLayout.getKeysUnderEachFinger()
    totalDistance = 0

    for letter in text:
        for fingerIndex in range(5):
            if fingerIndex == 4 or fingerIndex == 5:
                break

            for key in keysUnderEachFinger[fingerIndex]:
                if key.getPrimary() == letter:
                    if key != startPoses[fingerIndex]:
                        totalDistance += math.`dist`(startPoses[fingerIndex], key.getPosition())

    return totalDistance

def distanceTest(KeyboardLayout, textFileName):
    text = open(textFileName).read().lower()
    keys = KeyboardLayout.getKeys()
    # startPoses = KeyboardLayout.getFingerStart()
    keysUnderEachFinger = KeyboardLayout.getKeysUnderEachFinger()
    lastKey = keysUnderEachFinger
    totalDistance = 0

    # print(keysUnderEachFinger[0][1].getPrimary())
    for letter in text:
        for fingerIndex in range(10):
            # print(type(keysUnderEachFinger[fingerIndex][0]))
            for key in keysUnderEachFinger[fingerIndex]:
                if key.getPrimary() == letter:
                    if key != lastKey[fingerIndex]:
                        totalDistance += math.dist(lastKey[fingerIndex].getPostion(), key.getPosition())
                        lastKey[fingerIndex] = key
                        continue
            continue
        break

    return totalDistance