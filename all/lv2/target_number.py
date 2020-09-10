def recursive(n, val, arr, t):
    if n >= len(arr):
        if val == t:
            return 1
        else:
            return 0
    res1 = recursive(n+1, val + arr[n], arr, t)
    res2 = recursive(n+1, val - arr[n], arr, t)

    return res1 + res2

def solution(numbers, target):
    return recursive(0, 0, numbers, target)
