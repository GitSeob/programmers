import heapq

def solution(operations):
    heap = []

    for oper in operations:
        comm, num = oper.split(' ')
        num = int(num)
        if comm == 'I':
            heapq.heappush(heap, num)
        else:
            if len(heap) == 0:
                continue
            if num == 1:
                heap.remove(max(heap))
            else:
                heapq.heappop(heap)
    if len(heap) == 0:
        return [0, 0]
    return [max(heap), heap[0]]
