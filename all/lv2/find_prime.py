from math import sqrt
from itertools import permutations

def checkPrime(n):
    if n < 2:
        return False
    elif n == 2 :
        return True

    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    res = []
    for i in range(1, len(numbers)+1):
        numlist = list(map(''.join, permutations(numbers, i)))
        for n in numlist:
            if int(n) not in res and checkPrime(int(n)) == True:
                res.append(int(n))

    return len(res)
