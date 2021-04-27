
# graph's is a matrix, graph[i][j] is denoted to the distance between vertex i and vertex j.
INF = 10**9 + 7
def dijkstra(graph, tp):
	n = len(graph)
	if tp >= n:
		return -1 # it means that the input tp is invalid

	s = [False] * n
	lstd = [INF] * n
	lstd[tp] = 0
	path = [-1] * n
	for i in range(n):
		lstd[i] = graph[tp][i]
		if lstd[i] != INF:
			path[i] = tp


	for i in range(n):
		v = 0
		ld = INF
		for i in range(n):
			if not s[i] and ld > lstd[i]:
				ld = lstd[i]
				v = i
		s[v] = True
		# update the lstd[i]
		for i in range(n):
			if not s[i] and lstd[i] > lstd[v] + graph[v][i]:
					lstd[i] = lstd[v] + graph[v][i]
					path[i] = v

	return lstd, path


if __name__ == '__main__':
	n = 5
	graph = [[0, 3, 2, INF, INF, INF], [3, 0, 1, INF, INF, INF], [2, 1, 0, 1, INF, INF], [INF, INF, 1, 0, 10, 3], [INF, INF, INF, 10, 0, 4], [INF, 4, INF, 3, 4, 0]]
	d, path = dijkstra(graph, n)
	print(d)
	for i, p in enumerate(path):
		s = str(i) + "<-"
		while p != n:
			s += str(p) + "<-"
			p = path[p]
		s += str(p)
		print(s)


