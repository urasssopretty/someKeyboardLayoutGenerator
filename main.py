import json
from classKeyboardLayout import *
from generators.layoutGenerator import *


def main():
    layoutFileName = "layouts/normalQwerty.txt"
    layoutFile = json.loads(open(layoutFileName).read())
    layout = KeyboardLayout(layoutFile)

    # print(layout.getLabel())

    # for row in layout.getRows():
    #     for key in row:
    #         print(key.getPrimaryChar(), key.getPosition(), key.getKeyId())
    #     print()

    someTextFileName = "testTexts/alice_in_wonderland.txt"
    # someFile = open(someTextFileName).read()
    # print(charStats(string.ascii_lowercase, someFile))
    #
    # print("finger stats:", end=" ")
    # for element in fingerStats(layout, someFile):
    #     print(element, end=" ")

    # textFileName = "testTexts/somenews.txt"
    # print("classic distance test:", '%.3f' % classicDistanceTest(layout, textFileName))
    # print("distance test:", '%.3f' % oldSomeDistanceTest(layout, textFileName))
    # print("new distance test:", '%.3f' % someDistanceTest(layout, textFileName))

    mathLayoutGenerator(someTextFileName, "standard")


if __name__ == '__main__':
    main()
