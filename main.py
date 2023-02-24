import json
import string
from layoutTest.distanceTest import *

from classKeyboardLayout import *
from layoutGenerator import *


def main():
    # textFileName = "testTexts/alice_in_wonderland.txt"
    layoutFileName = "layouts/normalQwerty.txt"
    layoutFile = json.loads(open(layoutFileName).read())
    layout = KeyboardLayout(layoutFile)

    # for key in layout.getKeys():
    #     print(key.getPrimaryChar(), key.getPosition(), key.getKeyId())

    # print(charStats(string.ascii_lowercase, open("testTexts/alice_in_wonderland.txt").read()))

    textFileName = "testTexts/somenews.txt"
    print("classic distance test:", '%.3f' % classicDistanceTest(layout, textFileName))
    print("distance test:", '%.3f' % oldSomeDistanceTest(layout, textFileName))
    # print("distance test:", '%.3f' % someDistanceTest(layout, textFileName))
    # print("finger stats:", end=" ")
    # for element in fingerStats(layout, textFileName): print(element, end=" ")


if __name__ == '__main__':
    main()
