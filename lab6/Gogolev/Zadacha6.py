from sys import stdin
import math

FIRST_LINE = stdin.readline()
LIST = [int(p) for p in FIRST_LINE.split(' ')]
LIST1 = []
LIST2 = []

for x in LIST:
    if x >= 0:
        LIST2.append(x)
    else:
        LIST1.append(x)

d = len(str(max(LIST)))


def RADIX_SORT_1(LIST, d):
    for i in range(0, d):
        HELP_LIST = [[] for k in range(0, 10)]
        for x in LIST:
            RADIX_VALUE = (x // (10 ** i)) % 10
            HELP_LIST[RADIX_VALUE].append(x)
        LIST = []
        for k in range(0, 10):
            LIST = LIST + HELP_LIST[k]
    return LIST


def RADIX_SORT(LIST1, LIST2):
    LIST3 = []
    for x in LIST1:
        x = x * (-1)
        LIST3.append(x)
    LIST3 = RADIX_SORT_1(LIST3, d)
    LIST4 = []
    for x in LIST3:
        x = x * (-1)
        LIST4.append(x)
    LIST4.reverse()
    LIST2 = RADIX_SORT_1(LIST2, d)
    LIST3 = LIST4 + LIST2
    return LIST3


print(RADIX_SORT(LIST1, LIST2))
