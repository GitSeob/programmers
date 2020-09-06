def solution(n, times):
    right = n * max(times)
    left = 0
    flg = 0
    res = 0

    while left <= right:
        mid = (right + left) // 2
        count = 0
        for t in times:
            count += mid // t

        if count >= n:
            if flg:
                res = min(mid, res)
            else:
                res = mid
            right = mid - 1
        else:
            left = mid + 1

    return res
