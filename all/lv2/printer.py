def solution(priors, location):
    locs = [ i for i in range(len(priors))]
    res = []

    while len(priors) > 0:
        prior = priors[0]
        flg = True
        for i in range(1, len(priors)):
            if prior < priors[i]:
                prior = priors.pop(0)
                loc = locs.pop(0)
                priors.append(prior)
                locs.append(loc)
                flg = False
                break
        if flg:
            priors.pop(0)
            res.append(locs.pop(0))
    return res.index(location) + 1
