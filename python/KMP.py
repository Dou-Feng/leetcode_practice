
def preprocess_next(next, pat, m):
	next[0] = -1
	i, j = 0, 1
	while j < m:
		print(i, j)
		if i == -1 or pat[i] == pat[j]:
			i += 1
			j += 1
			next[j] = i
			
		else:
			i = next[i]


def KMP_search(txt: str, pat: str) -> []:
	n = len(txt)
	m = len(pat)

	next = [0] * (m+1)
	preprocess_next(next, pat, m)

	ret = []
	i, j = 0, 0
	while i < n:
		if j == -1 or txt[i] == pat[j]:
			i += 1
			j += 1

		if j == m:
			ret.append(i - m)

		elif i < n and txt[i] != pat[j]:
			j = next[j]

	return ret




