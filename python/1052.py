from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        ret = 0
        base = 0
        i = 0
        extra = 0
        window = 0
        for j, e in enumerate(customers):
            if grumpy[j]:
                window += customers[j]
            else:
                base += customers[j]
            if j - i >= X:
                window -= customers[i] * grumpy[i]
                i += 1
            extra = max(window, extra)
        return base + extra

if __name__ == '__main__':
    sol = Solution()
    s = sol.maxSatisfied(customers = [2,4,1,4,1], grumpy = [1,0,1,0,1], X = 2)
    print(s)