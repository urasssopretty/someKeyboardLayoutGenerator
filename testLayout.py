### tests
#   -   distance test
#   -   hand ux
#   -   another test

def distanceTestKeys(KeyboardLayout):
    keys = KeyboardLayout.getKeys()

    #   UPPER
    #   HOME
    #   BOTTOM ROW
    rows = [
        keys[:13],
        keys[14:27],
        keys[28:]
    ]

    finger = [[], [], [], [], [], [], [], [], [], []]

    for rowIndex in range(len(rows)):
        for keyIndex in range(len(rows[rowIndex])):
            for fingerID in range(10):
                if rows[rowIndex][keyIndex]["finger"] == fingerID+1:
                    finger[fingerID].append(rows[rowIndex][keyIndex])

    file = open("somenews.txt").read().lower()

    upperRow = "qwertyuiop[]\\"
    homeRow = "asdfghjkl;'"
    bottomRow = "zxcvbnm,./"
    # for letterIndex in range(len(file)):
    # for letter in file:


    return finger
