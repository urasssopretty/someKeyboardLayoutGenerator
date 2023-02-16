import json
from layoutTests.testLayout import LayoutTest
from classKeyboardLayout import KeyboardLayout
# from layoutTests.fingerStats import fingerStats
# from layoutTests.distanceTest import distanceTest
# from layoutTests.distanceTest import classicDistanceTest


def main():
    layoutFileName = "layouts/normalQwerty.txt"
    layoutFile = json.loads(open(layoutFileName).read())
    layout = KeyboardLayout(layoutFile)

    # for key in layout.getKeys():
    #     print(key.getPrimary(), key.getPosition())

    # print('%.3f' % classicDistanceTest(layout, "testTextes/somenews.txt", "metric"))
    # print('%.3f' % distanceTest(layout, "testTextes/somenews.txt"))
    print(LayoutTest.fingerStats("testTextes/somenews.txt", layout))

if __name__ == '__main__':
    main()
