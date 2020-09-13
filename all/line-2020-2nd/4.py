def solution(maze):
    cnt = 0
    row = 0
    col = 0
    N = len(maze)
    checkpos = {
        'right': (-1, 0),
        'left': (1, 0),
        'down': (0, 1),
        'up': (0, -1)
    }
    dirt = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }
    status = 'right'
    while row < N-1 or col < N-1:
        move = False
        print(status, (row, col))
        if status == 'right':
            if row-1 >= 0 and maze[row-1][col] == 0:
                row -= 1
                cnt += 1
                status = 'up'
                move = True

            elif status == 'right':
                if col == N-1 or maze[row][col+1] == 1:
                    status = 'down'

        elif status == 'up':
            if col-1 >= 0 and maze[row][col-1] == 0:
                col -= 1
                cnt += 1
                status = 'left'
                move = True

            elif status == 'up':
                if row == 0 or maze[row-1][col] == 1:
                    status = 'right'

        elif status == 'left':
            if row+1 < N and maze[row+1][col] == 0:
                row += 1
                cnt += 1
                status = 'down'
                move = True

            elif status == 'left':
                if col == 0 or maze[row][col-1] == 1:
                    status = 'up'

        elif status == 'down':
            if col+1 < N and maze[row][col+1] == 0:
                print('gogogogogogoo')
                col += 1
                cnt += 1
                status = 'right'
                move = True

            elif row == N-1 or maze[row+1][col] == 1:
                status = 'left'

        if move:
            continue
        nextrow, nextcol = row+dirt[status][0], col+dirt[status][1]
        print('----------', (row, col), '->', (nextrow, nextcol),status)
        if maze[nextrow][nextcol] == 1:
            continue
        else:
            cnt += 1
            prevrow = row
            prevcol = col
            row = nextrow
            col = nextcol

    return cnt


print(solution([[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]))
