from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i, rightmost = 0, 0
        while i < n-1:
            if i <= rightmost and nums[i]+i > rightmost:
                rightmost = nums[i] + i
            i += 1

        return rightmost >= i



if __name__ == '__main__':
    sol = Solution()
    s = sol.canJump([2,3,1,1,4])
    print(s)
    s = sol.canJump([3,2,99,0,4])
    print(s)
    s = sol.canJump([1,0,2,0,4])
    print(s)
    s = sol.canJump([3,0,0,0])
    print(s)