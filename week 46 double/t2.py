from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy


class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:

        # KMP match
        def match(src, pat):
            next = [0] * (len(pat) + 1)
            next[0] = -1
            i, j = 0, 1
            while j < len(pat):
                if i == -1 or pat[i] == pat[j]:
                    i += 1
                    j += 1
                    next[j] = i
                else:
                    i = next[i]

            i, j = 0, 0
            while i < len(src):
                if j == -1 or src[i] == pat[j]:
                    i += 1
                    j += 1
                if j == len(pat):
                    return i
                elif i < len(src) and src[i] != pat[j]:
                    j = next[j]

            return -1

        for item in groups:
            i = match(nums, item)
            # print(item, i)
            if i == -1:
                return False
            nums = nums[i:]

        return True



if __name__ == '__main__':
    sol = Solution()
    s = sol.canChoose(groups = [[1,-1,-1],[3,-2,0]], nums = [1,-1,0,1,-1,-1,3,-2,0])
    print(s)
    s = sol.canChoose(groups = [[10,-2],[1,2,3,4]], nums = [1,2,3,4,10,-2])
    print(s)
    s = sol.canChoose(groups = [[1,2,3],[3,4]], nums = [7,7,1,2,3,4,7,7])
    print(s)