from sys import stdin
import random

c = 0
d = 0
e = 0

first_line = stdin.readline()
list = [int(p) for p in first_line.split(' ')]


def QSORT(list, p, r):
    if p < r:
        q = RANDOM_PATRITION(list, p, r)
        QSORT(list, p, q - 1)
        QSORT(list, q + 1, r)
    return list


def PATRITION(list, p, r):
    x = list[r]
    i = p - 1
    for j in range(p, r):
        if list[j] < x:
            i += 1
            d = list[i]
            list[i] = list[j]
            list[j] = d
    e = list[i + 1]
    list[i + 1] = list[r]
    list[r] = e
    return i + 1


def RANDOM_PATRITION(list, p, r):
    i = random.randint(p, r)
    c = list[r]
    list[r] = list[i]
    list[i] = c
    return PATRITION(list, p, r)


QSORT(list, 0, len(list) - 1)
print(list)
