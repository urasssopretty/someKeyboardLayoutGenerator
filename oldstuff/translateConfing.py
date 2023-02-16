import json


def configIsCorrect(fileName):
    config = json.loads(open(fileName).read())
    fields = "label author moreInfoUrl moreInfoText fingerStart keyboardType keys"
    isCorrect = True

    for field in config:
        if field not in fields:
            print("ERROR ERROR ERROR\n\n", "field:", field, "cant be used for layout, generator dont support this")

    lenOfKeys = len(config["keys"])

    # print(type(config))
    # print(type(config["keys"]))
    # print(type(config["keys"][0]))
    # print(type(config["keys"][0]["primary"]))

    keysWithSignedPrimary = []

    for index in range(lenOfKeys):
        if config["keys"][index]["primary"] < 0:
            keysWithSignedPrimary.append(index)
        # print('#', index)
        # print("len:", len(config["keys"]))
        # print(config["keys"][index])
        # print("\n")

    counter = 0
    for index in keysWithSignedPrimary:
        config["keys"].pop(index - counter)
        counter += 1

    # outputFile = open("trueQwerty.txt", 'w')
    outputFile = open("{}_correct.txt".format(fileName[:-4], 'x'))
    outputFile = open("{}_correct.txt".format(fileName[:-4], 'w+'))
    outputFile.write(json.dumps(config).replace(",", ",\n"))
    # currentFile = open("trueQwerty.txt")
    # outputFile.write(outputFile.read())


configIsCorrect("../layouts/qwerty.txt")
