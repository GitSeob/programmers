def solution(clothes):
    cl = {}
    for row in clothes:
        if row[1] in cl:
            cl[row[1]].append(row[0])
        else:
            cl[row[1]] = [row[0]]
    keys = list(cl.keys())

    if len(keys) == 1:
        return len(cl[keys[0]])

    res = 1
    for key in keys:
        res *= len(cl[key])+1

    return res -1
