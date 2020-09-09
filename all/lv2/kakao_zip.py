def solution(msg):
    dic = {}

    for i in range(26):
        dic[chr(ord('A') + i)] = i+1

    res = []
    flg = False
    s = ''

    for ch in msg:
        if s + ch in dic:
            s += ch
        else:
            res.append(dic[s])
            dic[s+ch] = max(dic.values()) + 1
            s = ch

    res.append(dic[s])
    return res
