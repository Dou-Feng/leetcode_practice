from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect

class UF_balanced:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.depth = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp == yp:
            return False
        ## union
        if self.depth[xp] < self.depth[yp]:
            t = xp
            xp = yp
            yp = t
        self.parent[xp] = self.parent[yp]
        self.depth[xp] += self.depth[yp]
        return True

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UF_balanced(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    uf.union(i, j)

        ret = 0
        for i in range(n):
            if i == uf.parent[i]:
                ret += 1
        return ret



if __name__ == '__main__':
    sol = Solution()
    s = sol.findCircleNum([[1,0,0],[0,1,0],[0,0,1]])
    print(s)
    s = sol.findCircleNum([[0]])
    print(s)
    s = sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
    print(s)