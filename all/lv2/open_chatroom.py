def solution(record):
    behav = []
    ids = []
    users = {}

    for s in record:
        command = s.split(' ')
        nick = ''
        behav.append(command[0])
        ids.append(command[1])
        if command[0] != 'Leave':
            users[command[1]] = command[2]

    res = []
    for i in range(len(behav)):
        if behav[i] == 'Enter':
            res.append(users[ids[i]]+'님이 들어왔습니다.')
        elif behav[i] == 'Leave':
            res.append(users[ids[i]]+'님이 나갔습니다.')

    return res
