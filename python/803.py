from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        # 深拷贝
        grid_copy = copy.deepcopy(grid)

        # 把hits砖块设置为0
        for h in hits:
            grid_copy[h[0]][h[1]] = 0

        # 用并查集把屋顶和第一排的砖块连接起来
        # 用编号size表示屋顶
        m, n = len(grid), len(grid[0])
        size = m * n
        uf = UF(size + 1)
        for i in range(n):
            if grid_copy[0][i]:
                uf.union(i, size)

        # print(uf.getSize(size))
        # 然后把其他有关的砖块添加到并查集中
        for i in range(1, m):
            for j in range(n):
                if grid_copy[i][j] == 0:
                    continue

                if j > 0 and grid_copy[i][j-1] == 1:
                    uf.union(i * n + j-1, i*n + j)

                if grid_copy[i-1][j] == 1:
                    uf.union((i-1)*n + j, i*n + j)
                # print(uf.getSize(size))

        # 然后倒序添加hit掉的砖块
        # origin = uf.getSize(size)
        print(origin)
        dx = 0, 0, -1, 1
        dy = 1, -1, 0, 0
        ret = []
        for i in range(len(hits)-1, -1, -1):
            x, y = hits[i][0], hits[i][1]

            # 如果本来该位置就不存在砖块，那么不用添加
            if grid[x][y] == 0:
                ret.append(0)
                continue

            # 如果该砖块与顶部相连
            if x == 0:
                uf.union(size, x*n + y)

            for j in range(4):
                nx, ny = x + dx[j], y + dy[j]
                if 0 <= nx < m and 0 <= ny < n and grid_copy[nx][ny]:
                    uf.union(x*n+y, nx*n+ny)

            curr = uf.getSize(size)
            ret.append(curr - origin - 1 if  curr > origin else 0)
            origin = curr
            grid_copy[x][y] = 1

        return ret[::-1]


## 带有连通分量大小的并查集
class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.n = n

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

if __name__ == '__main__':
    sol = Solution()
    # s = sol.hitBricks(grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]])
    # print(s)
    # s = sol.hitBricks(grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]])
    # print(s)
    # s = sol.hitBricks(grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,3], [0, 0]])
    # print(s)
    # s = sol.hitBricks([[1],[1],[1],[1],[1]], [[3,0],[4,0],[1,0],[2,0],[0,0]])
    # print(s)
    s = sol.hitBricks([[1,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,1]], [[2,2]])
    print(s)