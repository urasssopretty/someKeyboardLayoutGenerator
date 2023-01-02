import string

### JSON format of keyb analizer
#   -   label
#   -   author
#   -   moreInfoUrl
#   -   moreInfoText
#   -   fingerStart
#   -   keyboardType
#   -   keys
#           -   primary
#           -   shift layer
#           -   fingerId
#           -   keyId


### my own interior json format
#   -   label
#   -   fingerStart
#   -   key
#       -   upper row
#           -   primary
#           -   shift layer
#           -   fingerId
#           -   keyId
#       -   home row
#       -   bottom row


### how to calculate distance
#   i wanna calcute not a real "distance", like adumb, but a how many keys to next key
#   fint sort list of keys

def output():
    seeAnotherFile = False
    if seeAnotherFile:
        print("kek lol")
    else:
        file = open("book-war-and-peace.txt").read().lower()
        # file = open("old.py").read().lower()
        alphabet = list(string.ascii_lowercase)
        # letterCounts = []
        dictLetterToCount = {}
        # dicCountToLetter = {}

        for index in range(0, len(alphabet)-1):
            count = file.count(alphabet[index])
            symbol = alphabet[index]
            dictLetterToCount[symbol] = count
            # dicCountToLetter[count] = symbol
            # letterCounts.append(file.count(alphabet[index]))
            # dictLetterToCount[alphabet[index]] = letterCounts[index]
            # dicCountToLetter[letterCounts[index]] = alphabet[index]

        # letterCounts.sort(reverse=True)
        # print(letterCounts)
        # print(dictLetterToCount)
        # print(dicCountToLetter)
        sorterLetters = sorted(dictLetterToCount, key=dictLetterToCount.get, reverse=True)
        print(sorterLetters)

    homeRow = sorterLetters[:9]
    upperRow = sorterLetters[10:18]
    bottomRow = sorterLetters[19:]

    print(upperRow)
    print(homeRow)
    print(bottomRow)

