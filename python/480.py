from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        odd = k % 2
        wind = sorted(nums[:k])
        ret = []
        for i in range(len(nums)-k):
            ret.append( wind[k//2] if odd else (wind[(k-1)//2] + wind[k//2]) / 2 )

            index = bisect.bisect_left(wind, nums[i])
            wind = wind[:index] + wind[index+1:]
            bisect.insort(wind, nums[i+k])
        ret.append( wind[k//2] if odd else (wind[(k-1)//2] + wind[k//2]) / 2 )
        return ret


if __name__ == '__main__':
    sol = Solution()
    s = sol.medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
    print(s)