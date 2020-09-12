def solution(dartResult):
	nums = []
	idx = -1
	num = ''
	for ch in dartResult:
		if ch.isdigit():
			num += ch
			continue
		else:
			if num != '':
				idx += 1
				nums.append(int(num))
				num = ''

		if ch == 'D':
			nums[idx] = nums[idx]**2
		elif ch == 'T':
			nums[idx] = nums[idx]**3
		elif ch == '*':
			nums[idx] *= 2
			if idx > 0:
				nums[idx-1] *= 2
		elif ch == '#':
			nums[idx] *= -1
	return sum(nums)

drs = ["1S2D*3T", "1D2S#10S", "1D2S0T", "1S*2T*3S", "1D#2S*3S", "1T2D3D#", "1D2S3T*"]

for dr in drs:
	print(solution(dr))
