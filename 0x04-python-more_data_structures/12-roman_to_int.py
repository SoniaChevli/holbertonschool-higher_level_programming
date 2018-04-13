#!/usr/bin/python3
def translate_letter(roman_string):
    new_string = []
    for i in roman_string:
        if i == 'M':
            new_string.append(1000)
        elif i == 'D':
            new_string.append(500)
        elif i == 'C':
            new_string.append(100)
        elif i == 'L':
            new_string.append(50)
        elif i == 'X':
            new_string.append(10)
        elif i == 'V':
            new_string.append(5)
        else:
            new_string.append(1)
    return new_string


def roman_to_int(roman_string):
    number = 0
    roman_string = translate_letter(roman_string)
    for i, d in enumerate(roman_string):
        i = i + 1
        j = d
        i = i - 1
        if d < j:
            number = number + (j - d)
            i = i + 1
        else:
            number = number + d

    return number
