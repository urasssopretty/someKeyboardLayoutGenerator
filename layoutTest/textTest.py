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