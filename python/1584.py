from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                edges.append((i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])))

        edges.sort(key = lambda e : e[2])

        uf = UF(n)
        ret = 0
        for e in edges:
            if uf.union(e[0], e[1]):
                ret += e[2]
                if uf.getSize(e[0]) == n:
                    return ret

        return ret

## 带有连通分量大小的并查集
class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)

        if xp == yp:
            return False

        ## union
        self.parent[yp] = xp
        self.size[xp] += self.size[yp]

        return True

    def getSize(self, x):
        return self.size[self.find(x)]

        return True

if __name__ == '__main__':
    sol = Solution()
    s = sol.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])
    print(s)