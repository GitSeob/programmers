res = 0

def checkAvail(n, matrix, row, col):
    for i in range(n):
        if matrix[i][col]:
            return False
    for i in range(n):
        if row-i >= 0:
            if col-i >= 0 and matrix[row-i][col-i] == 1:
                return False
            if col+i < n and matrix[row-i][col+i] == 1:
                return False

    return True

def recursive(n, matrix, row=0):
    global res
    if row >= n:
        return True
    for col in range(n):
        if checkAvail(n, matrix, row, col):
            matrix[row][col] = 1
            if (recursive(n, matrix, row+1)):
                res += 1
            matrix[row][col] = 0

    return False

def solution(n):
    matrix = []
    global res

    for i in range(n):
        matrix.append([0 for i in range(n)])

    recursive(n, matrix)
    return res
