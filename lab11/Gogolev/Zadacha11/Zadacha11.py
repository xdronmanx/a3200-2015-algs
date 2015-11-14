from sys import stdin

FIRST_LINE = stdin.readline()
LIST = [int(p) for p in FIRST_LINE.split(' ')]


def SQUARE(i):
    square = 0
    j = i + 1
    p = i + 2
    while j < len(LIST) and LIST[i] > LIST[j]:
        square = square + (j - i)
        j = j + 1
        p = p + 1
    if j != len(LIST):
        return square
    else:
        return 0


def MAX_SQUARE(LIST):
    s = 0
    for x in range(0, len(LIST) - 1):
        if SQUARE(x) > s:
            s = SQUARE(x)
    return s


print(MAX_SQUARE(LIST))
