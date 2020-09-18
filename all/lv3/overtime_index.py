import heapq

def solution(n, works):
    heap = []

    if n >= sum(works):
        return 0

    for work in works:
        heapq.heappush(heap, (-work, work))

    while n > 0:
        _, val = heapq.heappop(heap)

        val -= 1
        n -= 1
        heapq.heappush(heap, (-val, val))

    return sum([x[1]**2 for x in heap])
