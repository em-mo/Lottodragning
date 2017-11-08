from math import pow, floor

def divide_into_singles(value):
    no_chars = 1
    while pow(10, no_chars) < value:
        no_chars += 1

    chars = list()

    last_char = 0
    rest = 0
    for i in reversed(range(no_chars)):
        chars.append(int(floor((value - rest) / pow(10, i))))
        rest += (chars[no_chars - i - 1] * pow(10, i))
        print rest

    return chars