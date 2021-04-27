import collections
from typing import List
from functools import lru_cache

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        m, n = len(ring), len(key)

        lelist = collections.defaultdict(list)
        for i in range(m):
            lelist[ring[i]].append(i)

        # ans = 10**9 + 7
        @lru_cache(None)
        def dfs(cur, ki):
            # nonlocal ans
            if ki == n:
                # ans = min(ans, step)
                return 0

            # 有很多种选择
            ans = 10**9 + 7
            for loc in lelist[key[ki]]:
                add = min(abs(cur - loc), abs(m - cur + loc), abs(m - loc + cur)) + 1
                ans = min(ans, dfs(loc, ki+1) + add)

            return ans

        return dfs(0, 0)

    # 解法二，利用动态规划求解
    def findRotateSteps(self, ring: str, key: str) -> int:
        m, n = len(ring), len(key)
        lelist = collections.defaultdict(list)
        for i in range(m):
            lelist[ring[i]].append(i)

        dp = [[10**9+7] * (105) for _ in range(105) ]

        for i in range(n):
            if i == 0:
                for j, loc in enumerate(lelist[key[i]]):
                    cur = 0
                    dp[i][j] = min(abs(cur - loc), abs(m - cur + loc), abs(m - loc + cur)) + 1
            else:
                for j, cur in enumerate(lelist[key[i]]):
                    for k, loc in enumerate(lelist[key[i-1]]):
                        dis = min(abs(cur - loc), abs(m - cur + loc), abs(m - loc + cur)) + 1
                        dp[i][j] = min(dp[i][j], dis + dp[i-1][k])


        return min(dp[n-1])

sol = Solution()
print(sol.findRotateSteps("accccdccccbaaaaaaaaaaaeffffffffffcaccccdccccbaaaaaaaaaaaeffffffffffcghhhhhhhhjjjjjjsskkkkssssss", "acffffffffffffffffffffffffffffffaaccccckgj"))
# print(sol.findRotateSteps2("accccdccccbaaaaaaaaaaaeffffffffffc", "acf"))

print(sol.findRotateSteps2("accccdccccbaaaaaaaaaaaeffffffffffcaccccdccccbaaaaaaaaaaaeffffffffffcghhhhhhhhjjjjjjsskkkkssssss", "acffffffffffffffffffffffffffffffaaccccckgj"))

