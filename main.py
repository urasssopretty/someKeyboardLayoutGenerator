import json
from layoutTests.testLayout import LayoutTest
from classKeyboardLayout import KeyboardLayout


def main():
    layoutFileName = "layouts/normalQwerty.txt"
    layoutFile = json.loads(open(layoutFileName).read())
    layout = KeyboardLayout(layoutFile)

    textFileName = "testTextes/somenews.txt"

    print('%.3f' % LayoutTest.classicDistanceTest(layout, textFileName),
          '%.3f' % LayoutTest.distanceTest(layout, textFileName),
          LayoutTest.fingerStats(layout, textFileName)
    )


if __name__ == '__main__':
    main()
