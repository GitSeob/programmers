def checkAvailable(stones, k, mid):
    jump = 0
    for val in stones:
        if (val < mid):
            jump += 1
        else:
            jump = 0
        if (jump >= k):
            return False
    return True


def solution(stones, k):
    left = 1
    right = max(stones) + 1

    while (left < right - 1):
        mid = (left + right)//2
        if checkAvailable(stones, k, mid):
            left = mid
        else:
            right = mid

    return left
