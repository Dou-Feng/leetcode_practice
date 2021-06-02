from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect

## 不带权值的并查集
class Solution:
    def minimumTimeRequired2(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        tot = [10**9 for _ in range(1 << n)]
        tot[0] = 0
        for mask in range(1<<n):
            for i in range(n):
                if mask & (0x01 << i):
                    tot[mask] = min(tot[mask], tot[mask ^ (0x01 << i)] + jobs[i])
        # print(tot)
        dp = [[10**9] * (1 << n) for _ in range(k+1)]
        for i in range(k+1):
            dp[i][0] = 0
        for i in range(1, k+1):
            for mask in range(1 << n):
                sub = mask
                while sub:
                    dp[i][mask] = min(dp[i][mask], max(dp[i-1][mask ^ sub], tot[sub]))
                    ## 子集枚举
                    sub = (sub - 1) & mask
        # print(dp)
        return dp[k][(1 << n) - 1]

    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        tot = [10**9 for _ in range(1 << n)]
        tot[0] = 0
        for mask in range(1<<n):
            for i in range(n):
                if mask & (0x01 << i):
                    tot[mask] = min(tot[mask], tot[mask ^ (0x01 << i)] + jobs[i])
        # print(tot)

        def can(mid):
            dp = [10 ** 9] * (1 << n)
            dp[0] = 0
            for mask in range(1 << n):
                sub = mask
                while sub:
                    if tot[sub] <= mid:
                        dp[mask] = min(dp[mask], dp[mask ^ sub]+1)
                    sub = (sub - 1) & mask

            return dp[(1 << n) - 1] <= k

        l = max(jobs)
        r = sum(jobs)
        while l < r:
            mid = (l + r) // 2
            if can(mid):
                r = mid
            else:
                l = mid+1
        return r



if __name__ == '__main__':
    sol = Solution()
    s = sol.minimumTimeRequired(jobs = [3,2,3], k = 3)
    print(s)
    s = sol.minimumTimeRequired(jobs = [1,2,4,7,8], k = 2)
    print(s)
