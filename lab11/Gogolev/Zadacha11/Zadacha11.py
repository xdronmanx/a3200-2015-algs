from sys import stdin

first_line = stdin.readline()
list = [int(p) for p in first_line.split(' ')]


def SQUARE(i):
    square = 0
    j = i + 1
    p = i + 2
    while j < len(list) and list[i] > list[j]:
        square = square + (list[i] - list[j])
        j = j + 1
        p = p + 1
    if j != len(list):
        return square
    else:
        return 0


def MAX_SQUARE(list):
    s = 0
    for x in range(0, len(list) - 1):
        if SQUARE(x) > s:
            s = SQUARE(x)
    return s


print(MAX_SQUARE(list))
