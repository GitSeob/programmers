from collections import deque

def solution(prices):
    queue = deque([1, 0])
    if len(prices) == 2:
        return [1, 0]

    for i in range(len(prices)-3, -1, -1):
        cnt = 1
        for j in range(i+1, len(prices)-1):
            if prices[i] > prices[j]:
                break
            cnt += 1
        queue.appendleft(cnt)
    return list(queue)
