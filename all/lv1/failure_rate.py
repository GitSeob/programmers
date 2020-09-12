def solution(N, stages):
	res = [[i+1, 0] for i in range(N)]

	for i in range(1, N+1):
		total = 0
		clear = 0
		for stage in stages:
			if stage >= i:
				total += 1
				if stage > i:
					clear += 1
		res[i-1][1] = clear/total
	return [x for x, _ in sorted(res, key=lambda x: x[1])]

n1 = [2, 1, 2, 6, 2, 4, 3, 3]
n2 = [4, 4, 4, 4, 4]

print(solution(5, n1))
print(solution(4, n2))
