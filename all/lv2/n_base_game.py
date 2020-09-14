def conv(num, base):
    T='0123456789ABCDEF'
    i, j = divmod(num, base)
    if i == 0:
        return T[j]
    else:
        return conv(i, base) + T[j]

def solution(n, t, m, p):
    digits = []
    res = ''
    num = 0
    while len(digits) < t*m:
        digits += list(conv(num, n))
        num += 1
    for i in range(t):
        res += digits[i*m+p-1]
    return res
