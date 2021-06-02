from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums = nums + nums
        n, stack = len(nums) // 2, []
        ret = [-1] * n
        for i, e in enumerate(nums):
            if stack and i - stack[-1] >= n:
                break
            while stack and nums[stack[-1]] < e:
                j = stack.pop()
                ret[j] = e
            if i < n:
                stack.append(i)

        return ret



if __name__ == '__main__':
    sol = Solution()
    s = sol.nextGreaterElements([3,2,1,5,23,3,2,1])
    print(s)
    s = sol.nextGreaterElements([8,9,4,5,2])
    print(s)
    s = sol.nextGreaterElements([6,1,2,3,4,7])
    print(s)
