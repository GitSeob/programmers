from collections import deque

def solution(length, w, truck_w):
    t = 0
    queue = deque([])
    t_queue = []

    while len(truck_w) > 0 or len(queue) > 0:
        t += 1
        t_queue = [x-1 for x in t_queue]
        if len(t_queue) > 0 and t_queue[0] <= 0:
            t_queue.pop(0)
            queue.popleft()
        if len(truck_w) > 0:
            if sum(queue) + truck_w[0] > w:
                continue
            else:
                truck = truck_w.pop(0)
                queue.append(truck)
                t_queue.append(length)
    return t
