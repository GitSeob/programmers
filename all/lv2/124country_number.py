def solution(n):
    res = ''
    dic = {0: '1', 1: '2', 2: '4'}
    while n/3 > 0:
        res += dic[(n-1)%3]
        n = (n-1)//3
    return res[::-1]
