def solution(ball, orders):
    boru = []
    res = []

    while len(ball) > 0:
        while len(boru) > 0:
            flg = True
            for b in boru:
                if ball[0] == b:
                    res.append(ball.pop(0))
                    flg = False
                elif ball[-1] == b:
                    res.append(ball.pop(len(ball)-1))
                    flg = False
                if len(ball) == 0:
                    break
            if flg:
                break
        if len(orders) > 0:
            order = orders.pop(0)
            if ball[0] == order:
                res.append(ball.pop(0))
            elif ball[-1] == order:
                res.append(ball.pop(len(ball)-1))
            else:
                boru.append(order)

    return res

ip1 = [[1,2,3,4,5,6], [11,2,9,13,24]]
ip2 = [[6,2,5,1,4,3], [9,2,13,24,11]]

print(solution(ip1[1], ip2[1]))
# for i in range(2):
# 	print(solution(ip1[i], ip2[i]))
