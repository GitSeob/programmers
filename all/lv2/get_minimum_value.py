def solution(A,B):
    B.sort(reverse=True)
    A.sort()
    res = 0
    for i in range(len(A)):    
        res += A[i] * B[i]
    return res
