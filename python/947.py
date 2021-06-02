from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf  = UF(n + 1)
        
        coord = collections.defaultdict(list)
        for i, s in enumerate(stones):
            x, y = s[0], s[1]
            coord[x].append(i)
            coord[y+10**4+1].append(i)

        for values in coord.values():
            for i in range(len(values)):
                for j in range(i+1, len(values)):
                    uf.union(values[i], values[j])

        res = collections.defaultdict(int)
        for i in range(n):
            res[uf.find(i)] = uf.getSize(i)
            # print(i, uf.find(i), uf.getSize(i))

        ret = 0
        for v in res.values():
            ret += v -1
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
    s = sol.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])
    print(s)
    s = sol.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]])
    print(s)
    s = sol.removeStones([[0,0],[0,1],[1,1],[1,2],[2,2], [100,100], [100,101]])
    print(s)

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