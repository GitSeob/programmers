def solution(s):
    statusCount = 0;
    listS = list(s);

    for ch in listS:
        if ch == '(':
            statusCount+=1;
        else:
            statusCount-=1;
            if statusCount < 0:
                return False

    if statusCount == 0:
        return True
    return False
