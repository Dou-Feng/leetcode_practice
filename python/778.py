from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        left, right = max(grid[0][0], grid[n-1][n-1]), n*n - 1

        while left < right:
            mid = (left + right) // 2            
            uf = UF(n*n)
            for i in range(n):
                for j in range(n):
                    # up connect
                    if i > 0 and grid[i-1][j] <= mid and grid[i][j] <= mid:
                        uf.union((i-1)*n+j, i*n+j)
                    if j > 0 and grid[i][j-1] <= mid and grid[i][j] <= mid:
                        uf.union(i*n+j-1, i*n+j)

            if uf.connected(0, n*n-1):
                right = mid
            else:
                left = mid+1

        return right




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

    def connected(self, x, y):
        return self.find(x) == self.find(y)

if __name__ == '__main__':
    sol = Solution()
    s = sol.swimInWater([[0,2],[1,3]])
    print(s)
    s = sol.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]])
    print(s)