# questionnaire
# file select

def questions():
    flag = True
    print("\n\tCan i change ZXCV keys? Y/n\n\t(its important for Ctrl + C, Ctrl + V combinations)\n\t:")
    while True:
        userinput = input()
        if userinput.lower() in "yes " or userinput == "":
            flag = True
        elif userinput.lower() in "no":
            flag = False
        else:
            print(userinput)
            print("try again! i can understand u")
            print("\n\t:")
            continue
        break
    return flag


def output():
    return questions()
