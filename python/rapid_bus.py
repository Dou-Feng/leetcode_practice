from typing import List
from functools import lru_cache

class Solution:
    def busRapidTransit(self, target: int, inc: int, dec: int, jump: List[int], cost: List[int]) -> int:
        n = len(jump)
        MOD = 10**9 + 7
        @lru_cache(None)
        def dfs(target):
            if target <= 0:
                return 0
            elif target == 1:
                return inc

            ans = inc * target

            # 最后一步采用公交出行
            for i in range(n):
                pre = target // jump[i]
                step = target % jump[i]

                if step:
                    price = (min(dfs(pre) + step * inc, dfs(pre+1) + (jump[i] - step) * dec) + cost[i])
                else:
                    price = (dfs(pre) + cost[i])

                if price < ans:
                    # print("target:", target, "take bus", i, "price is", price)
                    ans = price

            return ans

        return dfs(target) % MOD

sol = Solution()
print(sol.busRapidTransit(31, 5, 3, [6], [10]))
print(sol.busRapidTransit(611, 4, 5, [3,6,8,11,5,10,4],[4,7,6,3,7,6,4]))


