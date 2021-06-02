from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        height = isWater

        que = queue.deque()
        valid = [[True] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if height[i][j] == 1:
                    que.append((i, j))
                    height[i][j] = 0
                    valid[i][j] = False
                else:
                    height[i][j] = 1
        dx, dy = (1, -1, 0, 0), (0, 0, -1, 1)
        while que:
            x, y = que.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and valid[nx][ny]:
                    height[nx][ny] = height[x][y] + 1
                    que.append((nx, ny))
                    valid[nx][ny] = False

        return height


if __name__ == '__main__':
    sol = Solution()
    s = sol.highestPeak(isWater = [[0,0,1],[1,0,0],[0,0,0]])
    print(s)