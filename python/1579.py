from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UF(n+1)
        bob = UF(n+1)

        edges.sort(key = lambda e : -e[0])

        ret = 0
        for e in edges:
            # print(e)
            if e[0] == 3:
                a = alice.union(e[1], e[2])
                b = bob.union(e[1], e[2])
                if not a and not b:
                    ret += 1
            elif e[0] == 2:
                if not bob.union(e[1], e[2]):
                    ret += 1
            else:
                if not alice.union(e[1], e[2]):
                    ret += 1

        return ret if alice.node == n and bob.node == n else -1

## 不带权值的并查集
class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.node = 1

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return False
        self.parent[rootx] = rooty
        self.node += 1
        return True

if __name__ == '__main__':
    sol = Solution()
    s = sol.maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]])
    print(s)
    s = sol.maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]])
    print(s)
    s = sol.maxNumEdgesToRemove(n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]])
    print(s)