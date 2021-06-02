from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq

class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.v = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)

        if rooty == rootx:
            return False

        if self.v[rootx] > self.v[rooty]:
            t = rootx
            rootx =  rooty
            rooty = t
        self.parent[rooty] = rootx
        self.v[rooty] += self.v[rootx]
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges) + 1
        uf = UF(N)
        for edge in edges:
            if not uf.union(edge[0], edge[1]):
                return [edge[0], edge[1]] if edge[0] < edge[1] else [edge[1], edge[0]]



if __name__ == '__main__':
    sol = Solution()
    s = sol.findRedundantConnection([[1,2], [1,3], [2,3]])
    print(s)
    s = sol.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]])
    print(s)