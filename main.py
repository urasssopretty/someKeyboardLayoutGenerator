import string


def language_selection():
    print("type is the number of the language that used in this file?")
    print("\t1. english")
    print("\t2. ukrainian")
    print("\t3. russian")
    print("\t4. french")
    print("\t5. polish")
    print("\t6. german")
    print("\t7. danish")
    print("\t8. italian")
    print("\t8. icelandic")
    print("\t9. norwegian")
    print("\t10. slovenian")

    while True:
        print("type number:\t", end='')
        user_input = input()

        if user_input not in "12345678910":
            print("INCORRECT INPUT")

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


def text_analysis(file_name, language):
    file = open_file(file_name)
    result = {}
    alphabet = list(string.ascii_lowercase)


def main():
    print("hello %username%\n")
    language_number = language_selection()
    file = file_selection()

    text_analysis(file, language_number)


if __name__ == '__main__':
    main()
