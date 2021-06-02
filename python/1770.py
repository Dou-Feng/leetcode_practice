from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)
        dp = [[0] * (m+1) for _ in  range(m+1)]
        ret = 0
        for k in range(1, m+1):
            for i in range(0, k+1):
                j = k - i
                if i == 0:
                    dp[i][j] = dp[i][j-1] + nums[-j] * multipliers[k-1]
                elif j == 0:
                     dp[i][j] = dp[i-1][j] + nums[i-1] * multipliers[k-1]
                else:
                    dp[i][j] = max( dp[i-1][j] + nums[i-1] * multipliers[k-1], \
                                dp[i][j-1] + nums[-j] * multipliers[k-1])
                # print(i, j, k, dp[i][j])
                if k == m:
                    ret = max(ret, dp[i][j])
        return ret


if __name__ == '__main__':
    sol = Solution()
    s = sol.maximumScore(nums = [1,2,3], multipliers = [3,2,1])
    print(s)
    s = sol.maximumScore(nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6])
    print(s)