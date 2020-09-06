def solution(brown, yellow):
    y = 0
    val = brown + yellow

    for x in range(1, yellow+1):
        if (yellow % x == 0):
            y = yellow//x
            if ((x+2)*(y+2) == val and x*y == yellow):
                if (y > x):
                    return [int(y+2), int(x+2)]
                return [int(x+2), int(y+2)]
