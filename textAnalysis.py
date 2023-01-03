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
#           -   shift
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

sorterLetters = []


def output():

    seeAnotherFile = False
    if seeAnotherFile:
        print("kek lol")
    else:
        file = open("book-war-and-peace.txt").read().lower()
        alphabet = list(string.ascii_lowercase)
        dictLetterToCount = {}

        for index in range(0, len(alphabet)-1):
            count = file.count(alphabet[index])
            symbol = alphabet[index]
            dictLetterToCount[symbol] = count

        sorterLetters.append(sorted(dictLetterToCount, key=dictLetterToCount.get, reverse=True))
        print(sorterLetters)

    homeRow = sorterLetters[:9]
    upperRow = sorterLetters[10:18]
    bottomRow = sorterLetters[19:]

    print(upperRow)
    print(homeRow)
    print(bottomRow)
