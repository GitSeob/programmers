def solution(m, musicinfos):
	msif = [x.split(',') for x in musicinfos]
	mlist = []
	for i in range(len(m)):
		if m[i] != '#':
			mlist.append(m[i])
		else:
			mlist[-1] += '#'
	lenM = len(mlist)

	for i in range(len(msif)):
		msif[i][0] = msif[i][0].split(':')
		msif[i][0] = [int(x) for x in msif[i][0]]
		msif[i][1] = msif[i][1].split(':')
		msif[i][1] = [int(x) for x in msif[i][1]]
		tmp = []
		for ch in msif[i][3]:
			if ch == '#':
				tmp[-1] += '#'
			else:
				tmp.append(ch)
		msif[i][3] = tmp

	real = []
	for i in range(len(msif)):
		length = (msif[i][1][0] - msif[i][0][0]) * 60 + msif[i][1][1] - msif[i][0][1]
		realSong = (msif[i][3] * (length//len(msif[i][3]))) + msif[i][3][0:length%len(msif[i][3])]
		real.append(realSong)

	res = []
	for i in range(len(real)):
		for j in range(len(real[i]) - lenM + 1):
			flg = True
			val = real[i][j:lenM+j]
			length = (msif[i][1][0] - msif[i][0][0]) * 60 + msif[i][1][1] - msif[i][0][1]
			for k in range(lenM):
				if val[k] != mlist[k]:
					flg = False
					length = 0
					break
			if flg and (msif[i][2], length) not in res:
				res.append((msif[i][2], length))
	if len(res) == 1:
		return res[0][0]
	elif len(res) > 1:
		return res[res.index(max(res, key=lambda x: x[1]))][0]
	return '(None)'


m1 = "ABCDEFG"
m2 = "CC#BCC#BCC#BCC#B"
m3 = "ABC"
m4 = "CDEFGAC"

musicinfos1 = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
musicinfos2 = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
musicinfos3 = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
musicinfos4 = ["12:00,12:06,HELLO,CDEFGA"]

print(solution(m1, musicinfos1)) # HELLO
print(solution(m2, musicinfos2)) # FOO
print(solution(m3, musicinfos3)) # WORLD
print(solution(m4, musicinfos4))
