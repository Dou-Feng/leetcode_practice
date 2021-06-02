from typing import List
import collections
import math
from functools import lru_cache
import queue
import bisect
import heapq
import copy

class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        pre = [0]
        for e in A:
            pre.append(pre[-1] + e)
        
        n = len(A)
        dp =  [[0] * (K+1) for _ in range(n+1)]
        for i in range(K+1):
            dp[i][i] = pre[i]
        for i in range(1, n+1):
            dp[i][1] = pre[i] / i
        for i in range(1, n+1):
            for j in range(2, min(i, K) + 1):
                for k in range(1, i-j+2):
                    # print(i, j, k, dp[i][j])
                    dp[i][j] = max(dp[i][j], dp[i-k][j-1] + (pre[i] - pre[i-k]) / k)

        
        # print(dp)
        return dp[n][K]

if __name__ == '__main__':
    sol = Solution()
    s = sol.largestSumOfAverages([1,2,3,4,5,6,7], 4)
    print(s)