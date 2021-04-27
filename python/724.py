from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = 0
        s = sum(nums)
        for i, n in enumerate(nums):
            if 2 * pre + n == s:
                return i
            pre += n

        return -1

if __name__ == '__main__':
    sol = Solution()
    s = sol.pivotIndex(nums = [1, 7, 3, 6, 5, 6])
    print(s)
    s = sol.pivotIndex(nums = [0, 0, 0, 0, 1])
    print(s)
    s = sol.pivotIndex(nums = [2, 1, -1])
    print(s)