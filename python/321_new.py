from typing import List
import collections
import queue
import bisect
from functools import lru_cache

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def getsub(nums, n):
            stack = []
            t = len(nums) - n
            for e in nums:
                while t and stack and e > stack[-1]:
                    stack.pop()
                    t -= 1
                stack.append(e)
            return stack[:n]

        def merge(A, B):
            ret = []
            while A or B:
                bigger = A if A > B else B
                ret.append(bigger.pop(0))

            return ret

        return max([merge(getsub(nums1, i), getsub(nums2, k-i) ) for i in range(k+1) if i <= len(nums1) and (k-i) <= len(nums2)])
        


if __name__ == "__main__":
    sol = Solution()
    s = sol.maxNumber([2,5,6,4,4,0], [7,3,8,0,6,5,7,6,2], 15)
    print(s)
    s = sol.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5)
    print(s)
    s = sol.maxNumber([6, 7], [6, 0, 4], 5)
    print(s)
    s = sol.maxNumber([8,6,9], [1,7,5], 3)
    print(s)



