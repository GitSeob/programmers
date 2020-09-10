def solution(citats):
    for h in range(max(citats), -1, -1):
        arr = [1 for j in citats if j >= h]
        if sum(arr) >= h:
            break;

    return h
