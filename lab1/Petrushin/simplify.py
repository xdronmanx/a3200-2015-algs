__author__ = 'Dmitry Petrsuhin'

import math

def is_simple(number):
    if number == 1:
        return False
    i = 2
    while i <= int(round(math.sqrt(number))):
        if number % i == 0:
            return False
        i += 1

    return True

def list_of_simple(number):
    answer = []

    for i in xrange(1, number + 1):
        answer.append(is_simple(i))

    return answer

x = int(input("Enter a number X to get list of simple numbers before X: "))
print(list_of_simple(x))