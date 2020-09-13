def solution(companies, applicants):
    comps = []
    rejects = []
    dic = {}
    for comp in companies:
        tmp = []
        a, b, c = comp.split(' ')
        dic[a] = []
        tmp.append(a)
        tmp.append(list(b))
        tmp.append(int(c))
        comps.append(tmp)

    for app in applicants:
        a, b, c = app.split(' ')
        tmp = []
        tmp.append(a)
        tmp.append(list(b))
        tmp.append(int(c))
        rejects.append(tmp)

    comp_names = dic.keys()
    count = 0
    while len(rejects) > 0:
        count += 1
        # print('--------------------', count, '-------------')
        while len(rejects) > 0:
            people = rejects.pop()
            if len(people[1]) > 0 and people[2] > 0:
                oper = people[1].pop(0)
                people[2] -= 1
                dic[oper].append(people)
        # print('dic---', dic)
        for i in range(len(comps)):
            tmp = []
            cnt = comps[i][2]
            for good in comps[i][1]:
                idx = -1
                for j in range(len(dic[comps[i][0]])):
                    if good == dic[comps[i][0]][j][0]:
                        idx = j
                        break
                if idx != -1:
                    tmp.append(dic[comps[i][0]].pop(idx))
                    cnt -= 1
                if cnt == 0:
                    break
            if len(tmp) > 0:
                for x in dic[comps[i][0]]:
                    rejects.append(x)
                dic[comps[i][0]] = sorted(tmp, key=lambda x: x[0])
    #     print('reject ------ ', rejects)
    # print('finish -------\n', dic, '\n--------')
    res = []
    for i in range(len(comps)):
        resStr = comps[i][0] + '_'
        for people in dic[comps[i][0]]:
            resStr += people[0]
        res.append(resStr)
    return res

ipt1 = ["A fabdec 2", "B cebdfa 2", "C ecfadb 2"]
ipt2 = ["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"]
print(solution(ipt1, ipt2))
