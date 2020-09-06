def solution(pb):
    pb.sort()

    for i, n in enumerate(pb):
        for nn in pb[i+1:]:
            if n in nn:
                return False
    return True
