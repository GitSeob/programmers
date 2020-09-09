from itertools import combinations

def solution(nums):
    allsum = sum(nums)
    sosus = set(range(2, allsum+1))
    res = 0

    for num in range(2, allsum+1):
        if num in sosus:
            sosus -= set(range(num*2, allsum+1, num))

    perms = list(combinations(nums, 3))
    for a, b, c in perms:
        plus = a+b+c
        if plus in sosus:
            res+=1
    return res
