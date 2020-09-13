import re

def solution(new_id):
	new_id = new_id.lower()
	nid = ''
	for i in range(len(new_id)):
		if new_id[i].isalpha() or new_id[i] == '-' or new_id[i] == '_' or new_id[i] == '.' or new_id[i].isdigit():
			nid += new_id[i]
	nid = re.sub('\.+', '.', nid)
	if len(nid) > 0 and nid[0] == '.':
		nid = nid[1:]
	if len(nid) > 0 and  nid[-1] == '.':
		nid = nid[:-1]

	if nid == '':
		nid = 'a'
	if len(nid) <= 2:
		while len(nid) < 3:
			nid = nid + nid[-1]
	elif len(nid) >= 16:
		nid = nid[0:15]
		if nid[0] == '.':
			nid = nid[1:]
		if nid[-1] == '.':
			nid = nid[:-1]

	return nid
