res = []

def move(board, row, col, target=None):
	pos = []
	if target == None:
		for r in range(row):
			if r != row and board[r][col] != 0:
				pos.append((r, col, 1))
				# return r, col, 1
		for c in range(col):
			if c != col and board[row][c] != 0:
				pos.append((row, c, 1))
				# return row, c, 1
	else:
		for r in range(row):
			if r != row and board[r][col] == target:
				pos.append((r, col, 1))
				# return r, col, 1
		for c in range(col):
			if c != col and board[row][col] == target:
				pos.append((row, c, 1))
				# return row, c, 1
	if len(pos) > 0:
		return pos
	for r in range(4):
		for c in range(4):
			if target==None:
				if board[r][c] != 0:
					pos.append((r, c, 2))
					# return r, c, 2
			else:
				if board[r][c] == target:
					pos.append((r, c, 2))
					# return r, c, 2
	print(pos)
	return pos

def recursive(board, r, c, me, cnt):
	calSum = 0
	board1 = [x for x in board]
	print(me, (r, c), board)
	for rr in range(4):
		for cc in range(4):
			calSum += board1[rr][cc]
	if calSum == 0:
		global res
		res.append(cnt)
		return True
	if me == None:
		if board[r][c] == 0:
			p_list = move(board1, r, c)
			for r, c, tmp in p_list:
				cnt += tmp
				me = board1[r][c]
				board[r][c] = 0
				cnt += 1
				return recursive(board1, r, c, me, cnt)
		else:
			me = board1[r][c]
			return recursive(board1, r, c, me, cnt+1)
	else:
		print((r, c), me)
		p_list = move(board1, r, c, me)
		print(me, 'get ---', p_list)
		for r, c, tmp in p_list:
			cnt += tmp
			board1[r][c] = 0
			cnt += 1
			me = None
			return recursive(board1, r, c, me, cnt)

	return False
	# print(f'-----------------{(r,c)} me : {me} // cnt: {cnt}')
	# return cnt + recursive(board, r, c, me)

def solution(board, r, c):

	recursive(board, r, c, None, 0)
	global res
	# return min(res)
	print(res)
	# return min(res)

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))
