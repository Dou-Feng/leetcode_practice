from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost * 4 <= runningCost:
            return -1
        minTime, maxProfit = 0, 0 
        time, profit = 0, 0
        for i, e in enumerate(customers):
            profit += min(4, e) * boardingCost - runningCost
            time += 1
            if profit > maxProfit:
                minTime = time
                maxProfit = profit
            if e > 4 and i + 1 < len(customers):
                customers[i+1] += e - 4

        customers[-1] -= min(4, customers[-1])
        minTime += customers[-1] // 4
        customers[-1] %= 4
        if customers[-1] * boardingCost - runningCost > 0:
            minTime += 1

        return minTime if maxProfit > 0 else -1


if __name__ == '__main__':
    sol = Solution()
    s = sol.minOperationsMaxProfit(customers = [8,3], boardingCost = 5, runningCost = 6)
    print(s)
    s = sol.minOperationsMaxProfit(customers = [10,9,6], boardingCost = 6, runningCost = 4)
    print(s)
    s = sol.minOperationsMaxProfit(customers = [10,10,6,4,7], boardingCost = 3, runningCost = 8)
    print(s)
