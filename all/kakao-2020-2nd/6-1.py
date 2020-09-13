def move(board, row, col, target=None):
	if target == None:
		for r in range(row):
			if r != row and board[r][col] != 0:
				return r, col, 1
		for c in range(col):
			if c != col and board[row][c] != 0:
				return row, c, 1
	else:
		for r in range(row):
			if r != row and board[r][col] == target:
				return r, col, 1
		for c in range(col):
			if c != col and board[row][col] == target:
				return row, c, 1
	for r in range(4):
		for c in range(4):
			if target==None:
				if board[r][c] != 0:
					return r, c, 2
			else:
				if board[r][c] == target:
					return r, c, 2

def recursive(board, r, c, me=None):
	cnt = 0
	calSum = 0
	for rr in range(4):
		for cc in range(4):
			calSum += board[rr][cc]
	if calSum == 0:
		return 0
	if me == None:
		if board[r][c] == 0:
			# print('me is 0', (r, c))
			r, c, tmp = move(board, r, c)
			cnt += tmp
		me = board[r][c]
		board[r][c] = 0
		cnt += 1
	else:
		r, c, tmp = move(board, r, c, me)
		cnt += tmp
		board[r][c] = 0
		cnt += 1
		me = None
	# print(f'-----------------{(r,c)} me : {me} // cnt: {cnt}')
	return cnt + recursive(board, r, c, me)

def solution(board, r, c):
	res = 0

	res = recursive(board, r, c)
	return res
print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))
