from sys import stdin

first_line = stdin.readline()
list = [int(p) for p in first_line.split(' ')]
k = 10


def sort_vstavkami(list):
    length = len(list)
    for i in range(1, length):
        j = i - 1
        key = list.pop(i)
        while (j >= 0) and (list[j] > key):
            j -= 1
        list.insert(j + 1, key)
    return list


def merge(leftpart, rightpart):
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


def mergesort(list):
    length = len(list)
    if length >= k:
        mid = int(length / 2)
        list = merge(mergesort(list[:mid]), mergesort(list[mid:]))
    else:
        list = sort_vstavkami(list)
    return list


print(mergesort(list))
