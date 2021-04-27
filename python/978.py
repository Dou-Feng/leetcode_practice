from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return len(arr)

        res = 0
        i, j, n = 0, 1, len(arr)
        while j < n - 1:
            if (arr[j-1] < arr[j] and arr[j] > arr[j+1]) or (arr[j-1] > arr[j] and arr[j] < arr[j+1]):
                # print("j", j)
                j += 1
            else:
                if not (j == i + 1 and arr[j] == arr[i]):
                    res = max(res, j - i + 1)
                i = j
                # print("i = j", i)
                j += 1
        if arr[-1] == arr[-2]:
            i += 1
        # print(i, j)
        res = max(res, j - i + 1)
        return res

if __name__ == '__main__':
    sol = Solution()
    s = sol.maxTurbulenceSize([9,4,2,10,7,8,8,1,9])
    print(s)
    s = sol.maxTurbulenceSize([9])
    print(s)
    s = sol.maxTurbulenceSize([9,8,7,7,6,7])
    print(s)
    s = sol.maxTurbulenceSize([9,9])
    print(s)
    s = sol.maxTurbulenceSize([9,8])
    print(s)
    s = sol.maxTurbulenceSize([100,100,100])
    print(s)
