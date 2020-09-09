from itertools import permutations

def calc(a, b, op):
    if op == '-':
        return str(int(a) - int(b))
    elif op == '+':
        return str(int(a) + int(b))
    else:
        return str(int(a) * int(b))

def solution(expression):
    exps = []
    exp = []
    res = []

    num = ''
    for ch in expression:
        if ch.isdigit():
            num += ch
        else:
            exps.append(num)
            exps.append(ch)
            exp.append(ch)
            num = ''
    if num != '':
        exps.append(num)

    pers = list(permutations(list(set(exp))))

    for tup in pers:
        stack = [x for x in exps]
        for per in tup:
            stack = calcSameOp(stack, per)
        res.append(abs(int(stack[-1])))
    return max(res)

def calcSameOp(arr, op):
    stack = []
    while len(arr) > 0:
        a = arr.pop(0)
        if a == op:
            val1 = stack.pop()
            val2 = arr.pop(0)
            stack.append(calc(val1, val2, a))
        else:
            stack.append(a)
    return stack
