from typing import List
import collections
import math
from functools import lru_cache
from functools import cache
import queue
import bisect
import heapq
import copy


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        palin = [[False] * n for _ in range(n)]
        for j in range(n):
            palin[j][j] = True
            for i in range(j-1, -1, -1):
                if s[i] == s[j] and (i+1 == j or palin[i+1][j-1]):
                    palin[i][j] = True 

        # print(palin)
        dp = [10**9 for _ in range(n+1)]
        dp[0] = 0
        for i in range(n):
            for j in range(i+1):
                if palin[j][i]:
                    dp[i+1] = min(dp[i+1], dp[j] + 1)

        return dp[n] - 1

if __name__ == '__main__':
    sol = Solution()
    s = sol.minCut("aab")
    print(s)
    s = sol.minCut("a")
    print(s)
    s = sol.minCut("ab")
    print(s)
    s = sol.minCut("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp")
    print(s)