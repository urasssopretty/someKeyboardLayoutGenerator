import string
import os
def openFile(fileName):
    return open(fileName, "r").read().lower()

def getReportOfText(fileName, text, abc):
    os.remove(fileName)

    fileText = openFile(fileName)

    res = {}
    for letter in abc:
        res[letter] = text.count(letter)

