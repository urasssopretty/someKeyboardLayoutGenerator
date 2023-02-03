import json

from layoutTests.distance import distanceTest
from classLayout import KeyboardLayout
# import questionnaire
# import textAnalysis
# import testLayout

# changeZXCV = questionnaire.output()
# textAnalysis.output()
def main():
    layoutFileName= "myQwerty.txt"
    layout = KeyboardLayout(layoutFileName)

    print(distanceTest(layout, "somenews.txt"))

    # print(testLayout.distanceTestKeys(layout))
    # print(layout.getKeys())

if __name__ == '__main__':
    main()
