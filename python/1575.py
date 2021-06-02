from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        @lru_cache(None)
        def dp(i, j):
            if j < 0:
                return 0
            ret = 0
            for k in range(n):
                if k == i:
                    continue
                ret += dp(k, j - abs(locations[i] - locations[k]))
            if i == finish:
                ret += 1
            return ret % (10**9 + 7)

        return dp(start, fuel)

if __name__ == '__main__':
    sol = Solution()
    s = sol.countRoutes(locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5)
    print(s)
    s = sol.countRoutes(locations = [4,3,1], start = 1, finish = 0, fuel = 6)
    print(s)