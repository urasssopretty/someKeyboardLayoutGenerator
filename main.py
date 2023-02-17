import json
from layoutTest.distanceTest import *

from classKeyboardLayout import *
from layoutGenerator import *


def main():
    layoutFileName = "layouts/normalQwerty.txt"
    layoutFile = json.loads(open(layoutFileName).read())
    layout = KeyboardLayout(layoutFile)

    # charStats(open("testTextes/alice_in_wonderland.txt").read())

    # rows = layout.getRows()
    # for row in rows:
    #     for key in row:
    #         print("#" + str(key.getKeyId()), key.getPrimary(), key.getPosition())

    # textFileName = "testTextes/somenews.txt"

    # print("classic distance test:", '%.3f' % classicDistanceTest(layout, textFileName))
    # print("distance test:", '%.3f' % someDistanceTest(layout, textFileName))
    # print("finger stats:", end=" ")
    # for element in fingerStats(layout, textFileName): print(element, end=" ")


if __name__ == '__main__':
    main()
