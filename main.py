import json
from classKeyboardLayout import *
from generators.layoutGenerator import *
from layoutTest.distanceTest import *


def main():
    layoutFileName = "layouts/normalQwerty.txt"
    layoutFile = json.loads(open(layoutFileName).read())
    layout = KeyboardLayout(layoutFile)

    someTextFileName = "testTexts/alice_in_wonderland.txt"
    generatedLayout = mathLayoutGenerator(someTextFileName, "standard")

    textFileName = "testTexts/somenews.txt"

    print("\nqwerty layout:")
    print("classic distance test:", '%.3f' % classicDistanceTest(layout, textFileName))
    print("distance test:", '%.3f' % oldSomeDistanceTest(layout, textFileName))
    # print("new distance test:", '%.3f' % someDistanceTest(layout, textFileName))

    print("\ngenerated layout:")
    print("classic distance test:", '%.3f' % classicDistanceTest(generatedLayout, textFileName))
    print("distance test:", '%.3f' % oldSomeDistanceTest(generatedLayout, textFileName))

    colemak = KeyboardLayout(json.loads(open("layouts/colemak.txt").read()))
    print("\ncolemak layout:")
    print("classic distance test:", '%.3f' % classicDistanceTest(colemak, textFileName))
    print("distance test:", '%.3f' % oldSomeDistanceTest(colemak, textFileName))
    # print("new distance test:", '%.3f' % someDistanceTest(generatedLayout, textFileName))


if __name__ == '__main__':
    main()
