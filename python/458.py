from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy
from math import ceil
from math import log

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        t = minutesToTest // minutesToDie
        def poor(b, t):
            n = ceil(log(b, 2))
            if t == 1:
                return n
            for x in range(1, 100000):
                if x >= b:
                    return x
                overlap = ceil(n / x)
                # print(b, t, n)
                y = poor(overlap, t-1)
                if x >= y + 1:
                    print("fit", b, t, x)
                    return x
            return 10**9
        
        return poor(buckets, t)


if __name__ == '__main__':
    sol = Solution()
    s = sol.poorPigs(buckets = 1000, minutesToDie = 15, minutesToTest = 60)
    print(s)
