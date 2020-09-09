def solution(progresses, speeds):
    complete_days = []
    res = []

    for i in range(len(progresses)):
        day = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) %  speeds[i] != 0:
            day += 1
        complete_days.append(day)

    while len(complete_days) > 0:
        count = 0
        checkVal = complete_days[0]
        for i in range(len(complete_days)):
            if complete_days[0] <= checkVal:
                count += 1
                complete_days.pop(0)
            else:
                break
        res.append(count)
    return res
