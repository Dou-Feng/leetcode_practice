from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect

class Solution:
    def partition(self, nums, begin, end):
        pivot = nums[begin]
        i, j = begin+1, end
        while i < j:
            while i < j and nums[i] > pivot:
                i += 1
            while i < j and nums[j] <= pivot:
                j -= 1
            t = nums[i]
            nums[i] = nums[j]
            nums[j] = t
        nums[begin] = nums[i-1]
        nums[i-1] = pivot
        return i-1

    def quicksort(self, nums, begin, end):
        if begin >= end:
            return begin
        mid = self.partition(nums, begin, end)
        # print(mid)
        self.quicksort(nums, begin, mid-1)
        self.quicksort(nums, mid+1, end)
        return len(nums) // 2

    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mid = self.quicksort(nums, 0, len(nums)-1)
        print(nums, mid)
        nums[1::2], nums[0::2] = nums[:mid], nums[mid:]
        return nums
        
        


if __name__ == '__main__':
    sol = Solution()
    s = sol.wiggleSort([1,5,1,1,6,4])
    print(s)
    s = sol.wiggleSort([2,1])
    print(s)