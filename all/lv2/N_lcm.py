from math import gcd

def solution(arr):
	arr = [int(x) for x in arr]
	res = arr[0]

	for i in range(1, len(arr)):
		res = int((res * arr[i]) / gcd(res, arr[i]))
	return res
