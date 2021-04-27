from typing import List
import collections
import queue
import bisect

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        ascend = True
        i = 0
        n = len(nums)
        if n < 2:
            return n
        # 首先考察起始的单调性
        prediff = nums[1] - nums[0]
        ret = 1 if prediff == 0 else 2
        for i in range(2, n):
            diff = nums[i] - nums[i-1]
            if (diff > 0 and prediff <= 0) or (diff < 0 and prediff >= 0):
                ret += 1
                prediff = diff        

        return ret


if __name__ == "__main__":
    sol = Solution()
    s = sol.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])
    print(s)
    s = sol.wiggleMaxLength([1,7,4,9,2,5])
    print(s)
    s = sol.wiggleMaxLength([1,2,3,4,5,6,7,8,9])
    print(s)
    s = sol.wiggleMaxLength([1,3,2,5,4])
    print(s)
    s = sol.wiggleMaxLength([0,0])
    print(s)
