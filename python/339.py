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
        self.weight = [1.0] * n

    def find(self, x):
        if x != self.parent[x]:
            origin = self.parent[x]
            self.parent[x] = self.find(self.parent[x])
            self.weight[x] *= self.weight[origin]
        return self.parent[x]

    def union(self, x, y, value):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return False

        self.parent[rootx] = rooty
        self.weight[rootx] = self.weight[y] * value / self.weight[x]
        return True

    def isConnected(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty:
            return self.weight[x] / self.weight[y]
        return -1.0

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        id = 0
        hashmap = dict()
        uf = UF(41)
        for i, elem in enumerate(equations):
            v1, v2 = elem[0], elem[1]
            if v1 not in hashmap:
                hashmap[v1] = id
                id += 1
            if v2 not in hashmap:
                hashmap[v2] = id
                id += 1

            uf.union(hashmap[v1], hashmap[v2], values[i])

        ret = []
        for qu in queries:
            if qu[0] not in hashmap or qu[1] not in hashmap:
                ret.append(-1.0)
                continue
            n1, n2 = hashmap[qu[0]], hashmap[qu[1]]
            ret.append(uf.isConnected(n1, n2))

        return ret


if __name__ == '__main__':
    sol = Solution()
    s = sol.calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
    print(s)
    s = sol.calcEquation(equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]])
    print(s)