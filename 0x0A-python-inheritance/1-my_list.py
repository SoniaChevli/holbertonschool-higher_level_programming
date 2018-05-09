#!/usr/bin/python3


class MyList(list):
    def __init__(self):
        pass

    def print_sorted(self):
        new_list = sorted(self)
        print('[', end='')
        print(*new_list, sep=', ', end='')
        print(']')


if __name__ == '__main__':
    import doctest
    doctest.testfile("./tests/1-my_list.txt")
