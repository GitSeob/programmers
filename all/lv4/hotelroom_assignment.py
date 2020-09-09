def solution(k, room_number):
    room = []
    roomMap = {}

    for i in room_number:
        n = i
        visit = [n]
        while n in roomMap:
            n = roomMap[n]
            visit.append(n)
        room.append(n)
        for key in visit:
            roomMap[key] = n+1

    return room
