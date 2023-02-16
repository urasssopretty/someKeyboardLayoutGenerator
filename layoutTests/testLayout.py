import math
# from classKeyboardLayout import KeyboardLayout

class LayoutTest(object):
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

    def distanceTest(KeyboardLayout, textFileName):
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

    def fingerStats(layout, fileName):
        text = open(fileName).read()
        # text = open(fileName).read().replace(' ', '')
        keys = layout.getKeys()
        keysPrimary = []
        keysUnderEachFinger = layout.getKeysUnderEachFinger()
        keyStats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for key in keys:
            keysPrimary.append(key.getPrimary())

        for letter in text:
            for finger in range(10):
                if finger == 4 or finger == 5:
                    continue

                for key in keysUnderEachFinger[finger]:
                    if key.getPrimary() == letter:
                        keyStats[finger] += 1

        return keyStats

