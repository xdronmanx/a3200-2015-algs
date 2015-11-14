from sys import stdin
import random

c = 0
d = 0
e = 0

FIRST_LINE = stdin.readline()
LIST = [int(p) for p in FIRST_LINE.split(' ')]


def QSORT(LIST, p, r):
    if p < r:
        q = RANDOM_PATRITION(LIST, p, r)
        QSORT(LIST, p, q - 1)
        QSORT(LIST, q + 1, r)


def PATRITION(LIST, p, r):
    x = LIST[r]
    i = p - 1
    for j in range(p, r):
        if LIST[j] <= x:
            i += 1
            d = LIST[i]
            LIST[i] = LIST[j]
            LIST[j] = d
    e = LIST[i + 1]
    LIST[i + 1] = LIST[r]
    LIST[r] = e
    return i + 1


def RANDOM_PATRITION(LIST, p, r):
    i = random.randint(p, r)
    c = LIST[r]
    LIST[r] = LIST[i]
    LIST[i] = c
    return PATRITION(LIST, p, r)


QSORT(LIST, 0, len(LIST) - 1)
print(LIST)
