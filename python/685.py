from typing import List

class DFU:
    def __init__(self, N):
        self.n = N
        self.f = [i for i in range(N)]

    def add(self, x, y):
        rootA = self.getRoot(x)
        rootB = self.getRoot(y)
        self.f[rootA] = rootB

    def getRoot(self, v):
        if v != self.f[v]:
            self.f[v] = self.getRoot(self.f[v])
        return self.f[v]


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = DFU(len(edges)+1)
        parent = [i for i in range(n+1)]

        conflict, cycle = -1, -1
        for i, e in enumerate(edges):
            u, v = e[0], e[1]
            if parent[v] != v:
                conflict = i
            else:
                parent[v] = u
                if uf.getRoot(u) == uf.getRoot(v):
                    cycle = i
                else:
                    uf.add(u, v)

        if conflict < 0:
            return [edges[cycle][0], edges[cycle][1]]
        else:
            if cycle >= 0:
                return [parent[edges[conflict][1]], edges[conflict][1]]
            else:
                return [edges[conflict][0], edges[conflict][1]]



sol = Solution()
print(sol.findRedundantDirectedConnection([[1,2], [1,3], [2,3]]))
print(sol.findRedundantDirectedConnection([[1,2], [2,3], [3,4], [4,1], [1,5]]))
print(sol.findRedundantDirectedConnection([[2, 1], [4, 2], [3, 1], [1, 4]]))