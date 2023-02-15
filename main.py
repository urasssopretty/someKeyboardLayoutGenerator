import json
from layoutTests.distance import distanceTest
from layoutTests.distance import classicDistanceTest
from classKeyboardLayout import KeyboardLayout


def main():
    layoutFileName = "layouts/normalQwerty.txt"
    layoutFile = json.loads(open(layoutFileName).read())
    layout = KeyboardLayout(layoutFile)

    # for key in layout.getKeys():
    #     print(key.getPrimary(), key.getPosition())

    print('%.3f' % classicDistanceTest(layout, "testTextes/somenews.txt", "metric"))
    print('%.3f' % distanceTest(layout, "testTextes/somenews.txt"))


if __name__ == '__main__':
    main()
