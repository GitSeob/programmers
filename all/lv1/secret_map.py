def solution(n, arr1, arr2):
	res = []
	for a, b in zip(arr1, arr2):
		line = ''
		div = 2**(n-1)
		# print(a, b)
		for _ in range(n):
			if a // div > 0 or b // div > 0:
				line += '#'
			else:
				line += ' '
			a = a%div
			b = b%div
			div = div//2
		res.append(line)
	return res

arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

arr3 = [46, 33, 33, 22, 31, 50]
arr4 = [27, 56, 19, 14, 14, 10]

print(solution(5, arr1, arr2))
print(solution(6, arr3, arr4))
