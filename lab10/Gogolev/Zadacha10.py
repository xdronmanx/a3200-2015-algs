from sys import stdin

FIRST_LINE = stdin.readline()
LIST = [int(p) for p in FIRST_LINE.split(' ')]


def PIF_COUTNER(LIST):
    HELP_LIST = set(LIST)
    LIST2 = list(HELP_LIST)
    LIST2.sort()
    COUNTER = 0
    for i in range(0, len(LIST2)):
        for j in range(0, len(LIST2)):
            for k in range(0, len(LIST2)):
                if LIST2[i] ** 2 + LIST2[j] ** 2 == LIST2[k] ** 2:
                    COUNTER = COUNTER + 1
    return int(COUNTER / 2)


print(PIF_COUTNER(LIST))
