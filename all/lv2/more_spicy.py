import heapq

def solution(scovs, K):
    cnt = 0
    heapq.heapify(scovs)

    for _ in range(len(scovs)):
        if len(scovs) <= 1:
            return -1
        cnt += 1
        mixed = heapq.heappop(scovs) + heapq.heappop(scovs)*2
        heapq.heappush(scovs, mixed)
        flg = True
        for scov in scovs:
            if scov < K:
                flg = False
                break
        if flg:
            break
    return cnt


# 스코빌 = 가장 맵지않은 스코빌 + 2번째로 맵지않은 스코빌 x 2
