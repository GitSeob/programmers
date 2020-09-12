def solution(N, stages):
	dic = {}
	n = len(stages)
	for i in range(1,N+1):
		if n == 0 :
			dic[i] = 0
			continue
		item = stages.count(i)/n
		n -= stages.count(i)
		dic[i] = item
	return sorted(dic, key=lambda k : dic[k], reverse = True)


n1 = [2, 1, 2, 6, 2, 4, 3, 3]
n2 = [4, 4, 4, 4, 4]

print(solution(5, n1))
print(solution(4, n2))
