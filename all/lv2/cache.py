def solution(cacheSize, cities):
    queue = []
    time = 0
    cities = [ x.lower() for x in cities ]

    for city in cities:
        if city in queue:
            time += 1
            queue.pop(queue.index(city))
            queue.append(city)
        else:
            time += 5
            queue.append(city)

        if len(queue) > cacheSize:
            queue.pop(0)

    return time
