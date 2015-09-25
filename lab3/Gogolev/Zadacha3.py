from sys import stdin

first_line = stdin.readline()
second_line = stdin.readline()
c = 0
n = int(first_line)
l = [int(p) for p in second_line.split(' ')]


def function(index, m):
    global c
    for i in range(0, int((m / l[index]) + 1)):
        k = m - i * l[index]
        if k == 0:
            c = c + 1
        else:
            if index < (l.__len__() - 1):
                function(index + 1, k)


function(0, n)
print(c)
