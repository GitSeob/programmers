def f1(x):
    return x[1]

def solution(genres, plays):
    play = {}
    gen = {}
    res = []

    for i, (gn, pl) in enumerate(zip(genres, plays)):
        if gn not in gen:
            play[gn] = pl
            gen[gn] = [(i, pl)]
        else:
            play[gn] += pl
            gen[gn].append((i, pl))
    # print(play)
    play = sorted(play.items(), key=f1,reverse=True)
    # print(play)
    for key, val in play:
        gen[key].sort(key=f1, reverse=True)
        res.append(gen[key][0][0])
        if len(gen[key]) > 1:
            res.append(gen[key][1][0])

    return res
