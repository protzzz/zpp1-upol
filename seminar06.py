def removing_spaces(str):
    space = " "
    for i in range(len(str)):
        str = str.replace("  ", space)
    print(str)
    return str


def word_new_line(str):
    zyx = False
    for i in str:
        if i != ' ':
            if zyx:
                print()
            print(i, end='')
            zyx = False
        else:
            zyx = True

str = input("Write smth: ")
removing_spaces(str)
word_new_line(str)