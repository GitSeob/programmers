def solution(boxes):
    stocks = []
    done = 0

    for box in boxes:
        for stock in box:
            stocks.append(stock)

    tmp_list = list(set(stocks))

    for stck in tmp_list:
        if stocks.count(stck)%2 == 0:
            done += 1
    return len(boxes) - done


