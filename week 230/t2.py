from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:

        combination = []
        toppingCosts = toppingCosts + toppingCosts
        def comb(i, sum):
            nonlocal combination
            if i == len(toppingCosts):
                combination.append(sum)
                return

            comb(i+1, sum)
            comb(i+1, sum+toppingCosts[i])

        comb(0, 0)
        combination.sort()
        # print(combination)
        ret = 10**9 + 7
        baseCosts.sort()
        for base in baseCosts:
            if base >= target:
                if abs(ret - target) > abs(base - target):
                    ret = base
                continue
            rest = target - base
            i = bisect.bisect_left(combination, rest)
            # print("i", i, rest, combination[i])
            # 如果在最右端说明只用对比最后一个元素
            ans = 10**9 + 7
            if i == len(combination):
                ans = combination[i-1] + base

            elif combination[i] == rest:
                return target
            else:
                if abs(rest - combination[i-1]) <= abs(rest - combination[i]):
                    ans = combination[i-1] + base
                else:
                    ans = combination[i] + base

            if abs(ret - target) > abs(ans - target) or (abs(ret - target) == abs(ans - target) and ret > ans):
                ret = ans


        return ret




if __name__ == '__main__':
    sol = Solution()
    s = sol.closestCost(baseCosts = [7,9], toppingCosts = [1,2,3,4,5], target = 30)
    print(s)