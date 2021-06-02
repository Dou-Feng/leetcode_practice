from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        uf = UF(n)
        for con in connections:
            uf.union(con[0], con[1])

        return  uf.cnt - 1


class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.cnt = n

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
        self.cnt -= 1
        return True


if __name__ == '__main__':
    sol = Solution()
    s = sol.makeConnected(n = 4, connections = [[0,1],[0,2],[1,2]])
    print(s)
    s = sol.makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]])
    print(s)
    s = sol.makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2]])
    print(s)
    s = sol.makeConnected(n = 5, connections = [[0,1],[0,2],[3,4],[2,3]])
    print(s)