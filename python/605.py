from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n <= 1 or n == 0:
                return True
            else:
                return False

        if not flowerbed[0] and not flowerbed[1]:
            flowerbed[0] = 1
            n -= 1

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i]:
                continue
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        m = len(flowerbed)
        if m > 2 and flowerbed[m-1] == 0 and flowerbed[m-2] == 0:
            n -= 1

        return not n

if __name__ == '__main__':
    sol = Solution()
    s = sol.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1)
    print(s)
    s = sol.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2)
    print(s)
    s = sol.canPlaceFlowers(flowerbed = [1], n = 1)
    print(s)
    s = sol.canPlaceFlowers(flowerbed = [0], n = 1)
    print(s)
    s = sol.canPlaceFlowers(flowerbed = [0], n = 0)
    print(s)
    s = sol.canPlaceFlowers(flowerbed = [0], n = 0)
    print(s)