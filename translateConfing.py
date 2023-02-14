import json

fileName = "layouts/qwerty.txt"
layoutFile = open(fileName).read()
jsonLayout = json.loads(layoutFile)

print('this is len:', len(jsonLayout["keys"]))
for index in range(len(jsonLayout["keys"])):
    print('#', index, end=' ')
    # print(index)
    try:
        print(jsonLayout["keys"][index]["primary"])
        jsonLayout["keys"].pop(index)
    except:
        print('THIS IS INDEX', index)

    # if jsonLayout["keys"][index]["primary"] > 0:
    #     jsonLayout["keys"].pop(index)
    #     print(jsonLayout["keys"].pop(index))
    #     del jsonLayout["keys"][index]


open("trueQwerty.txt", 'w').write(json.dumps(jsonLayout))

