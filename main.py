import json
from layoutTest.distanceTest import *
from layoutTest.textTest import *
from classKeyboardLayout import *


def main():
    layoutFileName = "layouts/normalQwerty.txt"
    layoutFile = json.loads(open(layoutFileName).read())
    layout = KeyboardLayout(layoutFile)

    textFileName = "testTextes/somenews.txt"

    print("classic distance test:", '%.3f' % classicDistanceTest(layout, textFileName))
    print("distance test:", '%.3f' % someDistanceTest(layout, textFileName))
    print("finger stats:", end=" ")
    for element in fingerStats(layout, textFileName): print(element, end=" ")


if __name__ == '__main__':
    main()
