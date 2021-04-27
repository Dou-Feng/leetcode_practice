from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        pre = [0]
        arr.sort()
        # print(arr)
        for a in arr:
            pre.append(pre[-1] + a)
        # print(pre)
        arr = [0] + arr 
        i, n = 0, len(arr) - 1
        ans = arr[-1]
        ans_i = n
        while i < n and pre[i] < target:
            # print("max and min", i, min, max)
            res = (target - pre[i]) / (n-i)
            # print(pre[i], "Rough res", res)
            res = int(res) + 1 if res - int(res) > 0.5 else int(res)
            # print("Res", res, "min", min, "max", max)
            if arr[i] <= res <= arr[i+1]-1:
                return res
            i += 1  

        return ans


if __name__ == '__main__':
    sol = Solution()
    s = sol.findBestValue(arr = [4,9,3], target = 10)
    print(s)
    s = sol.findBestValue(arr = [2,3,5], target = 10)
    print(s)
    s = sol.findBestValue([1,2,23,24,34,36], 110)
    print(s)