def getZipStr(s, n):
    res = ''
    s_len = len(s)
    ipt_idx = -1
    for i in range(0, s_len, n):
        rep = 1
        for j in range(i+n, s_len-n+1, n):
            if s[i:i+n] == s[i+(n*rep): i+(rep+1)*n]:
                rep += 1
            else:
                break
        if ipt_idx <= i:
            if rep > 1:
                res += str(rep) + s[i:i+n]
                ipt_idx = n*rep + i
            elif i+n > s_len:
                res += s[i:]
            else:
                res += s[i: i+n]
    return res

def solution(s):
    res = [len(s)]

    for n in range(1, len(s)//2 + 1):
        tmp = getZipStr(s, n)
        res.append(len(tmp))


    return min(res)
