#!/usr/bin/python3


def text_indentation(text):
    i = 0
    if type(text) is not str:
        raise TypeError("text must be a string")

    text = text.strip()

    while (i < len(text)):
        print("{:s}".format(text[i]), end='')
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print()
            print()
            while(text[i] == " " and i + 1 < len(text)):
                i += 1
        i += 1

if __name__ == '__main__':
    import doctest
    doctest.testfile("./tests/5-text_indentation.txt")
