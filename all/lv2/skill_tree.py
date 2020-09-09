def solution(skill, skill_trees):
    res = 0
    for skt in skill_trees:
        tmp = []
        flg = True

        for ch in skt:
            if ch in skill:
                tmp.append(ch)

        for i in range(len(tmp)):
            if tmp[i] != skill[i]:
                flg = False
                break

        if flg == True:
            res+=1

    return res
