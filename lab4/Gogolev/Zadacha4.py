from sys import stdin

first_line = stdin.readline()
list = [int(p) for p in first_line.split(' ')]
k = 10


def INSERTION_SORT(list):
    for j in range(1, len(list)):
        key = list[j]
        i = j - 1
        while (i >= 0) and (list[i] > key):
            list[i+1] = list[i]
            i = i - 1
        list[i+1] = key
    return list


def MERGE(leftpart, rightpart):
    list = []
    while leftpart and rightpart:
        if leftpart[0] < rightpart[0]:
            list.append(leftpart.pop(0))
        else:
            list.append(rightpart.pop(0))
    if leftpart:
        list.extend(leftpart)
    if rightpart:
        list.extend(rightpart)
    return list


def MERGE_SORT(list):
    length = len(list)
    if length >= 10:
        mid = int(length / 2)
        list = MERGE(MERGE_SORT(list[:mid]), MERGE_SORT(list[mid:]))
    else:
        list = INSERTION_SORT(list)
    return list


print(MERGE_SORT(list))
