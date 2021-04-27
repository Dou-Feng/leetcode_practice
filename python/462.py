from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        mid = nums[len(nums) // 2]
        return sum([abs(mid - nums[i]) for i in range(len(nums))])


if __name__ == '__main__':
    sol = Solution()
    s = sol.minMoves2([1,2,3])
    print(s)
    s = sol.minMoves2([1,1,4,5,6])
    print(s)
    s = sol.minMoves2([1])
    print(s)
    s = sol.minMoves2([])
    print(s)