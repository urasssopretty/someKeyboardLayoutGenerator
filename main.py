import string


def language_selection():
    languages = [
        "english",
        "ukrainian",
        "russian",
        "french",
        "polish",
        "german",
        "danish",
        "italian",
        "icelandic",
        "norwegian",
        "slovenian"
    ]

    print("type is the number of the language that used in this file?")

    for i in range(2, int(len(languages)), 2):
        print(str(i - 1) + ".\t" + languages[i - 1] + "\t", end='')
        print(str(i) + ".\t" + languages[i])

    while True:
        print("\n\ttype ur number:\t", end='')
        user_input = input()

        if user_input not in "12345678910":
            print("INCORRECT INPUT\n\n just try again")
        else:
            break

    return user_input


def file_selection():
    print("where is the file containing your everyday text??")
    # print("\t1. in this folder")
    # print("\t2. in other directory")
    # print("type ur answer:\t", end='')

    # user_input = input()
    while True:
        print("type file name:\t")
        user_input = input()

        print("its name is correct? \t", user_input, "yes/no?")
        correct = input()

        if correct in "yes":
            break

    return user_input


def open_file(file_name):
    return open(file_name, "r").read().lower()


# def text_analysis(file_name, language):
def text_analysis(file_name):
    file = open_file(file_name)
    alphabet = list(string.ascii_lowercase)
    result = []

    for index in range(len(alphabet)):
        result[index] = file.count(alphabet[index])

    return result


def changeZXCV():
    print("do u wanna save ZXCV keys for shortcuts? Y/n")
    user_input = input()

    if user_input.lower() in "yes " or user_input == "":
        return True
    else:
        return False


def main():
    print("hello %username%\n")
    language_number = language_selection()
    file = file_selection()

    # text_analysis(file, language_number)
    letterFrequency = text_analysis(file)
    # print("what is way of setting: easy/pro?")

    savePartOfQWERTY = changeZXCV()

    # if savePartOfQWERTY:


if __name__ == '__main__':
    main()
