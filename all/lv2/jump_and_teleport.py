def solution(n):
    cost = 0
    while n > 0:
        while n % 2 == 0:
            n = n//2
        n -= 1
        cost += 1
    return cost
