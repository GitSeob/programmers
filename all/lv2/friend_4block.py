def findRect(m, n, board):
	res = []
	arounds = [(0, 1), (1, 0), (1, 1)]
	for row in range(m-1):
		for col in range(n-1):
			block = board[row][col]
			if block == 'X':
				break
			flg = True
			for r, c in arounds:
				if block != board[row+r][col+c]:
					flg = False
					break
			if flg:
				res.append((row, col))
	return res

def removeRect(m, n, board, pts):
	arounds = [(0, 0), (0, 1), (1, 0), (1, 1)]
	cnt = 0
	for row, col in pts:
		for r, c in arounds:
			if board[row+r][col+c] != 'X':
				board[row+r][col+c] = 'X'
				cnt += 1
	return board, cnt

def downBlock(m, n, board, pts):
	arounds = [(0, 0), (0, 1), (1, 0), (1, 1)]
	emptys = [[] for _ in range(n)]
	for row, col in pts:
		for r, c in arounds:
			if row+r not in emptys[col+c]:
				emptys[col+c].append(row+r)
	for col in range(n):
		for row in emptys[col]:
			for i in range(0, row):
				if row-i-1 >= 0:
					board[row-i][col] = board[row-i-1][col]
		for row in range(len(emptys[col])):
			board[row][col] = 'X'
	return board

def solution(m, n, board):
	res = 0
	board = [list(x) for x in board]

	pts = findRect(m, n, board)
	while len(pts) > 0:
		board, cnt = removeRect(m, n, board, pts)
		print(board, cnt)
		res += cnt
		board = downBlock(m, n, board, pts)
		pts = findRect(m, n, board)

	print(board)

	return res


board1 = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
board2 = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(4, 5, board1)) # 14
# print(solution(6, 6, board2)) # 15

# [['X', 'X', 'X', 'X', 'E'],
#  ['X', 'X', 'X', 'X', 'E'],
#  ['X', 'X', 'X', 'D', 'F'],
#  ['X', 'X', 'X', 'D', 'F']]

# CCBDE
# AAADE
# AAABF
# CCBBF

# CCBDE
# XXXDE
# XXXBF
# CCBBF	6

# XXXDE
# XXXDE
# CCBBF
# CCBBF

