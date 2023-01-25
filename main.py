import json

from classLayout import keyboardLayout
import questionnaire
import textAnalysis
import testLayout


# changeZXCV = questionnaire.output()
# textAnalysis.output()
def main():
    layout = keyboardLayout("qwerty.txt")

    print(testLayout.distanceTestKeys(layout))
    # print(layout.getKeys())


if __name__ == '__main__':
    main()
