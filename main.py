import json

from classLayout import keyboardLayout
import questionnaire
import textAnalysis
import testLayout


# changeZXCV = questionnaire.output()
# textAnalysis.output()
def main():
    file = open("qwerty.txt").read()
    fileLayout = json.loads(file)

    layout = keyboardLayout(fileLayout["label"], fileLayout["fingerStart"], fileLayout["keys"])

    print(testLayout.distanceTestKeys(layout))


if __name__ == '__main__':
    main()
