import json
from layoutTests.distance import distanceTest
from layoutTests.distance import classicDistanceTest
from classKeyboardLayout import KeyboardLayout


def main():
    # layoutFileName = "myQwerty.txt"
    layoutFileName = "qwerty.txt"
    layoutFile = json.loads(open(layoutFileName).read())

    layout = KeyboardLayout(layoutFile)

    for key in layout.getKeys():
            print(key.getPrimary(), key.getPosition())

    # print(layout.getRows())
    print('%.3f' % classicDistanceTest(layout, "somenews.txt"))
    print('%.3f' % distanceTest(layout, "somenews.txt"))


if __name__ == '__main__':
    main()
