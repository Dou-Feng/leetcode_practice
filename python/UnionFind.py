from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect

## 不带权值的并查集
class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.weight = [0] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y, value):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return False

        self.parent[rootx] = rooty
        return True

    def isConnected(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty:
            return True
        return False


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
    s = sol.f()
    print(s)