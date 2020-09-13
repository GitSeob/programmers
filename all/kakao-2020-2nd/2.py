from itertools import combinations
import re

def overlap(orders, pattern, n):
    cnt = 0

    for order in orders:
        idx = 0
        while idx < n:
            if pattern[idx] in order:
                idx += 1
            else:
                break
            if idx == n:
                cnt += 1
                break
    return cnt

def solution(orders, course):
    orders = [sorted(x) for x in orders]
    dic = {}

    for num in course:
        for od in orders:
            if len(od) >= num:
                patterns = list(combinations(od, num))
                for pattern in patterns:
                    cnt = overlap(orders, list(pattern), num)
                    if cnt > 1:
                        if num in dic:
                            if (''.join(pattern), cnt) not in dic[num]:
                                dic[num].append((''.join(pattern), cnt))
                        else:
                            dic[num] = [(''.join(pattern), cnt)]
    res = []
    for num in course:
        if num in dic:
            maxNum = max(dic[num], key=lambda x: x[1])
            for name, cnt in dic[num]:
                if cnt == maxNum[1]:
                    res.append(name)

    return sorted(res)
