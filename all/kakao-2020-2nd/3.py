def solution(info, query):
    infos = []
    for i in info:
        tmp = i.split(' ')
        infos.append(tmp)
    qrs = []
    for q in query:
        tmp = q.split(' and ')
        food = tmp.pop()
        tmp += food.split(' ')
        qrs.append(tmp)

    res = []
    for qr in qrs:
        cnt = 0
        for people in infos:
            flg = True
            for i in range(4):
                if qr[i] == '-':
                    continue
                elif people[i] != qr[i]:
                    flg = False
                    break
            if flg:
                if qr[4] == '-' or int(qr[4]) <= int(people[4]):
                    cnt += 1
        res.append(cnt)

    return res
