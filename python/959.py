from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        uf = UF(4*(n*n))
        for i in range(n):
            for j in range(n):
                index = 4 * (n*i + j)
                if grid[i][j] == '/':
                    uf.union(index, index+3)
                    uf.union(index+1, index+2)
                elif grid[i][j] == '\\':
                    uf.union(index, index+1)
                    uf.union(index+2, index+3)
                else:
                    uf.union(index, index+1)
                    uf.union(index+1, index+2)
                    uf.union(index+2, index+3)
                    # print("Spaces", uf.num)

                # inter-block connection
                if i < n - 1:
                    uf.union(index+2, 4*((i+1)*n + j))
                if j < n - 1:
                    uf.union(index+1, 4*(i*n + j+1)+3)
                # print(i, j, uf.num)

        return uf.num

        

class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.weight = [0] * n
        self.num = n

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
        self.num -= 1
        return True

    def isConnected(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty:
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    s = sol.regionsBySlashes([
  " /",
  "/ "
])
    print(s)