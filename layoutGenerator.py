from classKeyboardLayout import *
from layoutTest.textTest import *


def mathLayoutGenerator(textFileName):
    abc = string.ascii_lowercase
    text = open(textFileName).read()
    charStatArr, charStatDict = charStats(text)
    # charStatDictValues = charStatDict.values()
    # charStatDictKeys = charStatDict.keys()
    fuckingList = []

    for index in range(len(abc)):
        fuckingList.append(abc[index])
        fuckingList.append(charStatDict[index])

    # for index in range(len(charStatArr)):
    #     fuckingList.append(charStatDictKeys[index])
    #     fuckingList.append(charStatArr[index])


    # print(list(charStat.values()))
    # print(list(charStat.keys()))

    # for letter in text:
    #     print(letter)
        # get text stat

    # return KeyboardLayout()


mathLayoutGenerator("testTextes/alice_in_wonderland.txt")
