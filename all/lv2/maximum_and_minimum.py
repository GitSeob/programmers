def solution(s):
    s = [int(x) for x in s.split(' ')]

    return str(min(s)) + ' ' + str(max(s))
