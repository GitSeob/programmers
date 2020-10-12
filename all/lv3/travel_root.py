travels = []

def dfs(tickets, origin="ICN", travel=[]):
    if len(tickets) == 0:
        global travels
        travels.append(travel)
        
    for i in range(len(tickets)):
        if tickets[i][0] == origin:
            tmp = [x for x in tickets]
            ticket = tmp.pop(i)
            tmp_travel = [x for x in travel]
            tmp_travel.append(ticket)
            dfs(tmp, ticket[1], tmp_travel)

def solution(tickets):
    global travels
    
    dfs(tickets)
    res_list = []
    for travel in travels:
        res_tmp = [travel[0][0]]
        for ticket in travel:
            res_tmp.append(ticket[1])
        res_list.append(res_tmp)
        
    if len(res_list) == 1:
        return res_list[0]
    
    res_list = sorted(res_list)
    # print('-------->', res_list)
    return res_list[0]
