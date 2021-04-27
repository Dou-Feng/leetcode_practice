from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        # binary search
        left, right = 0, 10**6
        while left < right:
            mid = (right +left) // 2
            q = queue.deque([(0,0)])
            seen = {(0, 0)}
            while q:
                x, y = q.popleft()
                for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny)not in seen and abs(heights[x][y] - heights[nx][ny]) <= mid:
                        seen.add((nx, ny))
                        q.append((nx, ny))
            if (m-1, n-1) in seen:
                right = mid
            else:
                left = mid+1

        return right


if __name__ == '__main__':
    sol = Solution()
    s = sol.minimumEffortPath(heights = [[1,2,2],[3,8,2],[5,3,5]])
    print(s)
    s = sol.minimumEffortPath(heights = [[1,2,3],[3,8,4],[5,3,5]])
    print(s)
    s = sol.minimumEffortPath(heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]])
    print(s)